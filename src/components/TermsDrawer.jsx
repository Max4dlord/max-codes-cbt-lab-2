import { useState } from 'react'

// "Key terms" — the full meaning of every abbreviation this particular question
// uses.  Kept collapsed so the question itself stays clean, and only rendered
// for questions that actually contain an abbreviation.
//
// The cathode ray oscilloscope is the one exception: it is always written out
// in the sentence itself ("cathode ray oscilloscope (CRO)"), never hidden here.
export default function TermsDrawer({ terms }) {
  const [open, setOpen] = useState(false)
  if (!terms || !terms.length) return null

  return (
    <div className="terms">
      <button
        type="button"
        className="terms-toggle"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
      >
        <span className="terms-caret" aria-hidden="true">{open ? '▾' : '▸'}</span>
        Key terms ({terms.length}) — what the abbreviations mean
      </button>

      {open && (
        <dl className="terms-list">
          {terms.map((t) => (
            <div className="terms-row" key={t.abbr}>
              <dt>{t.abbr}</dt>
              <dd>{t.full}</dd>
            </div>
          ))}
        </dl>
      )}
    </div>
  )
}
