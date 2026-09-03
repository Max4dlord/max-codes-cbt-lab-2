# -*- coding: utf-8 -*-
r"""EEE 252 — PART B past questions, FILE B: MOSFETs, BJTs, Small-Signal.
Sources: OAU exams, Sedra problem sets 1, pre-class problems, Assignments.r"""

QUESTIONS_B = []

def calc(topic, q, opts, ans, short, sol):
    QUESTIONS_B.append(dict(topicId=topic, kind="calc", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

def theory(topic, q, opts, ans, short, sol):
    QUESTIONS_B.append(dict(topicId=topic, kind="theory", question=q, options=opts,
                            correct=ans, short=short, solution=sol))

# =====================================================================
# TOPIC 4 — MOSFETs & NMOS TECHNOLOGY
# =====================================================================
T = "eee252-mosfet"

theory(T, "State the two main types of MOSFET, and describe their structure and circuit symbols.",
       ["Enhancement type (normally OFF, needs a gate voltage to form the channel) and depletion type (channel exists at $V_{GS} = 0$); the symbol arrow points IN for NMOS and OUT for PMOS",
        "NPN and PNP types, with the arrow at the base",
        "Forward and reverse types, distinguished by the gate oxide colour",
        "Silicon and germanium types, with three and four terminals respectively"], 0,
       "MOSFETs are enhancement (normally-off) or depletion (normally-on); NMOS arrow points in, PMOS out.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
MOSFETs come in two structural types:
- ENHANCEMENT: no conducting channel at $V_{GS} = 0$ — a gate voltage above the threshold $V_t$ must INDUCE the channel (normally OFF). Cross-section: source and drain n⁺ regions separated by a p-substrate, with a thin oxide under the metal gate; the induced channel bridges source and drain.
- DEPLETION: a channel is implanted so the device conducts at $V_{GS} = 0$ and the gate voltage can deplete it (normally ON).
Circuit symbols: the arrow on the body/source terminal points INWARD (toward the channel) for NMOS and OUTWARD for PMOS; the depletion symbol has a solid channel bar, the enhancement symbol a broken bar.

**Step 2: Testing the Options**
- **Option A (correct)**: both types plus the arrow conventions.
- **Option B (wrong)**: NPN/PNP are BJT types, and BJTs have three terminals.
- **Option C (wrong)**: "forward/reverse" is not a MOSFET classification.
- **Option D (wrong)**: silicon/germanium is a material choice, not a structural type.

**Step 3: Exam Trap Summary**
The trap is the arrow direction and the "normally" state. Anchor: eNhancement = No channel initially; NMOS arrow iN. In the written exam, sketch both cross-sections showing the oxide and the induced channel.
r""")

calc(T, "A process technology has $L_{min} = 0.4$ µm, $t_{ox} = 8$ nm, $\\mu_n = 450$ cm²/V·s, $V_t = 0.7$ V and $\\varepsilon_{ox} = 3.45\\times10^{-11}$ F/m. The oxide capacitance per unit area $C_{ox}$ is:",
     ["4.31 fF/µm²", "0.431 fF/µm²", "43.1 fF/µm²", "8.63 fF/µm²"], 0,
       "$C_{ox} = \\varepsilon_{ox}/t_{ox} = 3.45\\times10^{-11}/(8\\times10^{-9}) = 4.31$ mF/m² = 4.31 fF/µm².",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $t_{ox} = 8$ nm $= 8 \times 10^{-9}$ m, $\varepsilon_{ox} = 3.45 \times 10^{-11}$ F/m.
Governing law:
$$C_{ox} = \frac{\varepsilon_{ox}}{t_{ox}}$$

**Step 2: Full Mathematical Workings**
$$C_{ox} = \frac{3.45 \times 10^{-11}}{8 \times 10^{-9}}$$
$$C_{ox} = 4.3125 \times 10^{-3}\ F/m^2 = 4.31\ mF/m^2$$
Convert to the standard unit (fF/µm²):
$$1\ \frac{F}{m^2} = \frac{10^{15}\ fF}{10^{12}\ \mu m^2} = 10^{3}\ fF/\mu m^2$$
$$C_{ox} = 4.31\ fF/\mu m^2$$

**Step 3: Verification & Physical Interpretation**
About 4.3 fF/µm² is a typical value for an 8 nm gate oxide — remember $C_{ox}$ grows as $t_{ox}$ shrinks (that is why modern processes scale the oxide down).

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.431)**: a factor-of-10 error in $t_{ox}$ (80 nm) or the unit conversion.
- **Option C trap (43.1)**: the student treats $t_{ox}$ as 0.8 nm.
- **Option D trap (8.63)**: the student divides by $t_{ox}^2$ or doubles $\varepsilon_{ox}$.
r""")

calc(T, "For the same process ($C_{ox} = 4.31$ fF/µm², $\\mu_n = 450$ cm²/V·s), the process transconductance parameter $k'_n = \\mu_n C_{ox}$ is:",
     ["194 µA/V²", "19.4 µA/V²", "1.94 mA/V²", "97 µA/V²"], 0,
       "$k'_n = \\mu_n C_{ox} = 0.045 \\times 4.3125\\times10^{-3} = 1.94\\times10^{-4}$ A/V² = 194 µA/V².",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $\mu_n = 450$ cm²/V·s $= 450 \times 10^{-4}$ m²/V·s $= 0.045$ m²/V·s, $C_{ox} = 4.3125 \times 10^{-3}$ F/m².
Governing law:
$$k'_n = \mu_n C_{ox}$$

**Step 2: Full Mathematical Workings**
$$k'_n = 0.045 \times 4.3125 \times 10^{-3}$$
$$0.045 \times 4.3125 = 0.19406$$
$$k'_n = 0.19406 \times 10^{-3}$$
$$k'_n = 1.94 \times 10^{-4}\ A/V^2 = 194\ \mu A/V^2$$

**Step 3: Verification & Physical Interpretation**
194 µA/V² is a textbook-typical value for a 0.4 µm technology. The device parameter for a given geometry follows as $k_n = k'_n (W/L)$.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (19.4)**: the student forgets the cm²→m² conversion (divides by 10 again).
- **Option C trap (1.94 mA/V²)**: the student keeps $C_{ox}$ in F/cm² without converting.
- **Option D trap (97)**: the student halves $\mu_n$ (thinks in terms of hole mobility).
r""")

calc(T, "A MOSFET in this process has $W/L = 8$ µm/0.8 µm (so $k_n = k'_n(W/L)$ with $k'_n = 194$ µA/V²) and $V_t = 0.7$ V. To operate in saturation at $I_D = 100$ µA, the required overdrive voltage $V_{OV}$ is:",
     ["0.321 V", "0.226 V", "0.103 V", "0.454 V"], 0,
       "$k_n = 194\\mu \\times 10 = 1.94$ mA/V²; $V_{OV} = \\sqrt{2I_D/k_n} = \\sqrt{2\\times100\\mu/1.94m} = 0.321$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $W/L = 8/0.8 = 10$, $k'_n = 194$ µA/V², $I_D = 100$ µA, $V_t = 0.7$ V.
Governing laws:
$$k_n = k'_n\frac{W}{L} \qquad I_D = \frac{1}{2}k_n V_{OV}^2$$

**Step 2: Full Mathematical Workings**
Step A — device parameter:
$$k_n = 194 \times 10^{-6} \times \frac{8}{0.8}$$
$$k_n = 194 \times 10^{-6} \times 10$$
$$k_n = 1.94 \times 10^{-3}\ A/V^2$$
Step B — solve the saturation equation for the overdrive:
$$V_{OV} = \sqrt{\frac{2I_D}{k_n}}$$
$$V_{OV} = \sqrt{\frac{2 \times 100 \times 10^{-6}}{1.94 \times 10^{-3}}}$$
$$V_{OV} = \sqrt{0.10309}$$
$$V_{OV} = 0.321\ V$$

**Step 3: Verification & Physical Interpretation**
Checking: $I_D = \frac{1}{2} \times 1.94\text{m} \times 0.321^2 = 0.97\text{m} \times 0.103 = 100$ µA — exact. The overdrive of 0.32 V is the "excess" gate voltage above threshold that sets the channel current.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.226 V)**: the student forgets the factor 2 inside the square root.
- **Option C trap (0.103 V)**: the student reports $V_{OV}^2$ instead of taking the root.
- **Option D trap (0.454 V)**: the student uses $k_n = k'_n$ (forgets W/L = 10).
r""")

calc(T, "For the same device ($I_D = 100$ µA, $V_{OV} = 0.321$ V, $V_t = 0.7$ V), the required $V_{GS}$ and the minimum $V_{DS}$ for saturation are:",
     ["$V_{GS} = 1.021$ V, $V_{DS(min)} = 0.321$ V", "$V_{GS} = 1.021$ V, $V_{DS(min)} = 0.7$ V", "$V_{GS} = 0.321$ V, $V_{DS(min)} = 1.021$ V", "$V_{GS} = 1.4$ V, $V_{DS(min)} = 0.7$ V"], 0,
       "$V_{GS} = V_t + V_{OV} = 0.7 + 0.321 = 1.021$ V; saturation needs $V_{DS} \\ge V_{OV} = 0.321$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_t = 0.7$ V, $V_{OV} = 0.321$ V.
Governing laws:
$$V_{GS} = V_t + V_{OV} \qquad V_{DS(min)} = V_{OV}$$

**Step 2: Full Mathematical Workings**
$$V_{GS} = 0.7 + 0.321$$
$$V_{GS} = 1.021\ V$$
$$V_{DS(min)} = V_{OV} = 0.321\ V$$

**Step 3: Verification & Physical Interpretation**
The saturation boundary is the pinch-off condition $V_{DS} = V_{GS} - V_t = V_{OV}$: at 0.321 V of drain voltage the channel just pinches off. The gate needs 1.021 V — the threshold plus the overdrive needed for 100 µA.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student confuses $V_{DS(min)}$ with $V_t$ (pinch-off needs $V_{OV}$, not $V_t$).
- **Option C trap**: the student swaps $V_{GS}$ and $V_{DS(min)}$.
- **Option D trap**: the student takes $V_{OV} = 0.7$ V (forgets the calculation).
r""")

calc(T, "For the same device ($k_n = 1.94$ mA/V², $V_t = 0.7$ V), find $V_{OV}$ and $V_{GS}$ required for the MOSFET to operate as a 1000 Ω resistor for a very small $V_{DS}$.",
     ["$V_{OV} = 0.515$ V, $V_{GS} = 1.215$ V", "$V_{OV} = 0.515$ V, $V_{GS} = 0.515$ V", "$V_{OV} = 1.94$ V, $V_{GS} = 2.64$ V", "$V_{OV} = 0.258$ V, $V_{GS} = 0.958$ V"], 0,
       "Triode region: $r_{DS} = 1/(k_n V_{OV})$ ⇒ $V_{OV} = 1/(1.94m \\times 1000) = 0.515$ V; $V_{GS} = 1.215$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $k_n = 1.94$ mA/V², $V_t = 0.7$ V, target resistance $r_{DS} = 1000$ Ω at very small $V_{DS}$.
Governing law — triode-region channel resistance for $V_{DS} \ll V_{OV}$:
$$r_{DS} = \frac{1}{k_n(V_{GS} - V_t)} = \frac{1}{k_n V_{OV}}$$

**Step 2: Full Mathematical Workings**
Solve for the overdrive:
$$V_{OV} = \frac{1}{k_n r_{DS}}$$
$$V_{OV} = \frac{1}{1.94 \times 10^{-3} \times 1000}$$
$$V_{OV} = \frac{1}{1.94}$$
$$V_{OV} = 0.5155\ V \approx 0.515\ V$$
Gate voltage:
$$V_{GS} = V_t + V_{OV}$$
$$V_{GS} = 0.7 + 0.5155$$
$$V_{GS} = 1.2155\ V \approx 1.215\ V$$

**Step 3: Verification & Physical Interpretation**
In deep triode ($V_{DS} \to 0$) the channel is a linear resistor controlled by the gate. Checking: $1/(1.94m \times 0.5155) = 1000$ Ω — exact. This is how MOSFETs implement tunable resistances and switches in IC design.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student equates $V_{GS}$ with $V_{OV}$, forgetting to add $V_t$.
- **Option C trap**: the student uses $V_{OV} = k_n$ numerically (unit confusion) and adds wrongly.
- **Option D trap**: the student uses $r_{DS} = 2/(k_n V_{OV})$ (a factor-2 slip from the saturation formula).
r""")

calc(T, "A common-source amplifier operated from $V_{DD} = 2$ V has a maximum small-signal gain magnitude of 14 V/V. The overdrive voltage $V_{OV}$ at which the transistor operates is:",
     ["0.25 V", "0.143 V", "0.5 V", "0.125 V"], 0,
       "$|A_v|_{max} = 2(V_{DD}-V_{OV})/V_{OV}$ ⇒ $14 = 2(2-V_{OV})/V_{OV}$ ⇒ $V_{OV} = 0.25$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{DD} = 2$ V, $|A_v|_{max} = 14$.
Governing law — CS gain with a resistive load, $A_v = -g_m R_D$, expressed through the bias point:
$$|A_v| = \frac{2(V_{DD} - V_{DS})}{V_{OV}}$$
The MAXIMUM gain occurs at the edge of saturation, $V_{DS} = V_{OV}$:
$$|A_v|_{max} = \frac{2(V_{DD} - V_{OV})}{V_{OV}}$$

**Step 2: Full Mathematical Workings**
$$14 = \frac{2(2 - V_{OV})}{V_{OV}}$$
Multiply through by $V_{OV}$:
$$14V_{OV} = 4 - 2V_{OV}$$
$$14V_{OV} + 2V_{OV} = 4$$
$$16V_{OV} = 4$$
$$V_{OV} = \frac{4}{16}$$
$$V_{OV} = 0.25\ V$$

**Step 3: Verification & Physical Interpretation**
Checking: $|A_v|_{max} = 2(2 - 0.25)/0.25 = 3.5/0.25 = 14$ — exact. Biasing at the edge of saturation maximises $R_D$ while keeping the transistor in saturation, hence the maximum gain.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.143 V)**: the student uses $|A_v|_{max} = V_{DD}/V_{OV}$ (missing the factor 2 and the $V_{OV}$ in the numerator).
- **Option C trap (0.5 V)**: the student uses $|A_v|_{max} = 2V_{DD}/V_{OV}$ without subtracting $V_{OV}$.
- **Option D trap (0.125 V)**: the student misplaces a factor of 2 (uses 32 in the denominator).
r""")

calc(T, "In the same amplifier ($V_{DD} = 2$ V, $V_{OV} = 0.25$ V), the bias point Q at which a gain of −12 V/V is obtained has:",
     ["$V_{DS} = 0.5$ V", "$V_{DS} = 0.25$ V", "$V_{DS} = 1.0$ V", "$V_{DS} = 0.75$ V"], 0,
       "$|A_v| = 2(V_{DD}-V_{DS})/V_{OV}$ ⇒ $12 = 2(2-V_{DS})/0.25$ ⇒ $V_{DS} = 0.5$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{DD} = 2$ V, $V_{OV} = 0.25$ V, target $|A_v| = 12$.
Governing law:
$$|A_v| = \frac{2(V_{DD} - V_{DS})}{V_{OV}}$$

**Step 2: Full Mathematical Workings**
$$12 = \frac{2(2 - V_{DS})}{0.25}$$
$$12 \times 0.25 = 2(2 - V_{DS})$$
$$3 = 4 - 2V_{DS}$$
$$2V_{DS} = 4 - 3$$
$$2V_{DS} = 1$$
$$V_{DS} = 0.5\ V$$

**Step 3: Verification & Physical Interpretation**
At $V_{DS} = 0.5$ V (comfortably above $V_{OV} = 0.25$ V, so saturation holds), the gain drops from its 14 V/V maximum to 12 V/V because the larger $V_{DS}$ forces a smaller $R_D$ for the same current. The gain is thus a linear function of the bias point's drain voltage.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.25 V)**: the student reuses $V_{OV}$ — that would be the MAXIMUM-gain point (14 V/V), not 12.
- **Option C trap (1.0 V)**: the student solves $12 = 2V_{DS}/0.25$ incorrectly.
- **Option D trap (0.75 V)**: an arithmetic slip in rearranging $3 = 4 - 2V_{DS}$.
r""")

calc(T, "An NMOS transistor has $k_n = 10$ mA/V² and is biased at $V_{OV} = 0.2$ V. The DC bias current $I_D$ is:",
     ["0.2 mA", "0.4 mA", "0.1 mA", "2 mA"], 0,
       "$I_D = \\frac{1}{2}k_n V_{OV}^2 = 0.5 \\times 10m \\times 0.04 = 0.2$ mA.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $k_n = 10$ mA/V², $V_{OV} = 0.2$ V.
Governing law:
$$I_D = \frac{1}{2}k_n V_{OV}^2$$

**Step 2: Full Mathematical Workings**
$$V_{OV}^2 = 0.2 \times 0.2 = 0.04$$
$$\frac{1}{2}k_n = \frac{10}{2} = 5\ mA/V^2$$
$$I_D = 5 \times 0.04$$
$$I_D = 0.2\ mA$$

**Step 3: Verification & Physical Interpretation**
0.2 mA of drain current for a 0.2 V overdrive — the square law in action. Doubling $V_{OV}$ would QUADRUPLE the current.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.4 mA)**: the student forgets the ½ in the saturation formula.
- **Option C trap (0.1 mA)**: the student squares the half instead of $V_{OV}$.
- **Option D trap (2 mA)**: the student uses $I_D = k_n V_{OV}$ with a decimal slip.
r""")

calc(T, "For the same transistor ($k_n = 10$ mA/V², $V_{OV} = 0.2$ V), a +0.02 V signal is superimposed on $V_{GS}$. The increment in drain current (total current minus DC bias) is:",
     ["+0.042 mA", "+0.02 mA", "+0.002 mA", "+0.2 mA"], 0,
       "Total $i_D = \\frac{1}{2}k_n(V_{OV}+v_{gs})^2 = 5m \\times 0.22^2 = 0.242$ mA; increment = 0.242 − 0.2 = +0.042 mA.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $k_n = 10$ mA/V², $V_{OV} = 0.2$ V, signal $v_{gs} = +0.02$ V.
Governing law — the total instantaneous drain current:
$$i_D = \frac{1}{2}k_n(V_{OV} + v_{gs})^2$$

**Step 2: Full Mathematical Workings**
Step A — total current with the signal:
$$i_D = 5 \times (0.2 + 0.02)^2$$
$$0.2 + 0.02 = 0.22$$
$$0.22^2 = 0.0484$$
$$i_D = 5 \times 0.0484$$
$$i_D = 0.242\ mA$$
Step B — subtract the DC bias current $I_D = 0.2$ mA:
$$\Delta i_D = 0.242 - 0.2$$
$$\Delta i_D = +0.042\ mA$$

**Step 3: Verification & Physical Interpretation**
The square law makes the response slightly asymmetric: the positive half-cycle adds +0.042 mA. (For a −0.02 V signal the decrement would be −0.038 mA — see next question.) This asymmetry IS the nonlinear distortion the small-signal model neglects.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (+0.02 mA)**: the student linearises with the WRONG $g_m$ (1 mA/V instead of 2).
- **Option C trap (+0.002 mA)**: a factor-of-10 slip in $k_n$.
- **Option D trap (+0.2 mA)**: the student reports the DC current itself.
r""")

