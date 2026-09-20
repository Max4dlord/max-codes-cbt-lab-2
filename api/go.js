// ---------------------------------------------------------------------------
// GET /api/go?step=<id>&d=<deviceId>   ->  302 redirect to the real destination
//
// THIS is what makes a step un-fakeable-by-checkbox. The visitor does not open
// WhatsApp/LinkedIn directly; they open OUR endpoint, and the server redirects
// them. That means the server — not the browser — records that the click
// genuinely happened, and when.
//
// It sets a signed, HttpOnly "visit ticket" cookie. HttpOnly matters: page
// JavaScript cannot read or forge it, and the signature is an HMAC of
// (step, device, timestamp) using GATE_SECRET, which never leaves the server.
//
// /api/issue later re-reads those cookies and checks the server-recorded
// timestamps. A visitor who only ticks the boxes has no cookies, so no ticket,
// so no access — no matter what their browser claims.
// ---------------------------------------------------------------------------

import crypto from 'node:crypto'
import { SECRET, hmac, b64url, cleanDevice, configError } from './_lib.js'
import { STEPS, TICKET_TTL_MS, cookieName } from './_steps.js'

export function signTicket(stepId, deviceId, ts) {
  return b64url(hmac(`visit|v1|${stepId}|${deviceId}|${ts}`)).slice(0, 24)
}

/** Parse "a=1; b=2" into an object. */
export function parseCookies(header) {
  const out = {}
  for (const part of String(header || '').split(';')) {
    const i = part.indexOf('=')
    if (i < 0) continue
    out[part.slice(0, i).trim()] = decodeURIComponent(part.slice(i + 1).trim())
  }
  return out
}

/** Returns the server-recorded visit timestamp, or null if absent/forged. */
export function readTicket(cookies, stepId, deviceId) {
  const raw = cookies[cookieName(stepId)]
  if (!raw) return null
  const [tsStr, sig] = String(raw).split('.')
  const ts = Number(tsStr)
  if (!ts || !sig) return null
  const expect = signTicket(stepId, deviceId, ts)
  const a = Buffer.from(sig)
  const b = Buffer.from(expect)
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return null
  if (Date.now() - ts > TICKET_TTL_MS) return null
  return ts
}

export default async function handler(req, res) {
  if (configError()) return res.status(503).send('Access system not configured.')

  const url = new URL(req.url, `https://${req.headers.host}`)
  const stepId = url.searchParams.get('step')
  const deviceId = cleanDevice(url.searchParams.get('d'))
  const step = STEPS[stepId]

  // Never redirect to a caller-supplied URL — only to a known step.
  if (!step) return res.status(400).send('Unknown step.')
  if (!deviceId) return res.status(400).send('Missing device.')

  const ts = Date.now()
  const value = `${ts}.${signTicket(stepId, deviceId, ts)}`

  res.setHeader('Set-Cookie', [
    `${cookieName(stepId)}=${encodeURIComponent(value)}`,
    'Path=/',
    `Max-Age=${Math.floor(TICKET_TTL_MS / 1000)}`,
    'HttpOnly',            // page JS cannot read or forge it
    'Secure',
    'SameSite=Lax',        // still sent when they navigate back to us
  ].join('; '))

  res.setHeader('Cache-Control', 'no-store')
  res.writeHead(302, { Location: step.url })
  res.end()
}
