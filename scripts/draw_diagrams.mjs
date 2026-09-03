// ---------------------------------------------------------------------------
// Draws the question diagrams for the EEE 282 bank.
//   • 18 questions that had no figure get one that is specific to what is asked
//   • every question that mentions the CRO gets the FULL instrument:
//     chassis, graticule screen, Time/Div, Volts/Div, Position, Trigger,
//     Intensity/Focus, CH1/CH2 BNC inputs and the DC-AC-GND coupling switch,
//     with the control under discussion highlighted in OAU gold.
//
// Output: standalone .svg files in public/images/eee282/ (build_eee282_data.py
// then inlines them into src/data.js).
// ---------------------------------------------------------------------------
// Regenerate every question figure:
//   node scripts/draw_diagrams.mjs
// Output goes to public/images/eee282/; build_eee282_data.py then inlines them
// into src/data.js (run `python3 build_eee282_data.py` afterwards).
import fs from 'fs'
import { fileURLToPath } from 'url'
import path from 'path'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const ROOT = path.resolve(HERE, '..')
const SYM = JSON.parse(fs.readFileSync(path.join(HERE, 'symbols.json'), 'utf8'))
const OUT = path.join(ROOT, 'public/images/eee282')
const TPL = path.resolve(ROOT, '../eee282_app/template.html')
const BUILT = path.resolve(ROOT, '../EEE282_Question_Bank_App.html')

// ------------------------------- primitives -------------------------------
const NAVY = '#010080'
const GOLD = '#C9A227'
const GREEN = '#0B7A55'
const RED = '#C62828'
const GREY = '#5b6478'

// Named HTML entities (&nbsp;) are undefined in XML, so a saved .svg would not
// render. Numeric references work in both the XML and HTML parsers.
const NAMED = {
  amp: 38, lt: 60, gt: 62, quot: 34, apos: 39, nbsp: 160, mdash: 8212, ndash: 8211,
  minus: 8722, times: 215, divide: 247, middot: 183, deg: 176, Omega: 937, mu: 956,
  rarr: 8594, larr: 8592, uarr: 8593, darr: 8595, harr: 8596, approx: 8776,
  plusmn: 177, omega: 969, theta: 952, pi: 960, alpha: 945, beta: 946, sigma: 963,
}
const ents = (s) => String(s).replace(/&([a-zA-Z][a-zA-Z0-9]*);/g,
  (m, name) => (name in NAMED ? '&#' + NAMED[name] + ';' : m))

const txt = (x, y, cls, s, extra = '') =>
  `<text class="${cls}" x="${x}" y="${y}" ${extra}>${s}</text>`

const line = (x1, y1, x2, y2, stroke = NAVY, w = 2.2, dash = '') =>
  `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" stroke-width="${w}"` +
  ` stroke-linecap="round"${dash ? ` stroke-dasharray="${dash}"` : ''}/>`

const box = (x, y, w, h, fill = 'none', stroke = NAVY, sw = 2, rx = 8) =>
  `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"/>`

