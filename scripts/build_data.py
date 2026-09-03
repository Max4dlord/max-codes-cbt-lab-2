#!/usr/bin/env python3
"""Build src/data.js for CBT Lab 2 — EEE 282 (Obafemi Awolowo University).

Run from the repo root:  python3 scripts/build_data.py
Regenerate the figures first with:  node scripts/draw_diagrams.mjs

Single course: EEE 282 — Electronic & Electrical Introductory Practicals II.
30 questions: 17 MCQ + 7 calculations + 6 short answers.
Every question carries 4 options (the app is a CBT engine) AND, for the
calculation / short-answer questions, a typed-answer grader.
"""
import html.entities
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
SYMBOLS = json.loads((HERE / 'symbols.json').read_text())   # 62 clean 100x60 circuit symbols
DIAGRAM_DIR = ROOT / 'public' / 'images' / 'eee282'
IMG = '/images/eee282/{}.svg'   # build-time pointer only; emitted as an inline `diagram`

CAPTIONS = {
    'q01': "Active vs passive: an active part needs a supply and gives gain; a passive part only stores or dissipates",
    'q02': "PN junction diode: anode (P-type) and cathode (N-type, banded end)",
    'q03': "Potentiometer wired as a variable voltage divider (supply on 1 and 3, out on 2)",
    'q04': "NTC thermistor: resistance falls as temperature rises",
    'q05': "LDR: resistance is highest in total darkness",
    'q06': "Ceramic (non-polarised) compared with electrolytic (polarised) capacitor",
    'q07': "Zener diode: Z-shaped cathode, designed for reverse breakdown",
    'q08': "Classification grid: MOSFET and op-amp are active, potentiometer and inductor are passive",
    'q09': "A BJT behaves as two junctions sharing one terminal \u2014 the base",
    'q10': "DMM in diode mode: RED probe on pin 2 gives 0.65 V to both other pins, so it is an NPN",
    'q11': "DMM in diode mode: BLACK probe on pin 1 gives 0.68 V to both other pins, so it is a PNP",
    'q12': "Splitting emitter from collector: V(BE) reads slightly higher than V(BC)",
    'q13': "DMM in diode mode, red probe on the base of a TO-92 BJT",
    'q14': "DMM test: BLACK probe on pin 2 (PNP), 0.655 V to pin 1 and 0.661 V to pin 3",
    'q15': "A healthy BJT reads OL across collector-emitter in both probe directions",
    'q16': "Faulty BJT: collector-emitter short circuit \u2014 the meter reads 0.000 V instead of OL",
    'q17': "Faulty BJT: both junctions open, so every probe combination reads OL",
    'q18': "Two discrete diodes back to back: no single common pin, so this is not a BJT",
    'q19': "Full CRO front panel \u2014 TIME/DIV sets the horizontal (time) scale",
    'q20': "Full CRO front panel \u2014 VOLTS/DIV sets the vertical (amplitude) scale",
    'q21': "Full CRO front panel \u2014 AC coupling blocks the DC level and centres the trace on 0 V",
    'q22': "Full CRO front panel \u2014 one graticule division measures 1 cm \u00d7 1 cm",
    'q23': "Full CRO front panel \u2014 VERTICAL POSITION slides the trace without changing its amplitude",
    'q24': "Full CRO showing a 4-division peak-to-peak trace at 5 V/div",
    'q25': "Full CRO showing one cycle spanning 5 divisions at 2 ms/div",
    'q26': "Full CRO: a 250 Hz signal at 1 ms/div occupies 4 horizontal divisions per cycle",
    'q27': "Full CRO: 14.14 Vrms gives a 4-division peak-to-peak trace at 10 V/div",
    'q28': "Full CRO on DC coupling: the trace sits between +1 and +5 divisions at 2 V/div",
    'q29': "Full CRO dual trace: signal B crosses zero 1 division after A in an 8-division cycle",
    'q30': "Full CRO in X-Y mode showing a Lissajous figure with 4 horizontal and 1 vertical tangency"
}


# Arrowhead markers, keyed by the id used in the diagram builders.
# Some builders (q04, q05) draw arrows but forget to emit <defs>; an invalid
# marker reference makes the browser drop the whole line, so we guarantee the
# markers exist for every reference we find.
MARKERS = {
    'ah':   ('#C9A227', 9, 'M0,1 L9,5 L0,9 z'),     # gold arrowhead
    'ahn':  ('#010080', 9, 'M0,1 L9,5 L0,9 z'),     # navy arrowhead
    'ahs':  ('#C9A227', 9, 'M0,1 L9,5 L0,9 z'),     # gold, small
    'ahsb': ('#C9A227', 1, 'M10,1 L1,5 L10,9 z'),   # gold, reversed
}


def ensure_defs(inner, qid):
    """Inject a <defs> block for any arrowhead the markup references but never defines."""
    def base(ref_id):
        # refs/ids are namespaced as "<marker>-<question id>"; recover the marker name
        return ref_id.split('-')[0]

    referenced = {base(r) for r in re.findall(r'url\(#([^)]+)\)', inner)}
    defined = {base(i) for i in re.findall(r'id="([^"]+)"', inner)}
    missing = {m for m in referenced if m in MARKERS} - defined
    if not missing:
        return inner
    parts = ['<defs>']
    for mid in sorted(missing):
        colour, refx, path = MARKERS[mid]
        parts.append(
            f'<marker id="{mid}-{qid}" viewBox="0 0 10 10" refX="{refx}" refY="5" '
            f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="{path}" fill="{colour}"/></marker>'
        )
    parts.append('</defs>')
    return ''.join(parts) + inner


def numeric_entities(text):
    """Named HTML entities (&mdash;) are undefined in XML, so an .svg file using
    them renders as a broken image. Numeric references work in both parsers."""
    def repl(m):
        name = m.group(1)
        if name in html.entities.name2codepoint:
            return '&#%d;' % html.entities.name2codepoint[name]
        return m.group(0)
    return re.sub(r'&([a-zA-Z][a-zA-Z0-9]*);', repl, text)


def inline_diagram(key, qid):
    """Turn a standalone diagram file into a responsive, name-spaced raw SVG string.

    - the embedded <style> block is dropped (those rules now live in styles.css,
      scoped under .diagram-svg, so they can never leak into the app's CSS)
    - width/height are removed so the figure scales with its container
    - marker ids are made unique per question so several figures can share a page
    """
    text = (DIAGRAM_DIR / f'{key}.svg').read_text()
    m = re.match(r'<svg[^>]*viewBox="0 0 (\d+) (\d+)"[^>]*>(.*)</svg>', text, re.S)
    if not m:
        raise SystemExit(f'{key}.svg: could not parse viewBox')
    width, height, inner = m.group(1), m.group(2), m.group(3)
    inner = re.sub(r'<style>.*?</style>', '', inner, flags=re.S)
    for mid in ('ah', 'ahn', 'ahs', 'ahsb'):
        inner = inner.replace(f'id="{mid}"', f'id="{mid}-{qid}"')
        inner = inner.replace(f'url(#{mid})', f'url(#{mid}-{qid})')
    inner = numeric_entities(inner)
    inner = ensure_defs(inner, qid)
    inner = re.sub(r'>\s+<', '><', inner).strip()
    inner = re.sub(r'\s{2,}', ' ', inner)
    cap = CAPTIONS.get(key, '')
    return (
        f'<svg class="diagram-svg" xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" preserveAspectRatio="xMidYMid meet" '
        f'role="img" aria-label="{cap}">{inner}</svg>'
    )


def clean_symbol(name):
    """A circuit symbol from the library, themed and made responsive."""
    svg = SYMBOLS[name]
    svg = svg.replace('#111111', '#010080')          # OAU navy
    svg = svg.replace(' width="100" height="60"', '')
    svg = svg.replace('<svg ', '<svg class="sym-svg" preserveAspectRatio="xMidYMid meet" ', 1)
    return re.sub(r'\s{2,}', ' ', svg).strip()