calc(T, "The average of the +0.02 V and −0.02 V current increments (0.042 mA and 0.038 mA) divided by the total 0.04 V signal swing estimates $g_m$ as:",
     ["2.0 mA/V, matching $g_m = k_n V_{OV}$ exactly", "1.0 mA/V, half the true value", "4.0 mA/V, double the true value", "0.5 mA/V"], 0,
       "$g_m \\approx (0.042+0.038)/0.04 = 2.0$ mA/V $= k_n V_{OV} = 10m \\times 0.2$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: positive increment 0.042 mA (for +0.02 V), negative decrement 0.038 mA (for −0.02 V), total swing 0.04 V.
Governing law — finite-difference estimate of transconductance and the analytic formula:
$$g_m \approx \frac{\Delta i_D}{\Delta v_{GS}} \qquad g_m = k_n V_{OV}$$

**Step 2: Full Mathematical Workings**
Total current change over the full swing:
$$\Delta i_D = 0.042 + 0.038 = 0.080\ mA$$
Voltage swing:
$$\Delta v_{GS} = 0.02 - (-0.02) = 0.04\ V$$
Estimate:
$$g_m = \frac{0.080}{0.04}$$
$$g_m = 2.0\ mA/V$$
Analytic check:
$$g_m = k_n V_{OV} = 10 \times 0.2$$
$$g_m = 2.0\ mA/V$$

**Step 3: Verification & Physical Interpretation**
The chord-slope estimate equals the tangent-slope formula exactly for a pure square law — a satisfying confirmation that the small-signal model ($i_d = g_m v_{gs}$) is the linearisation of the square law about Q.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (1.0 mA/V)**: the student uses only ONE increment over the full swing.
- **Option C trap (4.0 mA/V)**: the student divides by 0.02 instead of 0.04.
- **Option D trap (0.5 mA/V)**: the student inverts the slope.
r""")

calc(T, "A sine wave $v_{gs} = V_{gs}\\sin\\omega t$ drives a square-law MOSFET amplifier. Using $\\sin^2\\theta = \\frac{1}{2} - \\frac{1}{2}\\cos 2\\theta$, the second-harmonic distortion ratio (2ω component ÷ ω component) is:",
     ["$V_{gs}/(4V_{OV})$", "$V_{gs}/(2V_{OV})$", "$V_{gs}^2/(4V_{OV}^2)$", "$V_{OV}/(4V_{gs})$"], 0,
       "The $v_{gs}^2$ term produces the 2ω component $\\frac{1}{4}k_nV_{gs}^2\\cos2\\omega t$; dividing by the fundamental $k_nV_{OV}V_{gs}\\sin\\omega t$ gives $V_{gs}/(4V_{OV})$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Governing law — total drain current with the sine drive:
$$i_D = \frac{1}{2}k_n(V_{OV} + V_{gs}\sin\omega t)^2$$

**Step 2: Full Mathematical Workings**
Expand the square:
$$i_D = \frac{1}{2}k_n\left(V_{OV}^2 + 2V_{OV}V_{gs}\sin\omega t + V_{gs}^2\sin^2\omega t\right)$$
Apply the trigonometric identity to the last term:
$$\sin^2\omega t = \frac{1}{2} - \frac{1}{2}\cos 2\omega t$$
$$i_D = \frac{1}{2}k_nV_{OV}^2 + k_nV_{OV}V_{gs}\sin\omega t + \frac{1}{4}k_nV_{gs}^2 - \frac{1}{4}k_nV_{gs}^2\cos 2\omega t$$
Identify the fundamental (ω) component and the second-harmonic (2ω) component:
$$\text{fundamental} = k_nV_{OV}V_{gs} \qquad \text{second harmonic} = \frac{1}{4}k_nV_{gs}^2$$
Ratio:
$$\text{HD}_2 = \frac{\frac{1}{4}k_nV_{gs}^2}{k_nV_{OV}V_{gs}}$$
$$\text{HD}_2 = \frac{V_{gs}}{4V_{OV}}$$

**Step 3: Verification & Physical Interpretation**
The distortion grows linearly with the signal amplitude and inversely with the overdrive — biasing DEEPER into saturation (larger $V_{OV}$) makes the amplifier more linear.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student loses the factor 2 from the $2V_{OV}V_{gs}$ cross-term.
- **Option C trap**: the student does not cancel $V_{gs}$ (ratio of powers, not amplitudes).
- **Option D trap**: the student inverts the ratio.
r""")

