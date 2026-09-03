# -*- coding: utf-8 -*-
r"""EEE 202 question bank — PART B (topics 6–9).r"""

QUESTIONS_B = []

def calc(topic, q, opts, ans, short, sol):
    QUESTIONS_B.append(dict(topicId=topic, kind="calc", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

def theory(topic, q, opts, ans, short, sol):
    QUESTIONS_B.append(dict(topicId=topic, kind="theory", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

# =====================================================================
# TOPIC 6 — MAGNETIC CIRCUITS & TRANSFORMERS
# =====================================================================
T = "eee-magcircuits-transformer"

theory(T, "The magnetomotive force (m.m.f.) of a coil of N turns carrying current I is:",
       ["F = NI, in amperes or ampere-turns", "F = N/I", "F = I/N", "F = NI²"], 0,
       "m.m.f. F = NI (ampere-turns) — the magnetic analogue of e.m.f.",
       r"""### Step 1: Core Principle
Magnetomotive force is the magnetic analogue of electromotive force — it is what drives flux around a magnetic circuit. For a coil of N turns carrying current I:
$$F = NI \quad \text{(amperes or ampere-turns)}$$

### Step 2: Testing the Options
- **Option A (correct)**: F = NI.
- **Option B (wrong)**: N/I is dimensionally wrong — more turns must give more m.m.f.
- **Option C (wrong)**: I/N likewise falls as turns increase.
- **Option D (wrong)**: the current appears squared, which is not the definition.

### Step 3: Exam Trap Summary
The trap is rearranging the turns/current relation. Anchor: m.m.f. grows with BOTH turns and current — it is their product.
r""")

theory(T, "The magnetic field strength (magnetising force) in a magnetic circuit is:",
       ["H = F/L = NI/L, in amperes per metre",
        "H = F × L",
        "H = F/L²",
        "H = NI × L"], 0,
       "H is the m.m.f. gradient: H = NI/L (A/m).",
       r"""### Step 1: Core Principle
Magnetic field strength H is the m.m.f. gradient — the m.m.f. per unit length of the magnetic path:
$$H = \frac{F}{l} = \frac{NI}{l} \quad \text{(amperes per metre)}$$

### Step 2: Testing the Options
- **Option A (correct)**: m.m.f. divided by path length.
- **Option B (wrong)**: multiplying by length would grow H with distance — backwards.
- **Option C (wrong)**: dividing by length² is not the definition.
- **Option D (wrong)**: NI × l confuses the field with the m.m.f. itself.

### Step 3: Exam Trap Summary
The trap is H vs F confusion: F = NI (ampere-turns, total drive) while H = NI/l (A/m, drive per metre). The unit A/m is the giveaway for H.
r""")

theory(T, "Flux density B and magnetic field strength H are related by:",
       ["B = μH, where μ is the permeability of the material",
        "B = H/μ",
        "B = μH²",
        "B = H + μ"], 0,
       "B = μH (teslas) — permeability links field strength to flux density.",
       r"""### Step 1: Core Principle
The flux density and field strength at any point of a field are related by the permeability of the material:
$$B = \mu H \quad \text{(teslas)}$$

### Step 2: Testing the Options
- **Option A (correct)**: B = μH.
- **Option B (wrong)**: dividing by μ would make denser materials produce LESS flux density.
- **Option C (wrong)**: H does not appear squared.
- **Option D (wrong)**: adding μ to H is dimensionally impossible.

### Step 3: Exam Trap Summary
The trap is inverting the relation. Anchor: higher permeability (better magnetic material) gives MORE flux density for the same H — so μ multiplies H.
r""")

theory(T, "The permeability of free space μ₀ equals:",
       ["4π × 10⁻⁷ H/m", "8.85 × 10⁻¹² F/m", "4π × 10⁻⁹ H/m", "1.26 H/m"], 0,
       "μ₀ = 4π × 10⁻⁷ henrys per metre.",
       r"""### Step 1: Core Principle
The permeability of free space is the reference permeability of a vacuum:
$$\mu_0 = 4\pi \times 10^{-7}\ H/m$$

### Step 2: Testing the Options
- **Option A (correct)**: the standard value.
- **Option B (wrong)**: $8.85\times10^{-12}\ F/m$ is the PERMITTIVITY of free space (ε₀) — the electrostatic twin.
- **Option C (wrong)**: the exponent is wrong (10⁻⁹).
- **Option D (wrong)**: 1.26 is the numerical value 4π but without the power of ten.

### Step 3: Exam Trap Summary
The trap is the μ₀/ε₀ pairing — both are 4π or 8.85 constants of "free space". Anchor: permeability μ₀ = 4π × 10⁻⁷ H/m; permittivity ε₀ = 8.85 × 10⁻¹² F/m.
r""")

theory(T, "Magnetic flux Φ, flux density B and area A are related by:",
       ["Φ = BA, with B = Φ/A",
        "Φ = B/A",
        "Φ = A/B",
        "Φ = B + A"], 0,
       "Φ = BA (webers); flux density B = Φ/A (teslas).",
       r"""### Step 1: Core Principle
Magnetic flux is the flux density multiplied by the area it threads:
$$\Phi = BA \quad \text{(webers)}$$
and therefore flux density is flux per unit area:
$$B = \frac{\Phi}{A} \quad \text{(teslas)}$$

### Step 2: Testing the Options
- **Option A (correct)**: Φ = BA.
- **Option B (wrong)**: dividing B by A shrinks the flux as area grows — backwards.
- **Option C (wrong)**: A/B is dimensionally wrong.
- **Option D (wrong)**: adding B and A is impossible dimensionally.

### Step 3: Exam Trap Summary
The trap is flux vs flux density. Anchor: flux (Wb) is the TOTAL; flux density (T) is the flux PER SQUARE METRE — density = total/area.
r""")

theory(T, "The reluctance S of a magnetic circuit is:",
       ["S = l/(μA) — the magnetic analogue of resistance",
        "S = μA/l",
        "S = l μ A",
        "S = A/(μl)"], 0,
       "Reluctance S = l/(μA) — the magnetic analogue of electrical resistance.",
       r"""### Step 1: Core Principle
Reluctance opposes flux exactly as resistance opposes current:
$$S = \frac{l}{\mu A}$$
where l is the length of the magnetic path, A its cross-sectional area, and μ the permeability. It is measured in A/Wb (ampere-turns per weber).

### Step 2: Testing the Options
- **Option A (correct)**: length over (permeability × area) — the analogue of $R = l/(\sigma A)$.
- **Option B (wrong)**: that is the conductance-like form (the reciprocal).
- **Option C (wrong)**: multiplying l, μ and A has the wrong dimensions.
- **Option D (wrong)**: area over (μl) is inverted.

### Step 3: Exam Trap Summary
The trap is inverting the reluctance formula. Anchor the electrical analogy: resistance = length/(conductivity × area), so reluctance = length/(permeability × area).
r""")

theory(T, "The relative permeability μᵣ of a material is:",
       ["the ratio of its permeability to that of free space",
        "the permeability of free space itself",
        "the ratio of its resistance to its reluctance",
        "the product μ₀ × A"], 0,
       "μᵣ = μ/μ₀ — the dimensionless ratio to free space.",
       r"""### Step 1: Core Principle
Relative permeability is the ratio of the material's permeability to the permeability of free space:
$$\mu_r = \frac{\mu}{\mu_0}$$
It is dimensionless, and the absolute permeability is $\mu = \mu_0\mu_r$.

### Step 2: Testing the Options
- **Option A (correct)**: μ/μ₀.
- **Option B (wrong)**: μ₀ is the free-space value, not a ratio.
- **Option C (wrong)**: resistance/reluctance is a meaningless ratio.
- **Option D (wrong)**: μ₀ × A is not a permeability.

### Step 3: Exam Trap Summary
The trap is quoting μ₀ when the material matters. Always multiply by μᵣ for real materials — for iron μᵣ can be hundreds or thousands.
r""")

theory(T, "Which pairing in the electrostatics ↔ electromagnetism analogy is CORRECT?",
       ["Electric field strength E ↔ Magnetic field strength H",
        "Electric flux density D ↔ Magnetomotive force F",
        "Permittivity ε ↔ Reluctance S",
        "Electric flux ↔ Magnetic flux density"], 0,
       "E ↔ H (field strengths); D ↔ B (flux densities); e.m.f. ↔ m.m.f.; ε ↔ μ.",
       r"""### Step 1: Core Principle
The analogy table pairs:
- electric flux ↔ magnetic flux (Φ)
- electric flux density D ↔ magnetic flux density B
- electric field strength E ↔ magnetic field strength H
- electromotive force ↔ magnetomotive force F
- electric p.d. ↔ magnetic p.d.
- permittivity ε ↔ permeability μ
- ε₀ ↔ μ₀; εᵣ ↔ μᵣ

### Step 2: Testing the Options
- **Option A (correct)**: both are FIELD STRENGTHS.
- **Option B (wrong)**: D is a flux DENSITY, so it pairs with B, not with the driving force F.
- **Option C (wrong)**: ε pairs with μ (both material properties); reluctance has no electrostatic twin in this table.
- **Option D (wrong)**: electric flux pairs with magnetic FLUX, not with flux density.

### Step 3: Exam Trap Summary
The trap is cross-pairing "flux" with "density" and "strength" terms. Build the table column by column: flux/flux-density/field-strength/driving-force/material-constant.
r

**Key recall:** the twin relations are $B = \mu H$ and $D = \varepsilon E$.""")

theory(T, "In an IDEAL transformer, the voltage and turns ratios are related by:",
       ["V₁/V₂ = N₁/N₂ = I₂/I₁",
        "V₁/V₂ = N₂/N₁",
        "V₁/V₂ = I₁/I₂",
        "V₁ V₂ = N₁ N₂"], 0,
       "Ideal transformer: V₁/V₂ = N₁/N₂ = I₂/I₁ (current steps inversely).",
       r"""### Step 1: Core Principle
For an ideal transformer, the voltage ratio equals the turns ratio, and the current ratio is the inverse (so power is conserved, $V_1 I_1 = V_2 I_2$):
$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}$$

### Step 2: Testing the Options
- **Option A (correct)**: both ratios in the standard order.
- **Option B (wrong)**: the turns ratio is inverted — this would predict voltage stepping UP with FEWER secondary turns.
- **Option C (wrong)**: I₁/I₂ is the inverse of the voltage ratio, so equating them is wrong.
- **Option D (wrong)**: products instead of ratios.

### Step 3: Exam Trap Summary
Two traps: inverting the turns ratio and inverting the current ratio. Anchor: more secondary turns → more secondary voltage → LESS secondary current (power conserved).
r""")

theory(T, "A transformer that increases voltage (more secondary turns than primary) is called:",
       ["a step-up transformer", "a step-down transformer", "an isolation transformer", "an autotransformer"], 0,
       "Step-up: N₂ > N₁ so V₂ > V₁.",
       r"""### Step 1: Core Principle
A step-up transformer has more turns on the secondary than the primary ($N_2 > N_1$), so the secondary voltage is higher: $V_2 = V_1\frac{N_2}{N_1}$. A step-down transformer has $N_2 < N_1$.

### Step 2: Testing the Options
- **Option A (correct)**: more secondary turns → higher voltage.
- **Option B (wrong)**: step-down LOWERS the voltage.
- **Option C (wrong)**: an isolation transformer has equal turns (1:1) — same voltage, galvanic separation.
- **Option D (wrong)**: an autotransformer shares one winding; it can step up or down depending on tapping.

### Step 3: Exam Trap Summary
The trap is naming the direction backwards. Anchor the word: "step-UP" = voltage goes UP = MORE secondary turns.
r""")

theory(T, "Why does a transformer operate only on AC (and not on steady DC)?",
       ["Transformer action relies on a changing flux to induce the secondary e.m.f. per Faraday's law",
        "DC would melt the iron core",
        "DC cannot flow through copper wire",
        "the primary resistance blocks DC"], 0,
       "Induction needs a changing flux (E = N dΦ/dt); steady DC gives constant flux → zero secondary e.m.f.",
       r"""### Step 1: Core Principle
The secondary voltage is induced by electromagnetic induction, which requires a CHANGING flux: $E = N\frac{d\Phi}{dt}$. A steady DC primary current produces a constant flux, so $d\Phi/dt = 0$ and no e.m.f. is induced in the secondary. AC, by definition changing, drives the transformer.

### Step 2: Testing the Options
- **Option A (correct)**: the changing-flux requirement.
- **Option B (wrong)**: DC would not melt the core — that is a heating argument unrelated to induction.
- **Option C (wrong)**: copper conducts DC perfectly well.
- **Option D (wrong)**: the primary resistance limits current but is not the reason induction fails.

### Step 3: Exam Trap Summary
The trap is answering with general "damage" arguments. The correct answer is always the physics: NO flux change → NO induction.
r""")

theory(T, "The main losses in a practical transformer are:",
       ["copper (I²R) losses and iron losses (eddy current + hysteresis)",
        "friction and windage losses only",
        "capacitive losses only",
        "radiation losses only"], 0,
       "Copper (I²R) losses plus iron losses — eddy current and hysteresis.",
       r"""### Step 1: Core Principle
A practical transformer dissipates power in two places: the WINDINGS (copper losses, $I^2R$, from winding resistance) and the CORE (iron losses — eddy-current heating in the laminations and hysteresis from the cyclic magnetisation).

### Step 2: Testing the Options
- **Option A (correct)**: copper + iron (eddy + hysteresis).
- **Option B (wrong)**: friction and windage are MACHINE losses (motors/generators), not transformer losses — a transformer has no moving parts.
- **Option C (wrong)**: capacitive losses are negligible in power transformers.
- **Option D (wrong)**: radiation is negligible at line frequencies.

### Step 3: Exam Trap Summary
The trap is importing rotating-machine losses (friction/windage) into a static device. Transformers only lose via I²R and core effects.
r""")

theory(T, "Magnetic flux lines:",
       ["form closed loops, never cross, and when parallel repel one another",
        "cross each other at right angles",
        "start and end in free space",
        "are straight lines only"], 0,
       "Flux lines: closed loops, no crossing, parallel lines repel.",
       r"""### Step 1: Core Principle
From the summary of important formulae (Hughes): a magnetic field can be described using lines of flux. Such lines form closed loops, do not cross, and when parallel they repel one another. Magnetic fields have north and south poles; like poles repel, unlike poles attract.

### Step 2: Testing the Options
- **Option A (correct)**: the three flux-line properties.
- **Option B (wrong)**: crossing would imply two field directions at one point — impossible.
- **Option C (wrong)**: flux lines always close on themselves (no isolated poles).
- **Option D (wrong)**: field lines curve (e.g. concentric circles around a wire).

### Step 3: Exam Trap Summary
The trap is importing electric-field-line behaviour (starting/ending on charges). Magnetic lines are always closed loops.
r

**Key recall:** flux lines represent the flux $\Phi = BA$; density is $B = \Phi/A$.""")

calc(T, "A coil of 500 turns carries 2 A. Its magnetomotive force is:",
     ["1000 ampere-turns", "250 ampere-turns", "500 ampere-turns", "1000 volts"], 0,
     "F = NI = 500 × 2 = 1000 ampere-turns.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 500$ turns, $I = 2\ A$.
Governing law:
$$F = NI$$

### Step 2: Full Mathematical Workings
$$F = 500 \times 2$$
$$F = 1000\ \text{ampere-turns}$$

### Step 3: Verification & Physical Interpretation
One thousand ampere-turns of magnetic drive — the total "pressure" pushing flux around the circuit. The unit is the ampere-turn (At), the magnetic analogue of the volt.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (250 At)**: the student divides by 2 instead of multiplying.
- **Option C trap (500 At)**: the student quotes the turns alone, forgetting the current.
- **Option D trap (1000 volts)**: the student attaches the WRONG unit — volts measure e.m.f., ampere-turns measure m.m.f.
r""")

calc(T, "A 1000-turn coil is wound on a magnetic path 0.5 m long and carries 2 A. The magnetic field strength H is:",
     ["4000 A/m", "2000 A/m", "1000 A/m", "500 A/m"], 0,
     "H = NI/l = (1000 × 2)/0.5 = 4000 A/m.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 1000$, $I = 2\ A$, path length $l = 0.5\ m$.
Governing law:
$$H = \frac{NI}{l}$$

### Step 2: Full Mathematical Workings
$$H = \frac{1000 \times 2}{0.5}$$
$$1000 \times 2 = 2000$$
$$H = \frac{2000}{0.5}$$
$$H = 4000\ A/m$$

### Step 3: Verification & Physical Interpretation
Dividing by a half-metre path doubles the m.m.f. per metre — 2000 ampere-turns spread over 0.5 m gives 4000 A/m of field strength.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (2000 A/m)**: the student stops at NI and forgets to divide by l.
- **Option C trap (1000 A/m)**: the student divides NI by 2 twice.
- **Option D trap (500 A/m)**: the student divides the turns by 2 and drops the current.
r""")

calc(T, "A flux density of 0.5 T passes through an area of 0.02 m². The flux is:",
     ["0.01 Wb", "0.1 Wb", "10 Wb", "0.001 Wb"], 0,
     "Φ = BA = 0.5 × 0.02 = 0.01 Wb.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $B = 0.5\ T$, $A = 0.02\ m^2$.
Governing law:
$$\Phi = BA$$

### Step 2: Full Mathematical Workings
$$\Phi = 0.5 \times 0.02$$
$$\Phi = 0.01\ Wb$$

### Step 3: Verification & Physical Interpretation
Half a tesla threading two hundredths of a square metre carries one hundredth of a weber. Flux is the "amount of magnetic field" passing through the area.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.1 Wb)**: the student misplaces the decimal (area read as 0.2 m²).
- **Option C trap (10 Wb)**: the student multiplies by 20 instead of 0.02.
- **Option D trap (0.001 Wb)**: the student treats the field as 0.05 T.
r""")

calc(T, "A flux density of 1.2 T passes through an area of 0.05 m². The flux is:",
     ["0.06 Wb", "0.6 Wb", "6 Wb", "0.006 Wb"], 0,
     "Φ = BA = 1.2 × 0.05 = 0.06 Wb.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $B = 1.2\ T$, $A = 0.05\ m^2$.
Governing law:
$$\Phi = BA$$

### Step 2: Full Mathematical Workings
$$\Phi = 1.2 \times 0.05$$
$$\Phi = 0.06\ Wb$$

### Step 3: Verification & Physical Interpretation
A strong 1.2 T field through 0.05 m² yields 0.06 Wb. Note the pattern: area × density, always the total flux.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.6 Wb)**: decimal slip (area read as 0.5 m²).
- **Option C trap (6 Wb)**: the student multiplies by 5 instead of 0.05.
- **Option D trap (0.006 Wb)**: decimal slip the other way.
r""")

calc(T, "A magnetic circuit has l = 0.5 m, A = 0.001 m² and relative permeability μᵣ = 1000. Its reluctance is about: (μ₀ = 4π × 10⁻⁷ H/m)",
     ["3.98 × 10⁵ A/Wb", "3.98 × 10⁶ A/Wb", "1.26 × 10⁵ A/Wb", "7.96 × 10⁵ A/Wb"], 0,
     "μ = μ₀μᵣ = 4π × 10⁻⁴; S = l/(μA) = 0.5/(4π × 10⁻⁴ × 0.001) = 3.98 × 10⁵ A/Wb.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $l = 0.5\ m$, $A = 0.001\ m^2$, $\mu_r = 1000$, $\mu_0 = 4\pi\times10^{-7}\ H/m$.
Governing laws:
$$\mu = \mu_0\mu_r \qquad S = \frac{l}{\mu A}$$

### Step 2: Full Mathematical Workings
Step A — absolute permeability:
$$\mu = \mu_0 \times \mu_r$$
$$\mu = 4\pi \times 10^{-7} \times 1000$$
$$\mu = 4\pi \times 10^{-4}$$
$$\mu = 1.2566 \times 10^{-3}\ H/m$$
Step B — reluctance:
$$S = \frac{l}{\mu A}$$
$$S = \frac{0.5}{1.2566 \times 10^{-3} \times 0.001}$$
$$1.2566 \times 10^{-3} \times 0.001 = 1.2566 \times 10^{-6}$$
$$S = \frac{0.5}{1.2566 \times 10^{-6}}$$
$$S = 3.98 \times 10^{5}\ A/Wb$$

### Step 3: Verification & Physical Interpretation
The reluctance of about 400,000 A/Wb is typical of a small magnetic core: the high relative permeability of iron keeps the reluctance low.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (3.98 × 10⁶)**: the student uses μᵣ = 100 (one order down) or A = 0.0001 m².
- **Option C trap (1.26 × 10⁵)**: the student forgets μᵣ and uses μ₀ alone — the classic error.
- **Option D trap (7.96 × 10⁵)**: the student doubles the length or halves the area.
r""")

calc(T, "A magnetic circuit has an m.m.f. of 500 At and a reluctance of 2 × 10⁶ A/Wb. The flux produced is:",
     ["0.25 mWb", "2.5 mWb", "1 mWb", "0.025 mWb"], 0,
     "Magnetic Ohm's law: Φ = F/S = 500/(2 × 10⁶) = 2.5 × 10⁻⁴ Wb = 0.25 mWb.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: m.m.f. $F = 500\ At$, reluctance $S = 2 \times 10^{6}\ A/Wb$.
Governing law — magnetic Ohm's law (the analogue of $I = V/R$):
$$\Phi = \frac{F}{S}$$

### Step 2: Full Mathematical Workings
$$\Phi = \frac{500}{2 \times 10^{6}}$$
$$\Phi = 250 \times 10^{-6}$$
$$\Phi = 2.5 \times 10^{-4}\ Wb$$
Convert to milliwebers:
$$2.5 \times 10^{-4}\ Wb = 0.25\ mWb$$

### Step 3: Verification & Physical Interpretation
Flux = driving m.m.f. ÷ opposing reluctance — the exact magnetic twin of Ohm's law. 500 ampere-turns against two million A/Wb of reluctance pushes through only a quarter of a milliweber.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (2.5 mWb)**: the student misplaces the power of ten (reads 10⁵).
- **Option C trap (1 mWb)**: the student uses S = 5 × 10⁵ instead of 2 × 10⁶.
- **Option D trap (0.025 mWb)**: the student divides by 10 again after the correct division.
r""")

calc(T, "A transformer has N₁ = 500 primary turns and N₂ = 100 secondary turns. With a primary voltage of 220 V, the secondary voltage is:",
     ["44 V", "110 V", "1100 V", "22 V"], 0,
     "V₂ = V₁ × (N₂/N₁) = 220 × (100/500) = 220 × 0.2 = 44 V (step-down).",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N_1 = 500$, $N_2 = 100$, $V_1 = 220\ V$.
Governing law — ideal transformer voltage ratio:
$$\frac{V_2}{V_1} = \frac{N_2}{N_1}$$

### Step 2: Full Mathematical Workings
Rearrange for the secondary voltage:
$$V_2 = V_1 \times \frac{N_2}{N_1}$$
$$V_2 = 220 \times \frac{100}{500}$$
$$\frac{100}{500} = \frac{1}{5} = 0.2$$
$$V_2 = 220 \times 0.2$$
$$V_2 = 44\ V$$

### Step 3: Verification & Physical Interpretation
Fewer secondary turns than primary means a step-DOWN transformer: 220 V reduced fivefold to 44 V, exactly the turns ratio 1:5.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (110 V)**: the student halves instead of dividing by five (ratio 0.5).
- **Option C trap (1100 V)**: the student INVERTS the ratio — using N₁/N₂ = 5 and multiplying (500/100 × 220).
- **Option D trap (22 V)**: the student divides by 10 (decimal slip in the ratio).
r""")

calc(T, "A step-up transformer has N₁ = 200 turns and N₂ = 1000 turns. With V₁ = 50 V, the secondary voltage is:",
     ["250 V", "10 V", "100 V", "500 V"], 0,
     "V₂ = V₁ × (N₂/N₁) = 50 × (1000/200) = 50 × 5 = 250 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N_1 = 200$, $N_2 = 1000$, $V_1 = 50\ V$.
Governing law:
$$V_2 = V_1 \times \frac{N_2}{N_1}$$

### Step 2: Full Mathematical Workings
$$V_2 = 50 \times \frac{1000}{200}$$
$$\frac{1000}{200} = 5$$
$$V_2 = 50 \times 5$$
$$V_2 = 250\ V$$

### Step 3: Verification & Physical Interpretation
Five times more secondary turns gives five times the voltage — a 1:5 step-UP transformer lifting 50 V to 250 V.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (10 V)**: the student inverts the ratio (200/1000 = 0.2 → 10 V).
- **Option C trap (100 V)**: the student uses a ratio of 2.
- **Option D trap (500 V)**: the student uses a ratio of 10.
r""")

calc(T, "A transformer has N₁ = 400 primary turns and N₂ = 50 secondary turns. With V₁ = 240 V, the secondary voltage is:",
     ["30 V", "48 V", "120 V", "1920 V"], 0,
     "V₂ = 240 × (50/400) = 240 × 0.125 = 30 V (step-down).",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N_1 = 400$, $N_2 = 50$, $V_1 = 240\ V$.
Governing law:
$$V_2 = V_1 \times \frac{N_2}{N_1}$$

### Step 2: Full Mathematical Workings
$$V_2 = 240 \times \frac{50}{400}$$
$$\frac{50}{400} = \frac{1}{8} = 0.125$$
$$V_2 = 240 \times 0.125$$
$$V_2 = 30\ V$$

### Step 3: Verification & Physical Interpretation
An 8:1 step-down ratio drops 240 V to 30 V — the typical mains-to-low-voltage supply transformer.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (48 V)**: the student uses a ratio of 0.2 (50/250).
- **Option C trap (120 V)**: the student halves the voltage (ratio 0.5).
- **Option D trap (1920 V)**: the student inverts the ratio (400/50 = 8 → 240 × 8).
r""")

calc(T, "A 600-turn primary must step 240 V down to 12 V. The number of secondary turns required is:",
     ["30 turns", "120 turns", "12000 turns", "50 turns"], 0,
     "N₂ = N₁ × (V₂/V₁) = 600 × (12/240) = 600 × 0.05 = 30 turns.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N_1 = 600$, $V_1 = 240\ V$, $V_2 = 12\ V$.
Governing law, rearranged for the secondary turns:
$$N_2 = N_1 \times \frac{V_2}{V_1}$$

### Step 2: Full Mathematical Workings
$$N_2 = 600 \times \frac{12}{240}$$
$$\frac{12}{240} = \frac{1}{20} = 0.05$$
$$N_2 = 600 \times 0.05$$
$$N_2 = 30\ \text{turns}$$

### Step 3: Verification & Physical Interpretation
The required 20:1 voltage reduction needs 20 times fewer secondary turns: 600/20 = 30 turns. Checking forward, $V_2 = 240 \times 30/600 = 12\ V$ — exact.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (120 turns)**: the student uses a 1:5 ratio instead of 1:20.
- **Option C trap (12000 turns)**: the student INVERTS the ratio (600 × 20).
- **Option D trap (50 turns)**: the student uses a 1:12 ratio.
r""")

calc(T, "An ideal transformer supplies a load at V₂ = 24 V, I₂ = 2 A from a primary at V₁ = 240 V. The primary current is:",
     ["0.2 A", "2 A", "20 A", "0.02 A"], 0,
     "I₁ = V₂I₂/V₁ = (24 × 2)/240 = 48/240 = 0.2 A.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $V_2 = 24\ V$, $I_2 = 2\ A$, $V_1 = 240\ V$.
Governing law — power conservation in an ideal transformer:
$$V_1 I_1 = V_2 I_2$$

### Step 2: Full Mathematical Workings
Rearrange for the primary current:
$$I_1 = \frac{V_2 I_2}{V_1}$$
$$I_1 = \frac{24 \times 2}{240}$$
$$24 \times 2 = 48$$
$$I_1 = \frac{48}{240}$$
$$I_1 = 0.2\ A$$

### Step 3: Verification & Physical Interpretation
The 10:1 voltage step-down must be accompanied by a 1:10 current step-up — but here we solve from the secondary side: 48 W of load power drawn at 240 V needs only 0.2 A on the primary.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (2 A)**: the student assumes primary current equals secondary current (forgetting the transformation).
- **Option C trap (20 A)**: the student multiplies by 10 instead of dividing.
- **Option D trap (0.02 A)**: the student divides by 100 (double ratio application).
r""")

calc(T, "A transformer with turns ratio N₁/N₂ = 10 supplies a secondary current of 3 A. The primary current is about:",
     ["0.3 A", "3 A", "30 A", "0.03 A"], 0,
     "I₁ = I₂ × (N₂/N₁) = 3 × (1/10) = 0.3 A.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $\frac{N_1}{N_2} = 10$, $I_2 = 3\ A$.
Governing law — ideal transformer current ratio:
$$\frac{I_1}{I_2} = \frac{N_2}{N_1}$$

### Step 2: Full Mathematical Workings
$$I_1 = I_2 \times \frac{N_2}{N_1}$$
$$\frac{N_2}{N_1} = \frac{1}{10}$$
$$I_1 = 3 \times \frac{1}{10}$$
$$I_1 = 0.3\ A$$

### Step 3: Verification & Physical Interpretation
Ten times more primary turns means one-tenth of the secondary current flows in the primary — the inverse of the voltage ratio, preserving power.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (3 A)**: the student ignores the transformation ratio.
- **Option C trap (30 A)**: the student multiplies by the ratio instead of dividing.
- **Option D trap (0.03 A)**: the student divides by 100.
r""")

calc(T, "A conductor of length 0.3 m moves at 10 m/s at right angles to a field of 0.5 T. The e.m.f. induced in it is:",
     ["1.5 V", "15 V", "0.15 V", "3 V"], 0,
     "E = Blv = 0.5 × 0.3 × 10 = 1.5 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $l = 0.3\ m$, $v = 10\ m/s$, $B = 0.5\ T$, motion perpendicular to the field.
Governing law — motional e.m.f.:
$$E = Blv$$

### Step 2: Full Mathematical Workings
$$E = 0.5 \times 0.3 \times 10$$
$$0.5 \times 0.3 = 0.15$$
$$0.15 \times 10 = 1.5$$
$$E = 1.5\ V$$

### Step 3: Verification & Physical Interpretation
A 0.3 m conductor sweeping 0.5 T at 10 m/s cuts 1.5 V of e.m.f. — the generator principle in one line.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (15 V)**: the student misplaces a decimal (length read as 3 m).
- **Option C trap (0.15 V)**: the student forgets the speed factor of 10.
- **Option D trap (3 V)**: the student doubles the field or the speed.
r""")

calc(T, "A conductor of length 0.25 m moves at 8 m/s at right angles to a field of 0.4 T. The induced e.m.f. is:",
     ["0.8 V", "8 V", "0.08 V", "1.25 V"], 0,
     "E = Blv = 0.4 × 0.25 × 8 = 0.8 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $l = 0.25\ m$, $v = 8\ m/s$, $B = 0.4\ T$.
Governing law:
$$E = Blv$$

### Step 2: Full Mathematical Workings
$$E = 0.4 \times 0.25 \times 8$$
$$0.4 \times 0.25 = 0.1$$
$$0.1 \times 8 = 0.8$$
$$E = 0.8\ V$$

### Step 3: Verification & Physical Interpretation
The product of the three quantities gives 0.8 V — a modest e.m.f. from a modest conductor speed.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (8 V)**: the student drops the field factor (uses B = 4 T).
- **Option C trap (0.08 V)**: decimal slip (length 0.025 m).
- **Option D trap (1.25 V)**: the student uses a field of 0.5 T and length 0.25 m with speed 10 — a recompute from a neighbouring problem.
r""")

# --- multi-part theoretical question (Topic 6) ---
theory(T, "Match each electrostatic quantity to its electromagnetic analogue: (a) electric field strength E (b) electric flux density D (c) permittivity ε (d) electromotive force.",
       ["magnetic field strength H; magnetic flux density B; permeability μ; magnetomotive force F",
        "magnetic flux Φ; H; reluctance S; magnetic p.d.",
        "B; H; μ₀; volt",
        "H; Φ; μ; ampere"], 0,
       "E ↔ H, D ↔ B, ε ↔ μ, e.m.f. ↔ m.m.f.",
       r"""### Step 1: Core Principle
The complete analogy:
(a) electric field strength E ↔ magnetic field strength H
(b) electric flux density D ↔ magnetic flux density B
(c) permittivity ε ↔ permeability μ
(d) electromotive force ↔ magnetomotive force F

### Step 2: Testing the Options
- **Option A (correct)**: all four pairings exact.
- **Option B (wrong)**: pairs E with flux (not field strength) and ε with reluctance — both broken.
- **Option C (wrong)**: part (a) swaps strength with density, and part (d) gives the volt (an e.m.f. unit, not the analogue quantity).
- **Option D (wrong)**: part (b) pairs D with flux instead of flux density.

### Step 3: Exam Trap Summary
The trap is mixing the four levels (flux / density / strength / driving force). Anchor the ladder: flux ↔ flux, density ↔ density, strength ↔ strength, e.m.f. ↔ m.m.f., ε ↔ μ.
r

**Key recall:** $B = \mu H$ and $D = \varepsilon E$ are the twin constitutive relations.""")

# =====================================================================
# TOPIC 7 — ELECTRICAL MOTORS & GENERATORS
# =====================================================================
T = "eee-motors-generators"

theory(T, "The key electromechanics demonstration of 1831 was by:",
       ["Michael Faraday — a conductor moved in a magnetic field generates current, and a current in a field develops motion",
        "Thomas Edison",
        "Hans Christian Oersted",
        "Charles Steinmetz"], 0,
       "Faraday (1831) demonstrated both directions: motion→e.m.f. (generator) and current→force (motor).",
       r"""### Step 1: Core Principle
At some point in 1831 Faraday demonstrated that a conductor moved in a magnetic field could generate a current, and that a current flowing in a conductor immersed in a magnetic field could develop motion. Over the next 30 years these two effects were developed into practical machines.

### Step 2: Testing the Options
- **Option A (correct)**: Faraday, 1831, both conversion directions.
- **Option B (wrong)**: Edison built the DC power system (1880s), not the 1831 discovery.
- **Option C (wrong)**: Oersted (1820) discovered that current deflects a compass — earlier, and one-directional only.
- **Option D (wrong)**: Steinmetz formalised AC analysis (1893).

### Step 3: Exam Trap Summary
The trap is mixing the names and dates of electromagnetism milestones. Anchor: Oersted 1820 (current→field), Faraday 1831 (induction), Steinmetz 1893 (phasors).
r

**Key relation:** the motional e.m.f. Faraday exploited is $E = Blv$.""")

theory(T, "An electric motor converts:",
       ["electrical energy into mechanical energy",
        "mechanical energy into electrical energy",
        "heat energy into electricity",
        "chemical energy into light"], 0,
       "Motor: electrical → mechanical (rotation).",
       r"""### Step 1: Core Principle
A motor takes electrical energy in and delivers mechanical energy out (rotation/torque) — the current-in-a-field force effect of Faraday's demonstration.

### Step 2: Testing the Options
- **Option A (correct)**: electrical → mechanical.
- **Option B (wrong)**: mechanical → electrical is the GENERATOR direction.
- **Option C (wrong)**: heat-to-electricity is thermoelectric generation, not a motor.
- **Option D (wrong)**: chemical-to-light describes some cells/lamps, not a motor.

### Step 3: Exam Trap Summary
The trap is reversing the two conversion directions. Anchor: MOTOR = electricity IN, motion OUT; GENERATOR = motion IN, electricity OUT.
r

**Key relation:** the motor force on a conductor is $F = BIl$.""")

theory(T, "A generator converts:",
       ["mechanical energy into electrical energy",
        "electrical energy into mechanical energy",
        "AC into DC",
        "voltage into current"], 0,
       "Generator: mechanical → electrical via electromagnetic induction.",
       r"""### Step 1: Core Principle
A generator converts mechanical energy (shaft rotation) into electrical energy — the relative motion of a conductor and magnetic flux induces the e.m.f.

### Step 2: Testing the Options
- **Option A (correct)**: mechanical → electrical.
- **Option B (wrong)**: that is the MOTOR direction.
- **Option C (wrong)**: AC→DC conversion is rectification, done by a commutator or rectifier — not the generator's energy role.
- **Option D (wrong)**: voltage and current are both electrical quantities, not an energy conversion.

### Step 3: Exam Trap Summary
Same duality, opposite direction. Also avoid answering "AC to DC" — the commutator does that INSIDE a DC generator, but the generator's overall job is mechanical→electrical.
r

**Key relation:** the generated e.m.f. per conductor is $E = Blv$.""")

theory(T, "A battery and a generator differ in that:",
       ["a battery converts stored chemical energy while a generator produces e.m.f. from motion in a magnetic field",
        "both produce e.m.f. by electromagnetic induction",
        "a generator stores energy chemically",
        "a battery produces AC only"], 0,
       "Battery = chemical storage; generator = induction from conductor-flux motion.",
       r"""### Step 1: Core Principle
A battery is a source of stored chemical energy (electrodes in an electrolyte), while a generator produces e.m.f. by the relative movement of a conductor and a magnetic flux (electromagnetic induction).

### Step 2: Testing the Options
- **Option A (correct)**: chemical storage vs induction.
- **Option B (wrong)**: batteries do NOT work by induction — only generators do.
- **Option C (wrong)**: generators do not store chemical energy.
- **Option D (wrong)**: batteries produce DC; AC comes from alternators.

### Step 3: Exam Trap Summary
The trap is assuming all e.m.f. sources work the same way. The notes' three sources — cells, generators, thermo-junctions — each use a different physical mechanism.
r

**Key contrast:** battery = chemical storage; generator obeys $E = Blv$ induction.""")

theory(T, "In a DC machine, the function of the commutator is to:",
       ["convert the alternating e.m.f. induced in the armature into a unidirectional (DC) output",
        "generate the magnetic field",
        "cool the machine",
        "increase the speed of rotation"], 0,
       "The commutator rectifies the armature's AC into DC at the brushes.",
       r"""### Step 1: Core Principle
The e.m.f. induced in the rotating armature conductors alternates as they pass under successive poles. The commutator — a segmented ring with brushes — reverses the connections each half-cycle so the EXTERNAL circuit always sees the same polarity: a unidirectional (DC) output.

### Step 2: Testing the Options
- **Option A (correct)**: AC-to-DC rectification by the commutator.
- **Option B (wrong)**: the FIELD system (poles/field windings) produces the flux.
- **Option C (wrong)**: cooling is done by fans/ventilation, not the commutator.
- **Option D (wrong)**: the commutator does not control speed.

### Step 3: Exam Trap Summary
The trap is assigning field-generating or speed roles to the commutator. Anchor: commutator = mechanical rectifier; field system = flux source.
r

**Key recall:** the armature e.m.f. alternates as $E = Blv$ before rectification.""")

theory(T, "Fleming's LEFT-hand rule is used for:",
       ["motors — finding the direction of force on a current-carrying conductor in a field",
        "generators — finding the direction of the induced e.m.f.",
        "finding the polarity of a battery",
        "calculating transformer ratios"], 0,
       "Left-hand rule (FBI) = motor force; right-hand rule = generator e.m.f.",
       r"""### Step 1: Core Principle
Fleming's left-hand rule (FBI: thuMb = Force/Motion, First finger = Field, seCond finger = Current) gives the direction of the FORCE on a current-carrying conductor — the MOTOR effect. The right-hand rule gives the direction of the INDUCED e.m.f. in a conductor moving in a field — the GENERATOR effect.

### Step 2: Testing the Options
- **Option A (correct)**: left hand = motor force.
- **Option B (wrong)**: the generator e.m.f. direction uses the RIGHT-hand rule.
- **Option C (wrong)**: battery polarity is chemistry, not a hand rule.
- **Option D (wrong)**: transformer ratios are arithmetic, not hand rules.

### Step 3: Exam Trap Summary
The trap is swapping the hands. Anchor: LEFT = Motor (think "motorists drive on the left" in Nigeria); RIGHT = geneRATOR.
r

**Key relation:** the force magnitude is $F = BIl\sin\theta$.""")

theory(T, "An AC generator is also called:",
       ["an alternator", "a dynamo", "a transformer", "a rectifier"], 0,
       "AC generator = alternator.",
       r"""### Step 1: Core Principle
A generator producing alternating e.m.f. is called an alternator — the armature's rotation in the field produces the sinusoid directly, with slip rings (not a commutator) delivering the AC.

### Step 2: Testing the Options
- **Option A (correct)**: alternator = AC generator.
- **Option B (wrong)**: dynamo is an older name associated with DC generators.
- **Option C (wrong)**: a transformer changes voltage levels; it does not generate.
- **Option D (wrong)**: a rectifier converts AC to DC.

### Step 3: Exam Trap Summary
The trap is the alternator/dynamo naming. Anchor: alternator = AC; dynamo = DC (historically).
r

**Key recall:** each alternator conductor develops $E = Blv$.""")

calc(T, "A conductor of length 0.5 m moves at 20 m/s perpendicular to a field of 1 T. The induced e.m.f. is:",
     ["10 V", "0.1 V", "40 V", "2.5 V"], 0,
     "E = Blv = 1 × 0.5 × 20 = 10 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $l = 0.5\ m$, $v = 20\ m/s$, $B = 1\ T$, motion perpendicular to the field.
Governing law:
$$E = Blv$$

### Step 2: Full Mathematical Workings
$$E = 1 \times 0.5 \times 20$$
$$1 \times 0.5 = 0.5$$
$$0.5 \times 20 = 10$$
$$E = 10\ V$$

### Step 3: Verification & Physical Interpretation
A half-metre conductor sweeping a one-tesla field at 20 m/s develops 10 V — the generator equation in its cleanest form.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.1 V)**: decimal slip (speed read as 0.2 m/s).
- **Option C trap (40 V)**: the student doubles the speed or the length.
- **Option D trap (2.5 V)**: the student divides by 4 (e.g. uses 0.25 m length).
r""")

calc(T, "A conductor of length 0.4 m moves at 5 m/s perpendicular to a field of 0.2 T. The induced e.m.f. is:",
     ["0.4 V", "4 V", "0.04 V", "2 V"], 0,
     "E = Blv = 0.2 × 0.4 × 5 = 0.4 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $l = 0.4\ m$, $v = 5\ m/s$, $B = 0.2\ T$.
Governing law:
$$E = Blv$$

### Step 2: Full Mathematical Workings
$$E = 0.2 \times 0.4 \times 5$$
$$0.2 \times 0.4 = 0.08$$
$$0.08 \times 5 = 0.4$$
$$E = 0.4\ V$$

### Step 3: Verification & Physical Interpretation
Small field, modest speed — 0.4 V results. The motional e.m.f. scales linearly with each of the three factors.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (4 V)**: decimal slip (field read as 2 T).
- **Option C trap (0.04 V)**: decimal slip (speed read as 0.5 m/s).
- **Option D trap (2 V)**: the student multiplies by 5 twice.
r""")

# --- multi-part theoretical question (Topic 7) ---
theory(T, "Which rule applies to which machine? (a) direction of force in a motor (b) direction of induced e.m.f. in a generator.",
       ["left-hand rule; right-hand rule",
        "right-hand rule; left-hand rule",
        "left-hand rule; left-hand rule",
        "right-hand rule; right-hand rule"], 0,
       "LEFT hand = motor force; RIGHT hand = generator e.m.f.",
       r"""### Step 1: Core Principle
(a) Motor force on a current-carrying conductor → Fleming's LEFT-hand rule (thuMb = Motion, First finger = Field, seCond finger = Current).
(b) Induced e.m.f. in a conductor moving in a field → Fleming's RIGHT-hand rule.

### Step 2: Testing the Options
- **Option A (correct)**: motor = left, generator = right.
- **Option B (wrong)**: both hands swapped — the classic inversion.
- **Option C (wrong)**: the generator needs the right hand.
- **Option D (wrong)**: the motor needs the left hand.

### Step 3: Exam Trap Summary
The swap is the single most common error in this topic. Anchor: "LEFT = Motor" (in Nigeria, motorists drive on the left) and the generator takes the other hand.
r

**Key relation:** motor force $F = BIl\sin\theta$; generator e.m.f. $E = Blv$.""")

# =====================================================================
# TOPIC 8 — INSTRUMENTS & INSTRUMENTATION
# =====================================================================
T = "eee-instruments"

theory(T, "Instrumentation is best defined as:",
       ["the use of devices (instruments) to detect, observe, measure, control, compute, communicate and display physical quantities",
        "the repair of electrical machines",
        "the generation of electrical power",
        "the design of transformers"], 0,
       "Instrumentation: detecting, observing, measuring, controlling, computing, communicating, displaying physical quantities.",
       r"""### Step 1: Core Principle
Per the reference material, instrumentation refers to the use of devices (instruments) to detect, observe, measure, control, compute, communicate and display physical quantities. All branches of experimental engineering depend on instrumentation systems.

### Step 2: Testing the Options
- **Option A (correct)**: the complete seven-verb definition.
- **Option B (wrong)**: repair is maintenance, not instrumentation.
- **Option C (wrong)**: generation is power engineering.
- **Option D (wrong)**: transformer design is a component activity.

### Step 3: Exam Trap Summary
The trap is narrowing instrumentation to "measuring only". The definition is deliberately broad — measurement is just one of seven functions.
r

**Key recall:** the displayed electrical quantities obey Ohm's law $V = IR$.""")

theory(T, "Instruments are said to extend human senses because they:",
       ["measure accurately and rapidly over a great range of distances and physical quantities",
        "replace human judgement entirely",
        "only amplify sounds",
        "are never used in engineering"], 0,
       "Instruments let humans measure accurately and quickly over a great range of quantities.",
       r"""### Step 1: Core Principle
The notes state that instruments let humans measure accurately and rapidly over a great range of distances and physical quantities — beyond what the senses can do directly (e.g. currents, voltages, tiny displacements).

### Step 2: Testing the Options
- **Option A (correct)**: accuracy, speed and range.
- **Option B (wrong)**: instruments AID judgement — they do not replace it.
- **Option C (wrong)**: sound amplification is one narrow function.
- **Option D (wrong)**: instruments are central to engineering, not absent from it.

### Step 3: Exam Trap Summary
The trap is overstating ("replace judgement") or understating the role. The definition is about EXTENDING the senses — accuracy + speed + range.
r

**Key recall:** instruments scale electrical readings through $V = IR$.""")

theory(T, "An ammeter must be connected:",
       ["in series with the circuit, and must have a very LOW resistance",
        "in parallel with the circuit, with a very high resistance",
        "in series with a very high resistance",
        "in parallel with a very low resistance"], 0,
       "Ammeter: in series, very low resistance (must not disturb the current).",
       r"""### Step 1: Core Principle
The ammeter measures the current flowing through a circuit, so it is placed in SERIES with the branch being measured. Its own resistance must be very LOW so that inserting it does not change the current it is measuring.

### Step 2: Testing the Options
- **Option A (correct)**: series + low resistance.
- **Option B (wrong)**: that is the VOLTMETER arrangement.
- **Option C (wrong)**: a series high resistance would choke the very current being measured.
- **Option D (wrong)**: a parallel low resistance would divert current away from the load.

### Step 3: Exam Trap Summary
The trap is the ammeter/voltmeter swap. Anchor: Ammeter = series = Almost-zero resistance; Voltmeter = parallel = Very large resistance.
r

**Key relation:** the shunt design equation is $I_m R_m = (I - I_m) R_{sh}$.""")

theory(T, "A voltmeter must be connected:",
       ["in parallel with the component, and must have a very HIGH resistance",
        "in series with the circuit, with a very low resistance",
        "in parallel with a very low resistance",
        "in series with a very high resistance"], 0,
       "Voltmeter: in parallel, very high resistance (draws negligible current).",
       r"""### Step 1: Core Principle
The voltmeter measures the potential difference ACROSS a component, so it is placed in PARALLEL with that component. Its resistance must be very HIGH so that it draws a negligible current and does not alter the voltage it is measuring.

### Step 2: Testing the Options
- **Option A (correct)**: parallel + high resistance.
- **Option B (wrong)**: that is the AMMETER arrangement.
- **Option C (wrong)**: a parallel low resistance would load the circuit and collapse the voltage.
- **Option D (wrong)**: a series voltmeter would block the circuit.

### Step 3: Exam Trap Summary
The ammeter/voltmeter swap again. Anchor: Voltmeter = parallel = Very high resistance (the two V's).
r

**Key relation:** the multiplier design is $R_t = V/I_{fsd}$, multiplier $= R_t - R_m$.""")

theory(T, "The permanent-magnet moving-coil (PMMC) instrument:",
       ["works on DC only (deflection reverses with polarity) and has a uniform scale",
        "works on AC and DC equally",
        "measures only AC power",
        "needs no magnet"], 0,
       "PMMC: DC only, uniform scale, polarity-sensitive.",
       r"""### Step 1: Core Principle
The PMMC (permanent-magnet moving coil) instrument uses a permanent magnet and a coil free to rotate in it. The deflection is proportional to the DC current through the coil, reverses if the polarity reverses (so it cannot read AC directly), and the scale is UNIFORM (linear).

### Step 2: Testing the Options
- **Option A (correct)**: DC-only + uniform scale.
- **Option B (wrong)**: on AC the pointer would merely vibrate around zero.
- **Option C (wrong)**: PMMC measures current/voltage, not power directly.
- **Option D (wrong)**: the permanent magnet is essential to its operation.

### Step 3: Exam Trap Summary
The trap is assuming all meters read both AC and DC. Anchor: PMMC = DC-only (permanent magnet gives fixed field direction); moving-iron = AC and DC.
r

**Key recall:** PMMC deflection is proportional to the DC current, $\text{deflection} \propto I$ (linear scale).""")

theory(T, "The moving-iron instrument:",
       ["works on both AC and DC (reads r.m.s.) and is robust, but has a non-uniform scale",
        "works on DC only",
        "has a perfectly uniform scale",
        "is used only for frequency measurement"], 0,
       "Moving iron: AC + DC (r.m.s.), robust, non-uniform scale.",
       r"""### Step 1: Core Principle
The moving-iron instrument deflects by the repulsion/attraction between fixed and moving iron pieces in the coil's field. The effect depends on the square of the current, so it responds to both AC and DC (indicating r.m.s. on AC). It is cheap and robust, but its scale is non-uniform (cramped at low readings).

### Step 2: Testing the Options
- **Option A (correct)**: AC + DC, robust, non-uniform scale.
- **Option B (wrong)**: it is the PMMC that is DC-only.
- **Option C (wrong)**: the scale is non-uniform — the opposite.
- **Option D (wrong)**: it measures current/voltage, not frequency.

### Step 3: Exam Trap Summary
The trap is transferring PMMC properties to the moving-iron type. Anchor the contrast: PMMC = DC only, uniform scale; moving iron = AC+DC, non-uniform scale.
r

**Key recall:** moving-iron deflection depends on the square of the current ($I^2$).""")

calc(T, "A moving-coil movement has full-scale deflection at 100 µA and internal resistance Rₘ = 1 kΩ. To use it as a 10 V voltmeter, the series multiplier required is:",
     ["99 kΩ", "100 kΩ", "10 kΩ", "1 kΩ"], 0,
     "Rₜ = V/I = 10/10⁻⁴ = 100 kΩ; multiplier = Rₜ − Rₘ = 100 − 1 = 99 kΩ.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: full-scale deflection current $I = 100\ \mu A = 1 \times 10^{-4}\ A$, movement resistance $R_m = 1\ k\Omega = 1000\ \Omega$, desired range $V = 10\ V$.
Governing laws:
$$R_t = \frac{V}{I} \qquad \text{multiplier} = R_t - R_m$$

### Step 2: Full Mathematical Workings
Step A — total resistance needed to drop 10 V at 100 µA:
$$R_t = \frac{10}{1 \times 10^{-4}}$$
$$R_t = 10 \times 10^{4}$$
$$R_t = 100\,000\ \Omega = 100\ k\Omega$$
Step B — subtract the movement's own resistance:
$$\text{multiplier} = 100\,000 - 1000$$
$$\text{multiplier} = 99\,000\ \Omega$$
$$\text{multiplier} = 99\ k\Omega$$

### Step 3: Verification & Physical Interpretation
The series multiplier absorbs 99 V of the 10 V range while the movement takes its own 0.1 V (100 µA × 1 kΩ). Checking: total 100 kΩ × 100 µA = 10 V — exact full scale.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (100 kΩ)**: the student forgets to SUBTRACT the movement resistance Rₘ.
- **Option C trap (10 kΩ)**: the student uses 1 mA instead of 100 µA for the movement current.
- **Option D trap (1 kΩ)**: the student quotes Rₘ itself, confusing it with the multiplier.
r""")

calc(T, "A moving-coil movement deflects fully at 50 µA and has Rₘ = 2 kΩ. To use it as a 5 V voltmeter, the series multiplier needed is:",
     ["98 kΩ", "100 kΩ", "50 kΩ", "10 kΩ"], 0,
     "Rₜ = 5/(5 × 10⁻⁵) = 100 kΩ; multiplier = 100 − 2 = 98 kΩ.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $I = 50\ \mu A = 5 \times 10^{-5}\ A$, $R_m = 2\ k\Omega = 2000\ \Omega$, $V = 5\ V$.
Governing laws:
$$R_t = \frac{V}{I} \qquad \text{multiplier} = R_t - R_m$$

### Step 2: Full Mathematical Workings
Step A:
$$R_t = \frac{5}{5 \times 10^{-5}}$$
$$R_t = 1 \times 10^{5}\ \Omega = 100\ k\Omega$$
Step B:
$$\text{multiplier} = 100\,000 - 2000$$
$$\text{multiplier} = 98\,000\ \Omega = 98\ k\Omega$$

### Step 3: Verification & Physical Interpretation
At full scale the movement drops 50 µA × 2 kΩ = 0.1 V, and the multiplier drops the remaining 4.9 V — together exactly 5 V.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (100 kΩ)**: forgetting to subtract Rₘ.
- **Option C trap (50 kΩ)**: using 100 µA as the movement current.
- **Option D trap (10 kΩ)**: using 0.5 mA as the movement current.
r""")

calc(T, "A 1 mA movement with Rₘ = 100 Ω is to be used as a 1 A ammeter. The shunt resistance required is about:",
     ["0.1 Ω", "1 Ω", "10 Ω", "100 Ω"], 0,
     "Iₘ Rₘ = (I − Iₘ) R_sh → R_sh = (0.001 × 100)/0.999 ≈ 0.1 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: movement current $I_m = 1\ mA = 0.001\ A$, movement resistance $R_m = 100\ \Omega$, desired full-scale current $I = 1\ A$.
Governing law — the shunt carries the excess current while the voltage across it equals the voltage across the movement:
$$I_m R_m = (I - I_m) R_{sh}$$

### Step 2: Full Mathematical Workings
Step A — current diverted through the shunt:
$$I - I_m = 1 - 0.001$$
$$I - I_m = 0.999\ A$$
Step B — rearrange for the shunt:
$$R_{sh} = \frac{I_m R_m}{I - I_m}$$
$$R_{sh} = \frac{0.001 \times 100}{0.999}$$
$$0.001 \times 100 = 0.1$$
$$R_{sh} = \frac{0.1}{0.999}$$
$$R_{sh} = 0.1001\ \Omega$$
$$R_{sh} \approx 0.1\ \Omega$$

### Step 3: Verification & Physical Interpretation
The shunt takes 999 mA while the movement takes its 1 mA; both see the same voltage (0.1 V). The tiny 0.1 Ω shunt keeps the ammeter's insertion resistance negligible, exactly as required.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (1 Ω)**: the student uses I = 0.1 A instead of 1 A.
- **Option C trap (10 Ω)**: the student divides by 0.01 — treating the movement current as 10 mA.
- **Option D trap (100 Ω)**: the student quotes Rₘ itself — the shunt must be far SMALLER than the movement.
r""")

# =====================================================================
# TOPIC 9 — NONLINEAR CIRCUITS (INTRODUCTION)
# =====================================================================
T = "eee-nonlinear"

theory(T, "In the i-v world of circuits, a circuit is classified as linear if:",
       ["its i-v graph is a straight line",
        "it contains a diode",
        "its i-v graph is curved",
        "it contains an op-amp"], 0,
       "Linear ⇔ straight-line i-v graph (v = Ri).",
       r"""### Step 1: Core Principle
Classification is done by examining the circuit's i-v graph: if the graph is a straight line the circuit is linear ($v = Ri$); any other shape — curved, piecewise, or otherwise — is nonlinear.

### Step 2: Testing the Options
- **Option A (correct)**: the straight-line criterion.
- **Option B (wrong)**: a diode is the archetypal NONLINEAR component (exponential i-v).
- **Option C (wrong)**: a curved graph is the nonlinear case.
- **Option D (wrong)**: op-amps are components — linearity is judged by the i-v graph, not the part list.

### Step 3: Exam Trap Summary
The trap is judging by components. Always reduce the question to the graph: straight line = linear, anything else = nonlinear.
r""")

theory(T, "The function y = x² is:",
       ["nonlinear — its graph is a parabola, not a straight line",
        "linear — its graph is a straight line",
        "piecewise linear",
        "a constant"], 0,
       "y = x² plots as a parabola → nonlinear.",
       r"""### Step 1: Core Principle
$y = x^2$ plots as a parabola — a curve, not a straight line. Since it cannot be written in the form $y = ax + b$, it is nonlinear.

### Step 2: Testing the Options
- **Option A (correct)**: parabola → nonlinear.
- **Option B (wrong)**: the graph is visibly curved.
- **Option C (wrong)**: piecewise linear describes functions like |x|, made of straight SEGMENTS — x² is a smooth curve.
- **Option D (wrong)**: x² varies with x; it is not constant.

### Step 3: Exam Trap Summary
The trap is assuming "simple function = linear". Linearity is a SHAPE property: only straight lines qualify.
r""")

theory(T, "The absolute value function y = |x| is classified as:",
       ["nonlinear (piecewise linear), because it cannot be written in the form y = ax + b",
        "linear",
        "a parabola",
        "an exponential"], 0,
       "|x| is made of two straight pieces but cannot be written as ax + b — so it is nonlinear.",
       r"""### Step 1: Core Principle
The function $y = |x|$ consists of two straight segments (slope +1 for x > 0, slope −1 for x < 0) meeting at a corner. It is still classified as NONLINEAR because no single expression of the form $y = ax + b$ describes the whole function.

### Step 2: Testing the Options
- **Option A (correct)**: piecewise linear, yet nonlinear.
- **Option B (wrong)**: two different slopes mean no single ax + b form exists.
- **Option C (wrong)**: a parabola curves smoothly; |x| has a corner.
- **Option D (wrong)**: an exponential is a different shape entirely.

### Step 3: Exam Trap Summary
This is the classic trap question: "its pieces are straight, so it must be linear". The classification depends on the WHOLE function being one straight line.
r""")

theory(T, "Why are nonlinear circuits important in engineering?",
       ["electrical devices like amplifiers and computers are built from nonlinear components",
        "they are easier to analyse than linear circuits",
        "they have no practical applications",
        "all practical circuits are linear"], 0,
       "Amplifiers, computers and most devices are built from nonlinear components.",
       r"""### Step 1: Core Principle
Electrical devices — amplifiers, computers, and most practical electronics — are built from nonlinear components. Understanding nonlinear circuits is therefore necessary to understand the design of these devices; this is where "real engineering" begins.

### Step 2: Testing the Options
- **Option A (correct)**: nonlinear components underlie real devices.
- **Option B (wrong)**: nonlinear circuits are HARDER to analyse — there are no hard-and-fast rules for most of them.
- **Option C (wrong)**: the applications are everywhere (oscillators, rectifiers, logic gates).
- **Option D (wrong)**: real circuits are overwhelmingly nonlinear.

### Step 3: Exam Trap Summary
The trap is assuming "easier = more important". The notes stress the opposite: nonlinearity is harder precisely because it is where real design happens.
r

**Key recall:** linear means the form $y = ax + b$; real devices depart from this straight line.""")

theory(T, "The negative resistance converter is:",
       ["a useful nonlinear op-amp circuit whose i-v slope is negative over a region, used to build oscillators",
        "a resistor that obeys Ohm's law",
        "a transformer winding arrangement",
        "a rectifier circuit"], 0,
       "Negative-resistance converter: negative i-v slope → delivers power → oscillator core.",
       r"""### Step 1: Core Principle
The negative resistance converter is an op-amp nonlinear circuit whose i-v characteristic has a negative slope over some region: increasing voltage produces decreasing current. Over that region it DELIVERS power instead of absorbing it — the exact property an oscillator needs to sustain its own oscillations.

### Step 2: Testing the Options
- **Option A (correct)**: the converter and its oscillator application.
- **Option B (wrong)**: an Ohmic resistor has a positive slope.
- **Option C (wrong)**: it is built around an op-amp, not transformer windings.
- **Option D (wrong)**: a rectifier converts AC to DC — unrelated to negative slope.

### Step 3: Exam Trap Summary
The trap is reading "negative resistance" as "small resistance". It means a NEGATIVE SLOPE on the i-v curve — power-source behaviour, not a tiny resistor.
r

**Key recall:** the negative-slope region has $dV/dI < 0$ — power-source behaviour.""")
