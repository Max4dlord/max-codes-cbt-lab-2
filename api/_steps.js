// ---------------------------------------------------------------------------
// SERVER-SIDE step registry.
//
// The real destination URLs live HERE, on the server — never in a query string.
// If /api/go accepted a `url` parameter it would be an open redirect, and our
// domain could be used to bounce people to phishing pages. The browser only
// ever names a step id; the server decides where that goes.
// ---------------------------------------------------------------------------

const WHATSAPP_NUMBER = '2348071202598'
const CONTACT_OPENER = 'Hi Max-codes, I just saved your contact from the CBT Lab.'

export const STEPS = {
  'save-contact': {
    required: true,
    url: `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(CONTACT_OPENER)}`,
  },
  'partner-channel': {
    required: true,
    url: 'https://whatsapp.com/channel/0029VbCgWG9Fy72HO20EgY3F',
  },
  'linkedin': {
    required: false,
    url: 'https://www.linkedin.com/in/toluwanimi-david-b6702a263',
  },
}

export const REQUIRED_STEPS = Object.keys(STEPS).filter((k) => STEPS[k].required)

// How long a visit must last before it counts. Measured with SERVER clocks at
// both ends, so the browser cannot shorten it.
export const MIN_DWELL_MS = 5000

// A visit ticket stays usable for a day, so someone who wanders off mid-flow
// does not have to start again.
export const TICKET_TTL_MS = 24 * 3600 * 1000

export const cookieName = (stepId) => `gs_${String(stepId).replace(/[^a-z0-9-]/gi, '')}`
