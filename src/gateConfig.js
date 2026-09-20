// ===========================================================================
// ACCESS GATE CONFIG  —  OAU CBT Lab
// ===========================================================================
// PUBLIC, cosmetic settings only. Nothing here is secret — it all ships in the
// browser bundle. The real secrets (GATE_SECRET, ADMIN_KEY) live in Vercel
// Environment Variables and never leave the server.
//
//  THE FLOW  (fully automated — no manual DM, no admin in the loop)
//  --------------------------------------------------------------------------
//   1. Save our contact      -> opens WhatsApp, they save the contact
//   2. Support our partner   -> follow the partner channel   (required)
//   3. Connect on LinkedIn   -> follow-for-follow            (optional)
//   4. Tap "Enter the CBT Lab" -> the SERVER grants access instantly
//
//  Each button goes through /api/go, so the SERVER records the click and the
//  time spent before redirecting. /api/issue accepts only that server-recorded
//  evidence — there is no checkbox for a visitor to tick, and skipping the UI
//  with a direct API call fails because there is no signed visit ticket.
//  Access is HMAC-bound to the device, so it cannot be passed to a friend.
// ===========================================================================

export const gateConfig = {
  enabled: true,          // ← false = app wide open (kill switch)
  accessVersion: 4,       // ← bump to force everyone to re-verify

  // NOTE: the actual destination URLs (WhatsApp contact, partner channel,
  // LinkedIn) deliberately live SERVER-SIDE in api/_steps.js. The browser only
  // ever names a step id, so links cannot be swapped or skipped client-side.

  title: 'Welcome to the OAU CBT Lab',
  subtitle:
    'Free for our community. A few quick things below, then you are in for 7 days — no codes to type, no waiting.',

  brandName: 'Max-codes',
  brandSub: 'CBT Lab',

  // ---- the steps ----------------------------------------------------------
  // Copy only. Each `id` MUST match a key in api/_steps.js, which holds the
  // real destination and decides whether the step is required.
  // `optional: true` here is purely the badge shown to the visitor.
  steps: [
    {
      id: 'save-contact',
      heading: 'Save our contact first',
      note:
        'Tap below to open our chat on WhatsApp, then save the number from there. ' +
        'It is how you get updates and support when you need them.',
      action: 'Open WhatsApp to save us',
      confirm: 'Saved — done',
    },
    {
      id: 'partner-channel',
      heading: "Kindly support us by following our partner's channel",
      note:
        'It keeps this CBT Lab free for everyone, and it only takes a second. Thank you 🙏',
      action: "Open our partner's channel",
      confirm: 'Followed — thank you',
    },
    {
      id: 'linkedin',
      optional: true,
      heading: "Let's connect with each other on LinkedIn",
      note:
        'This one is a genuine follow-for-follow: connect with us and we will ' +
        'connect right back. Send your own profile link in our WhatsApp chat ' +
        'and we will follow you — I will surely follow back. Thanks, Max cares 💚',
      action: 'Open LinkedIn',
      confirm: 'Connected — thank you',
    },
  ],
}
