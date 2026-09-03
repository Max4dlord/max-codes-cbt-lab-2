# -*- coding: utf-8 -*-
r"""EEE 202 question bank — PART A (topics 1–5).
Every calculation solution is exhaustive (Step 1–4, every line of working in
$$...$$ blocks, zero step-skipping) and analyses the trap behind each wrong
option. Theoretical solutions give the core principle, option-by-option
testing and the exam-trap summary.r"""

QUESTIONS_A = []

def calc(topic, q, opts, ans, short, sol):
    QUESTIONS_A.append(dict(topicId=topic, kind="calc", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

def theory(topic, q, opts, ans, short, sol):
    QUESTIONS_A.append(dict(topicId=topic, kind="theory", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

# =====================================================================
# TOPIC 1 — MAGNETISM & MOVING CHARGES
# =====================================================================
T = "eee-magnetism"

calc(T, "A charged particle with q = 40 C travels at 5 m/s in a magnetic field of 2 T, and the field direction is the SAME as the particle's path. The magnetic force on the particle is:",
     ["0 N", "400 N", "200 N", "800 N"], 0,
     "F = qvB sin θ, and since the motion is parallel to the field, θ = 0° so sin 0° = 0 and F = 0.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: charge $q = 40\ C$, velocity $v = 5\ m/s$, magnetic field $B = 2\ T$, and the field lies along the particle's path, so the angle between $v$ and $B$ is $\theta = 0^\circ$.
Governing law — the magnetic force on a moving charge:
$$F = qvB\sin\theta$$

### Step 2: Full Mathematical Workings
Substitute every value:
$$F = 40 \times 5 \times 2 \times \sin 0^\circ$$
$$40 \times 5 = 200$$
$$200 \times 2 = 400$$
$$F = 400 \times \sin 0^\circ$$
$$\sin 0^\circ = 0$$
$$F = 400 \times 0$$
$$F = 0\ N$$

### Step 3: Verification & Physical Interpretation
A charge moving PARALLEL to the magnetic field experiences no magnetic force — the force depends on the component of velocity cutting across the field. Zero crossing component means zero force. The result is physically consistent: field lines exert no side-ways push on a charge sliding along them.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (400 N)**: the student forgets the sine term entirely, effectively taking θ = 90° where sin 90° = 1.
- **Option C trap (200 N)**: the student substitutes θ = 30° (half of a right angle) and computes 400 × 0.5.
- **Option D trap (800 N)**: the student doubles the product, e.g. by multiplying by 2 again after computing 400.
r""")

calc(T, "A charged particle with q = 4 C travels at v = 20 m/s in a magnetic field B = 10 T, with an angle of 30° between v and B. The magnetic force on the particle is:",
     ["400 N", "800 N", "346 N", "200 N"], 0,
     "F = qvB sin θ = 4 × 20 × 10 × sin 30° = 800 × 0.5 = 400 N.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $q = 4\ C$, $v = 20\ m/s$, $B = 10\ T$, angle $\theta = 30^\circ$.
Governing law:
$$F = qvB\sin\theta$$

### Step 2: Full Mathematical Workings
$$F = 4 \times 20 \times 10 \times \sin 30^\circ$$
$$4 \times 20 = 80$$
$$80 \times 10 = 800$$
$$F = 800 \times \sin 30^\circ$$
$$\sin 30^\circ = \frac{1}{2} = 0.5$$
$$F = 800 \times 0.5$$
$$F = 400\ N$$

### Step 3: Verification & Physical Interpretation
Only the velocity component perpendicular to the field contributes to the force. At 30°, exactly half the full perpendicular force is developed, giving 400 N. The result matches the worked example in the lecture notes.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (800 N)**: the student uses sin 90° = 1 instead of sin 30°, ignoring the angle.
- **Option C trap (346 N)**: the student uses the cosine instead of the sine — cos 30° = 0.866 gives 800 × 0.866 ≈ 692.8 N; taking half of that value (346 N) is the classic "sine–cosine confusion" error.
- **Option D trap (200 N)**: the student divides by 4 (800/4) instead of by 2, i.e. treats sin 30° as 0.25.
r""")

calc(T, "A straight conductor of length 2 m carries a current of 3 A perpendicular to a magnetic field of 1.5 T. The force on the conductor is:",
     ["9 N", "4.5 N", "18 N", "0 N"], 0,
     "F = BIl sin θ = 1.5 × 3 × 2 × sin 90° = 9 N.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: length $l = 2\ m$, current $I = 3\ A$, field $B = 1.5\ T$, and the conductor is PERPENDICULAR to the field, so $\theta = 90^\circ$.
Governing law — force on a current-carrying conductor:
$$F = BIl\sin\theta$$

### Step 2: Full Mathematical Workings
$$F = 1.5 \times 3 \times 2 \times \sin 90^\circ$$
$$1.5 \times 3 = 4.5$$
$$4.5 \times 2 = 9$$
$$\sin 90^\circ = 1$$
$$F = 9 \times 1$$
$$F = 9\ N$$

### Step 3: Verification & Physical Interpretation
With the conductor cutting the field at right angles the full force develops. The direction follows Fleming's left-hand rule. Nine newtons is consistent with the moderate current, field and length given.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (4.5 N)**: the student stops after computing $B \times I$ and forgets to multiply by the length $l$.
- **Option C trap (18 N)**: the student doubles the answer, e.g. by taking the length as 4 m (double-sided conductor) or multiplying by 2 twice.
- **Option D trap (0 N)**: the student thinks a perpendicular conductor feels no force — the true zero-force case is a PARALLEL conductor.
r""")

calc(T, "A conductor of length 0.5 m carrying an unknown current i lies in a magnetic field B = 3 T at θ = 30° and experiences a force of 12 N. The current i is:",
     ["16 A", "8 A", "4 A", "24 A"], 0,
     "i = F/(Bl sin θ) = 12/(3 × 0.5 × 0.5) = 12/0.75 = 16 A.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: force $F = 12\ N$, length $l = 0.5\ m$, field $B = 3\ T$, angle $\theta = 30^\circ$.
Governing law, rearranged for the current:
$$F = BIl\sin\theta \quad\Rightarrow\quad I = \frac{F}{Bl\sin\theta}$$

### Step 2: Full Mathematical Workings
$$I = \frac{12}{3 \times 0.5 \times \sin 30^\circ}$$
$$3 \times 0.5 = 1.5$$
$$\sin 30^\circ = 0.5$$
$$1.5 \times 0.5 = 0.75$$
$$I = \frac{12}{0.75}$$
$$I = 16\ A$$

### Step 3: Verification & Physical Interpretation
The current of 16 A reproduces the given force: checking forward, $F = 3 \times 16 \times 0.5 \times 0.5 = 12\ N$, which confirms the rearrangement. Sixteen amperes is a realistic workshop-scale current.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (8 A)**: the student omits sin 30°, dividing by $Bl = 1.5$ instead of 0.75.
- **Option C trap (4 A)**: the student divides by 3 — treating the field value as the denominator instead of the product $Bl\sin\theta$.
- **Option D trap (24 A)**: the student multiplies by 2 after the division, i.e. computes 12/0.75 × 1.5.
r""")

calc(T, "A 2 m long solenoid has 2000 loops and carries 1600 A. The magnetic field strength at its centre is: (take μ₀ = 4π × 10⁻⁷ T·m/A)",
     ["2.01 T", "4.02 T", "0.50 T", "0.31 T"], 0,
     "B = μ₀ n I with n = N/L = 1000 turns/m, so B = (4π × 10⁻⁷)(1000)(1600) ≈ 2.01 T.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: solenoid length $L = 2\ m$, turns $N = 2000$, current $I = 1600\ A$, $\mu_0 = 4\pi\times10^{-7}\ T\cdot m/A$.
Governing law — field at the centre of a solenoid:
$$B = \mu_0 n I \quad\text{where}\quad n = \frac{N}{L}$$

### Step 2: Full Mathematical Workings
Compute the turns per metre first:
$$n = \frac{2000}{2}$$
$$n = 1000\ \text{turns per metre}$$
Substitute into the field law:
$$B = (4\pi \times 10^{-7}) \times 1000 \times 1600$$
$$4\pi \times 10^{-7} = 1.25664 \times 10^{-6}$$
$$1.25664 \times 10^{-6} \times 1000 = 1.25664 \times 10^{-3}$$
$$1.25664 \times 10^{-3} \times 1600 = 2.0106$$
$$B = 2.01\ T$$

### Step 3: Verification & Physical Interpretation
Two tesla is an extremely strong field, consistent with the huge current of 1600 A. The result matches the first solved example in the lecture notes exactly.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (4.02 T)**: the student uses the total turns $N = 2000$ instead of $n = N/L = 1000$ — forgetting to divide by the solenoid length exactly doubles the answer.
- **Option C trap (0.50 T)**: the student drops the factor 4 from $\mu_0 = 4\pi\times10^{-7}$, using $\pi\times10^{-7}$ instead.
- **Option D trap (0.31 T)**: the student copies the printed answer of the NEXT worked example (the 5 m solenoid) — a memorisation slip rather than a calculation error.
r""")

calc(T, "A 5 m long solenoid has 800 loops and carries 1700 A. The magnetic field strength at its centre is about:",
     ["0.34 T", "0.31 T", "1.71 T", "0.68 T"], 0,
     "n = 800/5 = 160 turns/m, so B = (4π × 10⁻⁷)(160)(1700) = 0.342 T ≈ 0.34 T (the notes' printed value 0.314 T is a rounding slip).",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 5\ m$, $N = 800$, $I = 1700\ A$, $\mu_0 = 4\pi\times10^{-7}\ T\cdot m/A$.
Governing law:
$$B = \mu_0 n I \quad\text{with}\quad n = \frac{N}{L}$$

### Step 2: Full Mathematical Workings
$$n = \frac{800}{5}$$
$$n = 160\ \text{turns per metre}$$
$$B = (4\pi \times 10^{-7}) \times 160 \times 1700$$
$$4\pi \times 10^{-7} = 1.25664 \times 10^{-6}$$
$$160 \times 1700 = 272\,000$$
$$B = 1.25664 \times 10^{-6} \times 272\,000$$
$$B = 0.3418\ T$$
$$B \approx 0.34\ T$$

### Step 3: Verification & Physical Interpretation
The computed value 0.342 T rounds to 0.34 T. The lecture notes print 0.314 T for this example — a transcription rounding slip — but the exact product of the stated numbers is 0.342 T, so 0.34 T is the mathematically correct option.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.31 T)**: the student copies the printed (slightly wrong) notes value without recomputing — always verify worked examples yourself.
- **Option C trap (1.71 T)**: the student uses $N = 800$ instead of $n = 160$, forgetting the division by the length $L = 5$.
- **Option D trap (0.68 T)**: the student halves the length (n = 320) or doubles the turns, doubling the field.
r""")

calc(T, "A 12 m long solenoid of 700 loops carries 800 A. The magnetic field strength at its centre is about:",
     ["0.0586 T", "0.0293 T", "0.117 T", "0.703 T"], 0,
     "n = 700/12 = 58.33 turns/m, so B = (4π × 10⁻⁷)(58.33)(800) = 0.0586 T.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 12\ m$, $N = 700$, $I = 800\ A$, $\mu_0 = 4\pi\times10^{-7}\ T\cdot m/A$.
Governing law:
$$B = \mu_0 n I \quad\text{with}\quad n = \frac{N}{L}$$

### Step 2: Full Mathematical Workings
$$n = \frac{700}{12}$$
$$n = 58.33\ \text{turns per metre}$$
$$B = (4\pi \times 10^{-7}) \times 58.33 \times 800$$
$$4\pi \times 10^{-7} = 1.25664 \times 10^{-6}$$
$$58.33 \times 800 = 46\,664$$
$$B = 1.25664 \times 10^{-6} \times 46\,664$$
$$B = 0.05864\ T$$
$$B \approx 0.0586\ T$$

### Step 3: Verification & Physical Interpretation
The long 12 m solenoid spreads its 700 turns thinly (only 58 turns per metre), so the field is small — about 0.059 T — matching the third solved example in the notes.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.0293 T)**: the student halves the turns-per-metre (or the current), halving the field.
- **Option C trap (0.117 T)**: the student doubles n or I, doubling the field.
- **Option D trap (0.703 T)**: the student uses total turns N = 700 instead of n = 58.33 — the missing ÷12 overstates the field by the factor L.
r""")

calc(T, "A 1 m long solenoid of 500 turns carries 4 A. The magnetic field at its centre is about:",
     ["2.51 mT", "5.03 mT", "0.63 mT", "1.26 mT"], 0,
     "n = 500 turns/m, so B = (4π × 10⁻⁷)(500)(4) = 2.51 × 10⁻³ T = 2.51 mT.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 1\ m$, $N = 500$, $I = 4\ A$, $\mu_0 = 4\pi\times10^{-7}\ T\cdot m/A$.
Governing law:
$$B = \mu_0 n I \quad\text{with}\quad n = \frac{N}{L}$$

### Step 2: Full Mathematical Workings
$$n = \frac{500}{1} = 500\ \text{turns per metre}$$
$$B = (4\pi \times 10^{-7}) \times 500 \times 4$$
$$4\pi \times 10^{-7} = 1.25664 \times 10^{-6}$$
$$500 \times 4 = 2000$$
$$B = 1.25664 \times 10^{-6} \times 2000$$
$$B = 2.513 \times 10^{-3}\ T$$
$$B = 2.51\ mT$$

### Step 3: Verification & Physical Interpretation
A compact 500-turn coil at 4 A produces about 2.5 millitesla — a typical small-solenoid value. Note the unit conversion: $2.51\times10^{-3}\ T = 2.51\ mT$.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (5.03 mT)**: the student doubles the turns or the current before substituting.
- **Option C trap (0.63 mT)**: the student drops the factor 4 in $\mu_0$ (using $\pi\times10^{-7}$), quartering the answer.
- **Option D trap (1.26 mT)**: the student halves the product — for example, by dividing by 2 after the multiplication.
r""")

calc(T, "A charge of 2 C moves at 10 m/s PERPENDICULAR to a magnetic field of 0.5 T. The magnetic force is:",
     ["10 N", "5 N", "20 N", "0 N"], 0,
     "F = qvB sin θ = 2 × 10 × 0.5 × sin 90° = 10 N.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $q = 2\ C$, $v = 10\ m/s$, $B = 0.5\ T$, and the motion is perpendicular to the field so $\theta = 90^\circ$.
Governing law:
$$F = qvB\sin\theta$$

### Step 2: Full Mathematical Workings
$$F = 2 \times 10 \times 0.5 \times \sin 90^\circ$$
$$2 \times 10 = 20$$
$$20 \times 0.5 = 10$$
$$\sin 90^\circ = 1$$
$$F = 10 \times 1$$
$$F = 10\ N$$

### Step 3: Verification & Physical Interpretation
Perpendicular motion develops the maximum force for the given charge, speed and field. Ten newtons is the ceiling value — any other angle would give less.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (5 N)**: the student halves the product (e.g. treats the field as 0.25 T or the charge as 1 C).
- **Option C trap (20 N)**: the student stops after computing $qv = 20$ and forgets the field factor 0.5.
- **Option D trap (0 N)**: the student applies the parallel-motion rule (θ = 0°) to a perpendicular case.
r""")

calc(T, "A charge of 5 C moves at 4 m/s at 90° to a field of 0.3 T. The magnetic force is:",
     ["6 N", "12 N", "3 N", "0 N"], 0,
     "F = qvB sin θ = 5 × 4 × 0.3 × 1 = 6 N.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $q = 5\ C$, $v = 4\ m/s$, $B = 0.3\ T$, $\theta = 90^\circ$.
Governing law:
$$F = qvB\sin\theta$$

### Step 2: Full Mathematical Workings
$$F = 5 \times 4 \times 0.3 \times \sin 90^\circ$$
$$5 \times 4 = 20$$
$$20 \times 0.3 = 6$$
$$\sin 90^\circ = 1$$
$$F = 6\ N$$

### Step 3: Verification & Physical Interpretation
At right angles the full force develops; six newtons follows directly from the product of the three given quantities. This is the same pattern as the perpendicular conductor case, applied to a free charge.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (12 N)**: the student doubles the product (e.g. uses B = 0.6 T).
- **Option C trap (3 N)**: the student halves the product (e.g. uses θ = 30°).
- **Option D trap (0 N)**: the student uses sin 0° — the parallel-motion trap.
r""")

theory(T, "Magnetism is best defined as:",
       ["the force produced by moving charges that attracts or repels other magnets and moving charges",
        "the force between two stationary electric charges",
        "the ability of a material to conduct electricity",
        "the resistance of a material to being magnetised"], 0,
       "Magnetism is the phenomenon associated with magnetic fields, which are produced by moving electric charges.",
       r"""### Step 1: Core Principle
The lecture notes define magnetism as the force produced by moving charge which attracts or repels other magnets and moving charges. Magnetic fields are produced by moving electric charges, so magnetism is a property of moving charged particles.

### Step 2: Testing the Options
- **Option A (correct)**: matches the notes' definition word for word — moving charges produce the force.
- **Option B (wrong)**: that is the electrostatic (Coulomb) force between STATIC charges — the opposite situation.
- **Option C (wrong)**: conductivity is a material property (how easily current flows), not magnetism.
- **Option D (wrong)**: resistance to magnetisation describes coercivity/diamagnetism, not magnetism itself.

### Step 3: Exam Trap Summary
The trap is confusing magnetism (moving charges) with electrostatics (static charges). In the exam, look for the phrase "moving charges" — it is the defining feature.
r

**Key relation:** the force law behind magnetism is $F = qvB\sin\theta$.""")

theory(T, "For any two magnetic poles:",
       ["like poles repel each other and opposite poles attract each other",
        "like poles attract each other and opposite poles repel each other",
        "all poles attract each other regardless of type",
        "poles neither attract nor repel"], 0,
       "Like poles repel; opposite (unlike) poles attract.",
       r"""### Step 1: Core Principle
The fundamental law of magnet poles: like (same-type) poles repel one another, and unlike (opposite) poles attract one another.

### Step 2: Testing the Options
- **Option A (correct)**: the standard statement of pole interaction.
- **Option B (wrong)**: it reverses both rules — the classic memory inversion.
- **Option C (wrong)**: only unlike poles attract; like poles repel.
- **Option D (wrong)**: poles always interact — there is no neutral case.

### Step 3: Exam Trap Summary
Students commonly invert the rule under pressure. Fix it by remembering the parallel with electric charges: same sign repel, opposite sign attract — magnets behave the same way for poles.
r

**Key recall:** the pole law is qualitative; the related quantitative law is $F = BIl\sin\theta$.""")

theory(T, "The property of magnetism was first observed in a naturally occurring material called:",
       ["Magnetite (Fe₃O₄)", "Hematite (Fe₂O₃)", "Bauxite (Al₂O₃)", "Calcite (CaCO₃)"], 0,
       "Magnetism was first observed in magnetite, Fe₃O₄ — hence the name 'magnets'.",
       r"""### Step 1: Core Principle
The notes state that the property of magnetism was first observed in a material called magnetite, $Fe_3O_4$ — hence the name "magnets". Magnetite is scattered around the Earth's crust and was first noticed by a shepherd in Greece.

### Step 2: Testing the Options
- **Option A (correct)**: magnetite, $Fe_3O_4$, is the historical first magnet.
- **Option B (wrong)**: hematite, $Fe_2O_3$, is an iron ore but not the first known magnetic material.
- **Option C (wrong)**: bauxite is aluminium ore — irrelevant to magnetism.
- **Option D (wrong)**: calcite is calcium carbonate — non-magnetic.

### Step 3: Exam Trap Summary
The trap is matching "magnetite" to the wrong formula. Anchor the pair: magnetite = Fe₃O₄ (three oxygens, the magnetic one).
r""")

theory(T, "Materials in which the electrons are arranged so their magnetic effects do NOT cancel out are called:",
       ["ferromagnetic materials", "diamagnetic materials", "insulators", "semiconductors"], 0,
       "Ferromagnetic materials have uncancelled electron magnets and act as permanent magnets.",
       r"""### Step 1: Core Principle
In most materials the individual electron magnets cancel each other out, so the material shows no net magnetism. In ferromagnetic materials the electrons are arranged so their magnetic effects do NOT cancel — they behave as permanent magnets and attract other metallic materials naturally.

### Step 2: Testing the Options
- **Option A (correct)**: ferromagnetic — the uncancelled arrangement.
- **Option B (wrong)**: diamagnetic materials weakly OPPOSE an applied field rather than showing uncancelled internal magnetism.
- **Option C (wrong)**: insulators are classified by electrical conduction, not magnetism.
- **Option D (wrong)**: semiconductors are likewise a conduction classification.

### Step 3: Exam Trap Summary
The trap is mixing material classifications: magnetic classes (ferro/para/dia) versus electrical classes (conductor/insulator/semiconductor). The question is about magnetism, so the answer must be a magnetic class.
r

**Key relation:** ferromagnetic materials have relative permeability $\mu_r \gg 1$ (hundreds to thousands).""")

theory(T, "Electromotive force (e.m.f.) is:",
       ["that which tends to produce an electric current in a circuit, with unit the volt (V)",
        "the opposition to current flow, with unit the ohm (Ω)",
        "the stored charge of a capacitor, with unit the coulomb (C)",
        "the power dissipated in a resistor, with unit the watt (W)"], 0,
       "e.m.f. is that which tends to produce an electric current in a circuit; symbol E, unit volt.",
       r"""### Step 1: Core Principle
The notes define: an electromotive force is that which tends to produce an electric current in a circuit, and the unit of e.m.f. is the volt. Symbol E, unit V.

### Step 2: Testing the Options
- **Option A (correct)**: the exact definition and unit from the notes.
- **Option B (wrong)**: opposition to current is resistance (ohm).
- **Option C (wrong)**: stored charge is the coulomb — a quantity, not a driving force.
- **Option D (wrong)**: power dissipation is the watt — an effect, not a cause of current.

### Step 3: Exam Trap Summary
The trap is confusing the four electrical quantities (e.m.f., resistance, charge, power). Anchor: e.m.f. is the "pressure" that DRIVES current, measured in volts.
r

**Key relation:** the e.m.f. drives current through the circuit per Ohm's law $I = E/R$.""")

theory(T, "Which of the following is NOT listed as a principal source of e.m.f.?",
       ["Friction between two insulators",
        "Electrodes of dissimilar materials immersed in an electrolyte (cells)",
        "Relative movement of a conductor and a magnetic flux (generators)",
        "Difference of temperature between junctions of dissimilar metals (thermo-junctions)"], 0,
       "The notes list cells, generators and thermo-junctions as e.m.f. sources — friction between insulators is not one of them.",
       r"""### Step 1: Core Principle
The notes list three principal sources of e.m.f.:
1. Electrodes of dissimilar materials in an electrolyte — primary and secondary cells (batteries).
2. Relative movement of a conductor and a magnetic flux — electric generators (equivalently, variation of flux linked with a coil).
3. Difference of temperature between junctions of dissimilar metals — thermo-junctions.

### Step 2: Testing the Options
- **Option A (correct as "not listed")**: friction between insulators produces static charge build-up, not a circuit-driving e.m.f., and is absent from the list.
- **Option B (wrong choice)**: cells are source 1.
- **Option C (wrong choice)**: generators are source 2.
- **Option D (wrong choice)**: thermo-junctions are source 3.

### Step 3: Exam Trap Summary
This is a "but one/except" question — read the negative carefully. The trap is rushing and picking a genuine source instead of the intruder.
r

**Key recall:** the generator source obeys the motional law $E = Blv$.""")

theory(T, "The B-field and the H-field are distinguished as follows:",
       ["The B-field is defined by the force it exerts on a moving charged particle (tesla), while the H-field is the magnetic field within a material (A/m)",
        "The B-field is measured in A/m and the H-field in tesla",
        "The H-field is defined by force on a moving charge and the B-field is within a material",
        "They are identical quantities with different names"], 0,
       "B-field = force-based definition, measured in tesla; H-field = field within a material, measured in A/m.",
       r"""### Step 1: Core Principle
The notes define:
- B-field: the magnetic field defined by the FORCE it exerts on a moving charged particle; measured in tesla (T); in CGS it is the gauss ($1\ T = 10^4\ G$).
- H-field: the magnetic field WITHIN a material rather than in a vacuum; measured in ampere/metre (A/m); in CGS the oersted ($1\ Oe = 1000/4\pi\ A/m \approx 79.577\ A/m$).

### Step 2: Testing the Options
- **Option A (correct)**: matches both definitions and both units.
- **Option B (wrong)**: swaps the units of the two fields.
- **Option C (wrong)**: swaps the definitions of the two fields.
- **Option D (wrong)**: they are distinct quantities linked by $B = \mu H$.

### Step 3: Exam Trap Summary
The trap is unit/definition swapping. Anchor: B for "body force" (tesla, what you feel), H for "hidden inside" (A/m, inside the material).
r""")

theory(T, "Which statement about magnetic field lines is FALSE?",
       ["Inside the magnet they run from the north pole to the south pole",
        "They never cross each other",
        "They form closed loops",
        "When parallel they repel one another"], 0,
       "Inside the magnet the field runs south→north (to close the loop); all other statements are true.",
       r"""### Step 1: Core Principle
Field-line rules: field lines form closed loops, never cross, and when parallel they repel one another. OUTSIDE a magnet the lines run north to south; INSIDE the magnet they run south to north, closing the loop.

### Step 2: Testing the Options
- **Option A (correct as FALSE)**: inside the magnet the lines run SOUTH to NORTH — stating north to south is the false statement.
- **Option B (true)**: lines never cross; crossing would imply two field directions at one point.
- **Option C (true)**: magnetic lines are closed loops (no isolated magnetic charges).
- **Option D (true)**: parallel lines repel, as in the Hughes summary of important formulae.

### Step 3: Exam Trap Summary
The trap is remembering only the outside-the-magnet convention (N→S) and applying it inside the magnet, where the direction reverses. Read "inside/outside" qualifiers with extreme care.
r

**Key recall:** for a solenoid, field strength follows $B = \mu_0 n I$ with $n = N/L$.""")

theory(T, "The force on a moving charge in a magnetic field is given by:",
       ["F = qvB sin θ", "F = qvB cos θ", "F = qE", "F = mB sin θ"], 0,
       "F = qvB sin θ, where θ is the angle between the velocity and the field.",
       r"""### Step 1: Core Principle
The lecture notes give the magnetic force on a moving charge as:
$$F = qvB\sin\theta$$
where $q$ is the charge, $v$ its velocity, $B$ the magnetic field, and $\theta$ the angle between the field and the velocity of the charge.

### Step 2: Testing the Options
- **Option A (correct)**: the sine form from the notes.
- **Option B (wrong)**: cosine would give maximum force for PARALLEL motion — physically backwards.
- **Option C (wrong)**: $F = qE$ is the ELECTRIC force, not the magnetic force.
- **Option D (wrong)**: mass $m$ appears in gravitational/Newtonian force expressions, not the magnetic force.

### Step 3: Exam Trap Summary
Two traps: using cosine (wrong angle convention) and confusing the electric force $qE$ with the magnetic force $qvB\sin\theta$. The magnetic force acts only on MOVING charges and only across the field.
r""")

# --- multi-part theoretical question (Topic 1) ---
theory(T, "Match each quantity to its SI unit: (a) magnetic flux (b) magnetic flux density (c) magnetic field strength (d) magnetomotive force.",
       ["weber, tesla, ampere per metre, ampere-turn",
        "tesla, weber, ampere per metre, volt",
        "weber, gauss, ampere per metre, ampere-turn",
        "tesla, weber, ampere-turn, ampere per metre"], 0,
       "Flux is measured in webers, flux density in teslas, field strength in A/m, and m.m.f. in ampere-turns.",
       r"""### Step 1: Core Principle
The four quantities and their SI units:
(a) magnetic flux $\Phi$ — weber (Wb)
(b) magnetic flux density $B = \Phi/A$ — tesla (T)
(c) magnetic field strength $H = NI/l$ — ampere per metre (A/m)
(d) magnetomotive force $F = NI$ — ampere-turn (At)

### Step 2: Testing the Options
- **Option A (correct)**: all four pairings are exact.
- **Option B (wrong)**: swaps flux and flux density in parts (a) and (b), and gives m.m.f. the unit volt (volt is the e.m.f. unit).
- **Option C (wrong)**: part (b) uses gauss — a CGS unit, not the SI unit.
- **Option D (wrong)**: parts (b) and (c) are swapped, and (c)/(d) are interchanged.

### Step 3: Exam Trap Summary
The traps are unit swaps between flux/ф density and between m.m.f./e.m.f. Anchor the chain: flux (Wb) → flux density (T = Wb/m²) → field strength (A/m) → m.m.f. (At), in decreasing "materiality".
r""")

# =====================================================================
# TOPIC 2 — ELECTROMAGNETIC INDUCTION & FARADAY'S LAWS
# =====================================================================
T = "eee-induction"

calc(T, "A coil of 50 turns is placed in a magnetic field whose flux density changes at a rate of 0.10 T/s. The e.m.f. induced in the coil is:",
     ["5 V", "0.5 V", "50 V", "0.002 V"], 0,
     "E = N × (dΦ/dt) = 50 × 0.10 = 5 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: turns $N = 50$, rate of change of flux $\frac{d\Phi}{dt} = 0.10\ T\cdot m^2/s$.
Governing law — Faraday's second law:
$$E = N\frac{d\Phi}{dt}$$

### Step 2: Full Mathematical Workings
$$E = 50 \times 0.10$$
$$E = 5.0\ V$$

### Step 3: Verification & Physical Interpretation
The induced e.m.f. is proportional to both the number of turns and the rate of flux change. Five volts is the magnitude; the minus sign of Lenz's law only indicates direction (opposing the change), so the reported magnitude is positive. This reproduces Solved Question 1 of the lecture notes.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.5 V)**: the student misplaces the decimal — reading the rate as 0.010 instead of 0.10.
- **Option C trap (50 V)**: the student multiplies by 100 turns instead of 50, or treats the rate as 1.0 T/s.
- **Option D trap (0.002 V)**: the student divides instead of multiplying ($50/0.10$ inverted to $0.10/50$).
r""")

calc(T, "A single loop of wire sits in a field whose flux increases at 0.02 T·m²/s. The loop's resistance is 5 Ω. The induced current is:",
     ["4 mA", "0.4 mA", "40 mA", "0.1 A"], 0,
     "E = N × (dΦ/dt) = 1 × 0.02 = 0.02 V; then I = E/R = 0.02/5 = 0.004 A = 4 mA.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: turns $N = 1$ (a single loop), $\frac{d\Phi}{dt} = 0.02\ T\cdot m^2/s$, resistance $R = 5\ \Omega$.
Governing laws — Faraday's second law and Ohm's law:
$$E = N\frac{d\Phi}{dt} \qquad I = \frac{E}{R}$$

### Step 2: Full Mathematical Workings
Step A — induced e.m.f.:
$$E = 1 \times 0.02$$
$$E = 0.02\ V$$
Step B — induced current:
$$I = \frac{0.02}{5}$$
$$I = 0.004\ A$$
Convert to milliamperes:
$$0.004\ A = 4\ mA$$

### Step 3: Verification & Physical Interpretation
The single loop develops only 0.02 V, and the 5 Ω loop limits the current to 4 milliamperes — small because there is only one turn. This matches Solved Question 2 of the notes.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.4 mA)**: the student computes E as 0.002 V (one decimal place too low) before dividing.
- **Option C trap (40 mA)**: the student computes E as 0.2 V (rate read as 0.2) before dividing.
- **Option D trap (0.1 A)**: the student computes I = 0.02 × 5 = 0.1 A — multiplying by R instead of dividing.
r""")

calc(T, "A coil of 100 turns has the flux through each turn decrease uniformly from 0.5 Wb to 0 Wb in 0.2 s. The induced e.m.f. is:",
     ["250 V", "25 V", "100 V", "500 V"], 0,
     "E = N × (ΔΦ/Δt) = 100 × (0.5/0.2) = 100 × 2.5 = 250 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 100$ turns, initial flux $\Phi_i = 0.5\ Wb$, final flux $\Phi_f = 0\ Wb$, time $\Delta t = 0.2\ s$.
Governing law (uniform-change form of Faraday's second law):
$$E = N\frac{\Delta\Phi}{\Delta t}$$

### Step 2: Full Mathematical Workings
Compute the flux change:
$$\Delta\Phi = \Phi_i - \Phi_f$$
$$\Delta\Phi = 0.5 - 0$$
$$\Delta\Phi = 0.5\ Wb$$
Compute the rate of change:
$$\frac{\Delta\Phi}{\Delta t} = \frac{0.5}{0.2}$$
$$\frac{\Delta\Phi}{\Delta t} = 2.5\ Wb/s$$
Multiply by the turns:
$$E = 100 \times 2.5$$
$$E = 250\ V$$

### Step 3: Verification & Physical Interpretation
Losing half a weber in only 0.2 s across 100 turns develops a strong 250 V. This is Solved Question 3 of the notes, reproduced exactly.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (25 V)**: the student forgets to multiply by N (computes only ΔΦ/Δt) or divides by 10.
- **Option C trap (100 V)**: the student multiplies N by the flux change only (100 × 0.5 × 2), mixing ΔΦ with Δt incorrectly.
- **Option D trap (500 V)**: the student uses Δt = 0.1 s (doubling the rate).
r""")

calc(T, "A rectangular coil of 20 turns, each of area 0.1 m², sits in a field B = 0.5 T. The coil is rotated so that the flux changes from its full value to zero in 0.05 s. The average e.m.f. induced is:",
     ["20 V", "10 V", "2 V", "40 V"], 0,
     "Φ = BA = 0.5 × 0.1 = 0.05 Wb; E = N × (ΔΦ/Δt) = 20 × (0.05/0.05) = 20 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 20$ turns, area per turn $A = 0.1\ m^2$, field $B = 0.5\ T$, time $\Delta t = 0.05\ s$.
Governing laws — flux through an area, then Faraday's second law:
$$\Phi = BA \qquad E = N\frac{\Delta\Phi}{\Delta t}$$

### Step 2: Full Mathematical Workings
Step A — initial flux (coil plane perpendicular to the field):
$$\Phi_i = BA$$
$$\Phi_i = 0.5 \times 0.1$$
$$\Phi_i = 0.05\ Wb$$
The coil is rotated until the flux is zero:
$$\Phi_f = 0\ Wb$$
$$\Delta\Phi = 0.05 - 0 = 0.05\ Wb$$
Step B — induced e.m.f.:
$$E = 20 \times \frac{0.05}{0.05}$$
$$\frac{0.05}{0.05} = 1$$
$$E = 20 \times 1$$
$$E = 20\ V$$

### Step 3: Verification & Physical Interpretation
The average induced e.m.f. of 20 V arises because the 0.05 Wb is removed in 0.05 s — a rate of 1 Wb/s across 20 turns. This matches Solved Question 4 of the notes.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (10 V)**: the student halves the rate — e.g. by using Δt = 0.1 s.
- **Option C trap (2 V)**: the student omits the turns N (0.05/0.05 = 1 V, then doubles it in a second slip).
- **Option D trap (40 V)**: the student doubles the turns or halves the time.
r""")

calc(T, "A coil of 80 turns has the flux through each turn decrease uniformly from 0.6 Wb to 0 Wb in 0.3 s. The induced e.m.f. is:",
     ["160 V", "16 V", "60 V", "320 V"], 0,
     "E = N × (ΔΦ/Δt) = 80 × (0.6/0.3) = 80 × 2 = 160 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 80$, $\Phi_i = 0.6\ Wb$, $\Phi_f = 0\ Wb$, $\Delta t = 0.3\ s$.
Governing law:
$$E = N\frac{\Delta\Phi}{\Delta t}$$

### Step 2: Full Mathematical Workings
$$\Delta\Phi = 0.6 - 0 = 0.6\ Wb$$
$$\frac{\Delta\Phi}{\Delta t} = \frac{0.6}{0.3}$$
$$\frac{0.6}{0.3} = 2\ Wb/s$$
$$E = 80 \times 2$$
$$E = 160\ V$$

### Step 3: Verification & Physical Interpretation
This is Unsolved Question 1 of the lecture notes, now solved: the flux vanishes at 2 Wb/s across 80 turns, giving 160 V.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (16 V)**: the student drops a factor of ten in the rate (0.2 Wb/s).
- **Option C trap (60 V)**: the student multiplies N by ΔΦ only (80 × 0.75 ≈ 60), confusing flux with rate.
- **Option D trap (320 V)**: the student halves the time to 0.15 s.
r""")

calc(T, "A single-turn circular loop of radius 0.1 m sits perpendicular to a field of 0.8 T which is then reduced to zero in 0.2 s. The induced e.m.f. is about: (take π = 3.14)",
     ["0.126 V", "0.063 V", "0.251 V", "1.26 V"], 0,
     "A = πr² = 3.14 × 0.01 = 0.0314 m²; Φ = BA = 0.8 × 0.0314 = 0.02513 Wb; E = ΔΦ/Δt = 0.02513/0.2 = 0.126 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 1$, radius $r = 0.1\ m$, field $B = 0.8\ T$, time $\Delta t = 0.2\ s$, $\pi = 3.14$.
Governing laws:
$$A = \pi r^2 \qquad \Phi = BA \qquad E = N\frac{\Delta\Phi}{\Delta t}$$

### Step 2: Full Mathematical Workings
Step A — loop area:
$$A = \pi r^2$$
$$A = 3.14 \times (0.1)^2$$
$$(0.1)^2 = 0.01$$
$$A = 3.14 \times 0.01$$
$$A = 0.0314\ m^2$$
Step B — initial flux (field perpendicular to the loop):
$$\Phi_i = BA$$
$$\Phi_i = 0.8 \times 0.0314$$
$$\Phi_i = 0.02512\ Wb$$
Step C — induced e.m.f. (flux falls to zero):
$$\Delta\Phi = 0.02512 - 0 = 0.02512\ Wb$$
$$E = 1 \times \frac{0.02512}{0.2}$$
$$E = \frac{0.02512}{0.2} = 0.1256\ V$$
$$E \approx 0.126\ V$$

### Step 3: Verification & Physical Interpretation
This is Unsolved Question 2 of the notes, now solved. The tiny loop area keeps the flux small, so the e.m.f. is a modest 126 mV despite the field vanishing in a fifth of a second.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.063 V)**: the student uses the diameter (0.2 m) as the radius, quartering... — in fact halving: using $A = \pi r$ instead of $\pi r^2$.
- **Option C trap (0.251 V)**: the student uses $\Delta t = 0.1$ s, doubling the answer.
- **Option D trap (1.26 V)**: the student misplaces the decimal — e.g. treating the radius as 1 m.
r""")

calc(T, "A coil of 50 turns sits in a field that changes at 0.15 T/s. The coil resistance is 10 Ω. The induced current is:",
     ["0.75 A", "7.5 A", "0.075 A", "1.5 A"], 0,
     "E = N × (dΦ/dt) = 50 × 0.15 = 7.5 V; I = E/R = 7.5/10 = 0.75 A.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 50$, $\frac{d\Phi}{dt} = 0.15\ T\cdot m^2/s$, $R = 10\ \Omega$.
Governing laws:
$$E = N\frac{d\Phi}{dt} \qquad I = \frac{E}{R}$$

### Step 2: Full Mathematical Workings
Step A — induced e.m.f.:
$$E = 50 \times 0.15$$
$$E = 7.5\ V$$
Step B — induced current:
$$I = \frac{7.5}{10}$$
$$I = 0.75\ A$$

### Step 3: Verification & Physical Interpretation
This is Unsolved Question 4 of the notes, now solved: 7.5 V across 10 Ω drives 0.75 A. The two-step pattern (Faraday then Ohm) is the standard exam pathway.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (7.5 A)**: the student stops at the e.m.f. and forgets to divide by R.
- **Option C trap (0.075 A)**: the student misplaces a decimal in E (0.75 V) before dividing.
- **Option D trap (1.5 A)**: the student doubles the current (e.g. by using R = 5 Ω).
r""")

calc(T, "A bar magnet moved towards a 40-turn coil increases the linked flux from 0 to 0.2 Wb in 0.05 s. With a coil resistance of 8 Ω, the induced e.m.f. and current are:",
     ["160 V and 20 A", "16 V and 2 A", "8 V and 1 A", "320 V and 40 A"], 0,
     "E = N × (ΔΦ/Δt) = 40 × (0.2/0.05) = 160 V; I = E/R = 160/8 = 20 A.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 40$, $\Phi_i = 0$, $\Phi_f = 0.2\ Wb$, $\Delta t = 0.05\ s$, $R = 8\ \Omega$.
Governing laws:
$$E = N\frac{\Delta\Phi}{\Delta t} \qquad I = \frac{E}{R}$$

### Step 2: Full Mathematical Workings
Step A — flux change:
$$\Delta\Phi = 0.2 - 0 = 0.2\ Wb$$
Step B — induced e.m.f.:
$$E = 40 \times \frac{0.2}{0.05}$$
$$\frac{0.2}{0.05} = 4\ Wb/s$$
$$E = 40 \times 4$$
$$E = 160\ V$$
Step C — induced current:
$$I = \frac{160}{8}$$
$$I = 20\ A$$

### Step 3: Verification & Physical Interpretation
This is Unsolved Question 5 of the notes, now solved. The fast magnet motion (0.05 s) across 40 turns gives 160 V, and the low coil resistance allows a strong 20 A induced current.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (16 V and 2 A)**: the student divides both answers by 10 — a decimal slip in the rate (0.4 Wb/s).
- **Option C trap (8 V and 1 A)**: the student omits N entirely and then divides by R.
- **Option D trap (320 V and 40 A)**: the student halves the time or doubles the turns, doubling both results.
r""")

calc(T, "A coil of 200 turns sits in a field changing at 0.05 T/s. The induced e.m.f. is:",
     ["10 V", "1 V", "100 V", "0.1 V"], 0,
     "E = N × (dΦ/dt) = 200 × 0.05 = 10 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 200$, $\frac{d\Phi}{dt} = 0.05\ T\cdot m^2/s$.
Governing law:
$$E = N\frac{d\Phi}{dt}$$

### Step 2: Full Mathematical Workings
$$E = 200 \times 0.05$$
$$200 \times 0.05 = 200 \times \frac{5}{100}$$
$$200 \times \frac{5}{100} = \frac{1000}{100}$$
$$E = 10\ V$$

### Step 3: Verification & Physical Interpretation
Two hundred turns times five hundredths of a tesla per second gives exactly 10 V — a clean one-step application of Faraday's second law.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (1 V)**: the student misplaces the decimal (rate read as 0.005).
- **Option C trap (100 V)**: the student reads the rate as 0.5 T/s.
- **Option D trap (0.1 V)**: the student divides 0.05 by 200 instead of multiplying.
r""")

calc(T, "A rectangular coil of 30 turns, each of area 0.05 m², sits in a field of 0.4 T. The coil is rotated from a position parallel to the field to perpendicular in 0.1 s. The average induced e.m.f. is:",
     ["6 V", "0.6 V", "60 V", "3 V"], 0,
     "Flux goes from 0 (parallel) to BA = 0.4 × 0.05 = 0.02 Wb (perpendicular); E = 30 × (0.02/0.1) = 6 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $N = 30$, $A = 0.05\ m^2$, $B = 0.4\ T$, $\Delta t = 0.1\ s$. Starting parallel to the field means $\Phi_i = 0$; ending perpendicular means $\Phi_f = BA$.
Governing laws:
$$\Phi = BA \qquad E = N\frac{\Delta\Phi}{\Delta t}$$

### Step 2: Full Mathematical Workings
Step A — final flux (perpendicular position):
$$\Phi_f = BA$$
$$\Phi_f = 0.4 \times 0.05$$
$$\Phi_f = 0.02\ Wb$$
Step B — flux change:
$$\Delta\Phi = 0.02 - 0 = 0.02\ Wb$$
Step C — induced e.m.f.:
$$E = 30 \times \frac{0.02}{0.1}$$
$$\frac{0.02}{0.1} = 0.2\ Wb/s$$
$$E = 30 \times 0.2$$
$$E = 6\ V$$

### Step 3: Verification & Physical Interpretation
This is Unsolved Question 3 of the notes, now solved. Rotating from parallel (no linkage) to perpendicular (full linkage $BA$) changes the flux by 0.02 Wb per turn; across 30 turns in 0.1 s this averages 6 V.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0.6 V)**: the student drops a factor of ten in the rate (0.02 Wb/s).
- **Option C trap (60 V)**: the student uses Δt = 0.01 s, multiplying by ten.
- **Option D trap (3 V)**: the student halves the turns (uses N = 15).
r""")

theory(T, "Faraday's FIRST law of electromagnetic induction states that:",
       ["an e.m.f. is induced in a conductor whenever it is placed in a changing magnetic field, and a current flows if the circuit is closed",
        "the induced e.m.f. equals the rate of change of flux linkage",
        "the induced effect always opposes the change producing it",
        "a current-carrying conductor experiences a force in a magnetic field"], 0,
       "First law: changing field → induced e.m.f.; closed circuit → induced current.",
       r"""### Step 1: Core Principle
Faraday's first law: whenever a conductor is placed in a changing magnetic field, an electromotive force is induced in the conductor. If the conductor forms a closed circuit, an induced current will also flow through it.

### Step 2: Testing the Options
- **Option A (correct)**: the exact statement of the first law.
- **Option B (wrong)**: that is Faraday's SECOND law (the quantitative rate-of-change statement).
- **Option C (wrong)**: that is Lenz's law (the direction rule).
- **Option D (wrong)**: that is the motor effect (force on a current-carrying conductor), a different phenomenon.

### Step 3: Exam Trap Summary
The trap is interchanging the three induction laws. Anchor: 1st law = WHEN induction happens (changing field, closed circuit), 2nd law = HOW MUCH (E = N dΦ/dt), Lenz = WHICH WAY (opposes).
r

**Key relation (the quantitative second law):** $E = N\,d\Phi/dt$.""")

theory(T, "Faraday's SECOND law states that the magnitude of the induced e.m.f. is:",
       ["equal to the rate of change of magnetic flux linked with the conductor",
        "equal to the magnetic flux itself",
        "inversely proportional to the number of turns",
        "independent of the rate of flux change"], 0,
       "Second law: E = N × (dΦ/dt) — e.m.f. equals the rate of change of flux linkage.",
       r"""### Step 1: Core Principle
Faraday's second law: the magnitude of the induced e.m.f. in a conductor is equal to the rate of change of magnetic flux linked with the conductor. With N turns, $E = N\frac{d\Phi}{dt}$.

### Step 2: Testing the Options
- **Option A (correct)**: the rate-of-change statement.
- **Option B (wrong)**: a steady flux induces nothing — induction needs CHANGE.
- **Option C (wrong)**: e.m.f. is DIRECTLY proportional to N (more turns, more voltage).
- **Option D (wrong)**: the rate of change is the very quantity the e.m.f. equals.

### Step 3: Exam Trap Summary
The trap is thinking "flux present = e.m.f. present". Only a CHANGING flux induces. Remember: static flux, zero e.m.f.; fast-changing flux, large e.m.f.
r""")

theory(T, "Eddy currents (also called Foucault currents) are:",
       ["loops of current induced in a conductor by a changing magnetic field, which create a field opposing the change (Lenz's law)",
        "the main working currents of a transformer's windings",
        "currents that flow only in superconductors",
        "currents produced directly by batteries"], 0,
       "Eddy currents are induced loops in bulk conductors; they oppose the changing field per Lenz's law.",
       r"""### Step 1: Core Principle
Eddy currents are loops of electric current induced in a conductor when it is placed in a changing magnetic field. They create a magnetic field that opposes the change in the original field, in accordance with Lenz's law. They are also called Foucault currents, and they appear in transformers, AC generators and magnetic flow meters.

### Step 2: Testing the Options
- **Option A (correct)**: the full definition, including the Lenz-law opposition.
- **Option B (wrong)**: the working currents are the designed winding currents, not the parasitic eddy loops.
- **Option C (wrong)**: eddy currents arise in ordinary conductors; they are not a superconductor phenomenon.
- **Option D (wrong)**: batteries are a chemical e.m.f. source, unrelated to induced loops.

### Step 3: Exam Trap Summary
The trap is conflating eddy currents with the useful winding currents. Eddy currents are the PARASITIC loops in the bulk metal — they waste power as heat unless laminated cores suppress them.
r

**Key relation:** the e.m.f. that drives the eddy loops is $E = N\,d\Phi/dt$.""")

# =====================================================================
# TOPIC 3 — AC WAVEFORMS & PHASORS
# =====================================================================
T = "eee-ac-phasors"

theory(T, "Direct current (DC) is described as:",
       ["a uni-directional supply whose value does not change with time",
        "a bi-directional supply that varies in magnitude and direction",
        "a supply that reverses polarity every half cycle",
        "a time-varying sinusoidal supply"], 0,
       "DC flows in one direction only with a fixed magnitude — it does not change with time.",
       r"""### Step 1: Core Principle
DC is a form of electrical current or voltage that flows around a circuit in one direction only — a "uni-directional" supply. It has a fixed magnitude (amplitude) and a definite direction (e.g. +12 V). DC power supplies do not change their value with respect to time; a constant uni-directional supply never changes or becomes negative unless its connections are physically reversed. Sources: power supplies, batteries, dynamos, solar cells.

### Step 2: Testing the Options
- **Option A (correct)**: the notes' exact description.
- **Option B (wrong)**: that is the description of AC.
- **Option C (wrong)**: polarity reversal every half cycle is AC behaviour.
- **Option D (wrong)**: a sinusoid is AC, not DC.

### Step 3: Exam Trap Summary
The trap is swapping the DC and AC definitions. Anchor: DC = constant + one direction; AC = time-varying + two directions.
r

**Key contrast:** DC is constant, while AC follows $A(t) = A_m\sin(2\pi ft)$.""")

theory(T, "An alternating (AC) waveform is defined as one that:",
       ["varies in both magnitude and direction in an even manner with respect to time",
        "flows in one direction only",
        "never changes polarity",
        "has a fixed magnitude at all times"], 0,
       "AC varies in both magnitude and direction with time — a 'bi-directional' waveform.",
       r"""### Step 1: Core Principle
An alternating function or AC waveform varies in both magnitude and direction in more or less an even manner with respect to time, making it a "bi-directional" waveform. The most common AC form is the sinusoidal waveform (sine wave), the domestic mains being the standard example.

### Step 2: Testing the Options
- **Option A (correct)**: magnitude AND direction vary — the defining feature of AC.
- **Option B (wrong)**: one-direction flow is DC.
- **Option C (wrong)**: AC reverses polarity every half cycle.
- **Option D (wrong)**: a fixed magnitude is DC behaviour.

### Step 3: Exam Trap Summary
Same trap, reversed — watch for "magnitude and direction" in the AC definition and "one direction only" for DC.
r

**Key form:** the sinusoid is $A(t) = A_m\sin(2\pi ft)$.""")

theory(T, "The general expression of a sinusoidal AC quantity is:",
       ["A(t) = Aₘ sin(2πft)", "A(t) = Aₘ e⁻ᵗ", "A(t) = Aₘ/t", "A(t) = Aₘ sin(t)/(2πf)"], 0,
       "A sinusoid is A(t) = Aₘ sin(2πft), where Aₘ is the amplitude and f the frequency.",
       r"""### Step 1: Core Principle
An AC function generally follows the mathematical sinusoid defined as:
$$A(t) = A_m\sin(2\pi ft)$$
where $A_m$ is the amplitude and $f$ the frequency.

### Step 2: Testing the Options
- **Option A (correct)**: the standard sinusoid.
- **Option B (wrong)**: an exponential decay — a transient, not a periodic waveform.
- **Option C (wrong)**: a hyperbolic decay — not periodic.
- **Option D (wrong)**: dividing by $2\pi f$ inside the argument is dimensionally wrong and not the sinusoid.

### Step 3: Exam Trap Summary
The trap is scrambling the argument $2\pi ft$. Anchor: the argument must be dimensionless — $2\pi$ times frequency times time.
r""")

theory(T, "The Period (T) of an AC waveform is:",
       ["the time in seconds the waveform takes to repeat itself from start to finish",
        "the number of times the waveform repeats in one second",
        "the peak amplitude of the waveform",
        "half the frequency"], 0,
       "Period T is the time for one complete cycle (seconds); frequency f = 1/T.",
       r"""### Step 1: Core Principle
The period T is the length of time in seconds that the waveform takes to repeat itself from start to finish — also called the periodic time for sine waves or the pulse width for square waves.

### Step 2: Testing the Options
- **Option A (correct)**: time per cycle.
- **Option B (wrong)**: cycles per second is the FREQUENCY, the reciprocal quantity.
- **Option C (wrong)**: the peak value is the amplitude, unrelated to timing.
- **Option D (wrong)**: T is the reciprocal of f, not half of it.

### Step 3: Exam Trap Summary
The classic trap: period vs frequency inversion. Anchor: period is in SECONDS, frequency in HERTZ — and they are reciprocals ($f = 1/T$).
r""")

theory(T, "The frequency (f) of a waveform is:",
       ["the number of times the waveform repeats itself within one second, and is the reciprocal of the period (f = 1/T)",
        "the time taken for one full cycle",
        "the amplitude divided by the period",
        "the peak-to-peak voltage"], 0,
       "Frequency = cycles per second, f = 1/T, unit hertz (Hz).",
       r"""### Step 1: Core Principle
Frequency f is the number of times the waveform repeats itself within a one-second time period. Frequency is the reciprocal of the time period, $f = 1/T$, with the unit hertz (Hz).

### Step 2: Testing the Options
- **Option A (correct)**: the exact definition with the reciprocal relation.
- **Option B (wrong)**: time per cycle is the period T.
- **Option C (wrong)**: amplitude/period is a meaningless ratio, not frequency.
- **Option D (wrong)**: peak-to-peak is a voltage measurement.

### Step 3: Exam Trap Summary
Period/frequency inversion again — in "one second, how many cycles?" think of 50 Hz mains = 50 cycles per second, so each cycle lasts 1/50 s = 20 ms.
r""")

theory(T, "The Amplitude (A) of an AC waveform is:",
       ["the magnitude or intensity of the signal, measured in volts or amps",
        "the time taken for one complete cycle",
        "the number of cycles per second",
        "the zero line of the waveform"], 0,
       "Amplitude is the magnitude/intensity of the waveform (its peak value).",
       r"""### Step 1: Core Principle
The amplitude A is the magnitude or intensity of the signal waveform, measured in volts or amps — the peak value measured from the zero line. Parts of the waveform above the zero axis represent flow in one direction; parts below represent flow in the opposite direction.

### Step 2: Testing the Options
- **Option A (correct)**: magnitude/intensity in volts or amps.
- **Option B (wrong)**: that is the period T.
- **Option C (wrong)**: that is the frequency f.
- **Option D (wrong)**: the zero line is the reference axis, not the amplitude.

### Step 3: Exam Trap Summary
The trap is mixing the three waveform characteristics (period, frequency, amplitude). Anchor: amplitude = "how big" (V or A), period = "how long" (s), frequency = "how often" (Hz).
r

**Key relation:** amplitude ties to the other values via $V_{rms} = 0.707 V_m$ and $V_{avg} = 0.637 V_m$.""")

theory(T, "The phasor method of analysing AC networks was made famous by:",
       ["Charles P. Steinmetz (General Electric, 1893)",
        "Thomas Edison",
        "Nikola Tesla",
        "James Clerk Maxwell"], 0,
       "Steinmetz — acquired by GE in 1893 — formalised the symbolic (phasor) method.",
       r"""### Step 1: Core Principle
When General Electric acquired a small firm in 1893, it gained the services of Charles P. Steinmetz. Steinmetz had completed his doctoral dissertation in mathematics at the University of Breslau and became famous for his symbolic method of analysing AC networks — the phasor transform.

### Step 2: Testing the Options
- **Option A (correct)**: Steinmetz, GE, 1893.
- **Option B (wrong)**: Edison championed the DC system, not the phasor method.
- **Option C (wrong)**: Tesla contributed to AC systems broadly, but the phasor formalisation is credited to Steinmetz.
- **Option D (wrong)**: Maxwell formulated electromagnetism, predating AC network phasors.

### Step 3: Exam Trap Summary
The trap is attributing AC mathematics to the famous names (Edison/Tesla/Maxwell). Anchor the fact: Steinmetz = phasor method, GE 1893.
r

**Key recall:** a phasor rotates at the angular frequency $\omega = 2\pi f$.""")

theory(T, "A phasor is best described as:",
       ["a rotating vector that represents the magnitude and phase of a sinusoidal quantity",
        "a scalar that represents only the amplitude",
        "a constant equal to the r.m.s. value",
        "a unit vector fixed along the x-axis"], 0,
       "A phasor is a rotating vector: its length gives magnitude, its angle gives phase.",
       r"""### Step 1: Core Principle
A phasor is a rotating vector representation of a sinusoidal quantity: the LENGTH of the vector represents the magnitude, and the ANGLE represents the phase. Because sinusoids of the same frequency add like vectors, phasors allow AC quantities to be combined without trigonometry.

### Step 2: Testing the Options
- **Option A (correct)**: magnitude + phase in one rotating vector.
- **Option B (wrong)**: amplitude alone loses the phase information — a phasor carries both.
- **Option C (wrong)**: a phasor is not a constant; it rotates at the angular frequency ω.
- **Option D (wrong)**: a fixed unit vector carries neither magnitude nor phase.

### Step 3: Exam Trap Summary
The trap is treating the phasor as a plain number. Remember: magnitude = length, phase = angle, rotation = frequency.
r

**Key relation:** the phasor angle advances at $\omega = 2\pi f$ each second.""")

theory(T, "Which statement about alternating quantities is correct?",
       ["They cannot be stored in batteries or cells like DC; they are generated by alternators or waveform generators when needed",
        "They are stored in batteries just like DC",
        "They are cheaper to store than to generate",
        "They always have zero frequency"], 0,
       "AC cannot be stored in cells; it is generated on demand by alternators.",
       r"""### Step 1: Core Principle
Alternating voltages and currents cannot be stored in batteries or cells like direct current can. It is much easier and cheaper to generate these quantities using alternators or waveform generators when they are needed.

### Step 2: Testing the Options
- **Option A (correct)**: the notes' exact statement.
- **Option B (wrong)**: batteries store DC only.
- **Option C (wrong)**: storage is impossible for AC, so "cheaper to store" is meaningless.
- **Option D (wrong)**: AC has a definite frequency (e.g. 50 Hz).

### Step 3: Exam Trap Summary
The trap is assuming batteries work for AC. Anchor: batteries = DC storage; AC = generate-on-demand.
r

**Key recall:** generation replaces storage; the angular frequency is $\omega = 2\pi f$.""")

theory(T, "In an AC circuit, the r.m.s. (effective) value of a current is:",
       ["the value of DC that would produce the same heating effect in the same resistance",
        "the peak value divided by π",
        "the average value over a full cycle",
        "always larger than the peak value"], 0,
       "r.m.s. = the DC equivalent that produces the same heating effect; for a sine wave V_rms = 0.707 Vₘ.",
       r"""### Step 1: Core Principle
The r.m.s. (root-mean-square) value of an alternating current is the value of direct current that would produce the same heating effect in the same resistance. For a sinusoid, $V_{rms} = \frac{V_m}{\sqrt{2}} = 0.707V_m$.

### Step 2: Testing the Options
- **Option A (correct)**: the heating-equivalence definition.
- **Option B (wrong)**: the half-cycle average uses 0.637; the peak/π is not a standard value.
- **Option C (wrong)**: the average over a FULL cycle of a sinusoid is ZERO.
- **Option D (wrong)**: r.m.s. is always SMALLER than the peak (0.707 of it).

### Step 3: Exam Trap Summary
Two traps: average vs r.m.s. (0.637 vs 0.707) and peak vs r.m.s. ordering. Anchor: r.m.s. < peak always; full-cycle average = 0.
r""")

calc(T, "A sinusoidal voltage has a period of 20 ms. Its frequency is:",
     ["50 Hz", "20 Hz", "500 Hz", "0.05 Hz"], 0,
     "f = 1/T = 1/(20 × 10⁻³) = 50 Hz.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: period $T = 20\ ms = 20 \times 10^{-3}\ s = 0.02\ s$.
Governing law:
$$f = \frac{1}{T}$$

### Step 2: Full Mathematical Workings
$$f = \frac{1}{0.02}$$
$$f = \frac{1}{2 \times 10^{-2}}$$
$$f = \frac{1}{2} \times 10^{2}$$
$$f = 0.5 \times 100$$
$$f = 50\ Hz$$

### Step 3: Verification & Physical Interpretation
Fifty hertz is the standard domestic mains frequency — a 20 ms period is exactly the mains cycle time, confirming the computation.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (20 Hz)**: the student reads the 20 ms as 20 Hz, ignoring the reciprocal.
- **Option C trap (500 Hz)**: the student treats 20 ms as 2 ms (10× slip).
- **Option D trap (0.05 Hz)**: the student inverts the conversion the wrong way, effectively computing T/1000.
r""")

calc(T, "A sine wave has a frequency of 1 kHz. Its period is:",
     ["1 ms", "1 s", "0.1 ms", "10 ms"], 0,
     "T = 1/f = 1/1000 = 0.001 s = 1 ms.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $f = 1\ kHz = 1000\ Hz$.
Governing law:
$$T = \frac{1}{f}$$

### Step 2: Full Mathematical Workings
$$T = \frac{1}{1000}$$
$$T = 0.001\ s$$
Convert to milliseconds:
$$0.001\ s = 1\ ms$$

### Step 3: Verification & Physical Interpretation
A kilohertz waveform completes one cycle each millisecond — the reciprocal relationship holds exactly.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (1 s)**: the student drops the milli- prefix (treats f as 1 Hz).
- **Option C trap (0.1 ms)**: the student multiplies by 1000 the wrong way.
- **Option D trap (10 ms)**: the student treats f as 100 Hz instead of 1000 Hz.
r""")

calc(T, "A waveform has a period of 2 ms. Its frequency is:",
     ["500 Hz", "200 Hz", "50 Hz", "2 kHz"], 0,
     "f = 1/T = 1/(2 × 10⁻³) = 500 Hz.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $T = 2\ ms = 2 \times 10^{-3}\ s$.
Governing law:
$$f = \frac{1}{T}$$

### Step 2: Full Mathematical Workings
$$f = \frac{1}{2 \times 10^{-3}}$$
$$f = \frac{1}{2} \times 10^{3}$$
$$f = 0.5 \times 1000$$
$$f = 500\ Hz$$

### Step 3: Verification & Physical Interpretation
Two milliseconds per cycle means five hundred cycles per second. The reciprocal relation is exact.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (200 Hz)**: the student uses $f = T \times 100$, a units scramble.
- **Option C trap (50 Hz)**: the student confuses 2 ms with the mains 20 ms period.
- **Option D trap (2 kHz)**: the student multiplies 2 by 1000 instead of dividing.
r""")

calc(T, "A 50 Hz supply has an angular frequency ω of: (take π = 3.14)",
     ["314 rad/s", "157 rad/s", "628 rad/s", "31.4 rad/s"], 0,
     "ω = 2πf = 2 × 3.14 × 50 = 314 rad/s.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $f = 50\ Hz$, $\pi = 3.14$.
Governing law:
$$\omega = 2\pi f$$

### Step 2: Full Mathematical Workings
$$\omega = 2 \times 3.14 \times 50$$
$$2 \times 3.14 = 6.28$$
$$6.28 \times 50 = 314$$
$$\omega = 314\ rad/s$$

### Step 3: Verification & Physical Interpretation
314 rad/s is the standard mains angular frequency — every second the phasor sweeps through $2\pi \times 50$ radians.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (157 rad/s)**: the student uses $\omega = \pi f$ (forgets the factor 2).
- **Option C trap (628 rad/s)**: the student uses $\omega = 4\pi f$.
- **Option D trap (31.4 rad/s)**: the student divides by 10 — a decimal slip.
r""")

calc(T, "A mains voltage has a peak value Vₘ = 311 V. Its r.m.s. value is about:",
     ["220 V", "311 V", "440 V", "156 V"], 0,
     "V_rms = Vₘ/√2 = 0.707 × 311 = 220 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: peak $V_m = 311\ V$.
Governing law:
$$V_{rms} = \frac{V_m}{\sqrt{2}} = 0.707 V_m$$

### Step 2: Full Mathematical Workings
$$V_{rms} = 0.707 \times 311$$
$$V_{rms} = 219.9\ V$$
$$V_{rms} \approx 220\ V$$

### Step 3: Verification & Physical Interpretation
311 V peak corresponds to the familiar 220 V (≈230 V) mains — the r.m.s. value is what voltmeters read and what "mains voltage" means in practice.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (311 V)**: the student reports the peak value without converting.
- **Option C trap (440 V)**: the student uses $\sqrt{2} \times V_m$ instead of dividing.
- **Option D trap (156 V)**: the student halves the peak (uses 0.5 instead of 0.707).
r""")

calc(T, "A supply is specified as 230 V r.m.s. Its peak value is about:",
     ["325 V", "163 V", "230 V", "460 V"], 0,
     "Vₘ = √2 × V_rms = 1.414 × 230 = 325 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $V_{rms} = 230\ V$.
Governing law (rearranged):
$$V_m = \sqrt{2}\ V_{rms} = 1.414 \times V_{rms}$$

### Step 2: Full Mathematical Workings
$$V_m = 1.414 \times 230$$
$$1.414 \times 230 = 325.2$$
$$V_m = 325\ V$$

### Step 3: Verification & Physical Interpretation
The 230 V r.m.s. supply peaks at about 325 V twice per cycle — matching the earlier example (311 V peak for 220 V r.m.s.).

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (163 V)**: the student divides by √2 instead of multiplying.
- **Option C trap (230 V)**: the student assumes r.m.s. equals peak.
- **Option D trap (460 V)**: the student doubles the r.m.s. value.
r""")

calc(T, "A sine wave has a peak value of 100 V. Its average value over a half cycle is about:",
     ["63.7 V", "70.7 V", "100 V", "50 V"], 0,
     "V_avg = 0.637 × Vₘ = 0.637 × 100 = 63.7 V.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: peak $V_m = 100\ V$.
Governing law — half-cycle average of a sinusoid:
$$V_{avg} = 0.637 \times V_m$$

### Step 2: Full Mathematical Workings
$$V_{avg} = 0.637 \times 100$$
$$V_{avg} = 63.7\ V$$

### Step 3: Verification & Physical Interpretation
Over half a cycle the sine wave averages 63.7% of its peak. (The average over a FULL cycle is zero, which is why the half-cycle average is the quoted figure.)

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (70.7 V)**: the student uses the r.m.s. factor 0.707 — the classic average/r.m.s. confusion.
- **Option C trap (100 V)**: the student reports the peak unchanged.
- **Option D trap (50 V)**: the student guesses half the peak.
r""")

calc(T, "A mains sine wave has Vₘ = 311 V. Its average value over a half cycle is about:",
     ["198 V", "220 V", "311 V", "440 V"], 0,
     "V_avg = 0.637 × 311 = 198 V (while V_rms = 0.707 × 311 = 220 V).",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $V_m = 311\ V$.
Governing law:
$$V_{avg} = 0.637 \times V_m$$

### Step 2: Full Mathematical Workings
$$V_{avg} = 0.637 \times 311$$
$$V_{avg} = 198.1\ V$$
$$V_{avg} \approx 198\ V$$

### Step 3: Verification & Physical Interpretation
The same 311 V mains peaks average to 198 V over a half cycle, while its r.m.s. is 220 V — the two factors (0.637 and 0.707) must never be swapped.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (220 V)**: the student computes the r.m.s. value instead — the most common slip.
- **Option C trap (311 V)**: the student reports the peak.
- **Option D trap (440 V)**: the student doubles the r.m.s. value.
r""")

calc(T, "An inductor L = 0.1 H is connected across a 50 Hz supply. Its inductive reactance is: (take π = 3.14)",
     ["31.4 Ω", "3.14 Ω", "62.8 Ω", "314 Ω"], 0,
     "X_L = 2πfL = 2 × 3.14 × 50 × 0.1 = 31.4 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 0.1\ H$, $f = 50\ Hz$, $\pi = 3.14$.
Governing law:
$$X_L = 2\pi f L$$

### Step 2: Full Mathematical Workings
$$X_L = 2 \times 3.14 \times 50 \times 0.1$$
$$2 \times 3.14 = 6.28$$
$$6.28 \times 50 = 314$$
$$314 \times 0.1 = 31.4$$
$$X_L = 31.4\ \Omega$$

### Step 3: Verification & Physical Interpretation
A 0.1 H coil at 50 Hz opposes AC with 31.4 Ω of reactance. Note the intermediate step: without the inductance factor the product is 314 — keeping L in the multiplication is essential.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (3.14 Ω)**: the student drops the factor 2 and the frequency (π × L only).
- **Option C trap (62.8 Ω)**: the student doubles L (0.2 H) — or the frequency.
- **Option D trap (314 Ω)**: the student forgets to multiply by L = 0.1, stopping at $2\pi f$.
r""")

calc(T, "An inductor L = 0.2 H is connected across a 50 Hz supply. Its inductive reactance is:",
     ["62.8 Ω", "31.4 Ω", "6.28 Ω", "125.6 Ω"], 0,
     "X_L = 2πfL = 2 × 3.14 × 50 × 0.2 = 62.8 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 0.2\ H$, $f = 50\ Hz$.
Governing law:
$$X_L = 2\pi f L$$

### Step 2: Full Mathematical Workings
$$X_L = 2 \times 3.14 \times 50 \times 0.2$$
$$2 \times 3.14 = 6.28$$
$$6.28 \times 50 = 314$$
$$314 \times 0.2 = 62.8$$
$$X_L = 62.8\ \Omega$$

### Step 3: Verification & Physical Interpretation
Doubling the inductance from 0.1 H to 0.2 H doubles the reactance from 31.4 Ω to 62.8 Ω — reactance scales linearly with L (and with f).

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (31.4 Ω)**: the student reuses the 0.1 H answer — reactance must be recomputed for the new inductance.
- **Option C trap (6.28 Ω)**: the student drops the frequency factor.
- **Option D trap (125.6 Ω)**: the student doubles the frequency as well as the inductance.
r""")

calc(T, "A capacitor C = 100 µF is connected across a 50 Hz supply. Its capacitive reactance is about:",
     ["31.8 Ω", "318 Ω", "3.18 Ω", "15.9 Ω"], 0,
     "X_C = 1/(2πfC) = 1/(2 × 3.14 × 50 × 100 × 10⁻⁶) = 31.8 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $C = 100\ \mu F = 100 \times 10^{-6}\ F$, $f = 50\ Hz$.
Governing law:
$$X_C = \frac{1}{2\pi f C}$$

### Step 2: Full Mathematical Workings
Compute the denominator:
$$2\pi f C = 2 \times 3.14 \times 50 \times 100 \times 10^{-6}$$
$$2 \times 3.14 = 6.28$$
$$6.28 \times 50 = 314$$
$$314 \times 100 \times 10^{-6} = 0.0314$$
$$X_C = \frac{1}{0.0314}$$
$$X_C = 31.85\ \Omega$$
$$X_C \approx 31.8\ \Omega$$

### Step 3: Verification & Physical Interpretation
At 50 Hz a 100 µF capacitor offers about 32 Ω of opposition. Note that capacitive reactance DECREASES as C or f increases — the inverse of inductive behaviour.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (318 Ω)**: the student treats C as 10 µF — one order of magnitude off.
- **Option C trap (3.18 Ω)**: the student treats C as 1 mF (1000 µF).
- **Option D trap (15.9 Ω)**: the student doubles the denominator, e.g. by using f = 100 Hz.
r""")

calc(T, "A capacitor C = 10 µF is connected across a 50 Hz supply. Its capacitive reactance is about:",
     ["318 Ω", "31.8 Ω", "3180 Ω", "159 Ω"], 0,
     "X_C = 1/(2πfC) = 1/(2 × 3.14 × 50 × 10 × 10⁻⁶) = 318 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $C = 10\ \mu F = 10 \times 10^{-6}\ F$, $f = 50\ Hz$.
Governing law:
$$X_C = \frac{1}{2\pi f C}$$

### Step 2: Full Mathematical Workings
$$2\pi f C = 2 \times 3.14 \times 50 \times 10 \times 10^{-6}$$
$$2 \times 3.14 = 6.28$$
$$6.28 \times 50 = 314$$
$$314 \times 10 \times 10^{-6} = 0.00314$$
$$X_C = \frac{1}{0.00314}$$
$$X_C = 318.5\ \Omega$$
$$X_C \approx 318\ \Omega$$

### Step 3: Verification & Physical Interpretation
Reducing the capacitance tenfold (100 µF → 10 µF) increases the reactance tenfold (31.8 Ω → 318 Ω) — the inverse relationship at work.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (31.8 Ω)**: the student reuses the 100 µF answer.
- **Option C trap (3180 Ω)**: the student treats C as 1 µF.
- **Option D trap (159 Ω)**: the student halves the answer (e.g. f = 100 Hz).
r""")

calc(T, "A series circuit has R = 3 Ω and inductive reactance X_L = 4 Ω. The magnitude of its impedance is:",
     ["5 Ω", "7 Ω", "1 Ω", "12 Ω"], 0,
     "|Z| = √(R² + X²) = √(3² + 4²) = √25 = 5 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $R = 3\ \Omega$, $X_L = 4\ \Omega$.
Governing law — impedance magnitude of an R-L series circuit:
$$Z = R + jX_L \qquad |Z| = \sqrt{R^2 + X_L^2}$$

### Step 2: Full Mathematical Workings
$$|Z| = \sqrt{3^2 + 4^2}$$
$$3^2 = 9$$
$$4^2 = 16$$
$$|Z| = \sqrt{9 + 16}$$
$$|Z| = \sqrt{25}$$
$$|Z| = 5\ \Omega$$

### Step 3: Verification & Physical Interpretation
The 3–4–5 triangle: resistance and reactance combine in quadrature (at right angles in the impedance triangle), so the impedance is 5 Ω — never 7 Ω.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (7 Ω)**: the student adds R + X directly — the most common impedance error.
- **Option C trap (1 Ω)**: the student subtracts X from R.
- **Option D trap (12 Ω)**: the student multiplies R × X.
r""")

calc(T, "A series circuit has R = 30 Ω and capacitive reactance X_C = 40 Ω. Its impedance magnitude is:",
     ["50 Ω", "70 Ω", "10 Ω", "35 Ω"], 0,
     "|Z| = √(R² + X_C²) = √(30² + 40²) = √2500 = 50 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $R = 30\ \Omega$, $X_C = 40\ \Omega$.
Governing law — impedance magnitude of an R-C series circuit:
$$Z = R - jX_C \qquad |Z| = \sqrt{R^2 + X_C^2}$$

### Step 2: Full Mathematical Workings
$$|Z| = \sqrt{30^2 + 40^2}$$
$$30^2 = 900$$
$$40^2 = 1600$$
$$|Z| = \sqrt{900 + 1600}$$
$$|Z| = \sqrt{2500}$$
$$|Z| = 50\ \Omega$$

### Step 3: Verification & Physical Interpretation
The 30–40–50 triangle again: the magnitude is always the square root of the sum of squares, regardless of whether the reactance is inductive or capacitive (the sign of j only affects the phase angle).

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (70 Ω)**: direct addition of R and X.
- **Option C trap (10 Ω)**: subtraction of X from R.
- **Option D trap (35 Ω)**: taking the simple average of R and X.
r""")

calc(T, "A series circuit has R = 8 Ω and X_C = 6 Ω. The magnitude of its impedance is:",
     ["10 Ω", "14 Ω", "2 Ω", "48 Ω"], 0,
     "|Z| = √(8² + 6²) = √(64 + 36) = √100 = 10 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $R = 8\ \Omega$, $X_C = 6\ \Omega$.
Governing law:
$$|Z| = \sqrt{R^2 + X_C^2}$$

### Step 2: Full Mathematical Workings
$$|Z| = \sqrt{8^2 + 6^2}$$
$$8^2 = 64$$
$$6^2 = 36$$
$$|Z| = \sqrt{64 + 36}$$
$$|Z| = \sqrt{100}$$
$$|Z| = 10\ \Omega$$

### Step 3: Verification & Physical Interpretation
The 6–8–10 triangle completes the set of Pythagorean impedances. Quadrature addition always gives less than the straight sum.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (14 Ω)**: direct addition.
- **Option C trap (2 Ω)**: subtraction.
- **Option D trap (48 Ω)**: multiplication of R and X.
r""")

calc(T, "A circuit has R = 6 Ω in series with X_L = 8 Ω. The magnitude of the equivalent impedance is:",
     ["10 Ω", "14 Ω", "2 Ω", "48 Ω"], 0,
     "|Z| = √(6² + 8²) = √(36 + 64) = 10 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $R = 6\ \Omega$, $X_L = 8\ \Omega$.
Governing law:
$$|Z| = \sqrt{R^2 + X_L^2}$$

### Step 2: Full Mathematical Workings
$$|Z| = \sqrt{6^2 + 8^2}$$
$$6^2 = 36$$
$$8^2 = 64$$
$$|Z| = \sqrt{36 + 64}$$
$$|Z| = \sqrt{100}$$
$$|Z| = 10\ \Omega$$

### Step 3: Verification & Physical Interpretation
Same 6–8–10 pattern as the previous question — practice both orders; the magnitude is identical for inductive and capacitive cases.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (14 Ω)**: direct addition.
- **Option C trap (2 Ω)**: subtraction.
- **Option D trap (48 Ω)**: multiplication.
r""")

# --- multi-part theoretical question (Topic 3) ---
theory(T, "For a 220 V, 50 Hz AC mains supply, which set gives the correct (a) peak voltage, (b) angular frequency and (c) period?",
       ["311 V, 314 rad/s, 20 ms",
        "311 V, 157 rad/s, 20 ms",
        "220 V, 314 rad/s, 50 ms",
        "156 V, 314 rad/s, 20 ms"], 0,
       "Vₘ = 1.414 × 220 = 311 V; ω = 2π × 50 = 314 rad/s; T = 1/50 = 20 ms.",
       r"""### Step 1: Core Principle
The three conversions:
(a) peak voltage $V_m = \sqrt{2}\ V_{rms} = 1.414 \times 220 = 311\ V$
(b) angular frequency $\omega = 2\pi f = 2 \times 3.14 \times 50 = 314\ rad/s$
(c) period $T = \frac{1}{f} = \frac{1}{50} = 0.02\ s = 20\ ms$

### Step 2: Testing the Options
- **Option A (correct)**: all three values match.
- **Option B (wrong)**: part (b) uses $\omega = \pi f$ (157 rad/s) — the factor 2 is missing.
- **Option C (wrong)**: part (a) reports the r.m.s. value as the peak, and part (c) uses T = 1/f incorrectly (50 ms instead of 20 ms).
- **Option D (wrong)**: part (a) divides the peak by 2 (156 V) instead of multiplying the r.m.s. by √2.

### Step 3: Exam Trap Summary
The traps are the factor-2 slip in ω, the r.m.s./peak confusion, and the period computation. In the written exam, show all three conversions as separate lines so each part earns its own mark.
r""")

# =====================================================================
# TOPIC 4 — RESONANCE IN AC CIRCUITS
# =====================================================================
T = "eee-resonance"

theory(T, "Series resonance occurs in an R-L-C series circuit when:",
       ["X_L = X_C", "R = X_L", "R = X_C", "the supply voltage is zero"], 0,
       "At series resonance the inductive and capacitive reactances cancel: X_L = X_C.",
       r"""### Step 1: Core Principle
Series resonance occurs when the inductive reactance equals the capacitive reactance: $X_L = X_C$. The two equal-and-opposite reactances cancel, leaving $Z = R$ — minimum impedance and maximum current.

### Step 2: Testing the Options
- **Option A (correct)**: the resonance condition.
- **Option B (wrong)**: R = X_L is a specific operating point, not the resonance condition.
- **Option C (wrong)**: R = X_C likewise has nothing to do with resonance.
- **Option D (wrong)**: resonance depends on the circuit's L and C, not on removing the supply.

### Step 3: Exam Trap Summary
The trap is inventing resistance-based "resonance conditions". Resonance is purely a reactance-balance phenomenon: $2\pi f L = 1/(2\pi f C)$.
r""")

theory(T, "At series resonance, the impedance of the R-L-C circuit is:",
       ["minimum and equal to R", "maximum and equal to X_L", "equal to X_C", "infinite"], 0,
       "X_L = X_C cancels, so Z = R — a minimum (purely resistive).",
       r"""### Step 1: Core Principle
The series impedance is $Z = R + j(X_L - X_C)$. At resonance $X_L = X_C$, so:
$$Z = R + j(0) = R$$
The impedance is a MINIMUM (equal to just the resistance), so the current is a maximum for a given supply voltage.

### Step 2: Testing the Options
- **Option A (correct)**: minimum impedance, equal to R.
- **Option B (wrong)**: maximum impedance describes PARALLEL resonance.
- **Option C (wrong)**: X_C is cancelled by X_L at resonance.
- **Option D (wrong)**: infinite impedance is the parallel-resonance idealisation.

### Step 3: Exam Trap Summary
The series/parallel duality is the favourite trap: series = minimum Z (maximum I); parallel = maximum Z (minimum I).
r""")

theory(T, "The resonant frequency of a series R-L-C circuit is given by:",
       ["f₀ = 1/(2π√(LC))", "f₀ = 2π√(LC)", "f₀ = 1/(2πLC)", "f₀ = √(LC)/(2π)"], 0,
       "Setting X_L = X_C and solving for f gives f₀ = 1/(2π√(LC)).",
       r"""### Step 1: Core Principle
At resonance $X_L = X_C$, that is:
$$2\pi f L = \frac{1}{2\pi f C}$$
Multiplying both sides by f and dividing by $2\pi L$:
$$f^2 = \frac{1}{(2\pi)^2 LC}$$
Taking the positive square root:
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

### Step 2: Testing the Options
- **Option A (correct)**: the derived expression.
- **Option B (wrong)**: the reciprocal — physically it grows with L and C, which is backwards.
- **Option C (wrong)**: the square root over LC is missing.
- **Option D (wrong)**: the numerator and denominator are inverted.

### Step 3: Exam Trap Summary
The traps are missing the square root and inverting the formula. In the written exam, ALWAYS show the derivation line $2\pi f L = 1/(2\pi f C)$ before quoting the result — it guards against inversion errors and earns method marks.
r""")

theory(T, "The quality factor (Q) of a resonant circuit measures:",
       ["the selectivity (sharpness) of the resonance", "the power dissipated in the resistor", "the number of components in the circuit", "the temperature rise of the coil"], 0,
       "Q measures how sharply the circuit resonates — high Q means a narrow bandwidth.",
       r"""### Step 1: Core Principle
The quality factor Q is a measure of the selectivity/sharpness of the resonance. A high Q means a sharp, selective resonance with a narrow bandwidth; a low Q means a broad, flat response.

### Step 2: Testing the Options
- **Option A (correct)**: sharpness/selectivity.
- **Option B (wrong)**: power dissipation is measured in watts, not by Q.
- **Option C (wrong)**: Q is a dimensionless ratio, not a component count.
- **Option D (wrong)**: temperature is an operating condition, unrelated to Q.

### Step 3: Exam Trap Summary
The trap is vague "quality" guesses. Anchor the operational meaning: high Q = sharp peak = narrow bandwidth = selective (like a radio tuner).
r

**Key relations:** $Q = X_L/R$ at resonance and bandwidth $= f_0/Q$.""")

calc(T, "A series circuit has L = 100 mH and C = 10 µF. Its resonant frequency is about: (take π = 3.14)",
     ["159 Hz", "15.9 Hz", "1590 Hz", "50 Hz"], 0,
     "LC = 0.1 × 10⁻⁵ = 10⁻⁶; √(LC) = 10⁻³; f₀ = 1/(2π × 10⁻³) = 159 Hz.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 100\ mH = 0.1\ H$, $C = 10\ \mu F = 10 \times 10^{-6}\ F$, $\pi = 3.14$.
Governing law:
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

### Step 2: Full Mathematical Workings
Step A — compute the LC product:
$$LC = 0.1 \times 10 \times 10^{-6}$$
$$LC = 1 \times 10^{-6}$$
Step B — take the square root:
$$\sqrt{LC} = \sqrt{1 \times 10^{-6}}$$
$$\sqrt{LC} = 1 \times 10^{-3}$$
Step C — take the reciprocal with the 2π factor:
$$f_0 = \frac{1}{2 \times 3.14 \times 1 \times 10^{-3}}$$
$$f_0 = \frac{1}{6.28 \times 10^{-3}}$$
$$f_0 = \frac{1000}{6.28}$$
$$f_0 = 159.2\ Hz$$
$$f_0 \approx 159\ Hz$$

### Step 3: Verification & Physical Interpretation
A 100 mH coil resonating with a 10 µF capacitor at 159 Hz — in the audio range, as expected for these component sizes. The three-line pattern (LC → √(LC) → reciprocal) earns full marks in the written exam.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (15.9 Hz)**: the student drops a factor of ten (uses L = 10 mH or C = 100 µF).
- **Option C trap (1590 Hz)**: the student gains a factor of ten (uses C = 1 µF).
- **Option D trap (50 Hz)**: the student confuses resonant frequency with the mains frequency.
r""")

calc(T, "A series circuit has L = 20 mH and C = 20 µF. Its resonant frequency is about:",
     ["252 Hz", "25.2 Hz", "2520 Hz", "126 Hz"], 0,
     "LC = 0.02 × 20 × 10⁻⁶ = 4 × 10⁻⁷; √(LC) = 6.32 × 10⁻⁴; f₀ = 1/(2π × 6.32 × 10⁻⁴) = 252 Hz.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 20\ mH = 0.02\ H$, $C = 20\ \mu F = 20 \times 10^{-6}\ F$.
Governing law:
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

### Step 2: Full Mathematical Workings
Step A — LC product:
$$LC = 0.02 \times 20 \times 10^{-6}$$
$$LC = 4 \times 10^{-7}$$
Step B — square root:
$$\sqrt{LC} = \sqrt{4 \times 10^{-7}}$$
$$\sqrt{LC} = 2 \times 10^{-3.5} = 6.32 \times 10^{-4}$$
Step C — reciprocal:
$$f_0 = \frac{1}{2 \times 3.14 \times 6.32 \times 10^{-4}}$$
$$f_0 = \frac{1}{3.97 \times 10^{-3}}$$
$$f_0 = 251.9\ Hz$$
$$f_0 \approx 252\ Hz$$

### Step 3: Verification & Physical Interpretation
Roughly 252 Hz — resonant frequency rises as LC shrinks, consistent with the previous example.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (25.2 Hz)**: a decimal slip in the LC product (one power of ten).
- **Option C trap (2520 Hz)**: the opposite decimal slip.
- **Option D trap (126 Hz)**: the student halves the answer — e.g. by using 4π instead of 2π in the denominator.
r""")

calc(T, "A series circuit has L = 40 mH and C = 10 µF. Its resonant frequency is about:",
     ["252 Hz", "25.2 Hz", "2520 Hz", "159 Hz"], 0,
     "LC = 0.04 × 10⁻⁵ = 4 × 10⁻⁷; f₀ = 1/(2π × 6.32 × 10⁻⁴) = 252 Hz.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 40\ mH = 0.04\ H$, $C = 10\ \mu F = 10 \times 10^{-6}\ F$.
Governing law:
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

### Step 2: Full Mathematical Workings
$$LC = 0.04 \times 10 \times 10^{-6}$$
$$LC = 4 \times 10^{-7}$$
$$\sqrt{LC} = 6.32 \times 10^{-4}$$
$$f_0 = \frac{1}{2 \times 3.14 \times 6.32 \times 10^{-4}}$$
$$f_0 = \frac{1}{3.97 \times 10^{-3}}$$
$$f_0 = 251.9\ Hz \approx 252\ Hz$$

### Step 3: Verification & Physical Interpretation
Quadrupling L while keeping C the same as the first example halves the resonant frequency from about 252 Hz... (check: L=100mH,C=10µF gave 159 Hz; here L=40mH gives 252 Hz — frequency is inversely proportional to √L, consistent: 159×√(100/40)=159×1.58=251 Hz).

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (25.2 Hz)**: power-of-ten slip in LC.
- **Option C trap (2520 Hz)**: power-of-ten slip the other way.
- **Option D trap (159 Hz)**: the student reuses the first example's answer without recomputing.
r""")

calc(T, "A series circuit has L = 10 mH and C = 100 µF. Its resonant frequency is about:",
     ["159 Hz", "15.9 Hz", "1590 Hz", "31.8 Hz"], 0,
     "LC = 0.01 × 10⁻⁴ = 10⁻⁶; f₀ = 1/(2π × 10⁻³) = 159 Hz.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $L = 10\ mH = 0.01\ H$, $C = 100\ \mu F = 100 \times 10^{-6}\ F$.
Governing law:
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

### Step 2: Full Mathematical Workings
$$LC = 0.01 \times 100 \times 10^{-6}$$
$$LC = 1 \times 10^{-6}$$
$$\sqrt{LC} = 1 \times 10^{-3}$$
$$f_0 = \frac{1}{2 \times 3.14 \times 1 \times 10^{-3}}$$
$$f_0 = \frac{1000}{6.28}$$
$$f_0 = 159.2\ Hz \approx 159\ Hz$$

### Step 3: Verification & Physical Interpretation
The same LC product as the first example (10⁻⁶), so the same 159 Hz — a useful check that f₀ depends only on the product LC, not on the individual values.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (15.9 Hz)**: power-of-ten slip.
- **Option C trap (1590 Hz)**: power-of-ten slip the other way.
- **Option D trap (31.8 Hz)**: the student divides by 4π instead of 2π.
r""")

calc(T, "In a series resonant circuit with R = 10 Ω and X_L = X_C = 100 Ω at resonance, the Q factor is:",
     ["10", "100", "1", "0.1"], 0,
     "Q = X_L/R = 100/10 = 10.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $R = 10\ \Omega$, $X_L = X_C = 100\ \Omega$ at resonance.
Governing law — Q factor at resonance:
$$Q = \frac{X_L}{R} = \frac{X_C}{R}$$

### Step 2: Full Mathematical Workings
$$Q = \frac{100}{10}$$
$$Q = 10$$

### Step 3: Verification & Physical Interpretation
The reactance is ten times the resistance, so the circuit stores ten times more energy per cycle than it dissipates — Q = 10, a moderately selective resonance.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (100)**: the student quotes the reactance itself as Q.
- **Option C trap (1)**: the student divides R by X (inverted ratio).
- **Option D trap (0.1)**: the student computes R/X twice-inverted, i.e. 10/100.
r""")

calc(T, "A series resonant circuit has f₀ = 100 kHz and Q = 50. Its bandwidth is:",
     ["2 kHz", "5 kHz", "20 kHz", "0.5 kHz"], 0,
     "Bandwidth = f₀/Q = 100 kHz/50 = 2 kHz.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $f_0 = 100\ kHz$, $Q = 50$.
Governing law:
$$\text{Bandwidth} = \frac{f_0}{Q}$$

### Step 2: Full Mathematical Workings
$$\text{Bandwidth} = \frac{100\ kHz}{50}$$
$$\text{Bandwidth} = 2\ kHz$$

### Step 3: Verification & Physical Interpretation
A Q of 50 concentrates the resonance into a 2 kHz band around 100 kHz — high Q, narrow bandwidth, high selectivity.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (5 kHz)**: the student uses Q = 20.
- **Option C trap (20 kHz)**: the student uses Q = 5.
- **Option D trap (0.5 kHz)**: the student multiplies instead of dividing (100 × 50 kHz inverted).
r""")

calc(T, "At resonance, a circuit has f₀ = 159 Hz and L = 100 mH. The inductive reactance X_L at resonance is about:",
     ["100 Ω", "1000 Ω", "10 Ω", "159 Ω"], 0,
     "X_L = 2πf₀L = 2 × 3.14 × 159 × 0.1 = 99.9 Ω ≈ 100 Ω (and X_C has the same value).",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $f_0 = 159\ Hz$, $L = 0.1\ H$.
Governing law:
$$X_L = 2\pi f L$$

### Step 2: Full Mathematical Workings
$$X_L = 2 \times 3.14 \times 159 \times 0.1$$
$$2 \times 3.14 = 6.28$$
$$6.28 \times 159 = 998.5$$
$$998.5 \times 0.1 = 99.85$$
$$X_L \approx 100\ \Omega$$

### Step 3: Verification & Physical Interpretation
At the resonant frequency the inductive and capacitive reactances are equal — so X_C ≈ 100 Ω as well. This is a handy cross-check of any f₀ calculation.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (1000 Ω)**: the student forgets the 0.1 H factor.
- **Option C trap (10 Ω)**: the student uses L = 10 mH.
- **Option D trap (159 Ω)**: the student quotes the frequency itself instead of computing the reactance.
r""")

# =====================================================================
# TOPIC 5 — NETWORK THEOREMS APPLIED TO AC
# =====================================================================
T = "eee-network-theorems"

theory(T, "Thévenin's theorem states that any linear two-terminal network can be replaced by:",
       ["a single voltage source (the open-circuit voltage) in series with the equivalent impedance",
        "a single current source in parallel with an impedance",
        "a single resistor only",
        "a capacitor and an inductor in series"], 0,
       "Thévenin: one voltage source (V_th) in SERIES with Z_th.",
       r"""### Step 1: Core Principle
Thévenin's theorem: any linear two-terminal network is equivalent to a single voltage source (the open-circuit voltage $V_{th}$ at the terminals) in SERIES with the equivalent impedance $Z_{th}$ (the impedance seen at the terminals with all independent sources killed). For AC networks $Z_{th}$ is complex ($R \pm jX$).

### Step 2: Testing the Options
- **Option A (correct)**: voltage source + series impedance.
- **Option B (wrong)**: that is NORTON's theorem — the dual form.
- **Option C (wrong)**: a resistor alone cannot represent the source.
- **Option D (wrong)**: specific components, not an equivalent network.

### Step 3: Exam Trap Summary
The trap is Thévenin/Norton swapping. Anchor: Thévenin = Voltage in Series; Norton = Current in Parallel — the two forms are interchangeable through $V_{th} = I_N Z_{th}$.
r""")

theory(T, "Norton's theorem states that any linear two-terminal network can be replaced by:",
       ["a single current source (the short-circuit current) in parallel with the same equivalent impedance",
        "a voltage source in series with an impedance",
        "an ideal transformer",
        "a resistor and an inductor in series"], 0,
       "Norton: one current source (I_N) in PARALLEL with Z_N = Z_th.",
       r"""### Step 1: Core Principle
Norton's theorem is the dual of Thévenin's: any linear two-terminal network is equivalent to a single current source (the short-circuit current $I_N$) in PARALLEL with $Z_N$, where $Z_N = Z_{th}$.

### Step 2: Testing the Options
- **Option A (correct)**: current source + parallel impedance.
- **Option B (wrong)**: that is Thévenin's form.
- **Option C (wrong)**: a transformer is a real device, not an equivalent network.
- **Option D (wrong)**: two components cannot represent the whole source behaviour.

### Step 3: Exam Trap Summary
Thévenin/Norton duality again — in the exam, map "voltage→series" and "current→parallel" before answering.
r""")

theory(T, "The superposition theorem states that in a linear network with several sources, the response in any branch is:",
       ["the algebraic sum of the responses produced by each source acting alone, with the other sources replaced by their internal impedances",
        "the product of the responses of all the sources",
        "the response of the largest source only",
        "the average of the responses of all the sources"], 0,
       "Superposition: one source at a time (others killed), then add the responses algebraically.",
       r"""### Step 1: Core Principle
Superposition: in a linear network, consider ONE source at a time — voltage sources replaced by short circuits, current sources replaced by open circuits — and the response in any branch is the ALGEBRAIC SUM of the individual responses. For AC networks the summation is done with phasors.

### Step 2: Testing the Options
- **Option A (correct)**: one-at-a-time plus algebraic summation.
- **Option B (wrong)**: responses are added, never multiplied.
- **Option C (wrong)**: all sources contribute; the largest is not special.
- **Option D (wrong)**: averaging loses the physics — contributions add.

### Step 3: Exam Trap Summary
Two traps: (1) using multiplication instead of addition; (2) killing sources wrongly — remember voltage sources become SHORTS and current sources become OPENS (their internal impedances remain).
r

**Key pattern:** responses add; series impedances combine as $Z_{eq} = Z_1 + Z_2$.""")

theory(T, "When applying Thévenin/Norton theorems to AC networks, the impedances must be treated as:",
       ["complex quantities (R ± jX) so that both magnitude and phase are preserved",
        "real resistances only",
        "imaginary numbers only",
        "scalar magnitudes without phase"], 0,
       "AC impedances are complex; keep the j-terms through every line.",
       r"""### Step 1: Core Principle
In AC networks the impedances are complex quantities of the form $Z = R \pm jX$. The theorems work exactly as in DC, but the arithmetic is complex, and carrying the j-terms preserves BOTH magnitude and phase of the equivalent.

### Step 2: Testing the Options
- **Option A (correct)**: complex treatment preserves magnitude + phase.
- **Option B (wrong)**: ignoring reactance gives wrong answers whenever L or C is present.
- **Option C (wrong)**: the real part (resistance) matters equally.
- **Option D (wrong)**: magnitude-only analysis loses the phase information entirely.

### Step 3: Exam Trap Summary
The trap is "magnitude-only" shortcuts. In the written exam, write Z in full complex form and combine j-terms explicitly — dropping j is the single most common error in AC theorem questions.
r""")

theory(T, "A circuit is classified as nonlinear when:",
       ["its i-v graph is not a straight line",
        "it contains only resistors",
        "its i-v graph is a straight line through the origin",
        "it contains no sources"], 0,
       "Linear ⇔ straight-line i-v graph; anything else is nonlinear.",
       r"""### Step 1: Core Principle
A circuit is classified by examining its i-v graph: a straight line means linear ($v = Ri$); ANY other shape means nonlinear. Examples: $i = v^2$ is nonlinear; even the piecewise-linear absolute value $|v|$ is nonlinear because it cannot be written as $y = ax + b$.

### Step 2: Testing the Options
- **Option A (correct)**: the graph-shape criterion.
- **Option B (wrong)**: resistors are precisely what MAKE a circuit linear.
- **Option C (wrong)**: a straight line through the origin is the linear case.
- **Option D (wrong)**: having no sources does not determine linearity.

### Step 3: Exam Trap Summary
The trap is classifying by component list instead of by graph shape. Always draw or imagine the i-v curve first.
r""")

theory(T, "The negative resistance converter is:",
       ["a useful nonlinear op-amp circuit whose i-v slope is negative over a region, used to build oscillators",
        "a resistor that obeys Ohm's law",
        "a transformer winding arrangement",
        "a rectifier circuit"], 0,
       "Negative-resistance converter: negative i-v slope; it delivers power — the core of oscillators.",
       r"""### Step 1: Core Principle
The negative resistance converter is an op-amp nonlinear circuit whose i-v characteristic has a NEGATIVE slope over some region: as voltage rises, current falls. Over that region it DELIVERS power instead of absorbing it — exactly what an oscillator needs to sustain its own oscillations.

### Step 2: Testing the Options
- **Option A (correct)**: the converter and its oscillator application.
- **Option B (wrong)**: an Ohmic resistor has a positive slope — the opposite.
- **Option C (wrong)**: it is built with an op-amp, not transformer windings.
- **Option D (wrong)**: a rectifier converts AC to DC; unrelated.

### Step 3: Exam Trap Summary
The trap is confusing "negative resistance" with "low resistance". Negative resistance means the v-i slope is negative (power source behaviour), not that R is a small positive number.
r

**Key recall:** over its active region the converter has a negative slope, $dV/dI < 0$.""")

calc(T, "Two impedances Z₁ = (100 + j100) Ω and Z₂ = (100 − j100) Ω are connected in series. The equivalent impedance is:",
     ["200 Ω (purely resistive)", "0 Ω", "j200 Ω", "100 Ω"], 0,
     "Z = Z₁ + Z₂ = (100 + j100) + (100 − j100) = 200 + j0 = 200 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $Z_1 = 100 + j100\ \Omega$, $Z_2 = 100 - j100\ \Omega$.
Governing law — series impedances add:
$$Z_{eq} = Z_1 + Z_2$$

### Step 2: Full Mathematical Workings
$$Z_{eq} = (100 + j100) + (100 - j100)$$
Add the real parts:
$$100 + 100 = 200$$
Add the imaginary parts:
$$j100 - j100 = j0$$
$$Z_{eq} = 200 + j0$$
$$Z_{eq} = 200\ \Omega\ \text{(purely resistive)}$$

### Step 3: Verification & Physical Interpretation
The inductive and capacitive reactances cancel exactly, leaving a pure 200 Ω resistance — the same physics as series resonance.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (0 Ω)**: the student cancels the real parts too, forgetting they add.
- **Option C trap (j200 Ω)**: the student adds the imaginary parts without cancelling (treating both as +j).
- **Option D trap (100 Ω)**: the student averages the two impedances instead of adding.
r""")

calc(T, "Two equal impedances of (50 + j50) Ω each are connected in PARALLEL. The equivalent impedance is:",
     ["(25 + j25) Ω", "(100 + j100) Ω", "(50 − j50) Ω", "50 Ω"], 0,
     "Two equal impedances in parallel halve: Z = (50 + j50)/2 = (25 + j25) Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $Z_1 = Z_2 = 50 + j50\ \Omega$, connected in parallel.
Governing law — parallel impedances:
$$Z_{eq} = \frac{Z_1 Z_2}{Z_1 + Z_2}$$

### Step 2: Full Mathematical Workings
Because the two impedances are EQUAL, $Z_1 = Z_2 = Z$, the formula specialises:
$$Z_{eq} = \frac{Z \times Z}{Z + Z}$$
$$Z_{eq} = \frac{Z^2}{2Z}$$
Cancel one factor of Z:
$$Z_{eq} = \frac{Z}{2}$$
$$Z_{eq} = \frac{50 + j50}{2}$$
$$Z_{eq} = 25 + j25\ \Omega$$

### Step 3: Verification & Physical Interpretation
Equal parallel impedances halve — both the real and imaginary parts divide by two. This shortcut is faster and safer than expanding the product/sum formula.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (100 + j100)**: the student ADDS the impedances (series rule) instead of halving.
- **Option C trap (50 − j50)**: the student conjugates the sign instead of halving.
- **Option D trap (50 Ω)**: the student halves only the real part and drops j.
r""")

calc(T, "A circuit has R = 8 Ω in series with X_L = 6 Ω. The magnitude of the equivalent impedance is:",
     ["10 Ω", "14 Ω", "2 Ω", "48 Ω"], 0,
     "|Z| = √(8² + 6²) = √(64 + 36) = √100 = 10 Ω.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $R = 8\ \Omega$, $X_L = 6\ \Omega$.
Governing law:
$$|Z| = \sqrt{R^2 + X_L^2}$$

### Step 2: Full Mathematical Workings
$$|Z| = \sqrt{8^2 + 6^2}$$
$$8^2 = 64$$
$$6^2 = 36$$
$$|Z| = \sqrt{64 + 36}$$
$$|Z| = \sqrt{100}$$
$$|Z| = 10\ \Omega$$

### Step 3: Verification & Physical Interpretation
The 6–8–10 impedance triangle. The theorem-work equivalent impedance is found the same way as any series R-X combination.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (14 Ω)**: direct addition of R and X.
- **Option C trap (2 Ω)**: subtraction.
- **Option D trap (48 Ω)**: multiplication.
r""")

calc(T, "The Thévenin equivalent of a network gives V_th = 20∠0° V and Z_th = (10 + j0) Ω. A load of (10 + j0) Ω is connected. The load current is:",
     ["1 A", "2 A", "0.5 A", "20 A"], 0,
     "I = V_th/(Z_th + Z_load) = 20/(10 + 10) = 20/20 = 1 A.",
     r"""### Step 1: Identification of Given Parameters and Governing Laws
Given: $V_{th} = 20\angle 0^\circ\ V$, $Z_{th} = 10\ \Omega$, $Z_{load} = 10\ \Omega$.
Governing law — current in the Thévenin model:
$$I = \frac{V_{th}}{Z_{th} + Z_{load}}$$

### Step 2: Full Mathematical Workings
$$Z_{th} + Z_{load} = 10 + 10 = 20\ \Omega$$
$$I = \frac{20}{20}$$
$$I = 1\ A$$

### Step 3: Verification & Physical Interpretation
The two 10 Ω impedances split the 20 V equally — 1 A flows to the load. With zero phase angle the current is in phase with the voltage.

### Step 4: Breakdown of Wrong Options / Common Student Mistakes
- **Option B trap (2 A)**: the student divides by Z_th only, forgetting the load impedance.
- **Option C trap (0.5 A)**: the student divides by 40 Ω (doubling the total).
- **Option D trap (20 A)**: the student multiplies V by Z (20 × 1).
r""")

# --- multi-part theoretical question (Topic 5) ---
theory(T, "Match each theorem to its equivalent-circuit form: (a) Thévenin (b) Norton (c) Superposition.",
       ["voltage source in series with Z; current source in parallel with Z; algebraic sum of single-source responses",
        "current source in series with Z; voltage source in parallel with Z; product of single-source responses",
        "voltage source in parallel with Z; current source in series with Z; sum of single-source responses",
        "current source in parallel with Z; voltage source in series with Z; average of single-source responses"], 0,
       "Thévenin = voltage in series; Norton = current in parallel; Superposition = algebraic sum.",
       r"""### Step 1: Core Principle
The three theorem forms:
(a) Thévenin — a voltage source (open-circuit voltage) in SERIES with the equivalent impedance.
(b) Norton — a current source (short-circuit current) in PARALLEL with the equivalent impedance.
(c) Superposition — the response is the ALGEBRAIC SUM of the responses from each source acting alone.

### Step 2: Testing the Options
- **Option A (correct)**: all three pairings exact.
- **Option B (wrong)**: the series/parallel placements are swapped, and superposition responses are summed, never multiplied.
- **Option C (wrong)**: Thévenin's source must be in SERIES (parallel is wrong), and Norton's in parallel.
- **Option D (wrong)**: superposition uses a sum, not an average; and the average would lose the physics.

### Step 3: Exam Trap Summary
The trap is the series/parallel swap between the two dual theorems. Anchor: "Thévenin = the series one; Norton = the parallel one", and superposition = SUM (never product or average).
r

**Key relation linking the dual forms:** $V_{th} = I_N Z_{th}$.""")
