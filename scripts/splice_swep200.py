#!/usr/bin/env python3
"""Splice the SWEP 200 course into src/data.js.

Run from the repo root:  python3 scripts/splice_swep200.py

Idempotent: re-running replaces the existing SWEP 200 block rather than
duplicating it, so you can rebuild after editing swep200_day1.py.

SWEP 200 is CATEGORY-structured (unlike EEE 282, which is flat):
  general    — cross-cutting SWEP/SIWES knowledge
  swep-days  — one topic per orientation day (Day 1 … Day 5)
  lectures   — one topic per individual lecture/presentation

Day 1 currently supplies 44 questions. Days 2-5 and the per-lecture topics are
declared as they arrive; a category with no topics would fail validation, so
only populated categories are emitted.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from swep200_day1 import QUESTIONS as DAY1  # noqa: E402
from swep200_day2 import QUESTIONS as DAY2  # noqa: E402
from swep200_day3 import QUESTIONS as DAY3  # noqa: E402
from swep200_day4 import QUESTIONS as DAY4  # noqa: E402
from swep200_day5 import QUESTIONS as DAY5  # noqa: E402

# Extra 20 per day (100 total) - fresh material not in original bank
try:
    from swep200_day1_extra import QUESTIONS as DAY1_EXTRA
except ImportError:
    DAY1_EXTRA = []
try:
    from swep200_day2_extra import QUESTIONS as DAY2_EXTRA
except ImportError:
    DAY2_EXTRA = []
try:
    from swep200_day3_extra import QUESTIONS as DAY3_EXTRA
except ImportError:
    DAY3_EXTRA = []
try:
    from swep200_day4_extra import QUESTIONS as DAY4_EXTRA
except ImportError:
    DAY4_EXTRA = []
try:
    from swep200_day5_extra import QUESTIONS as DAY5_EXTRA
except ImportError:
    DAY5_EXTRA = []

from swep200_lectures import LECTURES, question_lecture_map  # noqa: E402

DATA = ROOT / 'src' / 'data.js'

COURSE = {
    "id": "swep200",
    "code": "SWEP 200",
    "title": "Students Workshop Experience Programme",
    "heroTagline": "before the assessment",
    "blurb": (
        "Orientation-week preparation for SWEP 200: the NUC/ITF mandate and the "
        "tripartite structure, programme timelines and durations, the history and "
        "spread of the Industrial Training Fund, the SIWES story at OAU, and the "
        "amphitheatre rules you are assessed on. Test yourself across the whole "
        "course, one orientation day, or a single lecture — every question carries "
        "a full explanation traced back to the slide it came from."
    ),
    "accent": "#0F7B3F",
    "available": True,
}

CATEGORIES = [
    {
        "id": "general",
        "name": "General",
        "spansAll": True,
        "blurb": "Shuffled across every SWEP Day and lecture — the full-course mix.",
    },
    {
        "id": "swep-days",
        "name": "SWEP Days",
        "blurb": "Test one orientation day at a time, exactly as it was delivered.",
    },
    {
        "id": "lectures",
        "name": "Lectures & Presentations",
        "blurb": "Drill a single lecture or presentation on its own.",
    },
]

TOPICS = [
    {
        "id": "swep-day-1",
        "name": "Day 1 — Monday, 14th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 1 covered
Three lectures, recorded in the orientation ledger:

| # | Lecture | Speaker |
|---|---|---|
| 1 | Introduction to SWEP & SIWES; scope, durations, rules & regulations | **Prof. O. A. Olojede** |
| 2 | History & spread of the Industrial Training Fund (ITF) in Nigeria | **Prof. M. D. Shittu** |
| 3 | Benefits of Industrial Training for Science & Engineering students | **Prof. E. A. Taiwo** |

### The dates that carry marks
| Year | Event |
|---|---|
| **1971** | ITF established under **Act No. 47**; take-off grant **₦1,000,000 (£500,000)** |
| **1973** | SIWES established by ITF; **OAU (then University of Ife) among the first participants** |
| 1974 | SIWES actually started |
| to 1978 | ITF **fully funded** SIWES |
| **1979** | FME makes a **one-year IT programme compulsory** for Polytechnics/Colleges of Technology |
| **Jan 1980** | ITF **withdraws** from financing SIWES |
| 1980–1984 | **NUC & NBTE** fund the scheme; NBTE renames SIWES **COSITA** |
| **1984** | Scheme **expanded** to sciences, environmental sciences, agriculture; ITF resumes management **Nov 1984** (**IAGR** Dept.) |
| **1985** | **Decree No. 16 of August 1985** gives SIWES legal backing |
| 1987 | Austerity measures + **SAP** — firms stop providing accommodation |
| 1994 | **30% of firms** reject institutional requests; individual-merit applications |
| **1995** | ITF/NUC allocate **3–15 credit units** |
| 2011 | **ITF Amendment Act** — NISDP, WOSEP, STEPP-C, CONSEP, **SUPA** |

### Durations and credit units
- **SWEP 200** — ideally **12 weeks**, strict minimum **8 weeks** (after 200-Level Rain Semester)
- **SIWES I** — 12 weeks, after the **300**-Level Rain Semester
- **SIWES II** — **24 weeks (6 months)**, 400-Level Rain Semester + vacation. **Only SIWES II receives ITF stipends.**
- Polytechnics/Colleges of Education **4 months**; Universities **6 months**
- Credit units: **Year II: 3 · Year III: 3 · Year IV: 9** (Technology & EDM)
- Exempt 4-year programmes: **Architecture, Fine and Applied Arts, Industrial Chemistry**
- **Faculty of Agriculture** — consolidated **1-year 'Farm Year'**

### The daily schedule
| Time | Activity |
|---|---|
| 08:00 – 08:30 | Arrival + **first** attendance check |
| 08:30 – 09:00 | Recap of previous day |
| 09:00 – 10:30 | Lecture 1 |
| 10:30 – 12:00 | Lecture 2 |
| 12:00 – 12:30 | Break — **second check strictly 12:25–12:30** |
| 12:30 – 14:00 | Lecture 3 |

Orientation = **5 days, 14 lectures**. Signing the register for another student
is **handled as a criminal act**.

### ITF structure
**13-member Governing Council**; **15 Departments and 5 Units** at HQ; **42 Area
Offices**; **5 Skills Training Centres**. Four units report straight to the
Director-General: **Legal and Council Affairs, Internal Audit, Public Relations
and Publicity, SERVICOM**.

### Institutions participating in SIWES
| Type | Federal | State | Private |
|---|---|---|---|
| Universities | 56 | 58 | 72 |
| Polytechnics | 78 | **107** | 31 |
| Colleges of Education | 6 | 10 | 6 |
| **Total** | **140** | **175** | **109** |

### Traps to watch
- **SWEP = Students *Workshop* Experience Programme** (not "Work").
- **Act 47 → 1971 → created the ITF.** **Decree 16 → 1985 → backed SIWES.**
- ₦90 is the **1976** allowance, not 1981 (**₦250**).
- Supervisory allowance is **10%** of the student allowance.
- **42** = Area Offices, not HQ units.
- E-SIWES portal is **www.siwesdata.org**; e-payment came from **Yar'Adua's 2009 budget**.
""",
    },
    {
        "id": "swep-day-2",
        "name": "Day 2 — Tuesday, 15th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 2 covered
| # | Lecture | Speaker |
|---|---|---|
| 1 | Substance Abuse Awareness | **Dr. A. Olatunji** |
| 2 | Workshop & Industrial Safety | **Prof. A. A. Adeleke** |
| 3 | 21st-Century Employability Skills | **Prof. A. B. Ekanola** |

### Substance abuse — the numbers
| Measure | Figure |
|---|---|
| Global average use | **5.3%** |
| Nigeria, aged 15–64 | **14.3%** (≈ 14.4 million people) |
| Lifetime prevalence, SW Nigerian universities | **45% – 84.5%** |

Most abused: **alcohol, tobacco, codeine cough syrups, tramadol, cannabis**.

**Five categories of warning sign** — know which is which:
- **Physical** — bloodshot/glassy eyes, weight change, odours, tremors, poor hygiene
- **Behavioural** — new friend groups, secrecy, stealing, **impulsivity/risk-taking**
- **Academic** — absenteeism, falling grades, discipline, **unsubmitted assignments**
- **Psychological/Emotional** — mood swings, anxiety, depression, **hallucinations**
- **Social/Lifestyle** — money trouble, fights/cultism, sleep changes, drug joints

**Prevention** (before) vs **Intervention** (after):
- Prevention: campus drug education, life skills, peer support, restricting access, parents/community
- Intervention: early screening, counselling, medical treatment/rehab, policy & discipline, media campaigns
- **Multi-sectoral collaboration**: **NDLEA**, Federal Ministry of Health, NGOs, campus health services

### Safety — the numbers
- **5,486** US fatal occupational injuries in 2022 (**+5.7%** on 2021)
- **WHO** — large % of workers face hazards; **ILO** — economic costs 4%–6% of GDP
- High-risk: construction, agriculture, mining, manufacturing, healthcare

**PPE standards:**
- US safety glasses: **ANSI Z87.1**, Europe: **EN 166**
- High-visibility: **EN ISO 20471**; Welding: **EN ISO 11611**
- Respirators: **OSHA & NIOSH** — proper selection, fit testing, medical evaluation; **APRs** = air-purifying, **SARs** = supplied-air
- Nuclear PPE: **Tyvek, neoprene, nitrile** + **Anti-C/FR**; symbol = worker in full-body suit + respirator + **trefoil** (yellow/black)

**Hazards:**
- Chemical: toxic, flammable, corrosive
- Physical: noise, vibration, radiation, extreme temps, poor lighting
- Ergonomic: repetitive, awkward postures → musculoskeletal
- Biological: bacteria, viruses, fungi

**Controls (most → least effective):**
Elimination (most effective — remove hazard) → Substitution → Engineering (guarding, ventilation) → Administrative (procedures, training) → PPE (gloves, masks)

Safety signs: Prohibition = circular red border + diagonal line; Warning = triangular yellow/black; Mandatory = blue; Emergency = green; Fire = red.

Extinguishers: **RED** water (Class A), **BLUE** dry powder, **CREAM** foam, **BLACK** CO₂ (multipurpose electrical + liquids, **no residue**). Water types: stored pressure vs gas cartridge.

### Employability
**Definition:** capability to **obtain, retain, perform and progress** in employment. Not just about insufficient jobs — **many graduates are unemployable** (CBN recruitment, German software engineers).

**Agents of global transformation:** AI, automation, digital platforms, globalisation, remote work.

**8 clusters:** Communication/interpersonal, Critical thinking/problem-solving, Digital/technological, Creativity/innovation, Collaboration/teamwork, Personal effectiveness/emotional intelligence, Career management/entrepreneurship/leadership, Adaptability/lifelong learning/professional development.

**Communication:** oral/written, presentation, listening, negotiation, interpersonal, professional correspondence, digital — includes listening, nonverbal, clarity/concision, friendliness, confidence, empathy, open-mindedness, respect, feedback, picking right medium. Acquired through practice: speak/write, present/debate, teach/seminars, professional orgs, reports, feedback, record yourself.

**Critical thinking:** analyse objectively, evaluate evidence, identify assumptions, reach reasoned conclusions. Steps: Identify problem, Research, Determine data relevance, Ask questions, Identify best solution, Present, Analyze decision. Acquired via complex questions, reading widely, comparing perspectives, case studies, debating controversial, solving problems with no obvious answer, changing mind when better evidence.

Puzzles: storm bus stop (woman/man dreams, friend saved life, old ill lady, one seat); farmer fox goose beans boat (goose eats beans or fox eats goose if left unattended).

**Problem-solving:** identifying real problem, gathering info, analysing causes, generating alternatives, evaluating options, implementing, assessing results. Best way = real problems, projects: What problem can I solve today?

**Digital literacy:** basic requirement — use digital communication tools, search/evaluate info, work with digital platforms, manage documents, collaborate online, understand basic data, protect info, use responsibly. Beyond Word/email — sophisticated fluency.

**AI literacy:** what AI can/cannot do, limitations, formulate effective instructions, evaluate outputs, bias, privacy, IP, ethical responsible use. Goal not to compete but **become AI-enabled professional** — future belongs to **AI-enabled professionals** not just AI specialists. Acquired via practical applications: research, brainstorm, analyse, draft/revise, generate ideas, simulate scenarios, support learning, automate routine, improve productivity + human judgement.

**Creativity:** seeing possibilities others may not. **Innovation:** converting ideas into useful outcomes. Requires asking unconventional questions, attending details, analysing, open-mindedness, problem-solving, don't fear failure, assess/negate risks, seek more/better with less. Developed via different disciplines, reading outside field, travel, different perspectives, experiment, question: Is there better way?

**Teamwork:** working well, effective relationships diverse personalities, maturity agree/disagree, focus team goals not individual. Future workplace collaborative, complex problems cannot be solved by one discipline. Requires listening, sharing ideas, negotiation, resolving disagreements, respecting perspectives, coordinating activities. Brilliant individual who cannot work with others = organisational liability. Developed via group projects, student orgs, community service, sports, volunteering, professional associations, multidisciplinary projects, work placements — contribute without dominating.

**Emotional Intelligence:** understanding own emotions and recognising/responding to others — self-awareness, self-regulation, empathy, social awareness, relationship management. Requires internal motivation, self-regulation, self-awareness, empathy, social awareness. All human activities involve people; tech automates processes but relationships remain fundamental. Developed via active listening, receiving criticism without defensive, reflecting behaviour, empathy, observing actions affect others, managing anger/frustration professionally, seeking honest feedback, cultivating self-awareness.

**Social Intelligence:** ability to build, understand, manage, sustain interpersonal relationships — strong competencies, nourishing behaviours making others feel valued, trusted, respected.

**Adaptability & Resilience:** certainty = change, adaptable worker functions effectively despite change. Resilience = ability to recover from setbacks and continue moving forward — career contains rejection, failure, redundancy, organisational change, uncertainty — requires psychological/professional resilience. Developed via outside comfort zone, new skills, unfamiliar challenging assignments, different people, move across disciplines, learn from failure, avoid too comfortable.

**Leadership:** ability to influence people positively towards shared objective — needs vision & integrity, communication & emotional intelligence, decision-making & strategic thinking, collaboration & accountability. Acquired via leading project, organising event, volunteering, mentoring, solving problem, taking responsibility — develops through responsibility and practice.

**Entrepreneurial:** opportunity recognition & initiative, creativity & risk assessment, resourcefulness & financial awareness, networking & negotiation, value creation.

**Time Management:** time audit, block distractions, schedule yourself, avoid multitasking, insist others respect time, keep call to action in mind, get downtime/rest.

**Conflict Management:** ability to identify/manage conflicts sensibly, fairly, efficiently so they don't degenerate into crises but better synergy/teamwork — requires teamwork, problem-solving, emotional intelligence, communication, stress management.

**Ethical/Professional:** integrity & honesty, accountability & respect, confidentiality & responsibility, fairness & professional discipline.

**Career Management:** self-assessment strengths/weaknesses, researching occupations & setting career goals, building professional networks & preparing CVs/portfolios, interview skills & personal branding, networking & finding mentors, evaluating career opportunities.

**Acquisition:** Education & Experience, Practice & Reflection, Mentoring & Networking, Continuous Learning.

**Experiential Learning:** internships & industrial attachments, apprenticeships & volunteering, community & research projects, part-time work & student leadership, entrepreneurial activities — experience converts knowledge into competence.

**Formal Education:** not simply listen/reproduce in exams but solve problems, conduct research, make presentations, participate in debates, undertake projects, work in teams, engage industry, apply knowledge — classroom must become place where students do, not merely listen.

**Project-based learning:** develops teamwork, communication, leadership, creativity, problem-solving, time management, digital competence.

**Mentoring/Coaching:** provides guidance, experience, encouragement, professional insight, networks, constructive criticism.

**Self-Directed Learning:** today individual can learn from universities, professionals, experts, institutions worldwide — online courses, webinars, tutorials, digital libraries, professional communities — create personal learning plan, identify skills needed, set objectives.

**Micro-Credentials:** traditional degrees important but complemented by shorter forms — micro-credentials, professional certificates, short courses help acquire specific competencies quickly. Instead of Degree → employment → retirement, move towards Degree → work → reskill → work → upskill → career transition → lifelong learning.

**Networking:** provides information & mentors, opportunities & collaborations, employment & entrepreneurship, professional development — not only what you know but who knows what you can do. Build via conferences, seminars, professional associations, alumni networks, career fairs, industry events, online professional communities — mutually beneficial relationships.

**Portfolio:** CV tells what you claim you can do, portfolio can demonstrate it — containing research projects, presentations, software projects, designs, business ideas, community projects, certificates, professional achievements, evidence of impact.

**Challenge:** consciously/purposively develop appropriately soft, digital, technical skills — at least one at any point.

**Special Message:** degree is beginning of professional learning. While in university, develop at least five things alongside academic qualification: strong communication ability, digital capability, evidence of practical experience, professional network, learning habit.

**Skills vs Capabilities:** skill = ability to perform particular task; capability = ability to apply knowledge/skills effectively in changing circumstances — e.g., knowing particular software = skill, being able to learn new software when technology changes = capability.

**Future:** not about producing people who know everything (impossible), about producing people who can learn anything they need to know — become digitally capable, intellectually curious, emotionally intelligent, ethically responsible, entrepreneurial, collaborative, creative, adaptable — above all: be lifelong learner.
""",
    },
    {
        "id": "swep-day-3",
        "name": "Day 3 — Wednesday, 16th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 3 covered
| # | Lecture | Speaker |
|---|---|---|
| 1 | Entrepreneurship in the 5G Era | **Prof. A. B. Ayanwale** |
| 2 | Introduction to Renewable Energy (PV) Technology | **Dr. F. K. Ariyo** |
| 3 | Workshop Practice, Workforce & National Growth | **Prof. V. Omidiji** |

### Entrepreneurship in the 5G Era — key numbers
- Sub-Saharan Africa: **more than 1 billion people**, half **under 25 by 2050**; **1.2-billion-person market** = world's largest free trade area
- **Five mobile generations in 40 years**: 1G AMPS/TACS/NMT 1980s (foundation telephony), 2G GSM/D-AMPS/PDC/IS-95 1990s (telephony for everybody), 3G WCDMA/HSPA/cdma2000 2000s (foundation mobile broadband), 4G LTE 2010s (further enhanced broadband), 5G **NR** 2020s (interconnected devices, sensors, systems — verticals)
- **Three superpowers**: **eMBB** = insanely high speeds, massive bandwidth — firehose for data — "content and data delivery" superpower; **URLLC** = near-instantaneous response **~1ms** with extreme reliability — "real-time control and safety" superpower — autonomous drone fleets, tele-surgery, competitive gaming; **mMTC** = staggering number low-power devices simultaneously — "massive data collection" superpower — smart agriculture thousands sensors, asset tracking, billions smart-city devices
- **5G targets**: **>10 Gbps** peak data rates, **<1 ms** radio latency, **100 Mbps** guaranteed whenever needed, **10,000×** more traffic, **10–100×** more devices, **10 years** on battery; **10× lower latency** target **<1 ms**; additional capability targets **<10 μWh per tx**, **<2 cent/GB**
- Motivation: very young, very large, newly integrated market = condition where digital ventures scale

### PV Technology — the chain
**Opening Hook:** "What if your engineering skills could power a community?" Solar is not just panel on roof — multidisciplinary system: **POWER** Generate•convert•protect, **DATA** Measure•monitor•predict, **DESIGN** Size•model•optimise, **IMPACT** Homes•clinics•farms. Career signal: degree → solar specialisation: Electrical = power systems, Electronics = converters/sensors/embedded, Control = MPPT/regulation, Automation = AI/Data forecasting/fault diagnosis, Materials = semiconductors/PV devices, Enterprise = design/installation/service/finance.

**Energy flow:** SUNLIGHT photons → PV CELL DC electricity → MPPT extract power → INVERTER DC→AC → LOAD/GRID useful work. Engineering question: Where are losses — how reduce?

**Device physics:** p-type n-type p–n junction, photon creates electron-hole pairs, junction/contacts drive charge separation and current. Semiconductor absorbs light, carriers separated, external circuit carries current. PHYSICS → DEVICE → POWER.

**Scaling:** CELL single device → MODULE cells connected/packaged → STRING modules in series → ARRAY multiple strings field. Challenge grows: mismatch, protection, wiring, thermal, control, maintenance.

**I–V curve:** Isc, Voc, MPP Power. Engineering question: Where should converter operate to capture maximum power? Voltage.

**MPPT:** Irradiance changes, temperature changes, maximum-power point moves → PV ARRAY variable DC → MPPT CONTROLLER search/track → DC BUS regulated energy → INVERTER controlled AC — CONTROL SYSTEMS + POWER ELECTRONICS.

**Design Reality:** IRRADIANCE less sunlight → less current, TEMPERATURE higher cell temp → lower voltage, SHADING mismatch can hurt whole string, SOILING dust reduces optical input, MISMATCH cells/modules never perfectly identical, DEGRADATION performance changes with age. Good design is not "buy more panels" — understanding full chain of causes/effects.

**Architectures:** GRID-TIED PV inverter grid/load → Homes/offices/campuses, OFF-GRID PV controller battery → loads → Remote sites: PHCs, HYBRID PV + grid/generator + battery → Critical loads/resilience. CHOOSE ARCHITECTURE FROM LOAD AND RELIABILITY NEED — NOT PANEL COUNT.

**Components:** PV module, inverter, MPPT charge controller, battery storage, protection/distribution. Inverter = system translator: DC CONTROL AC — DC input PV array/battery, Switching MOSFET/IGBT/power stage, Control PWM current/voltage loops, Synchronization grid frequency & phase, Protection overcurrent/overvoltage/islanding — POWER ELECTRONICS + CONTROL + PROTECTION.

**Storage:** kW Power — how fast? kWh Energy — how much? Example 2-kW load 4h needs 8 kWh. SoC state of charge, DoD depth of discharge, BMS battery management system, Efficiency charge/discharge losses. STORAGE TURNS SUNSHINE INTO DISPATCHABLE ENERGY. Three components students identify immediately: Inverter DC→AC, MPPT controller regulates PV/battery charging, LiFePO₄ battery stores electrical energy.

**Digital Solar:** Solar plant is also data system: Irradiance W/m², PV voltage V, PV current A, Temperature °C, Energy yield kWh, Battery SoC % — MEASURE → TRANSMIT → VISUALISE. Once you can measure performance, you can start predicting. IoT • EMBEDDED • CLOUD • AI.

**Diagnostics:** Dust/soiling → power loss, Partial shade → mismatch, Hot spot → thermal risk, Loose connector → arcing/outage, Inverter trip → No AC output. Flow SENSOR DATA → ANOMALY → DIAGNOSIS → ACTION → VERIFY — predictive maintenance thinking.

**Next Frontier — Solar meets AI:** Forecast predict PV output from weather + history, Anomaly detection spot unusual behaviour early, Fault diagnosis map signatures to likely faults, Degradation/RUL estimate performance decline, Optimisation schedule storage and loads. ENGINEER OF FUTURE MAY BE BOTH POWER ENGINEER AND DATA SCIENTIST.

**Local Impact:** Homes reliable household electricity, Universities labs/ICT/campus loads, Clinics critical lighting + refrigeration, Agriculture water pumping + processing, Telecoms remote site power, Small business shops/offices/workshops. Engineering question not "Can solar work?" — "How make it reliable, affordable and intelligent?" Build Something: PROBLEM what fails? Who needs help? MEASURE collect trustworthy data, DESIGN model/size/protect, VALIDATE test against reality, SCALE document/improve/deploy. ENGINEERING VALUE = WORKING SOLUTION + EVIDENCE THAT IT WORKS.

**Mini Design Challenge:** Design introductory solar-battery system for small rural clinic. Daily energy = 8 kWh/day, Peak load = 2 kW, Autonomy = 1 day, Illustrative assumptions — choose PV capacity, battery capacity, inverter rating and basic protection. PV sizing, Battery sizing, Inverter sizing, Protection & safety, DISCUSS FOR 3 MINUTES.

**Real-world installation:** Look for PV array, DC protection, isolator, inverter, AC distribution and battery bank. Safety: PV safety non-negotiable.

### Workshop Practice
**Definition:** Hands-on training and skills required in engineering workshops. Hand tools (hammers, saws, pliers, marking tools), Machine tools (lathe, milling machine, drilling machine, power hack saw), Manufacturing methods (machining, casting, powder metallurgy, welding, recently additive manufacturing) — accomplished by human efforts or machinery. Many manufacturing processes automated and some hand-crafted. Note: manufacturing processes are various sub-divisions.

**Starts from:** 1 Identification of materials and properties — where can each material be used? common engineering materials used at shop floor? 2. Measurements: measuring instruments e.g., meter rule, vernier caliper, micrometer, etc.

**Safety measures:** Housekeeping clean organized reduces slips/trips/falls and fire risk, Emergency Procedures machine safety proper guarding moving parts regular maintenance ensuring operators adequately trained, Training and Communication proper training fostering open communication vital, Hazard Identification and Control continuous process, Proper Tool Use ensuring tools good condition appropriate for task used correctly, Ventilation adequate to remove fumes/dust/airborne hazards, Working Alone advisable avoid working alone ensure someone available assist accident, Fire Safety having extinguishers blankets knowing how to use vital, Ergonomics designing workstations/tasks minimize musculoskeletal injuries important, Electrical Safety precautions working with electricity insulated tools avoiding overloaded circuits critical, Waste Disposal proper disposal flammable/hazardous materials essential preventing accidents/environmental contamination, Signage and Warning.

**Control measures example:** machine guarding (engineering control) prevents accidental contact moving parts, training safe operation (administrative) and safety glasses (PPE) enhances protection — comprehensive approach.

### Traps to watch
- Sub-Saharan Africa **1 billion+** = current population, **1.2 billion** = free-trade market — do not swap.
- **100 Mbps** = guaranteed whenever needed, **>10 Gbps** = peak — do not swap.
- **MPP** = Maximum Power Point — where converter should operate.
- Good design ≠ buy more panels — understand chain of causes/effects.
- Architecture chosen from load/reliability need, not panel count.
- **kW** = power (how fast), **kWh** = energy (how much) — 2kW × 4h = 8kWh.
- Workshop starts from identification + measurements.
- Control example = guarding + training + glasses.
""",
    },
    {
        "id": "swep-day-4",
        "name": "Day 4 — Thursday, 17th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 4 covered
| # | Lecture | Speaker |
|---|---|---|
| 1 | Food Science & Engineering, Value-Addition & National Development | **Dr. W. A. Adebayo** |
| 2 | Demystifying Artificial Intelligence | **Dr. Aderonke Lawal** |
| 3 | Fire Awareness & Prevention | **Mr. M. A. Ibrahim** |

### Food Science & Engineering — Key Words
**Food Science:** study of physical, microbiological, and chemical makeup of food.
**Food Technology:** application of food science to selection, preservation, processing, packaging, distribution, and use of safe food.
**Food Engineering:** multidisciplinary field applying engineering principles (chemical, mechanical, process) to production, processing, preservation, distribution.

Branches of Food Science: Food Chemistry, Processing, Food Nutrition, Food Microbiology, Food Sensory, New Product Development.
Branches of Food Engineering: Food Safety Engineering, Sustainability and waste management, Process Engineering, Packaging Engineering, Equipment Design, Refrigeration and Cold Chain.

**Value-Addition:** transformation of raw agricultural produce into more desirable, convenient, nutritious products to increase market value, shelf life, acceptability.
Impact: economic growth, FOOD SECURITY and waste management, rural development, health and nutrition, industrial and technological advancement.

**Food Security:** exists when all people, at all times, have physical and economic access to sufficient, safe and nutritious food that meets dietary needs and preferences for active healthy life. Dimensions:
- Availability: sufficient quantities appropriate quality, domestic production or imports including food aids
- Access: adequate resources (entitlements) for nutritious diet
- Utilization: adequate diet, clean water, sanitation, health care to reach nutritional well-being — non-food inputs importance
- Stability: must have access at all times, not risk losing due to sudden shocks (economic/climatic crisis) or cyclical events (seasonal food insecurity)

Speaker contact: Dr. W. A. Adebayo (Food Process Engineering) adebayow@oauife.edu.ng; +234808060410278, Dept of Food Science and Technology, OAU.

### Food Science & 4IR — mind/heart/soul/body
**4IR** = blurring of physical, digital, biological. **Food Science & 4IR:** Mind (knowledge), Heart (emotional), Soul (inspired), Body (physical).

### AI — models and learning
**Model** = mathematical representation of patterns learned from data; digital brain.
**Process:** Data → Training → Model → Prediction → Feedback → Improved Model.
**Accuracy** = % correct predictions (95/100 = 95%). Caution: High accuracy good, but what kinds of errors? Example Western vs African names bias.
**Limitations:** biased data (Western vs African names), overfitting (crammer — student crams past questions but can't answer new ones), lack of context (sarcasm).
| Type | Learns from |
| **Supervised** | **Labelled** data — spam detection, face unlock |
| **Unsupervised** | **Unlabelled** data — Spotify clustering, Google News |
| **Reinforcement** | **Rewards/penalties** — self-driving cars, AlphaGo |

**LLM = Large Language Model.** Teachable Machine: **20–30 samples per class**, no coding, webcam, at teachablemachine.withgoogle.com, model learns by generalising not memorising.
**ChatGPT:** doesn't think, predicts next word via probability not understanding.
**Challenges:** data privacy, bias and fairness, job displacement, lack of regulation.
**Ways forward:** ethical AI, inclusive data, policies, human-AI collaboration.

### Fire Awareness
**Fire triangle: Heat + Fuel + Oxygen.**
**Control:** Cooling (heat), Smothering (oxygen), Starvation (fuel).
**Spread:** conduction, convection, radiation, spontaneous combustion.
**Basic necessities:** food, shelter, clothing. Natural detectors: brain and sensory organs olfactory lobes for smell.
**Causes:** Negligence & Human Error carelessness poor safety attitudes "I don't care", improper handling combustible materials. Statistical Insight OAU hostels: Moremi (most) → Akintola → Alumni → Mozambique → PG (least). Natural igniter: lightning and thunder. Biological/Animal: house pests/rodents gnawing electrical wires. Common Sources: Flammable Gases acetylene butane methane, Volatile Solvents perfumes alcohol illicit substances Colorado (Indian hemp/synthetic cannabis).

| Class | Fuel | Examples |
| **A** | Solids | Paper, wood, textiles |
| **B** | Flammable liquids | Kerosene, petrol, perfumes, alcohol |
| **C** | Flammable gases | Methane, acetylene, butane |
| **D** | Combustible metals | Potassium, sodium, calcium |
| **E** | Energized electrical | **Least frequent origin** |

**Colour bands:** RED water, BLUE dry powder, CREAM foam, BLACK CO₂. CO₂ multipurpose (electrical + liquids) and leaves no residue. Water extinguishers: stored pressure vs gas cartridge.
**OAU hostel fire ranking:** Moremi (most) → Akintola → Alumni → Mozambique → PG (least).
**Comparative safety** = manage it inside; **Absolute safety** = evacuate.
**In smoke: toxic smoke rises — lie flat and crawl.**

### Traps to watch
- Food **Science** studies, **Technology** applies, **Engineering** builds.
- 1IR **1760–1840**; 2IR **1860–1930** — do not swap.
- Graphene: **200× stronger** than steel but **one million times thinner** than hair.
- **Overfitting** = memorising; the crammer analogy.
- Class **D** is metals, **E** is electrical.
- Day 2 used extinguisher **shapes**; Day 4 uses **colour bands**. Answer per the named lecture.
- Food Security four dimensions: availability, access, utilization, stability.
- Value-addition transformation not just price increase.
- Basic necessities food shelter clothing; detector olfactory lobes.
- Natural igniter lightning/thunder; biological rodents gnawing wires.
- Volatile solvents perfumes alcohol Colorado.
- Comparative safety manage inside, absolute evacuate, smoke lie flat crawl.
- BLACK CO₂ multipurpose no residue.
""",
    },
    {
        "id": "swep-day-5",
        "name": "Day 5 — Friday, 18th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 5 covered
A single session: **Employers’ Expectations from Fresh Graduates in the
21st-Century Job Market**, delivered by a Representative of the **Nigeria
Employers’ Consultative Association (NECA)**.

### Core concepts
- SIWES is **not** an escape from academics — it is a period to convert experience
  into **verifiable skills** that guarantee **employability**
- It is for **building human networks** — *network brings good net worth*
- **Mindset shift:** see yourself as a **professional in training**, not a mere
  student — *you are being equipped to **create value and build evidence***

### The three numbers
| Number | What it counts |
|---|---|
| **3 to 5** | Learning **goals** |
| **4 to 5** | **Days** in the critical first period |
| **12** | **Weeks** in the action plan |

### Before SIWES
Research the **assigned organisation** · update **CV and LinkedIn** (**professional
email**) · define **3–5 learning goals** · prepare a **professional wardrobe** · daily
routine, notebooks, documents · know your **reporting line** · get a **Role Title** ·
meet all **ITF requirements**.

### First 4 to 5 days
From day one **observe, listen, introduce yourself properly**. **Ask questions** —
*career development is a **strategic effort***: *Who is my supervisor? What is my
responsibility? **What does success look like?*** Keep a **daily learning record**,
**dress appropriately**, **protect confidential information**.

### What employers notice (6)
**Punctuality · Communication** (listening and asking questions) **· Initiative ·
Team work** (supporting colleagues) **· Professionalism · Integrity**
> **Beware of office politics! Nobody is your best friend at work.**

### SIWES Learning Loop
**Observe → Ask questions / Practice → Document experiences → Reflect**
*Don’t just collect tasks, but **collate evidence** (How, when & what). Have a
**digital portfolio**. Do not have a **career mismatch**.*

### Skills to develop (7)
Technical skills acquisition · communication · **digital literacy** · team work ·
**speaking/presentation** · **work ethics** · **networking**.
Only **one** is technical — the rest are soft/transferable.

### Twelve Weeks Action Plan
Set **3–5 goals** · **CV and LinkedIn tailored to your goals** · build a **job
portfolio — document evidence** · build **technical skills** · **document evidence
of skills** · **close your skill gap**, develop and improve consistently.

### Traps to watch
- **Prepare notebooks** is *before*; **keep a daily learning record** is *during*.
- **Communication** and **team work** appear on **both** the employers’ list and the
  skills list — they cannot distinguish the two.
- **Punctuality, integrity, professionalism** are **observed traits**, not listed skills.
- **12 weeks** is the plan; **8 weeks** is the SWEP minimum; **24 weeks** is SIWES II.
- The note names the speaker only as a **NECA representative** — no personal name is given.
- Network brings net worth — building human networks.
- Professional in training mindset — create value and build evidence.
- Beware office politics — nobody is best friend at work.
- Don’t just collect tasks but collate evidence How/when/what — digital portfolio — avoid career mismatch.
- Close skill gap consistently part of 12-week plan.
""",
    },
]

