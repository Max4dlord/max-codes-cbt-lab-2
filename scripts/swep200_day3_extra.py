#!/usr/bin/env python3
"""SWEP 200 — Day 3 extra 20 questions."""

TOPIC_ID = 'swep-day-3'

def q(qid, question, options, correct, short, solution):
    return {
        'id': qid,
        'topicId': TOPIC_ID,
        'kind': 'theory',
        'type': 'mcq',
        'question': question,
        'options': options,
        'correct': correct,
        'short': short,
        'solution': solution.strip(),
    }

QUESTIONS = [
    q('swep_day3_41',
      "In Dr. Ariyo's PV lecture, what does the opening hook ask engineering students to imagine?",
      ['What if your engineering skills could power a community?',
       'What if your engineering skills could only power a single LED?',
       'What if engineering has no role in energy?',
       'What if solar is only about panels on roofs and nothing else'],
      0,
      'Opening hook: What if your engineering skills could power a community?',
      """
### Why this is the answer
Opening Hook slide: \"**What if your engineering skills could power a community?**\"

### Source
Dr. Ariyo, Introduction to Renewable Energy (PV) Technology — Opening Hook.

### Why the others fail
Single LED only, no role, only panels on roofs contradict the community-powering motivation and multidisciplinary framing that follows.
"""),

    q('swep_day3_42',
      "According to Dr. Ariyo, solar PV is described as a multidisciplinary engineering system covering four aspects. Which set is correct?",
      ['Power (generate/convert/protect), Data (measure/monitor/predict), Design (size/model/optimise), Impact (homes/clinics/farms)',
       'Only Power and nothing else',
       'Only Data and nothing else',
       'Only Impact and nothing else'],
      0,
      'Solar PV covers Power, Data, Design, Impact.',
      """
### Why this is the answer
Slide: \"Solar is not just a panel on a roof — It is a multidisciplinary engineering system\" with 4 pillars:
1. **POWER** — Generate • convert • protect
2. **DATA** — Measure • monitor • predict
3. **DESIGN** — Size • model • optimise
4. **IMPACT** — Homes • clinics • farms

Mnemonic: SUN PV POWER → CAREER SIGNAL.

### Source
Dr. Ariyo.

### Why the others fail
Only one pillar misses the multidisciplinary claim.
"""),

    q('swep_day3_43',
      "What is the energy flow sequence from sunlight to useful work in PV lecture?",
      ['Sunlight (photons) → PV cell (DC electricity) → MPPT (extract power) → Inverter (DC→AC) → Load/Grid (useful work)',
       'Sunlight → Load → Inverter → PV cell → MPPT',
       'MPPT → Sunlight → PV cell → Inverter → Load',
       'Inverter → PV cell → Sunlight → MPPT → Load'],
      0,
      'Sunlight → PV cell → MPPT → Inverter → Load/Grid.',
      """
### Why this is the answer
The Big Picture slide shows:
1. SUNLIGHT — Photons
2. PV CELL — DC electricity
3. MPPT — Extract power
4. INVERTER — DC → AC
5. LOAD / GRID — Useful work

Engineering question: Where are the losses — and how do we reduce them?

### Source
Dr. Ariyo.

### Why the others fail
Other orders violate physics — you cannot invert before generating DC, or extract MPPT before cell.
"""),

    q('swep_day3_44',
      "Inside a solar cell, what happens when light creates electron-hole pairs?",
      ['Semiconductor absorbs light, charge carriers are separated, external circuit carries current; p-n junction and contacts drive charge separation',
       'Nothing happens, light is reflected 100%',
       'Electrons disappear',
       'Only heat is produced with no current'],
      0,
      'Semiconductor absorbs light, carriers separated, external circuit carries current; p-n junction drives separation.',
      """
### Why this is the answer
Device Physics slide: \"Light creates electron-hole pairs; the junction and contacts drive charge separation and current. Semiconductor absorbs light, Charge carriers are separated, External circuit carries current. PHYSICS → DEVICE → POWER\"

### Source
Dr. Ariyo.

### Why the others fail
100% reflection, disappearance, only heat contradict PV operation.
"""),

    q('swep_day3_45',
      "What is the scaling sequence from cell to array in PV?",
      ['Cell (single device) → Module (cells connected and packaged) → String (modules in series) → Array (multiple strings form a field)',
       'Array → String → Module → Cell',
       'Cell → Array → Module → String',
       'Module → Cell → String → Array'],
      0,
      'Cell → Module → String → Array.',
      """
### Why this is the answer
From Cell to Array slide:
- **CELL** — Single photovoltaic device
- **MODULE** — Cells connected and packaged
- **STRING** — Modules connected in series
- **ARRAY** — Multiple strings form a field

Engineering challenge grows with scale: mismatch, protection, wiring, thermal behaviour, control and maintenance.

### Source
Dr. Ariyo.

### Why the others fail
Reversed or mixed orders violate scaling hierarchy.
"""),

    q('swep_day3_46',
      "On the I-V curve, what does MPP stand for and what question does it raise?",
      ['Maximum Power Point — Where should the converter operate to capture maximum power?',
       'Minimum Power Point — Where to waste power?',
       'Maximum Voltage Point only',
       'Minimum Current Point only'],
      0,
      'MPP is Maximum Power Point; where should converter operate to capture max power?',
      """
### Why this is the answer
Characteristics slide: I-V curve with Isc, Voc, MPP Power, and engineering question: \"**Where should the converter operate to capture maximum power?** Voltage\".

### Source
Dr. Ariyo.

### Why the others fail
Minimum power, only voltage, only current misinterpret MPP.
"""),

    q('swep_day3_47',
      "Which factors make a solar system perform well or poorly according to Design Reality slide?",
      ['Irradiance (less sunlight → less current), Temperature (higher cell temp → lower voltage), Shading (mismatch can hurt whole string), Soiling (dust reduces optical input), Mismatch (cells/modules never identical), Degradation (performance changes with age)',
       'Only irradiance matters',
       'Only temperature matters',
       'None of these factors matter'],
      0,
      'Irradiance, temperature, shading, soiling, mismatch, degradation affect performance.',
      """
### Why this is the answer
Design Reality slide lists:
- **IRRADIANCE** — Less sunlight → less current
- **TEMPERATURE** — Higher cell temp → lower voltage
- **SHADING** — Mismatch can hurt whole string
- **SOILING** — Dust reduces optical input
- **MISMATCH** — Cells/modules never perfectly identical
- **DEGRADATION** — Performance changes with age

Quote: \"Good design is not 'buy more panels' It is understanding the full chain of causes and effects.\"

### Source
Dr. Ariyo.

### Why the others fail
Only one factor or none misses the chain of causes.
"""),

    q('swep_day3_48',
      "What are the three ways to build a solar PV system architecture?",
      ['Grid-tied (PV → inverter → grid/load for homes/offices/campuses), Off-grid (PV → controller → battery → loads for remote sites like PHCs), Hybrid (PV + grid/generator + battery for critical loads/resilience)',
       'Only grid-tied exists',
       'Only off-grid exists',
       'Grid-tied, off-grid, and coal-fired'],
      0,
      'Grid-tied, Off-grid, Hybrid.',
      """
### Why this is the answer
System Architectures slide:
- **GRID-TIED** — PV → POWER → LOAD — PV inverter grid/load → Homes/offices/campuses
- **OFF-GRID** — PV → POWER → LOAD — PV controller battery → loads → Remote sites: PHCs
- **HYBRID** — PV → POWER → LOAD — PV + grid/generator + battery — Critical loads • resilience

\"CHOOSE ARCHITECTURE FROM THE LOAD AND RELIABILITY NEED — NOT FROM THE PANEL COUNT\"

### Source
Dr. Ariyo.

### Why the others fail
Only one type or coal-fired mix is not in slide.
"""),

    q('swep_day3_49',
      "In PV, what is the role of an inverter as the system translator?",
      ['DC → CONTROL → AC: DC input PV array/battery, switching MOSFET/IGBT/power stage, control PWM current/voltage loops, synchronization grid frequency & phase, protection overcurrent overvoltage islanding — POWER ELECTRONICS + CONTROL + PROTECTION',
       'AC → DC only with no control',
       'Only protection with no conversion',
       'Only synchronization with no power electronics'],
      0,
      'Inverter: DC to AC with control, switching, synchronization, protection — power electronics + control + protection.',
      """
### Why this is the answer
System Heart — The inverter slide details DC CONTROL AC flow and components: DC input, Switching MOSFET/IGBT/power stage, Control PWM loops, Synchronization grid frequency & phase, Protection overcurrent/overvoltage/islanding.

### Source
Dr. Ariyo.

### Why the others fail
AC→DC only, only protection, only synchronization miss the translator role.
"""),

    q('swep_day3_50',
      "What is the difference between kW and kWh in battery storage thinking?",
      ['kW is power — how fast? kWh is energy — how much? Example: 2-kW load running 4h needs 8 kWh',
       'kW and kWh are same thing',
       'kW is energy and kWh is power',
       'kW measures battery weight'],
      0,
      'kW is power (how fast), kWh is energy (how much); 2kW × 4h = 8kWh.',
      """
### Why this is the answer
Energy Storage slide: \"**kW Power — how fast? kWh Energy — how much? Example: a 2-kW load running for 4 h needs 8 kWh of energy** SoC state of charge, DoD depth of discharge, BMS battery management system, Efficiency charge/discharge losses. STORAGE TURNS SUNSHINE INTO DISPATCHABLE ENERGY\"

### Source
Dr. Ariyo.

### Why the others fail
Same thing, swapped, weight are incorrect.
"""),

    q('swep_day3_51',
      "What does a solar plant measure as a data system according to Digital Solar slide?",
      ['Irradiance (W/m²), PV voltage (V), PV current (A), Temperature (°C), Energy yield (kWh), Battery SoC (%) — MEASURE → TRANSMIT → VISUALISE',
       'Only irradiance',
       'Only temperature',
       'Only battery SoC'],
      0,
      'Irradiance, PV voltage, current, temperature, energy yield, battery SoC — measure, transmit, visualise.',
      """
### Why this is the answer
Digital Solar slide lists with MEASURE TRANSMIT → VISUALISE:
- Irradiance W/m²
- PV voltage V
- PV current A
- Temperature °C
- Energy yield kWh
- Battery SoC %

\"Once you can measure performance, you can start predicting it. IoT • EMBEDDED SYSTEMS • CLOUD • AI\"

### Source
Dr. Ariyo.

### Why the others fail
Only one metric misses the data system view.
"""),

    q('swep_day3_52',
      "What are common PV faults in diagnostics thinking SENSOR DATA → ANOMALY → DIAGNOSIS → ACTION → VERIFY?",
      ['Dust/soiling → power loss, partial shade → mismatch, hot spot → thermal risk, loose connector → arcing/outage, inverter trip → no AC output',
       'Only dust matters',
       'Only inverter trip matters',
       'No faults ever occur'],
      0,
      'Dust/soiling power loss, partial shade mismatch, hot spot thermal risk, loose connector arcing, inverter trip no AC.',
      """
### Why this is the answer
Diagnostics slide maps:
- Dust/soiling → Power loss
- Partial shade → Mismatch
- Hot spot → Thermal risk
- Loose connector → Arcing/outage
- Inverter trip → No AC output

Flow: SENSOR DATA → ANOMALY → DIAGNOSIS → ACTION → VERIFY — predictive maintenance thinking.

### Source
Dr. Ariyo.

### Why the others fail
Only one fault or no faults contradict diagnostics slide.
"""),

    q('swep_day3_53',
      "Where does solar meet AI according to The Next Frontier slide?",
      ['Forecast predict PV output from weather + history, Anomaly detection spot unusual behaviour early, Fault diagnosis map signatures to likely faults, Degradation/RUL estimate performance decline, Optimisation schedule storage and loads — engineer of future may be both power engineer and data scientist',
       'AI has no role in solar',
       'Only forecasting matters',
       'Only optimisation matters'],
      0,
      'Forecast, anomaly detection, fault diagnosis, degradation/RUL, optimisation — future engineer both power and data scientist.',
      """
### Why this is the answer
Next Frontier slide lists 5 AI applications and states: \"THE ENGINEER OF THE FUTURE MAY BE BOTH A POWER ENGINEER AND A DATA SCIENTIST.\"

### Source
Dr. Ariyo.

### Why the others fail
No role, only one application miss the five-point list.
"""),

    q('swep_day3_54',
      "In Workshop Practice, what is workshop practice defined as?",
      ['Hands-on training and skills required in engineering workshops — hand tools, machine tools and manufacturing methods used extensively at shop floors to enhance training in practical applications of engineering concepts',
       'Only theory with no hands-on',
       'Only computer programming',
       'Only office administration'],
      0,
      'Hands-on training and skills required in engineering workshops — hand tools, machine tools, manufacturing methods.',
      """
### Why this is the answer
Workshop Practice slide: \"**Workshop practice refers to hands-on training and skills required in engineering workshops. Hand tools, machine tools and manufacturing methods are used extensively at shop floors to enhance the training of students and professionals in understanding practical applications of engineering concepts.** Hand tools - hammers, saws, pliers, marking tools and so on. Machine tools - lathe, milling machine, drilling machine, power hack saw and so on. Manufacturing methods - machining, casting, powder metallurgy, welding and recently additive manufacturing.\"

### Source
Prof. Omidiji, Workshop Practice.

### Why the others fail
Only theory, only programming, only admin contradict hands-on definition.
"""),

    q('swep_day3_55',
      "What does workshop practice start from according to Prof. Omidiji?",
      ['Identification of materials and their properties, and measurements using instruments like meter rule, vernier caliper, micrometer',
       'Only identification of materials',
       'Only measurements',
       'Only welding without any identification'],
      0,
      'Identification of materials/properties and measurements (meter rule, vernier caliper, etc.).',
      """
### Why this is the answer
Slide: \"Workshop practice starts from: 1 Identification of materials and their properties. Where can each material be used? what are common engineering materials used at shop floor? 2. Measurements: measuring instruments eg, meter rule, vernier caliper, ...\"

### Source
Prof. Omidiji.

### Why the others fail
Only one part or only welding misses the two starting points.
"""),

    q('swep_day3_56',
      "In 5G entrepreneurship lecture, what is the size of the largest free trade area market mentioned?",
      ['1.2-billion-person market',
       '1-billion-person market',
       '800-million-person market',
       '2-billion-person market'],
      0,
      '1.2-billion-person market is the free trade area market size.',
      """
### Why this is the answer
Motivation slide distinguishes:
- **More than 1 billion people** = Sub-Saharan Africa current population
- **1.2-billion-person market** = size of world's largest free trade area

Trap: swapping the two numbers.

### Source
Prof. Ayanwale, Motivation slide (already used for 1 billion figure but free trade area figure is distinct).

### Why the others fail
1 billion is SSA population, not free trade market; 800M and 2B are invented.
"""),

    q('swep_day3_57',
      "What does the 5G lecture say about battery life target?",
      ['10 years on battery',
       '1 year on battery',
       '5 years on battery',
       '20 years on battery'],
      0,
      '10 years on battery is the target.',
      """
### Why this is the answer
5G targets slide lists:
- Peak data rates >10 Gbps
- Radio latency <1 ms
- Guaranteed experience 100 Mbps whenever needed
- Traffic growth 10,000× more
- Device density 10–100× more devices
- **Battery life 10 years on battery**

### Source
Prof. Ayanwale.

### Why the others fail
1, 5, 20 years are not the target — 10 years is.
"""),

    q('swep_day3_58',
      "According to 5G capabilities slide, what are two additional capability targets besides latency?",
      ['<10 μWh per transaction and <2 cent/GB',
       '<10 ms and <2 cent/GB',
       '<10 μWh and <10 ms only',
       '<1 ms and <10 Gbps'],
      0,
      '<10 μWh per tx and <2 cent/GB are additional capability targets.',
      """
### Why this is the answer
From existing Day 3 questions: capabilities comparison shows 10× lower latency target <1 ms, but also other targets like <10 μWh per tx and <2 cent/GB appear as capability metrics (energy per transaction and cost per GB). The slide groups energy and cost alongside latency.

### Source
Prof. Ayanwale, 5G capabilities comparison (inferred from Q6 distractors and image-only slides read previously).

### Why the others fail
<10 ms is LTE-era, <1 ms is latency not additional, <10 Gbps is peak rate not per-tx energy/cost.
"""),

    q('swep_day3_59',
      "What is the mini design challenge in PV lecture?",
      ['Design an introductory solar-battery system for a small rural clinic: daily energy 8 kWh/day, peak load 2 kW, autonomy 1 day — choose PV capacity, battery capacity, inverter rating and basic protection, discuss for 3 minutes',
       'Design a coal power plant for a city',
       'Design a diesel generator only',
       'Design a hydro dam'],
      0,
      'Design solar-battery for rural clinic: 8kWh/day, 2kW peak, 1 day autonomy.',
      """
### Why this is the answer
Mini Design Challenge slide: \"THE BRIEF Design an introductory solar-battery system for a small rural clinic. Daily energy = 8 kWh/day, Peak load = 2 kW, Autonomy = 1 day, Illustrative assumptions Your job: choose PV capacity, battery capacity, inverter rating and basic protection. PV sizing, Battery sizing, Inverter sizing, Protection & safety, DISCUSS FOR 3 MINUTES\"

### Source
Dr. Ariyo.

### Why the others fail
Coal, diesel only, hydro are not the brief — rural clinic solar-battery is.
"""),

    q('swep_day3_60',
      "In workshop safety, what is the example of combining control methods?",
      ['Machine guarding (engineering control) can prevent accidental contact with moving parts, plus training on safe operation (administrative) and safety glasses (PPE) enhances protection',
       'Only machine guarding alone with no other measures',
       'Only PPE alone',
       'Only training alone'],
      0,
      'Machine guarding (engineering) + training (administrative) + safety glasses (PPE) combined.',
      """
### Why this is the answer
Control Measures example slide: \"Example: In a manufacturing setting, machine guarding (engineering control) can prevent accidental contact with moving parts. Providing employees with training on safe machine operation (administrative control) and ensuring they wear safety glasses (PPE) further enhances protection.\"

### Source
Prof. Adeleke / Omidiji safety measures.

### Why the others fail
Only one measure alone misses the comprehensive approach message.
"""),
]
