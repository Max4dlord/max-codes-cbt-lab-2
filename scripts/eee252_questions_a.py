# -*- coding: utf-8 -*-
r"""EEE 252 — PART B past questions, FILE A: Diodes, Rectifiers & Op-Amps.
Sources: OAU 2023/24 Harmattan exam, 2023/24 1st-semester exam, 2021/22 Rain
test, 2026 photographed test, Assignments 3, Sedra problem sets.
Every calc solution: Step 1–4, zero step-skipping, LaTeX math, distractor
analysis. Theory solutions: core principle, option testing, trap summary.r"""

QUESTIONS_A = []

def calc(topic, q, opts, ans, short, sol):
    QUESTIONS_A.append(dict(topicId=topic, kind="calc", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

def theory(topic, q, opts, ans, short, sol):
    QUESTIONS_A.append(dict(topicId=topic, kind="theory", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

# =====================================================================
# TOPIC 1 — DIODE CIRCUITS & DIODE I-V CHARACTERISTICS
# =====================================================================
T = "eee252-diodes"

theory(T, "What is a nonlinear circuit element?",
       ["An element whose current–voltage relationship is not a straight line (its i-v graph is not of the form $i = av + b$)",
        "An element that obeys Ohm's law at all voltages",
        "An element whose i-v graph is a straight line through the origin",
        "An element with no resistance"], 0,
       "A nonlinear element has an i-v relation that is NOT a straight line — e.g. a diode's exponential law $i_D = I_S(e^{v_D/V_T}-1)$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
A circuit element is classified by its i-v characteristic. If the i-v graph is a straight line, the element is linear and can be written in the form $i = av + b$. Any element whose i-v graph is NOT a straight line is a nonlinear circuit element. The diode is the classic example: $i_D = I_S(e^{v_D/V_T} - 1)$ plots as an exponential curve.

**Step 2: Testing the Options**
- **Option A (correct)**: the straight-line test, with the diode's exponential law as the canonical example.
- **Option B (wrong)**: obeying Ohm's law at all voltages is the definition of a LINEAR resistor.
- **Option C (wrong)**: a straight line through the origin is the most linear element there is (ideal resistor).
- **Option D (wrong)**: "no resistance" describes an ideal short circuit, which is linear.

**Step 3: Exam Trap Summary**
The trap is confusing "nonlinear" with "non-ohmic and weird". The ONLY test is the shape of the i-v graph: straight line = linear; anything else (exponential, square-law, piecewise) = nonlinear. In the written exam, state the test first, then give the diode as the example.
r""")

calc(T, "A silicon diode has saturation current $I_S = 10^{-15}$ A and is forward-biased with $v_D = 0.7$ V. Using the Shockley equation with $V_T = 25$ mV, the diode current $i_D$ is about:",
     ["1.45 mA", "14.5 mA", "0.145 mA", "10⁻¹⁵ A"], 0,
     "$i_D = I_S(e^{v_D/V_T}-1) = 10^{-15}(e^{28}-1)$; $e^{28} \\approx 1.45\\times10^{12}$, so $i_D \\approx 1.45$ mA.",
     r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_S = 10^{-15}$ A, $v_D = 0.7$ V, $V_T = 25$ mV $= 0.025$ V.
Governing law — the Shockley (exponential) diode equation:
$$i_D = I_S(e^{v_D/V_T} - 1)$$

**Step 2: Full Mathematical Workings**
Compute the exponent:
$$\frac{v_D}{V_T} = \frac{0.7}{0.025}$$
$$\frac{0.7}{0.025} = 28$$
Substitute:
$$i_D = 10^{-15}(e^{28} - 1)$$
$$e^{28} = 1.4463 \times 10^{12}$$
Since $e^{28} \gg 1$, the $-1$ is negligible:
$$i_D = 10^{-15} \times 1.4463 \times 10^{12}$$
$$i_D = 1.4463 \times 10^{-3}$$
$$i_D = 1.45\ mA$$

**Step 3: Verification & Physical Interpretation**
0.7 V across a silicon junction drives about 1.45 mA — 28 thermal voltages of forward bias, consistent with the rule of thumb that every 60 mV decade multiplies the current tenfold. The $-1$ term matters only when $v_D$ is within a few $V_T$ of zero.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (14.5 mA)**: the student misplaces the exponent ($e^{29.9}$ style slip — i.e. using $v_D = 0.747$ V).
- **Option C trap (0.145 mA)**: a factor-of-10 slip in $e^{28}$ — e.g. reading $10^{11}$ instead of $10^{12}$.
- **Option D trap ($10^{-15}$ A)**: the student reports the SATURATION current $I_S$ itself, forgetting the exponential multiplication.
r""")

calc(T, "A diode conducts a DC current $I_D = 1$ mA at room temperature ($V_T = 25$ mV). Its small-signal (dynamic) resistance $r_d$ is:",
     ["25 Ω", "2.5 Ω", "250 Ω", "40 Ω"], 0,
     "$r_d = V_T/I_D = 25\\text{ mV}/1\\text{ mA} = 25\\ \\Omega$.",
     r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_D = 1$ mA $= 1 \times 10^{-3}$ A, $V_T = 25$ mV $= 25 \times 10^{-3}$ V.
Governing law — dynamic resistance of the diode:
$$r_d = \frac{V_T}{I_D}$$

**Step 2: Full Mathematical Workings**
$$r_d = \frac{25 \times 10^{-3}}{1 \times 10^{-3}}$$
Cancel the $10^{-3}$:
$$r_d = \frac{25}{1}$$
$$r_d = 25\ \Omega$$

**Step 3: Verification & Physical Interpretation**
The dynamic resistance is the slope resistance of the exponential curve at the bias point — the diode behaves like a 25 Ω resistor for SMALL signals about 1 mA. This is the single most useful diode number to memorise: "1 mA gives 25 Ω".

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (2.5 Ω)**: the student divides $V_T$ by 10 mA.
- **Option C trap (250 Ω)**: the student uses $I_D = 0.1$ mA.
- **Option D trap (40 Ω)**: the student uses $r_d = V_T/I_D \times \ln 10$ style mix-up, or applies the 40 mA/V transistor rule to a diode.
r""")

calc(T, "Four identical diodes are connected in series with a resistor R across a 15 V supply. For each diode, $v_D = 0.75$ V at $i_D = 1$ mA, and $V_T = 25$ mV. The total voltage across the four diodes is 3.3 V. The current through the diodes is about:",
     ["20 mA", "1 mA", "4 mA", "12 mA"], 0,
     "Per diode $v_D = 3.3/4 = 0.825$ V; $v_{D2}-v_{D1} = V_T\\ln(i_2/i_1)$ gives $0.075 = 0.025\\ln(i_2/1\\text{mA})$ ⇒ $i_2 = e^3$ mA ≈ 20 mA.",
     r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: four identical diodes in series; total voltage across them $4v_D = 3.3$ V; at reference current $i_{D1} = 1$ mA each diode drops $v_{D1} = 0.75$ V; $V_T = 25$ mV.
Governing law — the exponential diode relation between two operating points:
$$v_{D2} - v_{D1} = V_T \ln\frac{i_{D2}}{i_{D1}}$$

**Step 2: Full Mathematical Workings**
Voltage per diode:
$$v_{D2} = \frac{3.3}{4}$$
$$v_{D2} = 0.825\ V$$
Voltage difference from the reference point:
$$v_{D2} - v_{D1} = 0.825 - 0.75$$
$$v_{D2} - v_{D1} = 0.075\ V$$
Substitute into the exponential relation:
$$0.075 = 0.025 \ln\frac{i_{D2}}{1\ mA}$$
$$\frac{0.075}{0.025} = 3$$
$$\ln\frac{i_{D2}}{1\ mA} = 3$$
Exponentiate both sides:
$$\frac{i_{D2}}{1\ mA} = e^3$$
$$e^3 = 20.09$$
$$i_{D2} = 20.09\ mA \approx 20\ mA$$

**Step 3: Verification & Physical Interpretation**
Raising the per-diode drop by 75 mV (three thermal voltages) multiplies the current by $e^3 \approx 20$. The identical series diodes share the SAME current, so the string current is 20 mA.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (1 mA)**: the student ignores the higher 0.825 V drop and quotes the reference current.
- **Option C trap (4 mA)**: the student multiplies the reference current by the number of diodes.
- **Option D trap (12 mA)**: the student divides 3.3 V by 0.275 Ω style shortcut, or assumes a linear $v_D$–$i_D$ law.
r""")

calc(T, "In the same four-diode string across 15 V (diode current ≈ 20 mA, total diode drop 3.3 V), the series resistor R is about:",
     ["585 Ω", "750 Ω", "150 Ω", "1.2 kΩ"], 0,
     "R drops $15 - 3.3 = 11.7$ V at $20.09$ mA, so $R = 11.7/0.02009 = 582$ Ω ≈ 585 Ω.",
     r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: supply $V = 15$ V, total diode voltage $4v_D = 3.3$ V, string current $i_D = 20.09$ mA.
Governing law — Ohm's law for the series resistor:
$$V = i_D R + 4v_D \quad\Rightarrow\quad R = \frac{V - 4v_D}{i_D}$$

**Step 2: Full Mathematical Workings**
Voltage across the resistor:
$$V - 4v_D = 15 - 3.3$$
$$V - 4v_D = 11.7\ V$$
Resistor value:
$$R = \frac{11.7}{20.09 \times 10^{-3}}$$
$$R = \frac{11.7}{0.02009}$$
$$R = 582.4\ \Omega$$
$$R \approx 585\ \Omega$$

**Step 3: Verification & Physical Interpretation**
The resistor drops the remaining 11.7 V while carrying the 20 mA string current. Checking the loop: $0.02009 \times 582.4 + 3.3 = 11.7 + 3.3 = 15$ V — the KVL loop closes exactly.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (750 Ω)**: the student uses the reference current of 1 mA for four diodes — i.e. $R = 11.7/0.004$ style confusion.
- **Option C trap (150 Ω)**: the student divides the diode drop (3.3 V) by the current instead of the resistor drop.
- **Option D trap (1.2 kΩ)**: the student uses the per-diode 0.825 V instead of the total 3.3 V, giving $R = (15-0.825)/0.012$ style error.
r""")

theory(T, "State three limitations of diode logic gates (as used in simple AND/OR gates).",
       ["A 0.7 V drop per stage degrades logic levels; there is no gain so signals cannot be restored; they cannot invert (no NOT function)",
        "They consume no power; they invert signals; they have unlimited fan-out",
        "They need a clock; they are faster than CMOS; they amplify the input",
        "They work only with germanium diodes; they have infinite gain; they oscillate"], 0,
       "Diode logic loses 0.7 V per stage with no amplification, cannot restore levels, and provides no inversion.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
Diode logic gates (diode AND/OR with a pull-up/pull-down resistor) suffer from three fundamental limitations:
1. **Level degradation**: each conducting diode drops $\approx 0.7$ V, so cascaded gates progressively shift logic levels — a LOW propagating through n stages rises by $0.7n$ volts.
2. **No gain/restoration**: diode gates are passive; they cannot restore a degraded level to a full 0/5 V rail, so cascading beyond a few stages fails.
3. **No inversion**: diode logic cannot implement the NOT function; a complete logic family needs an inverting (active) element, which is why TTL/CMOS replaced diode logic.

**Step 2: Testing the Options**
- **Option A (correct)**: all three limitations stated.
- **Option B (wrong)**: diode gates DO consume power through the pull-up resistor and cannot invert.
- **Option C (wrong)**: diode gates are asynchronous (no clock) and slower/passive — they amplify nothing.
- **Option D (wrong)**: they work with silicon diodes and have no gain.

**Step 3: Exam Trap Summary**
The trap is inventing "advantages" for diode logic. Remember the pattern: passive (no gain) + 0.7 V/stage + no inversion = why real gates use transistors.
r""")

theory(T, "In a diode AND gate (diodes from inputs to output, pull-up resistor to $V_{CC} = 5$ V), both inputs are held at 5 V. The output voltage is:",
       ["5 V — both diodes are reverse/zero biased, so the pull-up holds the output at $V_{CC}$",
        "4.3 V — each diode drops 0.7 V",
        "0.7 V",
        "0 V"], 0,
       "With both anodes at 5 V and the cathode (output) also at 5 V via the pull-up, the diodes conduct no current, so $V_{out} = V_{CC} = 5$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
In the diode AND gate the output node is pulled HIGH by a resistor to $V_{CC} = 5$ V. A diode conducts only when its anode is about 0.7 V ABOVE its cathode. With both inputs at 5 V, each diode has anode = cathode = 5 V: the diode voltage is 0 V, below the 0.7 V threshold.

**Step 2: Testing the Options**
- **Option A (correct)**: no diode conducts, no current flows in the pull-up, so $V_{out} = V_{CC} = 5$ V with ZERO drop.
- **Option B (wrong)**: the 0.7 V drop applies only when a diode CONDUCTS — here neither conducts.
- **Option C (wrong)**: 0.7 V is the output when an input is LOW (diode conducting with anode at 0 V).
- **Option D (wrong)**: 0 V appears only if a diode's anode is at 0 V and the gate is pulling the output to 0.7 V.

**Step 3: Exam Trap Summary**
The trap is blindly subtracting 0.7 V "because there are diodes". The correct reflex: ask WHICH diode conducts first — a conducting diode drops 0.7 V; a non-conducting one drops whatever the circuit imposes. All-high inputs → no conduction → full 5 V output.
r""")

theory(T, "In the diode AND gate with a 0.7 V forward drop, the minimum voltage recognised as logic HIGH is 3.5 V. A LOW input (0 V) propagates through cascaded gates, each adding 0.7 V. The maximum number of cascaded stages that can be used before logic failure is:",
       ["4", "5", "10", "unlimited"], 0,
       "Stage n low-level = 0.7n V; failure when 0.7n ≥ 3.5 V, i.e. n = 5 — so only 4 stages are safe.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
When an input is LOW (0 V), its diode conducts and the gate output becomes $0 + 0.7 = 0.7$ V. That 0.7 V feeds the next gate's input; if THAT gate's other input is HIGH, its conducting diode lifts the output to $0.7 + 0.7 = 1.4$ V. Each cascaded stage adds 0.7 V to the propagated LOW level:
$$V_{LOW}(n) = 0.7 n$$

**Step 2: Full Mathematical Workings**
Logic failure occurs when the LOW level reaches the HIGH threshold, 3.5 V:
$$0.7 n \ge 3.5$$
$$n \ge \frac{3.5}{0.7}$$
$$n \ge 5$$
So the 5th stage would produce a "LOW" of 3.5 V — indistinguishable from HIGH. Therefore only:
$$n = 4$$
stages can be cascaded safely; the 5th fails.

**Step 3: Verification & Physical Interpretation**
At stage 4 the propagated low is $0.7 \times 4 = 2.8$ V, still below 3.5 V; at stage 5 it is exactly 3.5 V — at the failure boundary. This is precisely why diode logic cannot be cascaded deeply and why active gates (with gain) won.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (5)**: the student counts the FIRST failing stage instead of the last SAFE one.
- **Option C trap (10)**: the student divides 5 V by 0.7 V... no — by 0.5 V, i.e. uses the wrong threshold.
- **Option D trap (unlimited)**: the student forgets the 0.7 V/stage degradation entirely.
r""")

calc(T, "A clamping circuit consists of a capacitor C in series with the input, and a diode from the output node to ground (anode at ground, cathode at output — a negative clamper). The input is a square wave with levels +3 V and −1 V; the diode has a 0.7 V forward drop. The capacitor charges to:",
     ["2.3 V, with its left (input-side) plate positive",
      "3.7 V, with its right plate positive",
      "0.7 V, with the left plate positive",
      "1 V, with the right plate positive"], 0,
       "The diode conducts at the +3 V peak, clamping the output to +0.7 V, so the capacitor charges to 3 − 0.7 = 2.3 V (input plate positive).",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: square wave input $v_i = +3$ V / $-1$ V; diode (anode to ground, cathode to output) with $V_D = 0.7$ V.
Circuit layout (textual description): the input source connects to the LEFT plate of capacitor C; the RIGHT plate is the output node, where the diode's cathode is attached; the diode's anode is grounded. When the output tries to rise above $+0.7$ V the diode conducts and clamps it.

**Step 2: Full Mathematical Workings**
At the positive input peak ($v_i = +3$ V), the diode conducts and pins the output to:
$$v_o = +0.7\ V$$
Capacitor voltage (left plate relative to right):
$$V_C = v_i - v_o$$
$$V_C = 3 - 0.7$$
$$V_C = 2.3\ V$$
The left (input-side) plate is positive because $v_i > v_o$ during charging.

**Step 3: Verification & Physical Interpretation**
Once charged to 2.3 V, the capacitor behaves as a fixed battery: the output equals $v_o = v_i - 2.3$ V. At $v_i = +3$ V: $v_o = 0.7$ V (just at conduction); at $v_i = -1$ V: $v_o = -3.3$ V (diode OFF). The waveform is the input shifted DOWN by 2.3 V, with its positive peak clamped to +0.7 V.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (3.7 V)**: the student ADDS the diode drop to the peak (3 + 0.7) instead of subtracting.
- **Option C trap (0.7 V)**: the student confuses the output clamp level with the CAPACITOR voltage.
- **Option D trap (1 V)**: the student charges the capacitor with the negative peak (−1 + 0.7 mis-signed).
r""")

calc(T, "For the same negative clamper (input +3 V/−1 V, diode drop 0.7 V), the two output levels are:",
     ["+0.7 V and −3.3 V", "+3 V and −1 V", "+2.3 V and −1.7 V", "+3.7 V and −0.3 V"], 0,
       "Output = input − 2.3 V: +3 − 2.3 = +0.7 V and −1 − 2.3 = −3.3 V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Capacitor charged to $V_C = 2.3$ V (input plate positive). In steady state the output is the input shifted by the capacitor voltage:
$$v_o = v_i - V_C = v_i - 2.3$$

**Step 2: Full Mathematical Workings**
Positive input level:
$$v_o = 3 - 2.3$$
$$v_o = +0.7\ V$$
Negative input level:
$$v_o = -1 - 2.3$$
$$v_o = -3.3\ V$$

**Step 3: Verification & Physical Interpretation**
The positive peak is clamped to +0.7 V (the diode just conducts there), and the entire waveform sits 2.3 V lower than the input — a perfect DC-level shift. Sketching: the output square wave toggles between +0.7 V and −3.3 V, the same peak-to-peak (4 V) as the input.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student forgot the clamping action and copied the input levels.
- **Option C trap**: the student subtracted 0.7 V from BOTH levels instead of 2.3 V (i.e. treated the shift as the diode drop).
- **Option D trap**: the student ADDED 0.7 V to the positive level and subtracted it from the negative.
r""")

calc(T, "For the same negative clamper, the input changes to +3 V / −5 V. The new output levels are:",
     ["+0.7 V and −7.3 V", "+0.7 V and −5 V", "+3 V and −5 V", "+2.3 V and −5.7 V"], 0,
       "The positive peak still clamps to +0.7 V, so the shift remains 2.3 V: output = +0.7 V and −5 − 2.3 = −7.3 V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
The clamping level depends only on the POSITIVE peak (+3 V) and the diode drop (0.7 V), so the capacitor still charges to:
$$V_C = 3 - 0.7 = 2.3\ V$$
The negative level changes to $-5$ V.

**Step 2: Full Mathematical Workings**
$$v_o = v_i - 2.3$$
Positive peak:
$$v_o = 3 - 2.3 = +0.7\ V$$
Negative peak:
$$v_o = -5 - 2.3$$
$$v_o = -7.3\ V$$

**Step 3: Verification & Physical Interpretation**
Only the extreme positive value sets the clamp; making the negative excursion bigger simply pushes the lower output level further down by the same amount. The waveform is the same 2.3 V-down shift: +0.7 V / −7.3 V.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student clamped only the top level and left the bottom at −5 V — forgetting the capacitor shift applies to ALL levels.
- **Option C trap**: no clamping considered at all.
- **Option D trap**: the student re-derived the shift from the new peak-to-peak (8 V) instead of the positive peak.
r""")

calc(T, "Incremental (small-signal) analysis: a voltage source $v = V + \\Delta v$ (with $V = 30$ V DC, $\\Delta v = 200$ mV AC) drives a network through $R_1 = 4\\ \\Omega$ to node X; $R_2 = 4\\ \\Omega$ runs from X to the output node o; at node o a nonlinear element $Z_D$ ($i_D = v_D + v_D^2$, in amperes) connects to ground, and a current source $i = I + \\Delta i$ ($I = 10$ A DC, $\\Delta i = 100$ mA AC) feeds current INTO node o. The DC output voltage $V_o$ is about:",
     ["3.19 V", "2.45 V", "5.0 V", "0.0 V"], 0,
       "KCL at o with $v_X = (V + v_o)/2$: $(30-v_o)/8 + 10 = v_o + v_o^2$ ⇒ $v_o^2 + 1.125v_o - 13.75 = 0$ ⇒ $v_o \\approx 3.19$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V = 30$ V, $I = 10$ A, $R_1 = R_2 = 4\ \Omega$, element law $i_D = v_D + v_D^2$ (with $v_D = v_o$).
Schematic layout (textual): source v → $R_1$ → node X → $R_2$ → output node o; element $Z_D$ from o to ground; current source i (arrow INTO node o) from ground to o.
Governing laws — KCL at node X and node o:
$$\frac{v - v_X}{R_1} = \frac{v_X - v_o}{R_2} \qquad \frac{v_X - v_o}{R_2} + i = i_D(v_o)$$

**Step 2: Full Mathematical Workings**
Step A — from KCL at X with $R_1 = R_2$:
$$\frac{v - v_X}{4} = \frac{v_X - v_o}{4}$$
$$v - v_X = v_X - v_o$$
$$2v_X = v + v_o$$
$$v_X = \frac{v + v_o}{2}$$
Step B — substitute into KCL at o:
$$\frac{(v + v_o)/2 - v_o}{4} + i = v_o + v_o^2$$
$$\frac{v - v_o}{8} + i = v_o + v_o^2$$
Step C — DC solution ($v = 30$, $i = 10$):
$$\frac{30 - V_o}{8} + 10 = V_o + V_o^2$$
$$3.75 - 0.125V_o + 10 = V_o + V_o^2$$
$$V_o^2 + 1.125V_o - 13.75 = 0$$
Quadratic formula:
$$V_o = \frac{-1.125 + \sqrt{1.125^2 + 4 \times 13.75}}{2}$$
$$1.125^2 = 1.266 \qquad 4 \times 13.75 = 55$$
$$V_o = \frac{-1.125 + \sqrt{56.27}}{2}$$
$$\sqrt{56.27} = 7.501$$
$$V_o = \frac{6.376}{2}$$
$$V_o = 3.188\ V \approx 3.19\ V$$

**Step 3: Verification & Physical Interpretation**
Back-substitution: $i_D = 3.188 + 10.16 = 13.35$ A; LHS $= (30-3.188)/8 + 10 = 3.35 + 10 = 13.35$ A — KCL balances exactly. The nonlinear element's quadratic term adds about 10 A of extra current at this bias point.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (2.45 V)**: the student places the nonlinear element at the MIDDLE node X instead of the output (different topology).
- **Option C trap (5.0 V)**: the student drops the $v_o^2$ term entirely and solves the linear equation.
- **Option D trap (0.0 V)**: the student solves the wrong root of the quadratic or assumes the output node is grounded.
r""")

calc(T, "For the SAME incremental-analysis circuit (V = 30 V, I = 10 A, Δv = 200 mV, Δi = 100 mA, R₁ = R₂ = 4 Ω, i_D = v_D + v_D², DC solution V_o ≈ 3.19 V), the AC component of the output voltage is about:",
     ["16.7 mV", "167 mV", "1.67 mV", "33.3 mV"], 0,
       "Incremental conductance $g_D = 1 + 2V_o = 7.38$ S; KCL: $(\\Delta v - v_o)/8 + \\Delta i = g_D v_o$ ⇒ $v_o = (0.025 + 0.1)/7.505 = 16.7$ mV.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $\Delta v = 200$ mV $= 0.2$ V, $\Delta i = 100$ mA $= 0.1$ A, DC bias $V_o = 3.188$ V.
Governing laws — the incremental conductance of the element and the small-signal KCL:
$$g_D = \left.\frac{di_D}{dv_D}\right|_{V_o} = 1 + 2V_o \qquad \frac{\Delta v - v_o}{8} + \Delta i = g_D v_o$$

**Step 2: Full Mathematical Workings**
Step A — conductance at the bias point:
$$g_D = 1 + 2 \times 3.188$$
$$g_D = 1 + 6.376$$
$$g_D = 7.376\ S$$
Step B — small-signal KCL (with $v_X = (\Delta v + v_o)/2$ as before):
$$\frac{\Delta v - v_o}{8} + \Delta i = g_D v_o$$
$$\frac{0.2 - v_o}{8} + 0.1 = 7.376 v_o$$
$$0.025 - 0.125v_o + 0.1 = 7.376 v_o$$
$$0.125 = 7.501 v_o$$
$$v_o = \frac{0.125}{7.501}$$
$$v_o = 0.01666\ V = 16.7\ mV$$

**Step 3: Verification & Physical Interpretation**
A 200 mV input perturbation produces only 16.7 mV at the output — the low 4 Ω resistors fight the high conductance (7.4 S) of the nonlinear element, so most of the perturbation is absorbed by the current-source path. The AC gain is $\Delta v_o/\Delta v = 0.0167/0.2 = 0.083$ (−21.6 dB).

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (167 mV)**: the student forgets the $-1$ in the conductance derivative ($g_D = 2V_o$ alone → larger... actually uses $g_D = 2V_o$ and drops Δi).
- **Option C trap (1.67 mV)**: a factor-of-10 slip in the denominator (7.5 → 75).
- **Option D trap (33.3 mV)**: the student doubles the perturbation (uses 400 mV) or halves the denominator.
r""")

# =====================================================================
# TOPIC 2 — RECTIFICATION & POWER SUPPLY DESIGN
# =====================================================================
T = "eee252-rectifiers"

theory(T, "Match each rectifier to its diode count and PIV: (a) half-wave (b) centre-tapped full-wave (c) bridge full-wave.",
       ["1 diode, PIV = Vₘ; 2 diodes, PIV = 2Vₘ; 4 diodes, PIV = Vₘ",
        "1 diode, PIV = 2Vₘ; 2 diodes, PIV = Vₘ; 4 diodes, PIV = 2Vₘ",
        "2 diodes, PIV = Vₘ; 1 diode, PIV = 2Vₘ; 4 diodes, PIV = 2Vₘ",
        "1 diode, PIV = Vₘ/2; 2 diodes, PIV = Vₘ; 4 diodes, PIV = Vₘ/2"], 0,
       "Half-wave: 1 diode, PIV = Vₘ. Centre-tap: 2 diodes, PIV = 2Vₘ. Bridge: 4 diodes, PIV = Vₘ.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
- Half-wave: one diode conducts on alternate half-cycles; the OFF diode blocks the full peak $V_m$.
- Centre-tapped full-wave: two diodes conduct alternately; the OFF diode sees the FULL secondary winding, i.e. $2V_m$.
- Bridge full-wave: four diodes, two conducting at a time; each OFF diode blocks only $V_m$ (the other series diode shares the voltage).

**Step 2: Testing the Options**
- **Option A (correct)**: 1/Vₘ, 2/2Vₘ, 4/Vₘ — the standard summary table.
- **Option B (wrong)**: swaps the half-wave and centre-tap PIVs, and gives the bridge 2Vₘ.
- **Option C (wrong)**: wrong diode counts (half-wave uses 1, not 2).
- **Option D (wrong)**: halves the PIV values.

**Step 3: Exam Trap Summary**
The centre-tap $2V_m$ vs bridge $V_m$ distinction is the classic PIV trap. Anchor: the OFF diode in the centre-tap circuit sees the whole secondary (two halves in series); in the bridge it sees only one winding voltage.
r""")

calc(T, "A centre-tapped full-wave rectifier is fed from a transformer whose total secondary voltage is 200 V r.m.s. (100–0–100 V). The PIV rating each diode must withstand is:",
     ["282.8 V", "141.4 V", "200 V", "100 V"], 0,
       "PIV = 2Vₘ where $V_m = \\sqrt{2}\\times100 = 141.4$ V, so PIV = 282.8 V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: centre-tapped secondary, 100–0–100 V r.m.s. (each half = 100 V r.m.s.).
Governing laws:
$$V_m = \sqrt{2}\,V_{rms} \qquad \text{PIV}_{CT} = 2V_m$$

**Step 2: Full Mathematical Workings**
Peak voltage per half-winding:
$$V_m = \sqrt{2} \times 100$$
$$V_m = 1.414 \times 100$$
$$V_m = 141.4\ V$$
PIV of the centre-tapped rectifier:
$$\text{PIV} = 2V_m$$
$$\text{PIV} = 2 \times 141.4$$
$$\text{PIV} = 282.8\ V$$

**Step 3: Verification & Physical Interpretation**
When diode D1 conducts, diode D2 is OFF and must block the sum of the two half-winding peaks — hence $2V_m$. The design rule: choose diodes rated comfortably above 282.8 V.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (141.4 V)**: the student uses $V_m$ only — the BRIDGE PIV, not the centre-tap.
- **Option C trap (200 V)**: the student forgets the $\sqrt{2}$ peak conversion.
- **Option D trap (100 V)**: the student uses the r.m.s. value of one half-winding.
r""")

calc(T, "A bridge rectifier is fed from a 50 V r.m.s. secondary. The DC output voltage of the unfiltered rectifier is about:",
     ["45.0 V", "31.8 V", "70.7 V", "22.5 V"], 0,
       "$V_{DC} = 2V_m/\\pi$ with $V_m = \\sqrt{2}\\times50 = 70.71$ V ⇒ $V_{DC} = 141.4/\\pi = 45.0$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{rms} = 50$ V (bridge full-wave).
Governing laws:
$$V_m = \sqrt{2}\,V_{rms} \qquad V_{DC} = \frac{2V_m}{\pi}$$

**Step 2: Full Mathematical Workings**
$$V_m = 1.414 \times 50$$
$$V_m = 70.71\ V$$
$$V_{DC} = \frac{2 \times 70.71}{\pi}$$
$$V_{DC} = \frac{141.42}{3.1416}$$
$$V_{DC} = 45.0\ V$$

**Step 3: Verification & Physical Interpretation**
The full-wave DC average is $0.636V_m$; the two diode drops (≈1.4 V) are neglected under the ideal assumption, so the unfiltered output averages 45 V.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (31.8 V)**: the student uses the HALF-wave average $V_m/\pi$.
- **Option C trap (70.7 V)**: the student reports the PEAK value.
- **Option D trap (22.5 V)**: the student halves the full-wave average.
r""")

calc(T, "A full-wave rectifier with a capacitor filter supplies a load current of 100 mA. The line frequency is 50 Hz and the filter capacitor is 1000 µF. The approximate ripple voltage is:",
     ["1 V", "2 V", "0.5 V", "10 V"], 0,
       "Full-wave: $V_r = I_L/(2fC) = 0.1/(2\\times50\\times10^{-3}) = 1$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_L = 100$ mA $= 0.1$ A, $f = 50$ Hz, $C = 1000\ \mu F = 10^{-3}$ F.
Governing law — ripple of a full-wave rectifier with capacitor filter:
$$V_r = \frac{I_L}{2fC}$$

**Step 2: Full Mathematical Workings**
$$V_r = \frac{0.1}{2 \times 50 \times 10^{-3}}$$
$$2 \times 50 = 100$$
$$100 \times 10^{-3} = 0.1$$
$$V_r = \frac{0.1}{0.1}$$
$$V_r = 1\ V$$

**Step 3: Verification & Physical Interpretation**
The capacitor discharges for half a line period (10 ms) between peaks; 100 mA draining a 1000 µF capacitor for 10 ms drops it by $\Delta V = I\Delta t/C = 0.1 \times 0.01/10^{-3} = 1$ V — matching the formula. Note the ripple FREQUENCY is 100 Hz (2f), which halves the discharge time relative to half-wave.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (2 V)**: the student uses the HALF-wave formula ($I_L/fC$).
- **Option C trap (0.5 V)**: the student uses 200 Hz (or 2f for a 100 Hz line).
- **Option D trap (10 V)**: a factor-of-10 slip in the capacitance (100 µF).
r""")

theory(T, "Which list correctly ranks the three rectifier circuits by ripple factor (highest to lowest)?",
       ["Half-wave (121%), centre-tap full-wave (48%), bridge full-wave (48%)",
        "Bridge (121%), centre-tap (48%), half-wave (48%)",
        "All three have the same ripple factor",
        "Half-wave (48%), full-wave (121%)"], 0,
       "Half-wave ripple factor ≈ 1.21; both full-wave types ≈ 0.48.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
Ripple factor $\gamma = V_{r(rms)}/V_{DC}$: half-wave rectification leaves large gaps (γ ≈ 1.21, i.e. 121% of the DC value is AC ripple). Full-wave rectification (centre-tap OR bridge — they produce identical output waveforms) fills the negative half-cycles, cutting the ripple to γ ≈ 0.48.

**Step 2: Testing the Options**
- **Option A (correct)**: 121% then 48% then 48%.
- **Option B (wrong)**: attributes 121% to the bridge.
- **Option C (wrong)**: the waveforms are objectively different.
- **Option D (wrong)**: reverses the ranking.

**Step 3: Exam Trap Summary**
The trap is treating the bridge as "better" than the centre-tap for RIPPLE — they are electrically identical outputs (both full-wave). They differ only in PIV and diode count.
r""")

calc(T, "For the same load and capacitor, a full-wave rectifier's ripple is 1 V. If the circuit were changed to HALF-wave (same C, same load, same frequency), the ripple would become about:",
     ["2 V", "0.5 V", "1 V", "4 V"], 0,
       "Half-wave discharges for a FULL period (twice as long), so $V_r$ doubles: 2 V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Governing laws:
$$V_{r(HW)} = \frac{I_L}{fC} \qquad V_{r(FW)} = \frac{I_L}{2fC}$$
The half-wave capacitor must support the load for the FULL line period between peaks, exactly twice the full-wave discharge time.

**Step 2: Full Mathematical Workings**
$$\frac{V_{r(HW)}}{V_{r(FW)}} = \frac{I_L/(fC)}{I_L/(2fC)}$$
$$\frac{V_{r(HW)}}{V_{r(FW)}} = 2$$
$$V_{r(HW)} = 2 \times 1\ V = 2\ V$$

**Step 3: Verification & Physical Interpretation**
With only one peak per cycle, the capacitor discharges for 20 ms instead of 10 ms, losing twice the voltage. This is a major reason full-wave rectification is standard in power supplies.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.5 V)**: the student halves instead of doubles (thinking "full-wave is worse").
- **Option C trap (1 V)**: the student assumes ripple is independent of the rectifier type.
- **Option D trap (4 V)**: the student doubles twice (also changing the frequency term).
r""")

# =====================================================================
# TOPIC 3 — OPERATIONAL AMPLIFIERS
# =====================================================================
T = "eee252-opamp"

theory(T, "State the ideal op-amp assumptions and the resulting virtual-short rule.",
       ["Infinite open-loop gain, infinite input impedance, zero output impedance; with negative feedback v₊ = v₋ and i₊ = i₋ = 0",
        "Finite gain of 10, low input impedance, high output impedance; v₊ > v₋ always",
        "Unity gain, input currents set by the source, output depends on load",
        "Infinite gain only; the input currents are arbitrary"], 0,
       "Ideal: A→∞, R_in→∞, R_out = 0; with negative feedback the virtual short gives v₊ = v₋, i₊ = i₋ = 0.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
The ideal op-amp has: (1) infinite open-loop gain $A \to \infty$; (2) infinite input impedance (no input currents); (3) zero output impedance; (4) infinite bandwidth. Under NEGATIVE feedback, finite output requires $v_+ - v_- = v_o/A \to 0$, giving the VIRTUAL SHORT: $v_+ = v_-$, and since input impedance is infinite, $i_+ = i_- = 0$.

**Step 2: Testing the Options**
- **Option A (correct)**: the full set of ideal assumptions plus the virtual-short consequence.
- **Option B (wrong)**: those are non-ideal, low-quality characteristics.
- **Option C (wrong)**: the gain is infinite, not unity; input currents are zero.
- **Option D (wrong)**: incomplete — the input currents must be zero too.

**Step 3: Exam Trap Summary**
The virtual short requires NEGATIVE FEEDBACK — with positive feedback or open loop it does NOT apply. State that condition explicitly in every exam answer.
r""")

calc(T, "An inverting amplifier has $R_1 = 10$ kΩ (input) and $R_2 = 100$ kΩ (feedback). The closed-loop voltage gain is:",
     ["−10", "+10", "−11", "+11"], 0,
       "$A_v = -R_2/R_1 = -100/10 = -10$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $R_1 = 10$ kΩ, $R_2 = 100$ kΩ.
Governing law — inverting amplifier gain:
$$A_v = -\frac{R_2}{R_1}$$

**Step 2: Full Mathematical Workings**
$$A_v = -\frac{100\ k\Omega}{10\ k\Omega}$$
$$A_v = -\frac{100}{10}$$
$$A_v = -10$$

**Step 3: Verification & Physical Interpretation**
The inverting node is a virtual ground; the input current $v_i/10$k flows through the feedback resistor, producing $v_o = -100k \times v_i/10k = -10v_i$. The minus sign reflects the phase inversion of the inverting topology.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (+10)**: the student drops the minus sign — the #1 inverting-amplifier error.
- **Option C trap (−11)**: the student uses the NON-inverting formula $1 + R_2/R_1$.
- **Option D trap (+11)**: both errors combined.
r""")

calc(T, "A non-inverting amplifier uses $R_1 = 20$ kΩ (to ground) and $R_2 = 80$ kΩ (feedback). The gain is:",
     ["+5", "−5", "+4", "−4"], 0,
       "$A_v = 1 + R_2/R_1 = 1 + 80/20 = 5$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $R_1 = 20$ kΩ, $R_2 = 80$ kΩ.
Governing law — non-inverting amplifier:
$$A_v = 1 + \frac{R_2}{R_1}$$

**Step 2: Full Mathematical Workings**
$$A_v = 1 + \frac{80}{20}$$
$$A_v = 1 + 4$$
$$A_v = +5$$

**Step 3: Verification & Physical Interpretation**
The feedback divider feeds $v_- = v_o R_1/(R_1+R_2)$ back; the virtual short sets it equal to $v_i$: $v_i = v_o \times 20/100 \Rightarrow v_o = 5v_i$. Gain is positive (no inversion) and always ≥ 1.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (−5)**: the student applies the inverting sign convention.
- **Option C trap (+4)**: the student forgets the leading "1" (uses $R_2/R_1$ only).
- **Option D trap (−4)**: both errors.
r""")

calc(T, "A summing amplifier has $R_1 = 10$ kΩ, $R_2 = 20$ kΩ and feedback $R_f = 100$ kΩ. With $v_1 = 0.5$ V and $v_2 = 0.4$ V (both fed to the inverting node), the output is:",
     ["−7 V", "+7 V", "−5 V", "−3 V"], 0,
       "$v_o = -R_f(v_1/R_1 + v_2/R_2) = -100k(0.5/10k + 0.4/20k) = -(5 + 2) = -7$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $R_1 = 10$ kΩ, $R_2 = 20$ kΩ, $R_f = 100$ kΩ, $v_1 = 0.5$ V, $v_2 = 0.4$ V.
Governing law — inverting summing amplifier:
$$v_o = -R_f\left(\frac{v_1}{R_1} + \frac{v_2}{R_2}\right)$$

**Step 2: Full Mathematical Workings**
First term:
$$\frac{v_1}{R_1} = \frac{0.5}{10\ k} = 50\ \mu A$$
Second term:
$$\frac{v_2}{R_2} = \frac{0.4}{20\ k} = 20\ \mu A$$
Sum of input currents (virtual ground at the inverting node):
$$50 + 20 = 70\ \mu A$$
Output:
$$v_o = -100\ k \times 70\ \mu A$$
$$v_o = -7\ V$$

**Step 3: Verification & Physical Interpretation**
Each input contributes its own weighted gain ($-R_f/R_1 = -10$ and $-R_f/R_2 = -5$): $v_o = -10 \times 0.5 - 5 \times 0.4 = -5 - 2 = -7$ V. The summing junction performs a weighted average with inversion.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (+7 V)**: sign error.
- **Option C trap (−5 V)**: the student includes only the $v_1$ term.
- **Option D trap (−3 V)**: the student averages the gains wrongly (e.g. $(10+5)/2 \times 0.45$).
r""")

calc(T, "A difference amplifier has $R_1 = R_3 = 10$ kΩ and $R_2 = R_4 = 100$ kΩ. With $v_1 = 0.1$ V at the inverting input and $v_2 = 0.3$ V at the non-inverting input, the output is:",
     ["+2 V", "−2 V", "+4 V", "−4 V"], 0,
       "$v_o = (R_2/R_1)(v_2 - v_1) = 10 \\times 0.2 = +2$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $R_1 = R_3 = 10$ kΩ, $R_2 = R_4 = 100$ kΩ, $v_1 = 0.1$ V, $v_2 = 0.3$ V.
Governing law — difference amplifier with matched resistor ratios:
$$v_o = \frac{R_2}{R_1}(v_2 - v_1)$$

**Step 2: Full Mathematical Workings**
Differential gain:
$$\frac{R_2}{R_1} = \frac{100}{10} = 10$$
Input difference:
$$v_2 - v_1 = 0.3 - 0.1 = 0.2\ V$$
Output:
$$v_o = 10 \times 0.2$$
$$v_o = +2\ V$$

**Step 3: Verification & Physical Interpretation**
The non-inverting path divides $v_2$ by $R_3/(R_3+R_4) = 1/11$ and the inverting path superimposes; with matched pairs the result is the clean difference scaled by $R_2/R_1$. The output is positive because $v_2 > v_1$.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (−2 V)**: the student subtracts in the wrong order ($v_1 - v_2$).
- **Option C trap (+4 V)**: the student adds the inputs ($0.1 + 0.3 = 0.4$) before scaling.
- **Option D trap (−4 V)**: both errors.
r""")

theory(T, "Which transfer function belongs to a Miller (inverting) integrator built with input resistor R and feedback capacitor C?",
       ["$T(s) = -1/(sRC)$", "$T(s) = -sRC$", "$T(s) = 1 + sRC$", "$T(s) = -RC$"], 0,
       "Integrator: $v_o = -(1/RC)\\int v_i\\,dt$ ⇔ $T(s) = -1/(sRC)$ (a pole at the origin).",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
With the inverting node at virtual ground, $i_R = v_i/R$ flows into the feedback capacitor, so $v_o = -\frac{1}{C}\int i_R\,dt = -\frac{1}{RC}\int v_i\,dt$. In the s-domain (capacitor impedance $1/sC$):
$$T(s) = \frac{V_o}{V_i} = -\frac{1/(sC)}{R} = -\frac{1}{sRC}$$

**Step 2: Testing the Options**
- **Option A (correct)**: $-1/(sRC)$ — a pole at the origin, infinite DC gain.
- **Option B (wrong)**: $-sRC$ is the DIFFERENTIATOR.
- **Option C (wrong)**: $1 + sRC$ is a lead network, not an integrator.
- **Option D (wrong)**: a constant — no frequency dependence at all.

**Step 3: Exam Trap Summary**
Integrator ↔ differentiator reversal is the classic trap: integration ⇒ $1/s$ (pole at origin, passes DC infinitely), differentiation ⇒ $s$ (zero at origin, blocks DC). Also, the inverting integrator's sign is negative.
r""")

theory(T, "CMRR of an op-amp is defined as:",
       ["$CMRR = |A_d/A_{cm}|$, where $A_d$ is the differential gain and $A_{cm}$ the common-mode gain; often quoted as $20\\log_{10}CMRR$ dB",
        "$CMRR = A_d \\times A_{cm}$",
        "$CMRR = A_{cm}/A_d$",
        "$CMRR = A_d + A_{cm}$"], 0,
       "CMRR is the ratio of differential to common-mode gain; in dB: 20log₁₀(CMRR).",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
An op-amp amplifies the differential signal $v_d = v_+ - v_-$ with gain $A_d$ and, ideally, rejects the common-mode signal $v_{cm}$. The common-mode rejection ratio quantifies the rejection:
$$CMRR = \left|\frac{A_d}{A_{cm}}\right|$$
expressed in decibels as $CMRR_{dB} = 20\log_{10}(CMRR)$. Ideal op-amps have $A_{cm} = 0$ ⇒ infinite CMRR.

**Step 2: Testing the Options**
- **Option A (correct)**: the ratio with its dB form.
- **Option B (wrong)**: the product has no rejection meaning.
- **Option C (wrong)**: the reciprocal — it would BLOW UP for a good amplifier.
- **Option D (wrong)**: gains are ratios to be divided, not added.

**Step 3: Exam Trap Summary**
Two traps: inverting the ratio (it must be large for a GOOD amplifier) and forgetting the dB form uses $20\log_{10}$ (voltage gains), not $10\log_{10}$ (power).
r""")

calc(T, "An inverting op-amp circuit has feedback impedance formed by $R_2$ in parallel with capacitor C (from output to inverting node) and input resistor $R_L = 20$ kΩ. The low-frequency gain is −5 and the high-frequency gain is −3. The required $R_2$ and $R_3$ (where $R_3$ is in series with C inside the feedback branch) are:",
     ["$R_2 = 100$ kΩ, $R_3 = 150$ kΩ", "$R_2 = 60$ kΩ, $R_3 = 90$ kΩ", "$R_2 = 100$ kΩ, $R_3 = 100$ kΩ", "$R_2 = 150$ kΩ, $R_3 = 100$ kΩ"], 0,
       "DC: $R_2/R_L = 5$ ⇒ $R_2 = 100$ kΩ; HF: $(R_2\\parallel R_3)/R_L = 3$ ⇒ $R_3 = 150$ kΩ.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $R_L = 20$ kΩ (input resistor), $|A_{DC}| = 5$, $|A_{HF}| = 3$.
Circuit layout (textual): input $v_i$ → $R_L$ → inverting node; feedback branch from output to inverting node = $R_2$ in parallel with ($R_3$ in series with C).
Governing laws — inverting gain at the two extremes:
$$|A_{DC}| = \frac{R_2}{R_L} \qquad |A_{HF}| = \frac{R_2 \parallel R_3}{R_L}$$

**Step 2: Full Mathematical Workings**
Step A — at DC the capacitor is an open circuit, so only $R_2$ is in the feedback path:
$$\frac{R_2}{R_L} = 5$$
$$R_2 = 5 \times 20\ k\Omega = 100\ k\Omega$$
Step B — at high frequency the capacitor is a short, so $R_3$ appears in parallel with $R_2$:
$$\frac{R_2 \parallel R_3}{R_L} = 3$$
$$\frac{100k \times R_3}{100k + R_3} = 3 \times 20k = 60k$$
$$100k \times R_3 = 60k(100k + R_3)$$
$$100R_3 = 6000k + 60R_3$$
$$40R_3 = 6000k$$
$$R_3 = 150\ k\Omega$$

**Step 3: Verification & Physical Interpretation**
Checking: $R_2 \parallel R_3 = 100k \parallel 150k = \frac{100 \times 150}{250}k = 60$ kΩ, and $60/20 = 3$ — the high-frequency gain. The circuit is a lead-lag (shelving) amplifier: gain falls from 5 to 3 as the capacitor shorts $R_3$ at high frequency.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student scales both resistors by the wrong input resistance (12 kΩ).
- **Option C trap**: $R_2 = R_3$ would give HF gain $50/20 = 2.5$, not 3 — no parallel computation done.
- **Option D trap**: the student swaps $R_2$ and $R_3$ in the DC/HF roles.
r""")

theory(T, "For a second-order active filter with transfer function $T(s) = \\frac{K}{s^2/\\omega_0^2 + s/(Q\\omega_0) + 1}$, match the terms: (a) K (b) Q (c) $\\omega_0$.",
       ["DC (passband) gain; quality factor (sharpness of the peak); natural (pole) frequency",
        "corner frequency; gain; damping ratio",
        "quality factor; natural frequency; gain",
        "gain; natural frequency; quality factor"], 0,
       "K = passband gain, Q = quality factor, ω₀ = natural frequency.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
The standard second-order low-pass form is:
$$T(s) = \frac{K}{\frac{s^2}{\omega_0^2} + \frac{s}{Q\omega_0} + 1}$$
- $K$: the passband (low-frequency, $s \to 0$) gain.
- $\omega_0$: the natural (undamped) frequency — the location of the pole pair's radius.
- $Q$: the quality factor — the ratio $\omega_0/$bandwidth, measuring resonance sharpness ($Q = 0.707$ gives the maximally-flat Butterworth response).

**Step 2: Testing the Options**
- **Option A (correct)**: gain, Q, natural frequency.
- **Option B (wrong)**: mislabels all three.
- **Option C (wrong)**: scrambles the three labels.
- **Option D (wrong)**: swaps Q and $\omega_0$.

**Step 3: Exam Trap Summary**
The trap is reading Q and $\omega_0$ from the wrong coefficients. Always bring the denominator to the standard form with leading coefficient 1 and then read $\omega_0$ from the $s^2$ term and Q from the $s$ term: $Q = \omega_0/(\text{coefficient of } s)$.
r""")
