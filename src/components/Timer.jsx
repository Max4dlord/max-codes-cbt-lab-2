import { formatTime } from '../utils.js'

export default function Timer({ remainingSec, paused, onTogglePause }) {
  const low = remainingSec <= 30
  return (
    <div className={`timer ${low ? 'timer-low' : ''}`}>
      <div className="timer-time">{formatTime(remainingSec)}</div>
      <button className="btn btn-ghost btn-sm" onClick={onTogglePause}>
        {paused ? '▶ Resume' : '⏸ Pause'}
      </button>
      {paused && <span className="paused-tag">Paused</span>}
    </div>
  )
}
