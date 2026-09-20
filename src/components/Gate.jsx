import { useCallback, useEffect, useRef, useState } from 'react'
import { gateConfig } from '../gateConfig.js'
import {
  dmLinkUrl, stepUrl, fetchStepStatus, redeemCode, deviceLabel,
} from '../gateStore.js'

/**
 * Access gate — WhatsApp-bot flow.
 *
 * The student taps one button, WhatsApp opens with the message already typed,
 * they press send, and a bot replies within seconds with a tap-to-enter link.
 * Nobody waits on the admin, and there is no code hunting in a pinned post.
 *
 * The two community asks (partner channel, LinkedIn) sit below as genuine,
 * clearly-optional requests — because channel membership is not verifiable by
 * anybody, and pretending otherwise would just be theatre.
 */
export default function Gate({ onUnlock }) {
  const asks = gateConfig.steps || []

  const [code, setCode] = useState('')
  const [status, setStatus] = useState(null)
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)
  const [messaged, setMessaged] = useState(false)
  const pollRef = useRef(null)

  const refresh = useCallback(async () => {
    const s = await fetchStepStatus()
    if (s) setStatus(s)
  }, [])

  useEffect(() => {
    refresh()
    const onFocus = () => refresh()
    window.addEventListener('focus', onFocus)
    return () => window.removeEventListener('focus', onFocus)
  }, [refresh])

  useEffect(() => () => clearInterval(pollRef.current), [])

  // Magic link: the bot's reply contains .../#/?c=CODE, so tapping it lands
  // here and redeems with no typing at all.
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

  async function submitCode() {
    setError('')
    if (!code.trim()) { setError('Paste the code the bot sent you.'); return }
    setBusy(true)
    const r = await redeemCode(code.trim())
    if (r.ok) onUnlock(r.exp)
    else { setError(r.error); setBusy(false) }
  }

  const askState = (id) => (status && status[id]) || { visited: false, ready: false }

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

        {/* ---------------- the one required action ---------------- */}
        <div className="gate-primary">
          <div className="gate-primary-head">
            <span className="gate-step-no">1</span>
            <div>
              <div className="gate-step-label">Get your access on WhatsApp</div>
              <div className="gate-step-desc">
                Tap below — the message is already written. Just press send and
                our assistant replies instantly with your personal entry link.
              </div>
            </div>
          </div>

          <a
            className="btn btn-primary btn-lg gate-wa-cta"
            href={dmLinkUrl()}
            target="_blank"
            rel="noopener noreferrer"
            onClick={() => setMessaged(true)}
          >
            Message us on WhatsApp →
          </a>

          {messaged && (
            <p className="gate-hint-line">
              Sent it? Your reply arrives in a few seconds — just tap the link
              in it and you are in. You can also paste the code below.
            </p>
          )}
        </div>

        {/* ---------------- manual code fallback ---------------- */}
        <details className="gate-fallback" open={messaged}>
          <summary>Prefer to type the code?</summary>
          <div className="gate-code">
            <input
              className="gate-input"
              type="text"
              placeholder="e.g. EEE-XXXXXX"
              value={code}
              onChange={(e) => { setCode(e.target.value); setError('') }}
              onKeyDown={(e) => { if (e.key === 'Enter') submitCode() }}
              autoComplete="off"
              spellCheck="false"
            />
            <button
              className="btn btn-primary"
              onClick={submitCode}
              disabled={!code.trim() || busy}
            >
              {busy ? 'Checking…' : 'Enter'}
            </button>
          </div>
        </details>

        {error && <p className="gate-error" role="alert">{error}</p>}

        {/* ---------------- optional community asks ---------------- */}
        {asks.length > 0 && (
          <div className="gate-asks">
            <div className="gate-asks-head">
              A small favour, if you don’t mind 💚
              <span className="gate-optional">optional</span>
            </div>
            {asks.map((ask) => {
              const s = askState(ask.id)
              return (
                <div key={ask.id} className="gate-ask">
                  <div>
                    <div className="gate-ask-title">{ask.heading}</div>
                    <div className="gate-ask-note">{ask.note}</div>
                  </div>
                  <a
                    className={`btn btn-ghost btn-sm ${s.visited ? 'is-done' : ''}`}
                    href={stepUrl(ask.id)}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {s.visited ? 'Thank you ✓' : ask.action}
                  </a>
                </div>
              )
            })}
          </div>
        )}

        <p className="gate-note">
          Access lasts 7 days on this device and renews in seconds. Your test
          progress, scores and saved sessions are never affected.
        </p>

        <p className="gate-tiny">Your ID: {deviceLabel()}</p>
      </div>
    </div>
  )
}
