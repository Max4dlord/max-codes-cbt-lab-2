// ---------------------------------------------------------------------------
// Device identity + session token storage, and the API calls that use them.
//
// IMPORTANT DESIGN NOTE
// This file stores a token but it does NOT decide whether you are allowed in —
// /api/verify does, on the server. There is no "unlocked: true" flag to flip.
// The worst a tamperer can do locally is delete their own token.
//
// Test/study PROGRESS is stored under completely separate keys (progress.js)
// and is never touched by the gate. Access expiring never costs a student
// a single answer, score or resume point.
// ---------------------------------------------------------------------------

const DEV_KEY = 'cbt_device_v1'
const TOKEN_KEY = 'cbt_token_v1'
const STEPS_KEY = 'cbt_gate_steps_v1'

function randHex(bytes = 16) {
  try {
    const a = new Uint8Array(bytes)
    crypto.getRandomValues(a)
    return Array.from(a, (b) => b.toString(16).padStart(2, '0')).join('')
  } catch {
    return Math.random().toString(36).slice(2) + Date.now().toString(36)
  }
}

/** Stable random id for this browser/phone. Created once, reused forever. */
export function deviceId() {
  try {
    let id = localStorage.getItem(DEV_KEY)
    if (!id || !/^[A-Za-z0-9_-]{8,64}$/.test(id)) {
      id = randHex(12)
      localStorage.setItem(DEV_KEY, id)
    }
    return id
  } catch {
    return 'nostorage' + randHex(6)
  }
}

/** Short, readable form the student pastes into WhatsApp. */
export function deviceLabel() {
  const id = deviceId()
  return id.slice(0, 6).toUpperCase() + '-' + id.slice(6, 12).toUpperCase()
}

export function getToken() {
  try { return localStorage.getItem(TOKEN_KEY) } catch { return null }
}

export function setToken(t) {
  try { localStorage.setItem(TOKEN_KEY, t) } catch {}
}

export function clearToken() {
  try { localStorage.removeItem(TOKEN_KEY) } catch {}
}

async function post(url, body) {
  const r = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
  let data = {}
  try { data = await r.json() } catch {}
  return { status: r.status, data }
}

/** Ask the server whether the stored token is real and still alive. */
export async function verifyAccess() {
  const token = getToken()
  if (!token) return { ok: false, reason: 'missing' }
  try {
    const { data } = await post('/api/verify', { deviceId: deviceId(), token })
    if (!data.ok) clearToken()
    return data.ok ? { ok: true, exp: data.exp } : { ok: false, reason: data.reason }
  } catch {
    // Network down: fail CLOSED on purpose. Offline must not be a bypass.
    return { ok: false, reason: 'offline' }
  }
}

// ---------------------------------------------------------------------------
// Gate step progress.
//
// Tapping "save contact" or "open channel" navigates AWAY from the page (on
// phones WhatsApp/LinkedIn often replace the tab entirely). When the visitor
// comes back the React state is gone, so progress MUST live in localStorage or
// the gate appears to restart from scratch. Shape:
//   { [stepId]: { openedAt: ms, done: bool } }
// ---------------------------------------------------------------------------

export function loadSteps() {
  try {
    const raw = localStorage.getItem(STEPS_KEY)
    const v = raw ? JSON.parse(raw) : null
    return v && typeof v === 'object' ? v : {}
  } catch { return {} }
}

export function saveSteps(steps) {
  try { localStorage.setItem(STEPS_KEY, JSON.stringify(steps)) } catch {}
}

export function clearSteps() {
  try { localStorage.removeItem(STEPS_KEY) } catch {}
}

/**
 * Automated access: the server issues a device-bound 7-day session once the
 * required steps are complete. No code is typed and nothing is shared.
 */
export async function requestAccess(steps) {
  // Send only what the server needs: completion + how long they dwelled.
  const payload = {}
  for (const [id, v] of Object.entries(steps || {})) {
    payload[id] = {
      done: !!v.done,
      dwellMs: v.openedAt ? Math.max(0, Date.now() - v.openedAt) : 0,
    }
  }
  try {
    const { data } = await post('/api/issue', { deviceId: deviceId(), steps: payload })
    if (data.ok && data.token) { setToken(data.token); return { ok: true, exp: data.exp } }
    return { ok: false, error: data.error || 'Could not grant access just yet.' }
  } catch {
    return { ok: false, error: 'No internet connection. Connect and try again.' }
  }
}

/** Redeem a code (kept as a fallback / magic-link path). */
export async function redeemCode(code) {
  try {
    const { data } = await post('/api/unlock', { deviceId: deviceId(), code })
    if (data.ok && data.token) { setToken(data.token); return { ok: true, exp: data.exp } }
    return { ok: false, error: data.error || 'Could not verify that code.' }
  } catch {
    return { ok: false, error: 'No internet connection. Connect and try again.' }
  }
}

/** Human-readable time left, for the navbar badge. */
export function timeLeftLabel(exp) {
  if (!exp) return null
  const ms = exp - Date.now()
  if (ms <= 0) return 'expired'
  const d = Math.floor(ms / 86400000)
  const h = Math.floor((ms % 86400000) / 3600000)
  if (d > 0) return `${d}d ${h}h`
  const m = Math.floor((ms % 3600000) / 60000)
  return `${h}h ${m}m`
}