calc(T, "For the second-harmonic distortion to stay below 1% with $V_{gs} = 10$ mV, the minimum overdrive voltage is:",
     ["0.25 V", "0.1 V", "1.0 V", "0.4 V"], 0,
       "$V_{gs}/(4V_{OV}) < 0.01$ ⇒ $V_{OV} > 10\\text{mV}/(4\\times0.01) = 0.25$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{gs} = 10$ mV, distortion limit 1%.
Governing law:
$$\text{HD}_2 = \frac{V_{gs}}{4V_{OV}}$$

**Step 2: Full Mathematical Workings**
Require:
$$\frac{V_{gs}}{4V_{OV}} < 0.01$$
$$\frac{0.010}{4V_{OV}} < 0.01$$
$$4V_{OV} > \frac{0.010}{0.01}$$
$$4V_{OV} > 1$$
$$V_{OV} > 0.25\ V$$

**Step 3: Verification & Physical Interpretation**
Biasing at $V_{OV} \ge 0.25$ V keeps the second harmonic at or below 1% — a 25:1 ratio between bias overdrive and signal amplitude. This is the standard "small-signal is small" criterion for square-law devices.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.1 V)**: the student uses 2.5% as the limit (drops a factor of 4).
- **Option C trap (1.0 V)**: the student uses $V_{gs}/(2V_{OV})$ and flips a factor.
- **Option D trap (0.4 V)**: arithmetic slip on $0.01 \times 4 \times 0.01$.
r""")

calc(T, "A common-source amplifier with $g_m = 2$ mA/V and $R_D = 10$ kΩ is fed from a 1 MΩ source and drives a 10 kΩ load. The overall voltage gain $G_v$ is:",
     ["−10 V/V", "−20 V/V", "−5 V/V", "−15 V/V"], 0,
       "MOSFET input resistance is infinite, so $G_v = -g_m(R_D\\parallel R_L) = -2m \\times 5k = -10$ V/V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $g_m = 2$ mA/V, $R_D = 10$ kΩ, $R_{sig} = 1$ MΩ, $R_L = 10$ kΩ.
Governing law — overall gain of a CS amplifier:
$$G_v = \frac{R_{in}}{R_{in} + R_{sig}} \times \left[-g_m(R_D \parallel R_L)\right]$$

**Step 2: Full Mathematical Workings**
Step A — input resistance of a MOSFET gate is infinite, so the source-divider factor is unity:
$$\frac{R_{in}}{R_{in} + R_{sig}} = \frac{\infty}{\infty + 1M} = 1$$
Step B — load on the drain:
$$R_D \parallel R_L = \frac{10 \times 10}{10 + 10} = \frac{100}{20} = 5\ k\Omega$$
Step C — gain:
$$G_v = -2 \times 10^{-3} \times 5 \times 10^{3}$$
$$G_v = -10\ V/V$$

**Step 3: Verification & Physical Interpretation**
The MOSFET's infinite input resistance is its great advantage: a 1 MΩ source loses nothing at the input, unlike a BJT stage. The gain is set purely by $g_m$ and the drain load.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (−20)**: the student forgets the load $R_L$ (uses $R_D$ alone).
- **Option C trap (−5)**: the student divides by 2 twice or uses $g_m = 1$ mA/V.
- **Option D trap (−15)**: the student adds $R_D$ and $R_L$ instead of paralleling.
r""")

calc(T, "A common-source amplifier operates at $V_{OV} = 0.25$ V and must deliver an overall gain of −10 V/V into $R_L = 15$ kΩ, with the designer choosing $R_D = 2R_L = 30$ kΩ. The required $g_m$ and bias current $I_D$ are:",
     ["$g_m = 1$ mA/V, $I_D = 0.125$ mA", "$g_m = 2$ mA/V, $I_D = 0.25$ mA", "$g_m = 0.5$ mA/V, $I_D = 0.0625$ mA", "$g_m = 1$ mA/V, $I_D = 0.5$ mA"], 0,
       "$R_D\\parallel R_L = 30\\parallel15 = 10$ kΩ; $g_m = 10/10k = 1$ mA/V; $I_D = \\frac{1}{2}g_m V_{OV} = 0.5\\times1m\\times0.25 = 0.125$ mA.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{OV} = 0.25$ V, $|G_v| = 10$, $R_L = 15$ kΩ, $R_D = 2R_L = 30$ kΩ.
Governing laws:
$$|G_v| = g_m(R_D \parallel R_L) \qquad g_m = \frac{2I_D}{V_{OV}}$$

**Step 2: Full Mathematical Workings**
Step A — parallel load:
$$R_D \parallel R_L = \frac{30 \times 15}{30 + 15} = \frac{450}{45} = 10\ k\Omega$$
Step B — required transconductance:
$$g_m = \frac{10}{10\ k\Omega} = 1\ mA/V$$
Step C — bias current:
$$I_D = \frac{1}{2}g_m V_{OV}$$
$$I_D = \frac{1}{2} \times 1 \times 10^{-3} \times 0.25$$
$$I_D = 0.125\ mA$$

**Step 3: Verification & Physical Interpretation**
With the drain resistance fixed at twice the load, the parallel combination is 10 kΩ, so 1 mA/V of transconductance achieves the gain with a modest 0.125 mA of bias current.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student computes $I_D = g_m V_{OV}$ (forgets the ½).
- **Option C trap**: the student uses $R_D$ alone (30 kΩ) in the gain equation.
- **Option D trap**: the student computes $I_D = g_m V_{OV} \times 2$.
r""")

calc(T, "In the same amplifier ($g_m = 1$ mA/V, $R_L = 15$ kΩ), if $R_D$ is REDUCED to equal $R_L$ (15 kΩ) to increase the output swing, the new overall gain becomes:",
     ["−7.5 V/V", "−15 V/V", "−5 V/V", "−10 V/V"], 0,
       "$G_v = -g_m(R_D\\parallel R_L) = -1m \\times 7.5k = -7.5$ V/V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $g_m = 1$ mA/V, $R_D = R_L = 15$ kΩ.
Governing law:
$$G_v = -g_m(R_D \parallel R_L)$$

**Step 2: Full Mathematical Workings**
$$R_D \parallel R_L = \frac{15 \times 15}{15 + 15} = \frac{225}{30} = 7.5\ k\Omega$$
$$G_v = -1 \times 10^{-3} \times 7.5 \times 10^{3}$$
$$G_v = -7.5\ V/V$$

**Step 3: Verification & Physical Interpretation**
Halving $R_D$ from 30 kΩ to 15 kΩ reduces the parallel load from 10 kΩ to 7.5 kΩ — the gain falls by the same 25%. This is the classic gain-vs-swing trade-off: larger $R_D$ gives more gain but less headroom.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (−15)**: the student forgets the load resistance again.
- **Option C trap (−5)**: the student uses $\frac{1}{3}$ of the parallel value.
- **Option D trap (−10)**: the student reuses the old gain without recomputing.
r""")

calc(T, "Two identical CS amplifiers are cascaded; each stage has $I_D = 0.3$ mA, $V_{OV} = 0.2$ V and $R_D = 10$ kΩ. The source resistance is 200 kΩ and the final load is 10 kΩ. The overall gain $G_v$ is:",
     ["+450 V/V", "−450 V/V", "+225 V/V", "+900 V/V"], 0,
       "Each stage: $g_m = 2\\times0.3m/0.2 = 3$ mA/V; stage 1: −30 (no load, infinite gate input); stage 2: $-3m\\times5k = -15$; total $= (-30)(-15) = +450$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_D = 0.3$ mA, $V_{OV} = 0.2$ V, $R_D = 10$ kΩ per stage, $R_{sig} = 200$ kΩ, $R_L = 10$ kΩ.
Governing laws:
$$g_m = \frac{2I_D}{V_{OV}} \qquad A_{v} = -g_m(R_D \parallel R_{in,next})$$

**Step 2: Full Mathematical Workings**
Step A — per-stage transconductance:
$$g_m = \frac{2 \times 0.3 \times 10^{-3}}{0.2} = 3\ mA/V$$
Step B — first stage: its "load" is the second stage's GATE (infinite input resistance), and the MOSFET gate draws nothing from the source:
$$A_{v1} = -3m \times 10k = -30\ V/V$$
Step C — second stage: its drain sees $R_D \parallel R_L$:
$$R_D \parallel R_L = \frac{10 \times 10}{20} = 5\ k\Omega$$
$$A_{v2} = -3m \times 5k = -15\ V/V$$
Step D — cascade:
$$G_v = A_{v1} \times A_{v2}$$
$$G_v = (-30)(-15)$$
$$G_v = +450\ V/V$$

**Step 3: Verification & Physical Interpretation**
Two inverting stages in cascade give a NON-inverting overall response (+450). Because each MOSFET gate presents an open circuit, there is no interstage loading loss — a major advantage over BJT cascades.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (−450)**: the student forgets that two inversions cancel.
- **Option C trap (+225)**: the student loads the first stage with $R_D\parallel R_L$ too.
- **Option D trap (+900)**: the student uses $g_m = 6$ mA/V (forgets the ½ factor... uses $I_D/V_{OV}$).
r""")

calc(T, "An amplifier replaces its load resistor with a second NMOS (Q2) connected as a two-terminal device ($v_{DG} = 0$, always in saturation). With equal thresholds $V_{t1} = V_{t2} = V_t$ and equal currents $i_{D1} = i_{D2}$, the output voltage for Q1 in saturation is:",
     ["$v_O = V_{DD} - V_t - \\sqrt{(W/L)_1/(W/L)_2}\\,(v_I - V_t)$",
      "$v_O = V_{DD} - V_t + \\sqrt{(W/L)_2/(W/L)_1}\\,(v_I - V_t)$",
      "$v_O = (W/L)_1/(W/L)_2 \\times v_I$",
      "$v_O = V_{DD} - v_I$"], 0,
       "Equating $\\frac{1}{2}k'_n(W/L)_1(v_I-V_t)^2 = \\frac{1}{2}k'_n(W/L)_2(V_{DD}-v_O-V_t)^2$ and taking square roots gives the linear relation with gain $-\\sqrt{(W/L)_1/(W/L)_2}$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Schematic layout (textual): $V_{DD}$ connects to the DRAIN of load device Q2; Q2's gate and drain are TIED together (two-terminal connection), so $V_{SG2} = V_{DG2} = 0$ relative to its own source — Q2's source is the output node. Q1's drain is the output node, its source is ground, and its gate is driven by $v_I$.
Governing law — saturation currents:
$$i_{D1} = \frac{1}{2}k'_n\left(\frac{W}{L}\right)_1(v_I - V_t)^2 \qquad i_{D2} = \frac{1}{2}k'_n\left(\frac{W}{L}\right)_2(V_{DD} - v_O - V_t)^2$$

**Step 2: Full Mathematical Workings**
Equal currents:
$$\frac{1}{2}k'_n\left(\frac{W}{L}\right)_1(v_I - V_t)^2 = \frac{1}{2}k'_n\left(\frac{W}{L}\right)_2(V_{DD} - v_O - V_t)^2$$
Cancel $\frac{1}{2}k'_n$ and take the positive square root of both sides:
$$\sqrt{\left(\frac{W}{L}\right)_1}\,(v_I - V_t) = \sqrt{\left(\frac{W}{L}\right)_2}\,(V_{DD} - v_O - V_t)$$
Divide through by $\sqrt{(W/L)_2}$:
$$V_{DD} - v_O - V_t = \sqrt{\frac{(W/L)_1}{(W/L)_2}}\,(v_I - V_t)$$
Solve for $v_O$:
$$v_O = V_{DD} - V_t - \sqrt{\frac{(W/L)_1}{(W/L)_2}}\,(v_I - V_t)$$

**Step 3: Verification & Physical Interpretation**
The active (MOSFET) load acts like a current source with a square-law I-V, yet the equal-current constraint makes the transfer LINEAR — the amplifier is linear even for large signals, with gain $-\sqrt{(W/L)_1/(W/L)_2}$.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the ratio under the root is inverted and the sign wrong.
- **Option C trap**: the student neglects the $V_{DD}$ and $V_t$ offsets (assumes a pure resistive divider).
- **Option D trap**: the student ignores the device geometry entirely.
r""")

