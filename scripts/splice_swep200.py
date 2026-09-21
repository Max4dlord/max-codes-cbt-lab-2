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
        "course, one orientation day, or a single lecture \u2014 every question carries "
        "a full explanation traced back to the slide it came from."
    ),
    "accent": "#0F7B3F",
    "available": True,
}

CATEGORIES = [
    {
        # VIRTUAL category: owns no topics. `spansAll` makes the app shuffle
        # across every question in the course, so "General" = test everything
        # from all SWEP Days and all lectures at once.
        "id": "general",
        "name": "General",
        "spansAll": True,
        "blurb": "Shuffled across every SWEP Day and lecture \u2014 the full-course mix.",
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
        "name": "Day 1 \u2014 Monday, 14th September",
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
| **1971** | ITF established under **Act No. 47**; take-off grant **\u20a61,000,000 (\u00a3500,000)** |
| **1973** | SIWES established by ITF; **OAU (then University of Ife) among the first participants** |
| 1974 | SIWES actually started |
| to 1978 | ITF **fully funded** SIWES |
| **1979** | FME makes a **one-year IT programme compulsory** for Polytechnics/Colleges of Technology |
| **Jan 1980** | ITF **withdraws** from financing SIWES |
| 1980\u20131984 | **NUC & NBTE** fund the scheme; NBTE renames SIWES **COSITA** |
| **1984** | Scheme **expanded** to sciences, environmental sciences, agriculture; ITF resumes management **Nov 1984** (**IAGR** Dept.) |
| **1985** | **Decree No. 16 of August 1985** gives SIWES legal backing |
| 1987 | Austerity measures + **SAP** \u2014 firms stop providing accommodation |
| 1994 | **30% of firms** reject institutional requests; individual-merit applications |
| **1995** | ITF/NUC allocate **3\u201315 credit units** |
| 2011 | **ITF Amendment Act** \u2014 NISDP, WOSEP, STEPP-C, CONSEP, **SUPA** |

### Durations and credit units
- **SWEP 200** \u2014 ideally **12 weeks**, strict minimum **8 weeks** (after 200-Level Rain Semester)
- **SIWES I** \u2014 12 weeks, after the **300**-Level Rain Semester
- **SIWES II** \u2014 **24 weeks (6 months)**, 400-Level Rain Semester + vacation. **Only SIWES II receives ITF stipends.**
- Polytechnics/Colleges of Education **4 months**; Universities **6 months**
- Credit units: **Year II: 3 \u00b7 Year III: 3 \u00b7 Year IV: 9** (Technology & EDM)
- Exempt 4-year programmes: **Architecture, Fine and Applied Arts, Industrial Chemistry**
- **Faculty of Agriculture** \u2014 consolidated **1-year 'Farm Year'**

### The daily schedule
| Time | Activity |
|---|---|
| 08:00 \u2013 08:30 | Arrival + **first** attendance check |
| 08:30 \u2013 09:00 | Recap of previous day |
| 09:00 \u2013 10:30 | Lecture 1 |
| 10:30 \u2013 12:00 | Lecture 2 |
| 12:00 \u2013 12:30 | Break \u2014 **second check strictly 12:25\u201312:30** |
| 12:30 \u2013 14:00 | Lecture 3 |

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
- **Act 47 \u2192 1971 \u2192 created the ITF.** **Decree 16 \u2192 1985 \u2192 backed SIWES.**
- \u20a690 is the **1976** allowance, not 1981 (**\u20a6250**).
- Supervisory allowance is **10%** of the student allowance.
- **42** = Area Offices, not HQ units.
- E-SIWES portal is **www.siwesdata.org**; e-payment came from **Yar'Adua's 2009 budget**.
""",
    },
    {
        "id": "swep-day-2",
        "name": "Day 2 \u2014 Tuesday, 15th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 2 covered
| # | Lecture | Speaker |
|---|---|---|
| 1 | Substance Abuse Awareness | **Dr. A. Olatunji** |
| 2 | Workshop & Industrial Safety | **Prof. A. A. Adeleke** |
| 3 | 21st-Century Employability Skills | **Prof. A. B. Ekanola** |

### Substance abuse \u2014 the numbers
| Measure | Figure |
|---|---|
| Global average use | **5.3%** |
| Nigeria, aged 15\u201364 | **14.3%** (\u2248 14.4 million people) |
| Lifetime prevalence, SW Nigerian universities | **45% \u2013 84.5%** |

Most abused: **alcohol, tobacco, codeine cough syrups, tramadol, cannabis**.

**Five categories of warning sign** \u2014 know which is which:
- **Physical** \u2014 bloodshot/glassy eyes, weight change, odours, tremors, poor hygiene
- **Behavioural** \u2014 new friend groups, secrecy, stealing, **impulsivity/risk-taking**
- **Academic** \u2014 absenteeism, falling grades, discipline, **unsubmitted assignments**
- **Psychological/Emotional** \u2014 mood swings, anxiety, depression, **hallucinations**
- **Social/Lifestyle** \u2014 money trouble, fights/cultism, sleep changes, drug joints

**Prevention** (before) vs **Intervention** (after):
- Prevention: campus drug education, life skills, peer support, restricting access, parents/community
- Intervention: early screening, counselling, medical treatment/rehab, policy & discipline, media campaigns
- **Multi-sectoral collaboration**: **NDLEA**, Federal Ministry of Health, NGOs, campus health services

### Safety \u2014 the numbers
- **5,486** US fatal occupational injuries in 2022 (**+5.7%** on 2021)
- **WHO**: **20\u201350%** of workers face workplace hazards
- **ILO**: economic cost **1.8%\u20136% of GDP**

**High-risk industries**: construction, healthcare, manufacturing, transportation,
agriculture, iron & steel, chemical/petrochemical, heavy equipment operation.

**PPE standards**
| Standard | Covers | Region |
|---|---|---|
| **ANSI Z87.1** | Safety glasses | **US** |
| EN 166 | Safety glasses | Europe |
| EN ISO 20471 | High-visibility clothing | Europe |
| EN ISO 11611 | Welding protection | Europe |

**Hierarchy of control** (most \u2192 least effective):
**Elimination** \u2192 Substitution \u2192 Engineering \u2192 Administrative \u2192 **PPE (last line)**

**Safety signs \u2014 shape + colour**
| Type | Shape | Colour |
|---|---|---|
| Prohibition | Circular | Red border + diagonal |
| Warning | **Triangular** | Yellow/amber |
| Mandatory | Circular | **Blue** |
| Emergency/First-aid | Rectangular | **Green** |

**Fire extinguishers** \u2014 all red bodies, coded markings:
Water **green triangle** (A) \u00b7 CO2 **black square** (B, C) \u00b7
Foam **cream label** (A, B) \u00b7 Dry powder **blue circle** (A, B, C).
Never use water on an electrical fire.

**Bodies**: US \u2014 **OSHA** (enforces), **NIOSH** (research).
Nigeria \u2014 **NISCN**, **ISPON**, OSHAssociation, MAN, NACCIMA.

### Employability
**Definition**: the capabilities to **obtain, retain, perform and progress** in
employment. You can be employed yet barely employable if your skills are going obsolete.

**Agents of transformation**: AI, automation, digital platforms, globalisation, remote work.

**8 clusters**: communication \u00b7 critical thinking & problem-solving \u00b7 digital &
technological \u00b7 creativity & innovation \u00b7 collaboration & teamwork \u00b7 personal
effectiveness & emotional intelligence \u00b7 career management, entrepreneurship &
leadership \u00b7 adaptability, lifelong learning & professional development.

**Critical thinking order**: identify the problem \u2192 research \u2192 determine data
relevance \u2192 ask questions \u2192 identify best solution \u2192 present \u2192 analyse the decision.

**Key distinctions**
- **Creativity** sees possibilities; **innovation** converts them into useful outcomes.
- **Adaptability** = functioning through change; **resilience** = recovering from setbacks.
- A **skill** performs a task; a **capability** applies knowledge in *changing* circumstances.
- A **CV claims**; a **portfolio demonstrates**.
- Goal with AI: an **AI-enabled professional**, not competing with AI, not blind delegation.

**Career model**: Degree \u2192 work \u2192 reskill \u2192 work \u2192 upskill \u2192 transition \u2192
lifelong learning (via micro-credentials and short courses).

**Five things to build alongside the degree**: communication ability \u00b7 digital
capability \u00b7 evidence of practical experience \u00b7 a professional network \u00b7 a learning habit.

### Traps to watch
- **5.3%** global vs **14.3%** Nigeria vs **45\u201384.5%** university lifetime prevalence.
- Every warning-sign distractor is a **real** sign under a **different** category.
- **Prevention** precedes the problem; **intervention** follows it.
- **EN** = European, so **ANSI Z87.1** is the US one.
- **PPE is the weakest** control, not the strongest.
- Prohibition and mandatory signs are **both circular** \u2014 red vs blue decides.
- **8** skill clusters, but **5** things to build. Different lists.
""",
    },
    {
        "id": "swep-day-3",
        "name": "Day 3 \u2014 Wednesday, 16th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 3 covered
| # | Lecture | Speaker |
|---|---|---|
| 1 | Entrepreneurship in the 5G Era | **Prof. A. B. Ayanwale** (Agricultural Economics) |
| 2 | Renewable Energy & PV Technology | **Dr. F. K. Ariyo** (Electronic & Electrical Engineering) |
| 3 | Workshop Practice, Workforce & National Growth | **Prof. V. Omidiji** (PhD, REng (Mech), MNIMechE, MNIEM, MNSE) |

### 5G \u2014 the three superpowers
| Superpower | What it is | Its label |
|---|---|---|
| **eMBB** | Insanely high speed, massive bandwidth | \u201ccontent and data delivery\u201d |
| **URLLC** | **~1 ms** latency, extreme reliability | \u201creal-time control and safety\u201d |
| **mMTC** | Huge numbers of low-power devices | \u201cmassive data collection\u201d |

**Enablers:** **Network slicing** (rent a virtual network \u2014 lowers barrier to entry)
and **Edge computing** (process locally \u2014 privacy-first, real-time AI).

**Generations:** 1G AMPS/TACS/NMT (1980s) \u00b7 2G GSM (1990s) \u00b7 3G WCDMA/HSPA (2000s) \u00b7
**4G LTE (2010s)** \u00b7 **5G NR (2020s)**.

**5G targets:** **>10 Gbps** peak \u00b7 **<1 ms** radio latency \u00b7 100 Mbps whenever needed \u00b7
10 000\u00d7 traffic \u00b7 10\u2013100\u00d7 devices \u00b7 10 years on battery.

**Capabilities vs LTE:** 10\u00d7 data rates \u2192 10 Gbps \u00b7 10\u00d7 lower cost \u2192 <2 cent/GB \u00b7
10\u00d7 lower latency \u2192 **<1 ms** \u00b7 10\u00d7 lower IoT power \u2192 <10 \u03bcWh/tx \u00b7
5\u00d7 energy efficiency \u2192 <2 kWh/TB \u00b7 5\u00d7 spectral efficiency \u2192 >10 bps/cell/Hz.

**Spectrum:** 20\u201390 GHz \u2192 1 GHz/operator \u2192 5\u201320 Gbps \u00b7 Below 6 GHz \u2192 100 MHz \u2192 2 Gbps \u00b7
Below 1 GHz \u2192 10 MHz \u2192 0.2 Gbps. NR spans **400 MHz \u2013 90 GHz**.

**5 technology components:** new spectrum \u00b7 beamforming \u00b7 network slicing \u00b7
LTE dual connectivity/coexistence \u00b7 cloud-optimised architecture.

**Journey:** start with a **pain point**, then apply the **5G lens**. Team =
domain + technical + business. Monetise **as-a-service**. **6G** converges with
**AI, quantum computing and advanced sensing**.

### PV \u2014 solar as a multidisciplinary system
**Energy flow:** Sunlight \u2192 **PV cell** \u2192 **MPPT** \u2192 **inverter** \u2192 load/grid.
**Scaling:** CELL \u2192 MODULE \u2192 STRING \u2192 ARRAY.
**I\u2013V curve:** **Isc**, **MPP**, **Voc** \u2014 MPP is the *point*, MPPT the *technology*.
**Why MPPT:** irradiance and temperature change, so the MPP **moves**
(less sun \u2192 less current; hotter cell \u2192 lower voltage).

**Six performance factors:** irradiance \u00b7 temperature \u00b7 shading \u00b7 soiling \u00b7
mismatch \u00b7 degradation.

| Architecture | Flow | Use |
|---|---|---|
| Grid-tied | PV \u2192 inverter \u2192 grid/load | Homes, offices, campuses |
| **Off-grid** | PV \u2192 controller \u2192 battery \u2192 loads | Remote sites, PHCs |
| Hybrid | PV + grid/generator + battery | Critical loads, resilience |

**Storage:** **kW = how fast** (power), **kWh = how much** (energy).
A 2-kW load for 4 h needs **8 kWh**. Terms: SoC, DoD, BMS, efficiency.
**Three components to recognise:** inverter (DC\u2192AC) \u00b7 MPPT controller \u00b7 LiFePO\u2084 battery.
**Diagnostics:** soiling\u2192power loss \u00b7 partial shade\u2192mismatch \u00b7 hot spot\u2192thermal risk \u00b7
loose connector\u2192arcing/outage \u00b7 inverter trip\u2192no AC output.
**Clinic challenge:** 8 kWh/day, 2 kW peak, 1 day autonomy.
**Safety:** **PV DC stays energised in sunlight** \u2014 isolation must be planned.

### Workshop practice, workforce & national growth
**Resources:** hand tools (hammers, saws, pliers, marking tools) \u00b7 machine tools
(lathe, milling, drilling, **power hack saw**) \u00b7 manufacturing methods (machining,
casting, powder metallurgy, welding, additive).

**Sequence:** identify materials \u2192 measurements \u2192 marking out (**on the
marking-out table**) \u2192 cutting to size \u2192 joining or machining.

**Activity focuses:** skill development \u00b7 team building \u00b7 problem-solving.
**Five outcomes:** hands-on experience \u00b7 skill development \u00b7 safety awareness \u00b7
understanding manufacturing processes \u00b7 application in industrial production.

**Workforce** = all physically able and available people, **employed and
unemployed**. The question: *how many of the employable are employed?*

**Eq. 1:** Workshop Practice + Workforce = **\u00bd(National Growth)**
**Eq. 2:** Workshop Practice + Workforce + **Development Plan** = National Growth
Engineering **drives**; the development plan **catalyses**.

**GDP:** Nigeria Q1 2025 **3.13%** (up from **2.27%** in Q1 2024); Ghana **5.4%**.
Driver: reduced petrol imports via the **Dangote Refinery**.
**Growth factors:** government policies \u00b7 global economy \u00b7 **human capital**.
**NDP 2021\u20132025**, aligned with **Nigeria Agenda 2050**, four strategic objectives.
**Outcomes:** **TVET** in all Technical Colleges \u00b7 **COREN** to regulate engineering admissions.

### Traps to watch
- **100 Mbps** is the \u201cwhenever needed\u201d rate; **>10 Gbps** is the peak.
- **Quantum computing** belongs to the **6G** slide, not the 5 technology components.
- **MPP** is a point on the curve; **MPPT** is the tracking technology.
- **kW vs kWh** \u2014 inverter rated in kW, battery sized in kWh.
- **2.27%** is Nigeria\u2019s **Q1 2024** figure, not 2025.
- Eq. 1 gives only **half** of national growth \u2014 the plan supplies the rest.
- Ayanwale teaches 5G but is from **Agricultural Economics**; Adeleke (Materials
  Science) belongs to **Day 2**.
""",
    },
    {
        "id": "swep-day-4",
        "name": "Day 4 \u2014 Thursday, 17th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 4 covered
| # | Lecture | Speaker |
|---|---|---|
| 1 | Food Science & Engineering, Value-Addition and National Development (4IR) | **Dr. W. A. Adebayo** (Food Science and Technology) |
| 2 | Demystifying Artificial Intelligence | **Dr. Aderonke Lawal** (Computer Engineering) |
| 3 | Fire Awareness and Prevention | **Mr. M. A. Ibrahim** |

### Food Science \u2014 definitions and food security
- **Food Science** \u2014 the **study** of the physical, microbiological and chemical makeup of food
- **Food Technology** \u2014 the **application** of food science to selection, preservation, processing, packaging, distribution of **safe** food
- **Food Engineering** \u2014 the **multidisciplinary field** applying **engineering principles** to production, processing, preservation and distribution
- **Value-Addition** \u2014 transforming raw produce into **desirable, convenient, nutritious** products, raising **market value, shelf life, acceptability**

**Four dimensions of food security:** **Availability** (sufficient quantity/quality,
incl. imports) \u00b7 **Access** (entitlements) \u00b7 **Utilization** (diet, clean water,
sanitation, health care) \u00b7 **Stability** (at all times; no shocks/cyclical loss).

**Autarky** = deliberate isolation, **eliminating** international trade (China under
**Mao Tse Tung**, Japan, North Korea). **Food self-reliance** = integrated management
of production, export, import, storage, distribution + **strategic reserves**.

### Industrial Revolutions \u2014 exact dates
| IR | Dates | Defining change |
|---|---|---|
| Agrarian | before 1IR | Foraging \u2192 farming + domestication |
| **1IR** | **1760\u20131840, Britain** | Muscle/animal \u2192 **mechanical power**; birth of factories |
| **2IR** | **1860\u20131930** | **Electricity**, assembly lines \u2192 **mass production** |
| **3IR** | Began **1960s** | **Computer and information age** |
| **4IR** | About **2000** | Fusion across **physical, digital, biological** |

**IR definition:** *abrupt and radical change*. **Causative agents: energy,
communication, transportation.**
**3IR catalysts:** semiconductors \u00b7 mainframes (1960s) \u00b7 PCs (1970s\u201380s) \u00b7 internet (1990s).
**3IR drivers:** renewable energy \u00b7 ICT \u00b7 **3D printing**.
**4IR characteristics:** ubiquitous mobile internet \u00b7 cheaper, smaller sensors \u00b7 **AI and ML**;
enables **SMART FACTORIES**. Impacts are **HISTORIC, PROFOUND, DISRUPTIVE, MULTIFACETED**.
**4IR clusters:** Physical \u00b7 Digital \u00b7 Biological.
**Graphene: 200\u00d7 stronger than steel, one million times thinner than human hair**, good conductor.
**Four intelligences:** Contextual (**mind**) \u00b7 Emotional (**heart**) \u00b7 Inspired (**soul**) \u00b7 Physical (**body**).

### AI \u2014 models and learning
**Model** = a **mathematical representation of patterns learned from data**; a *digital brain*.
**Process:** **Data \u2192 Training \u2192 Model \u2192 Prediction \u2192 Feedback \u2192 Improved Model**.
**Accuracy** = % of correct predictions (95/100 = **95%**).
**Limitations:** **biased data** (Western vs African names) \u00b7 **overfitting** (the crammer) \u00b7 **lack of context** (sarcasm).
| Type | Learns from |
|---|---|
| **Supervised** | **Labelled** data \u2014 spam detection, face unlock |
| **Unsupervised** | **Unlabelled** data \u2014 Spotify clustering, Google News |
| **Reinforcement** | **Rewards/penalties** \u2014 self-driving cars, AlphaGo |

**LLM = Large Language Model.** Teachable Machine: **20\u201330 samples per class**.
**Challenges:** data privacy \u00b7 bias and fairness \u00b7 job displacement \u00b7 **lack of regulation**.
**Ways forward:** ethical AI \u00b7 inclusive data \u00b7 policies \u00b7 **human-AI collaboration**.

### Fire Awareness
**Fire triangle: Heat + Fuel + Oxygen.**
**Control:** **Cooling** (heat) \u00b7 **Smothering** (oxygen) \u00b7 **Starvation** (fuel).
**Spread:** conduction, convection, radiation, spontaneous combustion.

| Class | Fuel | Examples |
|---|---|---|
| **A** | Solids | Paper, wood, textiles |
| **B** | Flammable liquids | Kerosene, petrol, perfumes, alcohol |
| **C** | Flammable gases | Methane, acetylene, butane |
| **D** | Combustible metals | Potassium, sodium, calcium |
| **E** | Energized electrical | **Least frequent origin** |

**Colour bands:** **RED** water \u00b7 **BLUE** dry powder \u00b7 **CREAM** foam \u00b7 **BLACK** CO\u2082.
**CO\u2082** is multipurpose (electrical + liquids) and **leaves no residue**.
**OAU hostel fire ranking:** **Moremi (most)** \u2192 Akintola \u2192 Alumni \u2192 Mozambique \u2192 **PG (least)**.
**Comparative safety** = manage it **inside**; **Absolute safety** = **evacuate**.
**In smoke: toxic smoke rises \u2014 lie flat and crawl.**

### Traps to watch
- Food **Science** studies, **Technology** applies, **Engineering** builds.
- 1IR **1760\u20131840**; 2IR **1860\u20131930** \u2014 do not swap.
- Graphene: **200\u00d7 stronger** than steel but **one million times thinner** than hair.
- **Overfitting** = memorising; the crammer analogy.
- Class **D** is metals, **E** is electrical.
- Day 2 used extinguisher **shapes**; Day 4 uses **colour bands**. Answer per the named lecture.
""",
    },
    {
        "id": "swep-day-5",
        "name": "Day 5 \u2014 Friday, 18th September",
        "categoryId": "swep-days",
        "summaryNotes": """### What Day 5 covered
A single session: **Employers\u2019 Expectations from Fresh Graduates in the
21st-Century Job Market**, delivered by a Representative of the **Nigeria
Employers\u2019 Consultative Association (NECA)**.

### Core concepts
- SIWES is **not** an escape from academics \u2014 it is a period to convert experience
  into **verifiable skills** that guarantee **employability**
- It is for **building human networks** \u2014 *network brings good net worth*
- **Mindset shift:** see yourself as a **professional in training**, not a mere
  student \u2014 *you are being equipped to **create value and build evidence***

### The three numbers
| Number | What it counts |
|---|---|
| **3 to 5** | Learning **goals** |
| **4 to 5** | **Days** in the critical first period |
| **12** | **Weeks** in the action plan |

### Before SIWES
Research the **assigned organisation** \u00b7 update **CV and LinkedIn** (**professional
email**) \u00b7 define **3\u20135 learning goals** \u00b7 prepare a **professional wardrobe** \u00b7 daily
routine, notebooks, documents \u00b7 know your **reporting line** \u00b7 get a **Role Title** \u00b7
meet all **ITF requirements**.

### First 4 to 5 days
From day one **observe, listen, introduce yourself properly**. **Ask questions** \u2014
*career development is a **strategic effort***: *Who is my supervisor? What is my
responsibility? **What does success look like?*** Keep a **daily learning record**,
**dress appropriately**, **protect confidential information**.

### What employers notice (6)
**Punctuality \u00b7 Communication** (listening and asking questions) **\u00b7 Initiative \u00b7
Team work** (supporting colleagues) **\u00b7 Professionalism \u00b7 Integrity**
> **Beware of office politics! Nobody is your best friend at work.**

### SIWES Learning Loop
**Observe \u2192 Ask questions / Practice \u2192 Document experiences \u2192 Reflect**
*Don\u2019t just collect tasks, but **collate evidence** (How, when & what). Have a
**digital portfolio**. Do not have a **career mismatch**.*

### Skills to develop (7)
Technical skills acquisition \u00b7 communication \u00b7 **digital literacy** \u00b7 team work \u00b7
**speaking/presentation** \u00b7 **work ethics** \u00b7 **networking**.
Only **one** is technical \u2014 the rest are soft/transferable.

### Twelve Weeks Action Plan
Set **3\u20135 goals** \u00b7 **CV and LinkedIn tailored to your goals** \u00b7 build a **job
portfolio \u2014 document evidence** \u00b7 build **technical skills** \u00b7 **document evidence
of skills** \u00b7 **close your skill gap**, develop and improve consistently.

### Traps to watch
- **Prepare notebooks** is *before*; **keep a daily learning record** is *during*.
- **Communication** and **team work** appear on **both** the employers\u2019 list and the
  skills list \u2014 they cannot distinguish the two.
- **Punctuality, integrity, professionalism** are **observed traits**, not listed skills.
- **12 weeks** is the plan; **8 weeks** is the SWEP minimum; **24 weeks** is SIWES II.
- The note names the speaker only as a **NECA representative** \u2014 no personal name is given.
""",
    },
]

