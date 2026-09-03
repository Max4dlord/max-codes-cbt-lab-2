import { useState, useEffect } from 'react'
import { useNavigate, Navigate, Link } from 'react-router-dom'
import { loadStudySession, saveStudySession } from '../progress.js'
import { topicMeta } from '../data.js'
import { hasTypedAnswer } from '../graders.js'
import RichText from './RichText.jsx'

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

// Topic deep dives for EEE 282 — shown whenever a topic has no summaryNotes of its own
const TOPIC_DEEP_DIVE = {
  'active-passive': `### The rule that settles every classification
An **active** part needs an external supply and can control current or deliver power gain
(diode, zener, LED, BJT, MOSFET, op-amp, SCR). A **passive** part only stores or dissipates energy
(R, L, C, potentiometer, LDR, thermistor, transformer).

### Symbols worth five marks each
- Diode: triangle (anode) against a bar (cathode); the painted **band** is the cathode.
- Zener: same, with a **Z-shaped** cathode bar; runs in reverse breakdown at $V_Z$.
- Electrolytic capacitor: **polarised** — long lead positive, striped side negative.
- Potentiometer: track on pins **1 and 3**, wiper on **pin 2**.
- NTC: temperature up, resistance **down**. LDR: resistance highest in **darkness**.`,

  'bjt-diagnostics': `### Two diodes sharing a terminal
- **NPN** — the two **anodes** meet at the base. **Red probe on the base → NPN.**
- **PNP** — the two **cathodes** meet at the base. **Black probe on the base → PNP.**

### Sequence
1. Find the pin that shows $\\approx 0.6-0.7\,\\text{V}$ to **both** others → base.
2. Probe polarity on that base gives the type.
3. Split emitter from collector with $V_{BE} > V_{BC}$ (5–15 mV). **Larger drop = emitter.**
4. C–E must read **OL** both ways. 0.000 V = shorted; no drop anywhere = open.`,

  'cro-controls': `### What each control really does
- **Time/Div** = seconds per horizontal division (the time axis).
- **Volts/Div** = volts per vertical division (the amplitude axis).
- **Trigger level** freezes a moving trace.
- **Vertical Position** slides the trace up/down without changing its amplitude.
- **Coupling**: DC = everything, AC = DC blocked by a series capacitor, GND = the true 0 V line.

### Before every measurement
Switch to **GND**, park the flat line on the centre graticule line with **Vertical Position**, then
switch back to **DC**. Now every reading has a known zero reference.`,

  'cro-calculations': `### The five formulas
$$V_{p\\text{-}p} = (\\text{div}) \\times (\\text{Volts/Div})$$
$$V_p = \\frac{V_{p\\text{-}p}}{2},\\text{ } V_{rms} = 0.707V_p,\\text{ } V_p = 1.414V_{rms}$$
$$T = (\\text{div per cycle}) \\times (\\text{Time/Div}),\\text{ } f = \\frac{1}{T}$$
$$\\phi = \\frac{\\text{shift div}}{\\text{div per cycle}} \\times 360^\\circ$$
$$\\frac{f_y}{f_x} = \\frac{\\text{horizontal tangencies}}{\\text{vertical tangencies}}$$

### Traps that cost marks
- Convert **ms → s before** you take $1/T$.
- RMS is $0.707 \\times$ **peak**, never $0.707 \\times$ peak-to-peak.
- A DC offset is the **midpoint** of the trace, not its peak.`
}



// Topic-level diagrams for EEE 282 (used only when the question has none of its own)
const TOPIC_IMAGES = {
  'active-passive': '/images/eee282/q02.svg',
  'bjt-diagnostics': '/images/eee282/q13.svg',
  'cro-controls': '/images/eee282/q25.svg',
  'cro-calculations': '/images/eee282/q24.svg',
}