calc(T, "For the same active-load amplifier with $(W/L)_1 = 50$ µm/0.5 µm and $(W/L)_2 = 5$ µm/0.5 µm, the voltage gain is:",
     ["−3.16 V/V", "−10 V/V", "+3.16 V/V", "−7.07 V/V"], 0,
       "$A_v = -\\sqrt{(W/L)_1/(W/L)_2} = -\\sqrt{10} = -3.16$ V/V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $(W/L)_1 = 50/0.5 = 100$, $(W/L)_2 = 5/0.5 = 10$.
Governing law:
$$A_v = -\sqrt{\frac{(W/L)_1}{(W/L)_2}}$$

**Step 2: Full Mathematical Workings**
Ratio of geometries:
$$\frac{(W/L)_1}{(W/L)_2} = \frac{100}{10} = 10$$
Gain:
$$A_v = -\sqrt{10}$$
$$A_v = -3.162\ V/V$$

**Step 3: Verification & Physical Interpretation**
The gain is set purely by the geometry RATIO — process and temperature variations cancel out, which is why active-load amplifiers are preferred in IC design. The wide Q1 and narrow Q2 give a gain of about −3.16.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (−10)**: the student forgets the square root (uses the ratio directly).
- **Option C trap (+3.16)**: sign error — the CS stage inverts.
- **Option D trap (−7.07)**: the student roots the wrong ratio ($\sqrt{50}$).
r""")

calc(T, "A MOSFET amplifier (Fig. Q3a: $V_{DD} = 10$ V → $R_D = 10$ kΩ → drain; gate driven by $V_i$; source grounded) has $k = 2.5$ mA/V² and $V_t = 0.6$ V. To obtain a DC output $V_{out} = 5$ V in saturation, the DC input voltage $V_i$ is:",
     ["1.23 V", "0.63 V", "1.63 V", "2.23 V"], 0,
       "$I_D = (10-5)/10k = 0.5$ mA; $V_{OV} = \\sqrt{2I_D/k} = \\sqrt{0.4} = 0.632$ V; $V_i = V_{GS} = 0.6 + 0.632 = 1.232$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{DD} = 10$ V, $R_D = 10$ kΩ, $V_{out} = 5$ V, $k = 2.5$ mA/V², $V_t = 0.6$ V.
Governing laws:
$$I_D = \frac{V_{DD} - V_{out}}{R_D} \qquad I_D = \frac{1}{2}k(V_{GS} - V_t)^2$$

**Step 2: Full Mathematical Workings**
Step A — drain current from the output condition:
$$I_D = \frac{10 - 5}{10 \times 10^{3}}$$
$$I_D = 0.5 \times 10^{-3} = 0.5\ mA$$
Step B — overdrive voltage:
$$V_{OV} = \sqrt{\frac{2I_D}{k}}$$
$$V_{OV} = \sqrt{\frac{2 \times 0.5 \times 10^{-3}}{2.5 \times 10^{-3}}}$$
$$V_{OV} = \sqrt{0.4}$$
$$V_{OV} = 0.6325\ V$$
Step C — gate (input) voltage:
$$V_{GS} = V_t + V_{OV}$$
$$V_{GS} = 0.6 + 0.6325$$
$$V_{GS} = 1.2325\ V \approx 1.23\ V$$

**Step 3: Verification & Physical Interpretation**
$V_i = 1.23$ V biases the drain at exactly half the supply (5 V) — the standard maximum-swing bias point. Since $V_i = V_{GS}$ in this grounded-source circuit, the input must supply this DC level directly.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.63 V)**: the student reports $V_{OV}$ instead of $V_{GS}$ (forgets $V_t$).
- **Option C trap (1.63 V)**: the student uses $I_D = 1$ mA (from $V_{out} = 0$).
- **Option D trap (2.23 V)**: the student adds $V_{OV}$ twice.
r""")

theory(T, "For the same amplifier ($V_i = 1.23$ V, $V_{out} = 5$ V, $V_{OV} = 0.632$ V, $V_t = 0.6$ V), validate whether the MOSFET is truly in saturation.",
       ["Yes — $V_{DS} = 5$ V $\\ge V_{OV} = 0.632$ V and $V_{GS} > V_t$, so saturation holds",
        "No — $V_{DS}$ is below the threshold voltage",
        "No — the device is in the triode region",
        "Cannot be determined without $\\lambda$"], 0,
       "Saturation requires $V_{GS} > V_t$ AND $V_{DS} \\ge V_{OV}$; here 1.23 > 0.6 and 5 ≥ 0.632 — both satisfied.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
The two saturation conditions:
$$V_{GS} > V_t \qquad \text{AND} \qquad V_{DS} \ge V_{GS} - V_t = V_{OV}$$
With the source grounded, $V_{DS} = V_{out}$ and $V_{GS} = V_i$.

**Step 2: Full Mathematical Workings**
Condition 1:
$$V_{GS} = 1.2325\ V > V_t = 0.6\ V \quad\checkmark$$
Condition 2:
$$V_{OV} = V_{GS} - V_t = 1.2325 - 0.6 = 0.6325\ V$$
$$V_{DS} = V_{out} = 5\ V \ge 0.6325\ V \quad\checkmark$$
Both conditions hold — the saturation assumption is VALIDATED.

**Step 3: Verification & Physical Interpretation**
The drain sits 4.37 V above the pinch-off point, deep in saturation. If $V_{DS}$ had been less than $V_{OV}$, the original current equation would be wrong and the answer would have to be recomputed with the triode equation — always perform this validation after every bias calculation.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student compares $V_{DS}$ with $V_t$ instead of $V_{OV}$.
- **Option C trap**: the student confuses the condition for triode ($V_{DS} < V_{OV}$) with saturation.
- **Option D trap**: $\lambda$ affects the current VALUE, not the region boundary.
r""")

calc(T, "For the same amplifier (bias $I_D = 0.5$ mA, $V_{OV} = 0.632$ V, $R_D = 10$ kΩ), the small-signal voltage gain is:",
     ["−15.8 V/V", "+15.8 V/V", "−6.3 V/V", "−31.6 V/V"], 0,
       "$g_m = 2I_D/V_{OV} = 1.581$ mA/V; $A_v = -g_m R_D = -15.8$ V/V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_D = 0.5$ mA, $V_{OV} = 0.6325$ V, $R_D = 10$ kΩ.
Governing laws:
$$g_m = \frac{2I_D}{V_{OV}} \qquad A_v = -g_m R_D$$

**Step 2: Full Mathematical Workings**
Step A — transconductance:
$$g_m = \frac{2 \times 0.5 \times 10^{-3}}{0.6325}$$
$$g_m = \frac{1 \times 10^{-3}}{0.6325}$$
$$g_m = 1.581\ mA/V$$
Step B — gain:
$$A_v = -1.581 \times 10^{-3} \times 10 \times 10^{3}$$
$$A_v = -15.81\ V/V \approx -15.8\ V/V$$

**Step 3: Verification & Physical Interpretation**
The gain magnitude equals $2(V_{DD}-V_{out})/V_{OV} = 2 \times 5/0.6325 = 15.8$ — the drain-bias form of the same result. The minus sign is the hallmark of the common-source stage.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (+15.8)**: sign error — CS stages invert.
- **Option C trap (−6.3)**: the student uses $g_m = k_n V_{OV} \times \frac{1}{2}$ (forgets the factor 2 in $2I_D/V_{OV}$).
- **Option D trap (−31.6)**: the student doubles the current in the $g_m$ formula.
r""")

calc(T, "A MOSFET biasing circuit (Fig. 2) has $R_D = 1.5$ kΩ, $R_S = 500$ Ω, $R_1 = 400$ kΩ, $R_2 = 600$ kΩ and $V_{DD} = 12$ V. The PMOS parameters are $K_p = 0.5$ mA/V², $V_{tp} = -1.5$ V and $\\lambda = 0.01$. The drain current $I_D$ is about:",
     ["1.58 mA", "0.79 mA", "3.16 mA", "2.36 mA"], 0,
       "PMOS: $V_G = 12\\times600/1000 = 7.2$ V; $V_{SG} = 12 - 500I_D - 7.2$; $I_D = \\frac{1}{2}K_p(V_{SG}-1.5)^2$ iterates to $I_D \\approx 1.58$ mA.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $R_D = 1.5$ kΩ, $R_S = 500$ Ω, $R_1 = 400$ kΩ, $R_2 = 600$ kΩ, $V_{DD} = 12$ V, $K_p = 0.5$ mA/V², $|V_{tp}| = 1.5$ V.
Schematic layout (textual): PMOS source at the TOP — $V_{DD}$ → $R_S$ → source S; drain → $R_D$ → ground. The gate is fed by the divider $R_1$ (to $V_{DD}$) and $R_2$ (to ground). Governing laws:
$$V_G = V_{DD}\frac{R_2}{R_1+R_2} \qquad I_D = \frac{1}{2}K_p(V_{SG} - |V_{tp}|)^2$$

**Step 2: Full Mathematical Workings**
Step A — gate voltage:
$$V_G = 12 \times \frac{600}{400 + 600} = 12 \times 0.6 = 7.2\ V$$
Step B — source voltage and source-gate voltage:
$$V_S = V_{DD} - I_D R_S = 12 - 500I_D$$
$$V_{SG} = V_S - V_G = 12 - 500I_D - 7.2 = 4.8 - 500I_D$$
Step C — solve $I_D = \frac{1}{2}\times0.5m\times(4.8 - 500I_D - 1.5)^2$ by iteration:
$$I_D = 0.25m(3.3 - 500I_D)^2$$
Iteration: start $I_D = 1$ mA → $0.25m(2.8)^2 = 1.96$ mA → $0.25m(3.3-0.98)^2 = 1.346$ mA → $0.25m(3.3-0.673)^2 = 1.725$ mA → $0.25m(3.3-0.8625)^2 = 1.485$ mA → $0.25m(3.3-0.7425)^2 = 1.635$ mA → $0.25m(3.3-0.8175)^2 = 1.541$ mA → $0.25m(3.3-0.7705)^2 = 1.599$ mA → converges:
$$I_D \approx 1.58\ mA$$

**Step 3: Verification & Physical Interpretation**
The iteration converges because the feedback through $R_S$ is negative: more current lowers $V_{SG}$, reducing the current. Checking: $V_{SG} = 4.8 - 0.79 = 4.01$ V, $I_D = 0.25m(4.01-1.5)^2 = 0.25m \times 6.3 = 1.575$ mA ≈ 1.58 mA ✓.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.79 mA)**: the student forgets the ½ in the square law.
- **Option C trap (3.16 mA)**: the student omits the $R_S$ feedback entirely ($V_{SG} = 4.8$ V fixed).
- **Option D trap (2.36 mA)**: the student uses the NMOS sign conventions (wrong polarity).
r""")

calc(T, "For the same PMOS bias point ($I_D = 1.58$ mA, $V_{SG} \\approx 4.01$ V), the gate-to-source voltage $V_{GS}$, transconductance $g_m$ and output resistance $r_o$ are:",
     ["$V_{GS} = -4.01$ V, $g_m = 1.26$ mA/V, $r_o = 63.3$ kΩ",
      "$V_{GS} = +4.01$ V, $g_m = 1.26$ mA/V, $r_o = 63.3$ kΩ",
      "$V_{GS} = -4.01$ V, $g_m = 2.52$ mA/V, $r_o = 126.6$ kΩ",
      "$V_{GS} = -2.51$ V, $g_m = 1.26$ mA/V, $r_o = 63.3$ kΩ"], 0,
       "For a PMOS, $V_{GS} = -V_{SG} = -4.01$ V; $V_{OV} = 4.01 - 1.5 = 2.51$ V; $g_m = 2I_D/V_{OV} = 1.26$ mA/V; $r_o = 1/(\\lambda I_D) = 63.3$ kΩ.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_D = 1.58$ mA, $V_{SG} = 4.01$ V, $|V_{tp}| = 1.5$ V, $\lambda = 0.01$ V⁻¹.
Governing laws:
$$V_{GS} = -V_{SG} \qquad g_m = \frac{2I_D}{V_{OV}} \qquad r_o = \frac{1}{\lambda I_D}$$

**Step 2: Full Mathematical Workings**
Step A — gate-to-source voltage (PMOS convention):
$$V_{GS} = -V_{SG} = -4.01\ V$$
Step B — overdrive:
$$V_{OV} = V_{SG} - |V_{tp}| = 4.01 - 1.5 = 2.51\ V$$
Step C — transconductance:
$$g_m = \frac{2 \times 1.58 \times 10^{-3}}{2.51}$$
$$g_m = 1.259\ mA/V \approx 1.26\ mA/V$$
Step D — output resistance:
$$r_o = \frac{1}{0.01 \times 1.58 \times 10^{-3}}$$
$$r_o = \frac{1}{1.58 \times 10^{-5}}$$
$$r_o = 63.3\ k\Omega$$

**Step 3: Verification & Physical Interpretation**
PMOS quantities carry the opposite sign convention: $V_{GS}$ is negative, $V_{DS}$ will be negative, but the MAGNITUDES satisfy the same square law. $r_o = 63.3$ kΩ quantifies the channel-length modulation (1% per volt).

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: positive $V_{GS}$ — the classic PMOS sign error.
- **Option C trap**: the student uses $g_m = I_D/V_{OV}$ and doubles $r_o$.
- **Option D trap**: the student reports $-V_{OV}$ as $V_{GS}$, forgetting the threshold.
r""")