# ---------------------------------------------------------------------------
# The 20 components most often met in the EEE 282 bench course.
# (name, category, symbol key, primary uses)
# ---------------------------------------------------------------------------
COMPONENT_ROWS = [
    ('Resistor', 'Passive', 'Resistor (ANSI / zig-zag)',
     'Limits current, divides voltage, biases transistors and sets time constants with C or L.'),
    ('Potentiometer', 'Passive', 'Potentiometer (3-terminal)',
     'Variable voltage divider: full track across pins 1 and 3, output tapped from the wiper (pin 2). Volume, trim and reference-level controls.'),
    ('Rheostat / Variable resistor', 'Passive', 'Rheostat / variable resistor',
     'Two-terminal variable resistance for controlling current — lamp dimmers and motor speed in the lab.'),
    ('Thermistor (NTC)', 'Passive', 'Thermistor (NTC)',
     'Resistance falls as temperature rises. Temperature sensing, thermostats and inrush-current limiting.'),
    ('Light-dependent resistor (LDR)', 'Passive', 'Light-dependent resistor (LDR)',
     'Resistance is highest in darkness and falls in light. Street-light switches, light meters and opto-coupler inputs.'),
    ('Capacitor (non-polarised)', 'Passive', 'Capacitor (non-polarised)',
     'Ceramic/film types. Coupling and decoupling, timing networks, filters and oscillators — safe either way round.'),
    ('Capacitor (electrolytic)', 'Passive', 'Capacitor (polarised / electrolytic)',
     'Polarised high-value part for smoothing rectified DC, reservoir and bulk decoupling. Long lead positive; wrong polarity destroys it.'),
    ('Inductor', 'Passive', 'Inductor (air core)',
     'Stores energy in a magnetic field and opposes changes in current. Chokes, filters, tuned circuits and switching supplies.'),
    ('Transformer', 'Passive', 'Transformer (iron core)',
     'Steps AC voltage up or down and gives galvanic isolation. Mains adaptors and bench power supplies.'),
    ('Fuse', 'Passive', 'Fuse',
     'Sacrificial over-current protection: the element melts before the wiring or the circuit is damaged.'),
    ('Diode (PN junction)', 'Active', 'Diode',
     'Conducts in one direction only. Rectification, reverse-polarity protection and logic gating.'),
    ('LED', 'Active', 'LED (light-emitting diode)',
     'Emits light when forward biased. Indicators and displays; always needs a series resistor.'),
    ('Zener diode', 'Active', 'Zener diode',
     'Operates safely in reverse breakdown at a fixed voltage. Shunt voltage regulation and reference/ clipping.'),
    ('Bridge rectifier', 'Active', 'Bridge rectifier',
     'Four diodes in one package converting AC to pulsating DC — the front end of every bench supply.'),
    ('Photodiode', 'Active', 'Photodiode',
     'Converts light into current in reverse bias. Light sensing, optical receivers and isolators.'),
    ('NPN transistor (BJT)', 'Active', 'NPN transistor (BJT)',
     'Current-controlled switch and amplifier. Identified with the red meter probe on the base; V_BE > V_BC.'),
    ('PNP transistor (BJT)', 'Active', 'PNP transistor (BJT)',
     'Complementary BJT — high-side switching. Identified with the black meter probe on the base.'),
    ('N-channel MOSFET', 'Active', 'N-channel MOSFET (enhancement)',
     'Voltage-controlled switch with almost no gate current. Power switching, motor drivers and logic-level control.'),
    ('Operational amplifier', 'Active', 'Operational amplifier',
     'Very high gain differential amplifier. Comparators, buffers, summing, integrators and active filters.'),
    ('Voltage regulator (3-pin)', 'Active', 'Voltage regulator (3-pin)',
     'Fixed regulated DC output (e.g. 7805) from a higher, unregulated input — with input and output capacitors.'),
]


def component_symbols():
    rows = []
    for name, cat, key, uses in COMPONENT_ROWS:
        if key not in SYMBOLS:
            raise SystemExit(f'missing symbol: {key}')
        rows.append({'name': name, 'category': cat, 'symbol': clean_symbol(key), 'uses': uses})
    return rows
T = {
    'active': 'active-passive',
    'bjt': 'bjt-diagnostics',
    'cro': 'cro-controls',
    'calc': 'cro-calculations',
}

Q = []


def q(**kw):
    Q.append(kw)


# ===========================================================================
# TOPIC 1 — Active & Passive Components  (q01 - q08)
# ===========================================================================
q(id='eee282_q01', topicId=T['active'], kind='theory', type='mcq',
  image=IMG.format('q01'),
  question='Which fundamental property strictly distinguishes an active component from a passive component in an electrical circuit?',
  options=[
      'Active components dissipate energy, whereas passive components generate energy.',
      'Active components require an external power source to control electrical current or provide power gain.',
      'Passive components have non-linear voltage-current (V-I) characteristics.',
      'Passive components can amplify electrical signals without external power.',
  ], correct=1,
  short='Active parts need an external supply and can control current or deliver power gain; passive parts cannot add net energy to a circuit.',
  solution="""### The distinction
An **active** component needs an external power source to do its job and can use that supply to
*control* current or deliver **power gain** (amplification). A **passive** component cannot
introduce net energy: it only stores, dissipates or releases what is fed into it.

### Quick test
- Can it amplify, switch or rectify with the help of a supply rail? → **active**
  (transistor, diode, SCR, op-amp, MOSFET, LED, zener).
- Does it merely resist, store or transfer energy with no gain? → **passive**
  (resistor, capacitor, inductor, potentiometer, LDR, thermistor, transformer).

### Why the others are wrong
- *"Active dissipates, passive generates"* — exactly backwards. Dissipation is the passive
  signature (a resistor turns energy into heat); generation needs an active device plus a supply.
- *"Passive has non-linear V-I"* — non-linearity is **not** the test. A diode is non-linear and
  active; a thermistor is non-linear and passive.
- *"Passive can amplify without external power"* — amplification needs an energy source. Without
  one, the output power can never exceed the input power.""")

q(id='eee282_q02', topicId=T['active'], kind='theory', type='mcq', image=IMG.format('q02'),
  question='A standard PN junction diode is classified as an active component primarily because:',
  options=[
      'It stores electrical energy in a magnetic field.',
      'It possesses a non-linear V-I characteristic and controls current flow based on bias direction.',
      'It increases the total output power of an AC signal.',
      'It functions as a linear variable resistor.',
  ], correct=1,
  short='The diode is a semiconductor whose conduction depends on bias direction — it controls current rather than merely resisting it.',
  solution="""### Why the diode is active
A PN junction is a **semiconductor** device. Its behaviour depends on the *direction* of the applied
voltage: forward bias → conduction after about $0.7\\,\\text{V}$ (silicon); reverse bias → blocking.
That directional control of current is an active property.

### Reading the symbol (see figure)
- **Anode (A)** — P-type side, the plain triangle; connect to the **positive** rail for conduction.
- **Cathode (K)** — N-type side, the bar; the **band** printed on the body marks this end.
- Conventional current flows **anode → cathode**, i.e. in the direction the triangle points.

### Why the others are wrong
- *Stores energy in a magnetic field* → that is an **inductor** (passive).
- *Increases the output power of an AC signal* → a diode cannot amplify; it rectifies, and in fact
  it *loses* power across its junction drop.
- *Linear variable resistor* → a diode is deliberately **non-linear**; a potentiometer is the linear
  variable resistor.""")

q(id='eee282_q03', topicId=T['active'], kind='theory', type='text', image=IMG.format('q03'),
  question='When connecting a 3-terminal potentiometer as a variable voltage divider, across which two terminals is the input supply voltage connected, and from which terminal is the variable output tapped?',
  options=[
      'Input supply across terminals 1 and 3 (the two ends of the resistive track); output taken from terminal 2 (the wiper).',
      'Input supply across terminals 1 and 2; output taken from terminal 3.',
      'Input supply across terminals 2 and 3; output taken from terminal 1.',
      'Input supply to the wiper (terminal 2) and terminal 1; output taken from terminal 3.',
  ], correct=0,
  expected='Supply across the outer terminals 1 and 3; output tapped from the wiper, terminal 2.',
  match={'all': ['wiper', '1', '3'], 'any': ['2']},
  short='The full track sits between pins 1 and 3, so the supply goes there; the wiper (pin 2) is the slider that taps off any fraction of it.',
  solution="""### Potentiometer as a voltage divider
A potentiometer is one resistive track with a moving contact:

- **Terminals 1 and 3** — the two fixed ends of the track. The **whole** resistance $R$ lies
  between them, so the **supply is connected across 1 and 3**.
- **Terminal 2** — the **wiper** (slider). Its position sets the ratio, so the **output is taken
  from terminal 2** (usually with the other side of the output on terminal 1 or 3).

### The working equation
$$V_{out} = V_{in}\\times\\frac{R_{2\\to3}}{R_{1\\to3}}$$
At the bottom of the travel $V_{out}=0$; at the top $V_{out}=V_{in}$; everywhere between it varies
smoothly — which is exactly what "variable voltage divider" means.

### Exam traps
- Wiring the supply to the wiper and one end turns it into a **rheostat** (variable resistor), not
  a divider — you lose the ability to swing the output through the full range.
- Always confirm the pin numbering from the datasheet: on some trimmers the wiper is the middle
  pin, on others it is not.""")

q(id='eee282_q04', topicId=T['active'], kind='theory', type='mcq', image=IMG.format('q04'),
  question='How does the resistance of a Negative Temperature Coefficient (NTC) Thermistor behave as ambient temperature increases?',
  options=[
      'Resistance increases linearly.',
      'Resistance remains constant.',
      'Resistance decreases.',
      'Resistance drops abruptly to exactly zero.',
  ], correct=2,
  short='NTC = Negative Temperature Coefficient: heat frees more charge carriers, so resistance falls as temperature rises.',
  solution="""### NTC behaviour
Heat gives bound electrons in the semiconductor enough energy to become **free charge carriers**.
More carriers means **lower resistance**, so an NTC thermistor's resistance *falls* as temperature
*rises* — the "N" in NTC.

### Remember it this way
- **NTC** → **N**egative coefficient → temperature up, resistance **down**. Used for temperature
  sensing, inrush-current limiting, and thermostat inputs.
- **PTC** → **P**ositive coefficient → temperature up, resistance **up**. Used as a self-resetting
  fuse and for over-current protection.

### Why the others are wrong
- *Increases linearly* — that describes a PTC, and even then the curve is not perfectly linear.
- *Remains constant* — that is an ideal fixed resistor, not a thermistor.
- *Drops to exactly zero* — resistance falls steeply but never reaches zero; only a superconductor
  (not a thermistor) does that.""")

