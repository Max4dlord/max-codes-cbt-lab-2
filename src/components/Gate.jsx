import { useEffect, useRef, useState } from 'react'
import { gateConfig } from '../gateConfig.js'
import { loadSteps, saveSteps, requestAccess, redeemCode } from '../gateStore.js'
import { normalizeWhatsApp } from '../phone.js'

/**
 * Access gate.
 *
 * Design rules this component follows:
 *  - Progress is PERSISTED (localStorage) the instant a step is opened or
 *    confirmed. Tapping a link sends the visitor to WhatsApp/LinkedIn, which on
 *    phones often replaces the tab; when they return, nothing may restart.
 *  - Nothing admin-facing appears here. No phone number, no device id, no
 *    admin link, no mention of how codes are minted.
 *  - Steps read as friendly requests, never as "tasks".
 *  - Optional steps are clearly marked and never block access.
 *  - Access is granted automatically by the server once required steps are
 *    complete — the visitor never types a code.
 */
export default function Gate({ onUnlock }) {
  const steps = gateConfig.steps || []
  const required = steps.filter((s) => !s.optional)

  const [progress, setProgress] = useState(() => loadSteps())
  const [, setTick] = useState(0)
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)
  const timers = useRef({})

  // Drives the "please wait Ns" countdown label.
  useEffect(() => {
    const id = setInterval(() => setTick((t) => t + 1), 500)
    return () => clearInterval(id)
  }, [])
  useEffect(() => () => Object.values(timers.current).forEach(clearTimeout), [])

  // Magic-link fallback: .../#/?c=CODE redeems automatically.
  useEffect(() => {
    const qs = window.location.hash.split('?')[1]
    if (!qs) return
    const c = new URLSearchParams(qs).get('c')
    if (!c) return
    setBusy(true)
    redeemCode(c.trim()).then((r) => {
      try { window.history.replaceState(null, '', window.location.pathname + '#/') } catch {}
      if (r.ok) onUnlock(r.exp)
      else { setError(r.error); setBusy(false) }
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const dwellMs = (gateConfig.dwellSeconds ?? 6) * 1000

  function update(next) {
    setProgress(next)
    saveSteps(next)          // persist immediately — survives redirect + reload
  }

  function openStep(step) {
    const next = {
      ...progress,
      [step.id]: { ...(progress[step.id] || {}), openedAt: Date.now() },
    }
    update(next)
  }

  function toggleDone(step) {
    if (!isArmed(step)) return
    const cur = progress[step.id] || {}
    update({ ...progress, [step.id]: { ...cur, done: !cur.done } })
    setError('')
  }

  const isOpened = (step) => !!(progress[step.id] && progress[step.id].openedAt)
  const isDone = (step) => !!(progress[step.id] && progress[step.id].done)

  // A confirm box arms only after the visitor opened the link and the dwell
  // has elapsed. Because openedAt is persisted, time spent away counts too —
  // coming back from WhatsApp lands on an already-armed step.
  function isArmed(step) {
    const p = progress[step.id]
    if (!p || !p.openedAt) return false
    return Date.now() - p.openedAt >= dwellMs
  }

  function secondsLeft(step) {
    const p = progress[step.id]
    if (!p || !p.openedAt) return Math.ceil(dwellMs / 1000)
    return Math.max(0, Math.ceil((dwellMs - (Date.now() - p.openedAt)) / 1000))
  }

  function hrefFor(step) {
    if (step.kind === 'contact') {
      const wa = normalizeWhatsApp(gateConfig.whatsappNumber, gateConfig.defaultCountryCode)
      const text = step.message ? `?text=${encodeURIComponent(step.message)}` : ''
      return `https://wa.me/${wa}${text}`
    }
    return step.url
  }

  const allRequiredDone = required.every((s) => isDone(s))
  const doneCount = steps.filter((s) => isDone(s)).length

  async function unlock() {
    setError('')
    if (!allRequiredDone) {
      setError('Please complete the steps above first.')
      return
    }
    setBusy(true)
    const r = await requestAccess(progress)
    if (r.ok) onUnlock(r.exp)
    else { setError(r.error); setBusy(false) }
  }

  return (
    <div className="gate-shell">
      <div className="gate-card">
        <div className="gate-brand">
          <span className="nav-logo">MC</span>
          <span className="gate-brand-name">
            {gateConfig.brandName} · <em>{gateConfig.brandSub}</em>
          </span>
        </div>

        <h1>{gateConfig.title}</h1>
        <p className="gate-sub">{gateConfig.subtitle}</p>

        <div className="gate-progress" aria-hidden="true">
          <div
            className="gate-progress-bar"
            style={{ width: `${(doneCount / Math.max(1, steps.length)) * 100}%` }}
          />
        </div>

        <ol className="gate-steps">
          {steps.map((step, i) => {
            const opened = isOpened(step)
            const done = isDone(step)
            const armed = isArmed(step)
            return (
              <li key={step.id} className={`gate-step ${done ? 'is-done' : ''}`}>
                <div className="gate-step-head">
                  <span className="gate-step-no">{done ? '✓' : i + 1}</span>
                  <div>
                    <div className="gate-step-label">
                      {step.heading}
                      {step.optional && <span className="gate-optional">optional</span>}
                    </div>
                    <div className="gate-step-desc">{step.note}</div>
                  </div>
                </div>

                <div className="gate-step-actions">
                  <a
                    className={`btn gate-btn-wa ${done ? 'btn-ghost' : ''}`}
                    href={hrefFor(step)}
                    target="_blank"
                    rel="noopener noreferrer"
                    onClick={() => openStep(step)}
                  >
                    {step.action} →
                  </a>

                  <label
                    className={`gate-check ${done ? 'checked' : ''} ${armed ? '' : 'disabled'}`}
                    aria-disabled={!armed}
                  >
                    <input
                      type="checkbox"
                      checked={done}
                      disabled={!armed}
                      onChange={() => toggleDone(step)}
                    />
                    <span>
                      {armed
                        ? step.confirm
                        : opened
                          ? `One moment… ${secondsLeft(step)}s`
                          : 'Tap the button above first'}
                    </span>
                  </label>
                </div>
              </li>
            )
          })}
        </ol>

        {error && <p className="gate-error" role="alert">{error}</p>}

        <button
          className="btn btn-primary btn-lg gate-unlock"
          onClick={unlock}
          disabled={!allRequiredDone || busy}
        >
          {busy ? 'Setting you up…' : 'Enter the CBT Lab →'}
        </button>

        <p className="gate-note">
          Your access lasts 7 days on this device and renews in seconds. Your
          test progress, scores and saved sessions are never affected.
        </p>
      </div>
    </div>
  )
}