theory(T, "In NMOS logic circuits, how are AND and OR functions implemented, and what Boolean expression results for series/parallel combinations?",
       ["Series-connected NMOS transistors implement AND (all must conduct); parallel-connected implement OR (any conducts); e.g. Z = (A·B) + (C·D) for two series pairs in parallel",
        "Series implements OR and parallel implements AND",
        "Both series and parallel implement AND",
        "Logic functions cannot be built with NMOS transistors"], 0,
       "Series = AND (all transistors ON to pull down), parallel = OR (any transistor ON pulls down).",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
An NMOS conducts when its gate is HIGH. In a pull-down network:
- SERIES connection: the output is pulled LOW only when ALL transistors conduct ⇒ the pull-down condition is $A \cdot B \cdot \ldots$ (AND).
- PARALLEL connection: the output is pulled LOW when ANY transistor conducts ⇒ the pull-down condition is $A + B + \ldots$ (OR).
With a pull-up device on top, the output is the COMPLEMENT of the pull-down condition — which is how CMOS builds NAND/NOR, and how NMOS-only logic builds inverting gates.

**Step 2: Testing the Options**
- **Option A (correct)**: series = AND, parallel = OR, with the worked example.
- **Option B (wrong)**: exactly backwards.
- **Option C (wrong)**: parallel gives OR, not AND.
- **Option D (wrong)**: NMOS (and PMOS) logic is the basis of all modern digital circuits.

**Step 3: Exam Trap Summary**
Two traps: (1) forgetting that the pull-down network's conduction condition is the COMPLEMENT of the output; (2) swapping series/parallel. Anchor: "series needs everyone (AND); parallel needs anyone (OR)".
r""")

# =====================================================================
# TOPIC 5 — BIPOLAR JUNCTION TRANSISTORS
# =====================================================================
T = "eee252-bjt"

theory(T, "Match the three BJT operating modes to their junction bias conditions: (a) active (b) saturation (c) cutoff.",
       ["EBJ forward + CBJ reverse; EBJ forward + CBJ forward; EBJ reverse + CBJ reverse",
        "EBJ reverse + CBJ reverse; EBJ forward + CBJ forward; EBJ forward + CBJ reverse",
        "EBJ forward + CBJ forward; EBJ reverse + CBJ reverse; EBJ forward + CBJ reverse",
        "All junctions forward in every mode"], 0,
       "Active: EBJ fwd + CBJ rev. Saturation: both forward. Cutoff: both reverse.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
- ACTIVE (amplifier): emitter–base junction (EBJ) forward-biased ($V_{BE} \approx 0.7$ V), collector–base junction (CBJ) reverse-biased ($V_{CB} > 0$).
- SATURATION (switch ON): BOTH junctions forward-biased; $V_{CE}$ collapses to $V_{CE(sat)} \approx 0.2$ V.
- CUTOFF (switch OFF): BOTH junctions reverse-biased; all currents ≈ 0.

**Step 2: Testing the Options**
- **Option A (correct)**: the standard mode table.
- **Option B (wrong)**: cutoff and active are swapped.
- **Option C (wrong)**: active and saturation are swapped.
- **Option D (wrong)**: modes are distinguished precisely by junction biases.

**Step 3: Exam Trap Summary**
The trap is remembering only $V_{BE}$. The mode is set by BOTH junctions — always check the CBJ too. Mnemonic: "Active = amplifier (A for amplifier, CBJ reversed); Saturated = switch-on (both on)".
r""")

calc(T, "An npn BJT has $\\beta = 100$ and $I_S = 10^{-15}$ A. With $v_{BE} = 0.7$ V and $V_T = 25$ mV, the collector current $i_C$ and base current $i_B$ are:",
     ["$i_C = 1.45$ mA, $i_B = 14.5$ µA", "$i_C = 0.145$ mA, $i_B = 1.45$ µA", "$i_C = 14.5$ mA, $i_B = 145$ µA", "$i_C = 1.45$ mA, $i_B = 1.45$ mA"], 0,
       "$i_C = I_S e^{v_{BE}/V_T} = 10^{-15}e^{28} = 1.446$ mA; $i_B = i_C/\\beta = 14.46$ µA.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $\beta = 100$, $I_S = 10^{-15}$ A, $v_{BE} = 0.7$ V, $V_T = 25$ mV.
Governing laws:
$$i_C = I_S e^{v_{BE}/V_T} \qquad i_B = \frac{i_C}{\beta}$$

**Step 2: Full Mathematical Workings**
Step A — collector current:
$$\frac{v_{BE}}{V_T} = \frac{0.7}{0.025} = 28$$
$$i_C = 10^{-15} \times e^{28}$$
$$e^{28} = 1.4463 \times 10^{12}$$
$$i_C = 1.446 \times 10^{-3} = 1.446\ mA$$
Step B — base current:
$$i_B = \frac{1.446\ mA}{100}$$
$$i_B = 14.46\ \mu A$$

**Step 3: Verification & Physical Interpretation**
The collector current is controlled by $v_{BE}$ exponentially, and the base current is the "wasted" 1/β fraction of it. Emitter current then follows as $i_E = i_C + i_B = 1.460$ mA.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: factor-of-10 slip in $e^{28}$.
- **Option C trap**: the student multiplies by β instead of dividing for $i_B$.
- **Option D trap**: the student sets $i_B = i_C$ (forgets the β division).
r""")

calc(T, "For the same transistor ($\\beta = 100$), the alpha $\\alpha$ and the emitter current $i_E$ are:",
     ["$\\alpha = 0.9901$, $i_E = 1.46$ mA", "$\\alpha = 100$, $i_E = 1.45$ mA", "$\\alpha = 0.99$, $i_E = 1.45$ mA", "$\\alpha = 0.909$, $i_E = 1.59$ mA"], 0,
       "$\\alpha = \\beta/(\\beta+1) = 100/101 = 0.9901$; $i_E = i_C + i_B = 1.446 + 0.0145 = 1.46$ mA — and $i_E = i_C/\\alpha$ confirms it.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $\beta = 100$, $i_C = 1.446$ mA, $i_B = 14.46$ µA.
Governing laws:
$$\alpha = \frac{\beta}{\beta+1} \qquad i_E = i_C + i_B$$

**Step 2: Full Mathematical Workings**
Step A — alpha:
$$\alpha = \frac{100}{100+1} = \frac{100}{101}$$
$$\alpha = 0.9901$$
Step B — emitter current:
$$i_E = 1.446 + 0.01446$$
$$i_E = 1.460\ mA$$
Step C — numerical confirmation of $\alpha = \beta/(\beta+1)$ via $i_E = i_C/\alpha$:
$$\frac{i_C}{\alpha} = \frac{1.446}{0.9901} = 1.460\ mA = i_E \quad\checkmark$$

**Step 3: Verification & Physical Interpretation**
Alpha is the fraction of emitter current that reaches the collector — 99.01% for β = 100. The two relations $i_E = i_C + i_B$ and $\alpha = \beta/(\beta+1)$ are mutually consistent, as the problem demands.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: α can never exceed 1 — quoting α = 100 is the β value.
- **Option C trap**: $i_E$ must exceed $i_C$ by $i_B$; 1.45 mA neglects the base current.
- **Option D trap**: the student uses $\alpha = \beta/(\beta-1)$.
r""")