QUESTION_SETS = [DAY1, DAY2, DAY3, DAY4, DAY5]

BEGIN = '// ==== SWEP 200 BEGIN (generated by scripts/splice_swep200.py) ===='
END = '// ==== SWEP 200 END ===='


def js(obj, indent):
    """Dump as JSON (valid JS) with a fixed indent.

    ensure_ascii=True is deliberate: it escapes newlines inside long markdown
    strings (summaryNotes, solution) as \\n, so the emitted data.js stays a
    single valid JS expression instead of breaking across raw line breaks.
    """
    raw = json.dumps(obj, indent=2, ensure_ascii=True)
    pad = ' ' * indent
    return '\n'.join(pad + line if i else line for i, line in enumerate(raw.split('\n')))


def strip_previous(src):
    """Remove a previously spliced SWEP 200 block, if any, for idempotency."""
    # lectureMeta FIRST: its own `"swep200": [...]` would otherwise be consumed
    # by the generic loop below and throw the one-to-one order off.
    src = re.sub(r'export const lectureMeta = \{[\s\S]*?\n\}\n\n', '', src, count=1)
    # course entry
    src = re.sub(r'\n\s*\{\s*"id":\s*"swep200".*?\n\s*\},(?=\n\])', '', src, flags=re.S)
    # categoryMeta / topicMeta / questionBank entries (now the only remaining
    # `"swep200": [...]` blocks, in that exact order).
    for key in ('categoryMeta', 'topicMeta', 'questionBank'):
        src = re.sub(r'\n  "swep200": \[.*?\n  \],(?=\n)', '', src, count=1, flags=re.S)
    return src


