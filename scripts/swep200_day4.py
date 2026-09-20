#!/usr/bin/env python3
"""SWEP 200 - Day 4 question bank (40 questions).

Day 4: Thursday, 17th September. Three lectures, per the orientation ledger:
  1. Food Science & Engineering, Value-Addition and National Development (4IR)
                                            - Dr. W. A. Adebayo
  2. Demystifying Artificial Intelligence   - Dr. Aderonke Lawal
  3. Fire Awareness and Prevention          - Mr. M. A. Ibrahim

Authored from the source decks to the tertiary-examination standard of
Days 1-3, with the extra emphasis the course owner requested on
ACRONYMS/ABBREVIATIONS WITH FULL MEANINGS and on STATISTICAL STATEMENTS.

Weighting by material volume: Food Science/4IR 15, AI 13, Fire 12.

Verified page by page against:
  * SWEP 2026 Food Science and Technology and National Development (39 pp.)
  * Demystifying AI - SWEP200 - Dr. Lawal (27 pp.)
  * Fire Awareness and Prevention Notes v2 (3 pp.)
  * Handwritten Day 4 orientation ledger (speaker attributions)
"""

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
    # ============ Food Science, Value-Addition & 4IR (Dr. W. A. Adebayo) ======
    q('swep_day4_01',
      'Dr. W. A. Adebayo distinguishes three related terms. Which definition is correctly matched?',
      ['Food Science — the application of food science to selection, preservation, processing, packaging and distribution',
       'Food Technology — the study of the physical, microbiological and chemical makeup of food',
       'Food Engineering — the multidisciplinary field applying engineering principles to production, processing, preservation and distribution of foods',
       'Food Engineering — the study of consumer sensory preferences and new product development'],
      2,
      'Food Engineering applies engineering principles to food production and processing.',
      """
### Why this is the answer
The three key words are defined separately, and the distractors swap them:

| Term | Definition |
|---|---|
| **Food Science** | The **study** of the physical, microbiological and chemical **makeup** of food |
| **Food Technology** | The **application** of food science to selection, preservation, processing, packaging, distribution and use of **safe** food |
| **Food Engineering** | The **multidisciplinary field** applying **engineering principles** — chemical, mechanical, process — to production, processing, preservation and distribution |

### The logic that separates them
**Science studies it. Technology applies it. Engineering builds the systems.**
Only Food Engineering invokes *engineering principles* by name.

### The branches of each
- **Food Science:** food chemistry, processing, food nutrition, food microbiology,
  food sensory, new product development
- **Food Engineering:** food safety engineering, sustainability and waste
  management, process engineering, packaging engineering, equipment design,
  refrigeration and cold chain

### Source
Dr. W. A. Adebayo, "Key Words" and "Branches" slides.

### Why the others fail
Options A and B are genuine definitions attached to the **wrong term**. Option D
lists *food sensory* and *new product development*, which are branches of Food
**Science**, not the definition of Food Engineering.
"""),

    q('swep_day4_02',
      'According to the lecture, what is Value-Addition in food systems?',
      ['The taxation applied to processed food products before sale',
       'The transformation of raw agricultural produce into more desirable, convenient and nutritious products to increase market value, shelf life and consumer acceptability',
       'The addition of artificial preservatives to extend expiry dates',
       'The increase in farm-gate prices caused by seasonal scarcity'],
      1,
      'Value-addition transforms raw produce into more desirable, convenient, nutritious products.',
      """
### Why this is the answer
Value-addition *"involves food transformation of **raw agricultural produce**
into more **desirable, convenient, and nutritious** products to increase their
**market value, shelf life and consumers' acceptability**."*

Three inputs to remember — desirable, convenient, nutritious — and three outputs:
market value, shelf life, acceptability.

### Its impact on national development
Value addition contributes to national development by driving economic growth,
improving **FOOD SECURITY** and fostering social progress, specifically through:

| Channel |
|---|
| Economic growth |
| **Food security** and waste management |
| Rural development |
| Health and nutrition |
| Industrial and technological advancement |

### Why option C is a near-miss
Extending shelf life **is** one of the three stated outputs — but through
*transformation* into better products, not merely by dosing raw produce with
preservatives. The definition is about **upgrading the product**, not
stabilising it.

### Source
Dr. W. A. Adebayo, "Key Words (Cont'd)" slide.
"""),

    q('swep_day4_03',
      'The lecture gives a formal definition of Food Security. Which statement matches it?',
      ['Food security exists when a country produces all of its own food without imports',
       'Food security exists when all people, at all times, have physical and economic access to sufficient, safe and nutritious food meeting their dietary needs and food preferences for an active and healthy life',
       'Food security exists when national strategic grain reserves exceed one year of consumption',
       'Food security exists when food prices remain stable throughout the year'],
      1,
      'All people, at all times, with physical and economic access to sufficient, safe, nutritious food.',
      """
### Why this is the answer
The definition is quoted precisely: *"Food security **only exists when all
people, at all times**, have **physical and economic access** to **sufficient,
safe and nutritious** food that meets their **dietary needs and food
preferences** for an active and healthy life."*

Every clause is load-bearing — **all** people, at **all** times, with **both**
physical and economic access.

### The four dimensions it points to
| Dimension | What it means |
|---|---|
| **Availability** | Sufficient quantities of appropriate quality, from domestic production **or imports (including food aid)** |
| **Access** | Individuals' adequate resources — **entitlements** — to acquire appropriate foods |
| **Utilization** | Adequate diet, **clean water, sanitation and health care** to reach nutritional well-being |
| **Stability** | Access at **all times**, without risk from sudden shocks (economic/climatic) or cyclical events (seasonal insecurity) |

**Utilization** is the dimension students overlook — it shows that **non-food
inputs** matter to food security.

### Why option A is wrong
Availability explicitly includes **imports**. Producing everything yourself is
**autarky**, a different concept the lecture treats separately.

### Source
Dr. W. A. Adebayo, "Food Security" slides.
"""),

    q('swep_day4_04',
      'The lecture contrasts autarky with food self-reliance. Which description of AUTARKY is correct?',
      ['A country controlling its food needs through integrated management of production, export, import, storage and distribution',
       'A system of producing only those foods in which a country has comparative advantage',
       'A policy of maintaining strategic food reserves for natural disasters',
       'A deliberate economic policy of isolating a country to attain food self-sufficiency and eliminate international trade'],
      3,
      'Autarky is deliberate isolation to attain self-sufficiency and eliminate international trade.',
      """
### Why this is the answer
**Autarky** is *"the situation whereby a country embarks on a **deliberate
economic policy of isolating itself** in order to attain food self-sufficiency
and **eliminate international trade**."* It is explicitly described as *"the
opposite of free trade and open market system."*

### Historical examples given
Some Asiatic countries attempted this extreme policy: **China during the
Cultural Revolution** led by the late **Mao Tse Tung**, **Japan's isolation**,
and **North Korea**.

### The contrast being tested
| Concept | Stance on trade |
|---|---|
| **Autarky** | **Eliminates** international trade — isolation |
| **Food self-reliance** | **Manages** trade — production, **export, import**, storage, distribution |

Every other option describes **food self-reliance**: integrated management,
strategic reserves for emergencies, and producing where you hold **comparative
advantage**. Self-reliance is control, not isolation — that is the whole
distinction.

### Source
Dr. W. A. Adebayo, "The State of Food Security in Nigeria" slides.
"""),

    q('swep_day4_05',
      'How does the lecture define an Industrial Revolution (IR), and what are its causative agents?',
      ['A gradual improvement in factory output; agents are labour, capital and land',
       'A change in consumer taste; agents are advertising, media and fashion',
       'A political reorganisation of industry; agents are government, unions and investors',
       'An abrupt and radical change where new technologies or novel ways of perceiving the world trigger profound change in economic systems and social structures; agents are energy, communication and transportation'],
      3,
      'An IR is abrupt, radical change driven by energy, communication and transportation.',
      """
### Why this is the answer
The lecture first defines the word: *"By the word **'revolution'**, we mean
**'abrupt and radical change'**."* It then notes that *no society is static —
every society is perpetually in transition*.

An **Industrial Revolution (IR)** *"occurs when **new technologies and/or novel
ways of perceiving the world** trigger **profound change in economic systems and
social structures**."*

### The three causative agents
> **Energy · Communication · Transportation**

These three recur throughout the lecture: the **Agrarian Revolution**, the
**1IR** and the **2IR** are each said to have changed *energy/production systems,
transportation systems and communication systems*. That repetition is the
lecture's structural spine.

### The Agrarian Revolution — what came before
Prior to industrialisation, early men and women were **foraging** — gatherers of
fruits and hunters of animals. The transition to **farming and domestication of
animals**, using the combined efforts of **humans plus animals**, produced the
same three changes.

### Source
Dr. W. A. Adebayo, "Industrial Revolutions" slides.
"""),

    q('swep_day4_06',
      'What are the stated dates and defining transition of the First Industrial Revolution (1IR)?',
      ['1760–1840 in Britain; transition from muscle/animal power to mechanical power',
       '1860–1930 in Germany; transition to electric power and assembly lines',
       '1760–1840 in France; transition from agriculture to trade',
       '1800–1900 in Britain; transition from steam to electricity'],
      0,
      '1760–1840 in Britain, from muscle/animal power to mechanical power.',
      """
### Why this is the answer
The 1IR *"happened in the mid-18th to mid-19th Century. Precisely **1760–1840
in Britain**. It marked transition from **muscle/animal power to mechanical
power**. The transition to use of machines led to the **birth of the
factories**."*

### The full timeline of revolutions
| Revolution | Dates | Defining change |
|---|---|---|
| **1IR** | **1760–1840**, Britain | Muscle/animal → **mechanical power**; birth of factories |
| **2IR** | **1860–1930** | **Electricity**, electrically driven production and assembly lines; **mass production** |
| **3IR** | Began **1960s** | **Computer and information age** |
| **4IR** | Began about **2000** | Fusion of physical, digital and biological technologies |

### The trap in option B
**1860–1930** is real — but it belongs to the **2IR**, and the deck does not
attribute it to Germany. Adjacent-revolution dates are the sharpest distractors
in this topic, so anchor each pair firmly.

### Source
Dr. W. A. Adebayo, "First Industrial Revolution" and "Second Industrial
Revolution" slides.
"""),

    q('swep_day4_07',
      'The Second Industrial Revolution (2IR) is said to have been heralded by which development, producing what economic outcome?',
      ['The steam engine, producing the factory system',
       'The internet, producing the digital economy',
       'The semiconductor, producing the information economy',
       'The advent of electricity and electrically driven production/assembly lines, producing mass production or a manufacturing economy'],
      3,
      'Electricity and electrically driven assembly lines produced mass production.',
      """
### Why this is the answer
The 2IR occurred *"late in the 19th to early 20th Century. Precisely
**1860–1930**"*, and was heralded by:

- the **advent of electricity**, that is, **electric power**
- **electrically driven production and assembly lines**

*"This massive leap in power generation gave birth to **mass production or
manufacturing economy**."* Like its predecessors, the 2IR also changed
**energy/production, transportation and communication** systems.

### Matching each driver to its revolution
| Driver | Revolution |
|---|---|
| Steam / mechanical power | **1IR** |
| **Electricity** | **2IR** |
| **Semiconductors, computing** | **3IR** |
| Fusion of physical/digital/biological | **4IR** |

Every distractor here is a genuine driver — of a **different** revolution. The
internet in particular belongs to the **3IR** (the 1990s catalyst), not the 2IR.

### Source
Dr. W. A. Adebayo, "Second Industrial Revolution (2IR)" slide.
"""),

    q('swep_day4_08',
      'According to the lecture, what catalysed the Third Industrial Revolution (3IR), and when did it begin?',
      ['Began in the 1940s; catalysed by the telegraph and radio',
       'Began in the 1960s; catalysed by semiconductors, mainframe computing (1960s), personal computing (1970s–1980s) and the internet (1990s)',
       'Began in the 1980s; catalysed by mobile telephony and satellites',
       'Began about 2000; catalysed by artificial intelligence and robotics'],
      1,
      'The 3IR began in the 1960s, catalysed by semiconductors, computing and the internet.',
      """
### Why this is the answer
The 3IR *"began in the **1960s**. This was/is the **COMPUTER and INFORMATION
age**."* It was catalysed by:

| Catalyst | Era |
|---|---|
| Development of **semiconductors** | — |
| **Mainframe computing** | 1960s |
| **Personal computing** | 1970s + 1980s |
| **Internet** | 1990s |

### Its main driver — a convergence
The lecture names the convergence of:
- **Renewable energy** — which could lead to an **energy internet**
- **ICT** — clever software + internet
- **3D printing**

The fuller list of converging technologies: *clever software, novel materials,
more dexterous robots, new processes, and 3D printing* — described as *"the
wonders of the 3IR"*.

### Why option D is the trap
About **2000** is when the **4IR** began — and the deck stresses the 4IR is *"an
**offshoot of the 3IR**, because it builds on computer and information
revolutions"*. Some academics even argue they are not distinct.

### Source
Dr. W. A. Adebayo, "Third Industrial Revolution (3IR)" slides.
"""),

    q('swep_day4_09',
      'What makes the Fourth Industrial Revolution (4IR) fundamentally different from previous industrial revolutions?',
      ['Its reliance on fossil fuels for mass production',
       'Its rejection of computing in favour of biological systems',
       'Its confinement to the manufacturing sector alone',
       'The fusion of different technologies and their interaction across the physical, digital and biological domains'],
      3,
      'The fusion and interaction of technologies across physical, digital and biological domains.',
      """
### Why this is the answer
*"It is the **fusion of different technologies and their interaction across the
physical, digital and biological domains** that make the 4IR **fundamentally
different** from previous IRs."*

### The three clusters
> **Physical · Digital · Biological**
> *"All three are deeply interrelated and the various technologies benefit from
> each other based on the discoveries and progress each makes."*

### Its distinguishing characteristics
- Much more **ubiquitous and mobile internet**
- **Smaller and more powerful sensors** that have become **cheaper**
- **Artificial Intelligence (AI) and Machine Learning**

By enabling **"SMART FACTORIES"**, the 4IR creates a world in which **virtual and
physical systems of manufacturing cooperate flexibly**.

### Its impacts
Described as **HISTORIC, PROFOUND, DISRUPTIVE and MULTIFACETED** — disrupting
incumbents and reshaping production, consumption, transportation and delivery.
This **PARADIGM SHIFT** is *"fundamentally changing the way we live, work, and
relate to one another."*

### Source
Dr. W. A. Adebayo, "Fourth Industrial Revolution (4IR)" slides.
"""),

    q('swep_day4_10',
      'Under the Physical MegaTrend of the 4IR, the lecture cites an advanced material with specific properties. Which material and figures are given?',
      ['Kevlar — 100 times stronger than steel and twice as thin as human hair',
       'Carbon fibre — 50 times stronger than steel and a poor conductor of heat',
       'Graphene — 200 times stronger than steel, one million times thinner than human hair, and a good conductor of heat and electricity',
       'Titanium alloy — 200 times stronger than steel and self-healing'],
      2,
      'Graphene: 200× stronger than steel, one million times thinner than human hair.',
      """
### Why this is the answer
Under **New Materials**, the lecture describes smart materials that are
**self-healing, self-cleaning**, and **metals with memory** (which revert to
their original shapes). Its named example is:

> **Graphene** — *"an advanced material which is **200 times stronger than
> steel**, **one million times thinner than human hair**, and also a **good
> conductor of heat and electricity**."*

Three figures, all examinable: **200×**, **one million×**, and **good conductor**
of both heat and electricity.

### The full Physical MegaTrend
| Trend | Detail |
|---|---|
| **Autonomous vehicles** | Driverless cars, trucks, **drones, aircraft, boats and submersibles** |
| **3D Printing** | Creates a physical object layer upon layer from a digital 3D drawing |
| **Advanced Robotics** | Now across **all sectors** — military, nursing, agriculture; modern robots **access information remotely and act autonomously** instead of being programmed |
| **New Materials** | Self-healing, self-cleaning, memory metals — **graphene** |

### Source
Dr. W. A. Adebayo, "Physical MegaTrend" slides.
"""),

    q('swep_day4_11',
      'How does the lecture define the Internet of Things (IoT) under the Digital MegaTrend?',
      ['A network of undersea fibre-optic cables linking continents',
       'A protocol for encrypting mobile banking transactions',
       'A cloud storage service for industrial data archives',
       'Physical objects with sensors, processing ability, software and other technologies that connect and exchange data with other devices and systems over the internet or other communication networks'],
      3,
      'IoT is physical objects with sensors and software exchanging data over networks.',
      """
### Why this is the answer
The **Internet of Things (IoT)** *"describes **physical objects with sensors,
processing ability, software and other technologies** that **connect and
exchange data** with other devices and systems over the internet or other
communication networks."*

Note the four attributes an IoT object must have: **sensors, processing ability,
software, and connectivity**.

### The scale given
*"**Billions** of devices — smartphones, tablets, and computers — are connected
to the Internet and also **interconnected**."* Such monitoring systems can track
the **movement and trailing of objects and people**.

### The Biological MegaTrend, for contrast
Mainly in **Genetics** — *"not in the realm of simple biotechnology,
bioengineering or genetic modification"* — made possible by huge computing power
in **Bioinformatics**. Its benefits:
- Increasing ease of **gene sequencing**
- **Gene activation**
- **Gene editing** — ability to edit DNA and alter traits
- **Synthetic biology** — ability to customise by **writing DNA**

### Source
Dr. W. A. Adebayo, "Digital MegaTrend" and "Biological MegaTrend" slides.
"""),

    q('swep_day4_12',
      'The lecture prescribes four types of intelligence for navigating the 4IR. Which pairing of intelligence to its seat is correct?',
      ['Contextual intelligence — the heart', 'Emotional intelligence — the mind',
       'Inspired intelligence — the body', 'Physical intelligence — the body'],
      3,
      'Physical intelligence has to do with the body.',
      """
### Why this is the answer
To adapt, shape and harness the potential of disruption, the lecture says we
must nurture and apply **four different types of intelligence**, each tied to a
different seat:

| Intelligence | Seat | What it is about |
|---|---|---|
| **Contextual** | **Mind** | How we **understand and apply knowledge** — a prerequisite for adaptation and survival |
| **Emotional** | **Heart** | How we **process and integrate thoughts and feelings** and relate to ourselves and one another |
| **Inspired** | **Soul** | **Inspiration from the spiritual realm** |
| **Physical** | **Body** | **Self-preservation** — supporting and nourishing personal health and well-being |

Only **Physical → body** is correctly paired.

### The framing sentence
*"We can only meaningfully address these challenges if we mobilize the
**collective wisdom of our minds, hearts and souls**."* Mind, heart, soul — and
then body — is the exact order the four intelligences follow.

### On physical intelligence
Advances such as **implantable technologies** and **telemedicine** have positive
effects on it.

### Source
Dr. W. A. Adebayo, "How do I prepare to manage the impacts of the 4IR?" slides.
"""),

    q('swep_day4_13',
      'Which of the following is NOT listed among the impacts of the 4IR on value-addition in food systems?',
      ['Enhanced processing and efficiency through automation, robotics, IoT and smart sensors',
       'Improved product quality and innovation through AI, machine learning and 3D food printing',
       'Supply chain optimization through blockchain, traceability and cold chain technologies',
       'Elimination of the need for food safety regulation and inspection'],
      3,
      'Eliminating food safety regulation is not a listed impact.',
      """
### Why this is the answer
A **NOT** question. The lecture lists exactly four impacts of the 4IR on
value-addition in food systems:

| Impact | Enabling technologies |
|---|---|
| **Enhanced processing and efficiency** | Automation and robotics; **IoT and smart sensors** |
| **Improved product quality and innovation** | AI and machine learning; **3D food printing** |
| **Supply chain optimization** | **Blockchain and traceability**; cold chain technologies |
| **Consumer-centric value addition** | **Big data and AI**; smart packaging |

Nothing suggests regulation disappears — and it would contradict the deck, which
names **Food Safety Engineering** as a branch of food engineering.

### Note the fourth impact
**Consumer-centric value addition** is the one students forget, since the first
three are process-facing and only this one is customer-facing.

### The closing provocation
*"Now that **5IR** is fast approaching, what are your Plans/Preparations?"* —
the lecture ends by pointing past the 4IR entirely.

### Source
Dr. W. A. Adebayo, "Impacts of 4IR on Value-addition in Food Systems" slide.
"""),

    q('swep_day4_14',
      'Which two of the four food security dimensions are correctly described?',
      ['Availability — access by individuals to adequate resources or entitlements; Stability — sufficient quantities of appropriate quality',
       'Access — adequate diet, clean water, sanitation and health care; Utilization — sufficient quantities from domestic production or imports',
       'Availability — sufficient quantities of appropriate quality from domestic production or imports; Stability — access to adequate food at all times, without risk from sudden shocks or cyclical events',
       'Utilization — access at all times without risk of shocks; Access — clean water and sanitation'],
      2,
      'Availability is sufficient quantity/quality; Stability is access at all times.',
      """
### Why this is the answer
The four dimensions are distinct, and every distractor shuffles them:

| Dimension | Correct description |
|---|---|
| **Availability** | Sufficient **quantities** of appropriate **quality**, supplied through **domestic production or imports (including food aids)** |
| **Access** | Access by individuals to adequate **resources (entitlements)** for acquiring appropriate foods for a nutritious diet |
| **Utilization** | Adequate **diet, clean water, sanitation and health care** to reach nutritional well-being |
| **Stability** | Access to adequate food **at all times** — no risk of loss from **sudden shocks** (economic/climatic crisis) or **cyclical events** (seasonal insecurity) |

Only option C states two of them correctly.

### The memory hook
**Availability** = is the food *there*? **Access** = can you *get* it?
**Utilization** = can your body *use* it? **Stability** = is it there *always*?

### The wider definition it feeds
**National food security** is *"the ability of a country to ensure on a
**long-term basis** that its food systems provide the total population with
access to **timely, reliable and nutritionally adequate** supply of food."*

### Source
Dr. W. A. Adebayo, "Food Security" slides.
"""),

    q('swep_day4_15',
      'According to the Day 4 ledger, who delivered the lecture on Food Science and the Fourth Industrial Revolution?',
      ['Dr. Aderonke Lawal', 'Mr. M. A. Ibrahim',
       'Dr. W. A. Adebayo', 'Prof. V. Omidiji'],
      2,
      'Dr. W. A. Adebayo delivered the Food Science & 4IR lecture.',
      """
### Why this is the answer
The Day 4 ledger (Thursday, 17th September) records **Food Science & 4IR (4th
Industrial Revolution) — Dr. W. A. Adebayo**, noting that he covered the
branches of food engineering and the concept of food security, highlighting how
the 4IR impacts national development through **value addition and optimized food
systems**.

His title slide confirms: **Dr. W. A. Adebayo (Food Process Engineering),
Department of Food Science and Technology, Obafemi Awolowo University, Ile-Ife**.

### Day 4 at a glance
| # | Lecture | Speaker |
|---|---|---|
| 1 | **Food Science & 4IR** | **Dr. W. A. Adebayo** |
| 2 | Demystifying AI | Dr. Aderonke Lawal |
| 3 | Fire Awareness and Prevention | Mr. M. A. Ibrahim |

### Note the titles
Two **Dr.** and one **Mr.** — Mr. M. A. Ibrahim is the fire-safety speaker.
**Prof. V. Omidiji** is a genuine SWEP lecturer but belongs to **Day 3**
(Workshop Practice, Workforce and National Growth).

### Source
Handwritten "Record of the Orientation Week Activities", Day 4; deck title slide.
"""),

    # ================= Demystifying AI (Dr. Aderonke Lawal) ===================
    q('swep_day4_16',
      'How does Dr. Aderonke Lawal define a model in Artificial Intelligence?',
      ['A physical robot that performs human tasks',
       'A mathematical representation of patterns learned from data',
       'A database of pre-written answers retrieved on request',
       'A programming language used to write intelligent software'],
      1,
      'A model is a mathematical representation of patterns learned from data.',
      """
### Why this is the answer
*"A model is a **mathematical representation of patterns learned from data**. It
functions like a **digital brain** that recognizes patterns."*

The analogy offered: *"A student learns to solve problems by **practicing many
examples**."*

### Why option C is decisively wrong
A model does **not** store answers to retrieve. This is the deck's central
correction: it **learns patterns** and then **generalises** to new data. The
live-demo takeaway makes it explicit — *"Model learns by **generalising, not
memorising**"* — and a model that memorises instead is the defined failure mode
called **overfitting**.

### The AI learning process — big picture
> **Data → Training → Model → Prediction → Feedback → Improved Model**

*"AI systems learn by analyzing data and adjusting over time. The model is
**tested, corrected, and refined**."*

### Source
Dr. Aderonke Lawal, "What Is a Model in AI?" and "The AI Learning Process" slides.
"""),

    q('swep_day4_17',
      'What is the correct order of the six stages in the AI learning process presented in the lecture?',
      ['Training → Data → Model → Feedback → Prediction → Improved Model',
       'Data → Model → Training → Prediction → Improved Model → Feedback',
       'Data → Training → Model → Prediction → Feedback → Improved Model',
       'Model → Data → Training → Feedback → Prediction → Improved Model'],
      2,
      'Data → Training → Model → Prediction → Feedback → Improved Model.',
      """
### Why this is the answer
The lecture numbers the big picture 01 to 06:

| # | Stage |
|---|---|
| 01 | **Data** |
| 02 | **Training** |
| 03 | **Model** |
| 04 | **Prediction** |
| 05 | **Feedback** |
| 06 | **Improved Model** |

### Why the order cannot be rearranged
Each stage consumes the previous one's output. You cannot train without **data**;
the model is what training *produces*, so it cannot precede training; and
feedback is only possible once a **prediction** exists to be judged. The loop
then closes — the improved model becomes the basis for the next round.

### The training steps, made concrete
Using a **cat vs dog classifier**:
1. Collect images of cats and dogs
2. **Label** each image
3. Feed into a **neural network**
4. Adjust internal settings (**weights/biases**)
5. Use the model to classify **new** images

### Source
Dr. Aderonke Lawal, "The AI Learning Process — Big Picture" and "How Training
Works" slides.
"""),

    q('swep_day4_18',
      'In the lecture, how is model Accuracy defined and illustrated?',
      ['The speed at which a model produces predictions, measured in seconds',
       'The number of layers in a neural network',
       'The quantity of data used to train a model, measured in gigabytes',
       'The percentage of correct predictions a model makes — e.g. a facial recognition system correct 95 times out of 100 attempts has 95% accuracy'],
      3,
      'Accuracy is the percentage of correct predictions — 95 of 100 attempts is 95%.',
      """
### Why this is the answer
*"**Accuracy is the percentage of correct predictions** a model makes. It tells
us **how often** the model gets it right."*

The worked example: *"Imagine using a facial recognition system to unlock your
phone. If out of **100 attempts**, the phone correctly recognises your face
**95 times** → **Accuracy = 95%**."*

### The caution attached — and it is the real lesson
> **Key Point:** *"High accuracy is good, **but what kinds of errors is the
> model making?**"*

A model can score well overall and still fail badly on a specific group. That
warning leads directly into the next slide on **biased data producing biased
results** — a language model trained mostly on **Western names** might struggle
with **African names**, even at high headline accuracy.

### Source
Dr. Aderonke Lawal, "Model Accuracy" slide.
"""),

    q('swep_day4_19',
      'The lecture names three limitations of AI models. Which limitation is matched with the correct illustration?',
      ['Overfitting — a chatbot giving wrong advice because it cannot understand sarcasm',
       'Lack of context — a language model trained mostly on Western names struggling with African names',
       'Overfitting — a student who crams past questions but cannot answer new ones in the real exam',
       'Biased data — a model memorising training data but failing on new data'],
      2,
      'Overfitting is illustrated by a student who crams past questions but fails new ones.',
      """
### Why this is the answer
Three limitations, each with its own illustration — and the distractors swap them:

| Limitation | What it is | Illustration |
|---|---|---|
| **Biased Data → Biased Results** | Trained only on certain data types, so unfair or inaccurate | A language model trained mostly on **Western names** struggling with **African names** |
| **Overfitting** | The model **memorises training data** but fails on new data | **A student who crams past questions but can't answer new ones** |
| **Lack of Context** | Models don't **"understand"** like humans do | A chatbot giving wrong advice because it can't understand **sarcasm or emotion** |

Only option C pairs correctly.

### Why the overfitting analogy is so apt for students
It is the exact opposite of the desired behaviour described in the live demo:
*"Model learns by **generalising, not memorising**."* An overfitted model is a
crammer — perfect on the past paper, lost in the exam hall.

### Source
Dr. Aderonke Lawal, "Limitations of AI Models" slide.
"""),

    q('swep_day4_20',
      'Which type of machine learning is defined as learning from labelled data — data that already has the correct answer?',
      ['Unsupervised learning', 'Reinforcement learning',
       'Supervised learning', 'Deep learning'],
      2,
      'Supervised learning learns from labelled data.',
      """
### Why this is the answer
The lecture names three types of learning models:

| Type | Learns from | Analogy given |
|---|---|---|
| **Supervised** | **Labelled data** — already has the correct answer | *"Practising with **past questions and answers** before a test"* |
| **Unsupervised** | **Unlabelled data** — must find patterns itself | *"Sorting your clothes by colour or size **without anyone telling you how**"* |
| **Reinforcement** | **Rewards and penalties** from an environment | *"Learning to ride a bicycle — you **fall, adjust, and improve**"* |

**Supervised learning** is *"like a **teacher** guiding a student by giving both
the question **and the correct answer** during practice."*

### Its real-world examples
- **Email spam detection** — trained on emails labelled "spam" / "not spam"
- **Exam grading apps** — score answers against a bank of correct responses
- **Face unlock** — trained with your labelled face data (your photo = "you")

### Note
**Deep learning** is not one of the three types named in this lecture.

### Source
Dr. Aderonke Lawal, "Types of Learning Models" and "Supervised Learning" slides.
"""),

    q('swep_day4_21',
      'Which real-life example is correctly matched to its type of machine learning?',
      ['Spotify playlist clustering — supervised learning',
       'Google News grouping similar stories — reinforcement learning',
       'Email spam detection — unsupervised learning',
       'Self-driving cars learning to stay in lane by being rewarded — reinforcement learning'],
      3,
      'Self-driving cars learning through rewards is reinforcement learning.',
      """
### Why this is the answer
Each learning type has its own examples in the deck, and the distractors move
them around:

| Example | Correct type |
|---|---|
| Email spam detection | **Supervised** (labelled spam/not spam) |
| Exam grading apps, Face unlock | **Supervised** |
| **Spotify playlist clustering** | **Unsupervised** |
| Customer segmentation, Google News grouping | **Unsupervised** |
| **Self-driving cars rewarded for safe driving** | **Reinforcement** |
| Game AI (**AlphaGo**), personalised ads | **Reinforcement** |

### The test to apply
Ask what the model is given:
- Given **the right answers** → supervised
- Given **nothing but data** → unsupervised
- Given **rewards and penalties** → reinforcement

*"Learn to stay in lane or stop at lights **by being rewarded** for safe
driving"* names the reward mechanism explicitly, so it can only be
reinforcement learning.

### Source
Dr. Aderonke Lawal, "Supervised / Unsupervised / Reinforcement Learning" slides.
"""),

    q('swep_day4_22',
      'What does the abbreviation LLM stand for, as used in the ChatGPT demonstration?',
      ['Large Language Model', 'Logical Learning Machine',
       'Linear Learning Method', 'Layered Language Mechanism'],
      0,
      'LLM stands for Large Language Model.',
      """
### Why this is the answer
Demo 2 is described as *"ChatGPT or any **LLM (Large Language Model)**"*, used to
show how AI **predicts the next word** in a sentence using **pattern recognition
from large datasets**.

### The demo's central takeaway
> *"**ChatGPT doesn't think, it predicts** based on learned text patterns."*

Students type a partial sentence (e.g. *"Once upon a time, there was a ___"*),
guess the next word themselves, then reveal ChatGPT's prediction. The discussion
point: *"how it works through **probability, not understanding**."*

This connects straight back to the stated limitation **Lack of Context** —
models don't *"understand"* like humans do.

### The other demo, for contrast
**Demo 1: Google Teachable Machine** (image recognition) at
`teachablemachine.withgoogle.com` — no coding required, uses a webcam, record
**20–30 samples per class**, then train and test live. It demonstrates
**pattern recognition through examples** and that the model **generalises, not
memorises**.

### Source
Dr. Aderonke Lawal, "Demo 2: ChatGPT Prompt Prediction" and "Take Aways" slides.
"""),

    q('swep_day4_23',
      'In the Google Teachable Machine demonstration, how many samples per class does the lecture instruct students to record?',
      ['20–30 samples', '5–10 samples', '100–150 samples', '500 samples'],
      0,
      'Record 20–30 samples per class.',
      """
### Why this is the answer
The step-by-step instructions for **Demo 1** are explicit:

1. Visit the site and click **'Get Started'**
2. Choose **'Image Project' > 'Standard image model'**
3. Rename Class 1 and Class 2 (e.g. **'Hand Up'**, **'Hand Down'**)
4. **Record 20–30 samples per class** using your webcam
5. Click **'Train Model'** to build the model
6. Test predictions live using your gestures

### Why the number matters pedagogically
It is small enough to do live in a lecture, yet enough for the model to
generalise — demonstrating the key takeaway that *"more quality data = better
results"* without needing a dataset of thousands.

The follow-up question posed to the class: *"**How did the model learn and how
did it predict?**"*

### The demo's stated takeaways
Demonstrates **pattern recognition through examples**; the model **learns by
generalising, not memorising**; *"similar to how students study past
questions"*; and it is a *"great entry point to machine learning concepts"*.

### Source
Dr. Aderonke Lawal, "Live Demo: Teachable Machine: Step-by-Step" slide.
"""),

    q('swep_day4_24',
      'Which of the following is NOT listed among the four challenges of Artificial Intelligence?',
      ['Data privacy and security', 'Bias and fairness',
       'Excessive electricity consumption by data centres', 'Job displacement'],
      2,
      'Electricity consumption by data centres is not among the four listed challenges.',
      """
### Why this is the answer
A **NOT** question. The lecture lists exactly four challenges, each with an
example:

| # | Challenge | Example given |
|---|---|---|
| 1 | **Data Privacy and Security** | A fitness app tracking location and health metrics could be **hacked or misused** |
| 2 | **Bias and Fairness** | A **hiring algorithm** favouring one ethnic group due to biased historical data |
| 3 | **Job Displacement** | **Chatbots** taking over customer service in banks or telecom companies |
| 4 | **Lack of Regulation** | **Deepfakes** spreading fake news with no consequences |

Energy consumption appears nowhere.

### The four ways forward, paired against them
| Way forward | Example |
|---|---|
| **Ethical AI Development** | Building AI to **support teachers, not replace them** |
| **Inclusive and Diverse Data** | Including **Nigerian voices** in voice recognition training |
| **Clear Policies and Regulations** | **Nigeria's AI policy** for fair, safe use in healthcare and education |
| **Human-AI Collaboration** | Doctors using AI for faster diagnosis but **making the final decision themselves** |

Each remedy answers a challenge: inclusive data answers bias, policy answers the
regulation gap, collaboration answers displacement.

### Source
Dr. Aderonke Lawal, "Challenges of Artificial Intelligence" and "Ways Forward"
slides.
"""),

    q('swep_day4_25',
      'According to the lecture, how is AI transforming Electrical engineering specifically?',
      ['Smart grids and IoT', 'Defect detection using computer vision',
       'Precision farming and drone technology', 'Process optimization and AI-driven simulations'],
      0,
      'Electrical engineering is transformed through smart grids and IoT.',
      """
### Why this is the answer
The lecture maps AI onto each engineering discipline, and every distractor
belongs to a different one:

| Field | How AI transforms it |
|---|---|
| **Civil** | Smart cities, **predictive maintenance** of infrastructure |
| **Mechanical** | Robotics, intelligent control systems |
| **Electrical** | **Smart grids, IoT** |
| **Chemical** | Process optimization, AI-driven simulations |
| **Metallurgical** | **Defect detection using computer vision** |
| **Agricultural** | Precision farming, drone tech |
| **Food** | Quality control, smart supply chains |
| **Computer/Software** | ML models, algorithms, ethics |

### Why this slide matters in a SWEP context
SWEP 200 draws students from every engineering department, so the lecture gives
each one its own entry point. It also echoes Day 3's PV lecture, where
**forecasting, anomaly detection and fault diagnosis** were presented as the
meeting point of power engineering and data science.

### Key takeaways from the same deck
AI **learns from examples, not direct instructions**; a trained model makes
useful predictions; **more quality data = better results**; models need
evaluation over time. *"AI is powerful but **not perfect** — it needs **human
oversight** and continuous improvement."*

### Source
Dr. Aderonke Lawal, "How is AI transforming your field" and "Key Takeaways"
slides.
"""),

    q('swep_day4_26',
      'Who delivered the Demystifying Artificial Intelligence lecture, and from which department?',
      ['Dr. W. A. Adebayo — Food Science and Technology',
       'Dr. Aderonke Lawal — Computer Engineering Department',
       'Mr. M. A. Ibrahim — Works and Services',
       'Dr. F. K. Ariyo — Electronic and Electrical Engineering'],
      1,
      'Dr. Aderonke Lawal, Senior Lecturer, Computer Engineering Department, OAU.',
      """
### Why this is the answer
The title slide reads: *"Demystifying Artificial Intelligence — What You Should
Know About the Machine Learning World. **Dr Aderonke Lawal, Senior Lecturer,
Computer Engineering Department, OAU, Ile-Ife**."*

The Day 4 ledger confirms: **Demystifying AI (Dr. Lawal Aderonke)** — explained
AI models, learning types (**supervised, unsupervised, reinforcement**), and
AI's transformative role across engineering specializations, also addressing
critical challenges like **biased data, privacy and job displacement**.

### Why option D is the sharpest distractor
**Dr. F. K. Ariyo** is genuinely from **Electronic and Electrical Engineering**
— but he delivered **Day 3's** Renewable Energy & PV Technology lecture. Both
are real people with real departments; only the day differs.

### Source
Deck title slide; handwritten Day 4 ledger.
"""),

    q('swep_day4_27',
      'The AI lecture opens with an analogy for how a model learns. Which analogy is used?',
      ['A student who learns to solve problems by practising many examples',
       'A library that stores every book ever written',
       'A calculator that follows fixed arithmetic rules',
       'A dictionary that looks up definitions on demand'],
      0,
      'A student who learns to solve problems by practising many examples.',
      """
### Why this is the answer
Immediately after defining a model as a *mathematical representation of patterns
learned from data* that *functions like a **digital brain***, the lecture gives
its analogy:

> *"A **student learns to solve problems by practicing many examples**."*

### Why this analogy and not the others
Options A, C and D all describe **retrieval or fixed rules** — storing, looking
up, or following instructions. The deck's whole thesis is the opposite:

> **"AI learns from examples, not direct instructions."**

A calculator follows rules it was given; a model **infers** patterns it was never
told. That distinction is why the student analogy recurs across the deck — in
supervised learning (*"practising with past questions and answers"*), in
overfitting (*"a student who crams"*), and in the Teachable Machine demo
(*"similar to how students study past questions"*).

### Source
Dr. Aderonke Lawal, "What Is a Model in AI?" and "Key Takeaways" slides.
"""),

    q('swep_day4_28',
      'In the exam-score prediction example, what are the four stages the lecture describes?',
      ['Data collection, training the model, making a prediction, evaluation',
       'Hypothesis, experiment, observation, conclusion',
       'Input, processing, output, storage',
       'Design, build, test, deploy'],
      0,
      'Data collection, training the model, making a prediction, evaluation.',
      """
### Why this is the answer
The lecture builds a model that predicts student exam scores from study habits,
in four numbered stages:

| # | Stage | What happens |
|---|---|---|
| 1 | **Data Collection** | Students: **study hours, attendance, past grades**, etc. |
| 2 | **Training the Model** | The model learns how study habits **relate to** exam scores |
| 3 | **Making a Prediction** | A new student inputs data (e.g. **5 hours of study/day**) and the model predicts a likely score |
| 4 | **Evaluation** | **Compare the predicted score to the actual score** to check accuracy |

### How it maps to the big picture
These four are the same loop in miniature: **Data → Training → Model/Prediction
→ Feedback**. Stage 4 is where feedback enters, producing the improved model.

### The analogy given
*"Like a teacher guessing your likely performance based on your study routine —
but the AI uses **hundreds of patterns**!"*

### Source
Dr. Aderonke Lawal, "The Prediction Process — Can AI Predict Your Exam Score?"
slide.
"""),

    # ============== Fire Awareness and Prevention (Mr. M. A. Ibrahim) =========
    q('swep_day4_29',
      'What three elements make up the Fire Triangle, described as the factors of combustion?',
      ['Heat, fuel and oxygen', 'Heat, smoke and fuel',
       'Fuel, oxygen and carbon dioxide', 'Heat, pressure and oxygen'],
      0,
      'The fire triangle is Heat + Fuel + Oxygen.',
      """
### Why this is the answer
*"**The Fire Triangle (Factors of Combustion):** Fire requires **three essential
elements** to sustain combustion: **Heat + Fuel + Oxygen**."*

### Why the triangle matters practically
Every method of fire control works by **breaking one side of the triangle**:

| Method | Side removed | Example |
|---|---|---|
| **Cooling** | **Heat** | Lowering temperature below ignition point, e.g. using **water** |
| **Smothering** | **Oxygen** | Cutting off oxygen supply, e.g. a **fire blanket** or **CO₂** |
| **Starvation** | **Fuel** | Clearing, excavating or **isolating unburned combustible materials** away from the fire path |

Three elements, three counter-measures, one-to-one. That symmetry is the whole
theory of firefighting in this lecture.

### Why CO₂ is not a triangle element
Carbon dioxide is an **extinguishing agent** — it works by *displacing* oxygen
(smothering). Listing it as a component of combustion inverts its role.

### How fire spreads
Through **conduction, convection, radiation and spontaneous combustion**. And a
key principle: *"while different materials burn at different rates, **almost no
matter is entirely immune to burning** under sufficient temperature and heat
exposure."*

### Source
Mr. M. A. Ibrahim, "Factors of Combustion & Fire Sources" and "Principles of
Fire Control" sections.
"""),

    q('swep_day4_30',
      'According to the historical fire outbreak statistics for OAU campus hostels, which hall records the highest occurrence of fire outbreaks?',
      ['Akintola Hall', 'Alumni Hall', 'Moremi Hall', 'Mozambique Hall'],
      2,
      'Moremi Hall records the most frequent fire outbreaks.',
      """
### Why this is the answer
The statistical insight for **Obafemi Awolowo University (OAU)** hostels ranks
fire outbreak occurrence in this exact order:

| Rank | Hall |
|---|---|
| **1** | **Moremi Hall (most frequent)** |
| 2 | Akintola Hall |
| 3 | Alumni Hall |
| 4 | Mozambique Hall |
| 5 | Postgraduate (PG) Hall |

### Why the ordering is examinable, not trivia
Every distractor is a **real hall on the same list** — this is a pure
rank-position question, so knowing the halls is not enough; you must know the
order. **Moremi first, PG last.**

### The context it sits in
The statistic appears under **Causes of Fire Outbreaks**, immediately after
**Negligence & Human Error** — carelessness, poor safety attitudes (the *"I
don't care" attitude*) and improper handling of combustible materials. The
ranking is presented as evidence of where that negligence concentrates.

### Source
Mr. M. A. Ibrahim, "Causes of Fire Outbreaks — Statistical Insight (OAU Campus
Hostels)".
"""),

    q('swep_day4_31',
      'In the classification of fires, which class is correctly matched with its fuel type?',
      ['Class B — combustible metals such as potassium and sodium',
       'Class C — highly flammable liquids such as kerosene and petrol',
       'Class D — combustible metals such as potassium, sodium and calcium',
       'Class A — flammable gases such as methane and acetylene'],
      2,
      'Class D covers combustible metals — potassium, sodium, calcium.',
      """
### Why this is the answer
The classification table runs A to E, and the distractors shuffle it:

| Class | Fuel type | Examples |
|---|---|---|
| **A** | Free-burning **solid** combustible materials | Paper, wood, textiles, rubbish |
| **B** | Highly flammable **liquids** | Kerosene, petrol, perfumes, alcohol |
| **C** | Flammable **gases** | Methane, acetylene, butane |
| **D** | Combustible **metals** | **Potassium, sodium, calcium** |
| **E / Electrical** | **Energized electrical equipment** | Short-circuited wiring, appliances (**least frequent origin**) |

Only **Class D → combustible metals** is correct.

### The memory ladder
**A** solids → **B** liquids → **C** gases → **D** metals → **E** electrical.
It moves through the states of matter in order, then finishes with electricity.

### The statistic worth noting
**Class E / Electrical** is marked as the **least frequent origin** — a useful
counter to the common assumption that most fires start electrically.

### Source
Mr. M. A. Ibrahim, "Classification of Fires" table.
"""),

    q('swep_day4_32',
      'According to the standard colour code bands for extinguishers given in this lecture, which pairing is correct?',
      ['BLACK — Carbon dioxide (CO₂) gas extinguisher', 'BLUE — Foam extinguisher',
       'RED — Dry powder extinguisher', 'CREAM — Water extinguisher'],
      0,
      'BLACK indicates a carbon dioxide (CO₂) gas extinguisher.',
      """
### Why this is the answer
The standard colour code bands are given as:

| Colour | Extinguisher |
|---|---|
| **RED** | **Water** |
| **BLUE** | **Dry Powder** |
| **CREAM / BUTTER COLOUR** | **Foam** |
| **BLACK** | **Carbon Dioxide (CO₂) Gas** |

Only **BLACK → CO₂** is correctly paired; each distractor moves a real colour to
the wrong agent.

### What each extinguisher contains
- **Water** — expels water or dilute chemical solutions to **cool** Class A
  fires; available as **air-compressed (stored pressure)** or **gas cartridge**
- **Gas (CO₂)** — compressed carbon dioxide under high pressure; multipurpose for
  **electrical and flammable liquid** fires; **leaves no residue**
- **Dry Powder** — active chemicals such as **Sodium Bicarbonate** or
  **Aluminium Sulphate** in powdered form; effective on Classes **A, B and C**
- **Foam** — chemical solutions (**Aluminium Sulphate and Sodium Bicarbonate in
  liquid form**) with **double expellants**, creating a **blanket** over
  flammable liquids

### Note for cross-day consistency
Day 2's safety lecture described extinguishers as *red bodies with coloured
markings* (green triangle, black square, cream label, blue circle). This lecture
uses the **colour band** convention. When a question names the lecture, answer
from that lecture's scheme.

### Source
Mr. M. A. Ibrahim, "Types of Fire Extinguishers & Color Codes".
"""),

    q('swep_day4_33',
      'The lecture distinguishes Comparative Safety from Absolute Safety. Which definition of ABSOLUTE SAFETY is correct?',
      ['Immediately evacuating and exiting the hazardous building or area to guarantee personal protection',
       'Attempting to manage, suppress or contain the situation while still inside the building where fire is present',
       'Comparing the relative risk of two different fire classes before acting',
       'Ensuring the building complies fully with fire safety policy before occupation'],
      0,
      'Absolute safety is immediate evacuation to guarantee personal protection.',
      """
### Why this is the answer
The two safety management concepts are defined in direct contrast:

| Concept | Definition |
|---|---|
| **Comparative Safety** | *"Attempting to **manage, suppress, or contain** the situation **while still inside** the building where fire is present"* |
| **Absolute Safety** | *"**Immediately evacuating and exiting** the hazardous building/area to **guarantee personal protection**"* |

The distinction is **stay and fight** versus **leave and survive**. Only
evacuation *guarantees* protection — hence "absolute".

### Where it fits in the response protocol
The handling steps are:
- **Stay calm & raise alarm** — do not panic or cause a stampede; gently and
  calmly inform occupants for **orderly evacuation**
- **Structural & building safety** — mind architectural design and wall
  partitioning to prevent rapid spread
- **Electrical wiring safety** — proper, shielded, insulated wiring to avoid
  short circuits and overheating
- **Navigating smoke** — *"**toxic smoke rises**; **lie flat on the floor and
  crawl**"* toward the nearest emergency exit; **do not walk upright**
- **Emergency call** — contact the Fire Service as soon as it is safe

### Source
Mr. M. A. Ibrahim, "How to Handle and Control a Fire Outbreak — Safety
Management Concepts".
"""),

    q('swep_day4_34',
      'What does the lecture instruct a person to do in a smoke-filled room, and why?',
      ['Walk upright quickly, because smoke settles near the floor',
       'Lie flat on the floor and crawl toward the nearest exit, because toxic smoke rises',
       'Hold the breath and run in any direction to escape faster',
       'Open all windows first to release the smoke before moving'],
      1,
      'Lie flat and crawl — toxic smoke rises.',
      """
### Why this is the answer
The instruction is explicit: *"In a smoke-filled room, **do not walk upright**.
**Toxic smoke rises**; **lie flat on the floor and crawl** toward the nearest
emergency exit."*

### The physics behind it
Hot smoke is **less dense** than the surrounding air, so it accumulates at
ceiling level and works downward. The **breathable air is lowest in the room** —
which is exactly why standing puts your head in the most toxic layer. Option A
inverts the physics, which is what makes it dangerous rather than merely wrong.

### Why smoke, not flame, is the priority
The rescue technique listed in the practical demonstrations is *"how to lift and
carry an **unconscious victim affected by smoke inhalation** while asleep"* —
smoke incapacitates before fire reaches people.

### The related practical guidance
- **Extinguishing materials:** water, fire blankets, asbestos safety sheets
- **Field improvisation:** if professional equipment is unavailable, **soak
  heavy fabric/blankets in water** and use them to **smother** the oxygen supply
- **Emergency access:** clear safety doors and emergency exit windows

### Source
Mr. M. A. Ibrahim, "How to Handle and Control a Fire Outbreak" and "Practical
Demonstrations & Improvisation".
"""),

    q('swep_day4_35',
      'Which of the following is NOT listed among the causes or sources of fire outbreaks in the lecture?',
      ['Lightning and thunder as a natural igniter',
       'House pests or rodents gnawing through electrical wires',
       'Earth tremors fracturing underground gas pipelines',
       'Carelessness and the "I don\'t care" safety attitude'],
      2,
      'Earth tremors fracturing gas pipelines is not a listed cause.',
      """
### Why this is the answer
A **NOT** question. The causes given are:

| Category | Cause |
|---|---|
| **Natural igniter** | **Lightning and thunder** |
| **Biological/Animal** | **House pests or rodents gnawing through electrical wires** |
| **Negligence & Human Error** | Carelessness, poor safety attitudes (**"I don't care" attitude**), improper handling of combustible materials |

Earth tremors appear nowhere.

### The framing principle
*"Fire outbreaks can stem from both **natural and artificial** causes."* The
lecture opens by noting that the basic necessities of human life are **food,
shelter and clothing**, and that the **human brain and sensory organs** — such
as the **olfactory lobes for smell** — serve as **natural detectors** of
potential dangers like fire outbreaks.

### Common sources and volatile substances
- **Flammable gases:** **acetylene**, **butane**, **methane**
- **Volatile solvents and chemicals:** **perfumes**, **alcohol**, and illicit
  substances like **Colorado** (Indian hemp / synthetic cannabis)

Note that **perfumes and alcohol** also appear as **Class B** examples — the deck
is consistent across both sections.

### Source
Mr. M. A. Ibrahim, "Introduction & Fundamental Concepts" and "Causes of Fire
Outbreaks".
"""),

    q('swep_day4_36',
      'Fire can be controlled by breaking a side of the fire triangle. Which control method is correctly described?',
      ['Cooling — cutting off the supply of oxygen using a fire blanket',
       'Smothering — lowering the temperature below the ignition point using water',
       'Starvation — removing or isolating unburned combustible materials away from the path of the fire',
       'Starvation — reducing the oxygen concentration with carbon dioxide'],
      2,
      'Starvation removes the fuel — isolating unburned combustibles from the fire path.',
      """
### Why this is the answer
Three control methods, each breaking a different side of the triangle:

| Method | Side broken | How |
|---|---|---|
| **Cooling** | **Heat** | Lowering the temperature **below the ignition point**, e.g. using **water** |
| **Smothering** | **Oxygen** | **Cutting off the oxygen supply**, e.g. a **fire blanket** or **CO₂** |
| **Starvation** | **Fuel** | **Removing what is making the fire continuously burn** — clearing, excavating or **isolating unburned combustible materials** away from the fire path |

Only option C is correct. Options A and B **swap cooling and smothering**, and
option D gives starvation an oxygen mechanism that belongs to smothering.

### The naming logic
The word tells you the side: you *cool* heat, you *smother* oxygen, you *starve*
fuel. If you can recall the triangle — **heat, fuel, oxygen** — you can
reconstruct all three methods without memorising them separately.

### Field application
The improvisation guidance applies **smothering** directly: soak heavy
fabric/blankets in water and use them to **cut off the oxygen supply** from
flames.

### Source
Mr. M. A. Ibrahim, "Principles of Fire Control".
"""),

    q('swep_day4_37',
      'The Fire Awareness lecture states that the human body itself acts as a natural detector of danger. Which organ is specifically named?',
      ['The eyes, for detecting smoke',
       'The olfactory lobes, for smell',
       'The ears, for detecting alarms',
       'The skin, for detecting radiant heat'],
      1,
      'The olfactory lobes, which detect smell.',
      """
### Why this is the answer
*"The **human brain and sensory organs** (such as the **olfactory lobes for
smell**) serve as **natural detectors of potential dangers** that could lead to
disasters like fire outbreaks."*

Only the **olfactory lobes** are named specifically.

### Why smell, of all the senses
Smell detects fire **earliest**. You can smell burning insulation or smouldering
material before there is visible flame, visible smoke, or an audible alarm — and
crucially, **while asleep**, smell is not entirely disabled the way sight is.
That matters given the lecture's own rescue scenario of a victim overcome by
**smoke inhalation while asleep**.

### The framing it belongs to
The introduction establishes that the basic necessities of human life are
**food, shelter and clothing**, then presents the body's sensory apparatus as the
first line of fire detection — before any engineered detector.

### Source
Mr. M. A. Ibrahim, "Introduction & Fundamental Concepts".
"""),

    q('swep_day4_38',
      'Which extinguisher type is described as multipurpose for electrical and flammable liquid fires, leaving no residue?',
      ['Water extinguisher', 'Foam extinguisher',
       'Dry powder extinguisher', 'Gas (CO₂) extinguisher'],
      3,
      'The CO₂ gas extinguisher is multipurpose and leaves no residue.',
      """
### Why this is the answer
*"**Gas (CO₂) Extinguishers:** Contain **compressed carbon dioxide gas under
high pressure**. **Multipurpose for electrical and flammable liquid fires**.
**Leave no residue**."*

### Why "no residue" matters
It is the reason CO₂ is chosen for **electrical equipment** — servers,
switchgear, laboratory instruments. Powder and foam would contaminate or corrode
the equipment they save; CO₂ simply disperses.

### How it works
CO₂ extinguishes by **smothering** — displacing oxygen, which breaks the oxygen
side of the fire triangle. The Principles of Fire Control name it explicitly as
a smothering agent alongside the fire blanket.

### The comparison set
| Extinguisher | Distinctive feature |
|---|---|
| **Water** | Cools; **air-compressed** or **gas cartridge** types |
| **Foam** | **Double expellants**, forms a **blanket** over flammable liquids |
| **Dry Powder** | Sodium Bicarbonate or Aluminium Sulphate in **powdered** form; Classes **A, B, C** |
| **Gas (CO₂)** | **Multipurpose**, electrical + liquids, **no residue** |

Note that foam and dry powder share the same active chemicals — **Aluminium
Sulphate and Sodium Bicarbonate** — differing in **liquid** versus **powdered**
form.

### Source
Mr. M. A. Ibrahim, "Types of Fire Extinguishers & Color Codes".
"""),

    q('swep_day4_39',
      'Who delivered the Fire Awareness and Prevention session on Day 4?',
      ['Dr. W. A. Adebayo', 'Dr. Aderonke Lawal',
       'Mr. M. A. Ibrahim', 'Prof. A. A. Adeleke'],
      2,
      'Mr. M. A. Ibrahim delivered the Fire Awareness and Prevention session.',
      """
### Why this is the answer
The Day 4 ledger records **Fire Awareness & Prevention (Mr. M. A. Ibrahim)**,
noting that he detailed the **factors of combustion**, **fire classifications
(Class A to E)**, and the correct identification of fire extinguishers **by
colour code** (e.g. **Red for water, Blue for dry powder**), concluding with
practical safety protocols for handling outbreaks, including **safe evacuation
techniques and emergency rescue demonstrations**.

The notes themselves are headed: *"FIRE AWARENESS AND PREVENTION — Speaker:
**Mr. M. A. Ibrahim**."*

### Note the title
He is the only Day 4 speaker titled **Mr.** — the other two are **Dr.** That
alone distinguishes him.

### Why option D is the trap
**Prof. A. A. Adeleke** also lectured on safety — but that was **Day 2's
Workshop and Industrial Safety**, covering PPE standards, the hierarchy of
control and safety signage. Two different safety lectures, two different days,
two different speakers.

### Source
Handwritten "Record of the Orientation Week Activities", Day 4; notes header.
"""),

    q('swep_day4_40',
      'Which Day 4 statistic or figure is correctly stated?',
      ['Graphene is 200 times stronger than steel; the 1IR ran 1760–1840 in Britain; Moremi Hall records the most frequent OAU hostel fires',
       'Graphene is 20 times stronger than steel; the 1IR ran 1860–1930; Akintola Hall records the most frequent fires',
       'Graphene is 200 times thinner than steel; the 2IR began in the 1960s; PG Hall records the most frequent fires',
       'Graphene is one million times stronger than steel; the 3IR ran 1760–1840; Alumni Hall records the most frequent fires'],
      0,
      'Graphene 200× stronger than steel; 1IR 1760–1840 Britain; Moremi Hall most frequent.',
      """
### Why this is the answer
This question gathers Day 4's three headline figures into one check. Only option
A states all three correctly:

| Figure | Correct value | Source lecture |
|---|---|---|
| **Graphene strength** | **200 times stronger than steel** (and **one million times thinner than human hair**) | Food Science / 4IR |
| **First Industrial Revolution** | **1760–1840**, in **Britain** | Food Science / 4IR |
| **Most frequent OAU hostel fires** | **Moremi Hall** | Fire Awareness |

### How each distractor breaks
- **B** — shrinks graphene to 20×, moves the 1IR to the **2IR's** dates
  (1860–1930), and promotes Akintola (rank **2**) to first.
- **C** — swaps graphene's *strength* and *thinness* comparisons, gives the 2IR
  the **3IR's** start (1960s), and names PG Hall, which is **last (rank 5)**.
- **D** — applies the "one million times" figure to the wrong property (it is
  **thinness vs human hair**, not strength vs steel), gives the 3IR the 1IR's
  dates, and names Alumni (rank **3**).

### The lesson
Every wrong element is a **real Day 4 number attached to the wrong thing**. With
statistics, the danger is never the number you have never seen — it is the one
you have seen somewhere else.

### Source
Dr. W. A. Adebayo, "Physical MegaTrend" and "First Industrial Revolution";
Mr. M. A. Ibrahim, "Statistical Insight (OAU Campus Hostels)".
"""),
]

assert len(QUESTIONS) == 40, f'expected 40, got {len(QUESTIONS)}'
_ids = [x['id'] for x in QUESTIONS]
assert len(set(_ids)) == 40, 'duplicate ids'
for _q in QUESTIONS:
    assert len(_q['options']) == 4, f"{_q['id']}: needs 4 options"
    assert 0 <= _q['correct'] < 4, f"{_q['id']}: bad correct index"
    assert _q['short'] and _q['solution'], f"{_q['id']}: missing short/solution"
