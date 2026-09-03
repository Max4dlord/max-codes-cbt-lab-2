#!/usr/bin/env python3
"""Build Category 2 (Actual Past Questions) for AEE 202 from the Drive materials:
- AEE202 QB.txt (Section 1: past MCQs w/ answers; Section 2: lecture notes; Section 3: bonus)
- AEE 202_Compulsory.pdf (15 objective questions, answer key partially legible)
AI judgment is applied to fix/authenticate answers where the source key is
inconsistent, and every explanation cites the source material.
Emits .past_questions_out.json"""

import json

# ============================================================================
# SECTION 1 — Authentic past-paper MCQs (source: AGE 201 Workshop Practice
# past question + AEE202 QB.txt key). Kept verbatim where sane; fixed where the
# source is self-inconsistent (noted in solutions).
# ============================================================================
S1 = [
dict(q="Selection of a proper material for engineering purposes should be based on the following but one:", opts=["Availability of the material","Cost of the material","Suitability of the material","Size of the material"], ans=3,
     exp="The past question lists availability, cost and suitability as the bases for material selection — size is the odd one out (the same material can be produced in many sizes). Answer: size of the material."),
dict(q="A vernier caliper is a measuring instrument with higher precision than the ruler. The sliding scale is the:", opts=["main scale","mini scale","vernier scale","larger scale"], ans=2,
     exp="The vernier caliper has a fixed main scale and a movable sliding scale — the sliding scale is called the vernier scale; it allows readings to 0.02 mm or better."),
dict(q="A micrometer is a measuring device resembling:", opts=["a V-clamp","a C-clamp","a Y-clamp","a T-clamp"], ans=1,
     exp="The micrometer screw gauge has a rigid C-shaped frame, so it resembles a C-clamp (in fact one nickname for the frame is the 'C-frame')."),
dict(q="Marking out is based on the following principles except:", opts=["Defining the shape of the work piece","Making marks on the work piece to guide the machinist","Indicating the exact position of the work piece","Helping to remove excess cutting from the work piece"], ans=3,
     exp="Marking out means scribing guide lines: it defines the shape, guides the machinist and shows exact positions. Removing excess material is the job of cutting (sawing, filing, chipping) — not of marking out."),
dict(q="The common types of drills are but one:", opts=["flat drill","straight fluted drill","twist drill","pillar drill"], ans=3,
     exp="Flat drill, straight fluted drill and twist drill are all types of drills. A pillar drill is a drilling MACHINE (a machine tool), not a type of drill — that is the odd one out."),
dict(q="One of the following is a physical property of metals:", opts=["ductility","malleability","elasticity","density"], ans=3,
     exp="Ductility, malleability and elasticity are mechanical properties. Density (mass per unit volume) is a physical property of a metal."),
dict(q="The size of a drilling machine is determined by one of the following factors:", opts=["Range of spindle speeds","Net weight of the drill bit","Length of the base","Maximum drilling impact"], ans=0,
     exp="Per the past-question key, the size of a drilling machine is indicated by the range of spindle speeds (together with the largest drill diameter it can drive)."),
dict(q="In drilling a circular metal piece in the workshop, the spindle speed is based on one of the following:", opts=["cutting speed chosen for the metal piece","diameter of the metal piece","material of the metal piece","thickness of the metal piece"], ans=1,
     exp="The past-question key gives the diameter of the metal piece as the basis of spindle speed — in practice the r.p.m. is set from the recommended cutting speed AND the diameter (N = v/\u03c0d), and the key selects diameter as the listed factor."),
dict(q="A lathe machine can be used to cut machine components into various shapes and sizes. The work piece can be held between:", opts=["base stock and head stock","head stock and bottom stock","tail stock and high stock","head stock and tail stock"], ans=3,
     exp="A long work piece on the lathe is held between the headstock (driving end) and the tailstock (supporting end) — typically between centres or in the chuck with tailstock support."),
dict(q="Any engineering product is a product of ingenuity which depends on the following factors except one:", opts=["ability to conceptualize an idea","translating a good idea into design","transforming the design into a product in the workshop","fabrication of an idea into design"], ans=3,
     exp="Ingenuity involves conceptualising an idea, translating it into a design and transforming the design into a product. 'Fabrication of an idea into design' is a confused restatement — that is the odd one out."),
# Q11 — tolerance calculation set
dict(q="A hole and a shaft have basic diameters of 45 mm and 44.50 mm respectively, but were machined to actual sizes of 44.95 mm and 44.53 mm. If the shaft is permitted a bilateral tolerance of +0.05 mm and \u22120.01 mm, the maximum permissible variation in its diameter is:", opts=["0.04 mm","0.06 mm","0.05 mm","1.06 mm"], ans=1,
     exp="Maximum variation = upper limit \u2212 lower limit = (+0.05) \u2212 (\u22120.01) = 0.06 mm. (Tolerance = upper deviation \u2212 lower deviation.)"),
dict(q="For the same shaft (basic diameter 44.50 mm, tolerance +0.05/\u22120.01 mm), the minimum diameter to which the shaft can be cut is:", opts=["44.49 mm","44.55 mm","44.59 mm","44.50 mm"], ans=0,
     exp="Minimum shaft diameter = basic diameter + lower deviation = 44.50 + (\u22120.01) = 44.49 mm."),
dict(q="For the same mating parts (hole 44.95 mm actual on a 45 mm basic; shaft 44.53 mm actual on a 44.50 mm basic), the allowance and clearance respectively are about:", opts=["0.42 mm and 0.50 mm","0.45 mm and 0.50 mm","0.50 mm and 0.52 mm","0.50 mm and 0.50 mm"], ans=0,
     exp="Allowance = minimum hole \u2212 maximum shaft = 44.95 \u2212 44.53 = 0.42 mm. Clearance = maximum hole \u2212 minimum shaft = 45.00 \u2212 44.49 = 0.51 mm (\u2248 0.50 mm, which is why the key gives 0.42 mm and 0.50 mm). Answer: 0.42 mm and 0.50 mm."),
dict(q="All of these are types of hammer except:", opts=["ball peen","rectangular pein","straight pein","cross pein"], ans=1,
     exp="Ball peen, straight pein and cross pein are standard peen-hammer types (named after the shape of the peen). There is no 'rectangular pein' hammer — that is the odd one out."),
dict(q="One of the safety precautions required in drilling is:", opts=["knowing the speed of the drill","not holding revolving drill","knowing the cutting feed","all of the above"], ans=3,
     exp="Safe drilling requires knowing the correct drill speed and feed, and never holding/touching a revolving drill or workpiece — hence all of the above."),
dict(q="Adequate footwear is necessary in the workshop because of the following injuries:", opts=["cutting of the leg","slipping on the floor","sharp edges piercing the feet","heavy object falling on the feet"], ans=3,
     exp="The past-question key gives heavy objects falling on the feet as the main reason safety shoes (with toe protection) are compulsory in the workshop."),
dict(q="The engineer's steel rule is a measuring device used to measure:", opts=["straight dimensions","circular dimensions","linear dimensions","datum dimensions"], ans=2,
     exp="The steel rule measures linear dimensions (lengths along a line). Circular dimensions are measured with callipers/micrometers, and 'datum dimensions' is not a measurement type."),
dict(q="The datum used in engineering workshops is the:", opts=["base plate","lap base","surface plate","saddle base"], ans=2,
     exp="The surface plate is the workshop datum (reference plane) from which heights and dimensions are marked out and measured, e.g. with a scribing block."),
dict(q="With a good rule, measurement can be made with an accuracy of:", opts=["0.22 cm","0.20 mm","0.02 mm","0.20 cm"], ans=1,
     exp="A good steel rule reads accurately to about 0.20 mm (0.2 mm) — finer accuracy requires the vernier caliper or micrometer."),
dict(q="A calliper is a measuring device for determining:", opts=["linear measurement","hollow measurement","vertical measurement","simple measurement"], ans=0,
     exp="Inside and outside callipers transfer linear measurements (internal/external sizes) to a rule for reading."),
dict(q="For both inside and outside callipers the measurement determined is interpreted on:", opts=["rule","meter","ruling","metric"], ans=0,
     exp="Callipers have no scale of their own — the size they grip is transferred to and read off a rule."),
dict(q="On a television circuit board, joining of terminals is achievable by:", opts=["welding","pinning","melting","soldering","riveting"], ans=3,
     exp="Electronic terminals on circuit boards are joined by soldering — a low-temperature joining process using a lead-tin alloy filler, which is gentle enough for electronics."),
dict(q="The removal of sharp and rough edges on a work piece can be done by:", opts=["milling","grinding","scrapping","turning"], ans=2,
     exp="The past-question key gives scrapping (scraping). Hand scraping with a scraper is a fitting-shop method for removing sharp/rough edges (deburring); grinding would also smooth edges but the key credits scraping as the listed method."),
dict(q="A hacksaw is a:", opts=["welding tool","milling tool","varnishing tool","cutting tool"], ans=3,
     exp="The hacksaw is a hand cutting tool — it cuts metal bars into parts and removes layers of metal."),
dict(q="Characteristics of a good workshop floor are but one:", opts=["it must be resistant to wear and cheap to maintain","it must be able to support the weight of the worker","it must be able to resist the effect of process chemicals","it must be non-slip under normal working condition"], ans=2,
     exp="A good workshop floor must resist wear, carry loads (workers AND machines), and be non-slip. Resisting process chemicals is not a stated requirement in the key — that is the odd one out."),
dict(q="Ultra violet rays and flying splinters are most dangerous to the:", opts=["nose","head","eye","leg"], ans=2,
     exp="UV rays from welding arcs and flying splinters/chips primarily endanger the eyes — hence goggles/face shields (with proper shade for welding) are compulsory."),
dict(q="The efficient stroke for hacksaw is:", opts=["side stroke","backward stroke","forward stroke","upward stroke"], ans=2,
     exp="The hacksaw cuts on the forward stroke — the most active stroke, removing the maximum metal in one stroke. The return stroke is idle (no cutting pressure)."),
dict(q="Gloves are important in the workshop for preventing injury to the hand. Such injury may be due to:", opts=["electric shock","corrosive fluid","hot material","horse play","all of the above"], ans=4,
     exp="Gloves protect the hands from electric shock, corrosive fluids, hot materials and careless horseplay injuries — all of the above."),
dict(q="Chisel is a:", opts=["marking tool","cutting tool","riveting tool","milling tool","none of the above"], ans=1,
     exp="The cold chisel is a hand cutting tool — used to remove thick layers/edges of metal, usually together with a hammer."),
dict(q="You are required to produce a 'T' shaped object from a straight metal rod of 20 cm in length. Which of the following activities will you not do in carrying out the assignment?", opts=["Cutting","welding","grinding","milling"], ans=1,
     exp="Making a T-shape from a single rod involves cutting to length and shaping by grinding/milling. You would NOT weld — the key notes there is nothing to join (the T is formed from one piece)."),
dict(q="Which of these is not part of a hammer:", opts=["trunk","handle","pein","eye","head"], ans=0,
     exp="A hammer consists of the head (with face and pein), the eye (the hole in the head for the handle) and the handle. 'Trunk' is not a hammer part."),
dict(q="Stiffness is the ability of a metal to:", opts=["resist deformation under stress","resist externally applied forces","regain its original shape after deformation","retain deformation under load"], ans=0,
     exp="Stiffness is a mechanical property: the ability of a metal to resist deformation (deflection) under stress. Regaining original shape is elasticity; retaining deformation is plasticity."),
dict(q="One of these is a file type based on coarseness:", opts=["single cut","bastard cut","second cut","intermediate fine","none of the above"], ans=1,
     exp="Files are classified by coarseness (grade) as rough, bastard, second cut, smooth and dead smooth. 'Bastard cut' is therefore the coarseness grade; 'single cut' describes the cut pattern, not coarseness."),
dict(q="Parts of a micrometer include the following except:", opts=["anvil","spindle","beam","ratchet"], ans=2,
     exp="A micrometer has a frame, anvil, spindle, thimble, barrel/sleeve and ratchet (thimble stop). 'Beam' belongs to a vernier caliper, not a micrometer — it is the odd one out."),
dict(q="To measure both internal and external diameters of a hollow pipe, the most appropriate tool is:", opts=["inside caliper","outside caliper","linear caliper","vernier caliper"], ans=3,
     exp="A vernier caliper can take both inside and outside measurements (with its internal and external jaws) — so it is the most appropriate single tool for a hollow pipe."),
dict(q="One of the following is a type of measurement in workshop practice:", opts=["surface measurement","angular measurement","ground measurement","non-angular measurement"], ans=1,
     exp="Workshop measurement is classified into linear measurement and angular measurement (angles, e.g. with protractors/bevel gauges)."),
dict(q="Operations generally carried out on the workbench include:", opts=["hammering","welding","screwing","chipping"], ans=0,
     exp="The past-question key lists hammering as a typical workbench operation. (Welding is done in the welding bay, not on the bench.)"),
dict(q="Example of a non-linear measurement is the dimension of a:", opts=["cuboid","parallelogram","parabola","rectangle"], ans=2,
     exp="A parabola is a curve — its dimension is a non-linear measurement; the others are straight-edged shapes measured linearly."),
dict(q="A V-block is a tool for:", opts=["marking out","cutting","punching","blocking"], ans=0,
     exp="The V-block is a marking-out tool: it supports round bars and helps locate their centres during marking out (often with a scribing block)."),
dict(q="The hammer is made from:", opts=["mild steel","alloy steel","forged steel","carbon steel"], ans=2,
     exp="Per the past-question key, hammers are made from forged steel — forging aligns the grain and makes the head tough enough to withstand repeated blows."),
dict(q="A single cut file has separation of teeth in one direction of:", opts=["90 degrees","30 degrees","60 degrees","45 degrees"], ans=3,
     exp="The past-question key gives 45 degrees for the single-cut tooth angle (some textbooks quote 60\u201380\u00b0 depending on the convention; follow the key for this paper)."),
dict(q="Cast iron is obtained from melting pig iron with:", opts=["coke and aluminium","limestone and aluminium","aluminium and carbon","limestone and coke"], ans=3,
     exp="Cast iron is produced by remelting pig iron in a cupola with coke (fuel) and limestone (flux) — limestone and coke."),
dict(q="A pillar drilling machine consists of a ___ on which the drill spindle is attached:", opts=["beam","block","base","column"], ans=3,
     exp="The pillar drilling machine is built on a vertical column (pillar); the drilling head with the spindle is attached to and slides on this column."),
dict(q="The lathe bed provides sitting position for ___ and sliding guide ways:", opts=["tailstock","block","base","column"], ans=0,
     exp="The lathe bed carries the sliding guide ways on which the tailstock (and carriage) sit and slide along the machine."),
dict(q="The first step in drawing a 15 mm diameter hole on a metal plate in the workshop is:", opts=["punching the center point","drawing the circle","placing the workpiece on the drilling machine","marking the metal plate"], ans=0,
     exp="Per the key, you first punch the centre point (centre-punch the hole position) before drawing the circle — the punched centre guides the scribing/drilling."),
dict(q="An engineer designed a component to a length of 500 mm, but only a variation between 499.5 mm and 500.01 mm can be tolerated. This type of tolerance is called:", opts=["bilateral","multilateral","collateral","unilateral"], ans=0,
     exp="The permitted variation lies on BOTH sides of the basic size (499.5 is below 500, 500.01 is above) — that is a bilateral tolerance. (The handwritten key's '(d) Bilateral' is a slip; option (d) is unilateral, so the answer is (a) bilateral.)"),
]

