import { useState } from 'react'
import { gateConfig } from '../gateConfig.js'
import { saveUnlock } from '../progress.js'

/**
 * Access gate — shown instead of the app until the visitor completes the
 * configured tasks (e.g. follows the WhatsApp channel) and enters the code
 * posted there. Purely client-side; config lives in src/gateConfig.js.
 */
export default function Gate({ onUnlock }) {
  const [done, setDone] = useState({})
  const [code, setCode] = useState('')
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)

  const tasks = gateConfig.tasks || []
  const allDone = tasks.every((t) => done[t.id])

  function toggleTask(id) {
    setDone((d) => ({ ...d, [id]: !d[id] }))
  }

  function tryUnlock() {
    setError('')
    if (!allDone) {
      setError('Please complete the step(s) above first.')
      return
    }
    if (!code.trim()) {
      setError('Enter the access code from the WhatsApp channel.')
      return
    }
    setBusy(true)
    // small delay keeps the UI feeling deliberate
    setTimeout(() => {
      if (code.trim().toLowerCase() === gateConfig.code.toLowerCase()) {
        saveUnlock(gateConfig.accessVersion)
        onUnlock()
      } else {
        setError('That code is not correct. Check the latest post in the WhatsApp channel and try again.')
        setBusy(false)
      }
    }, 350)
  }

  return (
    <div className="gate-shell">
      <div className="gate-card">
        <div className="gate-brand">
          <span className="nav-logo">MC</span>
          <span className="gate-brand-name">Max-codes · <em>CBT Lab</em></span>
        </div>

        <h1>{gateConfig.title}</h1>
        <p className="gate-sub">{gateConfig.subtitle}</p>

        <ol className="gate-steps">
          {tasks.map((t, i) => (
            <li key={t.id} className="gate-step">
              <div className="gate-step-head">
                <span className="gate-step-no">{i + 1}</span>
                <div>
                  <div className="gate-step-label">{t.label}</div>
                  <div className="gate-step-desc">{t.description}</div>
                </div>
              </div>
              <div className="gate-step-actions">
                <a
                  className="btn gate-btn-wa"
                  href={t.url}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {t.buttonLabel}
                </a>
                <label className={`gate-check ${done[t.id] ? 'checked' : ''}`}>
                  <input
                    type="checkbox"
                    checked={!!done[t.id]}
                    onChange={() => toggleTask(t.id)}
                  />
                  <span>{t.confirmLabel}</span>
                </label>
              </div>
            </li>
          ))}
        </ol>

        <div className="gate-code">
          <label htmlFor="gate-code-input">Access code</label>
          <input
            id="gate-code-input"
            className="gate-input"
            type="text"
            placeholder="Paste the code from the channel"
            value={code}
            onChange={(e) => { setCode(e.target.value); setError('') }}
            onKeyDown={(e) => { if (e.key === 'Enter') tryUnlock() }}
            autoComplete="off"
            spellCheck="false"
          />
        </div>

        {error && <p className="gate-error" role="alert">{error}</p>}

        <button
          className="btn btn-primary btn-lg gate-unlock"
          onClick={tryUnlock}
          disabled={!allDone || !code.trim() || busy}
        >
          {busy ? 'Checking…' : 'Unlock the CBT Lab →'}
        </button>

        <p className="gate-note">
          🔒 This unlocks once on this device. You will only be asked again when a new access code is issued.
        </p>
      </div>
    </div>
  )
}
