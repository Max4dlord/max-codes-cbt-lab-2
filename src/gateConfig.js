// ===========================================================================
// ACCESS GATE CONFIG  —  Max-codes CBT Lab
// ===========================================================================
// Everything that controls the "join → unlock" gate lives in this one file.
//
//  HOW TO USE
//  --------------------------------------------------------------------------
//  1. enabled          : set to false to open the app to everyone (kill switch).
//  2. code             : the code you post in your WhatsApp channel/group.
//                        Students type it here to unlock the app.
//  3. accessVersion    : an unlock is valid UNTIL you bump this number.
//                        Bump it (1 → 2) whenever you change the code or want
//                        everyone to re-verify — all stored unlocks instantly
//                        become invalid on their next visit.
//  4. tasks            : the list of things users must do before the unlock
//                        button becomes active. To add more tasks later, just
//                        add another object here (see examples below).
//
//  Adding more tasks (copy one of these into `tasks`):
//    { id: 'join-group', type: 'follow-link',
//      label: 'Join our WhatsApp group',
//      description: 'Get answers, updates and new codes in the group.',
//      url: 'https://chat.whatsapp.com/YOUR_GROUP_LINK',
//      buttonLabel: 'Join WhatsApp group →',
//      confirmLabel: 'I have joined the group' }
//
//    { id: 'telegram', type: 'follow-link',
//      label: 'Join our Telegram channel',
//      description: 'Backup channel for announcements.',
//      url: 'https://t.me/YourChannel',
//      buttonLabel: 'Open Telegram →',
//      confirmLabel: 'I have joined the Telegram channel' }
//
//    { id: 'youtube', type: 'follow-link',
//      label: 'Subscribe on YouTube',
//      description: 'Video solutions and CBT walkthroughs.',
//      url: 'https://youtube.com/@YourChannel',
//      buttonLabel: 'Open YouTube →',
//      confirmLabel: 'I have subscribed' }
// ===========================================================================

export const gateConfig = {
  enabled: true,          // ← switch to false to disable the gate entirely
  accessVersion: 1,       // ← bump this to force everyone to re-unlock
  code: 'Maxprep3060',    // ← the access code (change anytime; bump version too)

  title: 'Unlock Max-codes CBT Lab',
  subtitle:
    'The CBT lab is free for our community. Complete the step(s) below, then enter the access code — it is posted inside our WhatsApp channel.',

  tasks: [
    {
      id: 'follow-channel',
      type: 'follow-link',
      label: 'Follow our WhatsApp channel',
      description:
        'All updates, new question banks and new access codes are posted there first.',
      url: 'https://whatsapp.com/channel/0029VbCgWG9Fy72HO20EgY3F',
      buttonLabel: 'Open WhatsApp channel →',
      confirmLabel: 'I have followed the channel',
    },
  ],
}