# ============================================================================
# SECTION 2 — Mike Media's lecture notes converted to MCQs (AI-formatted).
# ============================================================================
S2 = [
dict(q="Bringing new materials to life is termed:", opts=["manufacturing","designing","fabricating","production"], ans=0,
     exp="The lecture notes define manufacturing as 'bringing new materials to life' — transforming raw materials into finished products."),
dict(q="The popular safety slang in the workshop is:", opts=["Work first, safety next","Safety first, work next","No safety, more speed","Safety is optional"], ans=1,
     exp="The lecture notes state the popular workshop safety slang is 'Safety first, work next' — safety always comes before the job."),
dict(q="What does PPE mean in the workshop?", opts=["Personal protective equipments","Personal practice equipment","Protected personnel equipment","Personal protective engineering"], ans=0,
     exp="PPE = Personal Protective Equipment(s) — items worn to protect the worker, e.g. goggles, gloves, safety shoes and overalls."),
dict(q="The major difference between hand tools and power tools is:", opts=["their cost","the way power is supplied into them","their size","their material"], ans=1,
     exp="The lecture notes state the major difference is the power supply — hand tools are driven by human effort, while power tools have an external power source (electricity, compressed air, etc.)."),
dict(q="A file is a hand or power tool, and what is its function?", opts=["Hand tool used to remove metal","Power tool used to cut wood","Hand tool used to measure","Power tool used to mark out"], ans=0,
     exp="A file is a hand cutting tool — it removes metal in thin layers (with its slanting teeth) to clean and finish surfaces."),
dict(q="An example of power tools, per the lecture notes, includes:", opts=["hacksaw","file","drilling machine","chisel"], ans=2,
     exp="The lecture notes list the drilling machine as an example of a power tool (power-driven equipment). Hacksaw, file and chisel are hand tools."),
dict(q="The benchwork and fitting process consists of a rigid construction made of:", opts=["hard solid wood or steel","plastic and glass","aluminium sheet","soft wood only"], ans=0,
     exp="The bench is a rigid construction made of hard solid wood or steel — it must be strong enough to absorb hammering and filing loads."),
dict(q="What can you say about the terms 'fitting' and 'assembling'?", opts=["They are opposite operations","They are used interchangeably and are interdependent","Fitting is done only by machines","Assembling does not involve the bench"], ans=1,
     exp="The notes state the two terms are used interchangeably, though they are interdependent — both operations are carried out on the bench."),
dict(q="What type of tool is a vice, and which are its types?", opts=["Cutting tool — bench, pipe, hand, pin","Work holding tool — bench, pipe, hand, pin","Marking tool — bench, pipe, hand, pin","Measuring tool — bench, pipe, hand, pin"], ans=1,
     exp="A vice is a work-holding tool. The four types (BPHP): bench vice (fixed on the bench), pipe vice (holds round objects like pipes/shafts), hand vice (holds workpieces steady) and pin vice (holds tiny objects)."),
dict(q="Bench vices have a fixed and a movable jaw because:", opts=["the movable jaw can be adjusted to fit the size of the job","the fixed jaw is decorative","both jaws move together","only the fixed jaw grips"], ans=0,
     exp="The movable jaw slides so the opening can be adjusted to grip the size of the job being held."),
dict(q="How do you indicate the size of a vice?", opts=["By its weight","By the width of the jaw and the maximum opening between the two jaws","By the height of the bench","By the length of the handle"], ans=1,
     exp="Vice size is indicated by the width of its jaws and the maximum opening between the two jaws."),
dict(q="The material we work with when working on a work bench is the:", opts=["workpiece held in the jaws","bench top only","vice handle","floor"], ans=0,
     exp="The workpiece (the material being worked) is gripped in the jaws of the bench vice during benchwork."),
dict(q="What hammer mass is used for light jobs?", opts=["0.45 kg and above","0.33 kg to 0.45 kg","0.11 kg to 0.33 kg","0.05 kg to 0.10 kg"], ans=2,
     exp="Per the notes: light jobs use hammers of 0.11\u20130.33 kg; moderate jobs 0.33\u20130.45 kg; heavy jobs 0.45 kg and above."),
dict(q="What hammer mass is used for moderate jobs?", opts=["0.11 kg to 0.33 kg","0.33 kg to 0.45 kg","0.45 kg and above","below 0.11 kg"], ans=1,
     exp="Moderate jobs use hammers of 0.33\u20130.45 kg (light: 0.11\u20130.33 kg; heavy: 0.45 kg and above)."),
dict(q="What hammer mass is used for heavy jobs?", opts=["0.11 kg to 0.33 kg","0.33 kg to 0.45 kg","0.45 kg and above","below 0.11 kg"], ans=2,
     exp="Heavy jobs require hammers of 0.45 kg and above."),
dict(q="The processes involved in cutting operations are:", opts=["sawing, filing and chipping","drilling, reaming and tapping","marking, punching and scribing","bending, rolling and forging"], ans=0,
     exp="The lecture notes list the cutting operations as sawing, filing and chipping."),
dict(q="The two main functions of sawing are:", opts=["cutting into parts and removing layers","drilling holes and reaming","marking and punching","clamping and holding"], ans=0,
     exp="Sawing is used (1) to cut material into parts and (2) to remove layers of metal."),
dict(q="Which saw is used to cut material into parts?", opts=["hacksaw","coping saw","band saw","keyhole saw"], ans=0,
     exp="The hacksaw is the hand saw used to cut metal into parts (the notes: 'saw used to cut into parts is the hacksaw')."),
dict(q="How are the teeth of a hacksaw arranged?", opts=["all teeth in a straight row","alternately to left and right, leaving the 3rd or 4th tooth straight","all teeth bent to the right","all teeth bent to the left"], ans=1,
     exp="Hacksaw teeth are set alternately left and right with every 3rd or 4th tooth left straight — the set widens the cut so the blade does not jam."),
dict(q="The linear distance covered from one end to the other on a jaw is called:", opts=["a stroke","a pass","a traverse","a pitch"], ans=0,
     exp="The notes define stroke as the linear distance the cutting tool moves back and forth during hacksaw cutting."),
dict(q="The most active stroke in hacksaw cutting is called:", opts=["the return stroke","the forward stroke","the side stroke","the idle stroke"], ans=1,
     exp="The forward stroke is the most active — it removes the maximum amount of metal in one stroke (cutting is done on the push)."),
dict(q="What is the forward stroke?", opts=["The stroke that removes the maximum amount of metal in one stroke","The stroke that returns the blade","The stroke used for marking","The stroke that cools the blade"], ans=0,
     exp="The forward stroke removes the maximum metal in one stroke — it is the cutting stroke; the return stroke is idle."),
dict(q="What is the use of a chisel?", opts=["To remove the edge of metals in thick layers (more than about 0.6 mm)","To measure metal thickness","To hold the work piece","To finish wood surfaces"], ans=0,
     exp="The cold chisel removes metal in relatively thick layers — the notes say it removes the edge of metals more than about 0.6 mm thick (a file is used for thin layers)."),
dict(q="The slanting rows on the surface of a file are called:", opts=["the cut of teeth","the grain","the flutes","the lands"], ans=0,
     exp="The slanting rows of teeth on a file's surface are called the cut of the teeth (single or double cut)."),
dict(q="A file is used after sawing to:", opts=["clean the surface","cut the metal into parts","mark the surface","hold the work"], ans=0,
     exp="After sawing, the file cleans (finishes) the cut surface, removing saw marks and roughness."),
dict(q="Example sizes of files (per the notes) are:", opts=["100 mm to 250 mm and 250 mm to 450 mm","10 mm to 50 mm only","500 mm to 1000 mm","1 m and above"], ans=0,
     exp="The notes give file sizes of 100\u2013250 mm (small/fine range) and 250\u2013450 mm (heavier range)."),
dict(q="What is 'Marking out'?", opts=["The process of scribing lines on the worksheet as an appropriate cutting guide","The process of cutting the metal to size","The process of painting the work piece","The process of clamping the work"], ans=0,
     exp="Marking out is scribing lines on the work as a cutting guide — it defines the shape and shows the machinist exactly where to cut."),
dict(q="Define Accuracy:", opts=["How close repeated measurements are to each other","The quality of a value being close to the real/true value","How large the measurement is","The number of decimal places"], ans=1,
     exp="Accuracy is the closeness of a measured value to the real (true) value; precision is how close repeated measurements are to each other."),
dict(q="Define Precision:", opts=["How close repeated measurements are to each other","The closeness of a value to the true value","The size of the instrument","The skill of the operator"], ans=0,
     exp="Precision is the closeness (repeatability) of repeated measurements to each other — a precise instrument gives consistent readings."),
dict(q="The methods of filing are:", opts=["straight, cross and draw","hot, warm and cold","rough, smooth and fine","push, pull and lift"], ans=0,
     exp="The three filing methods are straight filing, cross filing and draw filing."),
dict(q="The process of cutting external threads is called:", opts=["dyeing (dieing)","tapping","reaming","broaching"], ans=0,
     exp="External threads are cut with a die — the process is called dyeing/dieing (die threading); internal threads are cut by tapping."),
dict(q="The process of cutting internal threads in an existing hole is called:", opts=["tapping","dyeing","drilling","reaming"], ans=0,
     exp="Cutting internal threads in a hole is tapping (with a tap); cutting external threads is dyeing (with a die)."),
dict(q="An example of temporary metal joining is:", opts=["bolting","soldering","riveting","welding"], ans=0,
     exp="Bolting is a temporary joint (can be disassembled without damage). Soldering, riveting and welding are permanent joints."),
dict(q="Examples of permanent metal joining include:", opts=["soldering, riveting and welding","bolting and nutting","clamping","keying"], ans=0,
     exp="The notes list soldering, riveting and welding as permanent joining methods (bolting is temporary)."),
dict(q="The two types of welding are:", opts=["arc welding and gas welding","spot and seam welding","cold and hot welding","manual and automatic welding"], ans=0,
     exp="The two basic types of welding are arc welding (heat from an electric arc) and gas welding (heat from burning a fuel gas, e.g. oxy-acetylene)."),
dict(q="The heat sources of the two welding types are:", opts=["arc \u2192 electricity; gas \u2192 oxy-acetylene","arc \u2192 gas; gas \u2192 electricity","both \u2192 electricity","both \u2192 gas"], ans=0,
     exp="Arc welding uses an electric arc as its heat source, while gas welding burns oxygen + acetylene (combustion)."),
dict(q="The chemical equation for the combustion of carbon is:", opts=["C + O\u2082 = CO\u2082","C + O\u2082 = CO","C + H\u2082O = CH\u2084","C + N\u2082 = CN"], ans=0,
     exp="The notes give C + O\u2082 \u2192 CO\u2082 — carbon burns in oxygen to form carbon dioxide (this underlies the heat release in the flame)."),
dict(q="How do we distinguish the oxygen cylinder from the acetylene cylinder?", opts=["Oxygen \u2014 black; acetylene \u2014 brownish","Oxygen \u2014 brownish; acetylene \u2014 black","Both are painted green","Oxygen \u2014 red; acetylene \u2014 blue"], ans=0,
     exp="Per the notes, the oxygen cylinder is black and the acetylene cylinder is brownish (maroon) — colour coding prevents dangerous mix-ups."),
dict(q="How is acetylene compressed into its cylinder?", opts=["Acetone absorbs the acetylene and compresses it in the cylinder","It is frozen into a solid","It is mixed with water","It is stored at low pressure only"], ans=0,
     exp="Acetylene is dissolved in acetone held in the porous mass inside the cylinder — the acetone absorbs and safely compresses the acetylene."),
dict(q="The different kinds of flames produced in the oxy-acetylene reaction are:", opts=["neutral, reducing (carburizing) and oxidizing flames","blue, red and yellow flames","hot, warm and cold flames","soft, medium and hard flames"], ans=0,
     exp="The three oxy-acetylene flames are: neutral (equal O\u2082/acetylene), reducing or carburizing (excess acetylene) and oxidizing (excess oxygen)."),
dict(q="What type of flame is produced if there is more oxygen than acetylene in the reaction?", opts=["oxidizing flame","neutral flame","carburizing flame","reducing flame"], ans=0,
     exp="Excess oxygen gives an oxidizing flame (used for brazing); excess acetylene gives a carburizing/reducing flame."),
dict(q="What type of flame is produced if there is more acetylene than oxygen in the reaction?", opts=["carburizing or reducing flame","oxidizing flame","neutral flame","blue flame"], ans=0,
     exp="Excess acetylene produces the carburizing (reducing) flame — it has three visible zones and is used for welding nickel/chromium alloys."),
dict(q="In the course of C\u2082H\u2082 + O\u2082 burning, which combustion zone is the hottest?", opts=["primary combustion zone (about 3300\u00b0C)","secondary combustion zone","outer envelope","the tip of the flame"], ans=0,
     exp="The notes give the primary combustion zone as the hottest part of the flame, with a temperature of about 3300\u00b0C."),
dict(q="How many types of joints are there, and which are they?", opts=["5 \u2014 tee, butt, corner, lap and edge joints","3 \u2014 tee, butt and lap","4 \u2014 butt, lap, edge and corner","6 \u2014 tee, butt, corner, lap, edge and seam"], ans=0,
     exp="There are five basic weld joints: tee joint, butt joint, corner joint, lap joint and edge joint."),
dict(q="What is a stroke?", opts=["The linear distance the cutting tool moves back and forth during hacksaw cutting","The width of the saw blade","The number of teeth per inch","The angle of the blade"], ans=0,
     exp="A stroke is the linear distance the cutting tool travels back and forth in a cutting operation (e.g. hacksaw cutting)."),
]

