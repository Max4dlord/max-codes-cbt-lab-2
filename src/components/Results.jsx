import { useState } from 'react'
import { Link, Navigate } from 'react-router-dom'
import { loadResults, clearResults } from '../progress.js'
import { formatTime } from '../utils.js'
import SolutionPanel from './SolutionPanel.jsx'
import RichText from './RichText.jsx'

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

export default function Results() {
  const [results, setResults] = useState(() => loadResults())
  const [openId, setOpenId] = useState(null)
  const [expandAll, setExpandAll] = useState(false)

  if (!results) return <Navigate to="/dashboard" replace />

  const { total, correctCount, wrongCount, unanswered, durationSec, timeUsedSec, items } = results
  const pct = total ? Math.round((correctCount / total) * 100) : 0
  const passed = pct >= 50
  const ringC = 2 * Math.PI * 70
  const ringOffset = ringC * (1 - pct / 100)
  const stroke = passed ? '#3BAA83' : '#E05252'
  const topicName = results.topicName

  const openItem = items.find((i) => i.id === openId) || null

  function retake() {
    clearResults()
    setResults(null)
  }

  return (
    <div className="results-shell">
      {/* ---------- Score summary ---------- */}
      <div className="score-card">
        <div className="score-ring">
          <svg width="160" height="160" viewBox="0 0 160 160">
            <circle className="ring-bg" cx="80" cy="80" r="70" />
            <circle
              className="ring-fg" cx="80" cy="80" r="70" stroke={stroke}
              strokeDasharray={ringC} strokeDashoffset={ringOffset}
            />
          </svg>
          <div className="ring-val">{pct}%</div>
        </div>
        <h2>{passed ? 'Nice work! 🎉' : 'Keep practising 💪'}</h2>
        <p className="verdict">
          {results.courseCode}{topicName ? ` · ${topicName}` : ' · Full course'} ·
          {' '}You scored <strong>{correctCount}</strong> out of <strong>{total}</strong>.
        </p>

        <div className="score-stats">
          <div className="score-stat"><div className="ss-num ok">{correctCount}</div><div className="ss-lbl">Correct</div></div>
          <div className="score-stat"><div className="ss-num bad">{wrongCount}</div><div className="ss-lbl">Wrong</div></div>
          <div className="score-stat"><div className="ss-num skip">{unanswered}</div><div className="ss-lbl">Skipped</div></div>
          <div className="score-stat"><div className="ss-num">{formatTime(timeUsedSec)}</div><div className="ss-lbl">Time used</div></div>
          <div className="score-stat"><div className="ss-num">{formatTime(durationSec)}</div><div className="ss-lbl">Allowed</div></div>
        </div>

        <div className="results-actions">
          <Link to="/dashboard" className="btn btn-primary" onClick={retake}>Take another test →</Link>
          <Link to="/dashboard" className="btn btn-ghost">Back to dashboard</Link>
        </div>
      </div>

      {/* ---------- Review ---------- */}
      <div className="page-head" style={{ marginBottom: 18 }}>
        <h1 style={{ fontSize: 24 }}>Review & solutions</h1>
        <p>Every question with a short explanation. Tap “Show full explanation” for the complete worked solution. Where you typed an answer instead of picking an option, your typed value is what was marked.</p>
      </div>

      <div className="flex" style={{ justifyContent: 'flex-end', marginBottom: 14 }}>
        <button className="btn btn-ghost btn-sm" onClick={() => setExpandAll((x) => !x)}>
          {expandAll ? 'Collapse all' : 'Expand all explanations'}
        </button>
      </div>

      <div className="review-list">
        {items.map((item, i) => {
          const statusLabel = item.status === 'ok' ? 'Correct' : item.status === 'bad' ? 'Incorrect' : 'Skipped'
          const showFull = expandAll
          return (
            <div className={`review-item ${item.status === 'ok' ? 'ok' : item.status === 'bad' ? 'bad' : 'skip'}`} key={item.id}>
              <div className="ri-head">
                <div className="ri-q"><span className="muted">Q{i + 1}.</span> <RichText text={item.question} className="rt-inline" /></div>
                <span className={`ri-status ${item.status}`}>{statusLabel}</span>
              </div>

              <div className="ri-opts">
                {item.options.map((opt, oi) => {
                  const isCorrect = oi === item.correct
                  const isUserWrong = item.userAnswer === oi && oi !== item.correct
                  const cls = isCorrect ? 'is-correct' : isUserWrong ? 'is-wrong' : ''
                  return (
                    <div className={`ri-opt ${cls}`} key={oi}>
                      <strong>{LETTERS[oi]}.</strong> <RichText text={opt} className="rt-inline" />
                      {isCorrect && <span style={{ marginLeft: 'auto' }}>✓ correct</span>}
                      {isUserWrong && <span style={{ marginLeft: 'auto' }}>your answer</span>}
                    </div>
                  )
                })}
                {item.userAnswer === undefined && (
                  <div className="ri-opt" style={{ color: 'var(--muted)' }}><em>You didn't answer this question.</em></div>
                )}
              </div>

              {item.typedAnswer && (
                <div className={`ri-typed ${item.typedOk ? 'ok' : 'bad'}`}>
                  <div className="ri-typed-head">
                    You typed: <strong>{item.typedAnswer}</strong>
                    <span className={`ri-typed-tag ${item.typedOk ? 'ok' : 'bad'}`}>
                      {item.typedOk ? '✓ marked correct' : '✗ marked incorrect'}
                    </span>
                  </div>
                  {item.expected && (
                    <div className="ri-typed-exp">Model answer: {item.expected}</div>
                  )}
                  {item.typedDetail && <div className="ri-typed-detail">{item.typedDetail}</div>}
                </div>
              )}

              <div className="ri-short">
                <strong>{item.status === 'ok' ? "Why it's right: " : "Why it's wrong: "}</strong>{' '}
                <RichText text={item.short} className="rt-inline" />
              </div>

              {showFull && (
                <RichText text={item.solution} className="panel-sol" style={{ marginTop: 0, marginBottom: 14 }} />
              )}

              <div className="ri-actions">
                <button className="btn btn-ghost btn-sm" onClick={() => setOpenId(item.id)}>
                  📖 Show full explanation
                </button>
              </div>
            </div>
          )
        })}
      </div>

      <SolutionPanel item={openItem} topicName={topicName} onClose={() => setOpenId(null)} />
    </div>
  )
}
