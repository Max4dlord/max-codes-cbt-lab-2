import { useEffect, useRef } from 'react'

// ---------------------------------------------------------------------------
// RichText — renders solution/notes text with light formatting:
//   ### Heading lines   -> styled headings
//   - bullet lines      -> bullet lists
//   | a | b |           -> markdown tables (header row + |---| separator)
//   **bold**            -> <strong>
//   $...$  /  $$...$$   -> KaTeX inline / display math (rendered once the
//                          KaTeX library has loaded; retries until ready)
// ---------------------------------------------------------------------------

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

function inline(s) {
  // bold markers **text**
  return s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
}

// A markdown table row: | cell | cell |
const isRow = (t) => t.startsWith('|') && t.endsWith('|') && t.length > 2
// The separator under the header: |---|:--:|
const isDivider = (t) => isRow(t) && /^\|[\s:|-]+\|$/.test(t) && t.includes('-')

const cellsOf = (t) => t.slice(1, -1).split('|').map((c) => c.trim())

function textToHtml(text) {
  const lines = String(text || '').split('\n')
  const out = []
  let inList = false
  const closeList = () => { if (inList) { out.push('</ul>'); inList = false } }

  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i]
    const t = raw.trim()

    // ---- markdown table: header row followed by a |---| divider ----
    if (isRow(t) && i + 1 < lines.length && isDivider(lines[i + 1].trim())) {
      closeList()
      const head = cellsOf(t)
      const body = []
      i += 2 // skip the header and the divider
      while (i < lines.length && isRow(lines[i].trim())) {
        body.push(cellsOf(lines[i].trim()))
        i++
      }
      i-- // the for-loop will advance past the last consumed line
      const th = head.map((c) => `<th>${inline(escapeHtml(c))}</th>`).join('')
      const trs = body
        .map((r) => `<tr>${r.map((c) => `<td>${inline(escapeHtml(c))}</td>`).join('')}</tr>`)
        .join('')
      out.push(
        `<div class="rt-table-wrap"><table class="rt-table">` +
        `<thead><tr>${th}</tr></thead><tbody>${trs}</tbody></table></div>`
      )
      continue
    }

    if (t.startsWith('### ')) {
      closeList()
      out.push(`<h4 class="rt-h">${inline(escapeHtml(t.slice(4)))}</h4>`)
    } else if (t.startsWith('- ')) {
      if (!inList) { out.push('<ul class="rt-ul">'); inList = true }
      out.push(`<li>${inline(escapeHtml(t.slice(2)))}</li>`)
    } else if (t === '') {
      closeList()
      out.push('<div class="rt-gap"></div>')
    } else {
      closeList()
      out.push(`<div class="rt-line">${inline(escapeHtml(t))}</div>`)
    }
  }
  closeList()
  return out.join('')
}

const DELIMS = [
  { left: '$$', right: '$$', display: true },
  { left: '$', right: '$', display: false }
]

export default function RichText({ text, className, ...rest }) {
  const ref = useRef(null)
  useEffect(() => {
    const el = ref.current
    if (!el) return
    let cancelled = false
    let attempts = 0
    const tryRender = () => {
      if (cancelled) return
      if (typeof window !== 'undefined' && typeof window.renderMathInElement === 'function') {
        try {
          window.renderMathInElement(el, { delimiters: DELIMS, throwOnError: false })
        } catch (e) {
          console.warn('KaTeX render failed:', e)
        }
      } else if (attempts < 25) {
        attempts += 1
        setTimeout(tryRender, 300)
      }
    }
    tryRender()
    return () => { cancelled = true }
  }, [text])

  return (
    <div
      className={className || 'panel-sol'}
      ref={ref}
      {...rest}
      dangerouslySetInnerHTML={{ __html: textToHtml(text) }}
    />
  )
}
