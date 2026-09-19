// ---------------------------------------------------------------------------
// POST /api/verify   { deviceId, token }  ->  { ok, exp }
//
// Called on every app load. The signature check happens on the SERVER, so a
// tech-savvy user cannot flip a localStorage boolean and walk in — there is no
// boolean to flip, only a token they cannot forge.
// ---------------------------------------------------------------------------

import { verifyToken, cleanDevice, json, readBody, configError } from './_lib.js'

export default async function handler(req, res) {
  if (req.method !== 'POST') return json(res, 405, { ok: false, error: 'Method not allowed' })

  if (configError()) return json(res, 503, { ok: false, reason: 'not-configured' })

  const body = await readBody(req)
  const deviceId = cleanDevice(body.deviceId)
  if (!deviceId) return json(res, 400, { ok: false, error: 'Invalid device id.' })

  const result = verifyToken(body.token, deviceId)
  if (!result.ok) return json(res, 401, { ok: false, reason: result.reason })

  return json(res, 200, { ok: true, exp: result.payload.exp })
}