export default function StudyRunner() {
  const navigate = useNavigate()
  const [session, setSession] = useState(() => loadStudySession())
  const [index, setIndex] = useState(session?.index ?? 0)
  const [showSolution, setShowSolution] = useState(false)
  const [revealed, setRevealed] = useState({})

  if (!session) return <Navigate to="/dashboard" replace />

  const questions = session.questionSet
  const total = questions.length
  const q = questions[index]
  const topicMetaEntry = (topicMeta[session.courseId] || []).find((t) => t.id === q.topicId) || {}
  const topicNote = topicMetaEntry.summaryNotes
  const topicLabel = topicMetaEntry.name || 'Mixed topics'
  const deepDive = topicNote || TOPIC_DEEP_DIVE[q.topicId] || `This topic covers ${q.topicId.replace(/-/g, ' ')}. Review the core definitions, formulas, and typical exam traps for this topic. Focus on understanding the *why* behind each option, not just memorizing the answer.`

  useEffect(() => {
    if (!session) return
    const next = { ...session, index }
    saveStudySession(next)
    setSession(next)
    setShowSolution(false)
  }, [index])

  function go(i) {
    if (i < 0 || i >= total) return
    setIndex(i)
  }

  function handleSeeExplanation() {
    setShowSolution(true)
    setRevealed(r => ({ ...r, [q.id]: true }))
  }

  function exitToDashboard() {
    navigate('/dashboard')
  }

  const pct = Math.round(((index + 1) / total) * 100)
  const topicImage = TOPIC_IMAGES[q.topicId]

  return (
    <div className="test-shell">
      <div className="test-topbar" style={{ background: 'linear-gradient(135deg, rgba(1,0,128,0.06), rgba(138,106,18,0.04))' }}>
        <div className="test-meta">
          <div>
            <div className="tm-title">{session.courseCode}{session.topicName ? ` · ${session.topicName}` : ' · Study Mode'} <span style={{ fontSize: 11, background: 'var(--primary)', color: '#fff', padding: '3px 8px', borderRadius: 999, marginLeft: 8, verticalAlign: 'middle' }}>STUDY MODE</span></div>
            <div className="tm-sub">Question {index + 1} of {total} · Correct answer already ticked · No timer</div>
          </div>
        </div>
        <div className="progress-wrap" style={{ minWidth: 180 }}>
          <div style={{ fontSize: 12, color: 'var(--muted)', fontWeight: 600 }}>PROGRESS</div>
          <div className="progress-bar"><div className="progress-fill" style={{ width: `${pct}%` }} /></div>
          <div style={{ fontSize: 11, color: 'var(--muted)', marginTop: 4 }}>{index + 1} / {total} · {Object.keys(revealed).length} explanations viewed</div>
        </div>
        <div className="flex gap-8">
          <button className="btn btn-ghost btn-sm" onClick={exitToDashboard}>Exit Study</button>
          <Link to="/dashboard" className="btn btn-primary btn-sm">New Study Set →</Link>
        </div>
      </div>

      <div className="test-body">
        <div className="qcard" style={{ borderLeft: '4px solid var(--primary)' }}>
          <div className="qhead">
            <span className="qindex">Study Question {index + 1} / {total}</span>
            <span className="qtopic">{topicLabel}</span>
          </div>
          <RichText text={q.question} className="qtext" />

          {q.image && (
            <div style={{ margin: '16px 0', padding: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)', borderRadius: 12, textAlign: 'center' }}>
              <img src={q.image} alt="Question diagram" style={{ maxWidth: '100%', maxHeight: 320, borderRadius: 8, border: '1px solid var(--border)' }} />
              <div style={{ fontSize: 12, color: 'var(--muted)', marginTop: 8 }}>Diagram for visual understanding — tap to zoom</div>
            </div>
          )}

          {topicImage && !q.image && (
            <div style={{ margin: '16px 0', padding: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)', borderRadius: 12, textAlign: 'center', opacity: 0.9 }}>
              <div style={{ fontSize: 12, color: 'var(--muted)', marginBottom: 8, fontWeight: 600 }}>📐 Topic Diagram — {topicLabel}</div>
              <img src={topicImage} alt={`${topicLabel} diagram`} style={{ maxWidth: '100%', maxHeight: 260, borderRadius: 8, border: '1px solid var(--border)' }} />
            </div>
          )}

          <div className="options">
            {q.options.map((opt, i) => {
              const isCorrect = i === q.correct
              return (
                <div
                  key={i}
                  className={`option ${isCorrect ? 'selected' : ''}`}
                  style={isCorrect ? { borderColor: 'var(--green)', background: 'var(--green-soft)', cursor: 'default' } : { cursor: 'default', opacity: 0.9 }}
                >
                  <span className="opt-key" style={isCorrect ? { background: 'var(--green)', color: '#fff', borderColor: 'var(--green)' } : {}}>{LETTERS[i]}</span>
                  <RichText text={opt} className="rt-opt" />
                  {isCorrect && <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--green)', background: '#fff', padding: '3px 8px', borderRadius: 999, border: '1px solid var(--green)' }}>✓ Correct</span>}
                </div>
              )
            })}
          </div>

          {hasTypedAnswer(q) && (
            <div className="typed-box study-typed">
              <div className="typed-label">✍️ Model written answer</div>
              <div className="typed-answer">{q.expected || q.options[q.correct]}</div>
              <div className="typed-hint">
                In the real exam you would write this out — the options above are here so you can
                check yourself in CBT format too.
              </div>
            </div>
          )}

          <div style={{ marginTop: 22, display: 'flex', gap: 12, flexWrap: 'wrap' }}>
            <button className="btn btn-primary" onClick={handleSeeExplanation} style={{ flex: 1, minWidth: 200 }}>
              {showSolution ? '✓ Explanation below — scroll down' : 'See Detailed Explanation →'}
            </button>
            <button className="btn btn-ghost" onClick={() => go(index + 1)} disabled={index === total - 1}>
              Next Question →
            </button>
          </div>

          <div className="ri-short" style={{ marginTop: 18, background: 'var(--card-2)' }}>
            <RichText text={'**Quick tip:** ' + q.short} className="rt-inline" />
          </div>

          {showSolution && (
            <div style={{ marginTop: 18, padding: 20, background: 'linear-gradient(135deg, rgba(1,0,128,0.06), rgba(138,106,18,0.04))', border: '1px solid var(--border)', borderRadius: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>📖 Study Mode — Very Detailed Explanation</div>
                <span className="qtopic" style={{ background: 'var(--green-soft)', color: 'var(--green)', borderColor: 'rgba(11,122,85,0.2)' }}>Correct: {LETTERS[q.correct]}. {q.options[q.correct]}</span>
              </div>
              <div className="panel-sol" style={{ background: '#fff' }}>
                <RichText text={q.solution} className="rt-block" />
                <div style={{ marginTop: 18, paddingTop: 18, borderTop: '1px dashed var(--border)' }}>
                  <div style={{ fontWeight: 700, color: 'var(--text)', marginBottom: 8 }}>
                    {topicNote
                      ? '📐 Topic Notes — Key Formulas, Abstractions & Exam Traps:'
                      : `📚 Deep Dive — More on ${topicLabel}:`}
                  </div>
                  <RichText text={deepDive} className="rt-block" />
                </div>
              </div>
              {(q.image || topicImage) && (
                <div style={{ marginTop: 16, padding: 12, background: '#fff', border: '1px solid var(--border)', borderRadius: 10, textAlign: 'center' }}>
                  <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--muted)', marginBottom: 8 }}>🖼️ Visual Reference — {topicLabel}</div>
                  <img src={q.image || topicImage} alt="Deep dive diagram" style={{ maxWidth: '100%', maxHeight: 320, borderRadius: 8 }} />
                </div>
              )}
              <div style={{ marginTop: 14, display: 'flex', gap: 10 }}>
                <button className="btn btn-ghost btn-sm" onClick={() => setShowSolution(false)}>Hide explanation</button>
                <button className="btn btn-primary btn-sm" onClick={() => go(index + 1)} disabled={index === total - 1}>Next →</button>
              </div>
            </div>
          )}

          <div className="qnav" style={{ marginTop: 24, borderTop: '1px solid var(--border)', paddingTop: 16 }}>
            <button className="btn btn-ghost" onClick={() => go(index - 1)} disabled={index === 0}>← Previous</button>
            <span style={{ fontSize: 12, color: 'var(--muted)' }}>Study Mode · No timer · Correct already ticked</span>
            {index < total - 1 ? (
              <button className="btn btn-primary" onClick={() => go(index + 1)}>Next →</button>
            ) : (
              <button className="btn btn-ghost" onClick={exitToDashboard}>Back to Dashboard</button>
            )}
          </div>
        </div>

        <div className="palette">
          <h4>Study Navigator</h4>
          <div className="palette-grid">
            {questions.map((qq, i) => {
              const cls = [
                'pcell',
                revealed[qq.id] ? 'answered' : '',
                i === index ? 'current' : ''
              ].filter(Boolean).join(' ')
              return (
                <button key={qq.id} className={cls} onClick={() => go(i)} title={`Question ${i + 1} ${revealed[qq.id] ? '(viewed)' : ''}`}>
                  {i + 1}
                </button>
              )
            })}
          </div>
          <div className="palette-legend">
            <span><span className="legend-dot" style={{ background: 'var(--green-soft)', border: '1px solid rgba(11,122,85,0.4)' }} />Viewed</span>
            <span><span className="legend-dot" style={{ background: 'var(--primary)' }} />Current</span>
          </div>
          <div style={{ marginTop: 18, padding: 12, background: 'var(--primary-soft)', borderRadius: 10, border: '1px solid rgba(1,0,128,0.12)' }}>
            <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)' }}>💡 How Study Mode works</div>
            <div style={{ fontSize: 12, color: 'var(--muted)', marginTop: 6, lineHeight: 1.5 }}>
              No timer. Correct answer is pre-ticked in green. Tap <strong>See Detailed Explanation</strong> for the very long, topic-focused deep dive — longer than Test Mode — with diagrams where needed.
            </div>
          </div>
          <p className="muted" style={{ fontSize: 12, marginTop: 12, lineHeight: 1.5 }}>
            Go at your own pace. No auto-save timer, no pressure.
          </p>
        </div>
      </div>
    </div>
  )
}
