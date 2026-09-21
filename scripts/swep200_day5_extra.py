#!/usr/bin/env python3
"""SWEP 200 — Day 5 extra 20 questions."""

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
    q('swep_day5_41',
      "According to Day 5 NECA lecture, what is SIWES not, and what should it be converted into?",
      ['SIWES is not an escape from academics — it is a period to convert experience into verifiable skills that guarantee employability',
       'SIWES is an escape from academics with no skills',
       'SIWES is only for collecting tasks',
       'SIWES is only for vacation'],
      0,
      'SIWES is not escape from academics — convert experience into verifiable skills for employability.',
      """
### Why this is the answer
Core Concepts slide: \"SIWES is **not** an escape from academics — it is a period to convert experience into **verifiable skills** that guarantee **employability**\" It is for building human networks — network brings good net worth.

### Source
NECA representative, SWEP Day 5.

### Why the others fail
Escape with no skills, only collecting tasks, only vacation contradict verifiable skills purpose.
"""),

    q('swep_day5_42',
      "What mindset shift does NECA lecture urge?",
      ['See yourself as a professional in training, not a mere student — you are being equipped to create value and build evidence',
       'See yourself as only a student with no professional responsibility',
       'See yourself as a visitor with no value creation',
       'See yourself as unemployed with no future'],
      0,
      'See yourself as professional in training, not mere student — create value and build evidence.',
      """
### Why this is the answer
Mindset Shift slide: \"See yourself as a **professional in training**, not a mere student — you are being equipped to **create value and build evidence**\"

### Source
NECA Day 5.

### Why the others fail
Only student, visitor, unemployed miss professional in training mindset.
"""),

    q('swep_day5_43',
      "What are the three numbers in NECA lecture and what they count?",
      ['3 to 5 learning goals, 4 to 5 days critical first period, 12 weeks action plan',
       '1 to 2 goals, 1 day, 2 weeks',
       '10 goals, 10 days, 10 weeks',
       '3 goals, 3 days, 3 weeks'],
      0,
      '3-5 learning goals, 4-5 days critical first period, 12 weeks action plan.',
      """
### Why this is the answer
The three numbers slide:
| Number | What it counts |
| **3 to 5** | Learning goals |
| **4 to 5** | Days in critical first period |
| **12** | Weeks in action plan |

### Source
NECA Day 5.

### Why the others fail
1-2, 10, 3 only miss the specific ranges.
"""),

    q('swep_day5_44',
      "What should be done before SIWES according to NECA lecture?",
      ['Research assigned organisation, update CV and LinkedIn (professional email), define 3–5 learning goals, prepare professional wardrobe, daily routine, notebooks, documents, know reporting line, get Role Title, meet ITF requirements',
       'Do nothing before SIWES',
       'Only prepare wardrobe and ignore organisation research',
       'Only update CV and ignore learning goals'],
      0,
      'Research organisation, update CV/LinkedIn professional email, define 3-5 goals, prepare wardrobe, routine, notebooks, reporting line, Role Title, ITF requirements.',
      """
### Why this is the answer
Things to Do Before SIWES slide lists all those items.

### Source
NECA Day 5.

### Why the others fail
Do nothing, only wardrobe, only CV miss comprehensive before-SIWE S checklist.
"""),

    q('swep_day5_45',
      "What should be done during first 4 to 5 days in SIWES?",
      ['From day one observe, listen, introduce yourself properly, ask questions (Who is my supervisor? What is my responsibility? What does success look like?), keep daily learning record, dress appropriately, protect confidential information',
       'From day one sleep and ignore supervisor',
       'From day one argue with colleagues',
       'From day one avoid asking questions'],
      0,
      'Observe, listen, introduce properly, ask supervisor/responsibility/success questions, keep daily learning record, dress appropriately, protect confidential info.',
      """
### Why this is the answer
What to Do During First 4-5 Days slide: \"From day one: Observe, listen, and introduce yourself properly to the audience. Ask questions (career development is strategic effort). Examples: Who is my supervisor? What is my responsibility? What does success look like? Keep a daily learning record and dress appropriately. Always protect confidential information and always ask questions.\"

### Source
NECA Day 5.

### Why the others fail
Sleep, argue, avoid questions contradict observe/listen/ask guidance.
"""),

    q('swep_day5_46',
      "What are the six things employers notice, observe, or expect?",
      ['Punctuality, Communication (listening and asking questions), Initiative, Team work (supporting colleagues), Professionalism, Integrity — Beware of office politics! Nobody is your best friend at work',
       'Only punctuality',
       'Only communication',
       'Only integrity'],
      0,
      'Punctuality, Communication, Initiative, Team work, Professionalism, Integrity — beware office politics.',
      """
### Why this is the answer
What Employers Notice slide lists 6: Punctuality, Communication (listening and asking questions), Initiative, Team work (supporting colleagues), Professionalism, Integrity. Note: Beware of office politics! Nobody is your best friend at work.

### Source
NECA Day 5.

### Why the others fail
Only one trait misses other five and office politics warning.
"""),

    q('swep_day5_47',
      "What is the SIWES Learning Loop?",
      ['Observe → Ask questions / Practice → Document experiences → Reflect — Don’t just collect tasks, but collate evidence (How, when & what), have digital portfolio, do not have career mismatch',
       'Only observe and do nothing else',
       'Only practice without documentation',
       'Only reflect without observing'],
      0,
      'Observe → Ask/Practice → Document → Reflect — collate evidence How/when/what, digital portfolio, avoid career mismatch.',
      """
### Why this is the answer
SIWES Learning Loop slide: \"Observe → Ask questions / Practice → Document experiences → Reflect Note: Don’t just collect tasks, but collate evidence (How, when & what). Have a digital portfolio. Do not have a career mismatch.\"

### Source
NECA Day 5.

### Why the others fail
Only one stage misses loop and evidence collation message.
"""),

    q('swep_day5_48',
      "What are the seven skills to develop according to NECA?",
      ['Technical skills acquisition, communication, digital literacy, team work, speaking/presentation, work ethics, networking — only one is technical, rest soft/transferable',
       'Only technical skills',
       'Only communication',
       'Only networking'],
      0,
      'Technical, communication, digital literacy, teamwork, speaking/presentation, work ethics, networking — only one technical.',
      """
### Why this is the answer
Skills to Develop slide lists 7: Technical skills acquisition, communication, digital literacy, team work, speaking/presentation, work ethics, networking. Only one is technical — rest are soft/transferable.

### Source
NECA Day 5.

### Why the others fail
Only one skill misses six others and the one-technical insight.
"""),

    q('swep_day5_49',
      "What is the Twelve Weeks Action Plan?",
      ['Set 3–5 goals, have CV and LinkedIn tailored to goals, build job portfolio — document evidence, build technical skills, document evidence of skills, close skill gap, develop and improve consistently',
       'Only set goals and do nothing else',
       'Only build portfolio',
       'Only close skill gap'],
      0,
      'Set 3-5 goals, CV/LinkedIn tailored, build job portfolio document evidence, build technical skills, document evidence, close skill gap, develop consistently.',
      """
### Why this is the answer
Twelve Weeks Action Plan slide: \"Set 3-5 goals. Have a CV and LinkedIn profile tailored to your goals. Build a job portfolio — document evidence. Build technical skills. Document evidence of skills. Close your skill gap, develop, and improve consistently.\"

### Source
NECA Day 5.

### Why the others fail
Only one action misses comprehensive plan.
"""),

    q('swep_day5_50',
      "What is the trap about notebooks vs daily learning record in Day 5?",
      ['Prepare notebooks is before SIWES; keep a daily learning record is during SIWES',
       'Both are before SIWES',
       'Both are during SIWES',
       'Both are after SIWES'],
      0,
      'Prepare notebooks is before; keep daily learning record is during.',
      """
### Why this is the answer
Traps to watch slide for Day 5: \"Prepare notebooks is before; keep a daily learning record is during.\"

### Source
Day 5 summaryNotes traps.

### Why the others fail
Both before, both during, both after swap the timing distinction.
"""),

    q('swep_day5_51',
      "Which two items appear on both employers’ observed list and skills list, so they cannot distinguish the two lists?",
      ['Communication and team work appear on both',
       'Punctuality and integrity appear on both',
       'Professionalism and initiative appear on both',
       'Technical skills and digital literacy appear on both'],
      0,
      'Communication and team work appear on both employers’ list and skills list.',
      """
### Why this is the answer
Traps slide: \"Communication and team work appear on both the employers’ list and the skills list — they cannot distinguish the two.\"

### Source
Day 5 summaryNotes.

### Why the others fail
Punctuality/integrity/professionalism are observed traits not listed as skills; technical/digital are only in skills list.
"""),

    q('swep_day5_52',
      "Which are observed traits, not listed skills, in Day 5?",
      ['Punctuality, integrity, professionalism are observed traits, not listed skills',
       'Communication and teamwork are observed traits only',
       'Technical skills are observed traits',
       'Digital literacy is observed trait'],
      0,
      'Punctuality, integrity, professionalism are observed traits, not listed skills.',
      """
### Why this is the answer
Traps: \"Punctuality, integrity, professionalism are observed traits, not listed skills.\"

### Source
Day 5 summaryNotes.

### Why the others fail
Communication/teamwork are both; technical/digital are skills not observed traits.
"""),

    q('swep_day5_53',
      "What is the duration distinction trap for Day 5?",
      ['12 weeks is the plan; 8 weeks is SWEP minimum; 24 weeks is SIWES II',
       '12 weeks is SWEP minimum; 8 weeks is plan; 24 weeks is SWEP',
       'All durations are same',
       '24 weeks is SWEP minimum'],
      0,
      '12 weeks is plan, 8 weeks SWEP minimum, 24 weeks SIWES II.',
      """
### Why this is the answer
Traps: \"12 weeks is the plan; 8 weeks is the SWEP minimum; 24 weeks is SIWES II.\"

### Source
Day 5 summaryNotes.

### Why the others fail
Swapped or same durations miss the three distinct numbers.
"""),

    q('swep_day5_54',
      "Who is the speaker for Day 5 according to notes?",
      ['Nigeria Employers’ Consultative Association (NECA) representative — no personal name given',
       'Prof. O. A. Olojede',
       'Prof. M. D. Shittu',
       'Dr. A. Olatunji'],
      0,
      'NECA representative — no personal name given.',
      """
### Why this is the answer
Day 5 summaryNotes and lectureMeta: Speaker is Nigeria Employers’ Consultative Association (NECA) — note says speaker only as NECA representative, no personal name given. Trap slide: \"The note names the speaker only as a NECA representative — no personal name is given.\"

### Source
Day 5 notes.

### Why the others fail
Olojede, Shittu, Olatunji are Day 1 and Day 2 speakers, not Day 5.
"""),

    q('swep_day5_55',
      "What does 'network brings good net worth' mean in SIWES context?",
      ['SIWES period is for building human networks',
       'SIWES is only for collecting money',
       'Networking is not important',
       'Net worth has no connection to network'],
      0,
      'SIWES period is for building human networks — network brings net worth.',
      """
### Why this is the answer
Core Concepts: \"The SIWES period is for building human networks, as network brings good net worth.\"

### Source
NECA Day 5.

### Why the others fail
Only money, not important, no connection contradict networking message.
"""),

    q('swep_day5_56',
      "What should a CV and LinkedIn be tailored to according to Twelve Weeks Action Plan?",
      ['Tailored to your goals (3–5 goals)',
       'Tailored to nothing',
       'Tailored to only one goal',
       'Tailored to random goals'],
      0,
      'CV and LinkedIn tailored to your goals.',
      """
### Why this is the answer
Plan: \"Have a CV and LinkedIn profile tailored to your goals.\"

### Source
NECA Day 5.

### Why the others fail
Nothing, only one, random contradict tailored to your 3-5 goals.
"""),

    q('swep_day5_57',
      "What does 'Don’t just collect tasks, but collate evidence' emphasize?",
      ['How, when & what — have a digital portfolio, avoid career mismatch',
       'Only collect tasks without evidence',
       'Only collate evidence without tasks',
       'Ignore evidence completely'],
      0,
      'Collate evidence How/when/what, digital portfolio, avoid career mismatch.',
      """
### Why this is the answer
Learning Loop note: \"Don’t just collect tasks, but collate evidence (How, when & what). Have a digital portfolio. Do not have a career mismatch.\"

### Source
NECA Day 5.

### Why the others fail
Only tasks, only evidence without tasks, ignore evidence miss How/when/what and portfolio message.
"""),

    q('swep_day5_58',
      "What is the warning about office politics in Day 5?",
      ['Beware of office politics! Nobody is your best friend at work',
       'Office politics is good and everyone is best friend',
       'Ignore office politics completely',
       'Office politics does not exist'],
      0,
      'Beware of office politics! Nobody is your best friend at work.',
      """
### Why this is the answer
Employers Notice slide includes: \"Note: Beware of office politics! Nobody is your best friend at work.\"

### Source
NECA Day 5.

### Why the others fail
Good/best friend, ignore, does not exist contradict warning.
"""),

    q('swep_day5_59',
      "What does 'close your skill gap, develop and improve consistently' refer to?",
      ['Part of Twelve Weeks Action Plan — close skill gap, develop and improve consistently',
       'Part of before SIWES only',
       'Not part of any plan',
       'Only for after SIWES'],
      0,
      'Part of Twelve Weeks Action Plan — close skill gap, develop consistently.',
      """
### Why this is the answer
Action Plan ends with: \"Close your skill gap, develop, and improve consistently.\"

### Source
NECA Day 5.

### Why the others fail
Only before, not part, only after miss its place in 12-week plan.
"""),

    q('swep_day5_60',
      "What is the difference between collecting tasks and collating evidence in SIWES?",
      ['Collecting tasks is just doing activities; collating evidence is documenting How, when & what with digital portfolio to build verifiable skills',
       'No difference, same thing',
       'Collecting tasks is better than collating evidence',
       'Collating evidence is not needed'],
      0,
      'Collecting tasks is doing activities; collating evidence is documenting How/when/what with portfolio for verifiable skills.',
      """
### Why this is the answer
Learning Loop teaching: Don't just collect tasks (activities) but collate evidence (How, when & what). Have digital portfolio. SIWES is not escape but period to convert experience into verifiable skills guaranteeing employability. Network brings net worth. Professional in training mindset.

### Source
NECA Day 5.

### Why the others fail
No difference, collecting better, not needed contradict evidence-based employability message.
"""),
]
