# -*- coding: utf-8 -*-
"""EEE 252 (Analog Electronics & Circuit Analysis) — PART A.
Topic metadata: core equations (LaTeX), key assumptions, mnemonics and
examiner traps. Anchored to Sedra & Smith, Microelectronic Circuits (8th ed.)
chapters 4–7 & 2, per the 252 lecture materials."""

TOPICS = [
{
"id": "eee252-diodes",
"name": "Diode Circuits & Diode I-V Characteristics",
"summaryNotes": r"""
### Key Abstractions & Principles
- A diode is a two-terminal nonlinear element: it conducts easily in the forward direction and blocks reverse current up to breakdown. The pn junction is formed by joining p-type and n-type semiconductors; current is carried by diffusion of majority carriers across the junction.
- The exponential (Shockley) model is the physical law of the diode. The piecewise-linear model (0.7 V battery + small resistance) is its practical approximation, and the ideal model (short when conducting, open when blocking) is used for first-pass circuit decisions.
- The Zener diode is designed to operate in REVERSE breakdown at a precise voltage $V_Z$; it is the heart of simple voltage regulators. Breakdown mechanisms: Zener (tunnelling, $V_Z < 5$ V) and avalanche (impact ionisation, $V_Z > 7$ V).
- Dynamic (small-signal) resistance $r_d$ describes the diode's response to small AC perturbations about a DC bias point — the basis of incremental analysis.

### Core Mathematical Relations
- $i_D = I_S(e^{v_D/V_T} - 1)$ : Shockley equation; $I_S$ = saturation current ($10^{-14}$–$10^{-15}$ A), $V_T = kT/q \approx 25$ mV at room temperature.
- $r_d = \frac{V_T}{I_D}$ : dynamic resistance at DC bias current $I_D$ (e.g. 25 Ω at 1 mA).
- $v_{D2} - v_{D1} = V_T \ln\frac{i_{D2}}{i_{D1}}$ : voltage change per decade/ratio of current — the tool for diode-string problems.
- Piecewise-linear model: conducting diode $=$ battery $V_{D0} = 0.7$ V in series with $r_D$; blocking diode $=$ open circuit.
- Zener regulator: $V_Z = V_{Z0} + r_z I_Z$; design uses $I_{Z(min)} \ge I_{ZK}$ and $I_{Z(max)} = I_{S(max)} - I_{L(min)}$.

### Key Approximations & Assumptions
- $v_D = 0.7$ V assumed whenever the diode conducts (silicon); drop the exponential detail.
- $V_T = 25$ mV at room temperature; use $V_T \ln(10) \approx 57.5$ mV per decade of current.
- Reverse-biased diode: $i_D = 0$ (ideal) until $v_D = -V_Z$ (zener).
- A diode conducts only if the circuit would otherwise push its anode above its cathode by $\ge 0.7$ V — always START by assuming a state, solve, then VERIFY the assumption.

### High-Yield Recall Tips & Mnemonics
- "Anode Above Cathode — Allow Current": the arrow of the symbol points in the direction of forward current.
- "1 mA → 25 Ω": remember the room-temperature dynamic resistance instantly ($r_d = 25$ mV/1 mA).
- "0.7 for silicon, 0.3 for germanium" — silicon dominates exam circuits.
- For "which diode is ON" problems: the diode with the LARGEST forward voltage difference wins first.

### Common Examiner Pitfalls & Exam Traps
- Trap 1: Forgetting the $-1$ in the Shockley equation — only matters for $v_D$ near 0; for $v_D \gg V_T$ use $i_D \approx I_S e^{v_D/V_T}$.
- Trap 2: Using $r_d = V_T/I_D$ with the WRONG current — always the DC bias current, not the signal current.
- Trap 3: Assuming both diodes in a multi-diode circuit conduct — usually one steals all the current; verify each assumption.
- Trap 4: Sign errors in clampers/strings: track the polarity the capacitor charges to, and re-derive, never guess.
"""
},
{
"id": "eee252-rectifiers",
"name": "Rectification & Power Supply Design",
"summaryNotes": r"""
### Key Abstractions & Principles
- Rectification converts AC into pulsating DC. Half-wave uses one diode (conducts on alternate half-cycles); full-wave uses two diodes with a centre-tapped transformer, and the bridge uses four diodes with no centre tap.
- The ripple factor measures the AC content remaining in the output: $\gamma = V_{r(rms)}/V_{DC}$. Lower is better; a capacitor filter across the load smooths the output by storing charge on peaks and releasing it between peaks.
- PIV (peak inverse voltage) is the maximum reverse voltage a diode must block — the key design spec for choosing diodes.
- A DC power supply chain: transformer → rectifier → capacitor filter → (optional) zener/IC regulator → load.

### Core Mathematical Relations
- Half-wave: $V_{DC} = \frac{V_m}{\pi} = 0.318V_m$; ripple factor $\gamma = 1.21$ (121%); efficiency $\eta = 40.6\%$; PIV $= V_m$.
- Full-wave (centre-tap AND bridge): $V_{DC} = \frac{2V_m}{\pi} = 0.636V_m$; $\gamma = 0.48$ (48%); $\eta = 81.2\%$; PIV $= 2V_m$ (centre-tap) or $V_m$ (bridge).
- Ripple voltage with capacitor filter: $V_r \approx \frac{I_L}{2fC}$ (full-wave) and $V_r \approx \frac{I_L}{fC}$ (half-wave), where $f$ = line frequency.
- $V_m = \sqrt{2}\,V_{rms}$; output frequency $= f$ (half-wave) or $2f$ (full-wave).
- Regulator design: $R_S = \frac{V_{S(min)} - V_Z}{I_{Z(min)} + I_{L(max)}}$.

### Key Approximations & Assumptions
- Ideal diodes (zero drop) unless the question specifies 0.7 V.
- $V_r \ll V_m$ so the output is nearly DC; the diode conducts only for a short "conduction angle" near the peak.
- Transformer losses, diode resistance and load regulation of the capacitor are neglected unless stated.

### High-Yield Recall Tips & Mnemonics
- "Bridge = 4 diodes = 1 PIV; Centre-tap = 2 diodes = 2 PIV." The bridge is kinder to diodes; the centre-tap is kinder to diode count.
- "Full-wave halves the ripple": 121% → 48%.
- "0.318 and 0.636" — the two DC averages; full-wave is exactly double.
- Ripple frequency doubles in full-wave: 50 Hz in, 100 Hz out.

### Common Examiner Pitfalls & Exam Traps
- Trap 1: Quoting PIV = $2V_m$ for a BRIDGE — it is $V_m$ for the bridge and $2V_m$ only for the centre-tapped circuit.
- Trap 2: Confusing $V_{DC}$ with $V_{rms}$ — DC value uses $V_m/\pi$ (or $2V_m/\pi$), not 0.707.
- Trap 3: Using the wrong ripple frequency in the capacitor formula ($f$ vs $2f$).
- Trap 4: Forgetting the factor $\sqrt{2}$ when a transformer secondary is given in r.m.s. volts.
"""
},
{
"id": "eee252-mosfet",
"name": "MOSFETs & NMOS Technology",
"summaryNotes": r"""
### Key Abstractions & Principles
- The MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a voltage-controlled device: the gate voltage controls the conducting channel between drain and source. NMOS uses an n-channel (electrons), PMOS a p-channel (holes).
- Regions of operation: CUTOFF (no channel, $i_D = 0$), TRIODE (channel exists, $V_{DS}$ small — behaves like a voltage-controlled resistor), and SATURATION (channel pinched off at the drain — behaves like a voltage-controlled current source).
- Process parameters: oxide capacitance per unit area $C_{ox} = \varepsilon_{ox}/t_{ox}$ and the transconductance parameter $k'_n = \mu_n C_{ox}$. Device parameter $k_n = k'_n (W/L)$.
- Channel-length modulation ($\lambda$) makes $i_D$ rise slightly with $V_{DS}$ in saturation — it is the MOSFET analogue of the BJT's Early effect. The body effect raises $V_t$ when the source is above the body.

### Core Mathematical Relations
- Cutoff: $V_{GS} < V_t \Rightarrow i_D = 0$.
- Triode: $i_D = k_n\left[(V_{GS}-V_t)V_{DS} - \frac{V_{DS}^2}{2}\right]$ for $V_{DS} \le V_{GS} - V_t$.
- Saturation: $i_D = \frac{1}{2}k_n(V_{GS}-V_t)^2\,(1+\lambda V_{DS})$ for $V_{DS} \ge V_{OV} = V_{GS}-V_t$.
- Overdrive voltage $V_{OV} = V_{GS} - V_t$; minimum $V_{DS}$ for saturation is $V_{DS} = V_{OV}$.
- $C_{ox} = \frac{\varepsilon_{ox}}{t_{ox}}$; $k'_n = \mu_n C_{ox}$; $k_n = k'_n\frac{W}{L}$.
- Triode small-$V_{DS}$ resistance: $r_{DS} \approx \frac{1}{k_n V_{OV}}$.

### Key Approximations & Assumptions
- $V_{GS} > V_t$ AND $V_{DS} \ge V_{GS} - V_t$ ⇔ saturation. These two inequalities are the whole game — always test both.
- $\lambda = 0$ (ignore channel-length modulation) unless the question gives a value.
- For hand analysis take $V_t$ constant (neglect body effect) unless explicitly asked.
- $V_{OV}$ is the "excess" gate voltage; a MOSFET at the edge of saturation has $V_{DS} = V_{OV}$.

### High-Yield Recall Tips & Mnemonics
- "Cut–Tri–Sat" in order of increasing $V_{DS}$.
- "Square law in saturation": $i_D \propto (V_{GS}-V_t)^2$ — doubling $V_{OV}$ quadruples $i_D$.
- "$V_{OV}$ is the king": $g_m = 2I_D/V_{OV}$, maximum gain $= 2V_{DD}/V_{OV}$ class results all route through it.
- NMOS "arrow points iN"; PMOS "arrow Points out" — remember which is which.

### Common Examiner Pitfalls & Exam Traps
- Trap 1: Testing only $V_{GS} > V_t$ and forgetting the second saturation test $V_{DS} \ge V_{OV}$.
- Trap 2: Unit confusion: $k'_n$ in $\mu A/V^2$ vs $k_n = k'_n(W/L)$; $C_{ox}$ in fF/µm² needs $t_{ox}$ in the SAME length unit.
- Trap 3: Using triode equations in saturation (or vice-versa) after misjudging the region.
- Trap 4: Forgetting $(1+\lambda V_{DS})$ when $\lambda$ is given, or including it when $\lambda = 0$.
"""
},
{
"id": "eee252-bjt",
"name": "Bipolar Junction Transistors (BJTs)",
"summaryNotes": r"""
### Key Abstractions & Principles
- The BJT is a current-controlled device: a small base current controls a large collector current. Three terminals: emitter, base, collector; two junctions: emitter–base (EBJ) and collector–base (CBJ).
- Modes of operation are set by junction biases: ACTIVE (EBJ forward, CBJ reverse — amplifier), SATURATION (both forward — switch ON), CUTOFF (both reverse — switch OFF), and reverse-active (rare).
- The Early effect: $i_C$ rises slightly with $v_{CE}$ in the active mode, described by the Early voltage $V_A$ — all $i_C$–$v_{CE}$ lines extrapolate to $-V_A$ on the voltage axis.
- DC biasing sets the quiescent point Q; the assume–solve–verify cycle is mandatory: assume active, compute, then check $V_{CE} > V_{CE(sat)}$ and $i_B > 0$.

### Core Mathematical Relations
- Active mode: $i_C = I_S e^{v_{BE}/V_T}$, $i_C = \beta i_B$, $i_E = (\beta+1)i_B = i_C + i_B$.
- $\alpha = \frac{\beta}{\beta+1}$, $\beta = \frac{\alpha}{1-\alpha}$; typically $\alpha \approx 0.99$, $\beta \approx 100$.
- $i_C = I_S e^{v_{BE}/V_T}(1 + \frac{v_{CE}}{V_A})$ : Early-effect form; $r_o = \frac{V_A}{I_C}$.
- Fixed bias: $I_B = \frac{V_{CC} - V_{BE}}{R_B}$, $I_C = \beta I_B$, $V_{CE} = V_{CC} - I_C R_C$.
- Saturation: $V_{CE(sat)} \approx 0.2$ V; forced $\beta_{forced} = \frac{I_C}{I_B} < \beta$.
- Saturation-mode current: $i_C = I_S e^{v_{BE}/V_T} - \frac{I_S}{\alpha_R}e^{v_{BC}/V_T}$ (second term when CBJ conducts).

### Key Approximations & Assumptions
- $V_{BE} = 0.7$ V whenever the EBJ conducts; $V_T = 25$ mV.
- Active mode requires $V_{BE} = 0.7$ V AND $V_{CE} \ge 0.2$–$0.3$ V; check both after solving.
- "Very high β" ⇒ $i_B \approx 0$, $i_E \approx i_C$ — solve the base circuit by inspection of voltages.
- Neglect Early effect unless $V_A$ is given.

### High-Yield Recall Tips & Mnemonics
- "EBJ forward + CBJ reverse = ACTIVE" — the amplifier state.
- "$V_{CE} \approx 0.2$ V means saturated; $V_{BE} < 0.7$ V means cutoff."
- "$\alpha$ is close to 1, $\beta$ is the gain" — $\alpha = \beta/(\beta+1)$.
- "Fixed bias is β-UNSTABLE": $I_C$ scales directly with $\beta$ — the exam's favourite criticism question.

### Common Examiner Pitfalls & Exam Traps
- Trap 1: Solving with active-mode equations and never verifying the mode — the #1 error in bias questions.
- Trap 2: Forgetting $V_{CE} = V_{CC} - I_C(R_C + R_E)$ when an emitter resistor is present.
- Trap 3: Using $\beta$ for an emitter-follower current ($i_E = (\beta+1)i_B$, not $\beta i_B$).
- Trap 4: In saturation, treating $i_C = \beta i_B$ — it is no longer valid; use $V_{CE(sat)}$ and circuit constraints.
"""
},
{
"id": "eee252-small-signal",
"name": "Small-Signal Models & Equivalent Circuits",
"summaryNotes": r"""
### Key Abstractions & Principles
- Small-signal analysis separates a circuit into its DC bias (quiescent point) and a small AC perturbation about it. Replace each transistor with its small-signal model, kill DC sources (voltage → short, current → open), and analyse the linear circuit.
- The hybrid-π model (BJT): input resistance $r_\pi$ between base and emitter, a voltage-controlled current source $g_m v_\pi$ at the output, and $r_o$ accounting for the Early effect. The T model is its exact dual, with $r_e$ in the emitter leg — use whichever makes the node analysis cleaner.
- The MOSFET model is the same hybrid-π without the base current: infinite input resistance, $g_m v_{gs}$ current source, $r_o = 1/(\lambda I_D)$.
- Key parameter formulas must be computed at the BIAS point (using $I_C$ or $I_D$).

### Core Mathematical Relations
- BJT: $g_m = \frac{I_C}{V_T}$; $r_\pi = \frac{\beta}{g_m} = \frac{V_T}{I_B}$; $r_e = \frac{\alpha}{g_m} = \frac{V_T}{I_E} \approx \frac{25\,\text{mV}}{I_E}$; $r_o = \frac{V_A}{I_C}$.
- MOSFET: $g_m = \frac{2I_D}{V_{OV}} = k_n V_{OV} = \sqrt{2k_n I_D}$; $r_o = \frac{1}{\lambda I_D}$.
- Common-source / common-emitter gain: $A_v = -g_m(R_D \parallel R_L \parallel r_o)$ / $-g_m(R_C \parallel R_L)$.
- $R_{in} = R_G \parallel R_{in,gate}$ (MOS, $\infty$) or $R_B \parallel r_\pi$ (BJT); $R_{out} = R_D \parallel r_o$.
- Overall gain with source resistance: $G_v = \frac{R_{in}}{R_{in}+R_{sig}} A_v$.

### Key Approximations & Assumptions
- Signals are small enough that the transistor stays linear about Q ($v_{be} \le 10$ mV for BJT; $v_{gs} \ll 2V_{OV}$ for MOS).
- $r_o$ is ignored (open circuit) unless $\lambda$/$V_A$ is given.
- Coupling and bypass capacitors are AC short circuits at signal frequency.
- $g_m$ in mA/V when $I_C$/$I_D$ in mA and $V_T$ in mV: $g_m = I_C/25$.

### High-Yield Recall Tips & Mnemonics
- "40 mA/V per mA": $g_m = I_C/V_T$ ⇒ 1 mA of collector current gives 40 mA/V transconductance.
- "T for Trouble-free emitter equations" — use the T model whenever the emitter node is shared.
- "Voltage in, current out = transconductance": $g_m$ is the heart of every gain formula.
- "The 25 mV rule": $r_e = 25/I_E$(mA) and $r_d = 25/I_D$(mA) — the same physics, two devices.

### Common Examiner Pitfalls & Exam Traps
- Trap 1: Computing $g_m$ with signal current instead of BIAS current.
- Trap 2: Omitting $r_\pi$ (or $r_e$) loading in multi-stage or source-loaded calculations.
- Trap 3: Wrong sign conventions — CS/CE invert ($-g_mR$); followers don't.
- Trap 4: Forgetting $R_{sig}$ when the question asks for OVERALL gain $G_v$, not $A_v$.
"""
},
{
"id": "eee252-opamp",
"name": "Operational Amplifiers (Op-Amps)",
"summaryNotes": r"""
### Key Abstractions & Principles
- The op-amp is a very high-gain differential amplifier used with negative feedback to build precision linear circuits. Ideal assumptions: infinite open-loop gain $A$, infinite input impedance, zero output impedance, infinite bandwidth.
- The VIRTUAL SHORT: with negative feedback and an ideal op-amp, $v_+ = v_-$ and zero current flows into either input. This single idea solves nearly every op-amp exam circuit.
- Real (non-ideal) op-amps: finite gain $A$ (typically $10^5$–$10^6$), finite bandwidth (gain–bandwidth product), input offset voltage/current, finite CMRR.
- CMRR quantifies the rejection of common-mode signals: $CMRR = |A_d/A_{cm}|$; in dB, $CMRR_{dB} = 20\log_{10}CMRR$.

### Core Mathematical Relations
- Inverting amplifier: $\frac{v_o}{v_i} = -\frac{R_2}{R_1}$; input resistance $= R_1$.
- Non-inverting amplifier: $\frac{v_o}{v_i} = 1 + \frac{R_2}{R_1}$; input resistance $\approx \infty$.
- Summing amplifier: $v_o = -R_f\left(\frac{v_1}{R_1} + \frac{v_2}{R_2} + \cdots\right)$.
- Difference amplifier: $v_o = \frac{R_2}{R_1}(v_2 - v_1)$ (with matched pairs).
- Integrator: $v_o(t) = -\frac{1}{RC}\int_0^t v_i(\tau)\,d\tau + v_o(0)$; transfer $T(s) = -\frac{1}{sRC}$.
- Differentiator: $v_o(t) = -RC\frac{dv_i}{dt}$; $T(s) = -sRC$.
- First-order low-pass (inverting): $T(s) = -\frac{R_2/R_1}{1 + sR_2C}$; DC gain $= -R_2/R_1$; cutoff $\omega_0 = 1/(R_2C)$.
- General 2nd-order active filter: $T(s) = \frac{K}{s^2/\omega_0^2 + s/(Q\omega_0) + 1}$ — read off $K$, $Q$, $\omega_0$.

### Key Approximations & Assumptions
- Ideal op-amp: $A \to \infty$ ⇒ $v_+ = v_-$ and $i_+ = i_- = 0$ (with negative feedback).
- Output never saturates: $|v_o| < V_{supply}$ — check in clipping questions.
- Capacitors: impedance $1/sC$; for steady-state AC use $s = j\omega$.
- Filter type is read from the limiting behaviour: $T(0)$ and $T(\infty)$.

### High-Yield Recall Tips & Mnemonics
- "Inverting = minus R2 over R1; non-inverting = one plus R2 over R1."
- "Summing at the inverting node gives a weighted negative sum."
- "Integrator = 1/s; differentiator = s" — poles and zeros in plain sight.
- "Low-pass passes DC ($s \to 0$); high-pass passes $\infty$ ($s \to \infty$)": test $T(0)$ and $T(\infty)$ to identify the filter.

### Common Examiner Pitfalls & Exam Traps
- Trap 1: Applying the virtual short when the feedback is POSITIVE (or absent) — it requires negative feedback.
- Trap 2: Writing the inverting gain without the minus sign.
- Trap 3: Mixing up $Q$ and $\omega_0$ in second-order filters — read them from the standard form's coefficients.
- Trap 4: Forgetting the initial condition / constant of integration in integrator problems.
"""
},
]
