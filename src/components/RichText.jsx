import { useEffect, useRef } from 'react'

// ---------------------------------------------------------------------------
// RichText — renders solution/notes text with light formatting:
//   ### Heading lines   -> styled headings
//   - bullet lines      -> bullet lists
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

function textToHtml(text) {
  const lines = String(text || '').split('\n')
  const out = []
  let inList = false
  const closeList = () => { if (inList) { out.push('</ul>'); inList = false } }
  for (const raw of lines) {
    const t = raw.trim()
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
