import { useEffect, useRef, useState } from 'react'
import { gateConfig } from '../gateConfig.js'
import { deviceId, deviceLabel, redeemCode } from '../gateStore.js'
import { normalizeWhatsApp, displayWhatsApp } from '../phone.js'

/**
 * Multi-step access gate.
 *
 *   1. Save my contact      (mandatory first — nothing else unlocks until done)
 *   2. Follow the channel
 *   3. Request code on WhatsApp  (pre-typed message carrying their device ID)
 *   4. Paste code -> server verifies -> in for 7 days
 *
 * Each step only unlocks the next one, and link steps arm their confirm box
 * only after a dwell timer, so nobody can blind-tick through.
 */
export default function Gate({ onUnlock }) {
  const [saved, setSaved] = useState(false)      // step 1 confirmed
  const [followed, setFollowed] = useState(false) // step 2 confirmed
  const [requested, setRequested] = useState(false) // step 3 tapped
  const [armed, setArmed] = useState({})          // dwell timers per step
  const [opened, setOpened] = useState({})
  const [, setTick] = useState(0)
  const [code, setCode] = useState('')
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)
  const [copied, setCopied] = useState(false)
  const timers = useRef({})

  useEffect(() => {
    const id = setInterval(() => setTick((t) => t + 1), 500)
    return () => clearInterval(id)
  }, [])

  // MAGIC LINK: if the admin sent  .../#/?c=MAX-XXXXXX  the student just taps it
  // and we redeem automatically — no typing, no paste, no mistakes.
  useEffect(() => {
    const q = window.location.hash.split('?')[1]
    if (!q) return
    const c = new URLSearchParams(q).get('c')
    if (!c) return
    setCode(c)
    setSaved(true); setFollowed(true); setRequested(true)
    setBusy(true)
    redeemCode(c.trim()).then((r) => {
      // Clean the code out of the URL either way, so it is not left in history.
      try { window.history.replaceState(null, '', window.location.pathname + '#/') } catch {}
      if (r.ok) onUnlock(r.exp)
      else { setError(r.error); setBusy(false) }
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])
  useEffect(() => () => Object.values(timers.current).forEach(clearTimeout), [])

  const dev = deviceId()
  const label = deviceLabel()
  // Normalised so ANY format in gateConfig (0..., +234..., 234...) builds a
  // working wa.me link. Students never see a broken "chat not found" page.
  const wa = normalizeWhatsApp(gateConfig.whatsappNumber, gateConfig.defaultCountryCode)
  const waPretty = displayWhatsApp(gateConfig.whatsappNumber, gateConfig.defaultCountryCode)
  const dwell = gateConfig.dwellSeconds ?? 6

  // Pre-typed WhatsApp message carrying the device ID.
  const msg = `${gateConfig.requestWord} ${label}`
  const dmUrl = `https://wa.me/${wa}?text=${encodeURIComponent(msg)}`

  // vCard download so "save my contact" is one tap, not a manual copy.
  const vcard = [
    'BEGIN:VCARD', 'VERSION:3.0',
    `FN:${gateConfig.contactName}`,
    `N:${gateConfig.contactName};;;;`,
    `TEL;TYPE=CELL:+${wa}`,
    `NOTE:Max-codes CBT Lab access`,
    'END:VCARD',
  ].join('\n')
  const vcardUrl = `data:text/vcard;charset=utf-8,${encodeURIComponent(vcard)}`

  function open(step) {
    setOpened((o) => ({ ...o, [step]: Date.now() }))
    timers.current[step] = setTimeout(
      () => setArmed((a) => ({ ...a, [step]: true })),
      dwell * 1000
    )
  }

  function left(step) {
    const s = opened[step]
    if (!s) return dwell
    return Math.max(0, Math.ceil((dwell * 1000 - (Date.now() - s)) / 1000))
  }

  function copyId() {
    try {
      navigator.clipboard.writeText(label)
      setCopied(true)
      setTimeout(() => setCopied(false), 1800)
    } catch {}
  }

  async function submit() {
    setError('')
    if (!code.trim()) { setError('Paste the code you received on WhatsApp.'); return }
    setBusy(true)
    const r = await redeemCode(code.trim())
    if (r.ok) onUnlock(r.exp)
    else { setError(r.error); setBusy(false) }
  }

  const stepClass = (active, done) =>
    `gate-step ${done ? 'is-done' : ''} ${active ? 'is-active' : 'is-locked'}`

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

        <ol className="gate-steps">
          {/* ---------------- STEP 1 — save contact ---------------- */}
          <li className={stepClass(true, saved)}>
            <div className="gate-step-head">
              <span className="gate-step-no">{saved ? '✓' : '1'}</span>
              <div>
                <div className="gate-step-label">Save my contact first</div>
                <div className="gate-step-desc">
                  WhatsApp will not deliver my reply if my number is not saved.
                  Tap to download the contact card, then save it.
                </div>
              </div>
            </div>
            <div className="gate-step-actions">
              <a
                className="btn gate-btn-wa"
                href={vcardUrl}
                download="Max-codes-CBT.vcf"
                onClick={() => open('save')}
              >
                Save contact ({waPretty}) ↓
              </a>
              <label className={`gate-check ${saved ? 'checked' : ''} ${armed.save ? '' : 'disabled'}`}>
                <input
                  type="checkbox" checked={saved} disabled={!armed.save}
                  onChange={() => setSaved((v) => !v)}
                />
                <span>
                  {armed.save ? 'I have saved the contact'
                    : opened.save ? `Verifying… ${left('save')}s`
                    : 'Tap the button above first'}
                </span>
              </label>
            </div>
          </li>

          {/* ---------------- STEP 2 — follow channel ---------------- */}
          <li className={stepClass(saved, followed)}>
            <div className="gate-step-head">
              <span className="gate-step-no">{followed ? '✓' : '2'}</span>
              <div>
                <div className="gate-step-label">Follow our WhatsApp channel</div>
                <div className="gate-step-desc">
                  New question banks, updates and announcements land there first.
                </div>
              </div>
            </div>
            {saved ? (
              <div className="gate-step-actions">
                <a
                  className="btn gate-btn-wa" href={gateConfig.channelUrl}
                  target="_blank" rel="noopener noreferrer"
                  onClick={() => open('follow')}
                >
                  Open WhatsApp channel →
                </a>
                <label className={`gate-check ${followed ? 'checked' : ''} ${armed.follow ? '' : 'disabled'}`}>
                  <input
                    type="checkbox" checked={followed} disabled={!armed.follow}
                    onChange={() => setFollowed((v) => !v)}
                  />
                  <span>
                    {armed.follow ? 'I have followed the channel'
                      : opened.follow ? `Verifying… ${left('follow')}s`
                      : 'Tap the button above first'}
                  </span>
                </label>
              </div>
            ) : (
              <p className="gate-locked-note">🔒 Complete step 1 first</p>
            )}
          </li>

          {/* ---------------- STEP 3 — request code ---------------- */}
          <li className={stepClass(saved && followed, requested)}>
            <div className="gate-step-head">
              <span className="gate-step-no">{requested ? '✓' : '3'}</span>
              <div>
                <div className="gate-step-label">Request your personal code</div>
                <div className="gate-step-desc">
                  The message is already typed for you — just hit send. Your code
                  works on <strong>this phone only</strong>.
                </div>
              </div>
            </div>
            {saved && followed ? (
              <div className="gate-step-actions">
                <a
                  className="btn btn-primary gate-btn-wa" href={dmUrl}
                  target="_blank" rel="noopener noreferrer"
                  onClick={() => setRequested(true)}
                >
                  Send &ldquo;{gateConfig.requestWord}&rdquo; on WhatsApp →
                </a>
                <div className="gate-devid">
                  <span>Your device ID</span>
                  <code>{label}</code>
                  <button type="button" className="btn btn-ghost btn-sm" onClick={copyId}>
                    {copied ? 'Copied ✓' : 'Copy'}
                  </button>
                </div>
              </div>
            ) : (
              <p className="gate-locked-note">🔒 Complete steps 1 and 2 first</p>
            )}
          </li>
        </ol>

        {/* ---------------- STEP 4 — enter code ---------------- */}
        {saved && followed && requested && (
          <>
            <div className="gate-code">
              <label htmlFor="gate-code-input">Enter the code I sent you</label>
              <input
                id="gate-code-input" className="gate-input" type="text"
                placeholder="e.g. MAX-XXXXXX" value={code}
                onChange={(e) => { setCode(e.target.value); setError('') }}
                onKeyDown={(e) => { if (e.key === 'Enter') submit() }}
                autoComplete="off" spellCheck="false"
              />
            </div>

            {error && <p className="gate-error" role="alert">{error}</p>}

            <button
              className="btn btn-primary btn-lg gate-unlock"
              onClick={submit} disabled={!code.trim() || busy}
            >
              {busy ? 'Verifying…' : 'Unlock the CBT Lab →'}
            </button>
          </>
        )}

        <p className="gate-note">
          🔒 Codes are generated per phone and verified on our server — a code
          sent to someone else will never work here. Access lasts 7 days, then
          you just request a new code. <strong>Your test progress, scores and
          saved sessions are never affected.</strong>
        </p>
      </div>
    </div>
  )
}
