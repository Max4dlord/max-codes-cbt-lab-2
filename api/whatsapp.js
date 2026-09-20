// ---------------------------------------------------------------------------
// WhatsApp DM bot  —  GET (webhook verify) + POST (incoming message)
//
// This is the automation that removes you from the loop entirely.
//
//   student taps "Message us"  ->  WhatsApp opens with "ACCESS A1B2C3-D4E5F6"
//   student hits send          ->  Meta calls THIS endpoint
//   this endpoint replies      ->  "Your code: MAX-XXXXXX  <tap-to-enter link>"
//
// No pinned posts, no waiting for you, no manual DM. Typically 2-3 seconds.
//
// WHY A DM AND NOT A CHANNEL FOLLOW
// WhatsApp Channels expose no membership API — Meta publishes none, and no BSP
// can sell you one. So "only release the code once they followed the channel"
// is not buildable by anyone, at any price. A DM is different: the student's
// message physically arrives at your number, so it is real, verifiable contact
// AND it hands you their WhatsApp contact automatically.
//
// COST (verified against Meta's pricing docs, Sept 2026)
//   * Inbound messages from users: always free.
//   * Your replies inside the 24h customer service window: free until
//     1 October 2026. After that Meta bills them at the utility rate
//     (roughly US$0.004-0.02 per reply depending on market).
//   So this is free now and ~a few naira per student later. Never a subscription.
//
// SETUP: see WHATSAPP-BOT-SETUP.md
// ---------------------------------------------------------------------------

import {
  SECRET, ADMIN_KEY, codeFor, cleanDevice, json, readBody, configError,
} from './_lib.js'

const TOKEN = process.env.WHATSAPP_TOKEN || ''
const PHONE_ID = process.env.WHATSAPP_PHONE_ID || ''
const VERIFY_TOKEN = process.env.WHATSAPP_VERIFY_TOKEN || ''
const PREFIX = process.env.CODE_PREFIX || 'EEE-'
const SITE = process.env.SITE_URL || ''

// The word a student sends. Matched loosely so "access", "Access!" all work.
const TRIGGER = /\b(access|code|unlock|start)\b/i

// Pull a device id out of "ACCESS A1B2C3-D4E5F6" (or a bare id).
function extractDevice(text) {
  const m = String(text || '').match(/([A-Za-z0-9]{6})-([A-Za-z0-9]{6})/)
  if (m) return (m[1] + m[2]).toLowerCase()
  const bare = String(text || '').match(/\b([A-Za-z0-9]{12})\b/)
  return bare ? bare[1].toLowerCase() : null
}

async function sendText(to, body) {
  if (!TOKEN || !PHONE_ID) return { ok: false, error: 'bot-not-configured' }
  const r = await fetch(`https://graph.facebook.com/v21.0/${PHONE_ID}/messages`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      messaging_product: 'whatsapp',
      to,
      type: 'text',
      text: { preview_url: true, body },
    }),
  })
  return { ok: r.ok, status: r.status }
}

export default async function handler(req, res) {
  // ---- Meta webhook verification handshake (one time, at setup) ----
  if (req.method === 'GET') {
    const url = new URL(req.url, `https://${req.headers.host}`)
    const mode = url.searchParams.get('hub.mode')
    const token = url.searchParams.get('hub.verify_token')
    const challenge = url.searchParams.get('hub.challenge')
    if (mode === 'subscribe' && VERIFY_TOKEN && token === VERIFY_TOKEN) {
      res.setHeader('Content-Type', 'text/plain')
      return res.status(200).send(challenge || '')
    }
    return res.status(403).send('Forbidden')
  }

  if (req.method !== 'POST') return json(res, 405, { ok: false })

  // Always ACK fast: Meta retries aggressively on a non-200, which would spam
  // the student with duplicate codes.
  const body = await readBody(req)

  try {
    const value = body?.entry?.[0]?.changes?.[0]?.value
    const msg = value?.messages?.[0]

    // Status callbacks (delivered/read) have no `messages` — ignore quietly.
    if (!msg || msg.type !== 'text') return json(res, 200, { ok: true })

    const from = msg.from                     // student's WhatsApp number
    const text = msg.text?.body || ''

    if (configError()) {
      await sendText(from, 'Our access system is being set up right now. Please try again shortly 🙏')
      return json(res, 200, { ok: true })
    }

    if (!TRIGGER.test(text)) {
      await sendText(
        from,
        'Hi 👋 To get into the CBT Lab, tap the "Message us" button on the site ' +
        'so your access code is matched to your phone.'
      )
      return json(res, 200, { ok: true })
    }

    const deviceId = cleanDevice(extractDevice(text))
    if (!deviceId) {
      await sendText(
        from,
        'Almost there! Please open the CBT Lab and tap the WhatsApp button there — ' +
        'it fills in a short ID that ties the code to your phone. ' +
        'Sending just "ACCESS" on its own cannot be matched to a device.'
      )
      return json(res, 200, { ok: true })
    }

    const code = codeFor(deviceId, undefined, PREFIX)
    const link = SITE ? `${SITE}/#/?c=${encodeURIComponent(code)}` : ''

    await sendText(
      from,
      `You're in ✅\n\nYour access code: *${code}*` +
      (link ? `\n\nOr just tap this and you're straight in:\n${link}` : '') +
      `\n\nWorks on that phone only, valid for 7 days. Enjoy the CBT Lab 💚\n— Max cares`
    )
  } catch (e) {
    console.warn('whatsapp webhook error:', e?.message)
  }

  return json(res, 200, { ok: true })
}
