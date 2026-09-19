import { useState } from 'react'

/**
 * Admin console at  #/admin-code
 *
 * A student DMs you:  "ACCESS A1B2C3-D4E5F6"
 * You paste that ID here, hit Generate, and copy the ready-made reply.
 * The admin key is checked on the SERVER — it is not in the bundle.
 */
export default function AdminCode() {
  const [adminKey, setAdminKey] = useState('')
  const [raw, setRaw] = useState('')
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)
  const [copied, setCopied] = useState('')
  const [notConfigured, setNotConfigured] = useState('')

  // Accepts "ACCESS A1B2C3-D4E5F6", "A1B2C3-D4E5F6" or the raw id.
  function parseId(text) {
    const t = String(text || '').trim()
    const m = t.match(/([A-Za-z0-9]{6})-?([A-Za-z0-9]{6})/)
    if (m) return (m[1] + m[2]).toLowerCase()
    const bare = t.replace(/[^A-Za-z0-9]/g, '')
    return bare.length >= 8 ? bare.toLowerCase() : ''
  }

  async function generate() {
    setError(''); setResult(null); setNotConfigured('')
    const deviceId = parseId(raw)
    if (!deviceId) { setError('Could not read a device ID from that text.'); return }
    setBusy(true)
    try {
      const r = await fetch('/api/admin-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ adminKey, deviceId }),
      })
      const data = await r.json()
      if (data.ok) setResult(data)
      else if (r.status === 503) setNotConfigured(data.error || 'Server not configured.')
      else setError(data.error || 'Failed.')
    } catch {
      setError('Network error. Are you online?')
    }
    setBusy(false)
  }

  function copy(text, tag) {
    try {
      navigator.clipboard.writeText(text)
      setCopied(tag); setTimeout(() => setCopied(''), 1800)
    } catch {}
  }

  // One-tap magic link: student taps it and the app redeems the code itself.
  const magicLink = result
    ? `${window.location.origin}/#/?c=${encodeURIComponent(result.code)}`
    : ''

  const reply = result
    ? `Here is your access ✅\n\nJust tap this link and you are in:\n${magicLink}\n\nOr enter this code manually: ${result.code}\n\nWorks on your phone only. Valid for 7 days. Enjoy 💪`
    : ''

  return (
    <div className="gate-shell">
      <div className="gate-card">
        <h1>Admin — issue an access code</h1>
        <p className="gate-sub">
          Paste the student&rsquo;s WhatsApp message (or just their device ID) below.
        </p>

        <div className="gate-code">
          <label htmlFor="admin-key">Admin key</label>
          <input
            id="admin-key" className="gate-input" type="password"
            value={adminKey} placeholder="Your admin key"
            onChange={(e) => setAdminKey(e.target.value)}
            autoComplete="off"
          />
        </div>

        <div className="gate-code">
          <label htmlFor="admin-dev">Student message / device ID</label>
          <input
            id="admin-dev" className="gate-input" type="text"
            value={raw} placeholder="ACCESS A1B2C3-D4E5F6"
            onChange={(e) => setRaw(e.target.value)}
            onKeyDown={(e) => { if (e.key === 'Enter') generate() }}
            autoComplete="off" spellCheck="false"
          />
        </div>

        {notConfigured && (
          <div className="gate-error" role="alert" style={{ textAlign: 'left', lineHeight: 1.6 }}>
            <strong>Setup needed.</strong> {notConfigured}
            <br /><br />
            Go to <strong>Vercel → this project → Settings → Environment
            Variables</strong> and add <code>GATE_SECRET</code>,{' '}
            <code>ADMIN_KEY</code> and <code>CODE_PREFIX</code> (tick Production,
            Preview and Development), then <strong>redeploy</strong>.
          </div>
        )}

        {error && <p className="gate-error" role="alert">{error}</p>}

        <button
          className="btn btn-primary btn-lg gate-unlock"
          onClick={generate} disabled={busy || !adminKey || !raw}
        >
          {busy ? 'Generating…' : 'Generate code'}
        </button>

        {result && (
          <div style={{ marginTop: 20 }}>
            <div style={{
              fontSize: '1.9rem', fontWeight: 800, letterSpacing: '2px',
              textAlign: 'center', padding: '16px', borderRadius: '12px',
              background: 'rgba(0,0,0,.06)',
            }}>
              {result.code}
            </div>

            <a
              className="btn btn-primary btn-lg"
              style={{ display: 'block', textAlign: 'center', marginTop: 12 }}
              href={`https://wa.me/?text=${encodeURIComponent(reply)}`}
              target="_blank" rel="noopener noreferrer"
            >
              Send on WhatsApp →
            </a>

            <div style={{ display: 'flex', gap: 8, marginTop: 10, flexWrap: 'wrap' }}>
              <button className="btn btn-ghost" onClick={() => copy(result.code, 'code')}>
                {copied === 'code' ? 'Copied ✓' : 'Copy code'}
              </button>
              <button className="btn btn-ghost" onClick={() => copy(magicLink, 'link')}>
                {copied === 'link' ? 'Copied ✓' : 'Copy link'}
              </button>
              <button className="btn btn-primary" onClick={() => copy(reply, 'reply')}>
                {copied === 'reply' ? 'Copied ✓' : 'Copy full reply'}
              </button>
            </div>

            <p className="gate-note" style={{ marginTop: 12 }}>
              Device: <code>{result.deviceId}</code><br />
              This code stops being issuable after{' '}
              {new Date(result.expiresAt).toLocaleString()}, but once the student
              redeems it they keep access for a full 7 days.
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
