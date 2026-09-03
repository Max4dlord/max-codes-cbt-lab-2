import { TELEGRAM_URL } from '../utils.js'
import RichText from './RichText.jsx'
import TermsDrawer from './TermsDrawer.jsx'

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

export default function SolutionPanel({ item, topicName, onClose }) {
  if (!item) return null
  return (
    <div className="overlay" onClick={onClose}>
      <div className="panel" onClick={(e) => e.stopPropagation()}>
        <div className="panel-head">
          <h3>Full solution</h3>
          <button className="btn btn-ghost btn-sm" onClick={onClose}>✕ Close</button>
        </div>

        <div className="p-topic" style={{ display: 'inline-block', marginBottom: 14 }}>
          {topicName || 'Mixed topics'}
        </div>

        <RichText text={item.question} className="panel-q" />

        <TermsDrawer terms={item.terms} />

        <div className="panel-ans">
          Correct answer: <strong>{LETTERS[item.correct]}. {item.options[item.correct]}</strong>
        </div>

        <div className="panel-label">Step-by-step working</div>
        <RichText text={item.solution} />

        <div className="panel-foot">
          <button className="btn btn-primary" onClick={onClose}>Back to review</button>
          {TELEGRAM_URL && (
            <a className="btn btn-ghost" href={TELEGRAM_URL} target="_blank" rel="noreferrer">
              Discuss in Telegram →
            </a>
          )}
        </div>
        <p className="hint" style={{ marginTop: 18 }}>
          This opens as an overlay — your results and progress are never disturbed.
          {TELEGRAM_URL
            ? ' The Telegram button opens in a new tab so nothing here is lost.'
            : ' Set TELEGRAM_URL in src/utils.js to add an optional "Discuss in Telegram" button.'}
        </p>
      </div>
    </div>
  )
}
