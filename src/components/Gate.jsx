import { useCallback, useEffect, useRef, useState } from 'react'
import { gateConfig } from '../gateConfig.js'
import { stepUrl, fetchStepStatus, requestAccess, redeemCode } from '../gateStore.js'

/**
 * Access gate.
 *
 * The important design change: there are NO self-certifying checkboxes. A step
 * is marked complete only because the SERVER recorded the visitor passing
 * through /api/go on the way to the destination. The UI simply reflects that
 * server state, so clicking around in DevTools changes nothing that matters.
 *
 * Other rules this component follows:
 *  - Nothing admin-facing: no phone number, no device id, no admin link.
 *  - Progress survives redirects and reloads, because the evidence is a
 *    server-side cookie rather than React state.
 *  - Steps read as friendly requests; optional ones never block access.
 */
export default function Gate({ onUnlock }) {
  const steps = gateConfig.steps || []
  const required = steps.filter((s) => !s.optional)

  const [status, setStatus] = useState(null)   // server truth
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)
  const pollRef = useRef(null)

  const refresh = useCallback(async () => {
    const s = await fetchStepStatus()
    if (s) setStatus(s)
    setLoading(false)
    return s
  }, [])

  // Initial read, plus a re-read whenever they come back to the tab — that is
  // the moment they return from WhatsApp or LinkedIn.
  useEffect(() => {
    refresh()
    const onFocus = () => refresh()
    const onVis = () => { if (!document.hidden) refresh() }
    window.addEventListener('focus', onFocus)
    document.addEventListener('visibilitychange', onVis)
    return () => {
      window.removeEventListener('focus', onFocus)
      document.removeEventListener('visibilitychange', onVis)
    }
  }, [refresh])

  // While any step is visited-but-still-counting-down, poll so the button
  // arms by itself without the visitor having to do anything.
  useEffect(() => {
    const waiting = status && Object.values(status).some((s) => s.visited && !s.ready)
    clearInterval(pollRef.current)
    if (waiting) pollRef.current = setInterval(refresh, 1500)
    return () => clearInterval(pollRef.current)
  }, [status, refresh])

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

  const st = (step) => (status && status[step.id]) || { visited: false, ready: false, waitMs: 0 }
  const allRequiredReady = required.every((s) => st(s).ready)
  const doneCount = steps.filter((s) => st(s).ready).length

  async function unlock() {
    setError('')
    setBusy(true)
    const r = await requestAccess()
    if (r.ok) { onUnlock(r.exp); return }
    setError(r.error)
    setBusy(false)
    refresh()
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
            const s = st(step)
            const secs = Math.ceil((s.waitMs || 0) / 1000)
            return (
              <li key={step.id} className={`gate-step ${s.ready ? 'is-done' : ''}`}>
                <div className="gate-step-head">
                  <span className="gate-step-no">{s.ready ? '✓' : i + 1}</span>
                  <div>
                    <div className="gate-step-label">
                      {step.heading}
                      {step.optional && <span className="gate-optional">optional</span>}
                    </div>
                    <div className="gate-step-desc">{step.note}</div>
                  </div>
                </div>

                <div className="gate-step-actions">
                  {/* Goes to our own server first, which records the visit and
                      then redirects. Not a normal outbound link. */}
                  <a
                    className={`btn gate-btn-wa ${s.ready ? 'btn-ghost' : ''}`}
                    href={stepUrl(step.id)}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {s.ready ? `${step.action} again` : step.action} →
                  </a>

                  <span className={`gate-state ${s.ready ? 'ok' : s.visited ? 'waiting' : ''}`}>
                    {loading
                      ? 'Checking…'
                      : s.ready
                        ? step.confirm
                        : s.visited
                          ? `Confirming… ${secs}s`
                          : 'Not yet done'}
                  </span>
                </div>
              </li>
            )
          })}
        </ol>

        {error && <p className="gate-error" role="alert">{error}</p>}

        <button
          className="btn btn-primary btn-lg gate-unlock"
          onClick={unlock}
          disabled={!allRequiredReady || busy || loading}
        >
          {busy ? 'Setting you up…' : 'Enter the CBT Lab →'}
        </button>

        {!allRequiredReady && !loading && (
          <p className="gate-hint-line">
            Tap each button above to continue — we confirm it automatically when
            you come back.
          </p>
        )}

        <p className="gate-note">
          Your access lasts 7 days on this device and renews in seconds. Your
          test progress, scores and saved sessions are never affected.
        </p>
      </div>
    </div>
  )
}