q(id='eee282_q05', topicId=T['active'], kind='theory', type='mcq', image=IMG.format('q05'),
  question='A Light Dependent Resistor (LDR) exhibits its highest resistance under which ambient condition?',
  options=['Direct sunlight', 'Total darkness', 'High temperature', 'High AC frequency input'],
  correct=1,
  short='Light creates carriers and lowers resistance, so the LDR is at its maximum resistance in total darkness.',
  solution="""### LDR behaviour
Photons striking the semiconductor free charge carriers. More light → more carriers → **lower
resistance**. In **total darkness** almost no carriers are freed, so the resistance is at its
maximum (typically hundreds of kΩ to MΩ, versus a few kΩ in bright light).

### Typical values to quote in the lab
- Dark: $R$ in the **MΩ** range.
- Bright light / direct sun: $R$ falls to **hundreds of Ω to a few kΩ**.

### Why the others are wrong
- *Direct sunlight* — that is where the resistance is **lowest**, not highest.
- *High temperature* — temperature is the thermistor's input variable, not the LDR's.
- *High AC frequency* — an LDR responds to light intensity, not to signal frequency.""")

q(id='eee282_q06', topicId=T['active'], kind='theory', type='mcq', image=IMG.format('q06'),
  question='Which capacitor type is polarized and requires strict terminal orientation during circuit assembly?',
  options=['Ceramic Capacitor', 'Mica Capacitor', 'Electrolytic Capacitor', 'Film Capacitor'],
  correct=2,
  short='Electrolytic capacitors are polarised — the oxide dielectric is formed electrochemically, so the positive lead must go to the positive rail.',
  solution="""### Polarised vs non-polarised
An **electrolytic** capacitor builds its dielectric as a microscopic **oxide layer** by
electrochemical action. Reverse that chemistry and the oxide breaks down: the part heats, vents and
can fail violently.

### Identification in the lab
- **Electrolytic** — long lead is **positive**, a printed **stripe with a minus sign** marks the
  negative side; values from about $1\\,\\mu\\text{F}$ upward, always polarised.
- **Ceramic / mica / film** — no polarity marking; safe to fit either way; usually pF to low µF.

### Exam trap
Fitting an electrolytic backwards is the single most common practical fault in a first-year power
supply. If a question mentions a smoothing capacitor on a rectifier, check the polarity first.

### Why the others are wrong
Ceramic, mica and film capacitors use a solid dielectric with no electrochemistry, so they are
non-polarised and orientation does not matter.""")

q(id='eee282_q07', topicId=T['active'], kind='theory', type='mcq', image=IMG.format('q07'),
  question='A Zener diode is specifically designed to operate safely in which region?',
  options=['Forward saturation region', 'Cut-off region', 'Reverse breakdown region', 'Ohmic linear region'],
  correct=2,
  short='A zener is doped to break down at a precise reverse voltage without damage — that constant voltage is what makes it a regulator.',
  solution="""### Zener operation
An ordinary diode is destroyed by reverse breakdown. A **zener** is doped so that breakdown occurs
at a precise, repeatable voltage ($V_Z$) and the device survives it. In that region the voltage
across it stays almost constant while the current changes — the basis of a **shunt regulator**.

### Series resistor is mandatory
A zener must **never** be connected straight across a supply. The series resistor $R_S$ limits the
current:
$$R_S = \\frac{V_{in}-V_Z}{I_Z}$$
Without it the zener exceeds its power rating and burns out.

### Why the others are wrong
- *Forward saturation / cut-off / ohmic linear* — these describe normal diode conduction or
  blocking. The zener's whole purpose is controlled **reverse breakdown**, which is why its symbol
  has the distinctive **Z-shaped cathode**.""")

q(id='eee282_q08', topicId=T['active'], kind='theory', type='text',
  image=IMG.format('q08'),
  question='Classify the following four components as either ACTIVE or PASSIVE: MOSFET, Potentiometer, Op-Amp, Inductor.',
  options=[
      'MOSFET: Active, Potentiometer: Passive, Op-Amp: Active, Inductor: Passive',
      'MOSFET: Passive, Potentiometer: Active, Op-Amp: Passive, Inductor: Active',
      'All four are active devices.',
      'All four are passive devices.',
  ], correct=0,
  expected='MOSFET: Active · Potentiometer: Passive · Op-Amp: Active · Inductor: Passive',
  match={'all': ['active', 'passive'],
         'minAny': {'n': 3, 'list': ['mosfet', 'potentiometer', 'op-amp', 'op amp', 'opamp', 'inductor']}},
  short='MOSFET and op-amp are active (both need a supply and give gain/control); potentiometer and inductor are passive.',
  solution="""### Classification
| Component | Class | Why |
|---|---|---|
| **MOSFET** | Active | Needs a supply; a gate voltage controls a much larger drain current → gain. |
| **Potentiometer** | Passive | A resistive divider. It *attenuates*; it can never add energy. |
| **Op-Amp** | Active | Needs supply rails and delivers very large voltage gain. |
| **Inductor** | Passive | Stores energy in a magnetic field and gives it back; no gain. |

### The one-line rule
Ask: *"Can this part use a power supply to control a bigger signal, or amplify?"* Yes → active.
No → passive.

### Why the other options are wrong
- Calling the MOSFET or op-amp passive ignores the supply pin and the gain they provide.
- Calling the potentiometer or inductor active confuses *control* (a knob) with *gain* — turning a
  knob does not inject energy into the circuit.""")

# ===========================================================================
# TOPIC 2 — BJT Pin & Type Diagnostics  (q09 - q18)
# ===========================================================================
q(id='eee282_q09', topicId=T['bjt'], kind='theory', type='mcq',
  image=IMG.format('q09'),
  question="When using a digital multimeter in Diode mode to identify a BJT's Base terminal, what specific reading pattern confirms you have found the Base?",
  options=[
      "A single pin that shows 'OL' to both other pins.",
      'A single pin that shows a forward voltage drop (approximately 0.6 V - 0.7 V) to BOTH of the other pins.',
      "A single pin that shows 0.000 V to one pin and 'OL' to the other.",
      'A pin that shows equal resistance in both directions.',
  ], correct=1,
  short='A BJT behaves like two diodes sharing one terminal. The base is the only pin that conducts (≈0.6–0.7 V) to both other pins with one probe polarity.',
  solution="""### The two-diodes model
A BJT is two PN junctions back-to-back sharing one terminal — the **base**:

- **NPN:** two diodes with their **anodes** tied together at the base.
- **PNP:** two diodes with their **cathodes** tied together at the base.

So with the correct probe polarity, **one pin** (the base) will show a junction drop of about
**0.6–0.7 V to each of the other two pins**.

### Procedure
1. Put the red probe on a candidate pin; touch black to the other two in turn.
2. If **both** read ≈0.6–0.7 V, the red probe is on the base of an **NPN**.
3. If both read `OL`, swap: black on that pin, red to the others. Two drops → **PNP**, base found.
4. Try the remaining pins until one gives the pattern.

### Why the others are wrong
- *OL to both pins* — that is the signature of the **collector-emitter** path on a healthy
  transistor, not the base.
- *0.000 V to one pin* — a dead short, which means a **faulty** device.
- *Equal resistance both ways* — that is a plain resistor, not a junction.""")

q(id='eee282_q10', topicId=T['bjt'], kind='theory', type='mcq',
  image=IMG.format('q10'),
  question='If placing the RED (positive) multimeter probe on Pin 2 yields a ~0.65 V drop to Pin 1 and a ~0.65 V drop to Pin 3, what is the polarity type of this transistor?',
  options=['PNP', 'NPN', 'JFET', 'MOSFET'], correct=1,
  short='Red probe common = NPN. The red lead supplies positive bias, so the shared pin must be P-type material between two N regions.',
  solution="""### Reasoning
A meter in diode mode pushes current out of its **red** lead. If red sits on one pin and both other
pins show a forward drop, red must be on the **anodes** of both junctions — i.e. the **P-type**
middle layer. P between two N layers is **NPN**.

### Memory aid
- **Red common → NPN** ("Red = N ot Pointing iN", or simply red = positive = anode = P-material).
- **Black common → PNP.** (Black is the negative/com lead; it sits on the N-type middle layer.)

### Why the others are wrong
- *PNP* would need the **black** probe on the common pin to show the two drops.
- *JFET / MOSFET* are not identified this way — a FET has no gate junction drop, and its
  drain-source path behaves like a resistor or a protected diode, not two junction drops.""")

q(id='eee282_q11', topicId=T['bjt'], kind='theory', type='mcq',
  image=IMG.format('q11'),
  question='If placing the BLACK (negative) multimeter probe on Pin 1 yields a ~0.68 V drop to Pin 2 and a ~0.68 V drop to Pin 3, what is the polarity type of this transistor?',
  options=['PNP', 'NPN', 'Zener', 'SCR'], correct=0,
  short='Black probe common = PNP. Black is the negative lead, so the shared pin is the N-type middle layer between two P regions.',
  solution="""### Reasoning
With **black** (COM, negative) on one pin and a forward drop to both others, current is flowing
*out of* the other two pins *into* the black lead. That means the shared pin is the **cathodes**
side — the **N-type** middle layer. N between two P layers is **PNP**.

### Pair it with q10
| Common probe | Reading | Device |
|---|---|---|
| Red on the pin | ≈0.6 V to both other pins | **NPN** |
| Black on the pin | ≈0.6 V to both other pins | **PNP** |

### Why the others are wrong
- *NPN* requires the **red** probe on the common pin.
- *Zener / SCR* — a zener is a two-terminal device; an SCR has a gate but its anode-cathode path
  reads `OL` both ways, so neither produces this three-pin two-drop pattern.""")

