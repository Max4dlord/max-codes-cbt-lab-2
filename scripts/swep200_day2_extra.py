#!/usr/bin/env python3
"""SWEP 200 — Day 2 extra 20 questions."""

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
    q('swep_day2_46',
      "In the Substance Abuse lecture, which of the following is listed as a physical sign?",
      ['Frequent nosebleeds or sniffing (may indicate snorting substances)',
       'Failure to submit assignments',
       'Involvement in fights or cultism',
       'Financial difficulties or repeated borrowing'],
      0,
      'Frequent nosebleeds or sniffing is a physical sign.',
      """
### Why this is the answer
Physical Signs slide lists:
- Bloodshot or glassy eyes
- Sudden weight loss or gain
- Unusual body odours (alcohol, cannabis)
- Poor hygiene and self-care
- **Frequent nosebleeds or sniffing (may indicate snorting)**
- Tremors, slurred speech, or unsteady gait

### Source
Dr. Olatunji, Substance Abuse — Signs and Symptoms.

### Why the others fail
Failure to submit assignments is academic; fights/cultism is social; financial difficulties is social/lifestyle — not physical.
"""),

    q('swep_day2_47',
      "Which of the following is listed as a behavioural change associated with substance abuse?",
      ['Loss of interest in hobbies, academics, or extracurriculars',
       'Bloodshot or glassy eyes',
       'Frequent absenteeism from lectures',
       'Hallucinations or delusions'],
      0,
      'Loss of interest in hobbies/academics is a behavioural change.',
      """
### Why this is the answer
Behavioural Changes slide:
- Sudden change in friend groups, especially peers known for drug use
- Secretive or suspicious behavior
- Lying, stealing, manipulation to obtain money/substances
- Increased impulsivity or risk-taking
- **Loss of interest in hobbies, academics, or extracurriculars**
- Neglect of responsibilities (missed classes/deadlines)

### Source
Dr. Olatunji.

### Why the others fail
Bloodshot eyes is physical; absenteeism is academic; hallucinations is psychological/emotional.
"""),

    q('swep_day2_48',
      "Which of the following is categorized as a psychological and emotional symptom of substance abuse?",
      ['Unexplained mood swings or irritability',
       'Sudden weight loss or gain',
       'Sudden change in friend groups',
       'Frequent visits to high-risk areas (drug joints)'],
      0,
      'Unexplained mood swings or irritability is psychological/emotional.',
      """
### Why this is the answer
Psychological/Emotional Symptoms slide lists:
- **Unexplained mood swings or irritability**
- Anxiety, restlessness, panic attacks
- Periods of excessive energy/agitation (stimulant)
- Depression, social withdrawal, emotional numbness
- Hallucinations/delusions (severe cases)

### Source
Dr. Olatunji.

### Why the others fail
Weight loss is physical; change friend groups is behavioural; visits to drug joints is social/lifestyle.
"""),

    q('swep_day2_49',
      "Which is listed as a social and lifestyle indicator of substance abuse?",
      ['Unusual sleeping patterns (e.g., insomnia or excessive sleeping)',
       'Tremors, slurred speech, or unsteady gait',
       'Declining grades and academic performance',
       'Anxiety, restlessness, or panic attacks'],
      0,
      'Unusual sleeping patterns is a social/lifestyle indicator.',
      """
### Why this is the answer
Social and Lifestyle Indicators slide:
- Financial difficulties or repeated borrowing
- Involvement in fights, cultism, confrontations
- Conflict with family/roommates
- **Unusual sleeping patterns (insomnia or excessive sleeping)**
- Frequent visits to high-risk areas (drug joints)

### Source
Dr. Olatunji.

### Why the others fail
Tremors is physical; declining grades is academic; anxiety is psychological.
"""),

    q('swep_day2_50',
      "Which of the following is listed under 'Preventive Strategies' for substance abuse?",
      ['Life Skills and Coping Mechanisms',
       'Counselling and Psychological Support',
       'Medical Treatment and Rehabilitation',
       'Early Identification and Screening'],
      0,
      'Life Skills and Coping Mechanisms is a preventive strategy.',
      """
### Why this is the answer
Prevention vs Intervention:
**Preventive (before):**
- Campus-Based Drug Education
- **Life Skills and Coping Mechanisms**
- Peer Support Networks
- Restricting Access to Substances
- Parental and Community Involvement

**Intervention (after):**
- Early Identification and Screening
- Counselling and Psychological Support
- Medical Treatment and Rehabilitation
- Policy and Disciplinary Framework
- Digital and Media Campaigns

### Source
Dr. Olatunji, Prevention and Intervention Strategies.

### Why the others fail
Counselling, medical treatment, early screening are intervention, not preventive.
"""),

    q('swep_day2_51',
      "Which organization is part of Multi-Sectoral Collaboration for substance abuse intervention?",
      ['National Drug Law Enforcement Agency (NDLEA)',
       'Nigerian Stock Exchange',
       'Federal Inland Revenue Service',
       'Nigerian Football Federation'],
      0,
      'NDLEA is part of multi-sectoral collaboration.',
      """
### Why this is the answer
Multi-Sectoral Collaboration slide lists:
- **National Drug Law Enforcement Agency (NDLEA)**
- Federal Ministry of Health
- Non-Governmental Organizations (NGOs)
- Campus health services

### Source
Dr. Olatunji.

### Why the others fail
Stock Exchange, FIRS, Football Federation are not listed in this collaboration.
"""),

    q('swep_day2_52',
      "In Workshop & Industrial Safety, what does OSHA and NIOSH set standards for?",
      ['Respirator use, focusing on proper selection, fit testing, and medical evaluation',
       'Academic grading systems',
       'Football match regulations',
       'Catering services in workshops'],
      0,
      'OSHA and NIOSH set standards for respirator use (selection, fit testing, medical evaluation).',
      """
### Why this is the answer
PPE slide: \"**In industrial settings, respirators are crucial for worker safety when exposed to hazardous airborne contaminants. OSHA and NIOSH set standards for respirator use, focusing on proper selection, fit testing, and medical evaluation.** Respirators are categorized as either air-purifying (APRs) or supplied-air (SARs).\"

### Source
Prof. Adeleke, Workshop & Industrial Safety — PPE respirator slide.

### Why the others fail
Academic grading, football, catering are unrelated to OSHA/NIOSH respirator standards.
"""),

    q('swep_day2_53',
      "What is the difference between APRs and SARs in respirator categorization?",
      ['APRs are air-purifying, SARs are supplied-air',
       'APRs are supplied-air, SARs are air-purifying',
       'Both are air-purifying',
       'Both are supplied-air'],
      0,
      'APRs are air-purifying, SARs are supplied-air.',
      """
### Why this is the answer
Slide: \"Respirators are categorized as either **air-purifying (APRs)** or **supplied-air (SARs)**, and must be appropriate for specific workplace hazards.\"

### Source
Prof. Adeleke.

### Why the others fail
Swapped definitions or both same are incorrect per slide.
"""),

    q('swep_day2_54',
      "Which materials are commonly used for protective clothing in nuclear power plants?",
      ['Tyvek, neoprene, and nitrile, often with flame-resistant (FR) fabrics like Anti-C/FR',
       'Cotton and silk only',
       'Paper and cardboard',
       'Glass and metal sheets'],
      0,
      'Tyvek, neoprene, nitrile with FR fabrics like Anti-C/FR are used in nuclear plants.',
      """
### Why this is the answer
PPE nuclear slide: \"Commonly used materials include **Tyvek, neoprene, and nitrile, often in conjunction with specialized flame-resistant (FR) fabrics like Anti-C/FR**. Proper donning, doffing, and decontamination procedures are also essential.\"

### Source
Prof. Adeleke.

### Why the others fail
Cotton/silk, paper/cardboard, glass/metal are not listed as nuclear PPE materials.
"""),

    q('swep_day2_55',
      "What is the most common symbol for protective clothing in nuclear power plants?",
      ['A figure of a worker in a full-body suit, often with a respirator or gas mask, and the universal radiation symbol (trefoil) in yellow and black or black and white',
       'A simple red cross',
       'A green leaf',
       'A blue circle with a white tick'],
      0,
      'Figure of worker in full-body suit with respirator/gas mask and radiation trefoil in yellow-black or black-white.',
      """
### Why this is the answer
Slide: \"**The most common symbol for protective clothing in nuclear power plants is a figure of a worker in a full-body suit, often with a respirator or gas mask, and the universal radiation symbol (trefoil) present, usually in yellow and black or black and white.**\"

### Source
Prof. Adeleke.

### Why the others fail
Red cross (medical), green leaf (environment), blue circle white tick (quality) are not nuclear PPE symbols.
"""),

    q('swep_day2_56',
      "Which of the following is an example of a physical hazard in the workshop?",
      ['Noise, vibration, radiation, extreme temperatures, and poor lighting',
       'Bacteria, viruses, fungi',
       'Repetitive tasks and awkward postures',
       'Toxic substances and flammable materials'],
      0,
      'Noise, vibration, radiation, extreme temperatures, poor lighting are physical hazards.',
      """
### Why this is the answer
Hazard classification:
- **Chemical Hazards:** toxic substances, flammable, corrosive agents
- **Physical Hazards:** **noise, vibration, radiation, extreme temperatures, poor lighting**
- **Ergonomic Hazards:** repetitive tasks, awkward postures, improper workstation design → musculoskeletal disorders
- **Biological Hazards:** bacteria, viruses, fungi

### Source
Prof. Adeleke, Common Industrial Hazards.

### Why the others fail
Bacteria is biological, repetitive tasks is ergonomic, toxic substances is chemical.
"""),

    q('swep_day2_57',
      "Which control measure is described as the most effective?",
      ['Elimination — completely removing the hazard from the workplace',
       'Personal Protective Equipment (PPE)',
       'Administrative Controls',
       'Substitution'],
      0,
      'Elimination — completely removing the hazard — is most effective.',
      """
### Why this is the answer
Control Measures slide lists in hierarchy:
- **Elimination: Completely removing the hazard from the workplace is the most effective control measure.**
- Substitution: Replacing hazardous materials/processes with safer alternatives
- Engineering Controls: physical changes like machine guarding, ventilation, noise reduction
- Administrative Controls: procedures, policies, training
- PPE: gloves, masks, respirators

### Source
Prof. Adeleke.

### Why the others fail
PPE is least effective (last resort), administrative and substitution are less effective than elimination.
"""),

    q('swep_day2_58',
      "In employability, what does the presentation say about many graduates being unemployable?",
      ['Many graduates are unemployable, hence difficulty to get jobs in a world becoming increasingly demanding and competitive — example of CBN recruitment exercise/software engineers in Germany',
       'All graduates are automatically employable',
       'Unemployment is only about insufficient number of jobs',
       'Employability is not important for job seeking'],
      0,
      'Many graduates are unemployable; example CBN recruitment and software engineers in Germany.',
      """
### Why this is the answer
Slides 4-5:
- \"**Not just about insufficient number of jobs**\"
- \"**Many graduates … are unemployable** Hence, difficulty to get jobs in a world becoming increasingly demanding and competitive on all fronts Example of CBN recruitment exercise/software engineers in Germany\"

### Source
Prof. Ekanola, 21st-Century Employability Skills.

### Why the others fail
Automatically employable, only insufficient jobs, not important are opposite of slide message.
"""),

    q('swep_day2_59',
      "What are the 8 clusters of 21st-century employability skills?",
      ['Communication and interpersonal; Critical thinking and problem-solving; Digital and technological; Creativity and innovation; Collaboration and teamwork; Personal effectiveness and emotional intelligence; Career management, entrepreneurship and leadership; Adaptability, lifelong learning and professional development',
       'Only technical skills and academic grades',
       'Only digital skills',
       'Only communication and nothing else'],
      0,
      'The 8 clusters cover communication, critical thinking, digital, creativity, teamwork, emotional intelligence, career/entrepreneurship/leadership, adaptability/lifelong learning.',
      """
### Why this is the answer
Slide 8 lists exactly:
1. Communication and interpersonal skills
2. Critical thinking and problem-solving skills
3. Digital and technological skills
4. Creativity and innovation skills
5. Collaboration and teamwork
6. Personal effectiveness and emotional intelligence
7. Career management, entrepreneurship and leadership
8. Adaptability, lifelong learning and professional development

### Source
Prof. Ekanola.

### Why the others fail
Only technical, only digital, only communication are incomplete — the model is 8 clusters.
"""),

    q('swep_day2_60',
      "According to employability lecture, what should the goal be regarding AI?",
      ['The goal should not be to compete with AI but to become a professional who can work intelligently with AI — AI-enabled professionals rather than AI specialists',
       'The goal should be to compete with AI and defeat it',
       'The goal should be to ignore AI completely',
       'The goal should be to ban AI from workplace'],
      0,
      'Goal is not to compete with AI but to become AI-enabled professional who works intelligently with AI.',
      """
### Why this is the answer
AI Literacy slides:
- \"**The goal should not be to compete with AI. It should be to become a professional who can work intelligently with AI**\"
- \"**The future may belong more to: AI-enabled professionals rather than simply AI specialists**\"

### Source
Prof. Ekanola, AI Literacy.

### Why the others fail
Compete/defeat, ignore, ban contradict the AI-enabled professional message.
"""),

    q('swep_day2_61',
      "Which of the following is listed as part of communication skills acquisition through practice?",
      ['Present & Debate, Teach & Participate in seminars, Join professional organisations, Write reports',
       'Sleep all day and avoid speaking',
       'Never ask for feedback',
       'Avoid all professional organisations'],
      0,
      'Present & Debate, Teach & Participate in seminars, Join professional organisations, Write reports are ways to acquire communication skills.',
      """
### Why this is the answer
How to acquire communication skills slide: \"We acquire them through practice. Speak & Write, Present & Debate, Teach & Participate in seminars, Join professional organisations, Write reports, Ask for feedback & record yourself speaking and review performance.\"

### Source
Prof. Ekanola.

### Why the others fail
Sleep all day, never ask feedback, avoid organisations are opposite of practice.
"""),

    q('swep_day2_62',
      "What is the 'farmer, fox, goose, bag of beans' puzzle used to illustrate?",
      ['Critical thinking and problem-solving — solving problems for which there is no obvious answer',
       'Physical strength',
       'Financial accounting',
       'Chemical engineering'],
      0,
      'It illustrates critical thinking/problem-solving for problems with no obvious answer.',
      """
### Why this is the answer
Slide 16 presents farmer puzzle as an easy exercise under Critical Thinking / Problem-Solving: \"A farmer bought a fox, a goose and a bag of beans... If left unattended together the goose will eat beans or fox will eat goose. How did he do it?\" It follows slides on exposing to complex questions, reading widely, comparing perspectives, debating controversial issues, solving problems with no obvious answer.

### Source
Prof. Ekanola.

### Why the others fail
Physical strength, accounting, chemical engineering are not the skill being illustrated.
"""),

    q('swep_day2_63',
      "What is the recommended way to develop adaptability?",
      ['Put yourself outside your comfort zone, learn new skills, take on unfamiliar challenging assignments, work with different people, move across disciplines, learn from failure',
       'Avoid becoming too comfortable is discouraged',
       'Stay in comfort zone forever',
       'Never learn new skills'],
      0,
      'Put outside comfort zone, learn new skills, take unfamiliar assignments, work different people, move across disciplines, learn from failure.',
      """
### Why this is the answer
How to develop adaptability slide: \"Put yourself outside your comfort zone, Learn new skills, Take on unfamiliar, challenging assignments, Work with different people, Move across disciplines, Learn from failure, Avoid becoming too comfortable with what you already know.\"

### Source
Prof. Ekanola.

### Why the others fail
Stay in comfort zone and never learn new skills are opposite; avoiding too comfortable is actually encouraged, so option B misstates.
"""),

    q('swep_day2_64',
      "According to the lecture, what does a portfolio demonstrate that a CV only claims?",
      ['A CV tells what you claim you can do; a portfolio can demonstrate it with evidence of projects, designs, software, etc.',
       'A portfolio is same as CV with no difference',
       'A portfolio is less important than CV',
       'A portfolio should contain only personal photos'],
      0,
      'CV tells claim; portfolio demonstrates with evidence.',
      """
### Why this is the answer
Building a Portfolio slide: \"**A CV tells an employer what you claim you can do. A portfolio can demonstrate it.** A graduate should therefore consider developing a portfolio containing: research projects; presentations; software projects; designs; business ideas; community projects; certificates; professional achievements; evidence of impact.\"

### Source
Prof. Ekanola.

### Why the others fail
Same as CV, less important, only personal photos contradict the evidence-demonstration purpose.
"""),

    q('swep_day2_65',
      "What is the time management advice given in employability lecture?",
      ['Do a time audit, block out distractions, schedule yourself, avoid multitasking, insist others respect your time, keep call to action in mind, get enough downtime and rest',
       'Multitask always and never schedule',
       'Never block distractions',
       'Avoid rest and downtime completely'],
      0,
      'Do time audit, block distractions, schedule, avoid multitasking, insist respect for time, keep call to action, get downtime/rest.',
      """
### Why this is the answer
Time Management slide lists:
- Do a time audit
- Block out distractions
- Schedule yourself
- Avoid multitasking
- Insist that others respect your time
- Keep your call to action in mind
- Get enough down time and rest

### Source
Prof. Ekanola.

### Why the others fail
Always multitask, never block distractions, avoid rest are opposite of advice.
"""),
]
