import { useEffect, useMemo, useRef, useState } from 'react'
import { componentSymbols } from '../data.js'

// ---------------------------------------------------------------------------
// ComponentsTableModal — the EEE 282 active / passive component reference.
//
// Visibility is driven with plain useState: the parent view owns `open`
// (it is toggled by the "View Components Table" button in Study Mode and in
// Review), this component mirrors it locally so it can close itself from the
// backdrop, the ✕ button or the Escape key. No portal, no library — just a
// fixed overlay styled from src/styles.css.
// ---------------------------------------------------------------------------
export default function ComponentsTableModal({ open, onClose }) {
  const [visible, setVisible] = useState(open)
  const [query, setQuery] = useState('')
  const [filter, setFilter] = useState('All')
  const panelRef = useRef(null)

  // Mirror the open prop so the modal can also close itself.
  useEffect(() => {
    setVisible(!!open)
  }, [open])

  // Escape to close + lock background scrolling while open.
  useEffect(() => {
    if (!visible) return
    const onKey = (e) => {
      if (e.key === 'Escape') {
        setVisible(false)
        if (typeof onClose === 'function') onClose()
      }
    }
    document.addEventListener('keydown', onKey)
    const previousOverflow = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    if (panelRef.current) panelRef.current.focus()
    return () => {
      document.removeEventListener('keydown', onKey)
      document.body.style.overflow = previousOverflow
    }
  }, [visible, onClose])

  const rows = useMemo(() => {
    const q = query.trim().toLowerCase()
    return componentSymbols.filter((c) => {
      if (filter !== 'All' && c.category !== filter) return false
      if (!q) return true
      return (
        c.name.toLowerCase().includes(q) ||
        c.category.toLowerCase().includes(q) ||
        c.uses.toLowerCase().includes(q)
      )
    })
  }, [query, filter])

  function close() {
    setVisible(false)
    if (typeof onClose === 'function') onClose()
  }

  if (!visible) return null

  const counts = {
    All: componentSymbols.length,
    Active: componentSymbols.filter((c) => c.category === 'Active').length,
    Passive: componentSymbols.filter((c) => c.category === 'Passive').length,
  }

  return (
    <div
      className="comp-overlay"
      role="dialog"
      aria-modal="true"
      aria-label="Active and passive components reference"
      onClick={close}
    >
      <div
        className="comp-panel"
        ref={panelRef}
        tabIndex={-1}
        onClick={(e) => e.stopPropagation()}
      >
        <div className="comp-head">
          <div>
            <h3>🔌 Active &amp; Passive Components — Quick Reference</h3>
            <p>
              The 20 components you meet most in EEE 282, with the circuit symbol you are
              expected to draw and what each one is for.
            </p>
          </div>
          <button className="btn btn-ghost btn-sm comp-close" onClick={close}>✕ Close</button>
        </div>

        <div className="comp-tools">
          <input
            className="comp-search"
            type="search"
            value={query}
            placeholder="Search a component or a use — e.g. zener, smoothing, sensing…"
            onChange={(e) => setQuery(e.target.value)}
          />
          <div className="comp-filter">
            {['All', 'Active', 'Passive'].map((f) => (
              <button
                key={f}
                type="button"
                className={filter === f ? 'active' : ''}
                onClick={() => setFilter(f)}
              >
                {f} ({counts[f]})
              </button>
            ))}
          </div>
        </div>

        <div className="comp-body">
          {rows.length === 0 ? (
            <div className="comp-empty">
              No component matches “{query}”. Try “capacitor”, “transistor” or “sensing”.
            </div>
          ) : (
            <table className="comp-table">
              <thead>
                <tr>
                  <th>Symbol</th>
                  <th>Component</th>
                  <th>Category</th>
                  <th>Primary uses / functions</th>
                </tr>
              </thead>
              <tbody>
                {rows.map((c) => (
                  <tr key={c.name}>
                    <td className="comp-sym-cell" data-label="Symbol">
                      <div dangerouslySetInnerHTML={{ __html: c.symbol }} />
                    </td>
                    <td data-label="Component" className="comp-name">{c.name}</td>
                    <td data-label="Category">
                      <span className={`comp-cat ${c.category.toLowerCase()}`}>{c.category}</span>
                    </td>
                    <td data-label="Primary uses" className="comp-uses">{c.uses}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>

        <div className="comp-foot">
          Showing {rows.length} of {componentSymbols.length} components ·
          {' '}Press <strong>Esc</strong> or tap outside to close.
        </div>
      </div>
    </div>
  )
}