# ============================================================================
# SECTION 3 — Bonus calculation (Anonymous)
# ============================================================================
S3 = [
dict(q="A product has an acceptable width of 18 \u00b1 2 mm. Calculate respectively the minimum and maximum acceptable sizes of the product:", opts=["16 mm and 20 mm","18 mm and 20 mm","16 mm and 18 mm","14 mm and 22 mm"], ans=0,
     exp="18 \u00b1 2 mm means the basic size is 18 mm with a tolerance of 2 mm on either side: minimum = 18 \u2212 2 = 16 mm; maximum = 18 + 2 = 20 mm."),
]

# ============================================================================
# AEE 202_Compulsory.pdf — 15 objective questions (chisels/files/hacksaw).
# The scanned key is partially legible; answers below are authenticated with
# standard workshop-technology knowledge and the readable part of the key.
# ============================================================================
COMP = [
dict(q="The cold chisels are made by:", opts=["drawing","rolling","piercing","forging"], ans=3,
     exp="Cold chisels are produced by forging — hot forging shapes the tough tool-steel body and head, giving it the strength to withstand hammer blows (the scanned key for this row was not clearly legible, so the answer follows standard workshop-technology practice)."),
dict(q="The cold chisels are made from:", opts=["cast iron","mild steel","cast tool steel","high speed steel","stainless steel"], ans=2,
     exp="Cold chisels are made from cast tool steel (high-carbon tool steel) — hard enough to cut metal yet tough enough not to shatter under impact; the scanned key also reads (c)."),
dict(q="The cross-section of a chisel is usually:", opts=["rectangular","square","hexagonal","octagonal","circular","triangular"], ans=3,
     exp="A cold chisel usually has an octagonal cross-section — the flats give a good grip and prevent rolling; the key reads (d) octagonal."),
dict(q="A diamond pointed chisel is used for cutting:", opts=["flat surfaces","grooves","keyways","V-shaped grooves","all of the above"], ans=3,
     exp="The diamond-point chisel is used for cutting V-shaped grooves (and squaring corners of grooves); the key reads (d)."),
dict(q="A file with 20 teeth in 25 mm is called:", opts=["rough file","bastard file","second cut file","smooth file","dead smooth file"], ans=0,
     exp="Files are graded by the number of teeth per 25 mm: about 20 teeth per 25 mm is a rough file (bastard \u2248 30, second cut \u2248 40, smooth \u2248 50\u201360, dead smooth \u2265 100); the key reads (a)."),
dict(q="When the file is moved to and fro over the work, it is known as:", opts=["cross filing","draw filing","pull and push filing","none of these"], ans=1,
     exp="Moving the file to and fro along the length of the work is draw filing (both hands on the file, light pressure) — it produces a fine finish; the key reads (b)."),
dict(q="When filing soft metals, the file teeth get clogged with minute particles of metal. The file should be cleaned by:", opts=["washing it with water","rubbing on wood","washing it with dilute acid","using a file card"], ans=3,
     exp="A clogged (pinned) file is cleaned with a file card — a wire brush used along the teeth (water/acid would rust the file); this is the standard workshop answer."),
dict(q="A file removes the metal during:", opts=["forward stroke","return stroke","both forward and return strokes","none of the above"], ans=0,
     exp="A file cuts only on the forward (push) stroke; pressure is released on the return stroke to preserve the teeth; the key reads (a)."),
dict(q="A hacksaw blade cuts on the:", opts=["forward stroke","return stroke","both forward and return strokes","cutting depends upon the direction of force"], ans=0,
     exp="A hacksaw blade cuts on the forward stroke — the teeth point forward, so cutting happens on the push; the return stroke is idle."),
dict(q="The teeth of a hacksaw blade are bent:", opts=["towards right","towards left","alternately to right and left and every third or fourth left straight","may be bent in any direction"], ans=2,
     exp="Hacksaw teeth are set alternately right and left, with every third or fourth tooth left straight — the set widens the kerf so the blade does not jam; the key reads (c)."),
dict(q="A hacksaw blade is specified by its:", opts=["length","material","width","number of teeth","none of the above"], ans=0,
     exp="A hacksaw blade is specified by its length — the centre-to-centre distance between the pin holes (e.g. 250 mm or 300 mm); the key reads (a)."),
dict(q="To prevent the body of the blade from jamming in the saw cut, the teeth of the blade are:", opts=["strengthened","sharpened","set","all of the above","none of the above"], ans=2,
     exp="The teeth are 'set' (bent alternately left and right) so the cut is wider than the blade body — preventing jamming; the key reads (c)."),
dict(q="The type of file used for wood work is:", opts=["single-cut file","double-cut file","rasp-cut file","any one of these"], ans=2,
     exp="Wood is filed with a rasp-cut file — its coarse, individually raised teeth remove soft wood quickly without clogging; the key reads (c)."),
dict(q="V-block is used to:", opts=["check the trueness of a flat surface","locate centres of round rods","check the surface roughness","none of the above"], ans=1,
     exp="A V-block supports round rods/bars and, with a scribing block, is used to locate (mark) their centres — standard workshop practice."),
dict(q="Scribing block is used to:", opts=["hold the round bars during marking","check the trueness of flat surfaces","locate the centres of round bars","check the surface roughness"], ans=2,
     exp="The scribing block, working from the surface plate, scribes lines on work and locates the centres of round bars held in a V-block."),
]

