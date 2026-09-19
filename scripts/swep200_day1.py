#!/usr/bin/env python3
"""SWEP 200 — Day 1 question bank (44 questions).

Questions supplied verbatim by the course owner. The Drive sources were used
ONLY to verify each stated answer and to write the rich per-question
explanations. Every fact below was checked against:

  * Prof. O. A. Olojede — "2026 SWEP 200 Orientation" lecture (9 pp.)
  * Prof. M. D. Shittu  — "History and Spread of the ITF in Nigeria" (25 pp.)
  * Prof. E. A. Taiwo   — "Benefits of Industrial Training" (26 pp., 16 of them
                          image-only slides read page by page)
  * Handwritten "Record of the Orientation Week Activities" — Day 1 ledger

Housekeeping applied to the supplied prompt:
  * "Option A: ..." prefixes stripped — the CBT renders A/B/C/D itself, so
    keeping them would print "A. Option A: ...".
  * Inline [span_n](start_span) citation artifacts removed.
  * Naira written as the real symbol (₦) rather than a capital N.
"""

TOPIC_ID = 'swep-day-1'


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
    q('swep_day1_01',
      "According to Prof. O.A. Olojede's lecture on University Rules & Regulations, the SWEP/SIWES scheme is jointly coordinated by the NUC and ITF. What does the acronym SET stand for in the NUC mandate, and what year was the ITF established?",
      ['Science, Engineering, and Technology; 1971',
       'Science, Education, and Technology; 1973',
       'Students, Engineering, and Training; 1974',
       'Science, Engineering, and Technology; 1985'],
      0,
      'SET stands for Science, Engineering, and Technology, and the ITF was established in 1971.',
      """
### Why this is the answer
The NUC mandate approved SWEP/SIWES for **S**cience, **E**ngineering and
**T**echnology (SET) courses in Nigerian tertiary institutions, specifically to
solve the practical-experience deficiency in those disciplines. The Industrial
Training Fund was established in **1971**, under Act No. 47 of that year.

### The tripartite structure
The scheme is jointly coordinated by the **NUC** and the **ITF**, and involves
three parties: the **Students**, the **Universities** and the **Industry**.

### Source
Prof. O. A. Olojede, "Background & Rationale" slide; corroborated by Prof. M. D.
Shittu's opening slide ("set up under Act 47 of 1971") and by the handwritten
Day 1 ledger, which records "NUC and ITF (est. 1971)".

### Why the others fail
- **Science, *Education*, and Technology; 1973** — swaps Engineering for
  Education. 1973 is when SIWES was established, not the ITF.
- **Students, Engineering, and Training; 1974** — fabricated expansion. 1974 is
  the year the ITF actually *started* running SIWES.
- **...; 1985** — 1985 is Decree No. 16, which gave SIWES legal backing. It has
  nothing to do with the ITF's founding.
"""),

    q('swep_day1_02',
      'Based on the 2026 SWEP 200 Orientation Daily Schedule presented by Prof. O. A. Olojede, what is the exact time window for the Second Attendance Registry Check, and which 5-year track module is the only one to receive ITF stipends?',
      ['12:00 – 12:30; SIWES I',
       '12:25 – 12:30; SIWES II',
       '08:00 – 08:30; SIWES II',
       '12:25 – 12:30; SWEP 200'],
      1,
      'The second check is strictly 12:25–12:30, and only SIWES II receives ITF stipends.',
      """
### Why this is the answer
Two separate facts have to line up:

1. **The midday break runs 12:00–12:30**, but the **Second Attendance Registry
   Check is strictly taken between 12:25 and 12:30** — the last five minutes.
   The break is for stretching; the register is not open for the whole half hour.
2. **Only SIWES II receives ITF stipends.** SIWES II spans the entire 400-Level
   Rain Semester plus part of the long vacation — a full **6 months (24 weeks)**.

### The full daily rhythm
| Time | Activity |
|---|---|
| 08:00 – 08:30 | Arrival + **First** attendance check |
| 08:30 – 09:00 | Recap of previous day |
| 09:00 – 10:30 | Lecture 1 |
| 10:30 – 12:00 | Lecture 2 |
| 12:00 – 12:30 | Break (**Second** check at 12:25–12:30) |
| 12:30 – 14:00 | Lecture 3 |

### Source
Prof. O. A. Olojede, "Training Timelines" and "Program Timelines" slides.

### Why the others fail
- **12:00–12:30; SIWES I** — assumes the register stays open the whole break,
  and SIWES I carries no stipend.
- **08:00–08:30; SIWES II** — that is the *morning* (first) registry window.
- **12:25–12:30; SWEP 200** — right time, wrong module. SWEP 200 is unpaid.
"""),

    q('swep_day1_03',
      "In Prof. E. A. Taiwo's lecture on the Benefits of Industrial Training, he detailed the historical progression of students' SIWES allowances. What were the exact allowance amounts paid in 1974, 1981, and 2000 respectively?",
      ['₦30, ₦90, ₦2,500',
       '₦30, ₦250, ₦2,500',
       '₦90, ₦250, ₦2,500',
       '₦30, ₦250, ₦2,000'],
      1,
      'The allowances were ₦30 in 1974, ₦250 in 1981, and ₦2,500 in 2000.',
      """
### Why this is the answer
The "Allowances" slide lists **four** monthly figures, and the question asks for
three of them. Read the years carefully:

| Year | Students' allowance (per month) |
|---|---|
| 1974 | **₦30** |
| 1976 | ₦90 |
| **1981** | **₦250** |
| 2000 | **₦2,500** |

So 1974 → ₦30, 1981 → ₦250, 2000 → ₦2,500. The ₦90 figure belongs to **1976**
and is the trap sitting in the middle of the list.

### Source
Prof. E. A. Taiwo, "Allowances" slide. The same slide notes the present-day
amount is left open ("???").

### Why the others fail
- **₦30, ₦90, ₦2,500** — substitutes the 1976 figure for the 1981 one.
- **₦90, ₦250, ₦2,500** — shifts the whole series one year forward.
- **₦30, ₦250, ₦2,000** — correct until the year 2000, which was ₦2,500.
"""),

    q('swep_day1_04',
      'During the period when the ITF withdrew from financing SIWES (1980-1984), the NBTE renamed the scheme to COSITA. What is the full meaning of the acronym COSITA as presented in Day 1 lectures?',
      ['Compulsory Supervised Industrial Training Attachment',
       'Cooperative Students Industrial Training Agency',
       'Coordinated Supervised Industrial Technical Attachment',
       'Compulsory Students Industrial Training Allowance'],
      0,
      'COSITA stands for Compulsory Supervised Industrial Training Attachment.',
      """
### Why this is the answer
Between **1980 and 1984** the Federal Government funded the scheme through the
**NUC and NBTE** rather than the ITF. During that window the **NBTE renamed
SIWES as COSITA — Compulsory Supervised Industrial Training Attachment**.

### How the name fits the history
Each word is doing work: the programme had just been made **compulsory** (the
1979 FME mandate), it remained **supervised**, it was **industrial training**,
and it took the form of an **attachment** to a firm.

### Source
Prof. E. A. Taiwo, "2.7 Brief History of SIWES" slide.

### Why the others fail
All three are invented expansions built from plausible SIWES vocabulary —
"Cooperative", "Coordinated", "Agency", "Allowance". This question tests whether
you memorised the exact historical wording, so the near-misses are deliberate.
"""),

    q('swep_day1_05',
      "According to Prof. M.D. Shittu's presentation on the History of ITF, what was the exact initial take-off grant provided by the Federal Government for the 1970-74 Plan Period, and in what year did the ITF and NUC allocate credit units to the SIWES programme at OAU?",
      ['₦2,500,000 (£1,000,000); 1985',
       '₦1,000,000 (£500,000); 1995',
       '₦1,000,000 (£500,000); 1994',
       '₦500,000 (£250,000); 1973'],
      1,
      'The initial grant was ₦1,000,000 (£500,000), and credit units were allocated in 1995.',
      """
### Why this is the answer
Two dates from opposite ends of Prof. Shittu's deck:

- **The take-off grant:** the Federal Government made available
  **₦1,000,000 (£500,000)** during the **1970–74 Plan Period**.
- **Credit units:** in **1995**, the ITF and the supervisory agencies adopted a
  resolution allocating credit units to SIWES — the ITF and NUC allocated
  **between 3 and 15 credit units** depending on course of study.

### Source
Prof. M. D. Shittu, "History of the Industrial Training Fund" and "The SIWES
Programme at OAU" slides.

### Why the others fail
- **₦2,500,000 (£1,000,000); 1985** — both figures invented.
- **₦1,000,000 (£500,000); 1994** — correct grant, wrong year. **1994** is when
  about **30% of firms began rejecting institutional requests**, preferring
  students to apply on individual merit. This is the sharpest distractor here.
- **₦500,000 (£250,000); 1973** — halves the grant; 1973 is when SIWES began.
"""),

    q('swep_day1_06',
      'Following the 1995 resolution discussed by Prof. M.D. Shittu, what is the exact distribution of SIWES credit units for Year II, Year III, and Year IV students in the OAU Faculty of Technology?',
      ['Year II: 2 units, Year III: 3 units, Year IV: 9 units',
       'Year II: 3 units, Year III: 3 units, Year IV: 6 units',
       'Year II: 3 units, Year III: 3 units, Year IV: 9 units',
       'Year II: 0 units, Year III: 6 units, Year IV: 9 units'],
      2,
      'The units are distributed as Year II: 3 units, Year III: 3 units, Year IV: 9 units.',
      """
### Why this is the answer
The 1995 allocation distributes the credit units across the years of study as:

| Year of study | Credit units |
|---|---|
| Year II (SWEP 200) | **3** |
| Year III (SIWES I) | **3** |
| Year IV (SIWES II) | **9** |

Total = **15 units**, which is the top of the "3 to 15 credit units" band the
ITF and NUC agreed.

### Why Year IV carries the weight
Year IV is **SIWES II** — the full **6-month (24-week)** industrial attachment,
and the only module that attracts ITF stipends. The heavier academic load
matches the far longer time commitment.

### Scope
This allocation is limited to the **Faculty of Technology** and most courses in
the **Faculty of Environmental Design and Management (EDM)**.

### Source
Prof. M. D. Shittu, "The SIWES Programme at OAU" slide.

### Why the others fail
Each alters one figure — 2 units in Year II, 6 units in Year IV, or a zeroed
Year II. Remember the shape: **3 / 3 / 9**.
"""),

    q('swep_day1_07',
      'Based on the Day 1 Summary of Activities handwritten ledger, which lecturer delivered the section explicitly highlighting the "primary concept, importance processes and interdependent relationship between Science and Engineering"?',
      ['Prof. O.A. Olojede',
       'Prof. M.D. Shittu',
       'Prof. E.A. Taiwo',
       'Engr. E.A. Taiwo'],
      2,
      'Prof. E.A. Taiwo delivered the lecture on the relationship between Science and Engineering.',
      """
### Why this is the answer
The handwritten Day 1 ledger records three lectures with three speakers. The
third entry — "**Benefits of Industrial Training for Science & Engineering
Students**", which "highlighted the primary concept, importance processes and
interdependent relationship between Science and Engineering" — is signed
**Speaker: Prof. E. A. Taiwo**.

This matches the title slide of his deck: *Prof. E. A. Taiwo, Department of
Chemical Engineering, Obafemi Awolowo University*.

### Day 1 at a glance
| # | Lecture | Speaker |
|---|---|---|
| 1 | Introduction to SWEP & SIWES; rules & regulations | Prof. O. A. Olojede |
| 2 | History & spread of the ITF in Nigeria | Prof. M. D. Shittu |
| 3 | Benefits of Industrial Training for Science & Engineering students | **Prof. E. A. Taiwo** |

### Why the others fail
- **Prof. Olojede** — taught rules, regulations and timelines.
- **Prof. Shittu** — taught ITF history and spread.
- **Engr. E. A. Taiwo** — right person, **wrong title**. The ledger and the
  slides both read **Prof.** Read titles as carefully as names.
"""),

    q('swep_day1_08',
      'Prof. E. A. Taiwo highlighted several intervention programs by the ITF designed to stimulate self-sufficiency in the Nation. What does the newest addition to these programs, the acronym SUPA, stand for?',
      ['Students Upgraded Practical Attachment',
       'Skill-Up Artisans',
       'Supervised Undergraduate Practical Assessment',
       'Standardized Utility for Professional Artisans'],
      1,
      'SUPA stands for Skill-Up Artisans.',
      """
### Why this is the answer
The **Amendment ITF Act of 2011** expanded the Fund's scope to "provide, promote
and encourage the acquisition of skills in order to stimulate self-sufficiency
in the Nation". On that premise the ITF launched several intervention
programmes, of which **Skill-Up Artisans (SUPA)** is explicitly described as
**"the newest addition"**.

### What SUPA actually does
- Tech-driven training
- Provides **official licensing**
- Grants access to **essential toolkits**
- Enhances craftsmanship and drives professional excellence
- Gives artisans access to **credit facilities**

### The full 2011 intervention list
NISDP, WOSEP, STEPP-C, CONSEP, and **SUPA**.

### Source
Prof. E. A. Taiwo, "ITF Mandate" and "Skill-Up Artisans (SUPA) — programme"
slides.

### Why the others fail
Note that SUPA targets **artisans**, not students. Two distractors wrongly frame
it as a student/undergraduate scheme; the fourth is corporate-sounding filler.
"""),

    q('swep_day1_09',
      'Which specific legal instrument legally backed the SIWES scheme, requiring all enrolled students in specialized engineering and applied sciences to have supervised industrial attachment, and directed the ITF to resume management?',
      ['Act 47 of 1971',
       'Decree No. 16 of August 1985',
       'The 2011 ITF Amendment Act',
       'Decree 47 of 1971'],
      1,
      'Decree No. 16 of August 1985 legally backed the scheme and directed the ITF to resume management.',
      """
### Why this is the answer
In **1985** the Federal Government legally backed SIWES through **Decree No. 16
of August 1985**. It required that *"all students enrolled in specialized
engineering, technical, business, applied sciences and applied arts should have
supervised industrial attachment as part of their studies"*.

The ITF was equally directed to **take charge and resume responsibility** for
managing SIWES (from November 1984), in collaboration with the supervising
agencies (NUC, NBTE).

### Don't confuse the two laws
| Instrument | Year | What it did |
|---|---|---|
| **Act / Decree 47** | 1971 | **Established the ITF itself** |
| **Decree No. 16** | 1985 | **Legally backed SIWES**, mandated attachment |
| 2011 Amendment | 2011 | Expanded ITF scope; launched NISDP, WOSEP, SUPA, etc. |

### Source
Prof. E. A. Taiwo, "2.7 Brief History of SIWES" (continued) slide.

### Why the others fail
Act 47 and Decree 47 of 1971 are the *same instrument* under two names, and both
created the Fund — they did not force SIWES expansion in the mid-80s. The 2011
Amendment came 26 years later.
"""),

    q('swep_day1_10',
      'According to Prof. E. A. Taiwo, what is the exact approved rate for the Supervisory allowance paid to the university to augment supervision expenses?',
      ["5% of students' allowance per month",
       '₦2,500 per student supervised',
       "10% of students' allowance per month",
       "15% of students' allowance per month"],
      2,
      "The supervisory allowance is exactly 10% of the students' allowance per month.",
      """
### Why this is the answer
The "Allowances" slide splits payment into two streams:

1. **Students' allowance** — the monthly figure paid to the trainee.
2. **Supervisory allowance** — "money paid to the university to augment
   supervision expenses", set at **10% of students' allowance per month**.

Because it is a **percentage**, the supervisory allowance automatically rises
whenever the student allowance is reviewed upward.

### Eligibility (same slide)
Satisfactory completion of **6 months** SIWES, evidenced by **Logbooks, Form 8
and Form SPE-1**, plus adequate vetting of logbooks.

### Source
Prof. E. A. Taiwo, "Allowances" slide.

### Why the others fail
- **₦2,500 per student** — that is the *year-2000 student* allowance, not the
  supervisory rate, and the supervisory figure is a percentage, not a flat sum.
- **5% / 15%** — plausible but simply wrong. The figure is **10%**.
"""),

    q('swep_day1_11',
      'According to Prof. O.A. Olojede, what is the ideal duration and the strict minimum duration for the SWEP 200 programme?',
      ['12 weeks ideally (strict minimum of 10 weeks)',
       '12 weeks ideally (strict minimum of 8 weeks)',
       '14 weeks ideally (strict minimum of 8 weeks)',
       '10 weeks ideally (strict minimum of 6 weeks)'],
      1,
      'SWEP 200 has an ideal duration of 12 weeks, with a strict minimum of 8 weeks.',
      """
### Why this is the answer
SWEP 200 runs for **ideally 12 weeks, with a strict minimum of 8 weeks**, during
the long vacation following the **200-Level Rain Semester**. The 8-week floor is
independently confirmed on Prof. Taiwo's "Components of SIWES" slide:
*"SWEP – Students Workshop Experience Programme (Min. of 8 wks.)"*.

### All three modules side by side
| Module | Duration | When |
|---|---|---|
| **SWEP 200** | 12 wks ideal, **8 wks minimum** | After 200-Level Rain Semester |
| **SIWES I** | 12 weeks | After 300-Level Rain Semester |
| **SIWES II** | **24 weeks (6 months)** | 400-Level Rain Semester + vacation |

### Source
Prof. O. A. Olojede, "Training Timelines: Scope, Durations & Programme
Frameworks" slide.

### Why the others fail
Each moves either the ideal figure or the floor. Anchor on **12 ideal / 8
minimum** — two numbers, both worth marks.
"""),

    q('swep_day1_12',
      'Under the 4-Year Program Exemptions outlined by Prof. Olojede, which specific disciplines are exempt from specific practical SWEP modules?',
      ['Architecture, Fine and Applied Arts, and Industrial Chemistry',
       'Chemical Engineering, Fine and Applied Arts, and Agricultural Science',
       'Architecture, Quantity Surveying, and Industrial Chemistry',
       'Architecture, Fine and Applied Arts, and Computer Engineering'],
      0,
      'Architecture, Fine and Applied Arts, and Industrial Chemistry are exempt.',
      """
### Why this is the answer
Under **4-Year Program Exemptions**, the named programmes are
**Architecture**, **Fine and Applied Arts**, and **Industrial Chemistry** —
these are exempt from specific practical modules.

### The related special case
The **Faculty of Agriculture** is handled separately: it employs a consolidated
**1-year 'Farm Year'** placement across the entire fourth academic session,
rather than the standard modules. That is a *substitution*, not an exemption.

### Source
Prof. O. A. Olojede, "Training Timelines" slide.

### Why the others fail
Each swaps in a discipline that is **not** exempt — Chemical Engineering,
Quantity Surveying and Computer Engineering are all core technical programmes
that keep their practical modules. Note the trap: *Industrial Chemistry* is
exempt, but *Chemical Engineering* is not.
"""),

    q('swep_day1_13',
      'How many strategically selected lectures are contained within the 5-day Orientation Blueprint for SWEP 200?',
      ['10 lectures', '12 lectures', '14 lectures', '15 lectures'],
      2,
      'The orientation spans 5 days and contains exactly 14 lectures.',
      """
### Why this is the answer
The Orientation Blueprint **spans 5 days and contains 14 strategically selected
lectures**.

### Why it is not simply 15
The daily schedule runs **three lectures a day** (09:00–10:30, 10:30–12:00,
12:30–14:00). Five days × three lectures = 15 slots, but the programme is
built around **14** lectures — one slot is not a numbered lecture. This is
exactly why the question is asked: the arithmetic guess gives the wrong answer.

### Source
Prof. O. A. Olojede, "Program Timelines: 2026 SWEP 200 Orientation Daily
Schedule" slide.

### Why the others fail
10 and 12 are simply too low. **15** is the tempting one — it is the number of
*slots*, not the number of *lectures*.
"""),

    q('swep_day1_14',
      'Regarding Amphitheatre Ground Rules (Part 2), what is the strict stance on device usage and physical posture?',
      ['iPads are allowed for note-taking, but dozing off is prohibited.',
       'Electronic restrictions require iPads and laptops to be put away entirely unless authorized, and dozing off or leaning heavily on trainees is disallowed.',
       'Laptops are allowed if muted, and audio headphones can be used for recording.',
       'Mobile phones can be on loud, but dietary rules bar any food.'],
      1,
      'Electronics must be put away unless authorized, and dozing/leaning is completely disallowed.',
      """
### Why this is the answer
**Electronic restrictions:** put away iPads, laptops and tablets **entirely**
unless they are part of authorised class activities. Audio
headphones/earphones are **prohibited**.

**Physical posture:** dozing off, deep sleeping, or leaning heavily on fellow
trainees is **completely disallowed**.

### The rest of Part 2
- **Movement control** — no aimless loitering between rows during a lecture.
- **Dietary & hygiene** — no food or drink other than **clean water**; no litter.
- **Dress code** — casual, inappropriate or indecent dressing is prohibited;
  dress formally. Leaving the venue needs **express coordinator permission**.

And from Part 1: mobile phones must remain **permanently on silent or vibration**.

### Source
Prof. O. A. Olojede, "Venue Decorum & Discipline: Amphitheatre Ground Rules
Part 2" slide.

### Why the others fail
Each contains one permission the rules never grant — iPads for notes, headphones
for recording, or phones on loud. Only clean water is allowed, and only
authorised device use.
"""),

    q('swep_day1_15',
      'What is the institutional consequence of attempting to sign the attendance register for another student during SWEP orientation?',
      ['A warning and deduction of attendance points.',
       'Immediate removal from the amphitheater.',
       'Handled as a criminal act.',
       "Suspension of the student's SIWES portal."],
      2,
      'Signing for another student is explicitly handled as a criminal act.',
      """
### Why this is the answer
Under **Attendance Integrity**, the rule is unambiguous: you must sign the
register **for yourself and by yourself only**, and *attempting to sign for
another student is handled as a criminal act*.

Note the wording — **attempting** is enough. The offence does not require that
the forged signature succeed.

### Why the penalty is set so high
Attendance is the backbone of the orientation: there are **two registry checks
every day** (08:00–08:30 and 12:25–12:30) across all five days. Signing for an
absent friend is falsification of an official record, which is why the
documentation escalates it beyond ordinary misconduct.

### Source
Prof. O. A. Olojede, "Venue Decorum & Integrity: Amphitheatre Ground Rules
Part 1" slide.

### Why the others fail
Warnings, removal from the hall and portal suspension are all softer,
*assumed* penalties. The slide deliberately uses the phrase **"criminal act"** —
do not downgrade it.
"""),

    q('swep_day1_16',
      'According to the Daily Schedule, what specific activity takes place between 08:30 and 09:00 every morning?',
      ['First Attendance Registry Check', 'Lecture 1',
       'Recap of previous day', 'Midday Break'],
      2,
      '08:30–09:00 is reserved for a recap of the previous day.',
      """
### Why this is the answer
The morning block is explicit: **08:30–09:00 is the Recap of the previous day**,
which sits between the arrival window and the first lecture.

### The full day
| Time | Activity |
|---|---|
| 08:00 – 08:30 | Arrival + **First** attendance registry check |
| **08:30 – 09:00** | **Recap of previous day** |
| 09:00 – 10:30 | Lecture 1 |
| 10:30 – 12:00 | Lecture 2 |
| 12:00 – 12:30 | Midday break (**Second** check, 12:25–12:30) |
| 12:30 – 14:00 | Lecture 3 |

Trainees must be **fully seated by 08:30** every morning — so the recap starts
the moment the arrival window closes.

### Source
Prof. O. A. Olojede, "Program Timelines" slide.

### Why the others fail
The registry check is **08:00–08:30**, Lecture 1 is **09:00–10:30**, and the
midday break is **12:00–12:30**. Each distractor is a real event at the wrong
time.
"""),

    q('swep_day1_17',
      'Prof. E.A. Taiwo provided a direct definition of the components of SIWES. What does the acronym SWEP specifically stand for?',
      ['Students Work Experience Programme',
       'Students Workshop Experience Programme',
       'Supervised Work Environment Protocol',
       'Students Working Experience Protocol'],
      1,
      'SWEP strictly stands for Students Workshop Experience Programme.',
      """
### Why this is the answer
Under **Components of SIWES**, the slide reads:
*"SWEP - Students **Workshop** Experience Programme (Min. of 8 wks.)"*.

The key word is **Workshop** — SWEP is Module 1, undergone **inside the school**
in the workshops, focusing on general workshop skills, safety protocols and
hands-on tool usage. SIWES is the module served **outside** in industry.

### The 3-tier OAU structure
| Tier | Full name | Duration |
|---|---|---|
| **SWEP** | Students **Workshop** Experience Programme | Min. 8 wks |
| SIWES I | Students Industrial Work Experience Scheme | 12 wks |
| SIWES II | Students Industrial Work Experience Scheme | 24 wks |

### Source
Prof. E. A. Taiwo, "2.0 Industrial Training — 2.1 Definitions" slide.

### Why the others fail
**"Students Work Experience Programme"** is the everyday misnomer, and it is the
answer most students pick — but it drops **Workshop**, which is the whole point
of the in-school module. The other two are fabricated.
"""),

    q('swep_day1_18',
      'In what year did the Federal Ministry of Education (FME) make it compulsory for all students of Polytechnics and Colleges of Technology to undergo a One-year IT programme?',
      ['1974', '1978', '1979', '1980'],
      2,
      'The FME made it compulsory in 1979.',
      """
### Why this is the answer
In **1979**, the Federal Ministry of Education made it **compulsory** for all
students of Polytechnics and Colleges of Technology to undergo a **One-year
Industrial Training programme**.

### Why this single year matters so much
It triggered everything that followed: the new compulsory intake made the
financial commitment unsustainable, so **by January 1980 the ITF withdrew from
financing SIWES** — which in turn handed funding to the NUC/NBTE (1980–1984)
and produced the **COSITA** renaming.

### The timeline in order
| Year | Event |
|---|---|
| 1973 | SIWES established by ITF |
| 1974 | SIWES actually started |
| to 1978 | ITF **fully funded** SIWES |
| **1979** | **FME makes 1-year IT compulsory** |
| Jan 1980 | ITF withdraws from financing |

### Source
Prof. E. A. Taiwo, "2.7 Brief History of SIWES" slide.

### Why the others fail
1974 is when SIWES started; 1978 is the end of full ITF funding; 1980 is the
withdrawal. Each distractor is the year immediately before or after.
"""),

    q('swep_day1_19',
      'Due to extreme financial commitment after the 1979 FME mandate, in what exact month and year did the ITF temporarily withdraw from financing SIWES?',
      ['January 1980', 'August 1980', 'November 1984', 'January 1978'],
      0,
      'The ITF withdrew from financing SIWES in January 1980.',
      """
### Why this is the answer
The slide is precise: after the 1979 mandate *"the commitment was much, **by
January 1980, ITF withdrew from financing SIWES**"*.

### Cause and effect
The 1979 FME directive made a one-year IT programme compulsory for **all**
Polytechnic and College of Technology students. That multiplied the number of
funded trainees overnight, and the Fund could not carry it.

### What filled the gap
**1980–1984:** the Federal Government funded the scheme through the **NUC and
NBTE**, and the NBTE renamed SIWES **COSITA**. The ITF was then directed to
resume management in **November 1984**.

### Source
Prof. E. A. Taiwo, "2.7 Brief History of SIWES" slide.

### Why the others fail
- **August 1980** — right year, invented month. *August* belongs to **Decree
  No. 16 of August 1985**.
- **November 1984** — the opposite event: when the ITF **resumed** control.
- **January 1978** — 1978 is when *full* ITF funding ended, before the mandate.
"""),

    q('swep_day1_20',
      'In what year was the SIWES scheme expanded to include courses in sciences, environmental sciences, agriculture, and other professional but non-technical courses?',
      ['1980', '1984', '1985', '1995'],
      1,
      'The scheme was expanded to include these additional courses in 1984.',
      """
### Why this is the answer
**In 1984** the scheme was expanded to include more courses in **sciences,
environmental sciences, agriculture and some other professional but
non-technical courses**.

Until then SIWES had been aimed at students whose courses were *directly related
to industry*. The 1984 expansion is what opened it to the broader spread of
disciplines participating today.

### 1984 was a busy year
It also saw the ITF **directed to resume management** of SIWES in **November
1984**, with the **IAGR Department** taking over administration.

### Source
Prof. E. A. Taiwo, "Brief History of SIWES" (continued) slide.

### Why the others fail
- **1980** — the NUC/NBTE funding takeover.
- **1985** — Decree No. 16 gave SIWES legal backing (the year *after*).
- **1995** — OAU credit-unit allocation, eleven years later.
"""),

    q('swep_day1_21',
      'When the ITF resumed responsibility for the management of SIWES in November 1984, which specific ITF department was responsible for SIWES administration?',
      ['Technical and Vocational Skills Training Department (TVSTD)',
       'Business Training and Development Department (BTD)',
       'Industrial Attachment, Grants and Reimbursement (IAGR) Department',
       'Field Services Department (FSD)'],
      2,
      'The IAGR Department was responsible for SIWES administration at that time.',
      """
### Why this is the answer
When the ITF resumed responsibility in **November 1984** — in collaboration with
the supervising agencies (NUC, NBTE) — the **Industrial Attachment, Grants and
Reimbursement (IAGR) Department** of the ITF was responsible for SIWES
administration **then**.

The name describes the three jobs exactly: placing students on **industrial
attachment**, disbursing **grants**, and handling employer **reimbursement**.

### Why "then" is the operative word
IAGR is the **historical** answer for 1984. The ITF has since restructured; the
modern organogram routes SIWES through the **Field Services Department**, which
contains a **SIWES Division** alongside Grants & Reimbursements. Read the date
in the question before answering.

### Source
Prof. E. A. Taiwo, "Brief History of SIWES" (continued) slide; modern structure
from Figure 1, Organogram of ITF.

### Why the others fail
TVSTD, BTD and FSD are all **current** ITF departments. They are correct names
in the wrong era.
"""),

    q('swep_day1_22',
      "According to Prof. Taiwo's lecture on E-SIWES, what is the exact official website URL used for transferring student records electronically?",
      ['www.itf-siwes.gov.ng', 'www.siwesdata.org',
       'www.esiwes.edu.ng', 'www.itf.org/siwes'],
      1,
      'The official portal is www.siwesdata.org.',
      """
### Why this is the answer
The **2.4 E-SIWES** slide states that *"it was planned that student records are
transferred electronically with the use of **www.siwesdata.org**"*.

### Why E-SIWES exists
The ITF had administered the scheme **manually**, and with the growing number of
institutions and students that became *"grueling"* and *"virtually impossible to
run hitch-free"*. Under E-SIWES, data is submitted online and allowances are
paid by **e-payment**.

### What the portal does
- Each participating **student and institution can verify** submitted records
- All relevant **forms can be downloaded**
- The slide notes the portal was still *"being perfected"* and hoped to launch
  soon

### Source
Prof. E. A. Taiwo, "2.4 E-SIWES" slide.

### Why the others fail
The other three borrow official-looking Nigerian domains (`.gov.ng`, `.edu.ng`)
which look more authoritative than the real answer. The actual portal is a
plain **`.org`**.
"""),

    q('swep_day1_23',
      'The E-payment system for SIWES is described as a subset of e-government. This initiative emerged from the budget presentation of which Nigerian President, and in what year?',
      ['President Olusegun Obasanjo in 2006',
       'President Goodluck Jonathan in 2011',
       'President Muhammadu Buhari in 2016',
       "President Umaru Musa Yar'Adua in 2009"],
      3,
      "It emerged from President Umaru Musa Yar'Adua's 2009 budget presentation.",
      """
### Why this is the answer
The **2.8 E-Payment System** slide states that e-payment is *a subset of
e-government*, **"emerging from the 2009 budget presentation by President Umaru
Musa Yar'Adua to the National Assembly"**.

### What e-government means here
The application of **electronic means** in the interaction between Government
and citizens, and Government and Business — direct payment and banking
**without physical appearance** of the agencies or bank.

### Source
Prof. E. A. Taiwo, "2.8 E-Payment System" slide.

### Why the others fail
Each pairs a real Nigerian president with a plausible year, but only
**Yar'Adua / 2009** matches the slide. Note that Yar'Adua's presidency
(2007–2010) is the only one that contains 2009.
"""),

    q('swep_day1_24',
      'Based on the structure of the Industrial Training Fund (ITF), how many Departments and Units operate at the Headquarters?',
      ['10 Departments and 3 Units', '15 Departments and 5 Units',
       '12 Departments and 4 Units', '15 Departments and 42 Units'],
      1,
      'The ITF operates with 15 Departments and 5 Units at the Headquarters.',
      """
### Why this is the answer
The **2.5 ITF AND SIWES** slide gives the full structure:

- A **13-member Governing Council**, headed by the Director-General
- **15 Departments and 5 Units** at the **Headquarters**
- **42 Area Offices**
- **5 Skills Training Centres**
- A **Centre for Industrial Training Excellence**

### Source
Prof. E. A. Taiwo, "2.5 ITF AND SIWES" slide.

### Why the others fail
**15 Departments and 42 Units** is the trap worth understanding: **42** is real,
but it counts **Area Offices** spread across the country, not Units at
headquarters. Keep the four numbers separate — **13** council members,
**15 + 5** at HQ, **42** area offices, **5** training centres.
"""),

    q('swep_day1_25',
      'Which of the following is NOT an acronym for one of the intervention programs expanded by the ITF under the 2011 Amendment Act to combat poverty and underemployment?',
      ['NISDP', 'WOSEP', 'CONSEP', 'COSITA'],
      3,
      'COSITA is a historical name for SIWES, not an intervention program under the 2011 Act.',
      """
### Why this is the answer
This is a **NOT** question — find the odd one out.

The **2011 ITF Amendment Act** intervention programmes are:

| Acronym | Full name |
|---|---|
| **NISDP** | National Industrial Skills Development Programme |
| **WOSEP** | Women Skills Empowerment Programme |
| **STEPP-C** | Skills Training & Empowerment Programme for the Physically Challenged |
| **CONSEP** | Construction Skills Empowerment Programme |
| **SUPA** | Skill-Up Artisans (the newest addition) |

**COSITA** belongs to a completely different era: it was the **NBTE's 1980–1984
renaming of SIWES** — Compulsory Supervised Industrial Training Attachment. It
predates the 2011 Act by roughly three decades.

### The purpose of the 2011 programmes
To develop **human capital** in order to combat *poverty, underemployment,
unemployment and youth restiveness*.

### Source
Prof. E. A. Taiwo, "ITF Mandate" slide.

### Why the others fail
NISDP, WOSEP and CONSEP are all **explicitly listed** 2011 intervention
programmes, so none of them can be the exception.
"""),

    q('swep_day1_26',
      'According to the chart on "Institutions Participating in SIWES", what is the exact breakdown of Federal, State, and Private Universities?',
      ['56 Federal, 58 State, 72 Private',
       '78 Federal, 107 State, 31 Private',
       '58 Federal, 56 State, 72 Private',
       '140 Federal, 175 State, 109 Private'],
      0,
      'Universities are divided into 56 Federal, 58 State, and 72 Private.',
      """
### Why this is the answer
The **Institutions Participating in SIWES** bar chart reads, for the
**UNIVERSITIES** cluster: **Fed 56, State 58, Private 72**.

### The complete chart
| Institution type | Federal | State | Private |
|---|---|---|---|
| **Universities** | **56** | **58** | **72** |
| Polytechnics | 78 | 107 | 31 |
| Colleges of Education | 6 | 10 | 6 |
| **TOTAL** | **140** | **175** | **109** |

Private universities (72) actually outnumber both Federal and State — the only
row where private leads.

### Source
Bar chart slide, "Institutions Participating in SIWES", Prof. E. A. Taiwo.

### Why the others fail
- **78 / 107 / 31** — that is the **Polytechnics** row.
- **58 / 56 / 72** — swaps Federal and State. Federal is the **smaller** at 56.
- **140 / 175 / 109** — the **TOTAL** column across all institution types.
"""),

    q('swep_day1_27',
      'According to the chart on "Institutions Participating in SIWES", what is the exact number of State Polytechnics participating in the scheme?',
      ['58', '107', '78', '175'],
      1,
      'There are exactly 107 State Polytechnics participating.',
      """
### Why this is the answer
In the **POLYTECHNICS** cluster of the bar chart the values are
**Fed 78, State 107, Private 31**. State Polytechnics therefore number
**107** — the tallest single non-total bar on the whole chart.

### Cross-check against the totals
State institutions sum to **58 (universities) + 107 (polytechnics) + 10
(colleges of education) = 175**, which matches the State total bar exactly. That
arithmetic confirms 107 is right.

### Source
Bar chart slide, "Institutions Participating in SIWES", Prof. E. A. Taiwo.

### Why the others fail
- **58** — State **Universities**, not polytechnics.
- **78** — **Federal** Polytechnics (same cluster, wrong bar).
- **175** — the **total** for all State institutions combined.
"""),

    q('swep_day1_28',
      'Who served as the very first Chief Executive (Secretary) of the ITF from 1971 to 1973?',
      ['Mrs. Ekei Nene Archibong', 'Alhaji Muhammed Dikko',
       'Dr. Abel Ubeku, OFR', 'Prof. Olu E. Akeredolu/Akerejola'],
      2,
      'Dr. Abel Ubeku served as the first Secretary from 1971-1973.',
      """
### Why this is the answer
"ITF Chief Executives from Inception to Date" opens with **1971–1973 · Dr. Abel
Ubeku, OFR · Secretary** — the very first entry, matching the Fund's founding
year.

### Note the changing job title
The role was styled **Secretary** at first, then **Director**, and only later
**Director-General**:

| Period | Chief Executive | Designation |
|---|---|---|
| **1971–1973** | **Dr. Abel Ubeku, OFR** | **Secretary** |
| 1973–1975 | Mrs. Ekei Nene Archibong | Secretary |
| 1976–1979 | Alhaji Muhammed Dikko | Director |
| 1980–1989 | Alhaji Muhammed Lawal Tildun Wada | Director-General |

### Source
Table slide, Prof. E. A. Taiwo's presentation.

### Why the others fail
Mrs. Archibong was the **second** Secretary (1973–1975); Alhaji Dikko was
**Director** (1976–1979); Prof. Akeredolu was DG (2000–2006).
"""),

    q('swep_day1_29',
      'Which Chief Executive (Director-General) of the ITF served during the period 2000-2006?',
      ['Prof. Longmas Sambo Wapmuk, OON', 'Alhaji Hassan Ahmed II, mni, MFR',
       'Sir Joseph Ntung Ari, KSM, KSS', 'Prof. Olu E. Akeredolu/Akerejola'],
      3,
      'Prof. Olu E. Akeredolu/Akerejola served as DG from 2000-2006.',
      """
### Why this is the answer
The table maps **2000–2006** to **Prof. Olu E. Akeredolu/Akerejola**,
Director-General.

### The surrounding sequence
| Period | Director-General |
|---|---|
| 1989–2000 | Alhaji Hassan Ahmed II, mni, MFR |
| **2000–2006** | **Prof. Olu E. Akeredolu/Akerejola** |
| 2006–2014 | Prof. Longmas Sambo Wapmuk, OON |
| 2014–2016 | Mrs. Juliet O. E. Chukkas-Onaeko, MFR |
| 2016–2023 | Sir Joseph Ntung Ari, KSM, KSS |

Because the periods run back-to-back, every distractor here is a **genuine DG**
from an adjacent block — you are being tested on the dates, not the names.

### Source
Table slide, "ITF Chief Executives from Inception to Date".

### Why the others fail
Prof. Wapmuk followed him (2006–2014); Alhaji Ahmed II preceded him
(1989–2000); Sir Joseph came much later (2016–2023).
"""),

    q('swep_day1_30',
      'Who is the current Director-General of the ITF as of 2024?',
      ['Mr. Dickson Onuoha', 'Dr. Afiz Oluwatoyin Ogun',
       'Mrs. Juliet O. E. Chukkas-Onaeko, MFR', 'Sir Joseph Ntung Ari'],
      1,
      'Dr. Afiz Oluwatoyin Ogun became the Director-General in 2024.',
      """
### Why this is the answer
The final row of the table reads **2024–present · Dr. Afiz Oluwatoyin Ogun ·
Director-General**.

### The immediate handover
| Period | Chief Executive | Designation |
|---|---|---|
| 2016–2023 | Sir Joseph Ntung Ari, KSM, KSS | Director-General |
| 2023–2024 | Mr. Dickson Onuoha | **Acting** Director-General |
| **2024–present** | **Dr. Afiz Oluwatoyin Ogun** | **Director-General** |

### Source
Table slide, "ITF Chief Executives from Inception to Date".

### Why the others fail
**Mr. Dickson Onuoha** is the sharpest distractor — he held the office in
2023–2024, but only in an **Acting** capacity, and handed over in 2024. Mrs.
Chukkas-Onaeko (2014–2016) and Sir Joseph (2016–2023) are earlier substantive DGs.
"""),

    q('swep_day1_31',
      "In Prof. M.D. Shittu's presentation, what specific legal Act set up the Industrial Training Fund?",
      ['Act 16 of 1985', 'Act 47 of 1971',
       'Decree 16 of 1971', 'The NUC Mandate of 1973'],
      1,
      'The ITF was set up under Act 47 of 1971.',
      """
### Why this is the answer
Prof. Shittu's opening slide states plainly: *"The Industrial Training Fund
(ITF) was set up under **Act No. 47 of 1971**."* Prof. Taiwo's deck refers to the
same instrument as *"Decree 47 of 1971 as Amended in the 2011 ITF ACT"* — **Act
47 and Decree 47 are the same law** under two naming conventions.

### What the Act was for
To **promote and encourage the acquisition of skills in industry and commerce**,
generating a pool of indigenous trained manpower sufficient for the economy. It
provided for **contributions from employers** and **subventions from the Federal
Government**.

### Keep the two numbers apart
- **47 → 1971 → created the ITF**
- **16 → 1985 → legally backed SIWES**

### Source
Prof. M. D. Shittu, "History of the Industrial Training Fund" slide.

### Why the others fail
"Act 16 of 1985" and "Decree 16 of 1971" both scramble the 1985 SIWES decree
into the ITF's founding. The NUC mandate is a policy approval, not the
establishing statute.
"""),

    q('swep_day1_32',
      'According to Prof. Shittu\'s presentation on "The SIWES Programme", what are the designated durations of the scheme for Polytechnics and Universities respectively?',
      ['Four months for Polytechnics; Six months for Universities',
       'Six months for Polytechnics; Four months for Universities',
       'Three months for Polytechnics; Six months for Universities',
       'Six months for both Polytechnics and Universities'],
      0,
      'It is 4 months for Polytechnics and 6 months for Universities.',
      """
### Why this is the answer
Under **Duration** on the SIWES Programme slide: **four months for Polytechnics
and Colleges of Education, and six months for the Universities**.

### Cross-check
The six-month university figure is consistent across the whole day's material:
**SIWES II spans 24 weeks (6 months)**, and eligibility for allowances requires
*"satisfactory completion of 6 months SIWES"*.

### The rest of that slide
- **Operators** — the ITF, the coordinating agencies (**NUC, NBTE, NCCE**),
  employers of labour, and the institutions
- **Funding** — Federal Government of Nigeria
- **Beneficiaries** — Agriculture, Engineering, Technology, Environmental
  Sciences, Education, Medical Sciences, Pure and Applied Sciences, Computing, etc.

### Source
Prof. M. D. Shittu, "THE SIWES PROGRAMME" slide.

### Why the others fail
Universities always take the **longer** attachment. Reversing the two, shrinking
polytechnics to three months, or equalising both at six all contradict the slide.
"""),

    q('swep_day1_33',
      'In what year was the SIWES Programme officially introduced, and when did Obafemi Awolowo University (then University of Ife) first start participating?',
      ['Introduced 1971; OAU joined 1974',
       'Introduced 1973; OAU joined 1973',
       'Introduced 1974; OAU joined 1979',
       'Introduced 1980; OAU joined 1985'],
      1,
      'The scheme was introduced in 1973, and OAU was one of the first participating institutions that same year.',
      """
### Why this is the answer
*"When the SIWES Programme was introduced in **1973**, University of Ife (now
Obafemi Awolowo University) was **one of the first participating
institutions**."* Both halves therefore fall in the **same year, 1973**.

### Reconciling 1973 and 1974
Prof. Taiwo's deck says SIWES was *"Established by ITF in 1973; but started
1974"* — establishment in 1973, first operation in 1974. Prof. Shittu's slide,
which this question is drawn from, uses **1973** for both the introduction and
OAU's entry. When a question names the lecturer, answer from that lecturer's
slide.

### What OAU participation looked like then
Students were placed on attachment **by the university**; host firms provided
**accommodation and transportation**; stipends were paid to the institution
before trainees arrived. It was a **graduation requirement carrying no credit
units** — that only changed in **1995**.

### Source
Prof. M. D. Shittu, "The SIWES Programme at OAU" slide.

### Why the others fail
1971 is the ITF's founding; 1974 is when SIWES began operating; 1980 and 1985
are the funding-crisis and legal-backing years.
"""),

    q('swep_day1_34',
      'According to the history of SIWES at OAU, what significant economic event in 1987 forced surviving companies to stop providing accommodation for trainees?',
      ['The 1987 NUC mandate withdrawal',
       'The privatization of Federal industries',
       'The second republic austerity measures and Structural Adjustment Programme (SAP)',
       'The withdrawal of ITF funding'],
      2,
      'The SAP and second republic austerity measures in 1987 impacted companies.',
      """
### Why this is the answer
By **1987**, the effects of the **second republic austerity measures** and the
then newly introduced **Structural Adjustment Programme (SAP)** by the military
administration had started hitting the firms hosting trainees.

### The knock-on effect
Surviving companies faced **massive retrenchment of staff**. They were still
receptive to institutional requests for placement, but **could no longer afford
accommodation** for trainees. Students were then placed on the basis of their
own ability to secure accommodation in the firms' cities — a situation that
lasted about **six years**, leading directly into the 1994 shift.

### Source
Prof. M. D. Shittu, "The SIWES Programme at OAU" slide.

### Why the others fail
- **ITF funding withdrawal** — real, but that was **January 1980**, seven years
  earlier and a different crisis.
- **NUC mandate withdrawal** and **privatisation of Federal industries** — not
  events described in this lecture.
"""),

    q('swep_day1_35',
      'What major shift in SIWES placement requests occurred at OAU in the year 1994?',
      ['30% of firms started rejecting institutional requests, preferring students to apply on individual merits.',
       'The university stopped placing students entirely, forcing ITF to step in.',
       'Companies stopped paying stipends to students.',
       'The university made SIWES optional due to placement difficulties.'],
      0,
      'In 1994, 30% of firms began rejecting bulk institutional placement requests.',
      """
### Why this is the answer
In **1994**, about **30% of the firms** started rejecting institutional requests,
preferring instead that **students apply for attachments on their individual
merits**. The institutions could hardly refuse, because the firms — mainly
corporate ones — were accepting students with **high cumulative grade points**.

### What it led to
Other industrial and commercial concerns adopted the same method, increasingly
based on **connections students could make** with firms, and institutional
requests became **practically phased out**. Firms began paying **stipends** for
accommodation and transport, and competition shifted to *which company offered
the highest stipend* — a dynamic Prof. Shittu notes is **still with us today**.

### Source
Prof. M. D. Shittu, "The SIWES Programme at OAU" slide.

### Why the others fail
- Stipends **started**, not stopped, in this period.
- The university did not stop placing students outright — placement decayed
  gradually.
- SIWES remained **compulsory** throughout; it was never made optional.
"""),

    q('swep_day1_36',
      'While the Faculty of Technology and EDM strictly allocate 3-15 SIWES credit units, which other faculties are expected to design and allocate credit units but are structurally lagging behind?',
      ['Law, Arts, and Humanities',
       'Sciences, Agriculture, Pharmacy, Health Sciences, Administration, and Social Sciences',
       'Education and Clinical Sciences only',
       'Environmental Design and Applied Arts'],
      1,
      'Sciences, Agriculture, Pharmacy, Health Sciences, Admin, and Social Sciences are also expected to allocate units.',
      """
### Why this is the answer
Prof. Shittu notes that the 1995 credit allocation is **limited to the Faculty of
Technology and most courses in EDM**, then lists the disciplines that *should
also benefit*: the **Sciences, Agriculture, Pharmacy, some departments in Health
Sciences, Administration and the Social Sciences**.

Each major discipline is **expected to design and allocate credit units** in
accordance with the periods allocated to SIWES in those courses — but, as he
puts it, *"this trend obtains till the present"*, meaning the gap persists.

### Source
Prof. M. D. Shittu, closing slides of "The SIWES Programme at OAU".

### Why the others fail
- **Law, Arts and Humanities** — not SIWES beneficiary disciplines.
- **Education and Clinical Sciences only** — far too narrow; Education is
  already a listed SIWES beneficiary.
- **Environmental Design and Applied Arts** — EDM is one of the faculties that
  **already allocates** units, so it cannot be among those lagging.
"""),

    q('swep_day1_37',
      'As part of the support machinery for training, the ITF gives a specific type of award. What is the name of this award as presented by Prof. Shittu?',
      ['Merit-based financial awards', 'Ex-gratia awards',
       'Pro-bono institutional grants', 'Subsidized corporate awards'],
      1,
      'The ITF gives ex-gratia awards as part of its support machinery.',
      """
### Why this is the answer
"The support machinery for training" lists six ways the Fund supports training,
and point **6** is simply *"giving **ex-gratia awards**"*.

### What "ex-gratia" means
Latin for *"out of grace"* — a payment made voluntarily, as a favour rather than
from legal obligation. The ITF is not contractually bound to give these; they
are discretionary.

### The full six-point machinery
1. Bearing a proportion of employers' **direct training costs**
2. Assisting and strengthening **training capability and facilities** nationwide
3. Directly building up **its own training facilities**
4. Organising **research and studies** into training
5. Publishing **training guides and manuals**
6. **Giving ex-gratia awards**

### Source
Prof. M. D. Shittu, "The support machinery for training" slide.

### Why the others fail
All three alternatives are plausible corporate phrasings, but the slide uses the
exact legal term **ex-gratia** — which is precisely what the question is testing.
"""),

    q('swep_day1_38',
      'Based on the Organizational Structure (Organogram) of the ITF presented by Prof. Shittu, which three units report directly to the Director-General alongside the Internal Audit Unit?',
      ['Field Services, SIWES Division, and Procurement Unit',
       'Legal and Council Affairs Unit, Public Relations and Publicity Unit, and SERVICOM Office',
       'Human Resources, Finance, and SERVICOM Office',
       'Corporate Planning, Legal and Council Affairs, and Audit Unit'],
      1,
      'The three parallel units are Legal and Council Affairs, Public Relations and Publicity, and the SERVICOM Office.',
      """
### Why this is the answer
In **Figure 1: Organogram of ITF**, four arrows branch sideways from the
**Director-General** to four staff units:

1. **Legal and Council Affairs Unit**
2. **Internal Audit Unit** *(named in the question)*
3. **Public Relations and Publicity Unit**
4. **SERVICOM Office**

So the three *alongside* Internal Audit are Legal and Council Affairs, Public
Relations and Publicity, and SERVICOM.

### Units vs Departments — read the chart shape
Above the DG sits the **Governing Council**. The four **units** hang off to the
**side** (advisory/oversight). The six **departments** sit in a row **below**:
Administration & Human Resource; Finance and Accounts; Consultancy, Research and
Information Tech.; **Field Services**; Industrial Training Devt.; and Business
Training Dev.

Note that **SIWES Div.** lives *under* the Field Services Department — two
levels down, not reporting to the DG.

### Source
Prof. M. D. Shittu, Figure 1: Organogram of ITF.

### Why the others fail
Each mixes tiers: Field Services and the SIWES Division are department-level or
lower, and Human Resources, Finance, Procurement and Corporate Planning are
**departments**, not the side units.
"""),

    q('swep_day1_39',
      'Based on the handwritten summary notes for Day 1, which speaker handled the sub-topic concerning the "Rules & Regulations guiding trainees/students conduct while the programme lasts"?',
      ['Prof. E.A. Taiwo', 'Prof. M.D. Shittu',
       'Prof. O.A. Olojede', 'Engr. M.D. Shittu'],
      2,
      'Prof. O.A. Olojede taught the Rules & Regulations.',
      """
### Why this is the answer
The Day 1 handwritten ledger records: *"Rules & Regulations guiding
trainees/students conduct while the programme lasts as well as the university
Rules for registration & Examination were treated. **Speaker: Prof. O. A.
Olojede**."*

This matches his slide deck exactly — its full title is *"General Introduction,
University Rules & Regulations on Course Registration & Examinations"*, and he
is **Deputy Director, ITCU, OAU**. The deck contains both amphitheatre decorum
sections and the OAU Academic Code.

### Source
Handwritten "Record of the Orientation Week Activities", Day 1 (Monday, 14th
September); Prof. Olojede's slide headers.

### Why the others fail
- **Prof. Taiwo** — benefits of industrial training.
- **Prof. Shittu** — ITF history and spread.
- **Engr. M. D. Shittu** — wrong person *and* wrong title.
"""),

    q('swep_day1_40',
      'According to the handwritten Day 1 Summary, which speaker specifically taught "How SIWES programme came into existence (Generally & in OAU)"?',
      ['Prof. E.A. Taiwo', 'Prof. O.A. Olojede',
       'Prof. M.D. Shittu', 'Engr. O.A. Olojede'],
      2,
      'Prof. M.D. Shittu taught how SIWES came into existence generally and in OAU.',
      """
### Why this is the answer
The ledger's second entry covers the **History & spread of the Industrial
Training Fund (ITF) in Nigeria**, and lists under it *"How SIWES programme came
into existence (Generally & in OAU)"*, closing with **Speaker: Prof. M. D.
Shittu**.

His deck confirms the scope — its outline runs: History of the ITF, Services
offered by ITF, ITF centres nationwide, **The SIWES Programme**, and **SIWES at
OAU**. The phrase *"Generally & in OAU"* maps onto those last two sections exactly.

### Source
Handwritten "Record of the Orientation Week Activities", Day 1; Prof. Shittu's
outline slide.

### Why the others fail
- **Prof. Taiwo** — benefits of industrial training.
- **Prof. Olojede** — rules, regulations and timelines.
- **Engr. O. A. Olojede** — wrong person *and* wrong title.
"""),

    q('swep_day1_41',
      'Under the "Scope, Durations & Programme Frameworks" timeline, when exactly is SIWES I held for students on 5-Year Tracks?',
      ['During the 400-Level Rain Semester',
       'During the long vacation following the 200-Level Rain Semester',
       'During the long vacation immediately after the 300-Level Rain Semester',
       'Throughout their entire fourth academic session'],
      2,
      'SIWES I is held during the long vacation after the 300-Level Rain Semester.',
      """
### Why this is the answer
For 5-Year Tracks, **SIWES I is held during the long vacation immediately after
the 300-Level Rain Semester**.

### The full ladder — note every option below is a real entry
| Module | When |
|---|---|
| **SWEP 200** | Long vacation after the **200**-Level Rain Semester |
| **SIWES I** | Long vacation after the **300**-Level Rain Semester |
| **SIWES II** | The entire **400**-Level Rain Semester + part of the vacation (24 wks) |
| Agriculture's 'Farm Year' | The entire **fourth academic session** |

Every distractor in this question is a genuine timeline from the same slide,
attached to the wrong module — so match the **level number** to the module.

### Source
Prof. O. A. Olojede, "Training Timelines: Scope, Durations & Programme
Frameworks" slide.

### Why the others fail
The 400-Level Rain Semester is **SIWES II**; the 200-Level vacation is **SWEP
200**; the fourth-session placement is the **Faculty of Agriculture's Farm Year**.
"""),

    q('swep_day1_42',
      "Which specific faculty employs a consolidated 1-year 'Farm Year' placement throughout their entire fourth academic session in place of standard modules?",
      ['Faculty of Environmental Design', 'Faculty of Agriculture',
       'Faculty of Science', 'Faculty of Technology'],
      1,
      "The Faculty of Agriculture employs the 1-year 'Farm Year'.",
      """
### Why this is the answer
The **Faculty of Agriculture** employs a consolidated **1-year 'Farm Year'**
placement throughout their **entire fourth academic session**, in place of the
standard SWEP/SIWES module pattern.

### Why agriculture is treated differently
Farming is **seasonal**. A 12-week vacation attachment cannot cover a full
planting-to-harvest cycle, so agriculture students need a continuous year on
placement to experience the complete agricultural calendar.

### Related but distinct
This is a **substitution**, not an exemption. Contrast it with the **4-Year
Program Exemptions** — Architecture, Fine and Applied Arts, and Industrial
Chemistry — which are exempt from specific practical modules altogether.

### Source
Prof. O. A. Olojede, "Training Timelines" slide.

### Why the others fail
Technology and EDM run the standard 3/3/9 credit-unit modules; the Faculty of
Science follows standard arrangements. Only Agriculture uses the 'Farm Year'
structure and terminology.
"""),

    q('swep_day1_43',
      'According to Prof. Taiwo, what is one major implication/benefit of the E-Payment system regarding the handling of physical cheques?',
      ['It requires students to physically verify cheques at the ITF office.',
       'It eliminates the stealing of cheques, forging of signatures, and disparity between amounts in words and figures.',
       'It allows institutions to print cheques locally to save time.',
       'It increases transaction costs but guarantees faster delivery.'],
      1,
      'E-payment eliminates stolen cheques, forged signatures, and number disparities.',
      """
### Why this is the answer
Under **"The implications"**, the final bullet reads *"**Eliminates Writing of
cheques:** No stolen of cheques again, forging of signature and disparity
between amount in words and figures will be eliminated totally."*

Remove the physical cheque and you remove all three failure modes at once —
theft, forgery, and the words-versus-figures mismatch.

### The other implications listed
- Cheque/cash payment of supervisory and student allowances **abrogated**
- **No physical contact** between ITF accounts officials and beneficiaries
- Easy **tracking of payments**, assisting the audit trail
- **Reduces cases of corruption**
- **Reduced transaction costs** and increased convenience
- Improved **financial reporting, transparency and accountability**

### Source
Prof. E. A. Taiwo, "The implications" slide (E-Payment System).

### Why the others fail
The system **removes** physical contact (so no office verification), **abolishes**
cheques rather than printing them locally, and **reduces** transaction costs
rather than increasing them. Each distractor inverts a stated benefit.
"""),

    q('swep_day1_44',
      'How is the SIWES programme primarily funded according to the "Operators and Funding" section of Prof. Shittu\'s lecture?',
      ['Jointly by the Federal Government and Private Industries',
       'Solely by the NUC and NBTE',
       'By the Federal Government of Nigeria',
       'By student union contributions and ITF grants'],
      2,
      'SIWES is funded by the Federal Government of Nigeria.',
      """
### Why this is the answer
On "THE SIWES PROGRAMME" slide, **Funding** is listed with a single line:
**"Federal Government of Nigeria"**.

### Don't confuse operators with funders
The same slide separates the roles clearly:

| Role | Who |
|---|---|
| **Operators** | ITF, coordinating agencies (**NUC, NBTE, NCCE**), employers of labour, institutions |
| **Funding** | **Federal Government of Nigeria** |
| Beneficiaries | Agriculture, Engineering, Technology, Environmental Sciences, Education, Medical Sciences, Pure & Applied Sciences, Computing, etc. |

Employers **operate** the scheme by hosting and supervising students — that is
not the same as funding it.

### Source
Prof. M. D. Shittu, "THE SIWES PROGRAMME" slide.

### Why the others fail
- **Jointly with Private Industries** — industries host and may pay stipends,
  but formal funding is Federal Government.
- **Solely by NUC and NBTE** — true only for the **1980–1984** interregnum.
- **Student union contributions** — never a funding source.
"""),
]

assert len(QUESTIONS) == 44, f'expected 44, got {len(QUESTIONS)}'
_ids = [x['id'] for x in QUESTIONS]
assert len(set(_ids)) == 44, 'duplicate ids'
for _q in QUESTIONS:
    assert len(_q['options']) == 4, f"{_q['id']}: needs 4 options"
    assert 0 <= _q['correct'] < 4, f"{_q['id']}: bad correct index"
