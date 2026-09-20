# WhatsApp bot — automatic access codes

Student taps one button → WhatsApp opens with the message already typed → they
press send → **a bot replies in ~2 seconds** with a tap-to-enter link.

No pinned posts. No waiting for you. You are not in the loop at all.

---

## Read this first: what is and isn't possible

**You asked:** can a bot give the code only to people who followed the channel
or saved my contact?

**Following a channel: no — and not because of cost.** WhatsApp Channels expose
**no membership API**. Meta publishes none, and no BSP can sell you one. So
"only release the code once they followed" is **not buildable by anyone, at any
price**. Any tool claiming to do it is guessing. That is why the channel follow
is now shown as a warm, clearly-optional request rather than a fake gate.

**Saving your contact: no, and it never was.** Nothing can see another person's
address book. But the DM flow makes it moot — they end up messaging you anyway,
so you get their contact automatically, which is better than asking and hoping.

**What the bot genuinely does:** a real message physically arrives at your
number from their real WhatsApp account. That is verified contact, it hands you
their number, and the code it returns is bound to their device so forwarding it
is useless.

---

## ⚠️ Cost — and one date that matters

Verified against Meta's own pricing docs (updated 10 Sept 2026):

| | Cost |
|---|---|
| Messages **from** students to you | **Always free** |
| Your bot's replies, within 24h of their message | **Free until 30 Sept 2026** |
| Same replies, **from 1 Oct 2026** | Billed at the utility rate |
| Meta Cloud API access, webhooks, setup | Free |

**From 1 October 2026 Meta starts charging for in-window replies.** Roughly
**US$0.004–0.02 per reply** depending on market — so about **₦6–₦30 per
student**, once each, for 7 days of access. Not a subscription, and only when
someone actually messages you.

Today it costs **₦0**. Budget a small amount from October. If you'd rather never
pay a kobo, the existing click-through gate still works and stays free forever —
tell me and I'll keep both, with the bot as the fast path.

Use **Meta Cloud API directly**. Do *not* use a BSP like Twilio or AiSensy —
they add a US$30–50/month platform fee on top. Meta charges you nothing monthly.

---

## Setup (about 20 minutes, once)

### 1. Create the Meta app
1. Go to **developers.facebook.com** → **My Apps** → **Create App**
2. Type: **Business**
3. Add the **WhatsApp** product

### 2. Get your test number working
In **WhatsApp → API Setup** you get a free test number immediately. Note:
- **Phone number ID** (a long number) → this is `WHATSAPP_PHONE_ID`
- **Temporary access token** (24h, for testing)

### 3. Make the token permanent
Temporary tokens expire daily — the bot would die every morning.
1. **Business Settings → Users → System Users → Add**
2. Name it (e.g. "CBT Bot"), role **Admin**
3. **Add Assets** → your WhatsApp account → full control
4. **Generate New Token** → select your app → tick `whatsapp_business_messaging`
   and `whatsapp_business_management`
5. Set expiry **Never** → copy it → this is `WHATSAPP_TOKEN`

### 4. Point the webhook at your site
1. **WhatsApp → Configuration → Webhook → Edit**
2. **Callback URL:** `https://exam-prep-by-max.vercel.app/api/whatsapp`
3. **Verify token:** any password you invent → this is `WHATSAPP_VERIFY_TOKEN`
4. Click **Verify and save** (our endpoint answers the handshake automatically)
5. Under **Webhook fields**, subscribe to **`messages`** ← easy to miss, and
   nothing works without it

### 5. Add the environment variables in Vercel
Settings → Environment Variables (tick Production, Preview, Development):

| Name | Value |
|---|---|
| `GATE_SECRET` | `53191c1cfdc793b0066ce5bea949be466795a9c984282489498e543720e05637` |
| `ADMIN_KEY` | `Dafidi1357` |
| `CODE_PREFIX` | `EEE-` |
| `WHATSAPP_TOKEN` | the permanent token from step 3 |
| `WHATSAPP_PHONE_ID` | the phone number ID from step 2 |
| `WHATSAPP_VERIFY_TOKEN` | whatever you chose in step 4 |
| `SITE_URL` | `https://exam-prep-by-max.vercel.app` |

Then **Redeploy** — env vars only apply to new deployments.

### 6. Go live with your own number
The test number only messages 5 pre-registered contacts. To use **08071202598**:
**WhatsApp → API Setup → Add phone number**, then verify it.

> **Important:** if that number is already on the WhatsApp Business app, choose
> the **Coexistence** path during onboarding. That keeps the app working on the
> same number while the bot runs alongside. If you onboard it as a standard API
> number instead, you lose normal app use on it — and undoing that means
> deleting the registration and waiting **1–2 months**. Get this one right.

---

## Testing it

1. Open the CBT Lab → tap **Message us on WhatsApp**
2. WhatsApp opens with `ACCESS A1B2C3-D4E5F6` pre-typed → send
3. Reply should arrive in seconds with a tap-to-enter link

**No reply?** Check, in order:
- Did you subscribe to the **`messages`** webhook field? (most common)
- Is `WHATSAPP_TOKEN` the permanent one, not the 24h test token?
- Did you redeploy after adding the env vars?
- Vercel → Deployments → Functions → `api/whatsapp` logs

---

## If the bot is ever down

Nothing breaks. `scripts/admin-code.mjs` still works locally:

```bash
GATE_SECRET=<your-secret> node scripts/admin-code.mjs "A1B2C3-D4E5F6"
```

Students can also paste a code manually via **"Prefer to type the code?"** on
the gate.
