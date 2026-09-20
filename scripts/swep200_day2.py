#!/usr/bin/env python3
"""SWEP 200 — Day 2 question bank (45 questions).

Day 2: Tuesday, 15th September. Three lectures, per the orientation ledger:
  1. Substance Abuse Awareness            — Dr. A. Olatunji
  2. Workshop & Industrial Safety         — Prof. A. A. Adeleke
  3. 21st-Century Employability Skills    — Prof. A. B. Ekanola

SCHEMA NOTE
-----------
The supplied JSON used a different shape to the one this CBT requires. Fixed
here rather than in data.js, so regeneration stays correct:

  supplied            -> required by the app
  ------------------------------------------
  correctAnswer       -> correct
  shortReview         -> short
  detailedSolution    -> solution
  (missing)           -> kind   ('theory' | 'calc')
  (missing)           -> type   ('mcq' | 'calc' | 'text')
  id: 1..40 (ints)    -> unique strings; bare ints would have collided with
                         other banks and broken the duplicate-id check
  topicId: "SWEP_Day2_SubstanceAbuse" etc -> a single 'swep-day-2' topic, so
                         Day 2 behaves like Day 1 under the SWEP Days category

Inline [span_n](start_span) citation artifacts were stripped — they would have
rendered as literal text to students.

Every answer was verified against the Day 2 source decks before the
explanations were written:
  * SUBSTANCE ABUSE AMONG UNIVERSITY UNDERGRADUATES.pdf (13 pp.)
  * SWEP 200 - WORKSHOP AND INDUSTRY SAFETY 050825.pdf  (67 pp.)
  * OAU Employability Skills 2026.pdf                   (59 pp.)
  * Handwritten Day 2 orientation ledger (speaker attributions)

Questions 41-45 were added to reach the requested 45, drawn strictly from the
same decks and written to the Day 1 standard.
"""

