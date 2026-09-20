#!/usr/bin/env python3
"""SWEP 200 - Day 5 question bank (40 questions).

Day 5: Friday, 18th September.
  Employers' Expectations from Fresh Graduates in the 21st-Century Job Market
  Speaker: Representative, Nigeria Employers' Consultative Association (NECA)

SOURCE NOTE
-----------
Day 5 has a single lecture and the shortest source in the week (a 3-page
organised note plus the ledger). The note names the speaker only as
"[Name] (Representative, Nigeria Employers' Consultative Association)" - the
personal name is genuinely absent from the material, so no question asks for
it. Questions that touch attribution ask for the ORGANISATION, which is stated.

Because the source is compact, coverage is exhaustive rather than sampled:
every bullet in all seven sections is examined, and the questions lean on
precise numbers (3-5 goals, first 4-5 days, 12 weeks), exact ordering (the
SIWES learning loop), and the near-identical lists that the note deliberately
places side by side (things to do BEFORE vs DURING, what employers NOTICE vs
skills to DEVELOP) - which is where a careless student loses marks.

Verified against:
  * SWEP_Day5_Organized_Notes_v2.pdf (3 pp.)
  * Handwritten Day 5 orientation ledger
"""

TOPIC_ID = 'swep-day-5'


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
    q('swep_day5_01',
      'The Day 5 session was delivered by a representative of which organisation?',
      ['National Universities Commission (NUC)',
       'Industrial Training Fund (ITF)',
       "Nigeria Employers' Consultative Association (NECA)",
       'Council for the Regulation of Engineering in Nigeria (COREN)'],
      2,
      "The Nigeria Employers' Consultative Association (NECA).",
      """
### Why this is the answer
The Day 5 note is headed *"Employers' Expectation from Fresh Graduates in the
21st-Century Job Market — Speaker: Representative, **Nigeria Employers'
Consultative Association**."*

### Why the organisation matters to the content
This is the only SWEP lecture delivered from the **employers' side of the
table**. Every other day was taught by academics or institutional officers;
Day 5 is industry telling students directly what it looks for. That is why the
note reads as expectations and warnings rather than theory — including the blunt
line *"Nobody is your best friend at work."*

### The other bodies, and where they actually appear
| Body | Where it features in SWEP |
|---|---|
| **NUC** | Day 1 — approved SWEP/SIWES for **SET** courses; allocated credit units with ITF |
| **ITF** | Day 1 — established **1971** under Act 47; Day 5 — *"meet all **ITF requirements** for valid participation"* |
| **COREN** | Day 3 — *"will now regulate admissions into our engineering programmes"* |

All three are real SWEP organisations, which is exactly what makes them good
distractors.

### Source
SWEP Day 5 note header; handwritten Day 5 ledger.
"""),

    q('swep_day5_02',
      'According to the lecture, what is SIWES properly meant to be?',
      ['A period to gain experience that should be converted into verifiable skills in order to guarantee employability',
       'A break from academic activities before final year',
       'A compulsory formality required only for graduation clearance',
       'An opportunity to secure immediate permanent employment'],
      0,
      'A period to convert experience into verifiable skills that guarantee employability.',
      """
### Why this is the answer
The note opens by correcting a misconception: *"SIWES is **not just an
industrial training or a means of escape from academic activities**, but a
period to gain experience that should be **converted into verifiable skills** in
order to **guarantee employability**."*

Note the operative word: **verifiable**. Experience alone is not the deliverable
— evidence of skill is.

### The second core concept
*"The SIWES period is for **building human networks**, as **network brings good
net worth**."*

Two purposes, then: **verifiable skills** and **human networks**. Both recur
through the rest of the note — the portfolio serves the first, networking skills
the second.

### The view the note explicitly rejects
The phrase *"a means of escape from academic activities"* appears in the note
precisely so it can be denied. It is the attitude the lecture exists to correct.

### Source
Day 5 note, "Core Concepts of SIWES".
"""),

    q('swep_day5_03',
      'What mindset shift does the lecture ask students to make?',
      ['See yourself as an employee entitled to a salary',
       'See yourself as a temporary visitor to the organisation',
       'See yourself as an observer with no responsibilities',
       'See yourself as a professional in training, not just a mere student, being equipped to create value and build evidence'],
      3,
      'See yourself as a professional in training, not a mere student.',
      """
### Why this is the answer
*"See yourself as a **professional in training**, not just a mere student. You
are being **equipped to create value and build evidence**."*

The handwritten ledger reinforces it: the session *"emphasised transitioning
from a **student mindset** to a **'professional in training'** to build
**verifiable skills and networks**."*

### The two verbs that define the shift
| Verb | What it means in practice |
|---|---|
| **Create value** | You are there to contribute, not merely to watch |
| **Build evidence** | Every contribution should leave a documented trace |

### Why this is the note's hinge
Every later instruction follows from it. A *student* collects tasks and waits to
be graded; a *professional in training* documents outcomes, asks strategic
questions, protects confidential information and manages a reporting line. The
mindset dictates the behaviour — which is why the note places it before the
checklists rather than after them.

### Source
Day 5 note, "Mindset Shift"; handwritten Day 5 ledger.
"""),

    q('swep_day5_04',
      'How many learning goals does the lecture instruct students to define for their SIWES programme?',
      ['1 to 2 goals', '10 goals', '6 to 8 goals', '3 to 5 goals'],
      3,
      'Define 3 to 5 learning goals.',
      """
### Why this is the answer
Under **Things to Do Before SIWES**: *"**Define 3 to 5 learning goals** for your
SIWES program."*

The same figure returns at the very end, under the **Twelve Weeks Action Plan**:
*"**Set 3-5 goals**."* The note states it twice — before the attachment and as
the first item of the action plan — which is a strong signal it is examinable.

### The three numbers of Day 5
| Number | What it counts |
|---|---|
| **3 to 5** | **Learning goals** |
| **4 to 5** | **Days** in the critical first period |
| **12** | **Weeks** in the action plan |

These are the only quantities in the entire note, and they are easily swapped
under pressure. **Goals 3-5, days 4-5, weeks 12.**

### Why so few goals
Three to five is small enough to pursue seriously across twelve weeks and to
evidence individually in a portfolio. A longer list would produce attendance
rather than achievement.

### Source
Day 5 note, "Things to Do Before SIWES" and "Twelve Weeks Action Plan".
"""),

    q('swep_day5_05',
      'Which of the following is NOT listed among the things to do BEFORE SIWES?',
      ['Make research on the assigned organisation',
       'Know your reporting line — whom to always report to',
       'Keep a daily learning record of tasks completed',
       'Prepare your professional wardrobe and avoid casual dressing'],
      2,
      'Keeping a daily learning record belongs to the first days DURING SIWES.',
      """
### Why this is the answer
A **NOT** question turning on the note's deliberate before/during split.

**Things to Do BEFORE SIWES:**
- Make **research** on the assigned organisation
- Update your **CV and social media profiles** (e.g. **LinkedIn**; use a
  **professional email address**)
- Define **3 to 5 learning goals**
- Prepare your **professional wardrobe**; avoid casual dressing
- Have a **daily routine**, prepare notebooks and necessary documents
- Know your **reporting line** — whom to always report to
- Make sure to get a **Role Title** — know your responsibility
- Meet all **ITF requirements** for valid participation

**Keep a daily learning record** appears under *What to Do During the First 4 to
5 Days*, not before.

### The distinction being tested
You cannot *record learning* before the attachment begins — there is nothing yet
to record. What you prepare beforehand is the **notebook**; what you do
afterwards is **fill it**. The note lists "prepare notebooks" before and "keep a
daily learning record" during, and that pairing is the trap.

### Source
Day 5 note, "Things to Do Before SIWES" and "What to Do During the First 4 to 5
Days in SIWES".
"""),

    q('swep_day5_06',
      'The lecture gives specific guidance on the first days of SIWES. What period does it cover, and what does it say to do from day one?',
      ['The first 4 to 5 days; observe, listen, and introduce yourself properly to the audience',
       'The first 1 to 2 days; sit quietly and avoid drawing attention',
       'The first 2 weeks; complete as many tasks as possible to impress',
       'The first month; request a formal performance review'],
      0,
      'The first 4 to 5 days: observe, listen and introduce yourself properly.',
      """
### Why this is the answer
The section is headed **"What to Do During the First 4 to 5 Days in SIWES"**,
and its opening instruction is: *"**From day one: Observe, listen, and introduce
yourself properly** to the audience."*

### The full first-days checklist
- **From day one:** observe, listen, introduce yourself properly
- **Ask questions** — *"career development is a **strategic effort**"*. The
  examples given: *Who is my supervisor? What is my responsibility? **What does
  success look like?***
- Keep a **daily learning record** and **dress appropriately**
- Always **protect confidential information** and **always ask questions**

### The posture the note rejects
The note says the opposite of sitting quietly. **Asking questions** is repeated
**twice** in four bullets — once with examples and once as a closing emphasis.
Silence is not the recommended posture; **strategic enquiry** is.

### The best of the three sample questions
*"**What does success look like?"** — it converts a vague placement into a
measurable target, which is what the whole note is driving at.

### Source
Day 5 note, "What to Do During the First 4 to 5 Days in SIWES".
"""),

    q('swep_day5_07',
      'Which set correctly lists what employers notice, observe or expect?',
      ['Punctuality, communication, initiative, team work, professionalism and integrity',
       'Punctuality, digital literacy, networking, work ethics and presentation skills',
       'Initiative, technical skills acquisition, team work and communication skills',
       'Integrity, observation, reflection, documentation and practice'],
      0,
      'Punctuality, communication, initiative, team work, professionalism, integrity.',
      """
### Why this is the answer
**What Employers Notice, Observe, or Expect** — exactly six items:

| # | Trait |
|---|---|
| 1 | **Punctuality** |
| 2 | **Communication** (listening and asking questions) |
| 3 | **Initiative** |
| 4 | **Team work** (supporting colleagues) |
| 5 | **Professionalism** |
| 6 | **Integrity** |

### Why the distractors are dangerous
The note contains **three separate lists** that overlap heavily, and each wrong
option blends two of them:

| List | Contents |
|---|---|
| **Employers notice** | Punctuality · communication · initiative · team work · professionalism · integrity |
| **Skills to develop** | Technical skills · communication · **digital literacy** · team work · **speaking/presentation** · **work ethics** · **networking** |
| **Learning loop** | **Observe · ask questions/practice · document · reflect** |

*Communication* and *team work* appear in two lists; *digital literacy*,
*networking* and *presentation* belong only to skills; *observe* and *reflect*
only to the loop.

### The warning attached
> **Beware of office politics! Nobody is your best friend at work.**

### Source
Day 5 note, "What Employers Notice, Observe, or Expect".
"""),

    q('swep_day5_08',
      'What is the correct order of the four stages of the SIWES Learning Loop?',
      ['Observe → ask questions / practice → document experiences → reflect',
       'Reflect → observe → document → practice',
       'Document → observe → reflect → practice',
       'Ask questions → reflect → observe → document'],
      0,
      'Observe → ask questions/practice → document experiences → reflect.',
      """
### Why this is the answer
The **SIWES Learning Loop** — *"using every assignment and activity as a
learning capability"* — runs:

| # | Stage |
|---|---|
| 1 | **Observe** |
| 2 | **Ask questions / Practice** |
| 3 | **Document experiences** |
| 4 | **Reflect** |

The handwritten ledger confirms the same order: *"the 'SIWES learning loop'
(**observe, practice, document, reflect**) to convert daily activities into
**tangible capabilities** rather than just completing tasks."*

### Why the sequence is logical
You must **observe** before you know what to ask; you **practise** what you
asked about; you **document** what you practised; and only then can you
**reflect** on documented evidence rather than vague memory. Reflection first —
as that alternative proposes — would have nothing to work on.

### The instruction attached
> *"**Don't just collect tasks, but collate evidence** (How, when & what). Have
> a **digital portfolio**. Do not have a **career mismatch**."*

**Collect tasks** versus **collate evidence** is the distinction the whole loop
exists to enforce.

### Source
Day 5 note, "SIWES Learning Loop"; handwritten Day 5 ledger.
"""),

    q('swep_day5_09',
      'The lecture warns students about a specific workplace hazard in social terms. What is the warning?',
      ['Beware of office politics — nobody is your best friend at work',
       'Beware of overtime — never work beyond official hours',
       'Beware of supervisors — avoid reporting to more than one person',
       'Beware of colleagues — never share any information at all'],
      0,
      'Beware of office politics! Nobody is your best friend at work.',
      """
### Why this is the answer
The note's warning is stated bluntly, immediately after the list of traits
employers look for:

> **Note: Beware of office politics! Nobody is your best friend at work.**

### How to read it correctly
It is a caution about **discretion**, not hostility. Read alongside two other
instructions, its meaning is clear:

- *"Always **protect confidential information**"* — guard what you disclose
- *"The SIWES period is for **building human networks**, as **network brings
  good net worth**"* — but *do* build relationships

So the note simultaneously tells students to **network deliberately** and to
**not confide indiscriminately**. That alternative overstates it into never sharing
anything, which would contradict the networking instruction entirely.

### A related instruction, not a hazard
Knowing your **reporting line** — *"whom to always report to"* — is listed as a
positive preparation task, not a hazard to avoid.

### Source
Day 5 note, "What Employers Notice, Observe, or Expect".
"""),

    q('swep_day5_10',
      'Which of the following is listed under "Skills to Develop" rather than under what employers notice?',
      ['Punctuality', 'Integrity', 'Digital literacy', 'Professionalism'],
      2,
      'Digital literacy is listed under Skills to Develop.',
      """
### Why this is the answer
**Skills to Develop** — seven items:

| # | Skill |
|---|---|
| 1 | Technical skills acquisition |
| 2 | Communication skills |
| 3 | **Digital literacy** |
| 4 | Team work |
| 5 | Speaking / Presentation skills |
| 6 | Work ethics |
| 7 | Networking skills |

**Punctuality, integrity and professionalism** belong to **What Employers
Notice, Observe, or Expect** — not to this list.

### The conceptual difference between the two lists
| List | Nature |
|---|---|
| **Employers notice** | **Behaviours and character** — how you conduct yourself |
| **Skills to develop** | **Capabilities** — what you can do |

Punctuality and integrity are not *skills* you train; they are dispositions you
demonstrate. Digital literacy and presentation *are* trainable capabilities.
That is why the note separates them.

### The overlap to watch
**Communication** and **team work** appear on **both** lists — they are
simultaneously observed and developed, which is why they cannot be used to tell
the lists apart.

### Source
Day 5 note, "Skills to Develop" and "What Employers Notice, Observe, or Expect".
"""),

    q('swep_day5_11',
      'What does the lecture say about networks, in the phrase used in the note?',
      ['Network brings good net worth', 'Network guarantees immediate employment',
       'Network replaces the need for technical skills', 'Network is only useful after graduation'],
      0,
      'Network brings good net worth.',
      """
### Why this is the answer
*"The SIWES period is for **building human networks**, as **network brings good
net worth**."*

The wordplay is deliberate — **net·work → net·worth** — which is precisely why it
is memorable and examinable.

### Where it reappears
**Networking skills** is the final entry in **Skills to Develop**, and the
before-SIWES checklist requires updating your **LinkedIn profile** — a
networking instrument. The 12-week plan then asks for *"a CV and **LinkedIn
profile** tailored to your goals"*. The theme runs the length of the note.

### Why that alternative is decisively wrong
The note never opposes networks to skills — it pairs them. The two stated
purposes of SIWES are *"**verifiable skills**"* **and** *"building **human
networks**"*. The ledger records both together: *"to build **verifiable skills
and networks**."*

They are complements, not substitutes.

### Source
Day 5 note, "Core Concepts of SIWES".
"""),

    q('swep_day5_12',
      'What does the lecture instruct regarding CVs and online presence before SIWES?',
      ['Update your CV and social media profiles, e.g. LinkedIn, and use a professional email address',
       'Delete all social media accounts to avoid distraction',
       'Wait until after SIWES before writing a CV',
       'Use a single generic CV for every organisation'],
      0,
      'Update your CV and social profiles (e.g. LinkedIn) and use a professional email address.',
      """
### Why this is the answer
Among the things to do **before** SIWES: *"**Update your CV and social media
profiles** (e.g. **LinkedIn**; use a **professional email address**)."*

Three components: the **CV**, the **profiles**, and the **email address**.

### Why the email address earns its own mention
It is the first thing an employer sees when you make contact — and an
unprofessional address undermines every other preparation. It is a small detail
the note singles out deliberately.

### A claim the note rules out
The **12-week action plan** requires *"a CV and LinkedIn profile **tailored to
your goals**"*. A single generic CV is the opposite of tailoring, and it would
also conflict with the instruction to *"make research on the assigned
organisation"*.

### The connected warning
> *"Do not have a **career mismatch**."*

Tailoring your CV to your stated goals, and your goals to the organisation you
researched, is how a mismatch is avoided.

### Source
Day 5 note, "Things to Do Before SIWES" and "Twelve Weeks Action Plan".
"""),

    q('swep_day5_13',
      'Which questions does the lecture give as examples of strategic questions to ask during the first days?',
      ['Who is my supervisor? What is my responsibility? What does success look like?',
       'When is payday? How much leave do I get? Can I work from home?',
       'Who is the highest paid here? Who is likely to be promoted? Who dislikes whom?',
       'Can I skip the logbook? Is attendance compulsory? When can I leave early?'],
      0,
      'Who is my supervisor? What is my responsibility? What does success look like?',
      """
### Why this is the answer
The note states: *"**Ask questions** (career development is a **strategic
effort**). Examples: **Who is my supervisor? What is my responsibility? What
does success look like?**"*

### What makes these strategic
Each one converts uncertainty into something actionable:

| Question | What it establishes |
|---|---|
| **Who is my supervisor?** | Your **reporting line** — also a before-SIWES item |
| **What is my responsibility?** | Your **Role Title** and scope |
| **What does success look like?** | The **standard you will be judged against** |

The third is the most valuable, because without it you can work hard and still
miss what the organisation actually wanted.

### The behaviour the note disqualifies
Those are exactly the enquiries the note's warning targets: *"**Beware of office
politics!** Nobody is your best friend at work."* Asking who dislikes whom is
participating in politics, not avoiding it.

### Source
Day 5 note, "What to Do During the First 4 to 5 Days in SIWES".
"""),

    q('swep_day5_14',
      'The Twelve Weeks Action Plan contains a specific set of instructions. Which of the following is among them?',
      ['Build a job portfolio and document evidence',
       'Change your organisation if the first week is difficult',
       'Delay skill-building until the final two weeks',
       'Focus only on technical skills and ignore soft skills'],
      0,
      'Build a job portfolio and document evidence.',
      """
### Why this is the answer
The **Twelve Weeks Action Plan** lists six instructions:

| # | Instruction |
|---|---|
| 1 | **Set 3-5 goals** |
| 2 | Have a **CV and LinkedIn profile tailored to your goals** |
| 3 | **Build a job portfolio — document evidence** |
| 4 | **Build technical skills** |
| 5 | **Document evidence of skills** |
| 6 | **Close your skill gap**, develop, and improve consistently |

### Note how often documentation appears
**Three** of the six items concern evidence — building the portfolio,
documenting evidence, and documenting evidence *of skills*. This echoes the
learning loop's instruction: *"**Don't just collect tasks, but collate
evidence** (How, when & what). Have a **digital portfolio**."*

Evidence is the single most repeated idea in the entire Day 5 note.

### A claim the note rules out
The ledger records the plan as *"acquiring **both technical and soft skills**"*,
and **Skills to Develop** lists communication, digital literacy, team work,
presentation, work ethics and networking alongside technical acquisition.

### Source
Day 5 note, "Twelve Weeks Action Plan"; handwritten Day 5 ledger.
"""),

    q('swep_day5_15',
      'What does the lecture mean by "collate evidence" rather than "collect tasks"?',
      ['Gather certificates from other organisations to boost your CV',
       'Collect signatures from every staff member you meet',
       'Record how, when and what you did, building a digital portfolio rather than merely completing assignments',
       'Keep copies of the organisation\'s confidential documents as proof'],
      2,
      'Record how, when and what you did, in a digital portfolio.',
      """
### Why this is the answer
The note's instruction is precise: *"**Don't just collect tasks, but collate
evidence** (**How, when & what**). Have a **digital portfolio**. Do not have a
**career mismatch**."*

The three-part bracket is the definition: evidence means recording **how** you
did it, **when**, and **what** it was.

### Task-collecting vs evidence-collating
| Collecting tasks | Collating evidence |
|---|---|
| "I worked in the maintenance unit" | "In week 3, I diagnosed and documented 12 motor faults using X procedure" |
| Unverifiable | **Verifiable** |

That word again — the note's opening promise was converting experience into
**verifiable** skills. The portfolio is the mechanism.

### A seriously wrong approach
It would violate an explicit instruction: *"Always **protect confidential
information**."* Taking an organisation's confidential documents as personal
proof is a breach of the **integrity** employers are said to be watching for.

### Source
Day 5 note, "SIWES Learning Loop".
"""),

    q('swep_day5_16',
      'According to the note, why must a student get a Role Title before or at the start of SIWES?',
      ['To negotiate a higher stipend',
       'To be listed on the organisation\'s payroll',
       'To qualify for ITF reimbursement',
       'To know your responsibility'],
      3,
      'A Role Title establishes what your responsibility is.',
      """
### Why this is the answer
The instruction reads: *"Make sure to get a **Role Title** — **know your
responsibility**."*

### Why this is more than administrative
Without a defined role, a SIWES student drifts into whatever odd jobs happen to
need doing — which produces attendance, not capability. A Role Title:

- anchors the **3 to 5 learning goals** to something concrete
- makes *"What is my responsibility?"* answerable on day one
- gives the **portfolio** a heading under which evidence can accumulate
- guards against the note's own warning: *"Do not have a **career mismatch**."*

### Its neighbours in the checklist
It sits directly beside **"Know your reporting line (i.e. whom to always report
to)"** and **"Meet all ITF requirements for valid participation."** Together
these three define your **position** (role), your **line** (supervisor) and your
**standing** (ITF compliance) — the structural facts you need before work begins.

### Source
Day 5 note, "Things to Do Before SIWES".
"""),

    q('swep_day5_17',
      'Which requirement must a student meet for valid participation in SIWES, as stated in the Day 5 note?',
      ['All NUC accreditation requirements', 'All NECA membership requirements',
       'All COREN registration requirements', 'All ITF requirements'],
      3,
      'Meet all ITF requirements for valid participation.',
      """
### Why this is the answer
The final item under **Things to Do Before SIWES** is: *"**Meet all ITF
requirements for valid participation**."*

### Why it is the ITF specifically
From Day 1: the **Industrial Training Fund (ITF)**, established in **1971** under
**Act No. 47**, is the body that **established SIWES in 1973** and administers
it. Eligibility for allowances depends on ITF documentation — **Logbooks, Form 8
and Form SPE-1**, with adequate vetting of logbooks.

"Valid participation" is therefore a **compliance** matter with the ITF, not an
academic or professional-body matter.

### The other bodies, correctly placed
| Body | Actual role |
|---|---|
| **NUC** | Approved SWEP/SIWES for SET courses; allocated credit units with ITF |
| **COREN** | Will regulate **admissions into engineering programmes** (Day 3) |
| **NECA** | The **employers' association** delivering this very lecture |

Each is real and each appears somewhere in SWEP — but only the **ITF** governs
participation validity.

### Source
Day 5 note, "Things to Do Before SIWES"; cross-referenced with Day 1 material.
"""),

    q('swep_day5_18',
      'Which of the following pairs a Day 5 instruction with the correct section of the note?',
      ['"Protect confidential information" — Things to Do Before SIWES',
       '"Prepare your professional wardrobe" — What to Do During the First 4 to 5 Days',
       '"Reflect" — SIWES Learning Loop',
       '"Networking skills" — What Employers Notice'],
      2,
      '"Reflect" is the fourth stage of the SIWES Learning Loop.',
      """
### Why this is the answer
Each option places an instruction in a section, and only one is correct:

| Instruction | Correct section |
|---|---|
| Protect confidential information | **During the first 4 to 5 days** |
| Prepare your professional wardrobe | **Before SIWES** |
| **Reflect** | **SIWES Learning Loop** ✓ |
| Networking skills | **Skills to Develop** |

### Why this question is worth asking
The Day 5 note is short but densely sectioned — **seven** headings across three
pages, with overlapping vocabulary. A student who reads it as one continuous list
will know all the content and still fail placement questions like this one.

### The seven sections, in order
1. Core Concepts of SIWES
2. Mindset Shift
3. Things to Do Before SIWES
4. What to Do During the First 4 to 5 Days
5. What Employers Notice, Observe, or Expect
6. SIWES Learning Loop
7. Skills to Develop → Twelve Weeks Action Plan

Notice the **chronological logic**: concepts → mindset → before → first days →
what is watched → how to learn → what to build.

### Source
Day 5 note, all sections.
"""),

    q('swep_day5_19',
      'What does the note say about dressing, both before and during SIWES?',
      ['Casual dressing is acceptable once you are known in the office',
       'Uniforms are provided by the ITF for all SIWES students',
       'Dress code depends entirely on the organisation and needs no preparation',
       'Prepare a professional wardrobe beforehand and dress appropriately during the attachment; avoid casual dressing'],
      3,
      'Prepare a professional wardrobe beforehand; dress appropriately throughout.',
      """
### Why this is the answer
Dressing appears **twice**, once in each phase:

| Phase | Instruction |
|---|---|
| **Before SIWES** | *"**Prepare your professional wardrobe**; **avoid casual dressing**."* |
| **First 4 to 5 days** | *"Keep a daily learning record and **dress appropriately**."* |

The handwritten ledger also lists **"dressing professionally"** among the
pre-SIWES preparations.

### Why it is treated as preparation, not improvisation
A professional wardrobe is something you **assemble in advance** — which is why
it sits in the *before* list. Turning up on day one intending to sort it out
later is exactly the failure the instruction anticipates.

### How it connects to the rest
Dress feeds **Professionalism**, one of the six things **employers notice**, and
it is a visible marker of the **mindset shift** — a *professional in training*
presents as one. It costs nothing in skill and is judged immediately.

### Source
Day 5 note, "Things to Do Before SIWES" and "What to Do During the First 4 to 5
Days"; handwritten Day 5 ledger.
"""),

    q('swep_day5_20',
      'The Day 5 ledger summarises the session in three parts. Which is NOT one of them?',
      ['Employer expectations and mindset shift from fresh graduates in the 21st century',
       'Workplace conduct and protocols',
       'Skill acquisition and action plan',
       'Salary negotiation and contract law'],
      3,
      'Salary negotiation and contract law is not part of the Day 5 summary.',
      """
### Why this is the answer
A **NOT** question. The Day 5 ledger records three parts:

| Part | Content |
|---|---|
| **Employer Expectations & Mindset Shift** | Transitioning from a student mindset to a *"professional in training"* to build **verifiable skills and networks**; pre-SIWES preparations — researching the assigned organisation, updating **CVs and LinkedIn**, defining learning goals, dressing professionally |
| **Workplace Conduct & Protocols** | Essential steps for the first few days — **active observation**, asking **strategic questions** about responsibilities, maintaining **confidentiality**; key traits employers expect — **punctuality, integrity, team work**, and the ability to **navigate office politics** |
| **Skill Acquisition & Action Plan** | The **SIWES learning loop** (observe, practice, document, reflect) to convert daily activities into **tangible capabilities** rather than just completing tasks; a **12-week action plan** on closing skill gaps, creating a **digital portfolio**, and acquiring **both technical and soft skills** |

**Salary negotiation and contract law** appears nowhere — neither in the ledger
nor in the note itself.

### Why its absence is consistent
The lecture's premise is that SIWES is about **building verifiable skills and
networks**, not terms of employment. The note never discusses pay at all.

### Source
Handwritten "Record of the Orientation Week Activities", Day 5.
"""),

    q('swep_day5_21',
      'According to the ledger, what is the purpose of the SIWES learning loop?',
      ['To fill the logbook with as many completed tasks as possible',
       'To convert daily activities into tangible capabilities rather than just completing tasks',
       'To reduce the number of hours spent at the organisation',
       'To allow students to rotate between multiple organisations'],
      1,
      'To convert daily activities into tangible capabilities, not just completed tasks.',
      """
### Why this is the answer
The ledger states it directly: the loop — *"**observe, practice, document,
reflect**"* — exists *"to **convert daily activities into tangible capabilities
rather than just completing tasks**."*

The note puts the same idea in its own words: *"**Don't just collect tasks, but
collate evidence**."*

### Task versus capability
| Completing tasks | Building capability |
|---|---|
| Measured in **activity** | Measured in **what you can now do** |
| Ends when the task ends | **Persists** beyond the placement |
| Fills a logbook | Fills a **portfolio** |

Collecting tasks is the precise failure mode the loop is designed to prevent — a full
logbook and an empty portfolio.

### The vocabulary to notice
Three related words run through Day 5: **verifiable** skills (core concept),
**evidence** (learning loop), **tangible** capabilities (ledger). All three
insist the same thing — the outcome must be demonstrable to someone else.

### Source
Handwritten Day 5 ledger; Day 5 note, "SIWES Learning Loop".
"""),

    q('swep_day5_22',
      'Which statement best captures what the lecture says about asking questions during SIWES?',
      ['Ask only when absolutely necessary to avoid appearing ignorant',
       'Career development is a strategic effort — ask questions, and always ask questions',
       'Direct all questions to fellow students rather than supervisors',
       'Submit all questions in writing at the end of the programme'],
      1,
      'Career development is a strategic effort — ask questions, always.',
      """
### Why this is the answer
The note treats questioning as central, stating it **twice** within the
first-days section:

- *"**Ask questions** (**career development is a strategic effort**)."*
- *"Always protect confidential information and **always ask questions**."*

### Where else it appears
| Location | How questioning features |
|---|---|
| **Learning loop** | Stage 2 is *"**Ask questions** / Practice"* |
| **Employers notice** | Communication is defined as *"listening and **asking questions**"* |
| **First days** | Three sample **strategic questions** are supplied |

Four separate sections, one behaviour. That density is the strongest possible
signal of what the lecture wants students to take away.

### Why "strategic" is the key adjective
It reframes asking from a confession of ignorance — that alternative's assumption — into
a **deliberate career tactic**. The sample questions prove the point: *"What
does success look like?"* is not ignorance, it is target-setting.

### Source
Day 5 note, "What to Do During the First 4 to 5 Days", "SIWES Learning Loop" and
"What Employers Notice".
"""),

    q('swep_day5_23',
      'The note instructs students to close a particular gap during the twelve weeks. What gap?',
      ['The attendance gap', 'The generation gap',
       'The salary gap', 'The skill gap'],
      3,
      'Close your skill gap, develop and improve consistently.',
      """
### Why this is the answer
The final item of the **Twelve Weeks Action Plan** reads: *"**Close your skill
gap**, develop, and improve consistently."*

The ledger repeats it: the 12-week plan is *"focused on **closing skill gaps**,
creating a digital portfolio, and acquiring both technical and soft skills."*

### Why a "gap" framing is used
It presupposes you have **identified** one — which is only possible if you have
first defined **3 to 5 learning goals** and know what **success looks like** in
your role. The gap is the distance between your current capability and those
targets.

That is why closing it is the **last** instruction: it depends on goal-setting
(item 1), tailoring (item 2), portfolio-building (item 3) and skill-building
(items 4-5) having already happened.

### Note the closing words
*"...develop, and **improve consistently**."* Not once, not at the end —
consistently across the twelve weeks. The loop is meant to run repeatedly, which
is exactly why it is called a **loop**.

### Source
Day 5 note, "Twelve Weeks Action Plan"; handwritten Day 5 ledger.
"""),

    q('swep_day5_24',
      'What does the lecture mean by warning students not to have a "career mismatch"?',
      ['Do not accept a placement in a different state from your university',
       'Do not change your course of study after SIWES',
       'Do not apply to more than one organisation at a time',
       'Do not allow your documented experience and portfolio to diverge from the career direction you intend to pursue'],
      3,
      'Do not let your experience and evidence diverge from your intended career direction.',
      """
### Why this is the answer
The warning appears at the close of the **SIWES Learning Loop**, immediately
after the instruction to collate evidence and keep a **digital portfolio**:
*"Have a digital portfolio. **Do not have a career mismatch**."*

Its placement is the clue. It is about **alignment between what you document and
where you are going**.

### What alignment looks like in the note
| Instruction | How it prevents mismatch |
|---|---|
| **Make research on the assigned organisation** | Know what the placement can offer |
| **Define 3 to 5 learning goals** | Decide what you intend to gain |
| **CV and LinkedIn tailored to your goals** | Present a coherent direction |
| **Build a portfolio — document evidence** | Accumulate proof pointing the same way |
| **Close your skill gap** | Correct the distance to your target |

A mismatch is what happens when twelve weeks of evidence points somewhere you
never intended to go.

### Why the alternatives miss
None concerns direction. Geography, application volume and course changes are
not discussed anywhere in the note.

### Source
Day 5 note, "SIWES Learning Loop", read against "Things to Do Before SIWES" and
the "Twelve Weeks Action Plan".
"""),

    q('swep_day5_25',
      'Which two skills appear on BOTH the "what employers notice" list and the "skills to develop" list?',
      ['Punctuality and integrity', 'Initiative and professionalism',
       'Digital literacy and networking', 'Communication and team work'],
      3,
      'Communication and team work appear on both lists.',
      """
### Why this is the answer
Laying the two lists side by side:

| What employers notice | Skills to develop |
|---|---|
| Punctuality | Technical skills acquisition |
| **Communication** | **Communication skills** |
| Initiative | Digital literacy |
| **Team work** | **Team work** |
| Professionalism | Speaking / Presentation skills |
| Integrity | Work ethics |
| — | Networking skills |

Only **communication** and **team work** appear on both.

### Why those two specifically
They are the only entries that are simultaneously a **trainable capability** and
an **observable behaviour**. You can be taught to communicate better, and an
employer can watch you do it. Punctuality is observed but not trained as a
skill; digital literacy is trained but not what the note lists as observed.

### How the note qualifies each
- **Communication** is glossed as *"listening and asking questions"*
- **Team work** is glossed as *"supporting colleagues"*

Both definitions describe **conduct toward other people** — which is why they
straddle the two lists.

### Source
Day 5 note, "What Employers Notice, Observe, or Expect" and "Skills to Develop".
"""),

    q('swep_day5_26',
      'How does the lecture characterise career development, in the phrase used in the note?',
      ['A matter of luck and timing', 'A strategic effort',
       'The responsibility of the employer alone', 'An activity best begun after graduation'],
      1,
      'Career development is a strategic effort.',
      """
### Why this is the answer
The phrase appears as a parenthetical justification for asking questions:
*"Ask questions (**career development is a strategic effort**)."*

### Why the word "strategic" carries the note
It frames the entire Day 5 message as **deliberate action rather than passive
progression**. Every instruction in the note is an instance of strategy:

| Instruction | The strategy behind it |
|---|---|
| Research the organisation **before** arriving | Prepare, don't react |
| Define **3-5 goals** | Choose outcomes in advance |
| Ask *"what does success look like?"* | Learn the standard early |
| **Document evidence** | Build proof deliberately |
| **Close your skill gap** | Correct course intentionally |

### The contrast with that alternative
The note's premise is the opposite — career development begins **during** SIWES,
in the second year of study, not after graduation. That is why there is a
twelve-week action plan rather than post-graduation advice.

Day 2's employability lecture made the same argument: *"An employable person
must learn how to **manage his/her career early**."*

### Source
Day 5 note, "What to Do During the First 4 to 5 Days in SIWES".
"""),

    q('swep_day5_27',
      'Which of these is explicitly listed among the "Things to Do Before SIWES"?',
      ['Negotiate your monthly allowance with the organisation',
       'Complete your final year project proposal',
       'Request a change of supervisor if unsatisfied',
       'Have a daily routine, prepare notebooks and necessary documents'],
      3,
      'Have a daily routine, prepare notebooks and necessary documents.',
      """
### Why this is the answer
The complete before-SIWES checklist is:

| # | Task |
|---|---|
| 1 | Make **research** on the assigned organisation |
| 2 | Update your **CV and social media profiles** (LinkedIn; professional email) |
| 3 | Define **3 to 5 learning goals** |
| 4 | Prepare your **professional wardrobe**; avoid casual dressing |
| 5 | **Have a daily routine, prepare notebooks and necessary documents** |
| 6 | Know your **reporting line** |
| 7 | Get a **Role Title** — know your responsibility |
| 8 | Meet all **ITF requirements** for valid participation |

### Why the notebook matters more than it looks
It is the physical precondition for the **daily learning record** kept during the
first days, and ultimately for the **portfolio**. The note's logic is sequential:
prepare the notebook *before*, fill it *during*, convert it to evidence *after*.

The **daily routine** serves **punctuality** — the first trait employers are
said to notice.

### Why the others are absent
Allowances are never discussed in this note. Changing supervisors contradicts
*"know your reporting line"*. Final-year projects are outside the scope of a
200-level industrial attachment.

### Source
Day 5 note, "Things to Do Before SIWES".
"""),

    q('swep_day5_28',
      'What does the note identify as the two things SIWES is FOR, taken together?',
      ['Earning a stipend and fulfilling a graduation requirement',
       'Building verifiable skills and building human networks',
       'Observing professionals and avoiding responsibility',
       'Testing career options and taking a break from study'],
      1,
      'Verifiable skills and human networks.',
      """
### Why this is the answer
The two **Core Concepts of SIWES** state exactly this:

1. *"SIWES is not just an industrial training or a means of escape from academic
   activities, but a period to gain experience that should be converted into
   **verifiable skills** in order to guarantee employability."*
2. *"The SIWES period is for **building human networks**, as network brings good
   net worth."*

The handwritten ledger compresses both into one phrase: *"to build **verifiable
skills and networks**."*

### How the rest of the note serves these two purposes
| Purpose | Served by |
|---|---|
| **Verifiable skills** | Learning loop · digital portfolio · document evidence · close the skill gap · technical + soft skills |
| **Human networks** | LinkedIn profile · networking skills · introduce yourself properly · knowing your reporting line |

Every section of the note attaches to one or the other. That is the structure
beneath what looks like a list of tips.

### The view the note explicitly rejects
*"Not just an industrial training or a **means of escape from academic
activities**"* — the note names and denies the low view of SIWES before offering
the right one.

### Source
Day 5 note, "Core Concepts of SIWES"; handwritten Day 5 ledger.
"""),

    q('swep_day5_29',
      'Which trait, listed among what employers notice, is glossed in the note as "supporting colleagues"?',
      ['Initiative', 'Integrity', 'Team work', 'Professionalism'],
      2,
      'Team work is glossed as supporting colleagues.',
      """
### Why this is the answer
The note attaches a short gloss to two of the six traits:

| Trait | Gloss given |
|---|---|
| Punctuality | — |
| **Communication** | *(listening and asking questions)* |
| Initiative | — |
| **Team work** | ***(supporting colleagues)*** |
| Professionalism | — |
| Integrity | — |

Only **communication** and **team work** are defined — and, tellingly, those are
the same two that reappear under **Skills to Develop**.

### What the gloss tells you
"Supporting colleagues" frames team work as **contribution to others**, not mere
participation in a group. Day 2's employability lecture made the identical
point: *"The important thing is to learn how to **contribute without always
needing to dominate**."*

### Why the glosses exist at all
The other four traits — punctuality, initiative, professionalism, integrity —
are self-explanatory. Communication and team work are vague enough to be
misunderstood, so the note pins them down.

### Source
Day 5 note, "What Employers Notice, Observe, or Expect".
"""),

    q('swep_day5_30',
      'Taken together, how many weeks does the Day 5 action plan cover, and how many goals should it contain?',
      ['8 weeks and 3-5 goals', '12 weeks and 3-5 goals',
       '12 weeks and 6-8 goals', '24 weeks and 3-5 goals'],
      1,
      'A twelve-week plan containing 3 to 5 goals.',
      """
### Why this is the answer
The section is titled **"Twelve Weeks Action Plan"**, and its first instruction
is **"Set 3-5 goals."** The ledger confirms: *"Concluded with a **12-week action
plan**."*

### Why twelve weeks, cross-referenced with Day 1
Day 1 established the programme durations:

| Module | Duration |
|---|---|
| **SWEP 200** | **12 weeks ideal** (minimum 8) |
| SIWES I | 12 weeks |
| SIWES II | 24 weeks (6 months) |

The twelve-week plan matches the **ideal SWEP 200 duration** exactly — it is
built for the attachment students are about to begin, not a generic timeframe.

### A real trap in the numbers
**24 weeks** is genuine — but it is **SIWES II**, the 400-level module, and the
only one that attracts ITF stipends. Wrong module, wrong year.

### The three Day 5 numbers, once more
**3-5** goals · **4-5** first days · **12** weeks.

### Source
Day 5 note, "Twelve Weeks Action Plan"; handwritten Day 5 ledger;
cross-referenced with Day 1 durations.
"""),

    q('swep_day5_31',
      'Which instruction about confidentiality does the note give?',
      ['Share all findings openly to demonstrate transparency',
       'Always protect confidential information',
       'Publish your daily learning record on social media',
       'Confidentiality applies only to senior staff, not SIWES students'],
      1,
      'Always protect confidential information.',
      """
### Why this is the answer
Among the first-days instructions: *"**Always protect confidential information**
and always ask questions."*

The ledger lists the same duty among workplace conduct essentials: *"maintaining
**confidentiality**."*

### Note the pairing in the sentence
Protecting information and asking questions appear in **one sentence**, joined by
"and". They are not in tension — you are expected to be **inquisitive about your
work** and **discreet about the organisation's information** at the same time.

### How it connects to integrity
**Integrity** is one of the six traits employers notice, and confidentiality is
its most testable form during a placement. A student who leaks information has
demonstrated the opposite of the trait being watched for.

### A genuine modern risk
The note requires a **daily learning record** and a **digital portfolio** — both
involve writing down what you did. The confidentiality instruction sets the
boundary: document **your learning**, not the organisation's protected
information. That distinction is what the "How, when & what" of evidence is
meant to capture.

### Source
Day 5 note, "What to Do During the First 4 to 5 Days"; handwritten Day 5 ledger.
"""),

    q('swep_day5_32',
      'Which of the following is NOT listed among the seven "Skills to Develop"?',
      ['Digital literacy', 'Speaking / Presentation skills',
       'Financial accounting skills', 'Work ethics'],
      2,
      'Financial accounting is not among the seven skills to develop.',
      """
### Why this is the answer
A **NOT** question. The seven skills are:

| # | Skill |
|---|---|
| 1 | Technical skills acquisition |
| 2 | Communication skills |
| 3 | **Digital literacy** |
| 4 | Team work |
| 5 | **Speaking / Presentation skills** |
| 6 | **Work ethics** |
| 7 | Networking skills |

**Financial accounting** appears nowhere in the Day 5 note.

### The composition worth noticing
Only **one** of the seven — technical skills acquisition — is technical. The
other six are **soft or transferable**. That balance is deliberate, and the
ledger confirms the intent: acquiring *"both **technical and soft skills**."*

It also echoes Day 2, where **communication** was called *"perhaps the most
fundamental employability skill"* and the warning ran: *"A highly intelligent
person who cannot communicate effectively may struggle in the workplace."*

### Source
Day 5 note, "Skills to Develop".
"""),

    q('swep_day5_33',
      'What does the note say a student should do from day one of the attachment?',
      ['Begin submitting reports to the ITF immediately',
       'Observe, listen, and introduce yourself properly to the audience',
       'Request a written job description before starting work',
       'Identify who holds informal power in the office'],
      1,
      'Observe, listen and introduce yourself properly.',
      """
### Why this is the answer
The first bullet of the first-days section reads: *"**From day one: Observe,
listen, and introduce yourself properly** to the audience."*

Three actions, and the order is meaningful — **observe** and **listen** come
before you speak, but introducing yourself is still a day-one duty, not something
to postpone.

### How it maps to the learning loop
The loop's first stage is **Observe**, and the ledger calls it *"**active
observation**"* — not passive watching. Day one begins the loop immediately.

### The behaviour the note disqualifies
Identifying informal power is office politics — precisely what the note warns
against: *"**Beware of office politics!** Nobody is your best friend at work."*

### Why that alternative misses
Knowing your **Role Title** and **reporting line** are *before*-SIWES tasks. By
day one you should already have them; asking then would mean the preparation was
skipped.

### Source
Day 5 note, "What to Do During the First 4 to 5 Days in SIWES"; handwritten
Day 5 ledger.
"""),

    q('swep_day5_34',
      'Which pairing of a Day 5 concept with its correct description is accurate?',
      ['Learning loop — a list of six traits employers look for',
       'Twelve weeks action plan — the four stages of observing and reflecting',
       'Digital portfolio — documented evidence of how, when and what you did',
       'Reporting line — the 3 to 5 goals you set for the programme'],
      2,
      'A digital portfolio holds documented evidence — how, when and what.',
      """
### Why this is the answer
Each option attaches a real Day 5 term to a description belonging to a different
one. The correct definitions are:

| Term | What it actually is |
|---|---|
| **SIWES Learning Loop** | Four stages: **observe → ask questions/practice → document → reflect** |
| **Twelve Weeks Action Plan** | Six instructions: goals, tailored CV/LinkedIn, portfolio, technical skills, documented evidence, close the skill gap |
| **Digital portfolio** | **Documented evidence — how, when and what** you did |
| **Reporting line** | **Whom you always report to** |

Only the digital-portfolio pairing is correct.

### Why the portfolio is the centre of Day 5
It is where the note's two demands converge: **verifiable** skills need
**evidence**, and evidence needs somewhere to live. The note mentions
documentation in the learning loop *and* twice more in the action plan —
**three** separate instructions pointing at one artefact.

The ledger agrees: the plan focuses on *"closing skill gaps, **creating a digital
portfolio**, and acquiring both technical and soft skills."*

### Source
Day 5 note, "SIWES Learning Loop", "Twelve Weeks Action Plan" and "Things to Do
Before SIWES".
"""),

    q('swep_day5_35',
      'According to the note, what should a student research before the attachment begins?',
      ['The salaries paid by competing organisations',
       'The assigned organisation', 'The examination timetable for the next session',
       'The personal backgrounds of the staff'],
      1,
      'Research the assigned organisation.',
      """
### Why this is the answer
The very first item under **Things to Do Before SIWES** is: *"**Make research on
the assigned organisation**."*

The ledger lists it first too: pre-SIWES preparations include *"**researching
assigned organisations**, updating CVs and LinkedIn profiles, defining learning
goals, and dressing professionally."*

### Why it comes first
Everything downstream depends on it. You cannot set meaningful **3-5 learning
goals** without knowing what the organisation actually does, and you cannot
**tailor a CV to your goals** without knowing which of your capabilities are
relevant to it. Research is the input to the entire preparation sequence.

### It also guards against the note's own warning
*"Do not have a **career mismatch**."* Researching the organisation before
arriving is the earliest opportunity to notice a mismatch — while something can
still be done about it.

### A claim the note rules out
Researching **staff backgrounds** rather than the organisation edges toward the
personal, which sits badly with the office-politics warning. The note directs
attention at the **institution**, not individuals.

### Source
Day 5 note, "Things to Do Before SIWES"; handwritten Day 5 ledger.
"""),

    q('swep_day5_36',
      'Which statement about the Day 5 lecture\'s view of tasks versus capabilities is correct?',
      ['Completing many tasks is the primary measure of a successful SIWES',
       'Tasks and capabilities are the same thing in an industrial setting',
       'Daily activities should be converted into tangible capabilities rather than merely being completed',
       'Capabilities matter only after the twelve weeks have ended'],
      2,
      'Daily activities should be converted into tangible capabilities.',
      """
### Why this is the answer
The ledger states the purpose of the learning loop as converting *"daily
activities into **tangible capabilities** rather than just completing tasks."*

The note gives the same instruction in its own register: *"**Don't just collect
tasks, but collate evidence** (How, when & what)."*

### Task vs capability
| | Task | Capability |
|---|---|---|
| **Measured by** | Activity completed | What you can now **do** |
| **Ends** | When the task ends | **Persists** beyond the placement |
| **Shown by** | A full logbook | A **portfolio** |
| **Verifiable?** | Not by itself | **Yes** — with evidence |

### Why this echoes Day 2
Prof. Ekanola drew the identical distinction between a **skill** (performing a
task) and a **capability** (applying knowledge in changing circumstances), and
insisted *"**experience converts knowledge into competence**."* Day 5 supplies
the mechanism — the loop — by which that conversion actually happens during an
attachment.

### A claim the note rules out
The conversion must happen **during** the twelve weeks, through the loop run
repeatedly. Waiting until the end leaves you with undocumented memories.

### Source
Handwritten Day 5 ledger; Day 5 note, "SIWES Learning Loop".
"""),

    q('swep_day5_37',
      'The note lists both technical and non-technical development. Which item represents the technical strand?',
      ['Work ethics', 'Networking skills',
       'Technical skills acquisition', 'Speaking / presentation skills'],
      2,
      'Technical skills acquisition is the technical strand.',
      """
### Why this is the answer
Of the seven **Skills to Develop**, only **technical skills acquisition** is
technical. The remaining six — communication, digital literacy, team work,
speaking/presentation, work ethics, networking — are soft or transferable.

### Where it reappears
The **Twelve Weeks Action Plan** dedicates two of its six items to this strand:
- *"**Build technical skills**"*
- *"**Document evidence of skills**"*

And the ledger closes with *"acquiring **both technical and soft skills**."*

### The balance being struck
| Strand | Count in the list |
|---|---|
| Technical | **1 of 7** |
| Soft / transferable | **6 of 7** |

That ratio is not an oversight. Employers, per this lecture, take technical
competence as the entry ticket and then judge on **punctuality, communication,
initiative, team work, professionalism and integrity** — five of which are not
technical at all.

### Source
Day 5 note, "Skills to Develop" and "Twelve Weeks Action Plan"; handwritten
Day 5 ledger.
"""),

    q('swep_day5_38',
      'What does the note instruct regarding the CV and LinkedIn profile within the twelve-week plan?',
      ['Have a CV and LinkedIn profile tailored to your goals',
       'Keep them unchanged until after graduation',
       'Replace the CV entirely with a video introduction',
       'Maintain separate profiles for each supervisor'],
      0,
      'Have a CV and LinkedIn profile tailored to your goals.',
      """
### Why this is the answer
The second instruction of the **Twelve Weeks Action Plan** is: *"Have a **CV and
LinkedIn profile tailored to your goals**."*

### Note that this is the second mention
It appeared first under **Things to Do Before SIWES** — *"Update your CV and
social media profiles (e.g. LinkedIn; use a professional email address)"* — and
returns here in the action plan.

The difference between the two mentions is the crucial part:

| Stage | Instruction |
|---|---|
| **Before SIWES** | **Update** them |
| **During the 12 weeks** | **Tailor** them **to your goals** |

Updating is housekeeping; **tailoring** is strategy. The note escalates from one
to the other once your **3-5 goals** exist to tailor toward.

### Why it belongs in the plan rather than the preparation list
A tailored profile depends on goals you have set and evidence you have
accumulated. It is therefore a **living document** revised across the twelve
weeks, not a one-off task ticked off beforehand.

### Source
Day 5 note, "Twelve Weeks Action Plan" and "Things to Do Before SIWES".
"""),

    q('swep_day5_39',
      'Which Day 5 numerical detail is correctly stated?',
      ['Define 5 to 8 learning goals; the first 4 to 5 days are critical; a 12-week action plan',
       'Define 3 to 5 learning goals; the first 4 to 5 days are critical; a 12-week action plan',
       'Define 3 to 5 learning goals; the first 2 weeks are critical; an 8-week action plan',
       'Define 3 to 5 learning goals; the first 4 to 5 days are critical; a 24-week action plan'],
      1,
      '3 to 5 goals, the first 4 to 5 days, and a 12-week plan.',
      """
### Why this is the answer
Day 5 contains exactly three numbers, and only that alternative states all of them
correctly:

| Detail | Correct value | Where stated |
|---|---|---|
| **Learning goals** | **3 to 5** | Before SIWES; repeated in the action plan |
| **Critical first period** | **First 4 to 5 days** | Section heading |
| **Action plan** | **Twelve weeks** | Section heading; confirmed by the ledger |

### How each distractor breaks
- **A** — inflates the goals to *5 to 8*.
- **C** — stretches the first days to *2 weeks* and shortens the plan to *8
  weeks*. Note that **8 weeks** is real, but it is the **minimum SWEP 200
  duration** from Day 1, not the plan length.
- **D** — uses **24 weeks**, which is genuine but belongs to **SIWES II**, the
  400-level module.

### The pattern across the week
As on Day 4, every wrong figure is a **real SWEP number borrowed from elsewhere**
— 8 weeks from the SWEP minimum, 24 weeks from SIWES II. With statistics, the
danger is always the number you have seen in a different place.

### Keep them straight
**Goals 3-5 · Days 4-5 · Weeks 12.**

### Source
Day 5 note, all sections; handwritten Day 5 ledger; cross-referenced with Day 1
durations.
"""),

    q('swep_day5_40',
      'Which summary best captures the overall message of the Day 5 session?',
      ['SIWES is a formality to be completed with minimum effort before final year',
       'Shift from a student mindset to a professional in training, convert daily activity into verifiable skills and evidence, and build networks over a structured twelve weeks',
       'Focus exclusively on technical competence, since employers judge nothing else',
       'Rely on the organisation to direct your learning, since goals are set by supervisors'],
      1,
      'Shift mindset, convert activity into verifiable skills and evidence, and build networks.',
      """
### Why this is the answer
Every element of that alternative is stated in the source:

| Element | Where it comes from |
|---|---|
| **Shift from student to professional in training** | Mindset Shift; ledger |
| **Convert activity into verifiable skills** | Core Concepts; learning loop |
| **Evidence** | *"Collate evidence (How, when & what)"*; digital portfolio |
| **Build networks** | *"Network brings good net worth"*; networking skills |
| **Structured twelve weeks** | Twelve Weeks Action Plan |

### Why each distractor is explicitly contradicted
| Claim | The note's actual position |
|---|---|
| A formality, minimum effort | *"**Not just** an industrial training or a **means of escape** from academic activities"* |
| Technical competence only | Six of seven skills are soft; employers notice punctuality, communication, initiative, team work, professionalism, integrity |
| Supervisors set your goals | *"**Define 3 to 5 learning goals**"* — yours to set; *"career development is a **strategic effort**"* |

### The single sentence that holds it together
> *"You are being **equipped to create value and build evidence**."*

Create value — that is the networks and the contribution. Build evidence — that
is the portfolio and the verifiable skills. Day 5 is those two instructions,
expanded.

### Source
Day 5 note, all sections; handwritten Day 5 ledger.
"""),
]

assert len(QUESTIONS) == 40, f'expected 40, got {len(QUESTIONS)}'
_ids = [x['id'] for x in QUESTIONS]
assert len(set(_ids)) == 40, 'duplicate ids'
for _q in QUESTIONS:
    assert len(_q['options']) == 4, f"{_q['id']}: needs 4 options"
    assert 0 <= _q['correct'] < 4, f"{_q['id']}: bad correct index"
    assert _q['short'] and _q['solution'], f"{_q['id']}: missing short/solution"