q(id='eee282_q12', topicId=T['bjt'], kind='theory', type='mcq',
  image=IMG.format('q12'),
  question="Once the Base terminal is identified, how do you distinguish the Emitter pin from the Collector pin using the multimeter's voltage drop readings?",
  options=[
      'The Base-Collector junction always has a higher voltage drop than the Base-Emitter junction.',
      'The Base-Emitter junction always has a slightly higher voltage drop than the Base-Collector junction.',
      "The Emitter pin will show an 'OL' reading.",
      'The Collector pin will beep in continuity mode.',
  ], correct=1,
  short='The emitter is more heavily doped than the collector, so V_BE reads a few millivolts higher than V_BC — the higher drop is the emitter.',
  solution="""### The doping rule
In a BJT the **emitter is heavily doped** and the **collector is lightly doped** (so it can sustain
a large reverse voltage). Heavier doping gives a **slightly larger junction drop**, so:

$$V_{BE} > V_{BC}\\quad\\text{(by roughly 5–15 mV)}$$

### Worked example
Base found with red on pin 2; black to pin 1 reads **0.712 V**, black to pin 3 reads **0.704 V**.
The **larger** reading, 0.712 V, is the **emitter** → pin 1. Pin 3 is the collector.

### Why the others are wrong
- *Base-Collector higher* — the reverse of the physics; the collector is the lightly doped side.
- *Emitter reads OL* — an `OL` reading means an open circuit, which would be a **faulty** device.
- *Collector beeps in continuity* — a healthy collector-emitter path does not conduct at all.

### Exam tip
The difference is small, so **write both readings down to the millivolt** before deciding. If the
two drops are identical to the last digit, re-measure — one of them will be higher.""")

q(id='eee282_q13', topicId=T['bjt'], kind='theory', type='text', image=IMG.format('q13'),
  question='You are testing an unknown transistor. With the RED probe on Pin 3, you measure 0.712 V on Pin 1 and 0.704 V on Pin 2. Identify the Type (NPN/PNP), Base, Emitter and Collector pins.',
  options=[
      'NPN — Base = Pin 3, Emitter = Pin 1, Collector = Pin 2',
      'NPN — Base = Pin 3, Emitter = Pin 2, Collector = Pin 1',
      'PNP — Base = Pin 3, Emitter = Pin 1, Collector = Pin 2',
      'NPN — Base = Pin 1, Emitter = Pin 3, Collector = Pin 2',
  ], correct=0,
  expected='Type: NPN · Base = Pin 3 · Emitter = Pin 1 (0.712 V) · Collector = Pin 2 (0.704 V)',
  match={'all': ['npn', '1', '2', '3']},
  short='Red common → NPN, so pin 3 is the base. The higher drop (0.712 V on pin 1) is the emitter; 0.704 V on pin 2 is the collector.',
  solution="""### Step 1 — Find the base and the type
The **red** probe is fixed on **pin 3** and *both* other pins show a junction drop, so pin 3 is the
common pin → **base**, and **red common means NPN**.

### Step 2 — Split emitter from collector
Compare the two readings:

- Pin 1 → **0.712 V** (larger)
- Pin 2 → **0.704 V** (smaller)

The emitter is more heavily doped, so $V_{BE} > V_{BC}$.
**Larger drop = emitter → pin 1.** Therefore **pin 2 is the collector**.

### Answer
| Quantity | Value |
|---|---|
| Type | **NPN** |
| Base | **Pin 3** |
| Emitter | **Pin 1** (0.712 V) |
| Collector | **Pin 2** (0.704 V) |

### Why the other options are wrong
- Swapping emitter/collector ignores the doping rule (the 8 mV difference is the whole clue).
- Calling it PNP contradicts "red probe common".
- Making pin 1 the base contradicts the statement that the *fixed* probe was on pin 3.""")

q(id='eee282_q14', topicId=T['bjt'], kind='theory', type='text',
  image=IMG.format('q14'),
  question='You are testing a transistor. With the BLACK probe on Pin 2, you measure 0.655 V on Pin 1 and 0.661 V on Pin 3. Identify the Type (NPN/PNP), Base, Emitter and Collector pins.',
  options=[
      'PNP — Base = Pin 2, Emitter = Pin 3, Collector = Pin 1',
      'PNP — Base = Pin 2, Emitter = Pin 1, Collector = Pin 3',
      'NPN — Base = Pin 2, Emitter = Pin 3, Collector = Pin 1',
      'PNP — Base = Pin 1, Emitter = Pin 3, Collector = Pin 2',
  ], correct=0,
  expected='Type: PNP · Base = Pin 2 · Emitter = Pin 3 (0.661 V) · Collector = Pin 1 (0.655 V)',
  match={'all': ['pnp', '1', '2', '3']},
  short='Black common → PNP, so pin 2 is the base. The higher drop (0.661 V on pin 3) is the emitter; 0.655 V on pin 1 is the collector.',
  solution="""### Step 1 — Find the base and the type
The **black** probe is fixed on **pin 2** and both other pins show a drop → pin 2 is the **base**,
and **black common means PNP**.

### Step 2 — Split emitter from collector
- Pin 1 → 0.655 V
- Pin 3 → **0.661 V** (larger)

Larger drop = **emitter** → **pin 3**. So **pin 1 is the collector**.

### Answer
| Quantity | Value |
|---|---|
| Type | **PNP** |
| Base | **Pin 2** |
| Emitter | **Pin 3** (0.661 V) |
| Collector | **Pin 1** (0.655 V) |

### Exam tip
The gap here is only **6 mV**. Decide nothing from memory of "pin order" — always let the larger
number name the emitter. This is the classic question where students lose a mark by assuming the
emitter is always a particular physical pin.""")

q(id='eee282_q15', topicId=T['bjt'], kind='theory', type='mcq',
  image=IMG.format('q15'),
  question="When testing a healthy BJT in Diode mode, what reading should you get if you place your probes directly across the Collector and Emitter pins?",
  options=[
      'Approximately 0.6 V in one direction, OL in the other.',
      "'OL' (Open Loop) in both directions.",
      '0.000 V in both directions.',
      'The sum of the two base junction voltage drops (approximately 1.2 V).',
  ], correct=1,
  short='Collector-emitter is two junctions back-to-back, so one is always reverse-biased: a healthy BJT reads OL both ways across C-E.',
  solution="""### Why OL both ways
Between collector and emitter the current would have to cross **two junctions in series**, and
whichever polarity you choose, **one of them is reverse-biased**. No current flows, so the meter
shows `OL` in **both** directions.

### This is your health check
- C-E reads **OL both ways** → junctions are intact (keep going; identify the pins).
- C-E reads **0.000 V** → **shorted** C-E: the device is faulty.
- Everything reads **OL** → **open** junctions: the device is blown.

### Why the others are wrong
- *0.6 V one way, OL the other* — that is a **single** junction (base-emitter or base-collector),
  not the C-E path.
- *0.000 V* — a short circuit, i.e. a failed transistor.
- *≈1.2 V* — you cannot add the two drops in series because one junction is always reverse-biased.""")

q(id='eee282_q16', topicId=T['bjt'], kind='theory', type='text',
  image=IMG.format('q16'),
  question='You test a transistor and find the Base is Pin 1 (NPN). However, when you measure between Pin 2 and Pin 3, the multimeter reads 0.000 V. What is the condition of this transistor?',
  options=[
      'The transistor is faulty — the collector and emitter are short-circuited.',
      'The transistor is healthy and is an NPN.',
      'The transistor is healthy and is a PNP.',
      'The transistor is faulty — the base junction is open circuit.',
  ], correct=0,
  expected='Faulty — collector-emitter short circuit (C-E should read OL on a healthy BJT).',
  match={'any': ['faulty', 'short', 'shorted', 'blown', 'damaged', 'dead', 'open']},
  short='A healthy C-E path must read OL. 0.000 V means the silicon has failed into a short, so the transistor is dead.',
  solution="""### Diagnosis
On a healthy BJT the collector-emitter path reads **`OL` in both directions** (two opposing
junctions). A reading of **0.000 V** means the meter sees a **dead short** — the semiconductor
material between those pins has broken down and fused.

### Verdict
**The transistor is faulty — short-circuited collector to emitter.** Bin it; do not build with it.

### Fault table for revision
| Measurement | Meaning |
|---|---|
| C-E reads `OL` both ways | Healthy — expected result |
| C-E reads `0.000 V` | **Shorted** C-E → faulty |
| No junction drop anywhere | **Open** junctions → faulty (blown) |
| Junction drop on base + C-E short | Partly shorted → faulty |

### Why the other options are wrong
- "Healthy" is impossible with a C-E short: the device can no longer block voltage.
- An **open** base junction would read `OL`, not `0.000 V`.""")

q(id='eee282_q17', topicId=T['bjt'], kind='theory', type='mcq',
  image=IMG.format('q17'),
  question="If every possible probe combination on a 3-pin BJT yields an 'OL' reading on your multimeter, what does this indicate?",
  options=[
      'It is a healthy NPN transistor.',
      'The multimeter is in the wrong mode; it must be in Ohms.',
      'The transistor is faulty (internally open/blown).',
      'It is a healthy PNP transistor.',
  ], correct=2,
  short='No forward drop on any of the six probe combinations means both junctions are open — the transistor is blown.',
  solution="""### Reasoning
A good BJT must show **two** forward drops (base→emitter and base→collector). If all **six** probe
combinations read `OL`, **neither junction conducts**: both are open circuit. The device is
**faulty (internally open / blown)**.

### Before you condemn it — check yourself
1. Meter is in **diode mode**, leads in the **VΩ / diode** jacks (not the 10 A jack).
2. The transistor is **out of circuit**; in-circuit readings are unreliable.
3. Leads are actually touching the pins (oxidation or a breadboard can fool you).
4. Compare against a known-good transistor to confirm the meter works.

### Why the others are wrong
- A healthy NPN or PNP **must** show two junction drops — `OL` everywhere is impossible.
- Ohms mode usually cannot forward-bias a silicon junction (its test voltage is too low), so the
  Ohms suggestion would make the problem worse, not fix it.""")

