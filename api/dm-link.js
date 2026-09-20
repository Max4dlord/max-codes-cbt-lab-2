// ---------------------------------------------------------------------------
// GET /api/dm-link?d=<deviceId>  ->  302 to the WhatsApp DM, pre-typed
//
// Same trick as /api/go: the student passes through our server, so we record
// that they really did open the chat. The pre-typed message carries their
// device id, which is what lets the bot mint a code bound to their phone.
// ---------------------------------------------------------------------------

import { cleanDevice, configError } from './_lib.js'
import { whatsappDmUrl, TICKET_TTL_MS, cookieName } from './_steps.js'
import { signTicket } from './go.js'

export default async function handler(req, res) {
  if (configError()) return res.status(503).send('Access system not configured.')

  const url = new URL(req.url, `https://${req.headers.host}`)
  const deviceId = cleanDevice(url.searchParams.get('d'))
  if (!deviceId) return res.status(400).send('Missing device.')

  const ts = Date.now()
  res.setHeader('Set-Cookie', [
    `${cookieName('whatsapp-dm')}=${encodeURIComponent(`${ts}.${signTicket('whatsapp-dm', deviceId, ts)}`)}`,
    'Path=/',
    `Max-Age=${Math.floor(TICKET_TTL_MS / 1000)}`,
    'HttpOnly', 'Secure', 'SameSite=Lax',
  ].join('; '))

  res.setHeader('Cache-Control', 'no-store')
  res.writeHead(302, { Location: whatsappDmUrl(deviceId) })
  res.end()
}
