// ---------------------------------------------------------------------------
// Typed-answer grading for CBT Lab 2 (EEE 282).
//
// Every question in the bank carries four options, so the app always works as
// a plain CBT. Questions flagged `type: 'calc'` or `type: 'text'` ALSO show a
// typed-answer box, which mirrors how the EEE 282 bench exam is actually
// answered (you compute a value, you don't pick one).
//
//   calc → numeric grader: every value in `num.values` must be matched by some
//          number the student typed, within a tolerance.
//   text → keyword grader: `match.all` (every keyword), `match.any` (at least
//          one) and `match.minAny` (at least n of a list).
//
// A non-empty typed answer always takes precedence over the chosen option.
// ---------------------------------------------------------------------------

// Pull every number out of a free-text string. Handles "20 V, 10 V, 7.07 V",
// "0.01s 100Hz", "45°", "1 cm" and comma thousands separators.
export function parseNumbers(raw) {
  const out = []
  const re = /-?\d+(?:\.\d+)?/g
  let m
  while ((m = re.exec(String(raw || ''))) !== null) {
    const v = Number(m[0])
    if (Number.isFinite(v)) out.push(v)
  }
  return out
}

function toleranceFor(v) {
  return Math.max(0.02, Math.abs(v) * 0.02)
}

// Numeric grading: all expected values must be matched.
export function gradeNumeric(values, raw) {
  const typed = parseNumbers(raw)
  if (!typed.length) {
    return { ok: false, matched: [], missing: values, detail: 'No number was entered.' }
  }
  const matched = []
  const missing = []
  for (const v of values) {
    const hit = typed.some((t) => Math.abs(t - v) <= toleranceFor(v))
    if (hit) matched.push(v)
    else missing.push(v)
  }
  const ok = missing.length === 0
  const detail = ok
    ? `All ${values.length} value${values.length > 1 ? 's' : ''} correct (${matched.join(', ')}).`
    : missing.length === values.length
      ? `None of the expected values (${values.join(', ')}) appear in your answer.`
      : `You got ${matched.join(', ')} right; ${missing.join(', ')} ${missing.length > 1 ? 'are' : 'is'} still missing or off.`
  return { ok, matched, missing, detail }
}

// Keyword grading for prose answers.
export function gradeKeywords(match, raw) {
  const t = String(raw || '').toLowerCase()
  if (!t.trim()) return { ok: false, detail: 'No answer was entered.' }
  const all = match?.all || []
  const any = match?.any || []
  const minAny = match?.minAny

  const missingAll = all.filter((w) => !t.includes(String(w).toLowerCase()))
  const anyHit = any.length === 0 || any.some((w) => t.includes(String(w).toLowerCase()))
  const hits = minAny
    ? (minAny.list || []).filter((w) => t.includes(String(w).toLowerCase())).length
    : 0
  const minOk = !minAny || hits >= minAny.n

  const ok = missingAll.length === 0 && anyHit && minOk
  let detail
  if (ok) detail = 'Your answer covers the required points.'
  else if (missingAll.length) detail = `Missing: ${missingAll.join(', ')}.`
  else if (!anyHit) detail = `Expected one of: ${any.join(', ')}.`
  else detail = `Name at least ${minAny.n} of: ${minAny.list.join(', ')} (you named ${hits}).`
  return { ok, detail }
}

// One entry point: grade whatever the student typed for a question.
export function gradeTyped(q, raw) {
  if (q.type === 'calc' && q.num) {
    return gradeNumeric(q.num.values || [], raw)
  }
  if (q.type === 'text' && q.match) {
    return gradeKeywords(q.match, raw)
  }
  return { ok: false, detail: 'This question has no typed-answer rule.' }
}

export function hasTypedAnswer(q) {
  return q.type === 'calc' || q.type === 'text'
}

// Helper text shown under the input box.
export function typedPrompt(q) {
  if (q.type === 'calc') {
    const unit = q.num?.unit ? ` in ${q.num.unit}` : ''
    const many = (q.num?.values || []).length > 1
    return many
      ? `Type every value you are asked for${unit}, separated by commas — e.g. 20, 10, 7.07`
      : `Type your answer${unit} — e.g. ${(q.num?.values || [0])[0]}`
  }
  if (q.type === 'text') return 'Type your answer in your own words (key terms are matched).'
  return ''
}