# ============================================================================
# Topic structure for Category 2
# ============================================================================
TOPICS = [
    {"id": "pq-measurement", "name": "Measurement, Precision & Tolerance", "categoryId": "past-questions"},
    {"id": "pq-benchwork", "name": "Marking Out & Benchwork", "categoryId": "past-questions"},
    {"id": "pq-hand-tools", "name": "Hammers, Chisels, Files & Hacksaw", "categoryId": "past-questions"},
    {"id": "pq-drilling-lathe", "name": "Drilling & Lathe Operations", "categoryId": "past-questions"},
    {"id": "pq-materials", "name": "Materials & Engineering Products", "categoryId": "past-questions"},
    {"id": "pq-joining-safety", "name": "Joining, Welding & Workshop Safety", "categoryId": "past-questions"},
]

# topicId -> (list, counter) assignment per question index in the combined lists
def assign(q, topic, idx):
    q["topicId"] = topic
    q["id"] = f"aee_pq_{topic}_{idx:02d}"

def first_sentence(exp):
    s = exp.strip()
    for i, ch in enumerate(s):
        if ch in ".!?" and i > 25:
            return s[: i + 1]
    return s[:140]

counters = {}
out = []

def add(q, topic):
    counters[topic] = counters.get(topic, 0) + 1
    assign(q, topic, counters[topic])
    sol = q["exp"] + (
        "\n\n\U0001F4D8 From the Actual Past Questions material"
        + (" (AGE 201 Workshop Practice past question)" if q["exp"].startswith("The past question") or "key" in q["exp"].lower() or q["exp"].startswith("Per the past") else " (lecture notes)")
        + ": this question is drawn from the past-question bank/lecture notes uploaded to the Drive. "
        + "The answer follows the material's own key, with standard workshop-practice reasoning applied where the key is unclear."
    )
    out.append({
        "id": f"aee_pq_{topic}_{counters[topic]:02d}",
        "topicId": topic,
        "question": q["q"],
        "options": q["opts"],
        "correct": q["ans"],
        "short": first_sentence(q["exp"]),
        "solution": sol,
    })
    return None

