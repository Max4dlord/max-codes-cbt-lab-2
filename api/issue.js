// ---------------------------------------------------------------------------
// POST /api/issue   { deviceId }  ->  { ok, token, exp }
//
// Grants a device-bound 7-day session — but ONLY on evidence the server itself
// recorded. It no longer believes anything the browser says about progress.
//
// How a step is proven
// ---------------------------------------------------------------------------
// Every required step must present a valid "visit ticket" cookie, set by
// /api/go when the server actually performed the redirect. Each ticket is an
// HttpOnly cookie signed with GATE_SECRET, so page JavaScript can neither read
// nor forge one, and a curl request that skips the UI simply has no cookies.
//
// Two server-side timestamps are compared:
//   * ticket time  — when the server sent them to WhatsApp/LinkedIn
//   * now          — when they came back and asked for access
// The gap must be at least MIN_DWELL_MS. Both readings come from server clocks,
// so the browser cannot shorten the wait.
//
// What this still cannot do (stated plainly, not papered over)
// ---------------------------------------------------------------------------
// No public API can confirm that someone pressed "Follow" once WhatsApp or
// LinkedIn has them. What is now provably true is that this device really was
// sent to the destination and really did spend time there. That is a genuine
// server-verified click-through, not a self-reported checkbox.
//
// Stateless: signed cookies only. No database, no KV. Free Hobby tier.
// ---------------------------------------------------------------------------

import { signToken, cleanDevice, json, readBody, configError } from './_lib.js'
import { REQUIRED_STEPS, MIN_DWELL_MS } from './_steps.js'
import { parseCookies, readTicket } from './go.js'

export default async function handler(req, res) {
  if (req.method !== 'POST') return json(res, 405, { ok: false, error: 'Method not allowed' })

  if (configError()) {
    return json(res, 503, {
      ok: false,
      error: 'Access system is not configured yet. Please try again shortly.',
    })
  }

  const body = await readBody(req)
  const deviceId = cleanDevice(body.deviceId)
  if (!deviceId) return json(res, 400, { ok: false, error: 'Could not identify this device.' })

  const cookies = parseCookies(req.headers.cookie)

  for (const stepId of REQUIRED_STEPS) {
    const ts = readTicket(cookies, stepId, deviceId)

    // No server-recorded visit: the step was never actually opened on this
    // device (or someone tried to skip the UI altogether).
    if (!ts) {
      return json(res, 403, {
        ok: false,
        error: 'Please tap the button for each step — we could not confirm that one yet.',
        missing: stepId,
      })
    }

    // Opened, but bounced straight back.
    if (Date.now() - ts < MIN_DWELL_MS) {
      return json(res, 429, {
        ok: false,
        error: 'That was a little too quick — please finish the step, then come back.',
        missing: stepId,
        retryInMs: MIN_DWELL_MS - (Date.now() - ts),
      })
    }
  }

  const { token, exp } = signToken(deviceId)
  return json(res, 200, { ok: true, token, exp })
}
