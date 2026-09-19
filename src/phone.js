// ---------------------------------------------------------------------------
// Phone number normalisation.
//
// WHY: wa.me links only work with the full international number, digits only,
// no "+", no spaces. If the admin ever types '0807...', '+234 807...' or
// '234-807-...', this converts it to the one correct form so students never
// hit a "phone number shared via link is not on WhatsApp" dead end.
//
// Change the number in gateConfig.js in ANY format — this handles the rest.
// ---------------------------------------------------------------------------

/**
 * Returns digits-only international form, e.g. '2348071202598'.
 *   '08071202598'      -> '2348071202598'   (leading 0 swapped for country code)
 *   '+234 807 120 2598'-> '2348071202598'   (plus and spaces stripped)
 *   '2348071202598'    -> '2348071202598'   (already fine)
 *   '8071202598'       -> '2348071202598'   (bare national number)
 */
export function normalizeWhatsApp(raw, countryCode = '234') {
  let d = String(raw || '').replace(/\D/g, '')   // strip +, spaces, dashes, ()
  const cc = String(countryCode || '234').replace(/\D/g, '')

  if (!d) return ''

  // 00 international prefix -> drop it
  if (d.startsWith('00')) d = d.slice(2)

  // Local trunk form: 0XXXXXXXXXX -> CC + XXXXXXXXXX
  if (d.startsWith('0')) return cc + d.replace(/^0+/, '')

  // Already has the country code
  if (d.startsWith(cc)) return d

  // Bare national number (e.g. 8071202598) -> prepend country code
  return cc + d
}

/** Pretty form for display only, e.g. '+234 807 120 2598'. */
export function displayWhatsApp(raw, countryCode = '234') {
  const d = normalizeWhatsApp(raw, countryCode)
  if (!d) return ''
  const cc = String(countryCode).replace(/\D/g, '')
  const rest = d.startsWith(cc) ? d.slice(cc.length) : d
  // Nigerian-style grouping: 3-3-4 (807 120 2598); falls back gracefully.
  const m = rest.match(/^(\d{3})(\d{3})(\d+)$/)
  const grouped = m ? `${m[1]} ${m[2]} ${m[3]}` : rest
  return `+${cc} ${grouped}`
}