# --- route Section 1 ---
def route1(t):
    if any(k in t for k in ["vernier", "micrometer", "steel rule", "calliper", "accuracy", "datum",
                            "tolerance", "variation", "minimum diameter", "allowance", "acceptable width",
                            "measurement", "non-linear", "hollow pipe"]):
        return "pq-measurement"
    if any(k in t for k in ["footwear", "ultra violet", "gloves", "workshop floor", "safety precaution", "horse play", "corrosive"]):
        return "pq-joining-safety"
    if any(k in t for k in ["marking out", "workbench", "vice", "bench", "v-block", "scribing"]):
        return "pq-benchwork"
    if any(k in t for k in ["hammer", "hacksaw", "chisel", "file", "stroke", "teeth", "blade", "pein", "coarseness"]):
        return "pq-hand-tools"
    if any(k in t for k in ["drill", "lathe", "spindle", "hole", "revolving", "pillar"]):
        return "pq-drilling-lathe"
    if any(k in t for k in ["soldering", "welding", "joint", "join", "flame", "acetylene", "oxygen", "arc", "bolt", "rivet", "permanent", "temporary"]):
        return "pq-joining-safety"
    if any(k in t for k in ["material", "metal", "cast iron", "stiffness", "ingenuity", "product", "manufacturing"]):
        return "pq-materials"
    return "pq-benchwork"

