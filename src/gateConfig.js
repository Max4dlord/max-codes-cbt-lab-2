// ===========================================================================
// ACCESS GATE CONFIG  —  OAU CBT Lab
// ===========================================================================
// PUBLIC, cosmetic settings only. Nothing here is secret — it all ships in the
// browser bundle. The real secrets (GATE_SECRET, ADMIN_KEY) live in Vercel
// Environment Variables and never leave the server.
//
//  THE FLOW  (a bot does the work — nobody waits on the admin)
//  --------------------------------------------------------------------------
//   1. Student taps "Message us on WhatsApp" (message pre-typed with their ID)
//   2. They press send
//   3. The bot at /api/whatsapp replies in seconds with a tap-to-enter link
//   4. Tapping it redeems automatically -> 7 days of access
//
//  The code is HMAC-derived from their DEVICE, so forwarding it to a friend
//  does nothing. Saving the contact happens naturally: they are now in your
//  DMs, which is better than asking and hoping.
//
//  The channel follow and LinkedIn connect are shown as OPTIONAL requests.
//  That is deliberate and honest: WhatsApp publishes no channel-membership
//  API, so nobody — at any price — can verify a follow. Anything claiming to
//  is guessing. They are asked warmly instead of gated falsely.
// ===========================================================================

export const gateConfig = {
  enabled: true,          // ← false = app wide open (kill switch)
  accessVersion: 4,       // ← bump to force everyone to re-verify

  // NOTE: the actual destination URLs (WhatsApp contact, partner channel,
  // LinkedIn) deliberately live SERVER-SIDE in api/_steps.js. The browser only
  // ever names a step id, so links cannot be swapped or skipped client-side.

  title: 'Welcome to the OAU CBT Lab',
  subtitle:
    'Free for our community. One tap on WhatsApp and you are in — our assistant replies in seconds.',

  brandName: 'Max-codes',
  brandSub: 'CBT Lab',

  // ---- optional community asks --------------------------------------------
  // Copy only. Each `id` MUST match a key in api/_steps.js, which holds the
  // real destination. None of these block access.
  steps: [
    {
      id: 'partner-channel',
      heading: "Kindly support us by following our partner's channel",
      note:
        'It keeps this CBT Lab free for everyone, and it only takes a second. Thank you 🙏',
      action: 'Open channel',
    },
    {
      id: 'linkedin',
      heading: "Let's connect with each other on LinkedIn",
      note:
        'A genuine follow-for-follow: connect with us and drop your own profile ' +
        'link in our WhatsApp chat — I will surely follow back. Thanks, Max cares 💚',
      action: 'Open LinkedIn',
    },
  ],
}