def main():
    src = DATA.read_text()
    if 'swep200' in src:
        print('! existing SWEP 200 block found — replacing it')
        src = strip_previous(src)

    questions = [q for group in QUESTION_SETS for q in group]

    # Stamp each question with the lecture it belongs to (SWEP 200 has a
    # per-lecture test mode that splits the bank by slide title).
    lmap = question_lecture_map()
    for q in questions:
        lid = lmap.get(q['id'])
        if lid is None:
            raise SystemExit(f"{q['id']}: no lecture mapped")
        q['lectureId'] = lid

    # Guard: every question must point at a declared topic, and every declared
    # category must end up owning at least one topic (the validator enforces
    # this too, but failing here gives a far clearer message).
    topic_ids = {t['id'] for t in TOPICS}
    for q in questions:
        if q['topicId'] not in topic_ids:
            raise SystemExit(f"{q['id']}: unknown topicId {q['topicId']!r}")
    used_cats = {t['categoryId'] for t in TOPICS}
    # Keep a category if it owns topics OR if it is a virtual span-all one.
    cats = [c for c in CATEGORIES
            if c['id'] in used_cats or c.get('spansAll')]
    dropped = [c['id'] for c in CATEGORIES
               if c['id'] not in used_cats and not c.get('spansAll')]
    if dropped:
        print(f'  (categories with no topics yet, omitted: {", ".join(dropped)})')

    # 1. courses ------------------------------------------------------------
    src = src.replace('  "available": true\n},\n]',
                      '  "available": true\n},\n' + js(COURSE, 0) + ',\n]', 1)

    # NOTE: plain str.replace, never re.sub, for these insertions. The JSON
    # payload contains backslash escapes (\n, \u2014) which re.sub would try to
    # interpret as regex replacement escapes and choke on.

    # 2. categoryMeta -------------------------------------------------------
    cat_payload = f'  "swep200": {js(cats, 2)},\n'
    if 'export const categoryMeta = {}' in src:
        src = src.replace('export const categoryMeta = {}',
                          'export const categoryMeta = {\n' + cat_payload + '}', 1)
    else:
        src = src.replace('export const categoryMeta = {\n',
                          'export const categoryMeta = {\n' + cat_payload, 1)

    # 3. topicMeta ----------------------------------------------------------
    src = src.replace('export const topicMeta = {\n',
                      'export const topicMeta = {\n  "swep200": ' + js(TOPICS, 2) + ',\n', 1)

    # 4. lectureMeta -------------------------------------------------------
    # Inserted before questionBank purely for readability; order is irrelevant
    # to the ES module imports. Each lecture carries the slide title it is
    # identified by, plus the day it belongs to and its speaker.
    src = src.replace('export const questionBank = {\n',
                      'export const lectureMeta = {\n  "swep200": ' + js(LECTURES, 2) + ',\n}\n\nexport const questionBank = {\n', 1)

    # 5. questionBank -------------------------------------------------------
    src = src.replace('export const questionBank = {\n',
                      'export const questionBank = {\n  "swep200": ' + js(questions, 2) + ',\n', 1)

    DATA.write_text(src)
    print(f'✅ SWEP 200 spliced: {len(questions)} questions across {len(LECTURES)} lectures, '
          f'{len(TOPICS)} topic(s), {len(cats)} categor(ies)')


if __name__ == '__main__':
    main()
