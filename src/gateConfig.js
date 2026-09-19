// ===========================================================================
// ACCESS GATE CONFIG  —  OAU EEE 282 CBT Lab
// ===========================================================================
// This file holds only PUBLIC, cosmetic settings. Nothing here is a secret —
// it all ships in the browser bundle. The real secrets (GATE_SECRET, ADMIN_KEY)
// live in Vercel Environment Variables and never leave the server.
//
//  THE FLOW
//  --------------------------------------------------------------------------
//   Step 1  Save my contact          (they must confirm before anything else)
//   Step 2  Follow the WhatsApp channel
//   Step 3  Tap "Request my code"  -> opens WhatsApp DM with the message
//           pre-typed, including their unique device ID. They just hit send.
//   Step 4  You reply with their code (from #/admin-code)
//   Step 5  They paste it -> server verifies -> 7 days of access
//
//  Codes are generated PER DEVICE on the server, so a shared code is dead on
//  arrival on any other phone.
// ===========================================================================

export const gateConfig = {
  enabled: true,          // ← false = app wide open (kill switch)
  accessVersion: 3,       // ← bump to force everyone to re-verify

  // ---- your details -------------------------------------------------------
  // International format, digits only, no "+" and no spaces.
  // Your WhatsApp number. Write it however you like — '08071202598',
  // '+234 807 120 2598' or '2348071202598' all work. It is normalised to the
  // international form automatically before any link is built, so a wrong
  // format can never produce a broken "chat not found" link for a student.
  whatsappNumber: '08071202598',
  defaultCountryCode: '234',   // used when the number starts with 0
  contactName: 'Max-codes EEE 282 CBT',
  channelUrl: 'https://whatsapp.com/channel/0029VbCgWG9Fy72HO20EgY3F',

  // The word they send you. Their device ID is appended automatically.
  requestWord: 'ACCESS',

  title: 'Unlock the OAU EEE 282 CBT Lab',
  subtitle:
    'Free for our community. Do the three quick steps below, get your personal code on WhatsApp, and you are in for 7 days.',

  // Seconds the user must spend on a link before its confirm box unlocks.
  dwellSeconds: 6,

  brandName: 'Max-codes',
  brandSub: 'EEE 282 CBT Lab',
}