calc(T, "Consider the circuit of Fig. P6.51: $V_{CC} = +5$ V through $R_C = 1$ kΩ to the collector; $R_E = 1$ kΩ from emitter to ground; base driven directly by $V_B$; very high β. For $V_B = +2.0$ V, the emitter voltage $V_E$ and collector voltage $V_C$ are:",
     ["$V_E = 1.3$ V, $V_C = 3.7$ V (active)", "$V_E = 2.0$ V, $V_C = 3.0$ V", "$V_E = 1.3$ V, $V_C = 5.0$ V", "$V_E = 0$ V, $V_C = 5$ V"], 0,
       "Active: $V_E = V_B - 0.7 = 1.3$ V; $I_E = 1.3$ mA ≈ $I_C$; $V_C = 5 - 1.3 = 3.7$ V; $V_{CB} = 3.7 - 2 = 1.7$ V > 0 ⇒ CBJ reverse — active confirmed.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{CC} = 5$ V, $R_C = R_E = 1$ kΩ, $V_B = 2$ V, very high β (so $i_B \approx 0$ and $i_E \approx i_C$).
Governing laws:
$$V_E = V_B - V_{BE} \qquad I_E = \frac{V_E}{R_E} \qquad V_C = V_{CC} - I_C R_C$$

**Step 2: Full Mathematical Workings**
Step A — assume ACTIVE mode, $V_{BE} = 0.7$ V:
$$V_E = 2 - 0.7 = 1.3\ V$$
Step B — emitter current:
$$I_E = \frac{1.3}{1k} = 1.3\ mA$$
Step C — with very high β, $I_C \approx I_E = 1.3$ mA:
$$V_C = 5 - 1.3 \times 10^{-3} \times 10^{3} = 5 - 1.3 = 3.7\ V$$
Step D — verify the active assumption via the CBJ:
$$V_{CB} = V_C - V_B = 3.7 - 2 = +1.7\ V > 0$$
CBJ reverse-biased ⇒ ACTIVE confirmed.

**Step 3: Verification & Physical Interpretation**
The collector sits 1.7 V above the base, keeping the CBJ safely reverse-biased — the transistor amplifies in its active region with $V_{CE} = V_C - V_E = 2.4$ V.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: $V_E = V_B$ forgets the 0.7 V EBJ drop.
- **Option C trap**: $V_C = 5$ V implies zero collector current — the student neglected $I_C R_C$.
- **Option D trap**: that is the cutoff case ($V_B$ too low to forward-bias the EBJ).
r""")

calc(T, "For the same circuit (Fig. P6.51, $V_{CC} = 5$ V, $R_C = R_E = 1$ kΩ, very high β), find $V_E$ and $V_C$ for $V_B = +1.7$ V.",
     ["$V_E = 1.0$ V, $V_C = 4.0$ V (active)", "$V_E = 1.7$ V, $V_C = 3.3$ V", "$V_E = 1.0$ V, $V_C = 5.0$ V", "$V_E = 0$ V, $V_C = 5$ V"], 0,
       "$V_E = 1.7 - 0.7 = 1.0$ V; $I_E = 1$ mA; $V_C = 5 - 1 = 4.0$ V; $V_{CB} = 2.3$ V > 0 ⇒ active.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_B = 1.7$ V, $V_{CC} = 5$ V, $R_C = R_E = 1$ kΩ, very high β.

**Step 2: Full Mathematical Workings**
Step A — assume active, $V_{BE} = 0.7$ V:
$$V_E = 1.7 - 0.7 = 1.0\ V$$
Step B:
$$I_E = \frac{1.0}{1k} = 1.0\ mA \approx I_C$$
Step C:
$$V_C = 5 - 1.0 = 4.0\ V$$
Step D — verify:
$$V_{CB} = 4.0 - 1.7 = +2.3\ V > 0$$
CBJ reverse ⇒ ACTIVE confirmed.

**Step 3: Verification & Physical Interpretation**
Lowering $V_B$ by 0.3 V reduces the emitter current by 0.3 mA and RAISES the collector voltage by 0.3 V (the stage inverts). The device remains comfortably active.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: $V_E = V_B$ — 0.7 V drop forgotten.
- **Option C trap**: collector current neglected.
- **Option D trap**: the cutoff case — requires $V_B < 0.7$ V.
r""")

calc(T, "For the same circuit (Fig. P6.51, very high β), find $V_E$, $V_C$ and the mode for $V_B = 0$ V.",
     ["$V_E = 0$ V, $V_C = 5$ V — CUTOFF (EBJ reverse-biased)",
      "$V_E = -0.7$ V, $V_C = 5$ V — active",
      "$V_E = 0$ V, $V_C = 0$ V — saturation",
      "$V_E = 0.7$ V, $V_C = 4.3$ V — active"], 0,
       "With $V_B = 0$ the EBJ sees $V_{BE} = 0 < 0.7$ V — it is OFF, so $I_E = 0$, $V_E = 0$ and $V_C = V_{CC} = 5$ V: cutoff.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_B = 0$ V. The EBJ requires $V_{BE} \approx 0.7$ V to conduct.

**Step 2: Full Mathematical Workings**
Step A — test the EBJ:
$$V_{BE} = V_B - V_E = 0 - V_E$$
For the EBJ to conduct we would need $V_{BE} = 0.7$ V, i.e. $V_E = -0.7$ V — impossible since $V_E$ cannot go negative in this circuit (emitter grounded through a resistor, no negative supply).
Step B — conclude CUTOFF:
$$I_E = I_C = I_B = 0$$
$$V_E = I_E R_E = 0\ V$$
Step C — collector voltage:
$$V_C = V_{CC} - I_C R_C = 5 - 0 = 5\ V$$

**Step 3: Verification & Physical Interpretation**
With zero base drive the transistor behaves as an OPEN switch: the full supply appears at the collector. This is the OFF state of the transistor switch.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: a negative emitter voltage would require a negative supply.
- **Option C trap**: in saturation $V_C$ collapses toward $V_E + 0.2$ V, not 0 V.
- **Option D trap**: the student assumes conduction without checking whether $V_B$ can forward-bias the EBJ.
r""")

calc(T, "For the same circuit (Fig. P6.51, very high β, $V_{CC} = 5$ V, $R_C = R_E = 1$ kΩ), find the HIGHEST value of $V_B$ for which the transistor still operates in the active mode.",
     ["3.1 V", "3.7 V", "2.4 V", "4.3 V"], 0,
       "Edge of saturation: $V_C = V_B - 0.5$ with $V_C = 5 - (V_B-0.7)$ ⇒ $V_B = 3.1$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{CC} = 5$ V, $R_C = R_E = 1$ kΩ, very high β ($I_C \approx I_E$).
Active mode is lost when the CBJ becomes forward-biased, i.e. when $V_C$ falls to $V_B - 0.5$ V (the CBJ just begins conducting; $V_{CE} = V_C - V_E = 0.2$ V at the edge of saturation).

**Step 2: Full Mathematical Workings**
In active mode:
$$V_E = V_B - 0.7$$
$$I_E = \frac{V_B - 0.7}{1k} = (V_B - 0.7)\ mA$$
$$V_C = 5 - (V_B - 0.7) = 5.7 - V_B$$
At the edge of saturation:
$$V_C = V_B - 0.5$$
Equate:
$$5.7 - V_B = V_B - 0.5$$
$$5.7 + 0.5 = 2V_B$$
$$2V_B = 6.2$$
$$V_B = 3.1\ V$$

**Step 3: Verification & Physical Interpretation**
At $V_B = 3.1$ V: $V_E = 2.4$ V, $I_C = 2.4$ mA, $V_C = 5 - 2.4 = 2.6$ V, and $V_C - V_B = -0.5$ V — the CBJ is exactly at the conduction edge. Any higher $V_B$ drives the transistor into saturation.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (3.7 V)**: the student uses the $V_C$ from the $V_B = 2$ V case as the boundary.
- **Option C trap (2.4 V)**: the student equates $V_B$ with $V_E$'s value at the edge.
- **Option D trap (4.3 V)**: the student uses $V_C = V_B - 0.7$ as the edge condition.
r""")

calc(T, "For the same circuit, find the value of $V_B$ at which the transistor operates in SATURATION with a forced β of 3.",
     ["3.44 V", "3.1 V", "3.9 V", "2.9 V"], 0,
       "In saturation $V_{CE} = 0.2$ V and $I_C = 3I_B$ with $I_E = 4I_B$: $V_B - 0.5 = 5 - 3(V_B-0.7)/4$ ⇒ $V_B = 3.44$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: forced $\beta_{forced} = 3$, $V_{CE(sat)} = 0.2$ V, $V_{BE} = 0.7$ V.
In saturation: $I_C = \beta_{forced} I_B = 3I_B$, and $I_E = I_C + I_B = 4I_B$.

**Step 2: Full Mathematical Workings**
Step A — emitter voltage and current:
$$V_E = V_B - 0.7$$
$$I_E = \frac{V_B - 0.7}{1k} = 4I_B \quad\Rightarrow\quad I_B = \frac{V_B - 0.7}{4k}$$
Step B — collector current and voltage:
$$I_C = 3I_B = \frac{3(V_B - 0.7)}{4k}$$
$$V_C = 5 - I_C \times 1k = 5 - \frac{3(V_B - 0.7)}{4}$$
Step C — saturation condition $V_C = V_E + 0.2$:
$$V_C = V_B - 0.7 + 0.2 = V_B - 0.5$$
Equate:
$$5 - \frac{3(V_B - 0.7)}{4} = V_B - 0.5$$
$$5 + 0.5 = V_B + \frac{3(V_B - 0.7)}{4}$$
Multiply by 4:
$$22 = 4V_B + 3V_B - 2.1$$
$$22 + 2.1 = 7V_B$$
$$V_B = \frac{24.1}{7} = 3.443\ V \approx 3.44\ V$$

**Step 3: Verification & Physical Interpretation**
Checking: $V_E = 2.743$ V, $I_E = 2.743$ mA, $I_B = 0.686$ mA, $I_C = 2.057$ mA — ratio $I_C/I_B = 3$ exactly (the forced β). The forced-β concept quantifies HOW DEEP the saturation is: 3 means well into saturation.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (3.1 V)**: that is the EDGE of saturation (forced β → β), not the deep-saturation point.
- **Option C trap (3.9 V)**: the student uses $I_E = 3I_B$ (forgets $I_E = I_C + I_B$).
- **Option D trap (2.9 V)**: arithmetic slip in clearing the fraction.
r""")

calc(T, "Consider the fixed-bias circuit: $V_{CC} = 12$ V → $R_B = 1$ MΩ → base; $V_{CC} = 12$ V → $R_C = 3$ kΩ → collector; emitter grounded; $V_{BE} = 0.7$ V. For β = 100, the quiescent $I_C$ and $V_{CE}$ are:",
     ["$I_C = 1.13$ mA, $V_{CE} = 8.61$ V", "$I_C = 11.3$ mA, $V_{CE} = -21.9$ V", "$I_C = 1.13$ mA, $V_{CE} = 3.39$ V", "$I_C = 0.113$ mA, $V_{CE} = 11.66$ V"], 0,
       "$I_B = (12-0.7)/1M = 11.3$ µA; $I_C = 100 \\times 11.3\\mu = 1.13$ mA; $V_{CE} = 12 - 1.13m\\times3k = 8.61$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{CC} = 12$ V, $R_B = 1$ MΩ, $R_C = 3$ kΩ, $V_{BE} = 0.7$ V, $\beta = 100$.
Governing laws — fixed bias:
$$I_B = \frac{V_{CC} - V_{BE}}{R_B} \qquad I_C = \beta I_B \qquad V_{CE} = V_{CC} - I_C R_C$$

**Step 2: Full Mathematical Workings**
Step A — base current:
$$I_B = \frac{12 - 0.7}{10^{6}}$$
$$I_B = \frac{11.3}{10^{6}} = 11.3\ \mu A$$
Step B — collector current:
$$I_C = 100 \times 11.3 \times 10^{-6}$$
$$I_C = 1.13 \times 10^{-3} = 1.13\ mA$$
Step C — collector-emitter voltage:
$$V_{CE} = 12 - 1.13 \times 10^{-3} \times 3 \times 10^{3}$$
$$V_{CE} = 12 - 3.39$$
$$V_{CE} = 8.61\ V$$

**Step 3: Verification & Physical Interpretation**
The quiescent point (1.13 mA, 8.61 V) sits in the active region with $V_{CE}$ well above $V_{CE(sat)}$ — the transistor is a valid amplifier at this bias.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student computes $I_B = 113$ µA (uses $R_B = 100$ kΩ).
- **Option C trap**: the student drops the $I_C R_C$ term from $V_{CE}$... (3.39 = the DROP, reported as $V_{CE}$).
- **Option D trap**: the student forgets β (uses $I_C = I_B$).
r""")

