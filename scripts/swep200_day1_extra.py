#!/usr/bin/env python3
"""SWEP 200 — Day 1 extra 20 questions (fresh, not in original 44)."""

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
    q('swep_day1_45',
      "In Prof. Shittu's history of ITF, the Fund's support machinery for training includes several mechanisms. Which of the following is listed as part of that machinery?",
      ['Bearing a proportion of the direct costs incurred by employers in human capital development',
       'Paying full salaries of all industrial workers nationwide',
       'Importing all training equipment from abroad',
       'Replacing university lecturers with industry staff'],
      0,
      'ITF bears a proportion of direct costs incurred by employers in human capital development.',
      """
### Why this is the answer
The \"support machinery for training\" slide lists how the Fund supports training:
1. **Bearing a proportion of the direct costs** incurred by employers in human capital development and performance improvement, focusing on current trends
2. Assisting/strengthening training capability and facilities nationwide (ICT emphasis)
3. Directly building its own training facilities
4. Organizing research and studies into training
5. Publishing training guides and manuals
6. Giving **ex-gratia awards**

Only option A appears verbatim in that list.

### Source
Prof. M. D. Shittu, \"The support machinery for training\" and \"Services\" slides; corroborated by the benefits deck organogram notes.

### Why the others fail
Full salary payment, importing all equipment, and replacing lecturers are invented — they confuse ITF's *partial reimbursement* role with total takeover.
"""),

    q('swep_day1_46',
      "According to the ITF organizational breakdown in the benefits deck, which of the following is a department of the ITF?",
      ['Business Training and Development Department (BTD)',
       'Ministry of Education Inspectorate Department',
       'National Universities Commission Department',
       'Students Affairs Department'],
      0,
      'Business Training and Development Department (BTD) is an ITF department.',
      """
### Why this is the answer
The benefits deck slide lists ITF departments as:
- **Business Training and Development Department (BTD)**
- Administration & Human Resources Department (A&HRD)
- Finance and Accounts Department (F&AD)
- Revenue, Inspectorate and Compliance Department (RI&CD)
- Field Services Department (FSD)
- Technical and Vocational Skills Training Department (TVSTD)
- Research and Curriculum Development Department (R&CDD)
- Information and Communication Technology Department (ICTD)
- Procurement Department (PD)
- Corporate Planning Department (CPD)

BTD is explicitly listed.

### Source
Prof. E. A. Taiwo, benefits deck page showing \"The various departments in ITF includes:\".

### Why the others fail
Ministry of Education Inspectorate, NUC Department, and Students Affairs are not ITF departments — they belong to other bodies in the SIWES ecosystem.
"""),

    q('swep_day1_47',
      "What are the exact numbers for ITF governance and spread as presented across Day 1 lectures?",
      ['13-member Governing Council, 15 Departments and 5 Units at HQ, 42 Area Offices, 5 Skills Training Centres',
       '15-member Governing Council, 13 Departments and 5 Units at HQ, 42 Area Offices, 5 Skills Training Centres',
       '13-member Governing Council, 42 Departments and 5 Units at HQ, 15 Area Offices, 5 Skills Training Centres',
       '13-member Governing Council, 15 Departments and 5 Units at HQ, 5 Area Offices, 42 Skills Training Centres'],
      0,
      '13-member Governing Council, 15 Departments and 5 Units at HQ, 42 Area Offices, 5 Skills Training Centres.',
      """
### Why this is the answer
Two sources converge:
- Olojede orientation notes: **13-member Governing Council; 15 Departments and 5 Units at HQ; 42 Area Offices; 5 Skills Training Centres**
- Shittu organogram slide reinforces 42 Area Offices and the department count

The numbers are deliberately easy to swap — 13 vs 15 vs 42 vs 5 — so the exact pairing matters.

### Source
Prof. O. A. Olojede summary notes and Prof. Shittu organogram.

### Why the others fail
Each swaps one pair: 15-member council (wrong), 42 departments (wrong), 5 Area Offices (wrong). The correct set is **13 / 15+5 / 42 / 5**.
"""),

    q('swep_day1_48',
      "Which four units report straight to the Director-General of ITF according to the organogram notes?",
      ['Legal and Council Affairs, Internal Audit, Public Relations and Publicity, SERVICOM',
       'Finance and Accounts, Procurement, Field Services, Corporate Planning',
       'Business Training and Development, Administration & HR, ICT, Research and Curriculum',
       'Revenue Inspectorate, Technical Vocational Skills Training, Procurement, Finance'],
      0,
      'Legal and Council Affairs, Internal Audit, Public Relations and Publicity, SERVICOM report directly to the DG.',
      """
### Why this is the answer
The handwritten Day 1 summary notes explicitly state: \"**Four units report straight to the Director-General: Legal and Council Affairs, Internal Audit, Public Relations and Publicity, SERVICOM**.\"

### Source
Day 1 summary notes (topicMeta swep-day-1 summaryNotes).

### Why the others fail
All other options list regular departments (Finance, Procurement, Field Services, BTD, etc.) which report through the normal hierarchy, not directly to the DG.
"""),

    q('swep_day1_49',
      "According to Prof. Shittu, how does the ITF's reimbursement system work for employers?",
      ['The Fund bears part of the cost incurred by employers in training employees by reimbursing part of the cost for courses undertaken',
       'The Fund pays 100% of all training costs plus full employee salaries',
       'The Fund only reimburses foreign training, not local training',
       'The Fund reimburses students directly, not employers'],
      0,
      'ITF bears part of the cost incurred by employers by reimbursing part of course costs.',
      """
### Why this is the answer
Slide text: \"**ITF reimburses employers for the development and support of training programmes they offer; i.e., the Fund bears part of the cost incurred by employers in training their employees by reimbursing part of the cost incurred for courses undertaken.**\"

Other returns include general availability of trained and mobile manpower throughout the economy — trainees complement workforce at subsidized cost.

### Source
Prof. Shittu, History of ITF deck.

### Why the others fail
100% plus salaries is exaggerated; foreign-only is invented; reimbursing students directly contradicts the employer-focused model.
"""),

    q('swep_day1_50',
      "Prof. E. A. Taiwo lists benefits of SIWES to Science and Technology. Which is NOT listed as one of those benefits?",
      ['Exposure to modern technology and industrial environments',
       'Development of practical and technical skills',
       'Bridging the gap between theory and practice',
       'Automatic award of first-class honours upon completion'],
      3,
      'Automatic award of first-class is not a SIWES benefit.',
      """
### Why this is the answer
Benefits slide lists:
1. **Bridging the gap between theory and practice** — apply scientific principles to real-life
2. **Development of practical and technical skills** — hands-on experience with lab equipment, industrial machines, software, analytical techniques
3. **Exposure to modern technology and industrial environments** — understanding current technological developments, familiarity with modern equipment, automation, digital technologies

Automatic first-class is never mentioned and would contradict tertiary assessment.

### Source
Prof. Taiwo, Benefits of Industrial Training deck.

### Why the others fail
Options A, B, C are verbatim benefits. Only D is fabricated.
"""),

    q('swep_day1_51',
      "What is the eligibility criterion for a student to be eligible for SIWES allowance as per Prof. Taiwo's slide?",
      ['Satisfactory completion of 6 months SIWES, evidenced from Logbooks, Form 8 and Form SPE-1, plus adequate vetting of Logbooks',
       'Completion of 3 months SWEP with attendance register only',
       'Payment of N5,000 to ITF headquarters',
       'Automatic eligibility for all 200-level students regardless of logbook'],
      0,
      'Eligibility requires 6 months SIWES, logbooks, Form 8, SPE-1, and vetting.',
      """
### Why this is the answer
Eligibility slide states:
- **Satisfactory completion of 6 months SIWES, evidenced from Logbooks, Form 8 and Form SPE-1**
- **Adequate vetting of Logbooks, etc**

The 6 months corresponds to SIWES II (24 weeks).

### Source
Prof. Taiwo, Allowances/Eligibility slide.

### Why the others fail
3 months SWEP, N5,000 payment, and automatic eligibility contradict the 6-month, evidence-based, vetted requirement.
"""),

    q('swep_day1_52',
      "What does Prof. Olojede state as the distinction between SWEP and SIWES in terms of location and focus?",
      ['SWEP is undergone traditionally inside the school focusing on general workshop skills, safety protocols and hands-on tool usage; SIWES is undergone in external industries bridging theory and industrial reality',
       'SWEP and SIWES are both undergone inside the school with no difference',
       'SWEP is external and SIWES is internal',
       'SWEP is for 400-level only while SIWES is for 200-level only'],
      0,
      'SWEP is inside school (workshop skills, safety, tools); SIWES is external (bridging theory and industry).',
      """
### Why this is the answer
Olojede slide:
- **Module 1 - SWEP: Undergone traditionally inside the school. Focuses on general workshop skills, safety protocols, and hands-on tool usage.**
- **Module 2 - SIWES: Undergone in external industries. Bridges the gap between theory and industrial reality, giving graduates a foretaste of the labor market.**

### Source
Prof. Olojede, Background & Rationale and Training Timelines.

### Why the others fail
Both inside, swapped locations, and level-only distinctions misrepresent the location/focus distinction.
"""),

    q('swep_day1_53',
      "What resume advantage does Prof. Olojede attribute to SWEP/SIWES?",
      ['Affords fresh graduates the highly valuable benefit of claiming cognate work experience directly on their resumes',
       'Guarantees automatic employment in Federal Government',
       'Exempts graduates from NYSC',
       'Provides free foreign scholarships to all participants'],
      0,
      'SWEP/SIWES affords fresh graduates cognate work experience for their resumes.',
      """
### Why this is the answer
Slide: \"**Resume Advantage: Affords fresh graduates the highly valuable benefit of claiming cognate work experience directly on their resumes.**\"

### Source
Prof. Olojede, Background & Rationale.

### Why the others fail
Automatic Federal job, NYSC exemption, and free foreign scholarships are not stated and would be false promises.
"""),

    q('swep_day1_54',
      "According to Amphitheatre Ground Rules Part 1, what is the rule on punctual seating and device usage?",
      ['Must be fully seated by 08:30 every morning and by 12:25 every afternoon; all mobile phones must be on silence',
       'Must be seated by 09:00 morning only; phones can be used freely',
       'No seating time specified; devices must be switched off completely',
       'Must be seated by 08:00 morning and 12:00 afternoon; phones on vibration allowed'],
      0,
      'Fully seated by 08:30 morning and 12:25 afternoon; devices on silence.',
      """
### Why this is the answer
Venue Decorum & Integrity slides:
- **Punctual Seating: Trainees must be fully seated by 08:30 every morning and by 12:25 every single afternoon.**
- **Device Silence: All mobile phones/devices must be on silence.**

Active engagement, no side-talking also listed.

### Source
Prof. Olojede, Venue Decorum & Integrity.

### Why the others fail
09:00, no time, 08:00/12:00, and vibration allowance contradict the exact 08:30/12:25 and silence rule.
"""),

    q('swep_day1_55',
      "Who served as ITF Chief Executive from 1976 to 1979?",
      ['Alhaji Muhammed Dikko, Director',
       'Dr. Abel Ubeku, OFR, Secretary',
       'Mrs. Ekei Nene Archibong, Secretary',
       'Alhaji Hassan Ahmed II, mni, MFR, Director-General'],
      0,
      'Alhaji Muhammed Dikko served 1976–1979 as Director.',
      """
### Why this is the answer
Chief Executives table:
| Period | Chief Executive |
| 1971–1973 | Dr. Abel Ubeku, OFR Secretary |
| 1973–1975 | Mrs. Ekei Nene Archibong Secretary |
| **1976–1979** | **Alhaji Muhammed Dikko Director** |
| 1980–1989 | Alhaji Muhammed Lawal Tildun Wada Director-General |

### Source
Prof. Taiwo, ITF Chief Executives from Inception to Date.

### Why the others fail
Ubeku is 1971-73, Archibong 1973-75, Hassan Ahmed II 1989-2000 — all adjacent but wrong period.
"""),

    q('swep_day1_56',
      "Who served as ITF Chief Executive from 1980 to 1989?",
      ['Alhaji Muhammed Lawal Tildun Wada, Director-General',
       'Prof. Olu E. Akeredolu/Akerejola, Director-General',
       'Sir Joseph Ntung Ari, KSM, KSS, Director-General',
       'Mr. Dickson Onuoha, Acting Director-General'],
      0,
      'Alhaji Muhammed Lawal Tildun Wada served 1980–1989.',
      """
### Why this is the answer
Table row: **1980–1989 Alhaji Muhammed Lawal Tildun Wada Director-General**

### Source
Prof. Taiwo chief executives slide.

### Why the others fail
Akeredolu is 2000-2006, Ari is 2016-2023, Onuoha is 2023-2024 acting — all different eras.
"""),

    q('swep_day1_57',
      "Who served as ITF Chief Executive from 2016 to 2023?",
      ['Sir Joseph Ntung Ari, KSM, KSS, Director-General',
       'Mrs. Juliet O. E. Chukkas-Onaeko, MFR, Director-General',
       'Dr. Afiz Oluwatoyin Ogun, Director-General',
       'Alhaji Hassan Ahmed II, mni, MFR, Director-General'],
      0,
      'Sir Joseph Ntung Ari served 2016–2023.',
      """
### Why this is the answer
Row: **2016–2023 Sir Joseph Ntung Ari, KSM, KSS Director-General**

### Source
Prof. Taiwo chief executives.

### Why the others fail
Chukkas-Onaeko is 2014-2016, Ogun is 2024-present, Hassan Ahmed II is 1989-2000.
"""),

    q('swep_day1_58',
      "According to Prof. Shittu, what provides for contributions on the part of employers and subventions on the part of Federal Government to finance ITF?",
      ['The Act provides for contributions on the part of employers and for subventions on the part of Federal Government',
       'A voluntary donation scheme by students',
       'Only foreign grants from UNESCO',
       'Only internally generated revenue from SIWES fees'],
      0,
      'The Act provides for employer contributions and Federal Government subventions.',
      """
### Why this is the answer
History slide: \"**To finance the scheme the Act provides for contributions on the part of employers and for subventions on the part of the Federal Government.**\"

### Source
Prof. Shittu, History of ITF.

### Why the others fail
Voluntary student donations, UNESCO-only, and SIWES fees-only contradict the Act-based dual financing.
"""),

    q('swep_day1_59',
      "Which of the following is listed as a service offered by ITF under 'Training in Poverty Alleviation and Self Employment' category?",
      ['Training in Poverty Alleviation and Self Employment is itself a listed ITF service',
       'Training in Space Technology and Satellite Launch',
       'Training in Underwater Basket Weaving',
       'Training in Forex Trading and Cryptocurrency'],
      0,
      'Training in Poverty Alleviation and Self Employment is a listed ITF service.',
      """
### Why this is the answer
ITF Services slide explicitly lists:
- Engineering and Technology Training
- Management and Supervisory Training
- Industrial Productivity and Efficiency (In-plant) Training
- Safety Training
- Computer Training
- Vocational and Apprentice Training
- Applied Research and Methodology Services & Training
- Training in Accounting & Financial Management
- Training in Secretarial and Modern Office Management
- **Training in Poverty Alleviation and Self Employment**
- Training in Instructional Technology
- Train the Trainer Programmes
- Placement of Students...
- Advisory and Management Consulting

### Source
Prof. Shittu services slides.

### Why the others fail
Space technology, underwater basket weaving, forex/crypto are not listed ITF services in the deck.
"""),

    q('swep_day1_60',
      "What is the current allowance question mark noted in Prof. Taiwo's allowance slide for present amount?",
      ['The present amount is shown as ??? indicating not specified/open',
       'The present amount is N10,000 fixed',
       'The present amount is N50,000 fixed',
       'The present amount is $100 fixed'],
      0,
      'Present amount is shown as ??? — not specified.',
      """
### Why this is the answer
Allowances slide lists:
1974 – N30/month
1976 – N90/month
1981 – N250/month
2000 – N2,500/month
**The present amount ???**

The ??? is a deliberate trap — it means the deck leaves present amount open.

### Source
Prof. Taiwo allowances slide.

### Why the others fail
N10,000, N50,000, $100 are invented figures not in slide; the slide explicitly shows ???.
"""),

    q('swep_day1_61',
      "Which faculty's 'Farm Year' is described as a consolidated 1-year placement throughout entire fourth academic session?",
      ['Faculty of Agriculture',
       'Faculty of Technology',
       'Faculty of Arts',
       'Faculty of Law'],
      0,
      'Faculty of Agriculture employs a consolidated 1-year Farm Year.',
      """
### Why this is the answer
Program Timelines slide: \"**Faculty of Agriculture: Employs a consolidated 1-year 'Farm Year' placement throughout their entire fourth academic session.**\"

### Source
Prof. Olojede.

### Why the others fail
Technology, Arts, Law are not described as having Farm Year — only Agriculture.
"""),

    q('swep_day1_62',
      "What is the consequence of 'You must sign the register for yourself and by yourself only' violation?",
      ['Attempting to sign for another student is handled as a criminal act',
       'A warning letter only',
       'No consequence, it is allowed',
       'Automatic extra credit'],
      0,
      'Signing for another is handled as a criminal act.',
      """
### Why this is the answer
Attendance Integrity rule: \"**You must sign the register for yourself and by yourself only. Attempting to sign for another student is handled as a criminal act.**\"

### Source
Prof. Olojede Venue Decorum.

### Why the others fail
Warning only, allowed, extra credit contradict the criminal act handling.
"""),

    q('swep_day1_63',
      "According to Day 1 lectures, which programmes are exempt from specific practical modules under 4-Year Program Exemptions?",
      ['Architecture, Fine and Applied Arts, and Industrial Chemistry',
       'Electrical Engineering, Mechanical Engineering, Chemical Engineering',
       'Medicine, Pharmacy, Nursing',
       'Computer Science, Mathematics, Physics'],
      0,
      'Architecture, Fine and Applied Arts, and Industrial Chemistry are exempt.',
      """
### Why this is the answer
Slide: \"**4-Year Program Exemptions: Programs like Architecture, Fine and Applied Arts, and Industrial Chemistry are exempt from specific practical modules.**\"

### Source
Prof. Olojede Training Timelines.

### Why the others fail
Engineering, Medicine/Pharmacy/Nursing, Computer Science/Math/Physics are not listed as exempt in this context.
"""),

    q('swep_day1_64',
      "What is the name of the award given by ITF as part of its support machinery?",
      ['Ex-gratia awards',
       'Nobel Prize awards',
       'Oscar awards',
       'Grammy awards'],
      0,
      'ITF gives ex-gratia awards.',
      """
### Why this is the answer
Support machinery list ends with: \"**giving ex-gratia awards**\".

### Source
Prof. Shittu.

### Why the others fail
Nobel, Oscar, Grammy are not ITF awards — ex-gratia is the term used.
"""),
]