q(id='eee282_q18', topicId=T['bjt'], kind='theory', type='mcq',
  image=IMG.format('q18'),
  question="You are probing a component with Red on Pin 1. Pin 2 shows 0.6 V and Pin 3 shows 'OL'. Switching to Black on Pin 1, Pin 2 shows 'OL' and Pin 3 shows 0.6 V. Is this a BJT?",
  options=[
      'Yes, it is an NPN.',
      'Yes, it is a PNP.',
      'No, a BJT must have a single common pin that conducts to both other pins with the same polarity.',
      'Yes, but the Base is broken.',
  ], correct=2,
  short='No — a BJT needs one pin that reads a drop to BOTH other pins with the SAME probe polarity. This pattern is two back-to-back diodes or two discrete diodes.',
  solution="""### The BJT signature
A BJT is two diodes sharing a node, so there **must** exist one pin and one probe polarity that
forward-biases **both** junctions at once. Here:

- Red on pin 1 → pin 2 conducts (0.6 V), pin 3 does **not** (`OL`).
- Black on pin 1 → pin 3 conducts (0.6 V), pin 2 does **not** (`OL`).

No single polarity on pin 1 reaches both pins, and repeating the test on pins 2 and 3 gives the
same "one conducts, one doesn't" pattern. **No common pin → not a BJT.**

### What it could be
Two **discrete diodes wired back-to-back** (or a diode network / a triac-like structure). Each
junction works on its own, but they do not share a base.

### Why the other options are wrong
- *NPN / PNP* — both require a pin that shows a drop to the other two **simultaneously**.
- *"Base is broken"* — if the base were open you would read `OL` on **every** combination, not
  0.6 V on four of them.""")

# ===========================================================================
# TOPIC 3 — CRO Controls & Functions  (q19 - q23)
# ===========================================================================
q(id='eee282_q19', topicId=T['cro'], kind='theory', type='mcq',
  image=IMG.format('q19'),
  question='Which control knob on a Cathode Ray Oscilloscope (CRO) adjusts the horizontal scale of the displayed waveform?',
  options=['Volts/Div', 'Focus Control', 'Time/Div (Time Base)', 'Vertical Position'], correct=2,
  short='Time/Div (the time base) sets how much time each horizontal division represents — the horizontal scale.',
  solution="""### The two axes
- **Horizontal axis = time** → controlled by **Time/Div** (the time base, in s/div, ms/div or µs/div).
- **Vertical axis = voltage** → controlled by **Volts/Div**.

### Using it
$$T = (\\text{divisions per cycle}) \\times (\\text{Time/Div setting}),\\qquad f = \\frac{1}{T}$$
Increase Time/Div and the trace spreads out horizontally, showing fewer cycles; decrease it and you
see more cycles in less detail.

### Why the others are wrong
- *Volts/Div* — the vertical (amplitude) scale.
- *Focus* — sharpness of the spot; it changes clarity, not scale.
- *Vertical Position* — moves the trace up and down; it does not rescale anything.""")

q(id='eee282_q20', topicId=T['cro'], kind='theory', type='mcq',
  image=IMG.format('q20'),
  question='The primary function of the Volts/Div knob on a CRO is to:',
  options=[
      'Alter the frequency of the input signal.',
      'Set the vertical amplitude scale (voltage represented per division).',
      'Adjust the electron beam sharpness.',
      'Shift the wave horizontally along the time axis.',
  ], correct=1,
  short='Volts/Div sets the vertical sensitivity: how many volts each vertical division represents.',
  solution="""### Volts/Div = vertical sensitivity
It scales the vertical deflection, fixing how many **volts** one vertical division represents
(e.g. 2 V/div, 5 V/div). Everything amplitude-related is read with it:
$$V_{p\\text{-}p} = (\\text{vertical divisions}) \\times (\\text{Volts/Div})$$

### Practical note
Turning the knob to a **smaller** V/div magnifies the waveform vertically — useful for small
signals, but it also magnifies noise and can drive the trace off-screen.

### Why the others are wrong
- *Alter the frequency* — a CRO never changes the signal; it only displays it.
- *Beam sharpness* — that is **Focus** (with **Intensity** for brightness).
- *Shift the wave horizontally* — that is **Horizontal Position** (or the trigger level).""")

q(id='eee282_q21', topicId=T['cro'], kind='theory', type='mcq',
  image=IMG.format('q21'),
  question="When the input coupling switch of a CRO channel is set to 'AC Coupling', what happens to the incoming signal?",
  options=[
      'The AC component is blocked, passing only DC voltage.',
      'A series capacitor blocks any DC offset voltage, passing only the AC signal.',
      'The signal is directly grounded.',
      'The signal amplitude is multiplied by a factor of 10.',
  ], correct=1,
  short='AC coupling puts a capacitor in series: it strips the DC level and passes only the varying part of the signal.',
  solution="""### AC vs DC vs GND
- **DC coupling** — the signal is connected straight through. You see **AC + DC** together, so you
  can measure a DC offset directly (needed for questions like q28).
- **AC coupling** — a **series capacitor** blocks the DC component, so the trace centres on zero
  and shows only the **varying** part. Ideal for inspecting a small ripple sitting on a large DC
  rail.
- **GND** — the input is grounded; the trace shows the **0 V reference**, which is how you position
  the zero baseline before measuring.

### Why the others are wrong
- *"AC is blocked, DC passes"* — backwards: the capacitor **blocks DC**.
- *Signal grounded* — that is the **GND** coupling position, not AC.
- *×10* — amplitude scaling is done by the **Volts/Div** knob or a ×10 **probe**, not by coupling.""")

q(id='eee282_q22', topicId=T['cro'], kind='theory', type='calc',
  image=IMG.format('q22'),
  question='What is the standard physical dimension of one major box grid (graticule) on a typical CRO screen display?',
  options=['1 cm × 1 cm', '0.5 cm × 0.5 cm', '2 cm × 2 cm', '1 inch × 1 inch'], correct=0,
  num={'values': [1], 'unit': 'cm'},
  expected='1 cm × 1 cm (one division)',
  short='One major graticule division is 1 cm × 1 cm on a standard CRO screen.',
  solution="""### The graticule
The screen is etched (or drawn) with a grid of **major divisions**, each **1 cm × 1 cm**. A typical
display is **8 vertical × 10 horizontal** divisions, and the minor ticks subdivide each major
division into **5**.

### Why it matters
Every CRO measurement is a count of divisions:
- Amplitude: $V_{p\\text{-}p} = \\text{vertical divisions} \\times \\text{Volts/Div}$
- Time: $T = \\text{horizontal divisions} \\times \\text{Time/Div}$

### Why the others are wrong
- 0.5 cm and 2 cm are not the standard major division; 1 **inch** (2.54 cm) is far too large for
  an oscilloscope graticule.""")

q(id='eee282_q23', topicId=T['cro'], kind='theory', type='mcq',
  image=IMG.format('q23'),
  question='Which control knob is adjusted to shift the entire displayed waveform up or down without altering its peak magnitude?',
  options=['Horizontal Position Knob', 'Vertical Position Knob', 'Intensity Knob', 'Volts/Div Knob'], correct=1,
  short='The Vertical Position knob adds a DC offset to the deflection, sliding the whole trace up or down without changing its amplitude.',
  solution="""### Vertical Position
It injects a small DC bias into the vertical deflection system, translating the **whole** trace up
or down. The peak-to-peak amplitude is unchanged — only where the trace sits on the screen changes.

### Classic use
1. Set coupling to **GND** — the trace becomes a flat line at the true **0 V** level.
2. Use **Vertical Position** to park that line on the centre graticule line.
3. Switch back to **DC** coupling — now every amplitude and DC-offset measurement is referenced to
   a known zero.

### Why the others are wrong
- *Horizontal Position* — moves the trace left/right in time.
- *Intensity* — brightness of the trace.
- *Volts/Div* — this **does** change the displayed magnitude, which the question rules out.""")

