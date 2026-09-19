# Access Gate — server-verified, per-device codes

## What changed

The old gate was 100% front-end: the secret shipped inside the JS bundle, so
anyone with DevTools could read it, forge a code, or flip a boolean and walk in.

Now the decision happens **on Vercel's servers**. `GATE_SECRET` never reaches
the browser. There is no "unlocked = true" flag to tamper with — the app holds
only a **signed token it cannot forge**, and asks the server on every load.

Cost: **₦0**. Three serverless functions, no database, no KV, no add-ons. It
sits inside Vercel's free Hobby tier (100k function calls/month; a gate check is
one tiny call per app load).

---

## The student flow

1. **Save my contact** — mandatory first step. Tapping it downloads a `.vcf`
   contact card, so it's one tap, not manual typing. Nothing else unlocks until
   they confirm.
2. **Follow the WhatsApp channel** — only appears after step 1.
3. **Request code** — one tap opens your WhatsApp DM with the message
   **already typed**: `ACCESS A1B2C3-D4E5F6`. They just press send.
4. **You reply** with their code (see admin console below).
5. **They paste it** → server verifies → in for **7 days**.

Each link step arms its confirm box only after a 6-second dwell timer, so nobody
blind-ticks through.

---

## Why sharing cannot work

The device ID is baked **inside the HMAC** that generates the code:

```
code = HMAC(GATE_SECRET, "code|v1|<deviceId>|<week>")
```

So a code issued for phone A is mathematically meaningless on phone B. Posting
it in a group chat achieves nothing. Verified end-to-end:

| Attack | Result |
|---|---|
| Friend pastes a code meant for someone else | ❌ rejected |
| Friend copies the whole session token | ❌ `wrong-device` |
| Tampering with the token's expiry date | ❌ `bad-signature` |
| Forging a signature without the secret | ❌ `bad-signature` |
| Going offline to dodge the check | ❌ fails closed |
| Editing localStorage | ❌ nothing to edit but their own token |

The only genuine bypass left is someone handing over their **unlocked physical
phone** — and no software anywhere solves that.

---

## Progress is never affected

The gate and the progress store use **completely separate localStorage keys**:

```
gate      : cbt_device_v1, cbt_token_v1
progress  : cbt_session_v2, cbt_results_v1, cbt_study_v2
```

Access lapsing after 7 days touches nothing. Scores, resumed sessions, study
position all survive. Re-verifying drops them exactly where they stopped.

---

## SETUP — do this once

### 1. Set your WhatsApp number

In `src/gateConfig.js`:

```js
whatsappNumber: '2348000000000',   // ⚠️ REPLACE — country code, digits only, no + and no spaces
```

For Nigeria: `0803 123 4567` becomes `2348031234567`. **The gate will not work
until you change this.**

### 2. Add the environment variables in Vercel

Vercel → your project → **Settings → Environment Variables**. Add three, ticking
Production, Preview and Development for each:

| Name | Value |
|---|---|
| `GATE_SECRET` | a long random string (see below) |
| `ADMIN_KEY` | your private admin password |
| `CODE_PREFIX` | `EEE-` |

Generate a strong secret:

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

> No `VITE_` prefix — that's deliberate. It keeps them server-only.
> Changing `GATE_SECRET` later invalidates every code and every active session.

### 3. Redeploy

Env vars only apply to **new** deployments. Vercel → Deployments → ⋯ → Redeploy.

---

## Issuing a code (your daily job)

A student DMs you: `ACCESS A1B2C3-D4E5F6`

1. Go to **`your-site.vercel.app/#/admin-code`**
2. Enter your admin key
3. Paste their whole message — it extracts the ID automatically
4. Hit **Generate code**
5. Hit **Copy full reply** → paste into WhatsApp → send

The reply is pre-written:

> Your access code: EEE-XXXXXX
> Go back to the CBT Lab and paste it in. Works on your phone only, valid for 7 days. Enjoy 💪

Bookmark the admin page. It's not linked anywhere in the UI.

---

## Timing

- **Code issuance window:** 7 days. A code you generate stays issuable for the
  current week (plus a grace week, so a code sent near midnight never dies).
- **Access length:** 7 days **from the moment they redeem**, not from issuance.
  Someone who redeems on day 6 still gets their full week.

Both are tunable in `api/_lib.js` (`CODE_PERIOD_MS`, `SESSION_MS`).

---

## Files

```
api/_lib.js             HMAC helpers, code generation, token sign/verify
api/unlock.js           POST — redeem a code, get a 7-day token
api/verify.js           POST — is this token real and alive?
api/admin-code.js       POST — admin-only, mint a code for a device
src/gateConfig.js       public cosmetic settings (number, channel, copy)
src/gateStore.js        device id, token storage, API calls
src/components/Gate.jsx       4-step gate UI
src/components/AdminCode.jsx  admin console at #/admin-code
src/App.jsx             server access check on load + on tab focus
vercel.json             rewrites now exclude /api/* (critical)
scripts/dev-api.mjs     local API for `npm run dev` — Vercel ignores this
.env.example            template for the env vars
```

---

## Local development

Two terminals:

```bash
GATE_SECRET=dev-secret ADMIN_KEY=letmein npm run dev:api   # API on :3001
npm run dev                                                # app on :5173
```

Vite proxies `/api/*` to the API automatically.

---

## Kill switch

`enabled: false` in `src/gateConfig.js` opens the app to everyone instantly.
`accessVersion` bump is available if you ever want a hard reset.

---

## If it gets heavy

This is manual — you DM each code yourself. That's fine for tens of students and
it drives real engagement with your channel. If volume grows, the upgrade path
is a WhatsApp bot (Twilio / 360dialog free tier) that replies with the code
automatically by calling `/api/admin-code`. The endpoint is already built for it.
