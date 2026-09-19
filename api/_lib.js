// ---------------------------------------------------------------------------
// Shared crypto helpers for the access-gate API.
//
// WHY THIS EXISTS
// The old gate was 100% front-end, so the secret shipped inside the JS bundle
// and anyone with DevTools could read it, forge a code, or just flip a flag.
// These helpers run ONLY on Vercel's servers. GATE_SECRET never reaches the
// browser, so a code cannot be computed or forged client-side.
//
// Everything here is stateless HMAC — no database, no KV, no add-ons.
// That keeps the whole thing inside Vercel's free Hobby tier.
// ---------------------------------------------------------------------------

import crypto from 'node:crypto'

export const SECRET = process.env.GATE_SECRET || 'dev-only-insecure-secret-change-me'
export const ADMIN_KEY = process.env.ADMIN_KEY || 'dev-admin-key'

// How long one *code cycle* lasts. A code issued in week N works in week N
// (and week N-1 as grace, so a code sent late at night never dies on them).
export const CODE_PERIOD_MS = 7 * 24 * 3600 * 1000

// How long an unlock lasts once redeemed, from the moment of redemption.
export const SESSION_MS = 7 * 24 * 3600 * 1000

// Unambiguous alphabet — no 0/O, no 1/I/L. Students type these on phones.
const ALPHABET = '23456789ABCDEFGHJKMNPQRSTUVWXYZ'

export function hmac(data) {
  return crypto.createHmac('sha256', SECRET).update(data).digest()
}

export function b64url(buf) {
  return Buffer.from(buf).toString('base64')
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

export function fromB64url(str) {
  return Buffer.from(String(str).replace(/-/g, '+').replace(/_/g, '/'), 'base64')
}

/** Constant-time compare so nobody can time-attack the code check. */
export function safeEqual(a, b) {
  const A = Buffer.from(String(a))
  const B = Buffer.from(String(b))
  if (A.length !== B.length) return false
  return crypto.timingSafeEqual(A, B)
}

export function codeWindow(at = Date.now()) {
  return Math.floor(at / CODE_PERIOD_MS)
}

/**
 * The code for ONE specific device in ONE specific week.
 *
 * This is the anti-sharing core: the device id is inside the HMAC, so a code
 * generated for phone A is mathematically meaningless on phone B. Pasting it
 * in a group chat achieves nothing.
 */
export function codeFor(deviceId, w = codeWindow(), prefix = 'MAX-') {
  const mac = hmac(`code|v1|${deviceId}|${w}`)
  let out = ''
  for (let i = 0; i < 6; i++) out += ALPHABET[mac[i] % ALPHABET.length]
  return prefix + out
}

const norm = (s) => String(s || '').trim().toUpperCase().replace(/[\s-]+/g, '')

/** Accepts the current week's code and the previous week's (grace). */
export function isCodeValid(deviceId, input, prefix = 'MAX-') {
  const given = norm(input)
  if (!given) return false
  const w = codeWindow()
  for (const win of [w, w - 1]) {
    if (safeEqual(given, norm(codeFor(deviceId, win, prefix)))) return true
  }
  return false
}

/**
 * Signed session token:  base64url(payload) + "." + base64url(hmac)
 * Payload = { d: deviceId, exp: ms, iat: ms }
 * The browser can READ it but cannot MINT one — no secret, no valid signature.
 */
export function signToken(deviceId, ttl = SESSION_MS) {
  const payload = { d: deviceId, iat: Date.now(), exp: Date.now() + ttl }
  const body = b64url(JSON.stringify(payload))
  const sig = b64url(hmac(`tok|v1|${body}`))
  return { token: `${body}.${sig}`, exp: payload.exp }
}

export function verifyToken(token, deviceId) {
  if (!token || typeof token !== 'string') return { ok: false, reason: 'missing' }
  const [body, sig] = token.split('.')
  if (!body || !sig) return { ok: false, reason: 'malformed' }
  const expect = b64url(hmac(`tok|v1|${body}`))
  if (!safeEqual(sig, expect)) return { ok: false, reason: 'bad-signature' }
  let payload
  try { payload = JSON.parse(fromB64url(body).toString('utf8')) }
  catch { return { ok: false, reason: 'malformed' } }
  if (!payload.exp || Date.now() > payload.exp) return { ok: false, reason: 'expired' }
  if (deviceId && payload.d !== deviceId) return { ok: false, reason: 'wrong-device' }
  return { ok: true, payload }
}

/** Basic hygiene on the device id coming from the browser. */
export function cleanDevice(id) {
  const s = String(id || '').trim()
  if (!/^[A-Za-z0-9_-]{8,64}$/.test(s)) return null
  return s
}

export function json(res, status, obj) {
  res.setHeader('Content-Type', 'application/json')
  res.setHeader('Cache-Control', 'no-store')
  res.status(status).send(JSON.stringify(obj))
}

export async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body
  if (typeof req.body === 'string') { try { return JSON.parse(req.body) } catch { return {} } }
  const chunks = []
  for await (const c of req) chunks.push(c)
  if (!chunks.length) return {}
  try { return JSON.parse(Buffer.concat(chunks).toString('utf8')) } catch { return {} }
}
