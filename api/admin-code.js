// ---------------------------------------------------------------------------
// POST /api/admin-code   { adminKey, deviceId }  ->  { ok, code, expiresAt }
//
// YOUR endpoint. A student DMs you "ACCESS <their device id>"; you paste that
// id here and get the one code that works on their phone only.
// The admin panel at #/admin-code calls this for you.
// ---------------------------------------------------------------------------

import {
  codeFor, codeWindow, CODE_PERIOD_MS, ADMIN_KEY,
  cleanDevice, safeEqual, json, readBody,
} from './_lib.js'

const PREFIX = process.env.CODE_PREFIX || 'MAX-'

export default async function handler(req, res) {
  if (req.method !== 'POST') return json(res, 405, { ok: false, error: 'Method not allowed' })

  const body = await readBody(req)
  if (!body.adminKey || !safeEqual(body.adminKey, ADMIN_KEY)) {
    return json(res, 401, { ok: false, error: 'Wrong admin key.' })
  }

  const deviceId = cleanDevice(body.deviceId)
  if (!deviceId) {
    return json(res, 400, {
      ok: false,
      error: 'That device ID looks wrong. It should be the long code the student pasted (letters/numbers, 8-64 chars).',
    })
  }

  const w = codeWindow()
  return json(res, 200, {
    ok: true,
    code: codeFor(deviceId, w, PREFIX),
    deviceId,
    expiresAt: (w + 1) * CODE_PERIOD_MS,
    note: 'Valid for this device only. Student keeps access 7 days from redemption.',
  })
}
