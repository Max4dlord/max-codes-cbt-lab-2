// ---------------------------------------------------------------------------
// POST /api/unlock   { deviceId, code }  ->  { ok, token, exp }
//
// The student's browser sends its device id plus the code you DM'd them.
// The server recomputes the expected code for THAT device and compares.
// If it matches, it mints a signed session token valid for 7 days.
//
// A code for device A simply does not verify on device B, so forwarding the
// code to a friend is useless. And the token is HMAC-signed with a secret
// that only Vercel holds — DevTools cannot forge one.
// ---------------------------------------------------------------------------

import { isCodeValid, signToken, cleanDevice, json, readBody, configError } from './_lib.js'

const PREFIX = process.env.CODE_PREFIX || 'MAX-'

export default async function handler(req, res) {
  if (req.method !== 'POST') return json(res, 405, { ok: false, error: 'Method not allowed' })

  const cfg = configError()
  if (cfg) return json(res, 503, { ok: false, error: 'Access system not configured yet. Please tell the admin.', detail: cfg })

  const body = await readBody(req)
  const deviceId = cleanDevice(body.deviceId)
  const code = body.code

  if (!deviceId) return json(res, 400, { ok: false, error: 'Invalid device id.' })
  if (!code) return json(res, 400, { ok: false, error: 'Enter the code you received on WhatsApp.' })

  if (!isCodeValid(deviceId, code, PREFIX)) {
    return json(res, 401, {
      ok: false,
      error: 'That code is not valid for this device. Codes are issued per phone — a code sent to someone else will never work here. Request your own on WhatsApp.',
    })
  }

  const { token, exp } = signToken(deviceId)
  return json(res, 200, { ok: true, token, exp })
}