# ===========================================================================
# TOPIC 4 — CRO Waveform Calculations  (q24 - q30)
# ===========================================================================
q(id='eee282_q24', topicId=T['calc'], kind='calc', type='calc', image=IMG.format('q24'),
  question='A sinusoidal wave covers 4 vertical major divisions from its lowest trough to its highest peak. If the Volts/Div knob is set to 5 V/div, calculate: (i) Peak-to-Peak Voltage (Vp-p), (ii) Peak Voltage (Vp), and (iii) RMS Voltage (Vrms).',
  options=[
      'Vp-p = 20 V, Vp = 10 V, Vrms = 7.07 V',
      'Vp-p = 20 V, Vp = 10 V, Vrms = 14.14 V',
      'Vp-p = 10 V, Vp = 20 V, Vrms = 7.07 V',
      'Vp-p = 20 V, Vp = 5 V, Vrms = 3.54 V',
  ], correct=0,
  num={'values': [20, 10, 7.07], 'unit': 'V'},
  expected='Vp-p = 20 V, Vp = 10 V, Vrms = 7.07 V',
  short='Vp-p = 4 div × 5 V/div = 20 V; Vp = 10 V; Vrms = 0.707 × 10 = 7.07 V.',
  solution="""### Step 1 — Peak-to-peak from the screen
The trough-to-peak height is 4 divisions, and each division is 5 V:
$$V_{p\\text{-}p} = 4\\ \\text{div} \\times 5\\ \\frac{\\text{V}}{\\text{div}} = 20\\ \\text{V}$$

### Step 2 — Peak value
$$V_p = \\frac{V_{p\\text{-}p}}{2} = \\frac{20}{2} = 10\\ \\text{V}$$

### Step 3 — RMS
For a sine wave:
$$V_{rms} = 0.707\\,V_p = 0.707 \\times 10 = 7.07\\ \\text{V}$$

### Answer
**Vp-p = 20 V, Vp = 10 V, Vrms = 7.07 V**

### Distractor analysis
- **14.14 V** — that is $V_{rms}$ if you (wrongly) start from $V_{p\\text{-}p}=20$ and use
  $V_{rms}=V_{p\\text{-}p}\\times0.707$. Never: RMS is **0.707 × peak**, not 0.707 × peak-to-peak.
- **Vp-p = 10, Vp = 20** — the halves are swapped; peak can never exceed peak-to-peak.
- **Vp = 5 V** — that halves the peak-to-peak **twice** (or mistakes 4 div for 2 div).

### Exam tip
Always write the units next to the division count *before* you multiply; most lost marks on CRO
questions are unit slips, not arithmetic slips.""")

q(id='eee282_q25', topicId=T['calc'], kind='calc', type='calc', image=IMG.format('q25'),
  question='One complete cycle of a periodic signal spans 5 horizontal divisions on a CRO screen. The Time/Div knob is set to 2 ms/div. Calculate: (i) Period of the signal (T in seconds), and (ii) Frequency of the signal (f in Hz).',
  options=[
      'T = 0.01 s (10 ms), f = 100 Hz',
      'T = 0.01 s (10 ms), f = 10 Hz',
      'T = 0.1 s (100 ms), f = 10 Hz',
      'T = 10 s, f = 0.1 Hz',
  ], correct=0,
  num={'values': [0.01, 100], 'unit': 's and Hz'},
  expected='T = 0.01 s (10 ms), f = 100 Hz',
  short='T = 5 div × 2 ms/div = 10 ms = 0.01 s; f = 1/T = 1/0.01 = 100 Hz.',
  solution="""### Step 1 — Period from the screen
One cycle occupies 5 divisions at 2 ms per division:
$$T = 5\\ \\text{div} \\times 2\\ \\frac{\\text{ms}}{\\text{div}} = 10\\ \\text{ms} = 0.01\\ \\text{s}$$

### Step 2 — Frequency
$$f = \\frac{1}{T} = \\frac{1}{0.01\\ \\text{s}} = 100\\ \\text{Hz}$$

### Answer
**T = 0.01 s (10 ms), f = 100 Hz**

### Distractor analysis
- **f = 10 Hz** — comes from treating 10 ms as 0.1 s. Check the prefix: **milli** = $10^{-3}$, so
  10 ms = 0.010 s.
- **T = 0.1 s** — a factor-of-ten slip on the same prefix conversion.
- **T = 10 s** — forgetting to convert ms to s entirely.

### Exam tip
Convert to **base units before** you divide: $T$ in seconds → $f$ in hertz, no surprises.""")

q(id='eee282_q26', topicId=T['calc'], kind='calc', type='calc',
  image=IMG.format('q26'),
  question='A sine wave signal has a frequency of 250 Hz. If the Time/Div knob on the CRO is set to 1 ms/div, how many horizontal major divisions will ONE complete cycle occupy on the screen?',
  options=['4 horizontal divisions', '2.5 horizontal divisions', '250 horizontal divisions', '0.4 horizontal divisions'],
  correct=0,
  num={'values': [4], 'unit': 'divisions'},
  expected='4 horizontal divisions',
  short='T = 1/250 = 0.004 s = 4 ms; at 1 ms/div that is 4 divisions.',
  solution="""### Step 1 — Period from frequency
$$T = \\frac{1}{f} = \\frac{1}{250} = 0.004\\ \\text{s} = 4\\ \\text{ms}$$

### Step 2 — Convert the period into divisions
$$\\text{Divisions} = \\frac{T}{\\text{Time/Div}} = \\frac{4\\ \\text{ms}}{1\\ \\text{ms/div}} = 4\\ \\text{divisions}$$

### Answer
**4 horizontal divisions**

### Distractor analysis
- **2.5 divisions** — inverting the ratio ($1\\text{ ms} / 4\\text{ ms}$ style error) or mixing up
  $f$ and $T$.
- **250 divisions** — using the frequency number as if it were a time.
- **0.4 divisions** — the reciprocal again, from dividing time-base by period.

### Sanity check
A 250 Hz signal with a 1 ms/div setting shows 4 cycles across a 10-division screen (40 ms total).
If your answer implies less than one cycle or hundreds of cycles, re-check the conversion.""")

q(id='eee282_q27', topicId=T['calc'], kind='calc', type='calc',
  image=IMG.format('q27'),
  question='A pure AC sine wave with an RMS voltage of 14.14 V is measured on a CRO set to 10 V/div. How many vertical divisions peak-to-peak will this wave occupy?',
  options=['4 vertical divisions peak-to-peak', '2 vertical divisions peak-to-peak',
           '8 vertical divisions peak-to-peak', '1.414 vertical divisions peak-to-peak'],
  correct=0,
  num={'values': [4], 'unit': 'divisions'},
  expected='4 vertical divisions peak-to-peak',
  short='Vp = 1.414 × 14.14 = 20 V; Vp-p = 40 V; at 10 V/div that is 4 divisions.',
  solution="""### Step 1 — RMS to peak
For a sine wave, $V_p = 1.414\\,V_{rms}$:
$$V_p = 1.414 \\times 14.14 = 20\\ \\text{V}$$

### Step 2 — Peak to peak-to-peak
$$V_{p\\text{-}p} = 2V_p = 2 \\times 20 = 40\\ \\text{V}$$

### Step 3 — Voltage into divisions
$$\\text{Divisions} = \\frac{V_{p\\text{-}p}}{\\text{Volts/Div}} = \\frac{40\\ \\text{V}}{10\\ \\text{V/div}} = 4\\ \\text{divisions}$$

### Answer
**4 vertical divisions peak-to-peak**

### Distractor analysis
- **2 divisions** — using $V_p$ (20 V) instead of $V_{p\\text{-}p}$ (40 V) in the last step.
- **8 divisions** — using $V_{rms}\\times2 = 28.28$ V and then rounding upward, or doubling twice.
- **1.414 divisions** — mistaking the *conversion constant* for the answer.

### Note on 14.14 V
Examiners pick 14.14 V on purpose: $14.14 \\times 1.414 \\approx 20$, a clean round number. When you
see 14.14 or 7.07, expect a factor of $\\sqrt{2}$ to be involved.""")

q(id='eee282_q28', topicId=T['calc'], kind='calc', type='calc', image=IMG.format('q28'),
  question='A signal displayed on a CRO set to DC coupling lies entirely above the zero baseline. The positive peak is at +5 divisions and the negative trough is at +1 division. The Volts/Div knob is at 2 V/div. Calculate: (i) Vp-p, (ii) AC Peak Voltage Vp, and (iii) DC Offset Voltage.',
  options=[
      'Vp-p = 8 V, Vp = 4 V, DC offset = 6 V',
      'Vp-p = 8 V, Vp = 4 V, DC offset = 4 V',
      'Vp-p = 12 V, Vp = 6 V, DC offset = 6 V',
      'Vp-p = 8 V, Vp = 8 V, DC offset = 6 V',
  ], correct=0,
  num={'values': [8, 4, 6], 'unit': 'V'},
  expected='Vp-p = 8 V, Vp = 4 V, DC offset = 6 V',
  short='Vp-p = (5−1) div × 2 = 8 V; Vp = 4 V; DC offset = midpoint (5+1)/2 = 3 div × 2 = 6 V.',
  solution="""### Reading the screen
Positive peak = **+5 div**, negative trough = **+1 div**, so the wave never crosses zero — a DC
level is lifting the whole sine wave.

### Step 1 — Peak-to-peak
$$V_{p\\text{-}p} = (5 - 1)\\ \\text{div} \\times 2\\ \\frac{\\text{V}}{\\text{div}} = 4 \\times 2 = 8\\ \\text{V}$$

### Step 2 — AC peak
$$V_p = \\frac{V_{p\\text{-}p}}{2} = \\frac{8}{2} = 4\\ \\text{V}$$

### Step 3 — DC offset (the mean level)
The DC level sits midway between the two extremes:
$$V_{DC} = \\frac{5 + 1}{2}\\ \\text{div} \\times 2\\ \\frac{\\text{V}}{\\text{div}} = 3 \\times 2 = 6\\ \\text{V}$$

### Answer
**Vp-p = 8 V, Vp = 4 V, DC offset = 6 V DC**

### Distractor analysis
- **DC offset = 4 V** — using $V_p$ as the offset. The offset is the **midpoint**, not the peak.
- **Vp-p = 12 V** — adding the divisions (5 + 1) instead of subtracting them.
- **Vp = 8 V** — failing to halve the peak-to-peak value.

### Exam tip
This is exactly why you park the trace on the centre line with the coupling in **GND** before
measuring: with DC coupling, "0 V" is not wherever the trace happens to sit.""")

