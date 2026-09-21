#!/usr/bin/env python3
"""SWEP 200 — Day 4 extra 20 questions."""

TOPIC_ID = 'swep-day-4'

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
    q('swep_day4_41',
      "In Food Science lecture, how are Food Science, Food Technology, and Food Engineering distinguished?",
      ['Food Science is study of physical, microbiological, chemical makeup of food; Food Technology is application of food science to selection, preservation, processing, packaging, distribution, use of safe food; Food Engineering is multidisciplinary field applying engineering principles (chemical, mechanical, process) to production, processing, preservation, distribution',
       'All three are exactly same with no difference',
       'Food Science is only about packaging, Technology only about chemistry, Engineering only about marketing',
       'Food Science is about engineering, Technology about science, Engineering about technology only'],
      0,
      'Science studies makeup; Technology applies science to selection/preservation/processing/packaging/distribution/use; Engineering applies engineering principles to production/processing/preservation/distribution.',
      """
### Why this is the answer
Key Words slide defines:
- **Food Science:** study of physical, microbiological, and chemical makeup of food
- **Food Technology:** application of food science to selection, preservation, processing, packaging, distribution, and use of safe food
- **Food Engineering:** multidisciplinary field that applies engineering principles, such as chemical, mechanical and process engineering to production, processing, preservation and distribution

### Source
Dr. Adebayo, Food Science & Engineering — Key Words.

### Why the others fail
Same, swapped, or marketing-only definitions contradict the three-tier distinction.
"""),

    q('swep_day4_42',
      "Which are branches of Food Science as listed?",
      ['Food Chemistry, Processing, Food Nutrition, Food Microbiology, Food Sensory, New Product Development',
       'Only Food Chemistry',
       'Only Processing and Nutrition',
       'Food Safety Engineering, Sustainability, Process Engineering, Packaging Engineering, Equipment Design, Refrigeration'],
      0,
      'Food Chemistry, Processing, Nutrition, Microbiology, Sensory, New Product Development are Food Science branches.',
      """
### Why this is the answer
Branches of Food Science slide lists:
- Food Chemistry
- Processing
- Food Nutrition
- Food Microbiology
- Food Sensory
- New Product Development

Branches of Food Engineering are different: Food Safety Engineering, Sustainability and waste management, Process Engineering, Packaging Engineering, Equipment Design, Refrigeration and Cold Chain.

### Source
Dr. Adebayo.

### Why the others fail
Only one or two branches miss full list; engineering branches belong to Food Engineering, not Food Science.
"""),

    q('swep_day4_43',
      "Which are branches of Food Engineering as listed?",
      ['Food Safety Engineering, Sustainability and waste management, Process Engineering, Packaging Engineering, Equipment Design, Refrigeration and Cold Chain',
       'Food Chemistry, Food Microbiology, Food Sensory',
       'Only Equipment Design',
       'Only Refrigeration'],
      0,
      'Food Safety Engineering, Sustainability/waste, Process, Packaging, Equipment Design, Refrigeration/Cold Chain are Food Engineering branches.',
      """
### Why this is the answer
Branches of Food Engineering slide lists exactly those six.

### Source
Dr. Adebayo.

### Why the others fail
Chemistry/Microbiology/Sensory are Food Science branches; only one branch misses others.
"""),

    q('swep_day4_44',
      "What is value-addition and its impact on national development?",
      ['Value-addition involves transformation of raw agricultural produce into more desirable, convenient, nutritious products to increase market value, shelf life, acceptability; impact: economic growth, FOOD SECURITY and waste management, rural development, health and nutrition, industrial and technological advancement',
       'Value-addition is only about increasing price with no other impact',
       'Value-addition has no impact on national development',
       'Value-addition only reduces shelf life'],
      0,
      'Transformation of raw produce into more desirable/convenient/nutritious products to increase value, shelf life, acceptability; drives economic growth, food security, rural development, health, industrial advancement.',
      """
### Why this is the answer
Key Words cont'd slide: \"Value-Addition: This involves foods transformation of raw agricultural produce into more desirable, convenient, and nutritious products to increase their market value, shelf life and consumers' acceptability\" Impact: \"Value addition contributes to national development by driving economic growth, improving FOOD SECURITY and fostering social progress – economic growth; FOOD SECURITY and waste management; rural development; health and nutrition; industrial and technological advancement\"

### Source
Dr. Adebayo.

### Why the others fail
Only price, no impact, reduces shelf life contradict definition.
"""),

    q('swep_day4_45',
      "What is the definition of Food Security and its dimensions?",
      ['Food security exists when all people, at all times, have physical and economic access to sufficient, safe and nutritious food that meets dietary needs and preferences for active healthy life; dimensions: availability, access (entitlements), utilization (adequate diet, clean water, sanitation, health care), stability (access at all times, not risk losing due to shocks or seasonal)',
       'Food security is only about having enough food sometimes',
       'Food security has only one dimension: availability',
       'Food security is only about importation'],
      0,
      'Food security when all people at all times have physical/economic access to sufficient safe nutritious food; dimensions availability, access, utilization, stability.',
      """
### Why this is the answer
Food Security slide gives full definition and four dimensions with explanations:
- Availability: sufficient quantities of appropriate quality, domestic production or imports including food aids
- Access: adequate resources (entitlements) for nutritious diet
- Utilization: adequate diet, clean water, sanitation, health care to reach nutritional well-being — non-food inputs importance
- Stability: must have access at all times, not risk losing due to sudden shocks (economic/climatic crisis) or cyclical events (seasonal food insecurity)

### Source
Dr. Adebayo.

### Why the others fail
Sometimes only, one dimension, only importation miss full definition.
"""),

    q('swep_day4_46',
      "In Fire Awareness, what are the basic necessities of human life mentioned and what serves as natural detector of fire?",
      ['Food, shelter, clothing are basic necessities; human brain and sensory organs such as olfactory lobes for smell serve as natural detectors of dangers like fire',
       'Only food is necessity; no natural detector',
       'Food, shelter, clothing, and internet are necessities; eyes only detector',
       'Only clothing is necessity'],
      0,
      'Food, shelter, clothing are basic necessities; brain and sensory organs like olfactory lobes for smell are natural detectors.',
      """
### Why this is the answer
Introduction & Fundamental Concepts slide: \"The basic necessities of human life are food, shelter, and clothing. The human brain and sensory organs (such as the olfactory lobes for smell) serve as natural detectors of potential dangers that could lead to disasters like fire outbreaks.\"

### Source
Mr. Ibrahim, Fire Awareness.

### Why the others fail
Only one necessity, internet added, only eyes miss the stated necessities and olfactory lobes.
"""),

    q('swep_day4_47',
      "What are natural and biological causes of fire outbreaks listed?",
      ['Natural igniter: lightning and thunder; Biological/Animal: house pests or rodents gnawing through electrical wires',
       'Natural igniter: only human carelessness; Biological: only plants',
       'Natural igniter: rain; Biological: only birds',
       'No natural causes exist'],
      0,
      'Natural: lightning and thunder; Biological/animal: pests/rodents gnawing wires.',
      """
### Why this is the answer
Causes slide lists: Natural igniter: Lightning and thunder. Biological/Animal causes: House pests or rodents gnawing through electrical wires. Plus negligence & human error, statistical insight OAU hostels.

### Source
Mr. Ibrahim.

### Why the others fail
Human carelessness is negligence not natural; rain, birds, no natural causes contradict slide.
"""),

    q('swep_day4_48',
      "What are volatile solvents & chemicals listed as common sources of fire?",
      ['Perfumes, alcohol, and illicit substances like Colorado (Indian hemp / synthetic cannabis)',
       'Only water',
       'Only sand',
       'Only wood'],
      0,
      'Perfumes, alcohol, Colorado (Indian hemp/synthetic cannabis) are volatile solvents/chemicals.',
      """
### Why this is the answer
Common Sources & Volatile Substances slide lists: Flammable Gases: Acetylene, Butane, Methane. Volatile Solvents & Chemicals: Perfumes, Alcohol, and illicit substances like Colorado (Indian hemp / synthetic cannabis).

### Source
Mr. Ibrahim.

### Why the others fail
Water, sand, wood alone miss the volatile solvents category.
"""),

    q('swep_day4_49',
      "What is the OAU hostel fire outbreak ranking from most to least frequent?",
      ['Moremi Hall (most frequent) → Akintola Hall → Alumni Hall → Mozambique Hall → Postgraduate (PG) Hall (least)',
       'PG Hall most, Moremi least',
       'Alumni most, Akintola least',
       'All hostels equal frequency'],
      0,
      'Moremi most → Akintola → Alumni → Mozambique → PG least.',
      """
### Why this is the answer
Statistical Insight slide: \"According to historical fire outbreak statistics at OAU, hostels with highest occurrence ordered as: Moremi Hall (Most frequent), Akintola Hall, Alumni Hall, Mozambique Hall, Postgraduate (PG) Hall\"

### Source
Mr. Ibrahim.

### Why the others fail
Reversed or equal frequency contradict ranking.
"""),

    q('swep_day4_50',
      "In AI lecture, what is Teachable Machine and its requirement?",
      ['Google Teachable Machine at teachablemachine.withgoogle.com — no coding required, uses webcam, record 20–30 samples per class, model learns by generalising not memorising',
       'A machine that requires PhD coding and 1000 samples per class minimum',
       'A machine that only works with text',
       'A machine that memorises only'],
      0,
      'Teachable Machine at teachablemachine.withgoogle.com, no coding, webcam, 20–30 samples per class, generalising not memorising.',
      """
### Why this is the answer
Demo 1 slide: Teachable Machine (image recognition) at teachablemachine.withgoogle.com — no coding required, uses webcam, record 20–30 samples per class. Takeaway: Model learns by generalising, not memorising. Opposite failure is overfitting (crammer).

### Source
Dr. Lawal, AI lecture — Demo 1 and Limitations.

### Why the others fail
PhD coding, 1000 samples, only text, only memorising contradict no-coding, 20–30 samples, generalising.
"""),

    q('swep_day4_51',
      "What does the AI lecture say about ChatGPT's operation?",
      ['ChatGPT does not think, it predicts based on learned text patterns through probability, not understanding — predicts next word',
       'ChatGPT thinks like human with consciousness',
       'ChatGPT only retrieves pre-written answers',
       'ChatGPT understands sarcasm perfectly'],
      0,
      'ChatGPT does not think, it predicts next word based on learned text patterns via probability, not understanding.',
      """
### Why this is the answer
Demo 2: \"ChatGPT or any LLM (Large Language Model)\" shows how AI predicts next word using pattern recognition from large datasets. Central takeaway: \"ChatGPT does not think, it predicts based on learned text patterns.\" Students type partial sentence \"Once upon a time, there was a ___\" guess next word, reveal ChatGPT prediction. Discussion: how it works through probability, not understanding. Connects to Lack of Context limitation.

### Source
Dr. Lawal.

### Why the others fail
Thinks like human, retrieves pre-written answers, understands sarcasm perfectly contradict probability not understanding and lack of context.
"""),

    q('swep_day4_52',
      "What are the four AI challenges listed?",
      ['Data privacy, bias and fairness, job displacement, lack of regulation',
       'Only data privacy',
       'Only job displacement',
       'Only lack of regulation'],
      0,
      'Data privacy, bias and fairness, job displacement, lack of regulation are challenges.',
      """
### Why this is the answer
Challenges slide lists: data privacy, bias and fairness, job displacement, lack of regulation. Ways forward: ethical AI, inclusive data, policies, human-AI collaboration.

### Source
Dr. Lawal.

### Why the others fail
Only one challenge misses other three.
"""),

    q('swep_day4_53',
      "What are the ways forward for AI challenges?",
      ['Ethical AI, inclusive data, policies, human-AI collaboration',
       'Only ethical AI',
       'Only ban AI',
       'Only ignore challenges'],
      0,
      'Ethical AI, inclusive data, policies, human-AI collaboration are ways forward.',
      """
### Why this is the answer
Ways forward slide: ethical AI, inclusive data, policies, human-AI collaboration.

### Source
Dr. Lawal.

### Why the others fail
Only one, ban, ignore miss comprehensive forward path.
"""),

    q('swep_day4_54',
      "What is comparative safety vs absolute safety in fire lecture?",
      ['Comparative safety = manage it inside; Absolute safety = evacuate',
       'Comparative safety = evacuate; Absolute safety = manage inside',
       'Both mean evacuate',
       'Both mean manage inside'],
      0,
      'Comparative safety manage inside; Absolute safety evacuate.',
      """
### Why this is the answer
Slide: \"Comparative safety = manage it inside; Absolute safety = evacuate.\" Also: In smoke: toxic smoke rises — lie flat and crawl.

### Source
Mr. Ibrahim.

### Why the others fail
Swapped or both same contradict definition.
"""),

    q('swep_day4_55',
      "What should you do in smoke during fire outbreak?",
      ['Toxic smoke rises — lie flat and crawl',
       'Stand up and run upright quickly',
       'Jump from building immediately',
       'Stay standing and inhale smoke'],
      0,
      'Toxic smoke rises — lie flat and crawl.',
      """
### Why this is the answer
Slide: \"In smoke: toxic smoke rises — lie flat and crawl.\"

### Source
Mr. Ibrahim.

### Why the others fail
Standing upright, jumping, inhaling smoke are unsafe — smoke rises, so low is safer.
"""),

    q('swep_day4_56',
      "In Food lecture, what does the speaker's contact info include?",
      ['Dr. W. A. Adebayo (Food Process Engineering) adebayow@oauife.edu.ng; +234808060410278, Department of Food Science and Technology, OAU Ile-Ife',
       'No contact info given',
       'Only email without phone',
       'Only phone without email'],
      0,
      'Dr. W. A. Adebayo, Food Process Engineering, adebayow@oauife.edu.ng, +234808060410278, Dept of Food Science and Technology, OAU.',
      """
### Why this is the answer
Title slide includes: Dr. W. A. Adebayo (Food Process Engineering) adebayow@oauife.edu.ng; +234808060410278 Department of Food Science and Technology, OAU Ile-Ife.

### Source
Dr. Adebayo title slide.

### Why the others fail
No contact, only one, contradict slide which has both email and phone.
"""),

    q('swep_day4_57',
      "What is the industrial revolution timeline mentioned as trap to watch?",
      ['1IR 1760–1840; 2IR 1860–1930 — do not swap',
       '1IR 1860–1930; 2IR 1760–1840',
       '1IR 1900–2000; 2IR 2000–2020',
       '1IR and 2IR same period'],
      0,
      '1IR 1760–1840; 2IR 1860–1930.',
      """
### Why this is the answer
Traps to watch slide for Day 4: \"1IR 1760–1840; 2IR 1860–1930 — do not swap.\"

### Source
Day 4 summaryNotes traps.

### Why the others fail
Swapped, modern dates, same period are traps.
"""),

    q('swep_day4_58',
      "What is graphene property mentioned as trap?",
      ['200× stronger than steel but one million times thinner than hair',
       'Same strength as steel and same thickness as hair',
       'Weaker than steel and thicker than hair',
       'Only stronger but not thinner'],
      0,
      '200× stronger than steel but one million times thinner than hair.',
      """
### Why this is the answer
Traps slide: \"Graphene: 200× stronger than steel but one million times thinner than hair.\"

### Source
Day 4 summaryNotes.

### Why the others fail
Same, weaker, only stronger miss exact figures.
"""),

    q('swep_day4_59',
      "In AI, what is the definition of model accuracy caution?",
      ['High accuracy is good, but what kinds of errors is the model making? — example biased data: Western names vs African names',
       'High accuracy means no errors ever',
       'Accuracy is irrelevant',
       'Only low accuracy matters'],
      0,
      'High accuracy good, but what kinds of errors? Example Western vs African names bias.',
      """
### Why this is the answer
Model Accuracy slide caution: \"Key Point: High accuracy is good, but what kinds of errors is the model making?\" Example: language model trained mostly on Western names might struggle with African names, even at high headline accuracy.

### Source
Dr. Lawal.

### Why the others fail
No errors ever, irrelevant, only low accuracy miss the caution about error types and bias.
"""),

    q('swep_day4_60',
      "What is the colour band for CO2 extinguisher and its property?",
      ['BLACK band — multipurpose for electrical + liquids and leaves no residue',
       'RED band — water only and leaves residue',
       'BLUE band — dry powder only',
       'CREAM band — foam only'],
      0,
      'BLACK band CO2 — multipurpose electrical + liquids, leaves no residue.',
      """
### Why this is the answer
Colour bands slide: RED water, BLUE dry powder, CREAM foam, BLACK CO2. CO2 is multipurpose (electrical + liquids) and leaves no residue.

### Source
Mr. Ibrahim, Types of Fire Extinguishers & Color Codes.

### Why the others fail
Red is water, blue dry powder, cream foam — only black is CO2 with no residue property.
"""),
]