calc(T, "The fixed-bias circuit (same values) is rebuilt with a different transistor of the same part number having β = 200. The new $I_C$ and $V_{CE}$ are:",
     ["$I_C = 2.26$ mA, $V_{CE} = 5.22$ V", "$I_C = 1.13$ mA, $V_{CE} = 8.61$ V", "$I_C = 2.26$ mA, $V_{CE} = 10.87$ V", "$I_C = 0.565$ mA, $V_{CE} = 10.3$ V"], 0,
       "$I_B$ is unchanged (11.3 µA — set only by $V_{CC}, R_B, V_{BE}$); $I_C = 200 \\times 11.3\\mu = 2.26$ mA; $V_{CE} = 12 - 6.78 = 5.22$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $\beta = 200$; circuit values unchanged.
Key observation: the base current of fixed bias does NOT depend on β:
$$I_B = \frac{V_{CC} - V_{BE}}{R_B}$$

**Step 2: Full Mathematical Workings**
Step A — base current (unchanged):
$$I_B = \frac{11.3}{10^{6}} = 11.3\ \mu A$$
Step B — new collector current:
$$I_C = 200 \times 11.3 \times 10^{-6}$$
$$I_C = 2.26\ mA$$
Step C — new $V_{CE}$:
$$V_{CE} = 12 - 2.26 \times 10^{-3} \times 3 \times 10^{3}$$
$$V_{CE} = 12 - 6.78$$
$$V_{CE} = 5.22\ V$$

**Step 3: Verification & Physical Interpretation**
Doubling β doubled $I_C$ and nearly halved $V_{CE}$ (from 8.61 V to 5.22 V). The Q-point is still active, but it has moved dramatically — this β-dependence is exactly why fixed bias is unacceptable in production.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student assumes $I_C$ is β-independent (that is the WISH, not the behaviour).
- **Option C trap**: the student adds instead of subtracting the collector drop.
- **Option D trap**: the student divides by β twice.
r""")

calc(T, "Between the β = 100 and β = 200 transistors in the same fixed-bias circuit, the percentage change in $I_C$ is:",
     ["+100%", "+50%", "+200%", "+25%"], 0,
       "$\\Delta I_C/I_C = (2.26 - 1.13)/1.13 = 100\\%$ — $I_C$ scales directly with β in fixed bias.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_C(100) = 1.13$ mA, $I_C(200) = 2.26$ mA.
Governing law:
$$\text{percentage change} = \frac{I_C(200) - I_C(100)}{I_C(100)} \times 100\%$$

**Step 2: Full Mathematical Workings**
$$\text{percentage change} = \frac{2.26 - 1.13}{1.13} \times 100\%$$
$$\frac{2.26 - 1.13}{1.13} = \frac{1.13}{1.13} = 1$$
$$\text{percentage change} = 100\%$$

**Step 3: Verification & Physical Interpretation**
In fixed bias $I_C = \beta I_B$ with $I_B$ fixed, so $I_C$ tracks β ONE-FOR-ONE: a 100% change in β produces a 100% change in $I_C$. No other biasing scheme behaves this badly.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (50%)**: the student divides the change by the NEW current.
- **Option C trap (200%)**: the student divides by $I_B$ instead of $I_C$.
- **Option D trap (25%)**: the student compares $V_{CE}$ changes instead of $I_C$.
r""")

theory(T, "Is the fixed-bias circuit ($V_{CC} = 12$ V, $R_B = 1$ MΩ, $R_C = 3$ kΩ) acceptable as the front end of an amplifier, and why?",
       ["No — the bias point depends directly on β, which varies enormously between transistors, making the design unreproducible",
        "Yes — it is the most stable biasing scheme available",
        "Yes — $V_{CE}$ stays constant regardless of β",
        "No — the circuit cannot amplify at all"], 0,
       "Fixed bias is β-unstable: $I_C = β(V_{CC}-V_{BE})/R_B$ moves one-for-one with β.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
Fixed bias sets $I_B = (V_{CC}-V_{BE})/R_B$ and therefore $I_C = \beta I_B$. Since β varies widely between individual transistors (even of the same part number) and with temperature, the quiescent point wanders correspondingly.

**Step 2: Testing the Options**
- **Option A (correct)**: the bias point is β-dependent and therefore unreproducible — a production amplifier cannot tolerate a 100% current change for a 2:1 β spread.
- **Option B (wrong)**: fixed bias is the LEAST stable of the standard schemes (emitter-degeneration and divider bias stabilise the point).
- **Option C (wrong)**: we computed $V_{CE}$ changing from 8.61 V to 5.22 V.
- **Option D (wrong)**: the circuit DOES amplify — its fault is instability, not incapability.

**Step 3: Exam Trap Summary**
This is the classic "criticise the bias scheme" question. The answer is always about β-STABILITY: state the equation $I_C = \beta(V_{CC}-V_{BE})/R_B$, point out the one-for-one β dependence, and note the fix (emitter resistor/voltage-divider bias).
r""")

# =====================================================================
# TOPIC 6 — SMALL-SIGNAL MODELS & EQUIVALENT CIRCUITS
# =====================================================================
T = "eee252-small-signal"

calc(T, "Consider the amplifier of Fig. 1 operated with $V_{CC} = +3$ V (collector load $R_C$, input applied to the base). The theoretical maximum voltage gain is:",
     ["−120 V/V", "−60 V/V", "−3 V/V", "+120 V/V"], 0,
       "$A_{v,max} = -V_{CC}/V_T = -3/0.025 = -120$ V/V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{CC} = 3$ V, $V_T = 25$ mV.
Governing law — the maximum CE gain is set by the supply and the thermal voltage:
$$A_{v,max} = -\frac{V_{CC}}{V_T}$$

**Step 2: Full Mathematical Workings**
$$A_{v,max} = -\frac{3}{0.025}$$
$$A_{v,max} = -\frac{3}{25 \times 10^{-3}}$$
$$A_{v,max} = -120\ V/V$$

**Step 3: Verification & Physical Interpretation**
The gain ceiling arises because $g_m = I_C/V_T$ while $R_C$ is limited by $I_C R_C = V_{CC} - V_{CE}$, so the product $g_m R_C$ peaks at $V_{CC}/V_T$. For a 3 V supply the theoretical ceiling is 120.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (−60)**: the student uses $V_{CC}/2$ in the numerator.
- **Option C trap (−3)**: the student divides by 1 V instead of $V_T$.
- **Option D trap (+120)**: sign error — CE stages invert.
r""")

calc(T, "For the same amplifier ($V_{CC} = 3$ V), the bias $V_{CE}$ needed to provide a gain of −60 V/V is:",
     ["1.5 V", "2.4 V", "0.6 V", "1.2 V"], 0,
       "$|A_v| = (V_{CC}-V_{CE})/V_T$ ⇒ $V_{CE} = V_{CC} - |A_v|V_T = 3 - 60\\times0.025 = 1.5$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $V_{CC} = 3$ V, target $|A_v| = 60$.
Governing law — CE gain in terms of the bias point:
$$|A_v| = \frac{V_{CC} - V_{CE}}{V_T}$$

**Step 2: Full Mathematical Workings**
$$V_{CE} = V_{CC} - |A_v| V_T$$
$$V_{CE} = 3 - 60 \times 0.025$$
$$60 \times 0.025 = 1.5$$
$$V_{CE} = 3 - 1.5 = 1.5\ V$$

**Step 3: Verification & Physical Interpretation**
Biasing at $V_{CE} = 1.5$ V leaves exactly $V_{CC} - V_{CE} = 1.5$ V across the collector resistor. Since $g_m R_C = (I_C/V_T)(V_{RC}/I_C) = V_{RC}/V_T = 1.5/0.025 = 60$, the gain is −60 V/V.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (2.4 V)**: the student uses $V_T = 10$ mV.
- **Option C trap (0.6 V)**: the student computes $|A_v|V_T$ and forgets to subtract from $V_{CC}$... reports $V_{CC}-2.4$ as 0.6 — arithmetic slip.
- **Option D trap (1.2 V)**: the student uses $V_{CC}/2.5$ style shortcut.
r""")

calc(T, "If the DC collector current at the bias point is to be 0.5 mA (with $V_{CE} = 1.5$ V, $V_{CC} = 3$ V), the required collector resistance $R_C$ is:",
     ["3 kΩ", "1.5 kΩ", "6 kΩ", "0.33 kΩ"], 0,
       "$R_C = (V_{CC}-V_{CE})/I_C = (3-1.5)/0.5m = 3$ kΩ.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_C = 0.5$ mA, $V_{CE} = 1.5$ V, $V_{CC} = 3$ V.
Governing law:
$$R_C = \frac{V_{CC} - V_{CE}}{I_C}$$

**Step 2: Full Mathematical Workings**
$$V_{CC} - V_{CE} = 3 - 1.5 = 1.5\ V$$
$$R_C = \frac{1.5}{0.5 \times 10^{-3}}$$
$$R_C = 3 \times 10^{3} = 3\ k\Omega$$

**Step 3: Verification & Physical Interpretation**
The 3 kΩ collector resistor drops exactly half the supply at the 0.5 mA bias point. Checking the gain: $g_m = 0.5m/0.025 = 20$ mA/V, $g_m R_C = 20m \times 3k = 60$ — consistent with the −60 V/V target.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (1.5 kΩ)**: the student divides $V_{CE}$ by $I_C$ instead of the resistor drop.
- **Option C trap (6 kΩ)**: the student uses $V_{CC}$ alone.
- **Option D trap (0.33 kΩ)**: the student inverts the ratio.
r""")

calc(T, "At the same bias point ($I_C = 0.5$ mA, $I_S = 10^{-15}$ A, $V_T = 25$ mV), the required $V_{BE}$ is:",
     ["0.673 V", "0.7 V", "0.635 V", "0.75 V"], 0,
       "$V_{BE} = V_T\\ln(I_C/I_S) = 0.025\\ln(5\\times10^{11}) = 0.025 \\times 26.94 = 0.673$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_C = 0.5$ mA, $I_S = 10^{-15}$ A, $V_T = 25$ mV.
Governing law (active mode, inverted):
$$V_{BE} = V_T \ln\frac{I_C}{I_S}$$

**Step 2: Full Mathematical Workings**
Ratio:
$$\frac{I_C}{I_S} = \frac{0.5 \times 10^{-3}}{10^{-15}} = 5 \times 10^{11}$$
Natural log:
$$\ln(5 \times 10^{11}) = \ln 5 + 11\ln 10$$
$$\ln 5 = 1.6094 \qquad 11\ln 10 = 11 \times 2.3026 = 25.329$$
$$\ln(5 \times 10^{11}) = 26.938$$
Multiply:
$$V_{BE} = 0.025 \times 26.938$$
$$V_{BE} = 0.6734\ V \approx 0.673\ V$$

**Step 3: Verification & Physical Interpretation**
The exact exponential model demands 0.673 V — slightly less than the 0.7 V rule of thumb, because 0.5 mA is below the ~1 mA where 0.7 V typically applies. In exams: use 0.7 V when told to; otherwise compute.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap (0.7 V)**: the student applies the rule of thumb instead of the exponential model.
- **Option C trap (0.635 V)**: the student drops the $\ln 5$ term (uses $11\ln 10$ only).
- **Option D trap (0.75 V)**: the student uses $I_C = 1$ mA.
r""")

calc(T, "A 5 mV peak sine wave $v_{be}$ is superimposed on $V_{BE}$ at the bias point (gain −60 V/V, $g_m = 20$ mA/V). The output voltage signal $v_{ce}$ and the signal collector current $i_c$ are:",
     ["$v_{ce} = -300$ mV, $i_c = 0.1$ mA", "$v_{ce} = -300$ mV, $i_c = 1$ mA", "$v_{ce} = -60$ mV, $i_c = 0.1$ mA", "$v_{ce} = +300$ mV, $i_c = 0.1$ mA"], 0,
       "$v_{ce} = A_v v_{be} = -60 \\times 5m = -300$ mV; $i_c = g_m v_{be} = 20m \\times 5m = 0.1$ mA.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $v_{be} = 5$ mV peak, $A_v = -60$, $g_m = 20$ mA/V.
Governing laws:
$$v_{ce} = A_v v_{be} \qquad i_c = g_m v_{be}$$

**Step 2: Full Mathematical Workings**
Step A — output voltage:
$$v_{ce} = -60 \times 5 \times 10^{-3}$$
$$v_{ce} = -300 \times 10^{-3} = -300\ mV\ \text{peak}$$
Step B — signal collector current:
$$i_c = 20 \times 10^{-3} \times 5 \times 10^{-3}$$
$$i_c = 100 \times 10^{-6} = 0.1\ mA\ \text{peak}$$

**Step 3: Verification & Physical Interpretation**
The collector current signal is $g_m v_{be}$ (20 mA/V transconductance), and the voltage swing is that current through the collector resistance: $0.1m \times 3k = 0.3$ V — matching $-A_v v_{be}$ exactly. The signal stays linear because 5 mV ≪ 25 mV.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: $i_c = 1$ mA uses $g_m = 200$ mA/V.
- **Option C trap**: $v_{ce}$ uses a gain of −12.
- **Option D trap**: sign error on $v_{ce}$ (CE stages invert).
r""")

