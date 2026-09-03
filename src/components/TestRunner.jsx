import { useEffect, useRef, useState } from 'react'
import { useNavigate, Navigate, Link } from 'react-router-dom'
import Timer from './Timer.jsx'
import RichText from './RichText.jsx'
import Diagram from './Diagram.jsx'
import TermsDrawer from './TermsDrawer.jsx'
import { loadSession, saveSession, clearSession, saveResults } from '../progress.js'
import { gradeTyped, hasTypedAnswer, typedPrompt } from '../graders.js'

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

export default function TestRunner() {
  const navigate = useNavigate()
  const [session, setSession] = useState(() => loadSession())

  // Live state, hydrated from the saved session.
  const [index, setIndex] = useState(session?.index ?? 0)
  const [answers, setAnswers] = useState(session?.answers ?? {})
  const [typed, setTyped] = useState(session?.typed ?? {})
  const [flagged, setFlagged] = useState(session?.flagged ?? [])
  const [remaining, setRemaining] = useState(session?.remainingSec ?? 0)
  const [paused, setPaused] = useState(session?.paused ?? false)
  const [showExit, setShowExit] = useState(false)
  const submittedRef = useRef(false)

  // If there's no session at all, bounce to the dashboard.
  if (!session) return <Navigate to="/dashboard" replace />

  const questions = session.questionSet
  const total = questions.length
  const q = questions[index]
  const answeredCount = questions.filter(
    (qq) => answers[qq.id] !== undefined || String(typed[qq.id] || '').trim()
  ).length

  // ----- Countdown effect -----
  useEffect(() => {
    if (paused || submittedRef.current) return
    if (remaining <= 0) {
      submitTest(true)
      return
    }
    const t = setTimeout(() => setRemaining((r) => r - 1), 1000)
    return () => clearTimeout(t)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [remaining, paused])

  // ----- Persist session on every change -----
  useEffect(() => {
    if (submittedRef.current) return
    setSession((prev) => {
      if (!prev) return prev
      const next = { ...prev, index, answers, typed, flagged, remainingSec: remaining, paused }
      saveSession(next)
      return next
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [index, answers, typed, flagged, remaining, paused])

  function selectOption(optIndex) {
    if (paused) return
    // Choosing an option clears any typed answer so the two never conflict.
    setTyped((t) => ({ ...t, [q.id]: '' }))
    setAnswers((a) => ({ ...a, [q.id]: optIndex }))
  }

  function setTypedAnswer(value) {
    if (paused) return
    setTyped((t) => ({ ...t, [q.id]: value }))
  }

  function go(i) {
    if (i < 0 || i >= total) return
    setIndex(i)
  }

  function toggleFlag() {
    setFlagged((f) => (f.includes(q.id) ? f.filter((x) => x !== q.id) : [...f, q.id]))
  }

  function togglePause() {
    setPaused((p) => !p)
  }

  function exitToDashboard() {
    // Progress is already saved by the persist effect; just leave.
    navigate('/dashboard')
  }

  function submitTest(auto = false) {
    if (submittedRef.current) return
    if (!auto) {
      const ok = window.confirm('Submit this test? You will see your score and full solutions.')
      if (!ok) return
    }
    submittedRef.current = true

    const timeUsedSec = session.durationSec - remaining
    let correctCount = 0
    let wrongCount = 0
    let unanswered = 0

    const items = questions.map((qq) => {
      const ua = answers[qq.id]
      const tw = String(typed[qq.id] || '').trim()
      let status
      let typedResult = null

      if (tw) {
        // A typed answer always takes precedence over the picked option.
        typedResult = gradeTyped(qq, tw)
        status = typedResult.ok ? 'ok' : 'bad'
        if (typedResult.ok) correctCount++
        else wrongCount++
      } else if (ua === undefined || ua === null) {
        status = 'skip'
        unanswered++
      } else if (ua === qq.correct) {
        status = 'ok'
        correctCount++
      } else {
        status = 'bad'
        wrongCount++
      }

      return {
        id: qq.id,
        topicId: qq.topicId,
        question: qq.question,
        options: qq.options,
        diagram: qq.diagram,
        diagramCaption: qq.diagramCaption,
        terms: qq.terms,
        correct: qq.correct,
        userAnswer: ua,
        typedAnswer: tw || undefined,
        typedOk: typedResult ? typedResult.ok : null,
        typedDetail: typedResult ? typedResult.detail : '',
        expected: qq.expected,
        short: qq.short,
        solution: qq.solution,
        status
      }
    })

    const results = {
      v: 1,
      courseCode: session.courseCode,
      courseTitle: session.courseTitle,
      topicName: session.topicName,
      mode: session.mode,
      total,
      correctCount,
      wrongCount,
      unanswered,
      durationSec: session.durationSec,
      timeUsedSec,
      items,
      finishedAt: Date.now()
    }

    saveResults(results)
    clearSession()
    navigate('/results')
  }

  const pct = Math.round(((index + 1) / total) * 100)

  return (
    <div className="test-shell">
      {/* ---------- Top bar ---------- */}
      <div className="test-topbar">
        <div className="test-meta">
          <div>
            <div className="tm-title">{session.courseCode}{session.topicName ? ` · ${session.topicName}` : ' · Full course'}</div>
            <div className="tm-sub">Question {index + 1} of {total} · {answeredCount} answered</div>
          </div>
        </div>
        <div className="progress-wrap">
          <Timer remainingSec={remaining} paused={paused} onTogglePause={togglePause} />
          <div className="progress-bar"><div className="progress-fill" style={{ width: `${pct}%` }} /></div>
        </div>
        <div className="flex gap-8">
          <button className="btn btn-ghost btn-sm" onClick={() => setShowExit(true)}>Exit</button>
          <button className="btn btn-primary btn-sm" onClick={() => submitTest(false)}>Submit</button>
        </div>
      </div>

      {/* ---------- Body ---------- */}
      <div className="test-body">
        <div className="qcard">
          <div className="qhead">
            <span className="qindex">Question {index + 1} / {total}</span>
            <span className="qtopic">{session.topicName || 'Mixed topics'}</span>
          </div>
          <RichText text={q.question} className="qtext" />

          <Diagram svg={q.diagram} caption={q.diagramCaption} />

          <TermsDrawer terms={q.terms} />

          <div className="options">
            {q.options.map((opt, i) => (
              <div
                key={i}
                className={`option ${answers[q.id] === i ? 'selected' : ''}`}
                onClick={() => selectOption(i)}
              >
                <span className="opt-key">{LETTERS[i]}</span>
                <RichText text={opt} className="rt-opt" />
              </div>
            ))}
          </div>

          {hasTypedAnswer(q) && (
            <div className="typed-box">
              <div className="typed-label">
                ✍️ Type your answer — just like the written exam
              </div>
              <div className="typed-row">
                <input
                  className="typed-input"
                  type="text"
                  inputMode="decimal"
                  autoComplete="off"
                  placeholder={q.type === 'calc' ? 'e.g. 20, 10, 7.07' : 'Your answer in your own words…'}
                  value={typed[q.id] || ''}
                  disabled={paused}
                  onChange={(e) => setTypedAnswer(e.target.value)}
                />
                {typed[q.id] ? (
                  <button className="btn btn-ghost btn-sm" onClick={() => setTypedAnswer('')} disabled={paused}>
                    Clear
                  </button>
                ) : null}
              </div>
              <div className="typed-hint">{typedPrompt(q)}</div>
            </div>
          )}

          <div className="qnav">
            <button className="btn btn-ghost" onClick={() => go(index - 1)} disabled={index === 0}>← Previous</button>
            <button className="flag-btn" onClick={toggleFlag} style={{ padding: '10px 16px' }}>
              {flagged.includes(q.id) ? '🚩 Flagged' : '🏳️ Flag for review'}
            </button>
            {index < total - 1 ? (
              <button className="btn btn-primary" onClick={() => go(index + 1)}>Next →</button>
            ) : (
              <button className="btn btn-primary" onClick={() => submitTest(false)}>Finish & submit →</button>
            )}
          </div>
        </div>

        {/* ---------- Palette ---------- */}
        <div className="palette">
          <h4>Question palette</h4>
          <div className="palette-grid">
            {questions.map((qq, i) => {
              const cls = [
                'pcell',
                (answers[qq.id] !== undefined || String(typed[qq.id] || '').trim()) ? 'answered' : '',
                flagged.includes(qq.id) ? 'flagged' : '',
                i === index ? 'current' : ''
              ].filter(Boolean).join(' ')
              return (
                <button key={qq.id} className={cls} onClick={() => go(i)} title={`Question ${i + 1}`}>
                  {i + 1}
                </button>
              )
            })}
          </div>
          <div className="palette-legend">
            <span><span className="legend-dot" style={{ background: 'var(--green-soft)', border: '1px solid rgba(61,186,140,0.4)' }} />Answered</span>
            <span><span className="legend-dot" style={{ background: 'var(--primary)' }} />Current</span>
            <span><span className="legend-dot" style={{ border: '1px solid var(--amber)' }} />Flagged</span>
          </div>
          <button className="btn btn-primary btn-sm" style={{ width: '100%', marginTop: 18 }} onClick={() => submitTest(false)}>
            Submit test
          </button>
          <p className="muted" style={{ fontSize: 12, marginTop: 12, lineHeight: 1.5 }}>
            Your answers, timer & position auto-save. Exiting is safe — resume anytime.
          </p>
        </div>
      </div>

      {/* ---------- Exit confirm ---------- */}
      {showExit && (
        <div className="overlay" onClick={() => setShowExit(false)}>
          <div className="panel" onClick={(e) => e.stopPropagation()} style={{ width: 'min(420px, 100%)' }}>
            <div className="panel-head">
              <h3>Leave the test?</h3>
              <button className="btn btn-ghost btn-sm" onClick={() => setShowExit(false)}>✕</button>
            </div>
            <p className="muted">
              Your progress (answers, timer, current question) is already saved. You can resume this exact
              test from the dashboard or the navbar whenever you're ready.
            </p>
            <div className="flex gap-8" style={{ marginTop: 18 }}>
              <button className="btn btn-primary" onClick={exitToDashboard}>Save & exit</button>
              <button className="btn btn-ghost" onClick={() => setShowExit(false)}>Keep practising</button>
            </div>
            <Link to="/dashboard" className="muted" style={{ display: 'block', marginTop: 14, fontSize: 13 }}>Go to dashboard</Link>
          </div>
        </div>
      )}
    </div>
  )
}
