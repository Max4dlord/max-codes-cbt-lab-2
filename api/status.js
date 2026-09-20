// ---------------------------------------------------------------------------
// POST /api/status   { deviceId }  ->  { ok, steps: { id: {visited, ready, waitMs} } }
//
// Lets the gate UI reflect what the SERVER actually recorded, rather than what
// the browser remembers. This is what allows the flow to survive a redirect,
// a reload, or even the tab being replaced: the evidence lives in HttpOnly
// cookies on our domain, so returning visitors are recognised instantly.
// ---------------------------------------------------------------------------

import { cleanDevice, json, readBody, configError } from './_lib.js'
import { STEPS, MIN_DWELL_MS } from './_steps.js'
import { parseCookies, readTicket } from './go.js'

export default async function handler(req, res) {
  if (req.method !== 'POST') return json(res, 405, { ok: false, error: 'Method not allowed' })
  if (configError()) return json(res, 503, { ok: false, error: 'Not configured' })

  const body = await readBody(req)
  const deviceId = cleanDevice(body.deviceId)
  if (!deviceId) return json(res, 400, { ok: false, error: 'Could not identify this device.' })

  const cookies = parseCookies(req.headers.cookie)
  const steps = {}

  for (const stepId of Object.keys(STEPS)) {
    const ts = readTicket(cookies, stepId, deviceId)
    const elapsed = ts ? Date.now() - ts : 0
    steps[stepId] = {
      visited: !!ts,
      ready: !!ts && elapsed >= MIN_DWELL_MS,
      waitMs: ts ? Math.max(0, MIN_DWELL_MS - elapsed) : MIN_DWELL_MS,
    }
  }

  return json(res, 200, { ok: true, steps })
}
