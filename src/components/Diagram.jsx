import { useState } from 'react'

// ---------------------------------------------------------------------------
// Diagram — renders a raw, responsive SVG string that lives in src/data.js.
//
// The markup is authored by us (build_eee282_data.py), carries no <script> and
// no <style>, and every marker id is namespaced per question, so it is safe to
// inject. Scaling is handled by CSS: viewBox drives the aspect ratio, the
// container drives the width.
// ---------------------------------------------------------------------------
export default function Diagram({ svg, caption, maxHeight = 320 }) {
  const [zoomed, setZoomed] = useState(false)
  if (!svg) return null

  return (
    <>
      <figure className="diagram">
        <div
          className="diagram-frame"
          style={{ maxHeight }}
          onClick={() => setZoomed(true)}
          dangerouslySetInnerHTML={{ __html: svg }}
        />
        <figcaption className="diagram-cap">
          {caption || 'Diagram for visual understanding — tap to zoom'}
        </figcaption>
      </figure>

      {zoomed && (
        <div className="overlay" onClick={() => setZoomed(false)}>
          <div className="diagram-zoom" onClick={(e) => e.stopPropagation()}>
            <div className="diagram-zoom-head">
              <span>{caption || 'Diagram'}</span>
              <button className="btn btn-ghost btn-sm" onClick={() => setZoomed(false)}>✕ Close</button>
            </div>
            <div className="diagram-zoom-body" dangerouslySetInnerHTML={{ __html: svg }} />
          </div>
        </div>
      )}
    </>
  )
}
