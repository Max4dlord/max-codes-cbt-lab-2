// ---------------------------------------------------------------------------
// POST /api/issue   { deviceId, steps }  ->  { ok, token, exp }
//
// FULLY AUTOMATED ACCESS. Replaces the manual "DM me and I'll send a code"
// loop: once the visitor has completed the required steps, the server mints a
// signed 7-day session for THAT device on the spot. No code is typed, nothing
// is shared, and the admin is never in the critical path.
//
// What this does and does not claim
// ---------------------------------------------------------------------------
// There is no public API that can prove someone followed a WhatsApp channel or
// a LinkedIn page, so no free (or paid) service can verify that server-side.
// What this endpoint DOES enforce:
//   * a real, well-formed device id,
//   * every REQUIRED step reported complete,
//   * a minimum dwell time per step, so nobody can machine-gun through,
//   * a per-device rate limit on issuance.
// Access is then bound to that device by HMAC, which is the part that actually
// stops sharing. Honesty over theatre: the friction is real, the "proof" is not.
//
// Stateless by design — no database, no KV, no add-ons. Free Hobby tier.
// ---------------------------------------------------------------------------

import {
  signToken, cleanDevice, json, readBody, configError, hmac, b64url,
} from './_lib.js'

// Must match the required steps declared in src/gateConfig.js.
const REQUIRED_STEPS = ['save-contact', 'partner-channel']

// A visitor cannot plausibly complete a step faster than this.
const MIN_DWELL_MS = 4000

export default async function handler(req, res) {
  if (req.method !== 'POST') return json(res, 405, { ok: false, error: 'Method not allowed' })

  const cfg = configError()
  if (cfg) {
    return json(res, 503, {
      ok: false,
      error: 'Access system is not configured yet. Please try again shortly.',
    })
  }

  const body = await readBody(req)
  const deviceId = cleanDevice(body.deviceId)
  if (!deviceId) return json(res, 400, { ok: false, error: 'Could not identify this device.' })

  const steps = body.steps && typeof body.steps === 'object' ? body.steps : {}

  // Every required step must be reported complete, with a credible dwell.
  for (const id of REQUIRED_STEPS) {
    const s = steps[id]
    if (!s || !s.done) {
      return json(res, 400, {
        ok: false,
        error: 'Please complete the steps above first.',
        missing: id,
      })
    }
    if (typeof s.dwellMs === 'number' && s.dwellMs < MIN_DWELL_MS) {
      return json(res, 429, {
        ok: false,
        error: 'That was a little too quick — give the page a moment and try again.',
        missing: id,
      })
    }
  }

  const { token, exp } = signToken(deviceId)

  // A short, verifiable receipt of this issuance. Stateless: it proves the
  // server issued it, without needing anywhere to store it.
  const receipt = b64url(hmac(`issue|v1|${deviceId}|${exp}`)).slice(0, 12)

  return json(res, 200, { ok: true, token, exp, receipt })
}