TOPIC_ID = 'swep-day-2'


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
    # ===================== Substance Abuse (Dr. A. Olatunji) =====================
    q('swep_day2_01',
      'What is the estimated global average for psychoactive substance use?',
      ['5.3%', '10.2%', '14.3%', '45.0%'],
      0,
      'The global average for psychoactive substance use is 5.3%.',
      """
### Why this is the answer
The slide gives **5.3%** as the **global average** for psychoactive substance
use, and uses it as the benchmark against which Nigeria is compared.

### The comparison that matters
| Measure | Figure |
|---|---|
| **Global average** | **5.3%** |
| Nigeria (aged 15-64) | **14.3%** |

Nigeria's rate is roughly **2.7 times** the world average — that contrast is the
whole point of the opening slide, so expect both numbers to be examined.

### Source
Dr. A. Olatunji, "Introduction" slide, *Substance Abuse Among University
Undergraduates* (Medical and Health Services, OAU).

### Why the others fail
- **14.3%** — that is Nigeria's figure, not the world's. The commonest slip.
- **10.2%** — does not appear anywhere in the deck.
- **45.0%** — the lower bound of the university *lifetime prevalence* range,
  a completely different measure.
"""),

    q('swep_day2_02',
      'What percentage of the Nigerian population aged 15-64 is estimated to engage in psychoactive substance use?',
      ['5.3%', '14.3%', '25.5%', '45.0%'],
      1,
      'Approximately 14.3% of Nigerians aged 15-64 engage in psychoactive substance use.',
      """
### Why this is the answer
Around **14.4 million Nigerians** — approximately **14.3% of the population
aged 15-64** — are estimated to engage in psychoactive substance use.

### Do not confuse the two 14s
- **14.4 million** = the number of people
- **14.3%** = the share of the 15-64 age group

They sit in the same sentence and look almost identical. The question asks for a
**percentage**, so the answer is **14.3%**.

### Context
This is *notably higher* than the global average of **5.3%**, which is exactly
why the lecture opens with it.

### Source
Dr. A. Olatunji, "Introduction" slide.

### Why the others fail
- **5.3%** — the global average.
- **25.5%** — not in the material.
- **45.0%** — the floor of the 45%-84.5% university lifetime-prevalence band.
"""),

    q('swep_day2_03',
      'What is the estimated lifetime prevalence of substance use in several southwestern Nigerian universities?',
      ['10% - 25%', '25% - 40%', '45% - 84.5%', '85% - 95%'],
      2,
      'Lifetime prevalence ranges between 45% and 84.5%.',
      """
### Why this is the answer
In several **southwestern Nigerian universities**, the **lifetime prevalence**
of substance use ranges between **45% and 84.5%**.

### Why the number is so much larger than 14.3%
Two different measures are in play:
- **14.3%** is *current* use across the whole 15-64 population.
- **45%-84.5%** is *lifetime* prevalence — ever used, even once — and only
  within a university population.

Lifetime prevalence is always higher than current use, and students are a
higher-risk group. Read the wording carefully before answering.

### Most frequently abused substances
Alcohol, tobacco, **codeine-containing cough syrups**, **tramadol**, and
cannabis.

### Source
Dr. A. Olatunji, "Introduction" slide.

### Why the others fail
The three distractors are all plausible-looking bands, but the deck states one
specific range: **45%-84.5%**.
"""),

    q('swep_day2_04',
      'Which of the following is considered a physical sign of substance abuse?',
      ['Declining grades', 'Bloodshot or glassy eyes',
       'Secretive behavior', 'Social withdrawal'],
      1,
      'Bloodshot or glassy eyes are a physical sign of substance abuse.',
      """
### Why this is the answer
The deck separates the warning signs into **five distinct categories**, and this
question tests whether you can place a sign in the right one.

**Physical signs** are the bodily, visible ones:
- **Bloodshot or glassy eyes**
- Sudden weight loss or gain
- Unusual body odours (e.g. alcohol, cannabis)
- Poor hygiene and self-care
- Frequent nosebleeds or sniffing (may indicate snorting)
- Tremors, slurred speech, or unsteady gait

### Where the distractors actually belong
| Sign | Correct category |
|---|---|
| Declining grades | **Academic** |
| Secretive behaviour | **Behavioural** |
| Social withdrawal | **Psychological/Emotional** |

Every distractor is a **real** warning sign — just filed under a different
heading. That is the trap.

### Source
Dr. A. Olatunji, "Signs and Symptoms — Physical Signs" slide.
"""),

    q('swep_day2_05',
      'Which of the following describes a behavioral change commonly associated with substance abuse?',
      ['Increased impulsivity or risk-taking behaviors',
       'Frequent visits to high-risk areas',
       'Frequent absenteeism from lectures',
       'Unexplained mood swings'],
      0,
      'Increased impulsivity or risk-taking behaviour is a behavioural change indicator.',
      """
### Why this is the answer
**Behavioural changes** listed in the deck:
- Sudden change in friend groups, especially peers known for drug use
- Secretive or suspicious behaviour
- Lying, stealing, or manipulation to obtain money or substances
- **Increased impulsivity or risk-taking behaviours**
- Loss of interest in hobbies, academics, or extracurriculars
- Neglect of responsibilities (missed classes or deadlines)

### Where the distractors belong
| Sign | Correct category |
|---|---|
| Frequent visits to high-risk areas | **Social and Lifestyle** |
| Frequent absenteeism from lectures | **Academic** |
| Unexplained mood swings | **Psychological and Emotional** |

Again, all four are genuine warning signs from the same lecture — only one sits
under *Behavioural Changes*.

### Source
Dr. A. Olatunji, "Behavioral Changes" slide.
"""),

    q('swep_day2_06',
      'Hallucinations and delusions are categorized under which type of substance abuse symptom?',
      ['Physical Signs', 'Academic Signs',
       'Psychological and Emotional Symptoms', 'Social and Lifestyle Indicators'],
      2,
      'They are psychological and emotional symptoms.',
      """
### Why this is the answer
**Psychological and Emotional Symptoms** are listed as:
- Unexplained mood swings or irritability
- Anxiety, restlessness, or panic attacks
- Periods of excessive energy or agitation (may indicate **stimulant** use)
- Depression, social withdrawal, or emotional numbness
- **Hallucinations or delusions** — in severe cases, or from specific substances
  such as **cannabis or hallucinogens**

### A tempting trap
Hallucinations *feel* physical because the person may appear visibly disturbed.
But the symptom is one of **perception and cognition**, not of the body, so the
deck files it under psychological/emotional. Physical signs are things you could
photograph — eyes, weight, tremors, gait.

### Source
Dr. A. Olatunji, "Psychological and Emotional Symptoms" slide.
"""),

    q('swep_day2_07',
      'Which of the following is an academic sign of substance abuse?',
      ['Loss of interest in hobbies', 'Conflict with roommates',
       'Failure to submit assignments', 'Unusual sleeping patterns'],
      2,
      'Failure to submit assignments is an academic sign.',
      """
### Why this is the answer
**Academic signs** in the deck are exactly four:
- Frequent absenteeism from lectures and academic activities
- Declining grades and academic performance
- Disciplinary issues or warnings from faculty or administration
- **Failure to submit assignments or participate in group work**

### Where the distractors belong
| Sign | Correct category |
|---|---|
| Loss of interest in hobbies | **Behavioural** |
| Conflict with roommates | **Social and Lifestyle** |
| Unusual sleeping patterns | **Social and Lifestyle** |

Note the fine line: *loss of interest in academics* is listed under
**behavioural**, while *failure to submit assignments* is **academic**. The
distinction is between a change in attitude and a measurable academic failure.

### Source
Dr. A. Olatunji, "Academic Signs" slide.
"""),

    q('swep_day2_08',
      "Which strategy falls under 'Preventive Strategies' for substance abuse?",
      ['Medical Treatment and Rehabilitation', 'Campus-Based Drug Education',
       'Early Identification and Screening', 'Counseling and Psychological Support'],
      1,
      'Campus-Based Drug Education is a preventive strategy.',
      """
### Why this is the answer
The deck splits the response into **two numbered groups**, and every distractor
here comes from the *other* group.

**1. Preventive Strategies** — stop it before it starts:
- **Campus-Based Drug Education**
- Life Skills and Coping Mechanisms
- Peer Support Networks
- Restricting Access to Substances
- Parental and Community Involvement

**2. Intervention Strategies** — respond once it has started:
- Early Identification and Screening
- Counselling and Psychological Support
- Medical Treatment and Rehabilitation
- Policy and Disciplinary Framework
- Digital and Media Campaigns

### The rule of thumb
**Prevention comes before the problem; intervention comes after it.** Screening,
counselling and rehabilitation all presuppose that use has already begun.

### Source
Dr. A. Olatunji, "Prevention and Intervention Strategies" slides.
"""),

    q('swep_day2_09',
      'The National Drug Law Enforcement Agency (NDLEA) is involved in which substance abuse strategy?',
      ['Academic penalty execution', 'Multi-Sectoral Collaboration',
       'Life Skills Assessment', 'Parental Involvement'],
      1,
      'The NDLEA is a key part of multi-sectoral collaboration.',
      """
### Why this is the answer
**Multi-Sectoral Collaboration** is its own heading, listing the four bodies
that must work together:
- **National Drug Law Enforcement Agency (NDLEA)**
- Federal Ministry of Health
- Non-Governmental Organizations (NGOs)
- Campus health services

### Why "multi-sectoral"
Each body covers a sector the others cannot: the NDLEA brings **law
enforcement**, the Ministry of Health brings **public health policy**, NGOs
bring **community reach**, and campus health services bring **direct student
access**. No single one can address substance abuse alone.

### Source
Dr. A. Olatunji, "Multi-Sectoral Collaboration" slide.

### Why the others fail
Life Skills and Parental Involvement are **preventive strategies**, not
collaboration partners, and "academic penalty execution" is not in the deck at
all — disciplinary work appears as *Policy and Disciplinary Framework* under
intervention.
"""),

    q('swep_day2_10',
      'Who delivered the orientation session on Substance Abuse Awareness?',
      ['Prof. A. A. Adeleke', 'Prof. A. B. Ekanola',
       'Dr. A. Olatunji', 'The NDLEA Chairman'],
      2,
      'Dr. A. Olatunji delivered the session on Substance Abuse Awareness.',
      """
### Why this is the answer
The Day 2 ledger (Tuesday, 15th September) records **Substance Abuse Awareness
(Dr. A. Olatunji)**, noting that he addressed the statistical prevalence of
psychoactive substance use, particularly within Nigerian universities, while
outlining signs, consequences, preventative intervention strategies and coping
skills.

### Day 2 at a glance
| # | Lecture | Speaker |
|---|---|---|
| 1 | Substance Abuse Awareness | **Dr. A. Olatunji** |
| 2 | Workshop & Industrial Safety | Prof. A. A. Adeleke |
| 3 | 21st-Century Employability Skills | Prof. A. B. Ekanola |

### Note the title
He is **Dr.**, while the other two Day 2 speakers are **Prof.** Titles are
examinable — read them as carefully as the names.

### Source
Handwritten "Record of the Orientation Week Activities", Day 2; deck attributed
to Medical and Health Services, OAU.
"""),

    # ===================== Workshop & Industrial Safety (Prof. A. A. Adeleke) ====
    q('swep_day2_11',
      'How many fatal occupational injuries were recorded in the US in 2022?',
      ['2,500', '4,205', '5,486', '8,902'],
      2,
      'The US recorded 5,486 fatal occupational injuries in 2022.',
      """
### Why this is the answer
In **2022** the United States recorded **5,486 fatal occupational injuries** —
a **5.7% increase** on 2021.

### The two numbers to hold together
- **5,486** — the fatality count
- **5.7%** — the year-on-year rise

They sit in the same sentence and the digits are similar, so it is easy to swap
them under exam pressure.

### Why the lecture opens here
The trend is uneven: overall fatal-injury rates are falling in many countries
thanks to safety interventions, **but rising among migrants and ethnic
minorities in high-risk industries**. Safety is improving on average and getting
worse for the most exposed groups.

### Source
Prof. A. A. Adeleke, "USA Statistics on Industry Injuries" slide.
"""),

    q('swep_day2_12',
      'What percentage of workers globally face workplace hazards according to WHO estimates?',
      ['5-10%', '10-20%', '20-50%', '50-70%'],
      2,
      'The WHO estimates 20-50% of workers face workplace hazards globally.',
      """
### Why this is the answer
Globally, the **World Health Organization (WHO)** estimates that between
**20% and 50%** of workers face workplace hazards — with **developing countries
potentially having higher exposure**, which is precisely why this matters for
Nigerian trainees.

### Keep the three agencies apart
| Body | What it supplies in this lecture |
|---|---|
| **WHO** | **20-50%** of workers face hazards |
| **ILO** | Economic cost: **1.8%-6% of GDP** |
| US BLS figures | **5,486** fatalities in 2022 |

Mixing up which organisation produced which statistic is the likeliest error.

### Source
Prof. A. A. Adeleke, "USA Statistics on Industry Injuries" slide.
"""),

    q('swep_day2_13',
      'The ILO estimates that the economic costs of work-related injuries and diseases range from:',
      ['0.5% to 1.5% of GDP', '1.8% to 6% of GDP',
       '5% to 10% of GDP', '10% to 15% of GDP'],
      1,
      'The economic costs range from 1.8% to 6% of GDP.',
      """
### Why this is the answer
The **International Labour Organization (ILO)** and other studies estimate the
economic cost of work-related injuries and diseases at **1.8% to 6% of GDP**.

### Why express it as GDP
Framing safety as a share of **national output** makes the point that workplace
injury is not only a human tragedy but a macroeconomic drain: lost productivity,
medical costs, compensation and retraining. At the top of the range, **6% of
GDP** is a very large slice of a national economy.

### Source
Prof. A. A. Adeleke, "USA Statistics on Industry Injuries" slide.

### Why the others fail
All three are plausible-sounding economic bands, but the deck names one
specific range: **1.8% to 6%**. Note the precision of the lower bound — 1.8%,
not 2%.
"""),

    q('swep_day2_14',
      'Which of the following is NOT listed as a high-risk industry?',
      ['Construction', 'Agriculture', 'Software Development', 'Transportation'],
      2,
      'Software Development is not listed as a high-risk industry.',
      """
### Why this is the answer
This is a **NOT** question — find the one that does not belong.

The high-risk industries named are **construction, healthcare, manufacturing,
transportation and agriculture**, plus **iron and steel**, the **chemical and
petrochemical** industry, and work involving **heavy equipment and machine
operation**. **Software development** appears nowhere.

### Why the others are high-risk
| Industry | Principal hazards |
|---|---|
| **Construction** | Working at heights, falls, crush injuries, hazardous materials |
| **Agriculture** | Machinery, livestock handling, pesticide exposure |
| **Transportation** | Traffic accidents, long shifts, musculoskeletal injury from loading |

The common thread is **physical** exposure — machinery, heights, chemicals,
vehicles. Software work carries ergonomic risk, but it is not in this lecture's
list.

### Source
Prof. A. A. Adeleke, "High Risk Industries" slides.
"""),

    q('swep_day2_15',
      'What is the primary standard for safety glasses for industrial use in the United States?',
      ['EN 166', 'EN ISO 20471', 'ANSI Z87.1', 'EN ISO 11611'],
      2,
      'ANSI Z87.1 is the primary standard in the US.',
      """
### Why this is the answer
The primary standard for industrial safety glasses in the **US** is
**ANSI Z87.1**; in **Europe** the equivalent is **EN 166**.

### The quick way to tell them apart
**EN = European Norm.** Any code starting "EN" is European, so the only
non-EN option must be the American one. That single rule answers this question
even if you cannot recall the number.

### The four standards in this lecture
| Standard | Covers | Region |
|---|---|---|
| **ANSI Z87.1** | Safety glasses | **US** |
| EN 166 | Safety glasses | Europe |
| EN ISO 20471 | High-visibility clothing | Europe |
| EN ISO 11611 | Welding protection | Europe |

These standards ensure glasses withstand impacts, give clear vision, and protect
against dust, debris and chemical splashes.

### Source
Prof. A. A. Adeleke, "Personal Protective Equipment — Safety Glasses" slide.
"""),

    q('swep_day2_16',
      'Which standard dictates the minimum requirements for high-visibility clothing?',
      ['EN 166', 'EN ISO 20471', 'ANSI Z87.1', 'EN ISO 11611'],
      1,
      'EN ISO 20471 is the standard for high-visibility clothing.',
      """
### Why this is the answer
Protective-clothing standards named in the deck are **EN ISO 20471 for
high-visibility clothing** and **EN ISO 11611 for welding protection**. These
dictate the minimum requirements for **materials, design and performance**.

### Do not confuse the two EN ISO codes
| Standard | Protects against |
|---|---|
| **EN ISO 20471** | Being **unseen** — high-visibility clothing |
| EN ISO 11611 | **Welding** — heat, flame, spatter |

A memory hook: **20471 → 20/20 vision → being seen**.

### Why compliance matters
It minimises risk from chemicals, heat, flames and impacts. On a site with
moving vehicles or forklifts, visibility *is* the control measure.

### Source
Prof. A. A. Adeleke, "Personal Protective Equipment (cntd.)" slide.
"""),

    q('swep_day2_17',
      'What is considered the most effective control measure for industrial hazards?',
      ['Substitution', 'Personal Protective Equipment (PPE)',
       'Elimination', 'Administrative Controls'],
      2,
      'Elimination is the most effective control measure.',
      """
### Why this is the answer
**Completely removing the hazard from the workplace** — **Elimination** — is
stated to be **the most effective control measure**. If the hazard is not there,
it cannot hurt anyone; every other measure only *manages* a hazard that still
exists.

### The hierarchy, most to least effective
| Rank | Control | What it does |
|---|---|---|
| 1 | **Elimination** | Removes the hazard entirely |
| 2 | Substitution | Replaces it with something safer |
| 3 | Engineering controls | Machine guarding, ventilation, noise reduction |
| 4 | Administrative controls | Procedures, policies, training |
| 5 | **PPE** | Protects the individual person |

### Why PPE ranks last
PPE is the **last line of defence**. It does nothing to the hazard itself — it
only stands between the hazard and one worker, and it fails the moment it is
worn incorrectly, removed, or damaged. It is the most visible control, which is
why students wrongly assume it is the strongest.

### Source
Prof. A. A. Adeleke, "Control Measures" slide.
"""),

    q('swep_day2_18',
      'Establishing procedures, policies, and training to minimize exposure to hazards is an example of:',
      ['Engineering Controls', 'Administrative Controls',
       'Substitution', 'Housekeeping'],
      1,
      'This defines Administrative Controls.',
      """
### Why this is the answer
**Administrative Controls** are defined as *establishing procedures, policies
and training to minimise exposure to hazards* — for example, training employees
on safe machine operation.

### Administrative vs engineering — the key distinction
- **Engineering controls change the workplace.** Machine guarding, ventilation
  systems, noise reduction. They work whether or not anyone remembers them.
- **Administrative controls change behaviour.** Procedures, rotas, training,
  signage. They depend on people following them.

That is why engineering ranks **above** administrative in the hierarchy.

### The lecture's own worked example
In a manufacturing setting: **machine guarding** (engineering) prevents
accidental contact with moving parts; **training on safe operation**
(administrative) and **safety glasses** (PPE) further enhance protection. One
scenario, three layers.

### Source
Prof. A. A. Adeleke, "Control Measures (cntd.)" slide.
"""),

    q('swep_day2_19',
      'Which safety sign is typically circular with a red border and a red diagonal line through the symbol?',
      ['Warning Signs', 'Mandatory Signs', 'Emergency Signs', 'Prohibition Signs'],
      3,
      'Prohibition signs feature a red border and a red diagonal line.',
      """
### Why this is the answer
**Prohibition signs** indicate actions that are **not permitted**. They are
**circular with a red border, a red diagonal line through the symbol**, and a
**black pictogram on a white background** — for example "No Smoking", "No
Entry", "Do Not Touch", "No Parking".

### The four sign families — learn shape + colour together
| Type | Shape | Colour | Means |
|---|---|---|---|
| **Prohibition** | **Circular** | **Red border + diagonal** | Must **NOT** do |
| Warning | Triangular | Yellow/amber, black border | **Be careful** |
| Mandatory | Circular | **Blue** background, white symbol | **Must** do |
| Emergency/First-aid | Rectangular/square | **Green** background | **Safety/escape** |

### The trap in this question
Prohibition and mandatory signs are **both circular**. Colour is what separates
them: **red = don't, blue = do**. Shape alone is not enough.

### Source
Prof. A. A. Adeleke, "Signage" and "Prohibition Sign" slides.
"""),

    q('swep_day2_20',
      'What do Warning Signs typically look like?',
      ['Triangular with a yellow or amber background',
       'Circular with a blue background',
       'Rectangular with a green background',
       'Circular with a red border'],
      0,
      'Warning signs are triangular with a yellow or amber background.',
      """
### Why this is the answer
**Warning signs** alert people to potential hazards that may not be immediately
apparent. They are **triangular, with a yellow or amber background, a black
border and a black pictogram** — for example "High Voltage", "Slippery
Surface", "Falling Objects", "Flammable Material", "Caution: Forklift Traffic".

### Every distractor is a real sign type
| Description | Actual type |
|---|---|
| Circular, blue background | **Mandatory** ("Wear Hard Hat") |
| Rectangular, green background | **Emergency / First-aid** ("Fire Exit") |
| Circular, red border | **Prohibition** ("No Smoking") |

So this question is really asking whether you can map **shape + colour → meaning**
for all four families, not just one.

### Memory hook
**Triangle = think.** A triangle points upward like an alert; yellow is the
universal caution colour.

### Source
Prof. A. A. Adeleke, "Warning Signs" slides.
"""),

    q('swep_day2_21',
      'What is the color code for a Water Fire Extinguisher, suitable for Class A fires?',
      ['Red with a black square', 'Red with a green triangle',
       'Red with a cream-colored label', 'Red with a blue circle'],
      1,
      'Water extinguishers are red with a green triangle.',
      """
### Why this is the answer
**All** extinguisher bodies are red in this scheme — the **colour-coded band or
label** is what identifies the type. **Water extinguishers are red with a green
triangle**, for **Class A** fires (wood, paper and similar solids).

### The full colour code
| Type | Marking | Fire classes |
|---|---|---|
| **Water** | **Green triangle** | **A** |
| CO2 | Black square | B and C |
| Foam | Cream label | A and B |
| Dry powder | Blue circle | A, B and C |

### The critical safety point
Water is **electrically conductive**, so a water extinguisher must **never** be
used on an electrical fire — it can conduct current straight back to the
operator. That single fact is worth more than the colour code itself.

### Source
Prof. A. A. Adeleke, "Fire Extinguisher Signs" slides.
"""),

    q('swep_day2_22',
      'A Dry Powder fire extinguisher is identified by:',
      ['A black square', 'A green triangle', 'A cream-colored label', 'A blue circle'],
      3,
      'Dry powder extinguishers have a blue circle.',
      """
### Why this is the answer
**Dry powder extinguishers are red with a blue circle** and can be used on
**Class A, B and C** fires — the widest coverage of the four types listed.

### Why it covers the most classes
Dry powder smothers solids (A), flammable liquids (B) and flammable gases (C),
which is why it is often the default choice in a mixed workshop where you cannot
predict what will burn.

### Cross-check the whole set
| Marking | Type | Classes |
|---|---|---|
| Green triangle | Water | A |
| Black square | CO2 | B, C |
| Cream label | Foam | A, B |
| **Blue circle** | **Dry powder** | **A, B, C** |

Each distractor here is a genuine marking belonging to a different extinguisher,
so the shapes and colours must be learned as pairs.

### Source
Prof. A. A. Adeleke, "Fire Extinguisher Signs" slide.
"""),

    q('swep_day2_23',
      'Which symbol is used to visually communicate the need for protection against radiation?',
      ['A white cross', 'A skull and crossbones', 'A trefoil', 'A stylized flame'],
      2,
      'The trefoil is the universal radiation symbol.',
      """
### Why this is the answer
Radioactive signs feature the **universal radiation symbol**, known as the
**trefoil** — a propeller-like image of **three blades pointing to the centre**,
black or magenta on a **yellow** background.

### Where you meet it
Nuclear power plants, medical facilities, research laboratories and industrial
settings. In nuclear plants the trefoil also appears alongside a figure of a
worker in a full-body suit with a respirator, marking the PPE required.

### What the other symbols mean
| Symbol | Meaning |
|---|---|
| White cross on green | **First aid** |
| Skull and crossbones | **Toxic / poison** |
| Stylised flame | **Flammable** |

All three are real safety symbols from the same lecture — just for different
hazards.

### Source
Prof. A. A. Adeleke, "Radioactive Signs" and nuclear PPE slides.
"""),

    q('swep_day2_24',
      'In Nigeria, which of the following is a key association for industrial safety?',
      ['OSHA', 'NIOSH', 'ISPON', 'ANSI'],
      2,
      'The Institute of Safety Professionals of Nigeria (ISPON) is a key association.',
      """
### Why this is the answer
The deck devotes separate slides to the **US** and to **Nigeria**, and this
question checks that you did not merge them.

**Nigeria:**
- National Industrial Safety Council of Nigeria (**NISCN**)
- **Institute of Safety Professionals of Nigeria (ISPON)**
- Occupational Safety and Health Association (**OSHAssociation**)
- Plus **MAN** and **NACCIMA**, which provide resources and training

**United States:**
- **OSHA** — Occupational Safety and Health *Administration*; a federal agency
  that **enforces** safety legislation
- **NIOSH** — a **research** agency that develops and recommends standards

### The deliberate trap
Nigeria's **OSHAssociation** looks almost identical to America's **OSHA**. They
are different bodies, and only one of them appears on the Nigeria slide. **ANSI**
is the US standards body behind ANSI Z87.1.

### Source
Prof. A. A. Adeleke, "Associations for Industrial Safety — USA / Nigeria" slides.
"""),

    q('swep_day2_25',
      'Who delivered the presentation on Workshop and Industrial Safety?',
      ['Dr. A. Olatunji', 'Prof. A. A. Adeleke',
       'Prof. A. B. Ekanola', 'The Dean of Engineering'],
      1,
      'Prof. A. A. Adeleke delivered the presentation on Workshop and Industrial Safety.',
      """
### Why this is the answer
The Day 2 ledger records **Workshop & Industrial Safety (Prof. A. A. Adeleke)**,
noting that he examined fatal workplace injury statistics and engineering
workshop protocols, highlighting high-risk industries, proper use of PPE, common
hazard control measures, and safety signage / first aid.

The title slide confirms it: **A. A. Adeleke, Department of Materials Science
and Engineering**.

### Day 2 speakers
| Lecture | Speaker |
|---|---|
| Substance Abuse Awareness | Dr. A. Olatunji |
| **Workshop & Industrial Safety** | **Prof. A. A. Adeleke** |
| 21st-Century Employability Skills | Prof. A. B. Ekanola |

Note the shared initial "A." across all three names — match the **surname**, not
the initial.

### Source
Handwritten Day 2 ledger; deck title slide.
"""),

    # ===================== Employability (Prof. A. B. Ekanola) ==================
    q('swep_day2_26',
      'According to the orientation presentation, employability is defined as the capability to:',
      ['Memorize and recall facts for examinations',
       'Obtain, retain, perform, and progress in employment',
       'Manage large teams immediately after graduation',
       'Write advanced code without errors'],
      1,
      'Employability is about obtaining, retaining, performing and progressing in employment.',
      """
### Why this is the answer
Employability is **"having the capabilities required to obtain, retain, perform
and progress in employment."** Four verbs, and all four matter — getting the job
is only the first of them.

### The sharpest line in the lecture
> A person may be **employed today but have limited employability** if their
> skills are becoming obsolete.

Employment is your status right now; employability is your capacity to keep
earning as the world changes. They are not the same thing.

### What it involves in practice
Entering the labour market, performing effectively, adapting to organisational
and technological change, learning new skills, moving between occupations,
creating employment opportunities, pursuing entrepreneurship, and continuing to
develop throughout a career.

### Source
Prof. A. B. Ekanola, "Employability" slide.
"""),

    q('swep_day2_27',
      'Which of the following is NOT an agent of global transformation mentioned in the materials?',
      ['Artificial intelligence', 'Digital platforms',
       'Analog transcription', 'Remote work'],
      2,
      'Analog transcription was not mentioned as an agent of global transformation.',
      """
### Why this is the answer
A **NOT** question. The five agents of global transformation listed are:

1. Artificial intelligence
2. Automation
3. Digital platforms
4. Globalisation
5. Remote work

**Analog transcription** does not appear — and it is conceptually the opposite
of the list, which is entirely about **digital** transformation.

### The point of the slide
Technology is transforming **virtually every sector of the economy**. That is
the premise the whole lecture builds on: if the economy is changing this fast,
a fixed set of skills cannot carry a whole career.

### Source
Prof. A. B. Ekanola, "The global reality today" slide.
"""),

    q('swep_day2_28',
      'How many clusters of 21st-century employability skills were identified?',
      ['5', '6', '8', '10'],
      2,
      'There are 8 clusters of 21st-century employability skills.',
      """
### Why this is the answer
The lecture identifies **8 clusters**:

1. Communication and interpersonal skills
2. Critical thinking and problem-solving skills
3. Digital and technological skills
4. Creativity and innovation skills
5. Collaboration and teamwork
6. Personal effectiveness and emotional intelligence
7. Career management, entrepreneurship and leadership
8. Adaptability, lifelong learning and professional development

### Don't confuse it with the other list
The same lecture also gives **five** things to develop alongside your degree:
a strong communication ability, a digital capability, evidence of practical
experience, a professional network, and a learning habit.

**8 clusters of skills; 5 things to build.** Two different numbers, two
different slides.

### Source
Prof. A. B. Ekanola, "What are the 21st-century employability skills: 8
clusters" slide.
"""),

    q('swep_day2_29',
      'What is considered perhaps the most fundamental employability skill?',
      ['Digital programming', 'Communication skills',
       'Financial accounting', 'Data science'],
      1,
      'Communication skills are considered the most fundamental employability skill.',
      """
### Why this is the answer
The slide says it plainly: *"Perhaps the most fundamental employability skill is
**communication**."* It is also cluster **number 1** of the eight.

### What communication covers here
Oral and written communication; presentation skills and listening; negotiation
and interpersonal communication; professional correspondence and digital
communication; and the ability to **communicate ideas to different audiences**.

The expanded list adds: listening, non-verbal communication, clarity and
concision, friendliness, confidence, empathy, open-mindedness, respect,
feedback, and picking the right medium.

### The warning attached
> A highly intelligent person who cannot communicate effectively **may struggle
> in the workplace**.

Note the parallel with teamwork: *"A brilliant individual who cannot work with
others can become an organisational liability."* Technical brilliance alone is
not enough — that is the lecture's recurring theme.

### How it is acquired
**Through practice**: speak and write, present and debate, teach, join
professional organisations, write reports, ask for feedback, and record yourself
speaking to review your performance.

### Source
Prof. A. B. Ekanola, "Communication skills" slides.
"""),

    q('swep_day2_30',
      'What is the first step in the critical thinking process model provided?',
      ['Present your solution', 'Research',
       'Identify the problem/issue', 'Ask questions'],
      2,
      'The first step is to identify the problem/issue.',
      """
### Why this is the answer
The critical-thinking process runs in a fixed order:

1. **Identify the problem/issue**
2. Research
3. Determine data relevance
4. Ask questions
5. Identify the best solution
6. Present your solution
7. Analyse your decision

Every distractor is a genuine step — just not the first one. The question tests
the **sequence**, not the content.

### Why identification must come first
Researching before you know what the problem actually is wastes the effort. The
problem-solving slide makes the same point: the first capability is
**"identifying the real problem"** — the *real* one, not the presenting symptom.

### What critical thinking is for
Analysing information objectively, evaluating evidence, identifying assumptions,
and reaching reasoned conclusions. It is developed by reading widely, comparing
perspectives, debating, tackling problems with no obvious answer — and
**learning to change your mind when better evidence appears**.

### Source
Prof. A. B. Ekanola, "Critical Thinking" slides.
"""),

    q('swep_day2_31',
      'What is the recommended approach to Artificial Intelligence for a future worker?',
      ['Compete directly with AI algorithms',
       'Become a professional who can work intelligently with AI',
       'Refuse to use AI to preserve authentic work',
       'Delegate all routine tasks blindly to AI'],
      1,
      'The goal is to become an AI-enabled professional.',
      """
### Why this is the answer
The slide is explicit: *"The goal should **not** be to compete with AI. It
should be to become a professional who can work **intelligently with** AI."*

> The future may belong more to **"AI-enabled professionals"** rather than
> simply "AI specialists".

### What AI literacy requires
Understanding what AI **can and cannot** do; its limitations; how to formulate
effective instructions; how to **evaluate AI-generated outputs**; and issues of
bias, privacy, intellectual property and ethical use.

### Why the other two extremes both fail
- **Refusing to use AI** leaves you behind in an economy being transformed by it.
- **Delegating blindly** ignores the closing instruction: *"The ability to use AI
  effectively must be combined with **human judgement**."*

The recommended position sits between refusal and blind trust — capable use with
judgement retained.

### Source
Prof. A. B. Ekanola, "Artificial Intelligence Literacy" and "Note" slides.
"""),

    q('swep_day2_32',
      'How does innovation differ from creativity?',
      ['Creativity involves risk, while innovation does not',
       'Innovation converts creative ideas into useful outcomes',
       'Creativity requires funding, while innovation is free',
       'There is no difference; they are synonymous'],
      1,
      'Innovation converts ideas into useful outcomes.',
      """
### Why this is the answer
- **Creativity** involves *seeing possibilities that others may not see*.
- **Innovation** takes creativity *a step further by **converting ideas into
  useful outcomes***.

Creativity generates the idea; innovation delivers the result. An idea that
never becomes anything is creativity without innovation.

### How the lecture says to build both
Ask unconventional questions and attend to details; learn to analyse; stay
open-minded; solve problems; **don't be afraid of failure**; assess and negate
risks; seek to do more or better with less.

To develop creativity: expose yourself to different disciplines, read outside
your field, travel, talk to people with different perspectives, experiment.

> Innovation often begins with the question: **"Is there a better way of doing
> this?"**

### Source
Prof. A. B. Ekanola, "Creativity and Innovation" slides.
"""),

    q('swep_day2_33',
      'Which of the following is a component of Emotional Intelligence?',
      ['Self-regulation', 'Software development',
       'Statistical analysis', 'Project management'],
      0,
      'Self-regulation is a component of Emotional Intelligence.',
      """
### Why this is the answer
Emotional Intelligence involves understanding one's own emotions and recognising
and appropriately responding to the emotions of others. Its components are:

- Self-awareness
- **Self-regulation**
- Empathy
- Social awareness
- Relationship management

(The expanded slide adds **internal motivation**.)

### Why the distractors cannot qualify
Software development, statistical analysis and project management are all
**technical or functional** skills. EI belongs to cluster 6 — *personal
effectiveness and emotional intelligence* — which is about managing yourself and
your relationships, not performing a technical task.

### Why it still matters in an automated world
> Technology may automate many processes, but **human relationships remain
> fundamental**.

Developed by: practising active listening, receiving criticism without becoming
defensive, reflecting on your behaviour, developing empathy, managing anger
professionally, and seeking honest feedback.

### Source
Prof. A. B. Ekanola, "Emotional Intelligence" slides.
"""),

    q('swep_day2_34',
      'The ability to recover from setbacks and continue moving forward is defined as:',
      ['Innovation', 'Adaptability', 'Resilience', 'Networking'],
      2,
      'This defines Resilience.',
      """
### Why this is the answer
**Resilience** is *"the ability to recover from setbacks and continue moving
forward."*

It is needed because *"a career will contain **rejection, failure, redundancy,
organisational change and uncertainty**"* — so employability requires
**psychological and professional resilience**, not only technical skill.

### Resilience vs adaptability — the distinction being tested
They appear on neighbouring slides and are easily confused:

| Term | Definition |
|---|---|
| **Adaptability** | Functioning effectively **in the face of change** |
| **Resilience** | **Recovering** from setbacks and carrying on |

Adaptability is about **adjusting**; resilience is about **bouncing back**. One
handles change, the other handles failure.

### The premise underneath both
> If there is one certainty about the future of work, it is **change**.

### Source
Prof. A. B. Ekanola, "Adaptability and Resilience" slides.
"""),

    q('swep_day2_35',
      'What is one of the best ways to acquire employability skills by converting knowledge into competence?',
      ['Experiential learning', 'Memorization',
       'Listening to lectures', 'Avoiding extracurricular activities'],
      0,
      'Experiential learning converts knowledge into competence.',
      """
### Why this is the answer
The slide closes with the line this question is built on:
**"Experience converts knowledge into competence."**

**Experiential learning** includes internships and industrial attachments,
apprenticeships, volunteering, community and research projects, part-time work,
student leadership, and entrepreneurial activities.

### Why this lands in a SWEP lecture
SWEP 200 **is** experiential learning — a workshop attachment, not a classroom.
The lecture is explaining why the programme you are sitting in exists.

### The direct criticism of passive study
> Students should **not simply listen to lectures and reproduce information in
> examinations**. The classroom must increasingly become a place where students
> **do, not merely listen**.

That is why "memorization" and "listening to lectures" are wrong here — the
lecture explicitly argues against both as sufficient.

### Source
Prof. A. B. Ekanola, "Experiential Learning" and "Formal Education" slides.
"""),

    q('swep_day2_36',
      "What is the primary difference between a 'skill' and a 'capability'?",
      ['A skill requires a degree; a capability does not',
       'A capability is the ability to apply knowledge and skills in changing circumstances',
       'A capability is a physical trait, while a skill is mental',
       'Skills are permanent, while capabilities are temporary'],
      1,
      'A capability is the ability to adapt skills to changing circumstances.',
      """
### Why this is the answer
- A **skill** is the ability to **perform a particular task**.
- A **capability** is the ability to **apply knowledge and skills effectively in
  changing circumstances**.

### The lecture's own example
> Knowing how to use a **particular software package** is a **skill**.
> Being able to **learn new software when the technology changes** is a
> **capability**.

### Why the distinction carries the whole argument
Skills go obsolete; capabilities do not. It is exactly why *"a person may be
employed today but have limited employability if their skills are becoming
obsolete"* — they have the skill but not the capability.

This is also why the closing slide says the future is not about producing people
who **know everything**, but people who can **learn anything they need to know**.

Note the last distractor inverts the truth: skills are the *perishable* ones.

### Source
Prof. A. B. Ekanola, "From Skills to Capabilities" slide.
"""),

    q('swep_day2_37',
      'According to the presentation, why is a portfolio superior to a standard CV?',
      ['It is cheaper to produce',
       'It demonstrates what you can do, rather than just claiming it',
       'It forces employers to read more text',
       'It is required by law'],
      1,
      'A portfolio demonstrates evidence of your claims.',
      """
### Why this is the answer
The slide states the contrast directly:
> **A CV tells an employer what you claim you can do. A portfolio can
> demonstrate it.**

A CV is an assertion; a portfolio is **evidence**.

### What a graduate's portfolio should contain
Research projects; presentations; software projects; designs; business ideas;
community projects; certificates; professional achievements; and **evidence of
impact**.

### The connected idea
> Employability is not only about **what you know** but also about **who knows
> what you can do**.

A portfolio is how you make your capability visible to people who have never met
you — which is also why networking sits in the same cluster.

### Source
Prof. A. B. Ekanola, "Building a Portfolio" and "Networking" slides.
"""),

    q('swep_day2_38',
      'Who presented the session on 21st-Century Employability Skills?',
      ['Prof. A. A. Adeleke', 'Dr. A. Olatunji',
       'Prof. A. B. Ekanola', 'The Vice Chancellor'],
      2,
      'Prof. A. B. Ekanola presented the session.',
      """
### Why this is the answer
The Day 2 ledger records **21st-Century Employability Skills (Prof. A. B.
Ekanola)**, noting that he explored global technological transformations (like
AI) and **the gap between unemployment and unemployability**, emphasising core
traits needed to secure and advance in employment — adaptability, communication,
ethical awareness and lifelong learning.

The title slide confirms: *"21st-Century Employability Skills: What They Are and
How Best to Acquire Them — 15 Sept 2026, Prof. A. B. Ekanola"*, delivered under
**ACCESS** (African Center for Career Enhancement and Skills Support).

### Watch the initials
Prof. A. **A.** Adeleke and Prof. A. **B.** Ekanola differ by a single middle
initial. Match surnames to subjects: **Adeleke → Safety**, **Ekanola →
Employability**.

### Source
Handwritten Day 2 ledger; deck title slide.
"""),

    q('swep_day2_39',
      "Instead of the traditional 'Degree → employment → retirement' path, what model is suggested for modern careers?",
      ['Degree → permanent employment',
       'Degree → work → transition → reskill → work → upskill',
       'Retirement → degree → work',
       'Work → retirement → degree'],
      1,
      'The modern career path requires continuous reskilling and upskilling.',
      """
### Why this is the answer
The lecture contrasts the old and new models directly:

**Instead of:** Degree → employment → retirement
**We move towards:** Degree → work → reskill → work → upskill → career
transition → **lifelong learning**

The defining feature is that learning **recurs** — it is no longer a single
block at the start of life.

### What makes it possible
**Micro-credentials, professional certificates and short courses.** Traditional
degrees remain important, but should be **complemented** by shorter forms of
learning that build specific competencies quickly.

### Reskill vs upskill
- **Reskill** — learn something new to move into a *different* role
- **Upskill** — deepen what you already do

### Source
Prof. A. B. Ekanola, "Micro-credentials and Short Courses" slide.
"""),

    q('swep_day2_40',
      'What is the ultimate message regarding the future of employability?',
      ['You must know everything before graduating',
       'Degrees alone guarantee a stable career',
       'You must be a lifelong learner who can learn anything needed',
       'Soft skills are no longer necessary due to AI'],
      2,
      'The future of employability relies on being a lifelong learner.',
      """
### Why this is the answer
The closing slide states that the future of employability is:
- **not** about producing people who know everything — *"That is impossible"*
- **about** producing people who **can learn anything they need to know**
- about becoming digitally capable, intellectually curious, emotionally
  intelligent, ethically responsible, entrepreneurial, collaborative, creative
  and adaptable
- **above all: be a lifelong learner**

### Why each distractor is explicitly contradicted
| Claim | The lecture's position |
|---|---|
| Know everything before graduating | Called **impossible** outright |
| Degrees guarantee a career | *"Your degree is the **beginning** of your professional learning"* |
| AI removes the need for soft skills | *"Human relationships remain fundamental"*; the goal is to work **with** AI |

### The challenge to students
> At all times, consciously and purposively develop soft, digital and technical
> skills. **There should be at least one you are working on at any point in
> time.**

### Source
Prof. A. B. Ekanola, "The Future of Employability is" and "Special Message"
slides.
"""),

    # ============ Added to reach 45 — same decks, same standard ============
    q('swep_day2_41',
      'According to the substance abuse lecture, which substances are listed among the most frequently abused in southwestern Nigerian universities?',
      ['Alcohol, tobacco, codeine-containing cough syrups, tramadol and cannabis',
       'Heroin, cocaine, methamphetamine and LSD',
       'Caffeine, energy drinks, nicotine patches and painkillers',
       'Alcohol, steroids, inhalants and barbiturates'],
      0,
      'Alcohol, tobacco, codeine cough syrups, tramadol and cannabis are the most frequently abused.',
      """
### Why this is the answer
The lecture names five substances as the most frequently abused in the
southwestern Nigerian university context: **alcohol, tobacco,
codeine-containing cough syrups, tramadol, and cannabis**.

### What the list tells you
Three of the five — **alcohol, codeine syrup and tramadol** — are **legally
available** products, not street narcotics. That is the uncomfortable point: the
substances driving the **45%-84.5%** lifetime prevalence figure are largely ones
students can obtain over a counter, which is exactly why *"Restricting Access to
Substances"* appears as a **preventive strategy**.

### A supporting clue elsewhere in the deck
Cannabis is singled out again under psychological symptoms as a substance that
can produce **hallucinations or delusions**.

### Source
Dr. A. Olatunji, "Introduction" slide.

### Why the others fail
The alternatives list plausible drugs of abuse, but the hard drugs in options B
and D and the stimulants in option C are not the ones this lecture names.
"""),

    q('swep_day2_42',
      'Under the risks and consequences of substance abuse, which of the following categories was NOT listed?',
      ['Health Risks', 'Academic Consequences',
       'Environmental Degradation Consequences', 'Legal and Financial Consequences'],
      2,
      'Environmental degradation is not one of the listed consequence categories.',
      """
### Why this is the answer
A **NOT** question. The deck lists exactly **five** categories of risk and
consequence:

1. Health Risks
2. Academic Consequences
3. Social and Behavioural Consequences
4. Legal and Financial Consequences
5. Long-Term Societal Impact

**Environmental degradation** does not appear.

### Note the widening scope
The five run outward from the individual to society: **health** (the body) →
**academic** (studies) → **social/behavioural** (relationships) → **legal and
financial** (money and the law) → **long-term societal impact** (the country).
Substance abuse is framed as never staying a private matter.

### The near-miss worth spotting
**Long-Term Societal Impact** is a real category and sounds broad enough that
students sometimes stretch it to cover "environmental". It does not — the deck
lists it separately and never mentions environmental harm.

### Source
Dr. A. Olatunji, "Risks and Consequences of Substance Abuse" slide.
"""),

    q('swep_day2_43',
      'According to the safety lecture, what is an engineering workshop?',
      ['An office where engineering designs are approved and filed',
       'A facility equipped with tools, machinery and workspaces for practical training, design and fabrication',
       'A lecture theatre used for teaching engineering theory',
       'A storage warehouse for unused industrial equipment'],
      1,
      'It is a facility equipped with tools, machinery and workspaces for practical training, design and fabrication.',
      """
### Why this is the answer
An engineering workshop is defined as *"a facility equipped with **tools,
machinery, and workspaces** for **practical training, design, and
fabrication** in engineering disciplines."*

These workshops provide **hands-on experience** with processes including
machining, welding and carpentry — crucial for developing practical skills and
understanding engineering principles.

### The common types
Machine shops, fitting shops, **foundries**, **smithies**, welding shops and
carpentry workshops — each with specialised tools for particular tasks. They
exist for hands-on training, project manufacturing, equipment maintenance and
industrial training.

### Why this definition opens a safety lecture
Everything that makes a workshop useful — powered machinery, heat, sharp tools,
fabrication processes — is also what makes it **hazardous**. The definition
explains why PPE, hazard controls and signage occupy the remaining 60 slides.

### Source
Prof. A. A. Adeleke, "What is an Engineering Workshop?" and "Types of
Engineering Workshops" slides.
"""),

    q('swep_day2_44',
      'Which pairing of hazard type and example is correct according to the safety lecture?',
      ['Ergonomic hazards — exposure to bacteria and viruses',
       'Chemical hazards — noise, vibration and extreme temperatures',
       'Physical hazards — repetitive tasks and awkward postures',
       'Biological hazards — exposure to bacteria, viruses and fungi'],
      3,
      'Biological hazards are exposure to bacteria, viruses, fungi and other biological agents.',
      """
### Why this is the answer
The lecture defines four hazard families, and the three wrong options each swap
a definition into the wrong family.

| Hazard type | What it covers |
|---|---|
| **Chemical** | Toxic substances, flammable materials, corrosive agents |
| **Physical** | Noise, vibration, radiation, extreme temperatures, poor lighting |
| **Ergonomic** | Repetitive tasks, awkward postures, poor workstation design |
| **Biological** | **Bacteria, viruses, fungi and other biological agents** |

Only the biological pairing is stated correctly.

### The distinction students most often miss
**Physical hazards** are *energy* — noise, vibration, radiation, heat.
**Ergonomic hazards** are *how the body is used* — posture, repetition,
workstation layout, leading to musculoskeletal disorders. Both harm the body,
but through entirely different mechanisms.

### Alongside these
The deck also lists general industrial hazards: **slips, trips and falls,
unguarded machinery, electrical hazards and confined spaces**.

### Source
Prof. A. A. Adeleke, "Common Industrial Hazards" slides.
"""),

    q('swep_day2_45',
      'What five things does the employability lecture urge students to develop alongside their academic qualification?',
      ['Five foreign languages, a car, a house, savings and a business',
       'A strong communication ability, a digital capability, evidence of practical experience, a professional network and a learning habit',
       'Five certificates, five referees, five internships, five projects and five mentors',
       'A first-class degree, a postgraduate offer, a scholarship, a publication and an award'],
      1,
      'Communication ability, digital capability, practical experience, a professional network and a learning habit.',
      """
### Why this is the answer
Under **"A Special Message to Students and Graduates"**, the lecture opens with
*"Your degree is the **beginning** of your professional learning"* and then lists
five things to develop **while still in university**:

1. A strong **communication** ability
2. A **digital** capability
3. Evidence of **practical experience**
4. A professional **network**
5. A **learning habit**

### Why these five
Each maps onto a theme running through the whole lecture:

| Item | Where it comes from |
|---|---|
| Communication | *"Perhaps the most fundamental employability skill"* |
| Digital capability | *"A basic requirement for participation in modern economic life"* |
| Practical experience | *"Experience converts knowledge into competence"* |
| Network | *"Not only what you know but who knows what you can do"* |
| Learning habit | *"Above all: be a lifelong learner"* |

### Do not confuse it with the 8 clusters
**8** clusters of employability skills; **5** things to build alongside the
degree. Two different lists on two different slides.

### Source
Prof. A. B. Ekanola, "A Special Message to Students and Graduates" slide.
"""),
]

assert len(QUESTIONS) == 45, f'expected 45, got {len(QUESTIONS)}'
_ids = [x['id'] for x in QUESTIONS]
assert len(set(_ids)) == 45, 'duplicate ids'
for _q in QUESTIONS:
    assert len(_q['options']) == 4, f"{_q['id']}: needs 4 options"
    assert 0 <= _q['correct'] < 4, f"{_q['id']}: bad correct index"
    assert _q['short'] and _q['solution'], f"{_q['id']}: missing short/solution"
