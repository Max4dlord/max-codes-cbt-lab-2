#!/usr/bin/env node
// ---------------------------------------------------------------------------
// ADMIN TOOL — runs on YOUR machine only. It is not part of the deployed app,
// so students can never see it, browse to it, or even learn it exists.
//
// You normally never need this: access is granted automatically by /api/issue.
// Keep it for the edge cases — someone on a locked-down browser, a student you
// want to hand access to directly, or debugging.
//
// USAGE
//   node scripts/admin-code.mjs <deviceId>
//
// The device id is shown to a student only if they open the in-app help and
// explicitly ask for it, so most of the time you will not need this at all.
//
// Requires GATE_SECRET in the environment — the SAME value set in Vercel:
//   GATE_SECRET=xxxx node scripts/admin-code.mjs a1b2c3d4e5f6
// ---------------------------------------------------------------------------

import crypto from 'node:crypto'

const SECRET = process.env.GATE_SECRET || ''
const PREFIX = process.env.CODE_PREFIX || 'EEE-'
const ALPHABET = '23456789ABCDEFGHJKMNPQRSTUVWXYZ'
const CODE_PERIOD_MS = 7 * 24 * 3600 * 1000

if (!SECRET || SECRET.length < 16) {
  console.error('\n✖ GATE_SECRET is not set (or is too short).')
  console.error('  Run it like this, using the same secret you put in Vercel:\n')
  console.error('    GATE_SECRET=your-secret node scripts/admin-code.mjs <deviceId>\n')
  process.exit(1)
}

const raw = process.argv[2]
if (!raw) {
  console.error('\nUsage: node scripts/admin-code.mjs <deviceId>\n')
  process.exit(1)
}

// Accept "A1B2C3-D4E5F6", "a1b2c3d4e5f6", or the message a student pasted.
const m = String(raw).match(/([A-Za-z0-9]{6})-?([A-Za-z0-9]{6})/)
const deviceId = m ? (m[1] + m[2]).toLowerCase() : String(raw).replace(/[^A-Za-z0-9]/g, '').toLowerCase()

if (!/^[a-z0-9]{8,64}$/.test(deviceId)) {
  console.error(`\n✖ "${raw}" does not look like a device id.\n`)
  process.exit(1)
}

const hmac = (data) => crypto.createHmac('sha256', SECRET).update(data).digest()
const w = Math.floor(Date.now() / CODE_PERIOD_MS)
const mac = hmac(`code|v1|${deviceId}|${w}`)

let code = PREFIX
for (let i = 0; i < 6; i++) code += ALPHABET[mac[i] % ALPHABET.length]

const expires = new Date((w + 1) * CODE_PERIOD_MS)

console.log(`\n  Device : ${deviceId}`)
console.log(`  CODE   : ${code}`)
console.log(`  Usable until ${expires.toLocaleString()}`)
console.log('  Works on that one device only. Once redeemed: 7 days of access.\n')