theory(T, "A BJT biased at $I_C = 1$ mA has $\\beta = 100$ and $V_A = 100$ V ($V_T = 25$ mV). Compute the hybrid-π parameters $g_m$, $r_\\pi$, $r_e$ and $r_o$.",
       ["$g_m = 40$ mA/V, $r_\\pi = 2.5$ kΩ, $r_e = 24.8$ Ω, $r_o = 100$ kΩ",
        "$g_m = 40$ mA/V, $r_\\pi = 25$ kΩ, $r_e = 25$ Ω, $r_o = 100$ kΩ",
        "$g_m = 25$ mA/V, $r_\\pi = 2.5$ kΩ, $r_e = 25$ Ω, $r_o = 10$ kΩ",
        "$g_m = 40$ mA/V, $r_\\pi = 2.5$ kΩ, $r_e = 25$ Ω, $r_o = 1$ MΩ"], 0,
       "$g_m = 1m/0.025 = 40$ mA/V; $r_\\pi = \\beta/g_m = 2.5$ kΩ; $r_e = V_T/I_E \\approx 24.8$ Ω; $r_o = V_A/I_C = 100$ kΩ.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $I_C = 1$ mA, $\beta = 100$, $V_A = 100$ V, $V_T = 25$ mV.
Governing laws:
$$g_m = \frac{I_C}{V_T} \qquad r_\pi = \frac{\beta}{g_m} \qquad r_e = \frac{V_T}{I_E} \qquad r_o = \frac{V_A}{I_C}$$

**Step 2: Full Mathematical Workings**
Step A — transconductance:
$$g_m = \frac{1 \times 10^{-3}}{25 \times 10^{-3}} = 40\ mA/V$$
Step B — base-emitter resistance:
$$r_\pi = \frac{100}{40 \times 10^{-3}} = 2500\ \Omega = 2.5\ k\Omega$$
Step C — emitter resistance (T model), with $I_E = I_C + I_B = 1.01$ mA:
$$r_e = \frac{25 \times 10^{-3}}{1.01 \times 10^{-3}} = 24.75\ \Omega \approx 24.8\ \Omega$$
Step D — output resistance (Early effect):
$$r_o = \frac{100}{1 \times 10^{-3}} = 100\ k\Omega$$

**Step 3: Verification & Physical Interpretation**
The "40 mA/V per mA" rule and the $r_e = 25$ mV/$I_E$ rule hold. $r_o$ models the Early effect: the collector current rises 1% per volt of $V_{CE}$, i.e. a 100 kΩ slope resistance.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: $r_\pi = \beta \times 25$mV confusion (uses $25k = \beta r_e$ without dividing by $I_C$).
- **Option C trap**: $g_m$ computed with $V_T = 40$ mV, and $r_o$ with $V_A = 10$ V.
- **Option D trap**: $r_o$ computed with $I_B$ instead of $I_C$.
r""")

calc(T, "A common-emitter amplifier uses a BJT with $\\beta = 100$ biased at $I_C = 0.5$ mA, with $R_C = 10$ kΩ. The input resistance $R_{in}$, output resistance $R_o$ and open-circuit gain $A_{vo}$ are:",
     ["$R_{in} = 5$ kΩ, $R_o = 10$ kΩ, $A_{vo} = -200$ V/V",
      "$R_{in} = 2.5$ kΩ, $R_o = 10$ kΩ, $A_{vo} = -100$ V/V",
      "$R_{in} = 5$ kΩ, $R_o = 5$ kΩ, $A_{vo} = -200$ V/V",
      "$R_{in} = 50$ kΩ, $R_o = 10$ kΩ, $A_{vo} = -200$ V/V"], 0,
       "$g_m = 20$ mA/V; $r_\\pi = 100/20m = 5$ kΩ = $R_{in}$; $R_o = R_C = 10$ kΩ; $A_{vo} = -g_m R_C = -200$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $\beta = 100$, $I_C = 0.5$ mA, $R_C = 10$ kΩ.
Governing laws:
$$g_m = \frac{I_C}{V_T} \qquad R_{in} = r_\pi = \frac{\beta}{g_m} \qquad R_o = R_C \qquad A_{vo} = -g_m R_C$$

**Step 2: Full Mathematical Workings**
Step A:
$$g_m = \frac{0.5 \times 10^{-3}}{0.025} = 20\ mA/V$$
Step B:
$$R_{in} = r_\pi = \frac{100}{20 \times 10^{-3}} = 5\ k\Omega$$
Step C:
$$R_o = R_C = 10\ k\Omega$$
Step D:
$$A_{vo} = -20 \times 10^{-3} \times 10 \times 10^{3} = -200\ V/V$$

**Step 3: Verification & Physical Interpretation**
The CE stage offers a moderate input resistance (5 kΩ — limited by $r_\pi$), an output resistance set by the collector resistor, and a large open-circuit gain. Note $R_{in}$ does NOT include any base biasing network — that would appear in parallel with $r_\pi$.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student uses $I_C = 1$ mA (hence $g_m = 40$, $r_\pi = 2.5$ k).
- **Option C trap**: $R_o$ reported as $R_C \parallel r_o$ with a wrongly small $r_o$.
- **Option D trap**: $R_{in} = \beta R_C$ — a classic dimensional mix-up.
r""")

calc(T, "The same CE amplifier ($R_{in} = 5$ kΩ, $A_{vo} = -200$, $R_o = 10$ kΩ) is fed from a 10 kΩ source and drives a 10 kΩ load. The resulting $A_v$ and overall gain $G_v$ are:",
     ["$A_v = -100$, $G_v = -33.3$ V/V", "$A_v = -200$, $G_v = -200$ V/V", "$A_v = -66.7$, $G_v = -22.2$ V/V", "$A_v = -100$, $G_v = -100$ V/V"], 0,
       "$A_v = A_{vo}\\times R_L/(R_L+R_o) = -200 \\times 10/20 = -100$; $G_v = A_v \\times R_{in}/(R_{in}+R_{sig}) = -100 \\times 5/15 = -33.3$.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $A_{vo} = -200$, $R_o = 10$ kΩ, $R_L = 10$ kΩ, $R_{in} = 5$ kΩ, $R_{sig} = 10$ kΩ.
Governing laws:
$$A_v = A_{vo}\frac{R_L}{R_L + R_o} \qquad G_v = A_v\frac{R_{in}}{R_{in} + R_{sig}}$$

**Step 2: Full Mathematical Workings**
Step A — gain with the load attached:
$$\frac{R_L}{R_L + R_o} = \frac{10}{10 + 10} = \frac{10}{20} = 0.5$$
$$A_v = -200 \times 0.5 = -100\ V/V$$
Step B — overall gain with the source resistance:
$$\frac{R_{in}}{R_{in} + R_{sig}} = \frac{5}{5 + 10} = \frac{5}{15} = \frac{1}{3}$$
$$G_v = -100 \times \frac{1}{3} = -33.3\ V/V$$

**Step 3: Verification & Physical Interpretation**
Both loading effects matter for a BJT stage: the load halves the gain, and the source divider cuts it by a further factor of 3. Equivalently, $G_v = -g_m(R_C \parallel R_L) \times r_\pi/(r_\pi + R_{sig}) = -20m \times 5k \times 1/3 = -33.3$ — identical.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student ignores BOTH loading effects (reports $A_{vo}$).
- **Option C trap**: the student uses $R_{in} = 10$ kΩ (includes $R_{sig}$ wrongly).
- **Option D trap**: the student applies only the load effect, forgetting the source divider.
r""")

calc(T, "If the peak $v_{be}$ is to be limited to 5 mV (in the same amplifier: $r_\\pi = 5$ kΩ, $R_{sig} = 10$ kΩ, $G_v = -33.3$), the allowed peak $v_{sig}$ and the resulting load output are:",
     ["$v_{sig} = 15$ mV, $v_o = -0.5$ V", "$v_{sig} = 5$ mV, $v_o = -0.167$ V", "$v_{sig} = 10$ mV, $v_o = -0.333$ V", "$v_{sig} = 25$ mV, $v_o = -0.833$ V"], 0,
       "$v_{be} = v_{sig}\\times r_\\pi/(r_\\pi+R_{sig}) = v_{sig}/3$ ⇒ $v_{sig} = 15$ mV; $v_o = G_v v_{sig} = -33.3 \\times 15m = -0.5$ V.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Identification of Given Parameters and Governing Laws**
Given: $v_{be,max} = 5$ mV, $r_\pi = 5$ kΩ, $R_{sig} = 10$ kΩ, $G_v = -33.3$.
Governing laws:
$$v_{be} = v_{sig}\frac{r_\pi}{r_\pi + R_{sig}} \qquad v_o = G_v v_{sig}$$

**Step 2: Full Mathematical Workings**
Step A — input division factor:
$$\frac{r_\pi}{r_\pi + R_{sig}} = \frac{5}{15} = \frac{1}{3}$$
Step B — allowed source amplitude:
$$5\ mV = v_{sig} \times \frac{1}{3}$$
$$v_{sig} = 15\ mV$$
Step C — output amplitude across the load:
$$v_o = -33.3 \times 15 \times 10^{-3}$$
$$v_o = -0.5\ V$$

**Step 3: Verification & Physical Interpretation**
The source must supply 15 mV because only one-third of it reaches the base-emitter junction; the 33.3-fold overall gain then produces a 0.5 V output swing. Keeping $v_{be} \le 5$ mV preserves the small-signal (linear) assumption.

**Step 4: Breakdown of Wrong Options / Common Student Mistakes**
- **Option B trap**: the student equates $v_{sig}$ with $v_{be}$ (forgets the divider).
- **Option C trap**: the student uses a ½ divider (wrong $r_\pi$).
- **Option D trap**: the student uses $v_{be,max} = 8.3$ mV (divides 25 by 3 instead of multiplying 5 by 3).
r""")

theory(T, "Which small-signal model should be used for a common-collector (emitter-follower) analysis, and why?",
       ["The T model — with $r_e$ in the emitter leg, the follower's gain $R_E/(R_E + r_e)$ falls out of a simple voltage divider",
        "The hybrid-π model only — the T model cannot handle followers",
        "Neither — followers must be analysed with the full nonlinear equations",
        "The MOSFET model, because followers are field-effect circuits"], 0,
       "The T model places r_e directly in the emitter, turning the follower into a voltage divider.",
       r"""### Step-by-Step Derivation & Solution

**Step 1: Core Principle**
In the T model the BJT is represented with $r_e = V_T/I_E$ in series with the EMITTER lead and a current source $i_e$ in the collector–emitter path. For the common-collector stage (signal into the base, output at the emitter through $R_E$), the circuit reduces to the divider $R_E/(R_E + r_e)$:
$$A_v = \frac{R_E}{R_E + r_e} \approx 1$$

**Step 2: Testing the Options**
- **Option A (correct)**: T model + the one-line divider result.
- **Option B (wrong)**: both models are exact and interchangeable; the T model is merely CLEANER here.
- **Option C (wrong)**: small-signal analysis is precisely what linearised models are for.
- **Option D (wrong)**: followers exist for BJTs too — this is the emitter follower.

**Step 3: Exam Trap Summary**
The trap is model rigidity. Both hybrid-π and T are always valid; the exam skill is choosing the one that makes the algebra trivial: T for emitter-in-common circuits (CC, CB), hybrid-π for base-in-common analysis (CE).
r""")