// a circuit symbol from the library, placed and themed
function sym(name, x, y, s, stroke = NAVY) {
  let g = SYM[name].replace(/^<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '')
  g = g.replace(/#111111/g, stroke)
  return `<g transform="translate(${x},${y}) scale(${s})">${g}</g>`
}

// CRO graticule (10 horizontal x 8 vertical divisions, minor ticks)
function croGrid(gx, gy, gw, gh, cols = 10, rows = 8) {
  const p = []
  const dx = gw / cols, dy = gh / rows
  p.push(`<rect x="${gx}" y="${gy}" width="${gw}" height="${gh}" fill="#fdfdff" stroke="${NAVY}" stroke-width="2"/>`)
  for (let i = 1; i < cols; i++) p.push(line(gx + i * dx, gy, gx + i * dx, gy + gh, '#c3cad9', 1))
  for (let j = 1; j < rows; j++) p.push(line(gx, gy + j * dy, gx + gw, gy + j * dy, '#c3cad9', 1))
  const cx = gx + gw / 2, cy = gy + gh / 2
  p.push(line(gx, cy, gx + gw, cy, '#7d89a8', 1.3))
  p.push(line(cx, gy, cx, gy + gh, '#7d89a8', 1.3))
  for (let i = 0; i < cols; i++) for (let k = 1; k < 5; k++) {
    const x = gx + i * dx + (k * dx) / 5
    p.push(line(x, cy - 3, x, cy + 3, '#7d89a8', 1.3))
  }
  for (let j = 0; j < rows; j++) for (let k = 1; k < 5; k++) {
    const y = gy + j * dy + (k * dy) / 5
    p.push(line(cx - 3, y, cx + 3, y, '#7d89a8', 1.3))
  }
  return p.join('')
}

function wavePath(x0, y0, w, cycles, amp, offset = 0, phase = 0) {
  let d = ''
  const N = 300
  for (let i = 0; i <= N; i++) {
    const t = i / N
    const x = x0 + t * w
    const y = y0 + offset - amp * Math.sin(2 * Math.PI * cycles * t + phase)
    d += (i ? ' L' : 'M') + x.toFixed(1) + ' ' + y.toFixed(1)
  }
  return d
}

// dimension bracket with arrow heads
function hBracket(x1, x2, y, label, colour = GOLD) {
  const p = []
  p.push(line(x1, y, x2, y, colour, 1.8))
  p.push(line(x1, y - 6, x1, y + 6, colour, 1.8))
  p.push(line(x2, y - 6, x2, y + 6, colour, 1.8))
  p.push(txt((x1 + x2) / 2, y - 10, 'tg', label, 'text-anchor="middle"'))
  return p.join('')
}
function vBracket(y1, y2, x, label, colour = GOLD) {
  const p = []
  p.push(line(x, y1, x, y2, colour, 1.8))
  p.push(line(x - 6, y1, x + 6, y1, colour, 1.8))
  p.push(line(x - 6, y2, x + 6, y2, colour, 1.8))
  p.push(txt(x + 10, (y1 + y2) / 2 + 4, 'tg', label))
  return p.join('')
}

// --------------------------- CRO front panel ------------------------------
function knob(cx, cy, r, label, value, hl = false, angle = -140) {
  let s = ''
  if (hl) {
    s += `<rect x="${cx - r - 12}" y="${cy - r - 14}" width="${2 * r + 24}" height="${2 * r + 56}" rx="10"` +
      ` fill="rgba(201,162,39,0.20)" stroke="${GOLD}" stroke-width="2"/>`
  }
  s += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="#ffffff" stroke="${NAVY}" stroke-width="2.2"/>`
  for (let i = 0; i < 12; i++) {
    const a = ((-150 + i * 30) * Math.PI) / 180
    s += line(cx + Math.cos(a) * (r - 8), cy + Math.sin(a) * (r - 8),
      cx + Math.cos(a) * (r - 3), cy + Math.sin(a) * (r - 3), '#7d89a8', 1.4)
  }
  const a = (angle * Math.PI) / 180
  s += line(cx, cy, cx + Math.cos(a) * (r - 7), cy + Math.sin(a) * (r - 7),
    hl ? GOLD : NAVY, 3)
  s += `<circle cx="${cx}" cy="${cy}" r="3.2" fill="${NAVY}"/>`
  s += txt(cx, cy + r + 17, hl ? 'tg' : 'tb', label, 'text-anchor="middle"')
  if (value) s += txt(cx, cy + r + 32, 't11', value, 'text-anchor="middle"')
  if (hl) s += txt(cx, cy + r + 47, 'tg', '&#9666; asked here', 'text-anchor="middle"')
  return s
}

function couplingSwitch(x, y, active) {
  const labels = ['DC', 'AC', 'GND']
  let s = box(x, y, 92, 74, '#ffffff', NAVY, 2, 8)
  s += txt(x + 46, y - 8, 'tb', 'COUPLING', 'text-anchor="middle"')
  labels.forEach((l, i) => {
    const ly = y + 20 + i * 20
    if (l === active) s += box(x + 6, ly - 13, 80, 19, 'rgba(201,162,39,0.22)', GOLD, 1.8, 5)
    s += txt(x + 14, ly, l === active ? 'tg' : 't12', l)
  })
  // lever pointing at the active position
  const idx = labels.indexOf(active)
  s += line(x - 10, y + 20 + idx * 20 - 5, x - 2, y + 20 + idx * 20 - 5, GOLD, 3)
  return s
}

function bnc(cx, cy, label, hl = false) {
  let s = ''
  if (hl) s += `<circle cx="${cx}" cy="${cy}" r="30" fill="rgba(201,162,39,0.20)" stroke="${GOLD}" stroke-width="2"/>`
  s += `<circle cx="${cx}" cy="${cy}" r="17" fill="#ffffff" stroke="${NAVY}" stroke-width="2.2"/>`
  s += `<circle cx="${cx}" cy="${cy}" r="6" fill="${NAVY}"/>`
  s += txt(cx, cy + 34, hl ? 'tg' : 'tb', label, 'text-anchor="middle"')
  return s
}

// full instrument: screen content is a nested <svg> so each trace keeps its
// own coordinate system and simply scales into the screen aperture.
function croPanel({ screen, vb, volts = '5 V/div', time = '2 ms/div', hl = null, xy = false, footer = '' }) {
  const W = 760, H = 500
  const p = []
  p.push(box(6, 6, W - 12, H - 12, '#f4f7fc', NAVY, 3, 14))
  p.push(txt(26, 34, 'tb', 'CATHODE RAY OSCILLOSCOPE (CRO)'))
  p.push(txt(W - 26, 34, 't11', 'EEE 282 &#183; Practicals II', 'text-anchor="end"'))
  p.push(line(26, 40, W - 26, 40, '#7d89a8', 1.2))

  // ---- screen ----
  p.push(box(40, 52, 470, 288, '#e8edf6', NAVY, 2.5, 8))
  p.push(
    `<svg x="48" y="60" width="454" height="272" viewBox="${vb}" preserveAspectRatio="xMidYMid meet">${screen}</svg>`
  )

  // ---- right-hand control column ----
  p.push(txt(530, 78, 'tb', 'VERTICAL'))
  p.push(knob(596, 118, 26, 'POSITION', '', hl === 'vertpos'))
  p.push(knob(690, 118, 26, 'VOLTS/DIV', volts, hl === 'voltsdiv'))
  p.push(txt(530, 190, 'tb', 'HORIZONTAL'))
  p.push(knob(596, 230, 26, 'POSITION', '', hl === 'horizpos'))
  p.push(knob(690, 230, 26, 'TIME/DIV', time, hl === 'timediv'))
  p.push(txt(530, 300, 'tb', 'TRIGGER'))
  p.push(knob(596, 340, 24, 'LEVEL', '', hl === 'trigger'))
  if (xy) {
    p.push(box(648, 316, 84, 48, 'rgba(201,162,39,0.22)', GOLD, 2, 8))
    p.push(txt(690, 336, 'tg', 'X-Y MODE', 'text-anchor="middle"'))
    p.push(txt(690, 352, 't11', 'sweep off', 'text-anchor="middle"'))
  } else {
    p.push(knob(690, 340, 24, 'SOURCE', 'CH1', false))
  }
  p.push(txt(530, 400, 'tb', 'DISPLAY'))
  const disp = knob(596, 440, 22, 'INTENSITY', '', false, -90)
  p.push(disp)
  p.push(knob(690, 440, 22, 'FOCUS', '', false, -90))

  // ---- input section under the screen ----
  p.push(line(40, 362, 510, 362, '#c3cad9', 1.2))
  p.push(bnc(96, 412, 'CH1', hl === 'bnc1'))
  p.push(couplingSwitch(150, 380, xy ? 'DC' : hl === 'coupling' ? 'AC' : 'DC'))
  p.push(bnc(330, 412, 'CH2', hl === 'bnc2'))
  p.push(couplingSwitch(384, 380, 'GND'))
  if (footer) p.push(txt(40, 470, 't12', footer))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}"` +
    ` preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// --------------------------- BJT / DMM pieces -----------------------------
function to92(x, y, pins = ['1', '2', '3']) {
  let s = ''
  s += `<path d="M${x},${y} h96 a10,10 0 0 1 10,10 v70 a10,10 0 0 1 -10,10 h-96 a10,10 0 0 1 -10,-10 v-70 a10,10 0 0 1 10,-10 z" fill="#eef1fa" stroke="${NAVY}" stroke-width="2.4"/>`
  s += line(x + 20, y + 70, x + 20, y + 90, NAVY, 3)
  s += line(x + 48, y + 70, x + 48, y + 90, NAVY, 3)
  s += line(x + 76, y + 70, x + 76, y + 90, NAVY, 3)
  pins.forEach((n, i) => {
    s += txt(x + 20 + i * 28, y + 106, 'tb', n, 'text-anchor="middle"')
    s += `<circle cx="${x + 20 + i * 28}" cy="${y + 70}" r="4" fill="${NAVY}"/>`
  })
  return s
}

function probe(x1, y1, x2, y2, colour, label, anchor = 'start') {
  let s = `<path d="M${x1},${y1} C${x1},${y1 + 40} ${x2},${y2 - 60} ${x2},${y2}" fill="none" stroke="${colour}" stroke-width="3" stroke-linecap="round"/>`
  s += `<circle cx="${x2}" cy="${y2}" r="5" fill="${colour}"/>`
  s += txt(x2 + (anchor === 'end' ? -10 : 10), y2 + 5, 'tb', label,
    `text-anchor="${anchor}" fill="${colour}"`)
  return s
}

function meter(x, y, w, h, reading, colour = NAVY) {
  let s = box(x, y, w, h, '#ffffff', NAVY, 2.2, 6)
  s += txt(x + w / 2, y + 22, 't11', 'DMM &#8212; DIODE MODE', 'text-anchor="middle"')
  s += txt(x + w / 2, y + h - 12, 't15', reading, `text-anchor="middle" fill="${colour}"`)
  return s
}

// ===========================================================================
// NON-CRO FIGURES
// ===========================================================================
const D = {}

// ---- q01: active vs passive ----
D.q01 = () => {
  const p = []
  p.push(box(20, 20, 250, 200, 'rgba(1,0,128,0.05)', NAVY, 2, 12))
  p.push(txt(145, 48, 'tb', 'ACTIVE', 'text-anchor="middle"'))
  p.push(txt(145, 68, 't12', 'needs a supply &#183; can give gain', 'text-anchor="middle"'))
  p.push(sym('DC source', 40, 90, 0.9))
  p.push(sym('NPN transistor (BJT)', 140, 90, 0.9))
  p.push(txt(40, 160, 't11', 'source', 'text-anchor="middle"'))
  p.push(txt(190, 160, 't11', 'transistor', 'text-anchor="middle"'))
  p.push(box(290, 20, 250, 200, 'rgba(201,162,39,0.12)', GOLD, 2, 12))
  p.push(txt(415, 48, 'tb', 'PASSIVE', 'text-anchor="middle"'))
  p.push(txt(415, 68, 't12', 'stores / dissipates only', 'text-anchor="middle"'))
  p.push(sym('Resistor (ANSI / zig-zag)', 300, 100, 0.85))
  p.push(sym('Inductor (air core)', 420, 100, 0.85))
  p.push(sym('Capacitor (non-polarised)', 360, 160, 0.85))
  p.push(txt(415, 208, 't11', 'R &#183; L &#183; C &#8212; no gain, no supply', 'text-anchor="middle"'))
  p.push(txt(280, 250, 'tg', 'The test: can it control a bigger signal using a supply?', 'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 270" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// ---- q08: classify four components ----
D.q08 = () => {
  const cells = [
    ['N-channel MOSFET (enhancement)', 'MOSFET', 'ACTIVE', 20, 20],
    ['Potentiometer (3-terminal)', 'Potentiometer', 'PASSIVE', 290, 20],
    ['Operational amplifier', 'Op-Amp', 'ACTIVE', 20, 150],
    ['Inductor (air core)', 'Inductor', 'PASSIVE', 290, 150],
  ]
  const p = []
  for (const [key, name, cls, x, y] of cells) {
    const active = cls === 'ACTIVE'
    p.push(box(x, y, 250, 118, active ? 'rgba(1,0,128,0.05)' : 'rgba(201,162,39,0.12)',
      active ? NAVY : GOLD, 2, 12))
    p.push(sym(key, x + 45, y + 34, 1.0))
    p.push(txt(x + 125, y + 30, 'tb', name, 'text-anchor="middle"'))
    p.push(txt(x + 125, y + 100, 'tg', cls, 'text-anchor="middle"'))
  }
  p.push(txt(280, 300, 't12', 'Active = needs a supply and can control or amplify. Passive = stores or dissipates only.',
    'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 320" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// ---- q09: a BJT is two diodes sharing the base ----
D.q09 = () => {
  const p = []
  p.push(txt(300, 26, 'tb', 'A BJT = two junctions sharing one terminal (the base)', 'text-anchor="middle"'))
  // NPN model: two diodes, anodes together
  p.push(box(20, 46, 260, 150, '#f7f9fd', NAVY, 1.6, 10))
  p.push(txt(150, 70, 'tb', 'NPN', 'text-anchor="middle"'))
  p.push(sym('Diode', 30, 96, 0.62, NAVY))
  p.push(sym('Diode', 145, 96, 0.62, NAVY))
  p.push(line(135, 112, 150, 112, NAVY, 2.6))
  p.push(txt(150, 186, 'tg', 'BASE', 'text-anchor="middle"'))
  p.push(txt(40, 140, 't12', 'C'))
  p.push(txt(275, 140, 't12', 'E'))
  // PNP model: cathodes together
  p.push(box(300, 46, 260, 150, '#f7f9fd', NAVY, 1.6, 10))
  p.push(txt(430, 70, 'tb', 'PNP', 'text-anchor="middle"'))
  p.push(`<g transform="translate(310,96) scale(0.62) rotate(180 50 15)">${SYM['Diode'].replace(/^<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '').replace(/#111111/g, NAVY)}</g>`)
  p.push(`<g transform="translate(425,96) scale(0.62) rotate(180 50 15)">${SYM['Diode'].replace(/^<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '').replace(/#111111/g, NAVY)}</g>`)
  p.push(line(415, 112, 430, 112, NAVY, 2.6))
  p.push(txt(430, 186, 'tg', 'BASE', 'text-anchor="middle"'))
  p.push(txt(320, 140, 't12', 'E'))
  p.push(txt(555, 140, 't12', 'C'))
  p.push(txt(300, 226, 't13', 'Only the base conducts to BOTH other pins at &#8776;0.6&#8211;0.7 V.', 'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 244" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// helper: DMM probing a TO-92
function probeFigure({ title, commonPin, probeColour, readings, verdict, notes }) {
  const p = []
  p.push(txt(300, 24, 'tb', title, 'text-anchor="middle"'))
  p.push(to92(180, 60))
  p.push(meter(30, 120, 150, 70, readings.label, readings.colour))
  readings.probes.forEach((pr) => {
    p.push(probe(pr.from[0], pr.from[1], pr.to[0], pr.to[1], probeColour, pr.reading, pr.anchor))
  })
  p.push(line(105, 190, 240, 150, probeColour, 3))
  p.push(box(430, 60, 130, 120, '#f7f9fd', verdict.colour, 2, 10))
  p.push(txt(495, 90, 'tb', verdict.type, `text-anchor="middle" fill="${verdict.colour}"`))
  p.push(txt(495, 112, 't12', 'Base = pin ' + commonPin, 'text-anchor="middle"'))
  verdict.lines.forEach((l, i) => p.push(txt(495, 136 + i * 18, 't12', l, 'text-anchor="middle"')))
  notes.forEach((n, i) => p.push(txt(300, 232 + i * 20, 't12', n, 'text-anchor="middle"')))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 ${260 + notes.length * 20}" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

D.q10 = () => probeFigure({
  title: 'RED probe on pin 2 &#8594; 0.65 V to both other pins',
  commonPin: '2',
  probeColour: RED,
  readings: {
    label: '0.65 V', colour: NAVY,
    probes: [
      { from: [140, 190], to: [200, 152], reading: '0.65 V', anchor: 'end' },
      { from: [140, 190], to: [256, 152], reading: '0.65 V' },
    ],
  },
  verdict: { type: 'NPN', colour: NAVY, lines: ['red = common base', '&#8594; NPN'] },
  notes: ['Red probe forward-biases both junctions from the same pin, so pin 2 is the P-type middle layer.'],
})

D.q11 = () => probeFigure({
  title: 'BLACK probe on pin 1 &#8594; 0.68 V to both other pins',
  commonPin: '1',
  probeColour: '#1f2937',
  readings: {
    label: '0.68 V', colour: NAVY,
    probes: [
      { from: [140, 190], to: [228, 152], reading: '0.68 V', anchor: 'end' },
      { from: [140, 190], to: [284, 152], reading: '0.68 V' },
    ],
  },
  verdict: { type: 'PNP', colour: NAVY, lines: ['black = common base', '&#8594; PNP'] },
  notes: ['Black (COM) on the shared pin means it is the N-type middle layer &#8212; a PNP transistor.'],
})

D.q14 = () => probeFigure({
  title: 'BLACK probe on pin 2 &#8594; 0.655 V and 0.661 V',
  commonPin: '2',
  probeColour: '#1f2937',
  readings: {
    label: '0.66 V', colour: NAVY,
    probes: [
      { from: [140, 190], to: [200, 152], reading: '0.655 V', anchor: 'end' },
      { from: [140, 190], to: [256, 152], reading: '0.661 V' },
    ],
  },
  verdict: { type: 'PNP', colour: NAVY, lines: ['Base = pin 2', 'E = pin 3 (0.661 V)', 'C = pin 1 (0.655 V)'] },
  notes: ['Black common &#8594; PNP.', 'The LARGER drop is the emitter, so pin 3 is the emitter and pin 1 the collector.'],
})

// ---- q12: emitter vs collector by junction drop ----
D.q12 = () => {
  const p = []
  p.push(txt(280, 24, 'tb', 'Splitting emitter from collector', 'text-anchor="middle"'))
  p.push(sym('NPN transistor (BJT)', 120, 60, 1.7))
  p.push(txt(150, 130, 'tb', 'NPN', 'text-anchor="middle"'))
  p.push(box(330, 70, 210, 120, '#f7f9fd', NAVY, 1.6, 10))
  p.push(txt(435, 96, 'tb', 'Junction drops', 'text-anchor="middle"'))
  p.push(txt(350, 126, 't13', 'V(BE) = 0.712 V'))
  p.push(txt(350, 152, 'tg', '&#8594; larger = EMITTER'))
  p.push(txt(350, 178, 't13', 'V(BC) = 0.704 V'))
  p.push(txt(280, 226, 't12', 'The emitter is more heavily doped, so its junction drop is 5&#8211;15 mV higher.',
    'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 248" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// ---- q15: healthy C-E reads OL both ways ----
D.q15 = () => {
  const p = []
  p.push(txt(290, 24, 'tb', 'Healthy transistor: C &#8211; E must read OL both ways', 'text-anchor="middle"'))
  p.push(box(20, 44, 250, 150, '#f7f9fd', NAVY, 1.6, 10))
  p.push(sym('NPN transistor (BJT)', 55, 90, 1.2))
  p.push(probe(120, 200, 75, 150, RED, 'red', 'end'))
  p.push(probe(230, 200, 190, 150, '#1f2937', 'black'))
  p.push(txt(145, 220, 't13', 'reading: OL', 'text-anchor="middle"'))
  p.push(box(300, 44, 250, 150, '#f7f9fd', NAVY, 1.6, 10))
  p.push(sym('NPN transistor (BJT)', 335, 90, 1.2))
  p.push(probe(400, 200, 355, 150, '#1f2937', 'black', 'end'))
  p.push(probe(510, 200, 470, 150, RED, 'red'))
  p.push(txt(425, 220, 't13', 'reading: OL', 'text-anchor="middle"'))
  p.push(txt(290, 250, 't12', 'Two junctions back to back: one is always reverse biased, so no current flows.',
    'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 268" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// ---- q16: C-E short ----
D.q16 = () => {
  const p = []
  p.push(txt(290, 24, 'tb', 'Fault: collector&#8211;emitter short', 'text-anchor="middle"'))
  p.push(sym('NPN transistor (BJT)', 200, 60, 1.6))
  p.push(line(300, 96, 300, 168, RED, 5))
  p.push(txt(312, 136, 'tb', 'SHORT', 'fill="' + RED + '"'))
  p.push(meter(40, 90, 150, 70, '0.000 V', RED))
  p.push(probe(120, 160, 300, 110, RED, '', 'end'))
  p.push(probe(120, 160, 300, 156, '#1f2937', ''))
  p.push(box(400, 90, 160, 70, 'rgba(198,40,40,0.08)', RED, 2, 10))
  p.push(txt(480, 118, 'tb', 'FAULTY', 'text-anchor="middle" fill="' + RED + '"'))
  p.push(txt(480, 140, 't12', 'replace the device', 'text-anchor="middle"'))
  p.push(txt(290, 210, 't12', '0.000 V across C&#8211;E (instead of OL) means the silicon has fused into a short.',
    'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 230" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// ---- q17: all OL = open ----
D.q17 = () => {
  const p = []
  p.push(txt(290, 24, 'tb', 'Fault: no junction conducts anywhere', 'text-anchor="middle"'))
  p.push(sym('NPN transistor (BJT)', 200, 60, 1.6))
  p.forEach(() => {})
  p.push(line(228, 108, 262, 142, RED, 3.4))
  p.push(line(262, 108, 228, 142, RED, 3.4))
  p.push(txt(300, 100, 'tb', 'open', 'fill="' + RED + '"'))
  p.push(meter(40, 90, 150, 70, 'OL', RED))
  p.push(probe(120, 160, 250, 110, RED, '', 'end'))
  p.push(probe(120, 160, 250, 156, '#1f2937', ''))
  p.push(box(400, 90, 160, 70, 'rgba(198,40,40,0.08)', RED, 2, 10))
  p.push(txt(480, 118, 'tb', 'BLOWN', 'text-anchor="middle" fill="' + RED + '"'))
  p.push(txt(480, 140, 't12', 'both junctions open', 'text-anchor="middle"'))
  p.push(txt(290, 210, 't12', 'All six probe combinations read OL &#8594; the transistor is open circuit.',
    'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 230" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// ---- q18: not a BJT ----
D.q18 = () => {
  const p = []
  p.push(txt(300, 24, 'tb', 'Two separate diodes, no common pin &#8594; NOT a BJT', 'text-anchor="middle"'))
  p.push(sym('Diode', 30, 90, 0.9))
  p.push(sym('Diode', 200, 90, 0.9))
  p.push(line(185, 118, 205, 118, NAVY, 2.6))
  p.push(txt(120, 190, 't13', 'two diodes back to back', 'text-anchor="middle"'))
  p.push(box(350, 60, 230, 130, '#f7f9fd', NAVY, 1.6, 10))
  p.push(txt(465, 86, 'tb', 'Probe results', 'text-anchor="middle"'))
  p.push(txt(365, 112, 't12', 'red on 1: pin 2 = 0.6 V, pin 3 = OL'))
  p.push(txt(365, 136, 't12', 'black on 1: pin 2 = OL, pin 3 = 0.6 V'))
  p.push(txt(365, 168, 'tg', 'No single pin reaches both.'))
  p.push(txt(300, 224, 't12', 'A BJT must have ONE pin that conducts to both others with the SAME polarity.',
    'text-anchor="middle"'))
  return `<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 244" preserveAspectRatio="xMidYMid meet" role="img">${p.join('')}</svg>`
}

// ===========================================================================
// CRO FIGURES  (screen content drawn in a 640x320 space, then placed in the
// full instrument by croPanel)
// ===========================================================================
const G = { x: 40, y: 20, w: 560, h: 280, cols: 10, rows: 8 }
const dx = G.w / G.cols, dy = G.h / G.rows
const cx = G.x + G.w / 2, cy = G.y + G.h / 2

const grid = () => croGrid(G.x, G.y, G.w, G.h, G.cols, G.rows)

D.q19 = () => croPanel({
  vb: '0 0 640 320',
  volts: '2 V/div', time: '1 ms/div', hl: 'timediv',
  footer: 'One horizontal division is set by the TIME/DIV knob: T = (divisions per cycle) &#215; (Time/Div).',
  screen: [
    grid(),
    `<path class="w" d="${wavePath(G.x, cy, G.w, 2, 2 * dy, 0, 0)}"/>`,
    hBracket(G.x, G.x + dx, G.y + G.h + 26, '1 div'),
    txt(G.x + G.w / 2, G.y + G.h + 56, 't13', 'horizontal axis = TIME &#8594; controlled by TIME/DIV', 'text-anchor="middle"'),
  ].join(''),
})

D.q20 = () => croPanel({
  vb: '0 0 640 320',
  volts: '2 V/div', time: '1 ms/div', hl: 'voltsdiv',
  footer: 'One vertical division is set by the VOLTS/DIV knob: Vp-p = (vertical divisions) &#215; (Volts/Div).',
  screen: [
    grid(),
    `<path class="w" d="${wavePath(G.x, cy, G.w, 2, 2 * dy, 0, 0)}"/>`,
    vBracket(cy - dy, cy, G.x - 22, '1 div'),
    txt(G.x + G.w + 8, cy - 30, 't13', 'vertical axis = VOLTS'),
    txt(G.x + G.w + 8, cy - 12, 't13', '&#8594; VOLTS/DIV'),
  ].join(''),
})

D.q21 = () => croPanel({
  vb: '0 0 640 320',
  volts: '1 V/div', time: '1 ms/div', hl: 'coupling',
  footer: 'AC coupling puts a capacitor in series: the DC level is blocked and the trace centres on 0 V.',
  screen: [
    grid(),
    `<path class="dm" d="${wavePath(G.x, cy - 2 * dy, G.w, 2, 1.5 * dy, 0, 0)}"/>`,
    `<path class="w" d="${wavePath(G.x, cy, G.w, 2, 1.5 * dy, 0, 0)}"/>`,
    line(G.x, cy - 2 * dy, G.x + G.w, cy - 2 * dy, GREY, 1.2, '6 5'),
    txt(G.x + 8, cy - 2 * dy - 12, 't12', 'input: AC riding on a DC level'),
    txt(G.x + 8, cy + 3 * dy, 't12', '&#8594; AC coupled output: centred on 0 V, DC removed'),
    txt(G.x + G.w, G.y + 16, 'tg', 'DC offset gone', 'text-anchor="end"'),
  ].join(''),
})

D.q22 = () => croPanel({
  vb: '0 0 640 320',
  volts: '1 V/div', time: '1 ms/div',
  footer: 'Standard graticule: one major division is 1 cm &#215; 1 cm, subdivided into 5 minor ticks.',
  screen: [
    grid(),
    `<rect x="${G.x + 3 * dx}" y="${G.y + 2 * dy}" width="${dx}" height="${dy}" fill="rgba(201,162,39,0.28)" stroke="${GOLD}" stroke-width="2"/>`,
    hBracket(G.x + 3 * dx, G.x + 4 * dx, G.y + 3 * dy + 34, '1 cm'),
    vBracket(G.y + 2 * dy, G.y + 3 * dy, G.x + 4 * dx + 46, '1 cm'),
    txt(G.x + G.w / 2, G.y + G.h + 74, 't13', 'one major division = 1 cm &#215; 1 cm (&#215;5 minor ticks each way)', 'text-anchor="middle"'),
  ].join(''),
})

D.q23 = () => croPanel({
  vb: '0 0 640 320',
  volts: '2 V/div', time: '1 ms/div', hl: 'vertpos',
  footer: 'VERTICAL POSITION slides the whole trace up or down; the peak-to-peak amplitude does not change.',
  screen: [
    grid(),
    `<path class="w" d="${wavePath(G.x, cy, G.w, 2, 1.5 * dy, 0, 0)}"/>`,
    `<path class="dm" d="${wavePath(G.x, cy, G.w, 2, 1.5 * dy, -2 * dy, 0)}"/>`,
    `<path d="M${G.x + G.w + 22},${cy} L${G.x + G.w + 22},${cy - 2 * dy}" fill="none" stroke="${GOLD}" stroke-width="2" marker-end="url(#ahsq23)"/>`,
    `<defs><marker id="ahsq23" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="${GOLD}"/></marker></defs>`,
    txt(G.x + G.w + 30, cy - dy, 'tg', 'position'),
    txt(G.x + 8, cy - 3 * dy - 6, 't12', 'same amplitude, shifted up'),
    txt(G.x + 8, cy + 3 * dy + 4, 't12', 'reference trace'),
  ].join(''),
})

D.q26 = () => croPanel({
  vb: '0 0 640 320',
  volts: '2 V/div', time: '1 ms/div',
  footer: 'f = 250 Hz &#8594; T = 4 ms; at 1 ms/div one cycle occupies 4 horizontal divisions.',
  screen: [
    grid(),
    `<path class="w" d="${wavePath(G.x + dx, cy, 4 * dx, 1, 2 * dy, 0, 0)}"/>`,
    line(G.x + dx, cy - 3 * dy, G.x + dx, cy + 3 * dy, GOLD, 1.4, '5 4'),
    line(G.x + 5 * dx, cy - 3 * dy, G.x + 5 * dx, cy + 3 * dy, GOLD, 1.4, '5 4'),
    hBracket(G.x + dx, G.x + 5 * dx, cy + 3 * dy + 14, '1 cycle = 4 div = 4 ms'),
    txt(G.x + G.w / 2, G.y + G.h + 62, 't13', 'f = 1 / T = 1 / 4 ms = 250 Hz', 'text-anchor="middle"'),
  ].join(''),
})

D.q27 = () => croPanel({
  vb: '0 0 640 320',
  volts: '10 V/div', time: '2 ms/div',
  footer: 'Vrms = 14.14 V &#8594; Vp = 20 V &#8594; Vp-p = 40 V; at 10 V/div that is 4 vertical divisions.',
  screen: [
    grid(),
    `<path class="w" d="${wavePath(G.x, cy, G.w, 2, 2 * dy, 0, 0)}"/>`,
    line(G.x - 16, cy - 2 * dy, G.x + G.w + 16, cy - 2 * dy, GOLD, 1.4, '5 4'),
    line(G.x - 16, cy + 2 * dy, G.x + G.w + 16, cy + 2 * dy, GOLD, 1.4, '5 4'),
    vBracket(cy - 2 * dy, cy + 2 * dy, G.x + G.w + 24, 'Vp-p = 4 div'),
    txt(G.x + 8, cy - 3 * dy, 't13', 'Vp = 20 V'),
    txt(G.x + 8, cy + 4 * dy, 't13', 'Vrms = 14.14 V'),
  ].join(''),
})

// ===========================================================================
// write files
// ===========================================================================
let n = 0
for (const [key, fn] of Object.entries(D)) {
  const svg = ents(fn())
  if (/NaN|undefined/.test(svg)) throw new Error('bad numbers in ' + key)
  fs.writeFileSync(`${OUT}/${key}.svg`, svg)
  console.log(key, svg.length, 'bytes')
  n++
}
console.log('wrote', n, 'new diagrams')

// ---------------------------------------------------------------------------
// The five CRO traces that already existed are re-issued inside the full
// instrument, so every question that mentions the CRO shows the whole scope.
// ---------------------------------------------------------------------------
const html = fs.readFileSync(BUILT, 'utf8')
const SYM2 = JSON.parse(html.match(/const SYM = (\{[\s\S]*?\});\n/)[1])
const tpl = fs.readFileSync(TPL, 'utf8')
const tStart = tpl.indexOf('const dec = s =>')
const tEnd = tpl.indexOf('\n};\n', tpl.indexOf('D.q30')) + 3
const Dold = new Function('SYM', tpl.slice(tStart, tEnd) + '\nreturn D;')(SYM2)

const WRAP = {
  q24: { volts: '5 V/div', time: '2 ms/div',
    footer: 'Screen: 4 divisions peak-to-peak at 5 V/div &#8594; Vp-p = 20 V, Vp = 10 V, Vrms = 7.07 V.' },
  q25: { volts: '2 V/div', time: '2 ms/div',
    footer: 'Screen: one cycle spans 5 divisions at 2 ms/div &#8594; T = 10 ms, f = 100 Hz.' },
  q28: { volts: '2 V/div', time: '2 ms/div',
    footer: 'DC coupling: the trace lies between +1 and +5 divisions &#8594; Vp-p = 8 V, Vp = 4 V, DC offset = 6 V.' },
  q29: { volts: '2 V/div', time: '1 ms/div',
    footer: 'Dual trace: one cycle spans 8 divisions and B crosses zero 1 division after A &#8594; phase = 45&#176;.' },
  q30: { volts: '2 V/div', time: 'X-Y', xy: true,
    footer: 'X-Y mode (sweep off): fy / fx = horizontal tangencies / vertical tangencies = 4 / 1 &#8594; fy = 200 Hz.' },
}

let w = 0
for (const [key, cfg] of Object.entries(WRAP)) {
  const raw = Dold[key]()
  const vb = raw.match(/viewBox="0 0 (\d+) (\d+)"/).slice(1, 3).join(' ')
  let inner = raw.replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '')
  inner = inner.replace(/#DAA520/g, '#C9A227').replace(/#000080/g, '#010080')
  // namespace the trace's own markers so they cannot clash with the panel's
  for (const m of [...new Set([...inner.matchAll(/id="(ah[a-z]*)"/g)].map((x) => x[1]))]) {
    inner = inner
      .replace(new RegExp(`id="${m}"`, 'g'), `id="${m}-${key}"`)
      .replace(new RegExp(`url\\(#${m}\\)`, 'g'), `url(#${m}-${key})`)
  }
  const svg = ents(croPanel({ screen: inner, vb, ...cfg }))
  if (/NaN|undefined/.test(svg)) throw new Error('bad numbers in ' + key)
  fs.writeFileSync(`${OUT}/${key}.svg`, svg)
  console.log(key, '(re-issued in full CRO)', svg.length, 'bytes')
  w++
}
console.log('wrapped', w, 'existing CRO traces')