q(id='eee282_q29', topicId=T['calc'], kind='calc', type='calc', image=IMG.format('q29'),
  question='In a dual-trace CRO phase measurement, one complete cycle of Signal A spans 8 horizontal divisions. Signal B passes through zero exactly 1 horizontal division after Signal A. Calculate the phase shift angle between the two signals in degrees.',
  options=['45°', '90°', '30°', '360°'], correct=0,
  num={'values': [45], 'unit': 'degrees'},
  expected='45°',
  short='Phase = (1 div / 8 div) × 360° = 45°.',
  solution="""### The phase formula
One full cycle = $360^\\circ$ = the number of divisions in one period (here, 8). So:
$$\\phi = \\frac{\\text{shift in divisions}}{\\text{divisions per cycle}} \\times 360^\\circ$$

### Substitution
$$\\phi = \\frac{1}{8} \\times 360^\\circ = 45^\\circ$$

### Answer
**45°** (Signal B lags Signal A by 45°.)

### Distractor analysis
- **90°** — assumes the shift is a quarter of a cycle (2 divisions) instead of one-eighth.
- **30°** — a guess based on 12 divisions per cycle, not the 8 given.
- **360°** — that is one **whole** cycle; a 1-division shift out of 8 is far smaller.

### Exam tips
- The answer is independent of the Time/Div setting — both the shift and the period are measured in
  the **same** divisions, so the setting cancels out.
- Only use this when **both** traces are on the same Time/Div setting (they always are on a
  dual-trace CRO).""")

q(id='eee282_q30', topicId=T['calc'], kind='calc', type='calc', image=IMG.format('q30'),
  question='A CRO in X-Y mode displays a Lissajous pattern. A reference frequency fx = 50 Hz is applied to the X-input. The pattern shows 4 horizontal tangency points and 1 vertical tangency point. Calculate the unknown frequency fy applied to the Y-input.',
  options=['200 Hz', '12.5 Hz', '50 Hz', '800 Hz'], correct=0,
  num={'values': [200], 'unit': 'Hz'},
  expected='200 Hz',
  short='fy/fx = horizontal tangencies / vertical tangencies = 4/1, so fy = 4 × 50 = 200 Hz.',
  solution="""### The Lissajous ratio
$$\\frac{f_y}{f_x} = \\frac{\\text{number of horizontal tangencies}}{\\text{number of vertical tangencies}}$$

### Substitution
$$\\frac{f_y}{50} = \\frac{4}{1} \\quad\\Rightarrow\\quad f_y = 4 \\times 50 = 200\\ \\text{Hz}$$

### Answer
**200 Hz**

### How to count tangencies
- **Horizontal tangency** — count how many points the curve touches a **horizontal** line drawn
  across the pattern (equivalently, the number of horizontal "lobes").
- **Vertical tangency** — the number of points touching a **vertical** line.
Do not count intersections with the graticule; count the **touching points on the outline** of the
figure.

### Distractor analysis
- **12.5 Hz** — the ratio inverted ($1/4 \\times 50$).
- **50 Hz** — assumes equal frequencies, which would give a circle/ellipse (1:1).
- **800 Hz** — multiplying by 16 instead of 4, usually from counting both axes' lobes together.

### Exam tip
This method only works when the two frequencies are in a **simple integer ratio**; otherwise the
figure drifts and cannot be read.""")

# ===========================================================================
# Course / topic metadata
# ===========================================================================
COURSE = {
    'id': 'eee282',
    'code': 'EEE 282',
    'title': 'Electronic & Electrical Introductory Practicals II',
    'blurb': ('Practical-first preparation for the EEE 282 bench exam: active vs passive '
              'components and their symbols, transistor (BJT) type and pin identification with a '
              'digital multimeter, and CRO controls plus every waveform calculation '
              '(Vp-p, Vp, Vrms, period, frequency, phase and Lissajous). 30 questions — each with '
              'a diagram where it helps, a worked solution and distractor analysis.'),
    'accent': '#010080',
    'available': True,
}

TOPICS = [
    {'id': T['active'], 'name': 'Active & Passive Components',
     'summaryNotes': """### Core rule
- **Active** — needs an external supply; can control current or give power gain
  (diode, zener, LED, BJT, MOSFET, op-amp, SCR).
- **Passive** — cannot add energy; stores or dissipates it (R, L, C, potentiometer, LDR,
  thermistor, transformer).

### Components you must be able to draw and use
- **Diode** — triangle (anode) into a bar (cathode); the **band** on the body marks the cathode.
- **Zener** — diode with a **Z-shaped** cathode; works in **reverse breakdown** at $V_Z$; always
  used with a series resistor.
- **Potentiometer** — full track between pins **1 and 3**; wiper on **pin 2**;
  $V_{out}=V_{in}\\frac{R_{2\\to3}}{R_{1\\to3}}$.
- **NTC thermistor** — temperature up, resistance **down** (PTC is the opposite).
- **LDR** — resistance **highest in darkness**, lowest in bright light.
- **Electrolytic capacitor** — **polarised**; long lead positive, striped side negative.

### Exam traps
- Non-linear does **not** mean active (a thermistor is non-linear and passive).
- Amplification always needs a supply — a passive network can only attenuate.
- Fitting an electrolytic the wrong way round is the classic bench fault."""},
    {'id': T['bjt'], 'name': 'BJT Pin & Type Diagnostics',
     'summaryNotes': """### The model
A BJT is **two diodes sharing the base**:
- **NPN** — the two **anodes** meet at the base.
- **PNP** — the two **cathodes** meet at the base.

### Identification routine (diode mode)
1. Find the pin that shows a drop of **≈0.6–0.7 V to both** other pins. That is the **base**.
2. **Red probe on the base → NPN.** **Black probe on the base → PNP.**
3. Split emitter from collector with the doping rule: $V_{BE} > V_{BC}$ by 5–15 mV.
   **The larger reading is the emitter.**

### Health checks
- **C–E reads `OL` both ways** → healthy (two opposing junctions).
- **C–E reads 0.000 V** → **shorted**, faulty.
- **No drop on any combination** → **open**, faulty.
- No single pin that conducts to both others → **not a BJT**.

### Exam traps
- The emitter/collector difference is only a few millivolts — write both readings down.
- Test the transistor **out of circuit**.
- Ohms mode usually cannot forward-bias a silicon junction; use **diode mode**."""},
    {'id': T['cro'], 'name': 'CRO Controls & Functions',
     'summaryNotes': """### The controls
| Control | Axis | What it does |
|---|---|---|
| **Time/Div** (time base) | horizontal | seconds per horizontal division |
| **Volts/Div** | vertical | volts per vertical division |
| **Trigger / Level** | horizontal | stabilises a stationary trace |
| **Vertical Position** | vertical | moves the trace up/down (no amplitude change) |
| **Horizontal Position** | horizontal | slides the trace left/right |
| **Focus / Intensity** | — | sharpness / brightness |
| **Coupling (DC / AC / GND)** | — | pass everything / block DC / show the 0 V line |

### The graticule
One **major division = 1 cm × 1 cm**; typical screen is **8 vertical × 10 horizontal** divisions,
each subdivided into 5 minor ticks.

### Set-up that earns marks
1. Coupling to **GND** → a flat line at true zero.
2. **Vertical Position** → park that line on the centre graticule line.
3. Back to **DC** → now measure amplitudes and DC offsets from a known reference.

### Exam traps
- **AC coupling hides the DC offset** — switch to DC before measuring one.
- The CRO never alters the signal; it only displays it."""},
    {'id': T['calc'], 'name': 'CRO Waveform Calculations',
     'summaryNotes': """### The five formulas
$$V_{p\\text{-}p} = (\\text{vert. div}) \\times (\\text{Volts/Div})$$
$$V_p = \\frac{V_{p\\text{-}p}}{2},\\qquad V_{rms} = 0.707\\,V_p,\\;\\; V_p = 1.414\\,V_{rms}$$
$$T = (\\text{horiz. div per cycle}) \\times (\\text{Time/Div}),\\qquad f = \\frac{1}{T}$$
$$\\phi = \\frac{\\text{shift div}}{\\text{div per cycle}} \\times 360^\\circ$$
$$\\frac{f_y}{f_x} = \\frac{\\text{horizontal tangencies}}{\\text{vertical tangencies}}$$

### DC-offset signals
$$V_{DC} = \\frac{(\\text{top div}) + (\\text{bottom div})}{2} \\times (\\text{Volts/Div})$$
The offset is the **midpoint** of the waveform, not its peak.

### Exam traps
- **milli** = $10^{-3}$: convert to seconds **before** computing frequency.
- RMS is **0.707 × peak**, never 0.707 × peak-to-peak.
- Phase needs no Time/Div — the units cancel because both measurements are in divisions.
- Lissajous figures only read cleanly when the frequencies are in a **simple integer ratio**."""},
]