QUESTION_SETS = [DAY1, DAY1_EXTRA, DAY2, DAY2_EXTRA, DAY3, DAY3_EXTRA, DAY4, DAY4_EXTRA, DAY5, DAY5_EXTRA]

BEGIN = '// ==== SWEP 200 BEGIN (generated by scripts/splice_swep200.py) ===='
END = '// ==== SWEP 200 END ===='


def js(obj, indent):
    raw = json.dumps(obj, indent=2, ensure_ascii=True)
    pad = ' ' * indent
    return '\n'.join(pad + line if i else line for i, line in enumerate(raw.split('\n')))


def strip_previous(src):
    src = re.sub(r'export const lectureMeta = \{[\s\S]*?\n\}\n\n', '', src, count=1)
    src = re.sub(r'\n\s*\{\s*\"id\":\s*\"swep200\".*?\n\s*\},(?=\n\])', '', src, flags=re.S)
    for key in ('categoryMeta', 'topicMeta', 'questionBank'):
        src = re.sub(r'\n  \"swep200\": \[.*?\n  \],(?=\n)', '', src, count=1, flags=re.S)
    return src


def main():
    src = DATA.read_text()
    if 'swep200' in src:
        print('! existing SWEP 200 block found — replacing it')
        src = strip_previous(src)

    questions = [q for group in QUESTION_SETS for q in group]

    lmap = question_lecture_map()
    for q in questions:
        lid = lmap.get(q['id'])
        if lid is None:
            raise SystemExit(f"{q['id']}: no lecture mapped")
        q['lectureId'] = lid

    topic_ids = {t['id'] for t in TOPICS}
    for q in questions:
        if q['topicId'] not in topic_ids:
            raise SystemExit(f"{q['id']}: unknown topicId {q['topicId']!r}")
    used_cats = {t['categoryId'] for t in TOPICS}
    cats = [c for c in CATEGORIES
            if c['id'] in used_cats or c.get('spansAll')]
    dropped = [c['id'] for c in CATEGORIES
               if c['id'] not in used_cats and not c.get('spansAll')]
    if dropped:
        print(f'  (categories with no topics yet, omitted: {", ".join(dropped)})')

    src = src.replace('  "available": true\n},\n]',
                      '  "available": true\n},\n' + js(COURSE, 0) + ',\n]', 1)

    cat_payload = f'  "swep200": {js(cats, 2)},\n'
    if 'export const categoryMeta = {}' in src:
        src = src.replace('export const categoryMeta = {}',
                          'export const categoryMeta = {\n' + cat_payload + '}', 1)
    else:
        src = src.replace('export const categoryMeta = {\n',
                          'export const categoryMeta = {\n' + cat_payload, 1)

    src = src.replace('export const topicMeta = {\n',
                      'export const topicMeta = {\n  "swep200": ' + js(TOPICS, 2) + ',\n', 1)

    src = src.replace('export const questionBank = {\n',
                      'export const lectureMeta = {\n  "swep200": ' + js(LECTURES, 2) + ',\n}\n\nexport const questionBank = {\n', 1)

    src = src.replace('export const questionBank = {\n',
                      'export const questionBank = {\n  "swep200": ' + js(questions, 2) + ',\n', 1)

    DATA.write_text(src)
    print(f'✅ SWEP 200 spliced: {len(questions)} questions across {len(LECTURES)} lectures, '
          f'{len(TOPICS)} topic(s), {len(cats)} categor(ies)')


if __name__ == '__main__':
    main()
