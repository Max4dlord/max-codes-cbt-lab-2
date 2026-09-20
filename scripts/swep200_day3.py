#!/usr/bin/env python3
"""SWEP 200 - Day 3 question bank (40 questions).

Day 3: Wednesday, 16th September. Three lectures, per the orientation ledger:
  1. Entrepreneurship in the 5G Era        - Prof. A. B. Ayanwale
  2. Renewable Energy & PV Technology      - Dr. F. K. Ariyo
  3. Workshop Practice, Workforce &
     National Growth                       - Prof. V. Omidiji

Authored from the source decks (no supplied JSON this time), to the same
tertiary-examination standard as Days 1-2:

  * exhaustive sweep of every deck section, weighted by material volume
    (5G 14 / PV 13 / Workshop 13)
  * stem mix: numeric recall, category placement, definition/distinction,
    NOT questions, acronyms, sequence/order, speaker attribution, compound
    two-fact stems
  * distractors are REAL facts from the same deck, deliberately misplaced -
    an adjacent figure, the neighbouring generation, the other architecture,
    the sibling equation - never invented nonsense
  * solution template: "Why this is the answer" -> teaching block (table /
    contrast / memory hook) -> "Source" -> "Why the others fail"
  * answer key balanced across A/B/C/D

Verified page by page against:
  * Entrepreneurship in the 5G Era (30 pp.; 11 image-only slides rendered and
    read individually - the 5G targets, spectrum, capability and traffic
    tables live only in those images)
  * Dr Ariyo, Introduction to Renewable Energy (PV) Technology (25 pp.)
  * SWEP 2026 - Omidiji, Workshop Practice, Workforce and National Growth (18 pp.)
  * Handwritten Day 3 orientation ledger (speaker attributions)
"""

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
    # =============== Entrepreneurship in the 5G Era (Prof. A. B. Ayanwale) ======
    q('swep_day3_01',
      "In Prof. A. B. Ayanwale's lecture, the motivation for the 5G4BE course cites Sub-Saharan Africa's population and its projected youth profile. What are the two figures given?",
      ['More than 1 billion people, half of whom will be under 25 by 2050',
       'More than 2 billion people, half of whom will be under 25 by 2050',
       'More than 1 billion people, a quarter of whom will be under 25 by 2030',
       'About 800 million people, half of whom will be under 35 by 2050'],
      0,
      'Sub-Saharan Africa has more than 1 billion people, half under 25 by 2050.',
      """
### Why this is the answer
The motivation slide states that Sub-Saharan Africa is *"home to **more than 1
billion people**, half of whom will be **under 25 years old by 2050**"* — a
diverse continent whose human and natural resources can yield inclusive growth,
eradicate poverty and improve livelihoods.

### The second figure on the same slide
The continent hosts the world's **largest free trade area** and a
**1.2-billion-person market**, creating an entirely new development path.

Note the two population numbers are different things:
| Figure | What it describes |
|---|---|
| **1 billion+** | Sub-Saharan Africa's current population |
| **1.2 billion** | The size of the free-trade market |

### Why this opens an entrepreneurship lecture
A very young, very large, newly integrated market is precisely the condition in
which new digital ventures scale. The demographics *are* the business case.

### Source
Prof. A. B. Ayanwale, "Overview of the 5G4BE course — Motivation" slide.

### Why the others fail
Each alters one element — the population, the age threshold, the proportion or
the year. The exact combination is **1 billion+ / half / under 25 / by 2050**.
"""),

    q('swep_day3_02',
      'According to the mobile-generation timeline in the 5G lecture, which technology is paired with the correct generation and decade?',
      ['3G — LTE — 2010s', '2G — WCDMA/HSPA — 1990s',
       '4G — LTE — 2010s', '5G — cdma2000 — 2020s'],
      2,
      '4G is LTE, belonging to the 2010s.',
      """
### Why this is the answer
The deck's "From 1G to 5G" slide notes that the world has witnessed **five
mobile generations in the last 40 years**, each with its own technology and
decade:

| Gen | Technology | Decade | Described as |
|---|---|---|---|
| 1G | AMPS, TACS, NMT | 1980s | Foundation of mobile telephony |
| 2G | GSM, D-AMPS, PDC, IS-95 | 1990s | Mobile telephony for everybody |
| 3G | WCDMA/HSPA, cdma2000 | 2000s | Foundation of mobile broadband |
| **4G** | **LTE** | **2010s** | Further enhanced mobile broadband |
| 5G | **NR** (New Radio) | 2020s | Interconnected devices, sensors and systems (verticals) |

Only **4G — LTE — 2010s** is correctly paired.

### The distinction that matters
3G is the **foundation** of mobile broadband; 4G **enhances** it; 5G changes the
target altogether, moving from phones to **verticals** — industry, cities,
machines.

### Source
Prof. A. B. Ayanwale, "Mobile network — From 1G to 5G" slide (3GPP New Radio).

### Why the others fail
LTE is 4G, not 3G. WCDMA/HSPA is 3G, not 2G. cdma2000 is 3G; 5G's radio is
**NR**.
"""),

    q('swep_day3_03',
      'The lecture describes three 5G "superpowers". Which one is defined as near-instantaneous response times with extreme reliability?',
      ['Enhanced Mobile Broadband (eMBB)',
       'Massive Machine-Type Communications (mMTC)',
       'Ultra-Reliable Low-Latency Communication (URLLC)',
       'Network Slicing'],
      2,
      'URLLC delivers near-instantaneous response with extreme reliability.',
      """
### Why this is the answer
**URLLC** is described as *near-instantaneous response times (as low as **1ms**)
with extreme reliability* — the **"real-time control and safety" superpower**.

### The three superpowers, kept apart
| Superpower | What it is | Entrepreneurial framing |
|---|---|---|
| **eMBB** | Insanely high speeds, massive bandwidth — *"a firehose for data"* | Content and data delivery |
| **URLLC** | **~1 ms latency**, extreme reliability | **Real-time control and safety** |
| **mMTC** | Connect a staggering number of low-power devices | Massive data collection |

### What URLLC unlocks
Autonomous drone fleets for last-mile delivery and industrial inspection;
mission-critical services such as remote-controlled manufacturing robotics and
**tele-surgery**; and competitive multiplayer gaming where latency is
imperceptible.

### Source
Prof. A. B. Ayanwale, "Superpower #2: Ultra-Reliable Low-Latency
Communication (URLLC)" slide.

### Why the others fail
eMBB is about **bandwidth**, mMTC about **device count**. Network Slicing is not
a superpower at all — it is listed separately as an **underlying enabler**.
"""),

    q('swep_day3_04',
      'Which pairing of a 5G superpower with its stated entrepreneurial advantage is correct?',
      ['eMBB — "massive data collection" superpower',
       'mMTC — "real-time control and safety" superpower',
       'URLLC — "content and data delivery" superpower',
       'mMTC — "massive data collection" superpower'],
      3,
      'mMTC is the "massive data collection" superpower.',
      """
### Why this is the answer
Each superpower is given a specific entrepreneurial label in the deck, and this
question tests whether the labels are matched to the right capability:

| Superpower | Its stated advantage |
|---|---|
| eMBB | *"content and data delivery"* superpower |
| URLLC | *"real-time control and safety"* superpower |
| **mMTC** | ***"massive data collection"*** **superpower** |

### Why mMTC earns that label
It connects a *staggering number of low-power devices simultaneously*, enabling
smart agriculture with thousands of soil, weather and crop sensors; end-to-end
asset tracking across a supply chain; and analysis of data from **billions** of
smart-city devices for traffic, waste and energy optimisation.

The logic is simple: mMTC's value is in the **number of sources**, not the speed
of any one of them — so its business model is collection, not delivery.

### Source
Prof. A. B. Ayanwale, "Superpower #3: Massive Machine-Type Communications"
slide.

### Why the others fail
Each swaps a label onto the wrong superpower. All three labels are real; only
one pairing is right.
"""),

    q('swep_day3_05',
      'According to the 5G targets slide, what are the stated peak data rate and radio latency targets for 5G?',
      ['>10 Gbps peak data rates and <1 ms radio latency',
       '>1 Gbps peak data rates and <10 ms radio latency',
       '100 Mbps peak data rates and <1 ms radio latency',
       '>10 Gbps peak data rates and <10 ms radio latency'],
      0,
      '5G targets >10 Gbps peak data rates and <1 ms radio latency.',
      """
### Why this is the answer
The "5G targets" slide sets out the headline numbers:

| Target | Value |
|---|---|
| **Peak data rates** | **>10 Gbps** |
| **Radio latency** | **<1 ms** |
| Guaranteed experience | **100 Mbps** whenever needed |
| Traffic growth | **10 000×** more traffic |
| Device density | **10–100×** more devices |
| Battery life | **10 years** on battery |

### The trap inside this question
**100 Mbps** is a real 5G figure — but it is the *"whenever needed"* guaranteed
rate, **not** the peak. Peak is **>10 Gbps**. One slide, two speed numbers, two
very different meanings.

### How the targets map to the superpowers
The slide groups them: *"Unlimited experience"* → eMBB; *"For everything"* →
IoT/mMTC; *"Instant action"* → URLLC.

### Source
Prof. A. B. Ayanwale, "What is 5G? — 5G targets" slide (3GPP New Radio).
"""),

    q('swep_day3_06',
      'On the 5G capabilities comparison against LTE, 5G targets 10× lower latency. What specific target value is given?',
      ['<10 ms', '<10 μWh per tx', '<2 cent/GB', '<1 ms'],
      3,
      'The 10× lower latency target is <1 ms.',
      """
### Why this is the answer
The "5G capabilities" table lists each gain against LTE alongside a hard target
value:

| Gain vs LTE | Target value |
|---|---|
| 10× data rates | 10 Gbps |
| 10× lower cost | <2 cent/GB |
| **10× lower latency** | **<1 ms** |
| 10× lower IoT power | <10 μWh per tx |
| 5× energy efficiency | <2 kWh/TB |
| 5× spectral efficiency | >10 bps/cell/Hz |

### Why the distractors are dangerous
Every wrong option is a **real target value from the very same table** — just
attached to a different row. `<2 cent/GB` is the cost target; `<10 μWh per tx`
is the IoT power target. Reading the row, not just recognising the number, is
what earns the mark.

### Note the pattern
The first four gains are **10×**; the last two are **5×**. Energy and spectral
efficiency improve less dramatically than speed, cost, latency and IoT power.

### Source
Prof. A. B. Ayanwale, "What is 5G? — 5G capabilities" slide.
"""),

    q('swep_day3_07',
      'According to the 5G spectrum table, what data rate is associated with the 20–90 GHz band, and what spectrum per operator does it assume?',
      ['2 Gbps with 100 MHz per operator',
       '0.2 Gbps with 10 MHz per operator',
       '5–20 Gbps with 1 GHz per operator',
       '5–20 Gbps with 100 MHz per operator'],
      2,
      'The 20–90 GHz band gives 5–20 Gbps with 1 GHz of spectrum per operator.',
      """
### Why this is the answer
The 5G spectrum table pairs each band with the spectrum an operator gets and the
resulting data rate:

| Spectrum | Per operator | Data rate |
|---|---|---|
| **20–90 GHz** | **1 GHz** | **5–20 Gbps** |
| Below 6 GHz | 100 MHz | 2 Gbps |
| Below 1 GHz | 10 MHz | 0.2 Gbps |

### The engineering principle behind the table
More bandwidth buys more speed, but higher frequencies travel less far and
penetrate buildings poorly. So the slide maps each band to a coverage role:

- **20–90 GHz** → *extreme local data rates*
- **Below 6 GHz** → *high rates with urban macro sites*
- **Below 1 GHz** → *wide area and deep indoor coverage*

That is the trade-off an entrepreneur must design around — you cannot have
20 Gbps **and** deep indoor coverage from the same band.

### Also stated
5G NR is designed for flexible use of all spectrum from **400 MHz to 90 GHz**,
including licensed, shared and unlicensed (TDD/FDD). New IMT bands were
identified at **WRC-19**.

### Source
Prof. A. B. Ayanwale, "What is 5G? — 5G Spectrum" slide.
"""),

    q('swep_day3_08',
      'Which of the following is NOT listed among the five 5G technology components?',
      ['New spectrum', 'Beamforming', 'Network slicing', 'Quantum encryption'],
      3,
      'Quantum encryption is not one of the five 5G technology components.',
      """
### Why this is the answer
A **NOT** question. The deck names exactly five technology components:

1. **New spectrum**
2. **Beamforming**
3. **Network slicing**
4. LTE dual connectivity and LTE coexistence
5. Cloud-optimised architecture — *move part of the cloud processing to the edge*

**Quantum encryption** appears nowhere in the component list.

### The near-miss worth noting
**Quantum computing** *is* mentioned in this lecture — but on the **6G** slide,
as a future convergence alongside AI and advanced sensing. It is a
*forward-looking* technology, not a current 5G component. Recognising a term
from elsewhere in the deck is not the same as it belonging here.

### Two components double as business opportunities
**Network slicing** lets a founder rent a virtual network optimised for their
application instead of building infrastructure, and **edge computing** enables
privacy-first, real-time AI. Both are explicitly framed as lowering the barrier
to entry.

### Source
Prof. A. B. Ayanwale, "What is 5G? — Technology components" and "The Underlying
Enablers" slides.
"""),

    q('swep_day3_09',
      'How does the lecture describe Network Slicing as an entrepreneurial enabler?',
      ['It allows founders to buy discounted spectrum licences from regulators',
       'It lets a founder rent a virtual network slice optimised for their application, lowering the barrier to entry',
       'It splits company equity among technical and business co-founders',
       'It processes data locally instead of in a distant cloud'],
      1,
      'Network slicing lets founders rent an optimised virtual network instead of building one.',
      """
### Why this is the answer
The slide addresses the founder directly: *"Don't have the capital to build a
massive network? No problem. You can **rent a virtual network slice** perfectly
optimised for your application's needs, whether it's for low latency or high
bandwidth. This **dramatically lowers the barrier to entry** for
entrepreneurs."*

### The two enablers side by side
| Enabler | What it does | Business effect |
|---|---|---|
| **Network Slicing** | Rent a virtual network tuned to your needs | **Removes the capital barrier** |
| **Edge Computing** | Process data **locally**, not in a distant cloud | Privacy-first models, real-time AI |

### The trap in option D
*"Processes data locally instead of in a distant cloud"* is a genuine, correctly
worded definition — **of edge computing**, the other enabler on the same slide.
Classic adjacent-fact distractor.

### Source
Prof. A. B. Ayanwale, "The Underlying Enablers: Fueling Your Business" slide.
"""),

    q('swep_day3_10',
      'Under Smart Manufacturing (Industry 4.0), what problem does the lecture say 5G addresses?',
      ['Manufacturing is inefficient, with costly downtime and reliance on rigid, wired infrastructure',
       'Access to specialists is limited and patient monitoring is cumbersome',
       'Urban infrastructure is static and reactive, causing congestion',
       'Content is passive and AR/VR requires expensive hardware'],
      0,
      'Manufacturing suffers costly downtime and rigid, wired infrastructure.',
      """
### Why this is the answer
The lecture structures each industry as **Problem → 5G Solution → Startup
Ideas**. For **Smart Manufacturing (Industry 4.0)** the problem is that
manufacturing is *often inefficient, with **costly downtime** and a reliance on
**rigid, wired infrastructure***. The 5G solution is *wireless, flexible and
real-time*.

### Every distractor is another industry's problem statement
| Problem stated | Belongs to |
|---|---|
| Limited specialist access, cumbersome monitoring | **Smart Healthcare** |
| Static, reactive urban infrastructure | **Smart Cities & Urban Tech** |
| Passive content, expensive AR/VR hardware | **Media & Entertainment** |

All four are verbatim problems from the deck — only one belongs to
manufacturing.

### The startup ideas that follow
**Predictive Maintenance as a Service** (5G sensors plus edge AI predicting
component failure, sold on subscription), **AR-Powered Training**, and
**Autonomous Warehouse Logistics** using 5G-enabled AGVs.

### Source
Prof. A. B. Ayanwale, "Part 2: Industry-Specific Opportunities for Founders —
1. Smart Manufacturing" slide.
"""),

    q('swep_day3_11',
      'The lecture recommends a specific method for finding a 5G business idea. What is the correct order of that approach?',
      ['Start with a 5G capability, then search for an industry that might need it',
       'Start with a pain point, then apply the "5G lens" to see how a superpower uniquely solves it',
       'Start with a business model canvas, then choose a technology',
       'Start by assembling a technical team, then let them choose the product'],
      1,
      'Start with a pain point, then apply the "5G lens".',
      """
### Why this is the answer
The instruction is explicit: *"**Don't start with a solution; start with a pain
point.** What's a major problem in an industry you're passionate about?"* Only
then do you apply the **"5G lens"** — asking how high speed, low latency or
massive connectivity can solve that problem in a way that **wasn't possible
before**.

### The lecture's worked example
> **Pain point:** it is difficult for remote doctors to get a high-quality,
> real-time view of a patient's wound.
> **5G lens:** use **eMBB** to stream ultra-HD video from a portable camera, and
> **URLLC** to let the remote doctor control the camera's focus.

Note that one pain point pulls in **two different superpowers** — that is what
applying the lens properly looks like.

### Why the sequence matters
Option A is precisely the trap: starting from the technology produces a solution
hunting for a problem. The other two steps are real — the Business Model Canvas
and team-building both appear — but they come **later** in Part 3, after the
idea exists.

### Source
Prof. A. B. Ayanwale, "Part 3: The Entrepreneurial Journey in 5G — 1. Finding
Your Idea: The '5G Lens'" slide.
"""),

    q('swep_day3_12',
      'According to the lecture, a great 5G startup team is multidisciplinary. Which three roles are named?',
      ['Domain experts, technical experts and business strategists',
       'Investors, marketers and software developers',
       'Network operators, regulators and hardware suppliers',
       'Data scientists, lawyers and accountants'],
      0,
      'Domain experts, technical experts and business strategists.',
      """
### Why this is the answer
*"A great 5G startup isn't just a tech team. It's a **multidisciplinary
team**."* The three named roles are:

| Role | What they bring | Example given |
|---|---|---|
| **Domain experts** | Deep understanding of the target industry | A **nurse** for health tech; a **supply chain manager** for logistics |
| **Technical experts** | Networking, cloud/edge computing, data science | Engineers |
| **Business strategists** | A viable business model and funding | — |

### The point being made
The **domain expert is listed first**, ahead of the engineers. A team that
understands 5G but not the industry will build something technically impressive
that nobody in that sector needs. This mirrors the "start with a pain point"
rule — you cannot identify a real pain point without someone who lives it.

### Why option C is tempting
Mobile operators and hardware manufacturers **are** named in the deck — but as
**Key Partners** on the Business Model Canvas, not as members of your team.

### Source
Prof. A. B. Ayanwale, "2. Building Your Team: The Right Mix" slide.
"""),

    q('swep_day3_13',
      'Which monetisation strategy does the lecture identify as "a key theme" for 5G startups?',
      ['Selling expensive hardware outright with a one-off margin',
       'Licensing patents to mobile network operators',
       '"As-a-Service" models, selling functionality rather than hardware',
       'Advertising-funded free access for all users'],
      2,
      '"As-a-Service" models are named as the key theme.',
      """
### Why this is the answer
The slide states: *"**'As-a-Service' Models:** This is a **key theme**. Instead
of selling expensive hardware, sell the **functionality as a service** (e.g.
Robotics-as-a-Service, Predictive Maintenance-as-a-Service)."*

### The three monetisation strategies listed
1. **"As-a-Service" models** — the key theme
2. **Usage-based pricing** — charge per data transmitted or per hour of usage
3. **Subscription & platform fees** — monthly consumer subscriptions, or a
   platform fee for developers building on your technology

### Why "as-a-service" fits 5G specifically
It mirrors what 5G does to infrastructure itself. **Network slicing** lets you
rent a network instead of building one; the same logic then flows to your
customers, who rent your capability instead of buying your hardware. Option A is
the exact model the slide tells founders to move **away** from.

### Where it reappears
The Smart Manufacturing section applies it directly — *Predictive Maintenance as
a Service*, sold on a **subscription model**.

### Source
Prof. A. B. Ayanwale, "3. Monetization Strategies for Startups" slide.
"""),

    q('swep_day3_14',
      'In the "Beyond 5G" discussion, which technologies is 6G expected to converge with?',
      ['Blockchain, 3D printing and biotechnology',
       'Artificial Intelligence, Quantum Computing and advanced sensing technologies',
       'Satellite television, fibre optics and copper broadband',
       'Virtual reality, cloud gaming and social media'],
      1,
      '6G is expected to converge with AI, quantum computing and advanced sensing.',
      """
### Why this is the answer
*"5G is here, but the research for **6G** has already begun... Expect even
greater convergence with **Artificial Intelligence (AI)**, **Quantum
Computing**, and **advanced sensing technologies**. The lines between the
physical and digital worlds will continue to blur."*

6G is envisioned to be more **immersive, intelligent and integrated**.

### Why this matters for the exam
This is also where **quantum computing** appears — a fact tested from the other
direction in the technology-components question. Quantum belongs to **6G's
future**, not to 5G's present architecture. Knowing *which slide* a term sits on
is what separates recall from understanding.

### The closing posture
*"The entrepreneurial journey in connectivity is **just beginning**"* — the
lecture deliberately ends by pointing past the technology students just learned.

### Source
Prof. A. B. Ayanwale, "Beyond 5G: Towards 6G and the Future" slide.
"""),

    # =============== Renewable Energy & PV Technology (Dr. F. K. Ariyo) ========
    q('swep_day3_15',
      'Dr. F. K. Ariyo opens by arguing that solar is not merely a panel on a roof. How is it characterised instead?',
      ['A purely electrical installation governed by wiring regulations',
       'A financial product best understood through payback periods',
       'A civil engineering structure requiring roof reinforcement',
       'A multidisciplinary engineering system'],
      3,
      'Solar is presented as a multidisciplinary engineering system.',
      """
### Why this is the answer
The opening hook is unambiguous: *"Solar is **not just a panel on a roof** — it
is a **multidisciplinary engineering system**."* The slide frames it across four
pillars:

| Pillar | Activity |
|---|---|
| **POWER** | Generate • convert • protect |
| **DATA** | Measure • monitor • predict |
| **DESIGN** | Size • model • optimise |
| **IMPACT** | Homes • clinics • farms |

Summarised as **SUN → PV → POWER**.

### Why "multidisciplinary" is the operative word
The following slide maps solar onto six disciplines students are already
studying — **Electrical** (power systems, machines, protection), **Electronics**
(converters, sensors, embedded), **Control** (MPPT, regulation, automation),
**AI/Data** (forecasting, fault diagnosis), **Materials** (semiconductors, PV
devices) and **Enterprise** (design, installation, service, finance).

The lecture's framing: **your degree → your solar specialisation**. Solar is not
a separate subject; it is where existing skills converge.

### Source
Dr. F. K. Ariyo, "Opening Hook" and "Career Signal" slides.
"""),

    q('swep_day3_16',
      'In the solar energy chain described as "from sunlight to useful work", what is the correct order of the five stages?',
      ['Sunlight → PV cell → inverter → MPPT → load/grid',
       'Sunlight → MPPT → PV cell → inverter → load/grid',
       'Sunlight → PV cell → MPPT → inverter → load/grid',
       'PV cell → sunlight → MPPT → load/grid → inverter'],
      2,
      'Sunlight → PV cell → MPPT → inverter → load/grid.',
      """
### Why this is the answer
"The Big Picture" slide sets out the energy flow in five numbered stages:

| # | Stage | What happens |
|---|---|---|
| 1 | **Sunlight** | Photons |
| 2 | **PV cell** | DC electricity |
| 3 | **MPPT** | Extract maximum power |
| 4 | **Inverter** | DC → AC |
| 5 | **Load / Grid** | Useful work |

### Why MPPT must precede the inverter
The PV array produces **variable DC**. MPPT tracks the moving maximum-power
point and delivers a **regulated DC bus**; only then does the inverter convert
that to **controlled AC**. Swapping them — as option A does — would ask the
inverter to work from an unoptimised, fluctuating input.

The deck confirms the chain elsewhere: *PV array (variable DC) → MPPT controller
(search/track) → DC bus (regulated energy) → inverter (controlled AC)*.

### The engineering question attached
*"**Where are the losses — and how do we reduce them?**"* Each arrow in the
chain is a place efficiency is lost.

### Source
Dr. F. K. Ariyo, "The Big Picture" and "Power Electronics" slides.
"""),

    q('swep_day3_17',
      'Inside a solar cell, what sequence does the lecture use to explain how light becomes current?',
      ['The semiconductor stores light as heat, which is later converted to electricity',
       'Light creates electron–hole pairs; the junction and contacts separate charge; the external circuit carries current',
       'The p–n junction emits photons which are captured by the contacts',
       'Sunlight directly induces alternating current in the cell wiring'],
      1,
      'Light creates electron–hole pairs; the junction separates charge; the external circuit carries current.',
      """
### Why this is the answer
The device-physics slide asks students to *"think like an electron"* and gives
three steps:

1. **Semiconductor absorbs light** — light creates **electron–hole pairs**
2. **Charge carriers are separated** — by the **p–n junction** and contacts
3. **External circuit carries current**

Summarised as **PHYSICS → DEVICE → POWER**.

### Why option D is decisively wrong
A PV cell produces **DC**, not AC. That is the entire reason an **inverter**
exists later in the chain. If sunlight induced AC directly, stage 4 of the
energy flow would be unnecessary.

### Scaling the device
One cell is tiny, so engineering scales it: **CELL → MODULE → STRING → ARRAY**
(single photovoltaic device → cells connected and packaged → modules in series →
strings forming a field). The challenge grows with scale: **mismatch,
protection, wiring, thermal behaviour, control and maintenance**.

### Source
Dr. F. K. Ariyo, "Device Physics" and "From Cell to Array" slides.
"""),

    q('swep_day3_18',
      'On the I–V curve of a photovoltaic panel, which three points are labelled?',
      ['Isc, MPP and Voc', 'Isc, MPPT and Vmax',
       'Imax, MPP and Vsc', 'Ioc, MPP and Vsc'],
      0,
      'The I–V curve is labelled with Isc, MPP and Voc.',
      """
### Why this is the answer
The characteristics slide plots current and power against voltage, labelling
three points:

| Symbol | Meaning | Where it sits |
|---|---|---|
| **Isc** | Short-circuit current | Vertical axis, zero volts |
| **MPP** | **Maximum Power Point** | The knee of the curve |
| **Voc** | Open-circuit voltage | Horizontal axis, zero current |

### The distinction the distractors exploit
**MPP** is the *point* on the curve. **MPPT** is the **tracking technology** —
the controller that hunts for that point. Option B swaps the point for the
technique, which is the single most common confusion in introductory PV.

Likewise the subscripts are not interchangeable: **sc** = short-circuit,
**oc** = open-circuit. "Vsc" and "Ioc" are meaningless — short-circuit voltage
is zero, and open-circuit current is zero.

### The engineering question on the slide
*"Where should the converter operate to capture maximum power?"* — the answer,
of course, is at the **MPP**, which is precisely what MPPT is for.

### Source
Dr. F. K. Ariyo, "Characteristics" slide.
"""),

    q('swep_day3_19',
      'Why is Maximum Power Point Tracking (MPPT) necessary rather than simply fixing the operating point once?',
      ['Because inverters can only accept one fixed voltage',
       'Because the grid frequency varies through the day',
       'Because batteries must always be charged at constant current',
       'Because irradiance and temperature change, so the maximum-power point moves'],
      3,
      'Irradiance and temperature change, so the maximum-power point moves.',
      """
### Why this is the answer
The slide states the cause directly: *"Irradiance changes → temperature changes
→ **the maximum-power point moves**."* A fixed operating point would be optimal
only for one instant; MPPT is described as *"making every ray count"*.

### The two drivers, from the design-reality slide
| Condition | Effect on the panel |
|---|---|
| **Less irradiance** | Less **current** |
| **Higher cell temperature** | Lower **voltage** |

Since power is the product of the two, any change in sun or heat shifts the MPP
along the I–V curve. Both vary continuously through a day.

### Where MPPT sits
**PV array** (variable DC) → **MPPT controller** (search/track) → **DC bus**
(regulated) → **inverter** (controlled AC). The deck labels this the meeting
point of **control systems + power electronics**.

### Source
Dr. F. K. Ariyo, "Power Electronics: MPPT" and "Design Reality" slides.
"""),

    q('swep_day3_20',
      'Which of the following is NOT listed among the six factors affecting solar system performance?',
      ['Soiling', 'Shading', 'Grid tariff structure', 'Degradation'],
      2,
      'Grid tariff structure is not one of the six performance factors.',
      """
### Why this is the answer
A **NOT** question. "Design Reality" names exactly six factors:

| Factor | Effect |
|---|---|
| **Irradiance** | Less sunlight → less current |
| **Temperature** | Higher cell temperature → lower voltage |
| **Shading** | Mismatch can hurt a **whole string** |
| **Soiling** | Dust reduces optical input |
| **Mismatch** | Cells/modules are never perfectly identical |
| **Degradation** | Performance changes with age |

**Grid tariff structure** is a commercial consideration, not a physical
performance factor, and appears nowhere on the slide.

### The design principle attached
*"Good design is **not 'buy more panels'**. It is understanding the **full chain
of causes and effects**."* Adding capacity does not fix shading, soiling or
mismatch — diagnosis does.

### Note how severe shading is
Shading is not local: partial shade on one module can **hurt a whole string**
through mismatch. That is why it reappears in the diagnostics slide as a named
fault.

### Source
Dr. F. K. Ariyo, "Design Reality" slide.
"""),

    q('swep_day3_21',
      'The lecture describes three PV system architectures. Which description matches the OFF-GRID configuration?',
      ['PV → inverter → grid/load, used for homes, offices and campuses',
       'PV → controller → battery → loads, used for remote sites such as primary health centres',
       'PV + grid/generator + battery, used for critical loads and resilience',
       'PV → grid only, with no storage or local loads'],
      1,
      'Off-grid runs PV → controller → battery → loads, for remote sites.',
      """
### Why this is the answer
Three architectures are set out side by side:

| Architecture | Flow | Typical use |
|---|---|---|
| **Grid-tied** | PV → inverter → grid/load | Homes, offices, campuses |
| **Off-grid** | **PV → controller → battery → loads** | **Remote sites: PHCs** |
| **Hybrid** | PV + grid/generator + battery | Critical loads, resilience |

### The defining feature of off-grid
There is **no grid in the chain at all**. Because nothing else can supply power
when the sun is down, the **battery is mandatory** — it is the only thing
standing between the load and darkness. In grid-tied systems the grid plays that
role; in hybrid, both are available.

### The rule the slide insists on
> **Choose architecture from the load and reliability need — not from the panel
> count.**

A rural clinic needing 24-hour refrigeration has a *reliability* requirement,
and that dictates off-grid or hybrid before anyone counts panels.

### Source
Dr. F. K. Ariyo, "System Architectures" slide.
"""),

    q('swep_day3_22',
      'In the battery storage discussion, what distinction does the lecture draw between kW and kWh?',
      ['kW is energy and kWh is power',
       'kW measures battery capacity and kWh measures charging speed',
       'kW applies to DC systems and kWh to AC systems',
       'kW measures how fast (power) and kWh measures how much (energy)'],
      3,
      'kW is power — how fast; kWh is energy — how much.',
      """
### Why this is the answer
The slide instructs students to *"think in kW and kWh"*:

| Unit | Question it answers |
|---|---|
| **kW** | **Power — how fast?** |
| **kWh** | **Energy — how much?** |

### The worked example on the slide
> A **2-kW** load running for **4 h** needs **8 kWh** of energy.

That is simply **power × time = energy**, and it is the calculation behind every
battery sizing decision.

### The related battery terms introduced
- **SoC** — state of charge
- **DoD** — depth of discharge
- **BMS** — battery management system
- **Efficiency** — charge/discharge losses

### Why the distinction matters
> **Storage turns sunshine into dispatchable energy.**

An inverter must be rated in **kW** to survive the peak load; a battery must be
sized in **kWh** to last the night. Confuse the two and the system fails in one
direction or the other.

### Source
Dr. F. K. Ariyo, "Energy Storage" slide.
"""),

    q('swep_day3_23',
      'Which three components does the lecture say students should be able to identify immediately?',
      ['Inverter, MPPT controller and LiFePO₄ battery',
       'PV module, junction box and earthing rod',
       'Transformer, circuit breaker and busbar',
       'Irradiance sensor, thermocouple and data logger'],
      0,
      'Inverter, MPPT charge controller and LiFePO₄ battery.',
      """
### Why this is the answer
The "Component Deep Dive" slide names three components *"students should be able
to identify immediately"*, each with its one-line function:

| Component | Function |
|---|---|
| **Inverter** | **DC → AC** |
| **MPPT controller** | Regulates PV/battery charging |
| **LiFePO₄ battery** | Stores electrical energy |

### The fuller component chain
The recognition slide lists the whole system: **PV module → inverter → MPPT
charge controller → battery storage → protection/distribution**.

### Inside the inverter — "the system translator"
| Aspect | Detail |
|---|---|
| DC input | PV array / battery |
| Switching | **MOSFET / IGBT** power stage |
| Control | **PWM**, current/voltage loops |
| Synchronisation | Grid **frequency and phase** |
| Protection | Overcurrent, overvoltage, **islanding** |

Summarised as **DC → CONTROL → AC**: power electronics + control + protection.

### Source
Dr. F. K. Ariyo, "Component Recognition", "Component Deep Dive" and "System
Heart" slides.
"""),

    q('swep_day3_24',
      'The lecture argues a solar plant is also a data system. Which set of quantities does it list as measured, transmitted and visualised?',
      ['Share price, tariff rate and payback period',
       'Irradiance, PV voltage, PV current, temperature, energy yield and battery SoC',
       'Wind speed, rainfall, humidity and air pressure',
       'Panel dimensions, weight, tilt angle and azimuth'],
      1,
      'Irradiance, PV voltage, PV current, temperature, energy yield and battery state of charge.',
      """
### Why this is the answer
"Digital Solar" lists six measured quantities, each following the same pipeline
of **MEASURE → TRANSMIT → VISUALISE**:

| Quantity | Unit |
|---|---|
| Irradiance | W/m² |
| PV voltage | V |
| PV current | A |
| Temperature | °C |
| Energy yield | kWh |
| Battery SoC | % |

### The line that matters
> **Once you can measure performance, you can start predicting it.**

That single sentence is the bridge from hardware to **IoT • embedded systems •
cloud • AI**, and it sets up the entire diagnostics and AI section that follows.

### Why option C is a near-miss
Weather data is genuinely used in this lecture — but on the **AI** slide, where
forecasting predicts *"PV output from **weather** + history"*. It is an **input
to prediction**, not one of the six quantities the plant itself measures.

### Source
Dr. F. K. Ariyo, "Digital Solar" slide.
"""),

    q('swep_day3_25',
      'In the diagnostics section, which fault is paired with the correct consequence?',
      ['Partial shade → no AC output', 'Loose connector → arcing/outage',
       'Inverter trip → thermal risk', 'Hot spot → power loss only'],
      1,
      'A loose connector causes arcing/outage.',
      """
### Why this is the answer
The diagnostics slide maps five faults to five consequences:

| Fault | Consequence |
|---|---|
| Dust/soiling | Power loss |
| Partial shade | **Mismatch** |
| Hot spot | **Thermal risk** |
| **Loose connector** | **Arcing / outage** |
| Inverter trip | **No AC output** |

Only **loose connector → arcing/outage** is correctly paired.

### How the distractors were built
Each wrong option takes a real fault and attaches **another fault's real
consequence**: *no AC output* belongs to inverter trip, *thermal risk* to hot
spot, *power loss* to soiling. Every term is genuine; only the pairing is wrong.

### The workflow being taught
**SENSOR DATA → ANOMALY → DIAGNOSIS → ACTION → VERIFY.**
The slide calls this *"**predictive maintenance thinking** — applied to energy
infrastructure"*, which is the same concept the 5G lecture sells as
*Predictive-Maintenance-as-a-Service*. Two Day 3 lectures, one idea.

### Source
Dr. F. K. Ariyo, "Diagnostics" slide.
"""),

    q('swep_day3_26',
      'In the mini design challenge for a small rural clinic, what three illustrative assumptions are given?',
      ['Daily energy 8 kWh/day, peak load 2 kW, autonomy 1 day',
       'Daily energy 2 kWh/day, peak load 8 kW, autonomy 2 days',
       'Daily energy 8 kWh/day, peak load 4 kW, autonomy 3 days',
       'Daily energy 4 kWh/day, peak load 2 kW, autonomy 1 day'],
      0,
      'Daily energy 8 kWh/day, peak load 2 kW, autonomy 1 day.',
      """
### Why this is the answer
The brief asks students to design an introductory solar-battery system for a
small rural clinic, with three illustrative assumptions:

| Assumption | Value |
|---|---|
| **Daily energy** | **8 kWh/day** |
| **Peak load** | **2 kW** |
| **Autonomy** | **1 day** |

Students must then choose **PV capacity, battery capacity, inverter rating and
basic protection**.

### These are not arbitrary numbers
They are the same figures as the storage worked example: *a **2-kW** load running
for **4 h** needs **8 kWh***. The challenge reuses them deliberately, so each
assumption drives one sizing decision:

- **Peak load (2 kW)** → sizes the **inverter**
- **Daily energy (8 kWh)** → sizes the **PV array**
- **Autonomy (1 day)** → sizes the **battery**

That mapping is the actual lesson — which number governs which component.

### Source
Dr. F. K. Ariyo, "Mini Design Challenge" slide; cross-referenced with "Energy
Storage".
"""),

    q('swep_day3_27',
      'According to the PV safety slide, why is isolation planning stressed as non-negotiable?',
      ['Because inverters cannot be switched off once installed',
       'Because AC wiring is more dangerous than DC wiring',
       'Because batteries discharge instantly when disconnected',
       'Because PV DC can remain energised in sunlight'],
      3,
      'PV DC can remain energised in sunlight, so isolation must be planned.',
      """
### Why this is the answer
The safety slide opens with the hazard that makes PV different from ordinary
electrical work: *"**PV DC can remain energised in sunlight** — isolation must be
planned."*

You cannot switch off the sun. A conventional circuit is made safe by opening a
breaker upstream; a PV array keeps generating whenever light falls on it, so the
isolation strategy has to be **designed in**, not improvised at the point of
maintenance.

### The five safety requirements listed
| Requirement | Purpose |
|---|---|
| **Isolation** | PV DC stays live in sunlight |
| **Overcurrent protection** | Protect strings, conductors, equipment |
| **Surge protection & earthing** | Manage transient and fault energy |
| **Battery hazards** | Correct **BMS**, enclosure and procedures |
| **Competent installation** | Follow manuals and applicable standards |

### Source
Dr. F. K. Ariyo, "Safety" slide.

### Why the others fail
Nothing in the deck claims AC is more dangerous than DC — the point is the
opposite, that PV's **DC side** carries an unusual, persistent hazard.
"""),

    # ====== Workshop Practice, Workforce & National Growth (Prof. V. Omidiji) ==
    q('swep_day3_28',
      'Prof. V. Omidiji defines workshop practice as hands-on training using three categories of resource. Which item is correctly classified?',
      ['The lathe is a hand tool', 'Powder metallurgy is a machine tool',
       'The power hack saw is a machine tool', 'Marking tools are manufacturing methods'],
      2,
      'The power hack saw is classified as a machine tool.',
      """
### Why this is the answer
Workshop practice *"refers to **hands-on training and skills** required in
engineering workshops"*, and the deck sorts its resources into three groups:

| Category | Examples given |
|---|---|
| **Hand tools** | Hammers, saws, pliers, **marking tools** |
| **Machine tools** | The **lathe**, milling machine, drilling machine, **power hack saw** |
| **Manufacturing methods** | Machining, casting, **powder metallurgy**, welding, **additive manufacturing** |

Only the **power hack saw → machine tool** pairing is correct.

### Why the classification is examinable
Each distractor moves a real item into the wrong category — the lathe (a machine
tool) called a hand tool, powder metallurgy (a *method*) called a tool, marking
tools (hand tools) called methods. The distinction is between **what you hold**,
**what you operate**, and **what you do**.

### Note on automation
The deck adds that *"many manufacturing processes are **automated** and some are
**hand-crafted**"*, accomplished by human effort or machinery — and that each
process has various sub-divisions.

### Source
Prof. V. Omidiji, "What is workshop practice?" slide.
"""),

    q('swep_day3_29',
      'Workshop practice is described as starting from a defined sequence. What is the correct order of the first five stages?',
      ['Measurements → identification of materials → marking out → cutting → joining or machining',
       'Identification of materials → measurements → marking out → cutting to measured sizes → joining or machining',
       'Marking out → cutting → measurements → identification of materials → joining',
       'Identification of materials → marking out → measurements → joining → cutting'],
      1,
      'Materials → measurements → marking out → cutting → joining or machining.',
      """
### Why this is the answer
The deck numbers the stages explicitly:

| # | Stage | Detail |
|---|---|---|
| 1 | **Identification of materials and their properties** | Where can each material be used? |
| 2 | **Measurements** | Meter rule, **vernier calliper**, micrometer screw gauge |
| 3 | **Marking out** | *"Done on the **marking-out table**, not on the floor"* |
| 4 | **Cutting to measured sizes** | Hack saw or other cutting devices |
| 5 | **Joining or machining** | Joining by **welding**; machining by conventional methods |

### Why the order is logical, not arbitrary
You cannot measure sensibly until you know what the material is and how it
behaves; you cannot mark out before measuring; and you certainly cannot cut
before marking. Each stage supplies the input for the next — which is exactly why
an examiner can test it as a sequence.

### The detail worth remembering
Marking out is done **on the marking-out table, not on the floor** — a small
instruction, but the deck states it pointedly, and precision in marking is what
makes the later cut accurate.

### Source
Prof. V. Omidiji, "Workshop practice starts from:" slide.
"""),

    q('swep_day3_30',
      'Activities in workshop practice are broadly categorised into three focuses. Which three?',
      ['Skill development, team building and problem-solving',
       'Lecturing, examination and certification',
       'Design, procurement and installation',
       'Marking, cutting and welding'],
      0,
      'Skill development, team building and problem-solving.',
      """
### Why this is the answer
*"Workshop practice activities can be broadly categorised into those focused on
**skill development**, **team building**, and **problem-solving**."* These are
delivered through **hands-on tasks, group discussions and simulations** to
facilitate learning and collaboration.

### Note what is absent
Only one of the three is purely technical. **Team building** and
**problem-solving** are human competencies — the same ground Day 2's
employability lecture covered under *collaboration and teamwork* and *critical
thinking and problem-solving*. The workshop is being presented as a place where
soft skills are trained alongside technical ones.

### Why option D is the trap
Marking, cutting and welding are genuine workshop **operations** — they appear in
the five-stage sequence — but they are *tasks*, not the *focus categories* of the
activities. The question asks what the activities are **for**, not what they
consist of.

### Source
Prof. V. Omidiji, "Activities in Workshop Practice" slide.
"""),

    q('swep_day3_31',
      'Among the detailed outcomes of workshop practice, which is listed under "Skill Development" rather than another heading?',
      ['Direct exposure to machine tools like lathes and milling machines',
       'Covering production methods such as casting, forging, welding and machining',
       'Teaching proper handling of tools to prevent workplace accidents',
       'Enhancing precision, accuracy and efficiency with metals, plastics and composites'],
      3,
      'Enhancing precision, accuracy and efficiency is listed under Skill Development.',
      """
### Why this is the answer
The deck numbers five detailed outcomes, and each distractor belongs to a
different one:

| # | Outcome | What it covers |
|---|---|---|
| 1 | **Hands-on Experience** | Direct exposure to lathes, milling, drilling, welding equipment |
| 2 | **Skill Development** | **Precision, accuracy, efficiency** with metals, plastics, composites; troubleshooting |
| 3 | **Safety Awareness** | Proper handling of tools; **PPE** |
| 4 | **Understanding Manufacturing Processes** | Casting, forging, welding, machining |
| 5 | **Application in Industrial Production** | Prototypes, assembly, testing finished products |

### The category-placement pattern
As in Day 2's warning-sign questions, **every option here is a genuine outcome
from the same slide** — placed under the wrong heading. The mark is earned by
knowing *which* heading owns it, not by recognising the words.

### The overall claim
Workshop practice *"enhances technical skills, improves problem-solving
abilities, and ensures precision in manufacturing and assembly"*, while
promoting safety awareness and preparing engineers for real-world industrial
challenges.

### Source
Prof. V. Omidiji, "Why is workshop practice important?" slides.
"""),

    q('swep_day3_32',
      'Which of the following is NOT among the workshop safety precautions listed by Prof. Omidiji?',
      ['Wear tight clothes, as loose clothing or long hair brings danger',
       'Never use a file or screwdriver without a handle',
       'Work alone whenever possible to avoid distraction',
       'Never operate a machine unless you thoroughly understand its mechanism'],
      2,
      'Working alone is not advised — the listed precautions never recommend it.',
      """
### Why this is the answer
A **NOT** question. The precautions listed are:

- Wear **tight clothes** — loose clothing or long hair brings danger
- Wear **covered footwear** — never sandals or slippers
- Never use a **file or screwdriver without a handle**
- Do not use a **hammer without a wedge**
- Never operate a machine unless you **thoroughly understand its mechanism**
- Wear **goggles** while chipping, welding or grinding
- Always wear **safety gloves, apron or dungaree and leather shoes**
- Never touch overhead lines unless properly **earthed and dead**
- Do not throw **water** on equipment — water conducts electricity

Nothing endorses working alone.

### It is in fact the opposite
Day 2's safety lecture stated plainly that *"it is advisable to **avoid working
alone** in a workshop to ensure there is someone available to assist in case of
an accident."* Option C inverts a real safety rule — the most dangerous kind of
distractor, because it sounds disciplined.

### The reasoning behind the rest
Each precaution removes a specific mechanism of injury: entanglement (clothing,
hair), impalement (unhandled tools), flying debris (goggles), electrocution
(overhead lines, water).

### Source
Prof. V. Omidiji, "Workshop Safety Precautions" slide.
"""),

    q('swep_day3_33',
      'How does Prof. Omidiji define "workforce"?',
      ['Only those currently in paid employment',
       'The total number of physically fit people in a country able to do jobs and available for work, employed and unemployed alike',
       'Graduates of technical colleges awaiting placement',
       'All citizens above the age of eighteen'],
      1,
      'Workforce is everyone physically able and available to work — employed and unemployed.',
      """
### Why this is the answer
*"Workforce is the **total number of people in a country who are able
(physically fit) to do jobs** and they are **available** for the works.
Therefore **employed and unemployed people are referred to as workforce**."*

Two conditions: **able** and **available**. Employment status is irrelevant to
membership.

### The question the lecture then poses
> *"How many are the employed of the employable?"*

That is where workshop practice enters — the gap between being counted in the
workforce and being genuinely **employable**. It is the same distinction Day 2
drew between *unemployment* and *unemployability*.

### How workshop practice closes the gap
- **Skill development and competency** — hands-on experience with manufacturing,
  design and analysis makes graduates **more employable**
- **Bridging education and employment** — workshops **simulate real-world
  workplace scenarios**
- **Addressing workforce challenges** — safety and health workshops improve
  well-being and reduce hazards
- **Fostering innovation and adaptation** — creative problem-solving and
  adaptability, including **AI workshops** preparing people for the future of work
- **Cross-functional collaboration** — broadens perspectives, enhances strategic
  thinking

### Source
Prof. V. Omidiji, "How does Workshop Practice enhance Workforce?" slides.
"""),

    q('swep_day3_34',
      'Prof. Omidiji expresses the relationship between workshop practice, workforce and national growth as two equations. What does Equation 1 state?',
      ['Workshop Practice + Workforce = National Growth',
       'Workforce + Development Plan = ½(National Growth)',
       'Workshop Practice + Development Plan = National Growth',
       'Workshop Practice + Workforce = ½(National Growth)'],
      3,
      'Equation 1: Workshop Practice + Workforce = ½(National Growth).',
      """
### Why this is the answer
The lecture states two equations:

> **Eq. 1:** Workshop Practice + Workforce = **½(National Growth)**
> **Eq. 2:** Workshop Practice + Workforce + **Development Plan** = National Growth

### What the halving is saying
Skills and people alone deliver only **half** of national growth. The missing
half is the **development plan**. As the deck puts it: *"Equation 2 tells us that
**without proper planning, national growth would wobble**."*

### The roles, stated precisely
> **Engineering (workshop practice and workforce) is the *driver* of the good
> standard of living, while the developmental plan *catalyses* it.**

Driver and catalyst — two different functions. Neither alone is sufficient.

### The definition underneath
National growth is *"the increase in a country's wealth and economic output over
time"*, spanning political, economic, social, cultural, scientific and material
spheres. Its key indicator is *"the capacity of a nation to enhance its
citizens' **standard of living**."*

### Source
Prof. V. Omidiji, "Relationship between workshop practice, workforce and
national growth" slide.
"""),

    q('swep_day3_35',
      "According to the lecture, what were Nigeria's Q1 2025 GDP growth rate and the comparative figure for Ghana?",
      ['2.27% for Nigeria and 5.4% for Ghana',
       '3.13% for Nigeria and 5.4% for Ghana',
       '3.13% for Nigeria and 2.27% for Ghana',
       '5.4% for Nigeria and 3.13% for Ghana'],
      1,
      "Nigeria's Q1 2025 GDP growth was 3.13%; Ghana's was 5.4%.",
      """
### Why this is the answer
*"Nigeria's GDP growth in **Q1 2025** was reported at **3.13%**, an increase from
the **2.27%** recorded in **Q1 2024**. The GDP of **Ghana** was reported at
**5.4%** growth."*

| Economy | Period | Growth |
|---|---|---|
| Nigeria | Q1 2024 | 2.27% |
| **Nigeria** | **Q1 2025** | **3.13%** |
| **Ghana** | — | **5.4%** |

### Three numbers, easily mixed
**2.27%** is the trap: it is Nigeria's, but from the **previous year**. The
question asks for Q1 **2025**. Option C uses it as Ghana's figure.

### The driver the lecture identifies
Asked what drove the improvement, the deck answers: *"**Reduction in petrol
imports** driven by the operation of the **Dangote Refinery**."* A
manufacturing-capacity change moving a national statistic — which is the
lecture's entire thesis about engineering and growth.

### The question posed alongside
*"Do we have enough goods and services produced within the country that would
enhance the GDP?"* — GDP being *the total value of goods and services produced
within a country*.

### Source
Prof. V. Omidiji, "Economic growth" slide.
"""),

    q('swep_day3_36',
      'Which three factors influencing national growth are named in the lecture?',
      ['Government policies, global economy and human capital',
       'Population size, land mass and natural resources',
       'Foreign aid, tourism and remittances',
       'Interest rates, inflation and exchange rates'],
      0,
      'Government policies, the global economy and human capital.',
      """
### Why this is the answer
The slide lists exactly three:

| # | Factor | How it acts |
|---|---|---|
| 1 | **Government policies** | Taxation, trade and investment can significantly impact growth |
| 2 | **Global economy** | International trade and global conditions influence the growth trajectory |
| 3 | **Human capital** | *"A **skilled and educated workforce** is essential for sustained growth"* |

### Why factor 3 is the lecture's anchor
**Human capital** is exactly what workshop practice produces. Of the three
factors, it is the only one a university can act on directly — policies belong
to government and the global economy is external. That is the argument for SWEP
itself.

### Note the qualifier
It is not *any* workforce but a **skilled and educated** one. This connects
straight back to the employability question: being in the workforce is not the
same as being employable, and only the skilled portion drives growth.

### Source
Prof. V. Omidiji, "Factors influencing national growth" slide.
"""),

    q('swep_day3_37',
      "What is the stated period of Nigeria's National Development Plan referenced in the lecture, and which long-term aspiration is it aligned with?",
      ['NDP 2021–2025, aligned with Nigeria Agenda 2050',
       'NDP 2020–2024, aligned with Vision 2020',
       'NDP 2021–2025, aligned with Vision 2030',
       'NDP 2023–2027, aligned with Nigeria Agenda 2050'],
      0,
      'NDP 2021–2025, aligned with Nigeria Agenda 2050.',
      """
### Why this is the answer
The lecture quotes the Plan directly: the vision of Nigeria's **National
Development Plan (NDP, 2021–2025)** is consistent with the socio-economic
transformation envisioned in the long-term aspiration *"encapsulated in the
**Nigeria Agenda 2050**."*

### The approach it adopts
An **integrated and multi-sectoral development approach**, recognising the
*"multi-faceted and interlinked nature of sustainable development"*, which
requires interventions tackled **simultaneously** through coordinated
implementation.

### Its four strategic objectives
1. Establishing a strong foundation for a **concentric diversified economy**
2. Investment in critical **physical, financial, science and innovation
   infrastructure**
3. Building a solid framework and capacities to **strengthen security and ensure
   good governance**
4. Enabling a **vibrant, educated and healthy populace**

### Why the plan appears in an engineering lecture
It is the **"Development Plan"** term of **Equation 2**. Without it, by the
lecture's own arithmetic, workshop practice and workforce deliver only half of
national growth.

### Source
Prof. V. Omidiji, "The development plan of Nigeria" slide.
"""),

    q('swep_day3_38',
      'Which two outcomes from the National Development Plan does the lecture highlight?',
      ['Free tertiary education and a new national minimum wage',
       'Mandatory AI training and a national apprenticeship levy',
       'Establishment of new federal polytechnics and abolition of SIWES',
       'Introduction of the TVET Programme to all Technical Colleges, and COREN regulating admissions into engineering programmes'],
      3,
      'The TVET Programme in all Technical Colleges, and COREN regulating engineering admissions.',
      """
### Why this is the answer
The deck lists two outcomes from the Plan:

1. **Introduction of the TVET Programme to all the Technical Colleges in
   Nigeria** — with **incentives promised to would-be candidates** to make the
   programme attractive
2. **COREN will now regulate admissions into our engineering programmes**

### What each one targets
| Outcome | Effect on the growth equation |
|---|---|
| **TVET** in all technical colleges | Expands the **skilled workforce** — the human-capital factor |
| **COREN** regulating admissions | Raises **quality control** at entry into engineering |

One widens the pipeline, the other guards its standard. Both act on **human
capital**, the one growth factor a university can influence.

### The conclusion drawn
> *"The **handshake** between the workshop practice and workforce to produce
> national growth cannot be over-emphasised. There must be a top relationship
> between them, revised and renewed to enhance rapid development."*

### Source
Prof. V. Omidiji, "Outcomes from the PLAN" and "Conclusion" slides.
"""),

    q('swep_day3_39',
      'According to the Day 3 orientation ledger, who delivered the lecture on Renewable Energy and PV Technology?',
      ['Prof. A. B. Ayanwale', 'Prof. V. Omidiji',
       'Dr. F. K. Ariyo', 'Prof. A. A. Adeleke'],
      2,
      'Dr. F. K. Ariyo delivered the Renewable Energy & PV Technology lecture.',
      """
### Why this is the answer
The Day 3 ledger (Wednesday, 16th September) records **Renewable Energy & PV
Technology (Dr. F. K. Ariyo)**, noting that he introduced solar energy as a
**multidisciplinary field** encompassing materials science and control
regulations, and covered the mechanics of PV cells, system design (e.g.
off-grid), energy storage, AI integration and career pathways in solar
engineering.

His title slide confirms: **Dr. F. K. Ariyo, Department of Electronic and
Electrical Engineering, Obafemi Awolowo University, Ile-Ife**.

### Day 3 at a glance
| # | Lecture | Speaker |
|---|---|---|
| 1 | Entrepreneurship in the 5G Era | Prof. A. B. Ayanwale |
| 2 | **Renewable Energy & PV Technology** | **Dr. F. K. Ariyo** |
| 3 | Workshop Practice, Workforce & National Growth | Prof. V. Omidiji |

### Note the title and the decoy
Ariyo is **Dr.**, the other two Day 3 speakers are **Prof.** And **Prof. A. A.
Adeleke** is a real SWEP lecturer — but he delivered **Day 2's** Workshop &
Industrial Safety. Speakers from adjacent days make the sharpest distractors.

### Source
Handwritten "Record of the Orientation Week Activities", Day 3; deck title slide.
"""),

    q('swep_day3_40',
      'Which Day 3 speaker is correctly matched with the department or discipline stated on their material?',
      ['Prof. A. B. Ayanwale — Department of Electronic and Electrical Engineering',
       'Dr. F. K. Ariyo — Department of Agricultural Economics',
       'Prof. V. Omidiji — PhD, REng (Mech), MNIMechE, MNIEM, MNSE',
       'Prof. A. B. Ayanwale — Department of Materials Science and Engineering'],
      2,
      'Prof. V. Omidiji is credited as PhD, REng (Mech), MNIMechE, MNIEM, MNSE.',
      """
### Why this is the answer
Each Day 3 deck carries its author's own credentials on the title slide:

| Speaker | As stated on their material |
|---|---|
| Prof. A. B. Ayanwale | Professor, **Department of Agricultural Economics**, OAU |
| Dr. F. K. Ariyo | **Department of Electronic and Electrical Engineering**, OAU |
| **Prof. V. Omidiji** | **PhD, REng (Mech), MNIMechE, MNIEM, MNSE** |

Only the Omidiji pairing is correct.

### The detail worth pausing on
The 5G entrepreneurship lecture was delivered by a professor of **Agricultural
Economics** — not an engineer. That is not an oddity; it reinforces the lecture's
own argument that a 5G venture needs **domain experts and business strategists**,
not only technical experts. The messenger demonstrates the message.

### How the distractors were built
Options A and B **swap Ayanwale's and Ariyo's departments** with each other.
Option D borrows **Materials Science and Engineering** — which is real, but it is
**Prof. A. A. Adeleke's** department from Day 2.

### Source
Title slides of all three Day 3 decks; Day 2 deck for the Materials Science
attribution.
"""),
]

assert len(QUESTIONS) == 40, f'expected 40, got {len(QUESTIONS)}'
_ids = [x['id'] for x in QUESTIONS]
assert len(set(_ids)) == 40, 'duplicate ids'
for _q in QUESTIONS:
    assert len(_q['options']) == 4, f"{_q['id']}: needs 4 options"
    assert 0 <= _q['correct'] < 4, f"{_q['id']}: bad correct index"
    assert _q['short'] and _q['solution'], f"{_q['id']}: missing short/solution"
