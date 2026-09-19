// ===========================================================================
// ACCESS GATE CONFIG  —  OAU CBT Lab
// ===========================================================================
// PUBLIC, cosmetic settings only. Nothing here is secret — it all ships in the
// browser bundle. The real secrets (GATE_SECRET, ADMIN_KEY) live in Vercel
// Environment Variables and never leave the server.
//
//  THE FLOW  (fully automated — no manual DM, no admin in the loop)
//  --------------------------------------------------------------------------
//   1. Save our contact      -> opens WhatsApp directly, they save the contact
//   2. Support our partner   -> follow the partner channel   (required)
//   3. Connect on LinkedIn   -> follow-for-follow            (optional)
//   4. Tap "Get my access"   -> the SERVER issues the code instantly
//
//  The code is minted by /api/issue for that one device, so nothing needs to
//  be typed or shared, and a code lifted from one phone is dead on another.
// ===========================================================================

export const gateConfig = {
  enabled: true,          // ← false = app wide open (kill switch)
  accessVersion: 4,       // ← bump to force everyone to re-verify

  // ---- contact ------------------------------------------------------------
  // Write the number however you like — '08071202598', '+234 807 120 2598'
  // or '2348071202598'. It is normalised before any link is built, so a wrong
  // format can never produce a broken "chat not found" link.
  // NOTE: the number is never displayed in the UI, only used to build the link.
  whatsappNumber: '08071202598',
  defaultCountryCode: '234',
  contactName: 'Max-codes OAU CBT Lab',

  title: 'Welcome to the OAU CBT Lab',
  subtitle:
    'Free for our community. A few quick things below, then you are in for 7 days — no codes to type, no waiting.',

  // Seconds a visitor must spend on a link before its confirm box unlocks.
  dwellSeconds: 6,

  brandName: 'Max-codes',
  brandSub: 'CBT Lab',

  // ---- the steps ----------------------------------------------------------
  // `kind` drives behaviour:
  //   'contact'  — opens a WhatsApp chat so they can save the contact
  //   'link'     — opens any URL in a new tab
  // `optional: true` means the step is encouraged but never blocks access.
  steps: [
    {
      id: 'save-contact',
      kind: 'contact',
      heading: 'Save our contact first',
      note:
        'Tap below to open our chat on WhatsApp, then save the number from there. ' +
        'It is how you get updates and support when you need them.',
      action: 'Open WhatsApp to save us',
      confirm: 'Saved — done',
      // Pre-typed opener so the chat is not empty when it opens.
      message: 'Hi Max-codes 👋 I just saved your contact from the CBT Lab.',
    },
    {
      id: 'partner-channel',
      kind: 'link',
      heading: "Kindly support us by following our partner's channel",
      note:
        'It keeps this CBT Lab free for everyone, and it only takes a second. Thank you 🙏',
      // ⚠️ REPLACE with the partner channel link when you have it.
      url: 'https://whatsapp.com/channel/0029VbCgWG9Fy72HO20EgY3F',
      action: "Open our partner's channel",
      confirm: 'Followed — thank you',
    },
    {
      id: 'linkedin',
      kind: 'link',
      optional: true,
      heading: "Let's connect with each other on LinkedIn",
      note:
        'This one is a genuine follow-for-follow: connect with us and we will ' +
        'connect right back. Send your own profile link in our WhatsApp chat ' +
        'and we will follow you — I will surely follow back. Thanks, Max cares 💚',
      // ⚠️ REPLACE with your real LinkedIn profile URL.
      url: 'https://www.linkedin.com/in/max-codes',
      action: 'Open LinkedIn',
      confirm: 'Connected — thank you',
    },
  ],
}
