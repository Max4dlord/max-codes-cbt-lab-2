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
]

QUESTION_SETS = [DAY1, DAY2]

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
    # course entry
    src = re.sub(r'\n\s*\{\s*"id":\s*"swep200".*?\n\s*\},(?=\n\])', '', src, flags=re.S)
    # categoryMeta / topicMeta / questionBank entries
    for key in ('categoryMeta', 'topicMeta', 'questionBank'):
        src = re.sub(r'\n  "swep200": \[.*?\n  \],(?=\n)', '', src, count=1, flags=re.S)
    return src


def main():
    src = DATA.read_text()
    if 'swep200' in src:
        print('! existing SWEP 200 block found — replacing it')
        src = strip_previous(src)

    questions = [q for group in QUESTION_SETS for q in group]

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

    # 4. questionBank -------------------------------------------------------
    src = src.replace('export const questionBank = {\n',
                      'export const questionBank = {\n  "swep200": ' + js(questions, 2) + ',\n', 1)

    DATA.write_text(src)
    print(f'✅ SWEP 200 spliced: {len(questions)} questions, '
          f'{len(TOPICS)} topic(s), {len(cats)} categor(ies)')


if __name__ == '__main__':
    main()