# ---------------------------------------------------------------------------
# Abbreviations
# ---------------------------------------------------------------------------
# Two different jobs, deliberately kept apart:
#
# 1. The cathode ray oscilloscope is ALWAYS written out in full -
#    "cathode ray oscilloscope (CRO)" - at every single place it appears, so
#    nobody ever has to guess what "CRO" stands for.  (INLINE)
#
# 2. Every other technical abbreviation keeps its short form in the prose,
#    because that is how it is written in the lab manual and printed on the
#    instrument panel.  Instead of cluttering the sentences, each question
#    carries a "Key terms" drawer listing the full meaning of only the
#    abbreviations that question actually uses.  (TERMS)
#
# Math spans ($...$, $$...$$) and code spans (`...`) are never touched.

INLINE = [
    dict(re=r'\bCRO\b', lower='cathode ray oscilloscope (CRO)',
         title='Cathode Ray Oscilloscope (CRO)'),
]

# (pattern, short form, full meaning) — grouped roughly by theme.
TERMS = [
    (r'\bBJTs?\b', 'BJT', 'bipolar junction transistor'),
    (r'\bDMMs?\b', 'DMM', 'digital multimeter'),
    (r'\bMOSFETs?\b', 'MOSFET', 'metal-oxide-semiconductor field-effect transistor'),
    (r'\bJFETs?\b', 'JFET', 'junction field-effect transistor'),
    (r'\bFETs?\b', 'FET', 'field-effect transistor'),
    (r'\bSCRs?\b', 'SCR', 'silicon-controlled rectifier'),
    (r'\bLEDs?\b', 'LED', 'light-emitting diode'),
    (r'\bLCDs?\b', 'LCD', 'liquid crystal display'),
    (r'\bLDRs?\b', 'LDR', 'light-dependent resistor'),
    (r'\bNTC\b', 'NTC', 'negative temperature coefficient'),
    (r'\bPTC\b', 'PTC', 'positive temperature coefficient'),
    (r'\bICs?\b', 'IC', 'integrated circuit'),
    (r'\bop-amps?\b', 'op-amp', 'operational amplifier'),
    (r'\bBNC\b', 'BNC', 'Bayonet Neill-Concelman connector (the twist-lock socket)'),
    (r'\bCOM\b', 'COM', 'common terminal — where the meter\'s black lead plugs in'),
    (r'\bOL\b', 'OL', 'over-limit — what the meter shows when nothing conducts'),
    (r'\bRMS\b', 'RMS', 'root mean square'),
    (r'\bGND\b', 'GND', 'ground — the 0 V reference line'),
    (r'\bAC\b', 'AC', 'alternating current'),
    (r'\bDC\b', 'DC', 'direct current'),
    (r'\bNPN\b', 'NPN', 'negative-positive-negative'),
    (r'\bPNP\b', 'PNP', 'positive-negative-positive'),
    (r'\bV\(BE\)\b', 'V(BE)', 'base-emitter voltage'),
    (r'\bV\(BC\)\b', 'V(BC)', 'base-collector voltage'),
    (r'\bV\(CE\)\b', 'V(CE)', 'collector-emitter voltage'),
    (r'\bC[-–—]E\b', 'C-E', 'collector-emitter'),
    (r'\bV-I\b', 'V-I', 'voltage-current'),
    (r'\bVp-p\b', 'Vp-p', 'peak-to-peak voltage'),
    (r'\bVrms\b', 'Vrms', 'root-mean-square voltage'),
    (r'\bVp\b(?!-)', 'Vp', 'peak voltage'),
    (r'\bVolts/Div\b', 'Volts/Div', 'volts per division — the vertical scale'),
    (r'\bTime/Div\b', 'Time/Div', 'time per division — the horizontal scale'),
    (r'\bV/div\b', 'V/div', 'volts per division'),
    (r'\bms/div\b', 'ms/div', 'milliseconds per division'),
    (r'\bs/div\b', 's/div', 'seconds per division'),
    (r'\bCH1\b', 'CH1', 'channel 1 input'),
    (r'\bCH2\b', 'CH2', 'channel 2 input'),
]

_MATH_OR_CODE = re.compile(r'\$\$[\s\S]*?\$\$|\$[^$\n]*\$|`[^`]*`')
_ARTICLE = re.compile(r'\b([Aa])n\s+(?=[bcdfgjklmnpqrstvwz])')
_TERMS = [(re.compile(p, re.I), abbr, full) for p, abbr, full in TERMS]


def expand(text):
    """Write "cathode ray oscilloscope (CRO)" out in full, everywhere."""
    if not isinstance(text, str) or not text:
        return text
    spans = []

    def stash(m):
        spans.append(m.group(0))
        return '\x00%d\x00' % (len(spans) - 1)

    protected = _MATH_OR_CODE.sub(stash, text)
    result, cursor = [], 0
    for m in re.finditer('\x00(\\d+)\x00', protected):
        result.append(_expand_segment(protected[cursor:m.start()]))
        result.append(spans[int(m.group(1))])
        cursor = m.end()
    result.append(_expand_segment(protected[cursor:]))
    return _ARTICLE.sub(lambda m: m.group(1) + ' ', ''.join(result))


def _expand_segment(seg):
    for entry in INLINE:
        pattern = re.compile(entry['re'], re.I)
        base = entry['lower'].split('(')[0].strip()
        guard = base.lower() if len(base.split()) >= 2 else None
        out, last = [], 0
        for m in pattern.finditer(seg):
            window = seg[max(0, m.start() - 60):m.start()].lower()
            if guard and guard in window:      # already spelled out by hand
                continue
            raw = seg[:m.start()]
            # capitalise only when the abbreviation opens the string, its line
            # (bullet) or a sentence - never mid-sentence after a colon or dash
            form = entry['title'] if (raw == '' or raw.rstrip() == ''
                                      or raw.rstrip().endswith(('.', '!', '?'))
                                      or raw.endswith(('\n', '- ', '* '))) \
                else entry['lower']
            out.append(seg[last:m.start()])
            out.append(form)
            last = m.end()
        if out:
            out.append(seg[last:])
            seg = ''.join(out)
    return seg


def collect_terms(*blocks):
    """Abbreviations a question actually uses, for its "Key terms" drawer.

    A term that the text already spells out in words is left out — the drawer
    exists to explain, not to repeat.
    """
    text = '\n'.join(b for b in blocks if isinstance(b, str))
    if not text.strip():
        return []
    text = _MATH_OR_CODE.sub(' ', text)
    lower = text.lower()
    found, seen = [], set()
    for pattern, abbr, full in _TERMS:
        if abbr in seen:
            continue
        if pattern.search(text) and full.split(' —')[0].strip().lower() not in lower:
            seen.add(abbr)
            found.append({'abbr': abbr, 'full': full})
    return found


def expand_fields(obj, fields):
    """Expand a set of human-readable string / list-of-string fields in place."""
    for f in fields:
        v = obj.get(f)
        if isinstance(v, str):
            obj[f] = expand(v)
        elif isinstance(v, list):
            obj[f] = [expand(x) if isinstance(x, str) else x for x in v]
    return obj



def main():
    out = []
    out.append('// ===========================================================================\n'
               '// QUESTION BANK  —  CBT Lab 2 · Obafemi Awolowo University · EEE 282\n'
               '// ---------------------------------------------------------------------------\n'
               '// Generated by build_eee282_data.py. One course: EEE 282.\n'
               '// Question fields:\n'
               '//   type    : "mcq" | "calc" | "text"  (calc/text also render a typed answer box)\n'
               '//   num     : { values: [...], unit }  numeric grader (all values must be matched)\n'
               '//   match   : { all: [], any: [], minAny: {n, list} }  keyword grader for "text"\n'
               '//   expected: the model typed answer shown in Study mode and Results\n'
               '// ===========================================================================\n')

    # spell out every abbreviation in the human-readable copy
    for k in ('title', 'blurb'):
        COURSE[k] = expand(COURSE[k])
    for t in TOPICS:
        t['name'] = expand(t['name'])
        t['summaryNotes'] = expand(t.get('summaryNotes', ''))

    out.append('export const courses = [\n' + json.dumps(COURSE, indent=2) + ',\n]\n')
    out.append('export const categoryMeta = {}\n')
    out.append('export const topicMeta = ' + json.dumps({'eee282': TOPICS}, indent=2) + '\n')

    bank = []
    for item in Q:
        # migrate external image files -> inline, responsive raw SVG strings
        if item.get('image'):
            key = item['image'].rsplit('/', 1)[-1].replace('.svg', '')
            item['diagram'] = inline_diagram(key, item['id'])
            item['diagramCaption'] = expand(CAPTIONS.get(key, ''))
            del item['image']
        expand_fields(item, ('question', 'short', 'solution', 'expected', 'options'))
        terms = collect_terms(item.get('question', ''), item.get('diagramCaption', ''),
                              *(item.get('options') or []))
        if terms:
            item['terms'] = terms
        bank.append(item)
    out.append('export const questionBank = ' + json.dumps({'eee282': bank}, indent=2) + '\n')

    comps = component_symbols()
    out.append('export const componentSymbols = ' + json.dumps(comps, indent=2) + '\n')
    print('component symbols:', len(comps),
          '| active:', sum(1 for c in comps if c['category'] == 'Active'),
          '| passive:', sum(1 for c in comps if c['category'] == 'Passive'))

    p = ROOT / 'src' / 'data.js'
    p.write_text('\n'.join(out))
    print('wrote', p, p.stat().st_size, 'bytes |', len(Q), 'questions')
    from collections import Counter
    print('topics :', Counter(q_['topicId'] for q_ in Q))
    print('types  :', Counter(q_['type'] for q_ in Q))
    print('diagrams:', sum(1 for q_ in Q if q_.get('diagram')))


if __name__ == '__main__':
    main()