for q in S1:
    add(q, route1(q["q"].lower()))

# --- route Section 2 ---
def route2(t):
    if any(k in t for k in ["accuracy", "precision"]):
        return "pq-measurement"
    if any(k in t for k in ["ppe", "safety"]):
        return "pq-joining-safety"
    if any(k in t for k in ["hammer mass", "light jobs", "moderate jobs", "heavy jobs", "hacksaw", "chisel",
                            "file", "teeth", "sawing", "filing", "saw", "stroke", "cut of teeth", "cutting operations",
                            "hand tools", "power tools"]):
        return "pq-hand-tools"
    if any(k in t for k in ["bench", "vice", "fitting", "assembling", "marking out", "work bench", "jaw"]):
        return "pq-benchwork"
    if any(k in t for k in ["welding", "flame", "acetylene", "oxygen", "joint", "soldering", "riveting", "bolting",
                            "dyeing", "tapping", "threads", "combustion", "cylinder", "zone", "temporary", "permanent"]):
        return "pq-joining-safety"
    return "pq-materials"

for q in S2:
    add(q, route2(q["q"].lower()))

# --- route Section 3 (bonus) ---
for q in S3:
    add(q, "pq-measurement")

# --- route Compulsory ---
for q in COMP:
    topic = "pq-benchwork" if ("V-block" in q["q"] or "Scribing block" in q["q"]) else "pq-hand-tools"
    add(q, topic)

if __name__ == "__main__":
    json.dump({"topics": TOPICS, "questions": out},
              open(".past_questions_out.json", "w"), ensure_ascii=False, indent=2)
    by_t = {}
    for q in out:
        by_t[q["topicId"]] = by_t.get(q["topicId"], 0) + 1
    print("TOTAL:", len(out))
    for k, v in by_t.items():
        print(" ", k, "->", v)
