import { useState, useEffect } from 'react'
import { useNavigate, Navigate, Link } from 'react-router-dom'
import { loadStudySession, saveStudySession } from '../progress.js'
import { topicMeta } from '../data.js'
import RichText from './RichText.jsx'

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

// Topic-focused deep dives for AEE — each appears for any question from that topic
const TOPIC_DEEP_DIVE = {
  'welding-processes-defects': `WELDING PROCESSES & DEFECTS — Master overview (merges Welding Defects, Classification, MIG, TIG, Gas, Arc, Production & Metal Joining):
DEFECTS (11 key ones): Slag = flux on surface (low heat + slow speed); Undercut = groove melted away (high amperage, wrong angle); Porosity = holes (low gas, too fast); Incomplete Fusion/Cold Weld = gap, breaks soon (low heat, wrong angle); Overlap = excess metal flowing onto base (too much weld); Underfill = valley, too little metal (too fast); Spatter = bumps to grind (low amperage, long wire); Excessive Convexity = mountain vs Concavity = valley; Excessive Reinforcement = too tall/wide; Incomplete Penetration = wire doesn't reach root; Excessive Penetration = burn-through (dwell too long).
CLASSIFICATION: Arc (Carbon, Metal, MIG, TIG, Plasma, Submerged, Electro-slag); Gas (Oxy-acetylene, Air-acetylene, Oxy-hydrogen); Resistance (Butt, Spot, Seam, Projection, Percussion); Thermit; Solid State (Friction, Ultrasonic, Diffusion, Explosive); Newer (Electron-beam, Laser); Related (Brazing, Soldering, cutting).
MIG: DCRP power supply + wire feeder + gas control. Shielding gases: Argon thin sheet, Helium thick metals, CO₂ low/medium carbon steel. AWS ER 70 S 6 = electrode, rod, 70,000 psi tensile, solid bare wire, composition 6. Metal transfer: Globular, Short-arc (4-step short circuit), Spray.
TIG: non-consumable tungsten electrode + separate filler; AC/DC power + high-frequency unit; #11/12 lens; argon/helium shielding; welds ferrous & non-ferrous with less spatter.
GAS: cylinders O₂ 125, acetylene 16 kg/cm²; working pressures O₂ 1, acetylene 0.15 kg/cm². Flame types: Neutral (1:1 — hottest, ideal), Carburizing/Reducing (excess acetylene — 3 zones, Ni/Cr alloys), Oxidizing (excess oxygen — brazing). Light acetylene first, never exceed 15 psi acetylene.
ARC: heat from electric arc; AC transformer or DC generator; EXXXX electrode code: 1st two digits = tensile strength in ksi (E6013 → 60,000 psi), 3rd = position (1 all, 2 flat+horizontal, 3 flat only), 4th = coating. Positions: Flat, Horizontal, Vertical, Overhead (hardest).
PRODUCTION: Plastic/Pressure (heated to plastic, forced together — Resistance) vs Fusion/Non-Pressure (molten — Gas, Arc). Robotic welding automates weld + handling.
JOINING: Temporary (bolts, rivets) vs Permanent. Soldering <450°C (lead-tin ~183°C), Brazing >450°C (below base melting), Welding melts the base metal.
Exam tip: identify the key phrase — "holes" = Porosity, "flux on surface" = Slag, "groove" = Undercut, "gap/cold" = Fusion, "valley" = Underfill/Concavity, "mountain" = Convexity, "burn through" = Excessive Penetration.`,

  'fasteners': `FASTENERS — Overview (bolts, heads, points, rivets & inserts):
BOLTS: Carriage (round head, ribs/flats prevent turning — attractive external), Hex (most common, 3 grades, ¼-4"), Track (elliptical head, railroads), Aircraft (high-strength, D.O.D.), Lag (square head, conical point, wood/masonry), Square, Plow, Flanged.
HEADS: Washer/Flanged (no separate washer needed), Binding (undercut, stranded wire, electrical), Fillister (deep slot, high torque), Truss (large bearing area, soft materials), Pan, 12-point (aircraft, high torque), Flat (flush).
POINTS: Cup (most common, Rockwell C45), Flat (frequent resetting), Cone (permanent, greatest holding), Oval (frequent adjustment, lowest holding), Half Dog (permanent, spotted hole).
RIVETS: Semitubular (hole depth ≤1.12× diameter, becomes solid when set — MOST USED), Full tubular (hole >1.12× diameter, punches own holes in soft materials), Bifurcated/split (prongs make own holes), Metal Piercing (pierces thin sandwich, hardness ≤RB50), Pull-mandrel blind (pull-through, break, nonbreak).
INSERTS: Pressed-in, Self-tapping, Solid-bushing, Molded-in, Ultrasonic (thermoplastics), Wire-thread (repair).
CALCULATION: Taper pin — taper ¼" per foot, d = D − 0.02088 × L (inches). Example: D = 0.5", L = 2" → d = 0.45824".`,

  'metal-working': `METAL WORKING (HOT & COLD) — Overview:
HOT WORKING SAFETY: proper clothing, eye protection (#10/12 arc, #4 gas), hair restrained, correct tools, ventilated area, never touch hot metal, turn off heat, avoid flammables.
MELTING POINTS: Wrought iron 1540°C, Mild steel 1483°C, Cast iron 1261°C (white), Copper 1094°C, Zinc 427°C, Lead 316°C.
HEAT SOURCES: Electrical — Elect soldering 204°C/150W, Carbon arc 4982°C/150A, TIG/MIG 6427°C/200A. Chemical — Propane torch 1261°C, Acetylene 3485°C, Propane cutting 2873°C.
ANVIL PARTS: Hardy hole (for cutting), Pritchel hole, Face, Horn, Base, Cutting block, Body. Tongs: curved lip, flat lip, gad.
COMMERCIAL METAL SHAPES (how measured): Hexagon/Octagon = distance across flats; Round = diameter; I-beam = height × web thickness × flange width; Plate = thickness × width; Sheet metal = thickness × width × length; Square/Tubing/Angle/Band/Channel = width × length (or leg × leg × thickness).
Exam tip: "How is a Hexagon measured?" → across flats. Round → diameter. I-beam → height × web × flange.`,

  'heat-treatment': `HEAT TREATMENT OF STEEL — Full topic:
Purpose: Hardening, Tempering, Annealing.
HARDENING: heat steel (pearlite) to light cherry red → Austenite, then cool QUICKLY in warm water → Martensite (very hard).
TEMPERING: reheat hardened steel for desired hardness + toughness. Stages: 93–204°C retain hardness + some toughness; 204–371°C moderately hard/tough; 371–538°C less hard, more tough.
TEMPER COLOURS: Yellow 221°C (hammers), Straw 243°C (punches/dies), Light brown 260°C (axes), Purple 277°C (rivet sets), Blue 293°C (screwdrivers/springs), Gray 371°C = soft (annealing point).
ANNEALING: heat above 716°C (critical, depends on carbon) and cool SLOWLY (oven/vermiculite/sand) — softens, allows bending, relieves stress.
Exam tip: quick cool = hardening; slow cool = annealing; reheating after hardening = tempering.`,

  'cutting-tools': `CUTTING TOOLS & HACKSAWS — Key points:
FILES: selected by length, coarseness, shape, teeth (parts: Tang, Heel, Body, Edge, Point). Coarseness: Bastard, Second cut, Smooth. Cuts: Single, Double.
HACKSAW BLADE TPI (pick by stock thickness): 14 TPI for 1" and over (cast iron, machine steel, brass); 18 TPI for ¼"–1" (annealed tool steel); 24 TPI for 1/8"–¼" (iron, steel, drill rod); 32 TPI for 1/8" and less.
THREE-TEETH RULE: at least 3 teeth must contact the metal (too coarse = teeth break, too fine = inefficient).
BROKEN BLADE: turn work over and start a new blade on the opposite side, or finish with another old blade.
PEEN HAMMERS: Ball peen, Straight peen, Cross peen. COLD CHISELS: Cape, Half-round nose, Diamond point.
Exam tip: given a stock thickness, pick the TPI whose range contains it.`,

  'drilling': `DRILLING & DRILL PRESS — Key points:
DRILLING: round hole made with a rotating end-cutting tool (drill). REAMING: enlarges to a very accurate size with a reamer (end + side cutting).
PROCEDURE: centre-punch a dent → lubricate → hold in vise (or V-block for round work) → drill.
RPM (Table 5-2, high-speed drills): 1/4" in low-carbon steel 1,200–1,700 RPM, in aluminium/brass 3,000–4,500 RPM; 1/2" in aluminium 1,500–2,250 RPM. Reduce by half for carbon drills. For number/letter drills use the nearest fractional size.
TWIST DRILL PARTS: Tang, Heel, Body, Edge, Point. Shanks: tapered, straight, bit-stock, blacksmith.
DRILL SIZES: Number (80 = 0.0135" to 1 = 0.2280"), Letter (A = 0.2340" to Z = 0.4130"), Fractional (1/64" = 0.0156" to 1").
CUTTING FLUIDS: Aluminium → kerosene/soluble oil; Brass/Bronze → soluble/mineral; Cast iron → dry/compressed air; Copper → soluble/lard/mineral; Tool steel → sulfurized oil.
TAPPING: cutting internal threads with a tap (taper, plug, bottoming types).`,

  'bench-work-fitting': `BENCH WORK & FITTING — Overview:
Bench Work = making/creating by hand at the bench; Fitting = assembling components together.
HACKSAW: teeth set alternately right/left, every 3rd/4th tooth straight.
COLD CHISEL: removes thick layers; has clearance, rake and cutting angles. FILE: removes thin layers with slanting teeth; classified by size (100–200 mm fine, 200–400 mm heavy) and cut (single 60°, double 60° + 80°).
FILING METHODS: Cross filing (across the work), Straight filing, Draw filing (both hands on the file).
MARKING OUT: scribing guide lines; tools include Surface/Table, Scriber, Punch, V-block, Angle plate, Try-Square.
WORKSHOP MACHINES seen in the material: sheet rolling (4ft/8ft), electronic punching (1000W), pillar drilling (variable speed), pedestal grinding, bandsaw, press, hand shear, lathe, heavy-duty lathe.
This topic is mostly theory — focus on definitions and tool names.`,

  'machine-operations': `MACHINE OPERATIONS — Shaping, Turning, Milling, Drilling, Sawing, Robotics:
SHAPING: cutting so a part fits another, very precise (down to ½ mm), small fine cuts; needs programming; disadvantage — needs a very skilled technician if the tool breaks.
TURNING: material removal to create rotational parts on a lathe (workpiece rotates, cutter feeds). Advantage: 360° removal. Disadvantage: hard to rotate with precise accuracy.
MILLING: multi-point rotating tool removes metal briskly. Advantage: performs almost any operation with great accuracy — indispensable. Disadvantage: needs training, expensive.
DRILLING: round hole with an end cutting tool. Advantage: very fast, small accurate holes. Disadvantage: factory temperatures affect it.
SAWING: cuts bars/shapes in plates with disks/blades/bands. Advantage: cuts strong objects precisely. Disadvantage: very dangerous (hand/finger accidents).
ROBOTIC WELDING: programmable robots fully automate welding + handling (resistance spot + arc in automotive). Introduced in the US 1960s, welding take-off 1980s. Advantages: speed, less injury. Disadvantages: expensive, costly to fix, may cause cold welds/pinholes, needs training.`,

  'advanced-manufacturing': `ADVANCED MANUFACTURING — Definition & Goals:
DEFINITION: use of innovative technology ("advanced", "innovative", "cutting edge") to improve products or processes; integrates new technology in both products and processes.
APPROACH: builds for immediate/nearly immediate sale, not for stock; more flexible to changing needs.
GOAL: produce in the least amount of time while minimizing waste; out-perform competitors, build faster/better.
CHARACTERISTICS: high level of design; technologically complex and superior to counterparts; cutting-edge/innovative; reliable, affordable, readily available; newer/better/exciting; solves common problems.
EXAMPLE: Toyota vs GM. Robotic technology is "the way of the future".
VOCABULARY: Innovative, Relevant, Cutting Edge, Flexible, Specifically, Approach.
Exam tip: "fundamental goal" → least time + least waste; "characteristics" → high design, complex/superior, cutting-edge, reliable/affordable.`,

  'hand-tools': `HAND & POWER TOOLS — Overview:
The material separates WORKSHOP HAND TOOLS from POWER TOOLS and MACHINES.
Hand tools: hacksaw (e.g. the 100 mm (4") WESTMORE hacksaw shown in the slides), files, chisels, hammers, screwdrivers, spanners/wrenches, pliers — operated by hand power.
Power tools: electrically driven portable tools (e.g. BOSCH belt sander, DEWALT tools listed under power tools in the material).
Machines: fixed workshop machines (e.g. pillar drilling machine) are NOT power tools.
Exam tip: read the question carefully — it will ask whether the item is listed under Hand Tools, Power Tools or Machines.`,

  'jigs-fixtures': `JIGS & FIXTURES — Complete topic:
DEFINITION: Jigs and fixtures are production tools used to accurately manufacture duplicate and interchangeable parts. They are specially designed so large numbers of components can be machined or assembled identically, ensuring interchangeability.
INTERCHANGEABILITY: essential for mass production — it facilitates easy assembly and reduces unit cost.
JIG vs FIXTURE: a jig holds the work AND guides the cutting tool; a fixture only holds/locates the work. Both eliminate individual marking, positioning and frequent checking.
ADVANTAGES: Productivity (eliminates marking/positioning/checking, higher speed-feed-depth with rigid clamping); Skill reduction (unskilled/semi-skilled operators can be employed → labour cost savings); Interchangeability (identical parts); Cost & time savings.
LOCATING POINTS: good facilities must be provided for locating the work; the workpiece must be easily inserted and quickly removed so no time is wasted placing it.
Exam tip: "increases productivity by eliminating marking & checking" and "makes unskilled operators possible" are the two most-quoted advantages.`,

  'workshop-safety': `WORKSHOP SAFETY & HAZARDS — Comprehensive:
ACCIDENTS: unforeseen circumstances that occur unavoidably; usually due to negligence. Safety rules are a must.
IRRESPONSIBLE BEHAVIOUR (3 categories): The Careless Ones — observe no precautions, always surprised, usually first to get hurt; The Clever Ones — take careless risks, "know it all" (identified by their missing fingers); The Doctors — joke about everything, even at the expense of safety.
HORSEPLAY: absolutely forbidden — pranks cause injuries; a supervisor should remove offenders.
CLOTHING/PPE: wool/cotton coveralls or lab coats, good repair, proper fit, safety shoes; no rolling sleeves, no ties/watches/rings; restrain hair and scarves; goggles/gloves/masks as required.
TOOLS: never use without instruction + permission; use tools in good condition; never clean/adjust/lubricate while operating; never leave unattended; keep guards in place; keep the area tidy; report all injuries.
ARC WELDING SAFETY: #10/12 filter lens, clear flip-up for chipping, insulated holder/cables, never weld wet, wool/cotton only, metal container for stubs, ventilate (lead/zinc fumes are toxic), no matches/lighters.
GAS WELDING SAFETY: #4 filter, open acetylene ≤3/4 turn (quick close) and oxygen fully, never exceed 15 psi acetylene, point tip away from body, light with an approved lighter, never leave a lit torch, no oil/grease near oxygen (explosive).
COLD METAL WORKING: eye protection, proper clothing, restrained hair, correct tools, clean area, guards in place.
Exam tip: Arc = #10/12, Gas = #4; acetylene ≤15 psi and ≤3/4 turn.`,  'fs-centre-lathe': `CENTRE LATHE & LATHE OPERATIONS — First Shared Slide overview:
• Cutting speed: recommended 35 m/min for cast iron/mild steel with HSS tools; 65–70 m/min with tungsten carbide; non-ferrous materials allow much higher speeds. Cutting fluid removes heat and lubricates the tool face (reduces chip–tool friction) — use it for efficiency and longer tool life.
• The lathe: centre lathe = engine lathe; main function is producing cylindrical surfaces. Bed holds/supports all parts (machined guide ways on top). Headstock (extreme left) has shafts/gears in oil, motor-driven shaft, hollow spindle driven at various r.p.m. by changing gears, chuck (3/4 jaw). Tailstock (right end) slides on guide ways, spindle axis coincides with headstock spindle axis; carries the dead centre (live centre if it rotates with the work). Carriage slides bed-length, driven by hand wheel or feed rod/shaft; cross slide moves crosswise; compound rest rotates in a horizontal plane (protractor reading, used for taper turning, manual only); apron hides the gears. Lead screw (screwed) = screw cutting; feed shaft (plain) = turning etc.; engaged one at a time.
• Size of lathe = distance between headstock chuck and tailstock centre (longest job). Swing = vertical distance chuck centre to bed = radius of largest work piece.
• Work holding: 3-jaw self-centering (round stock); 4-jaw for irregular jobs (each jaw independent); centering = work centre line coincides with spindle centre line.
• Turning: v = πdN; tool tip at job centre height; depth of cut 1–1.5 mm via cross slide; traverse by carriage (right to left); feed in mm/rev; feed per minute = N × f; repeat passes (1–1.5 mm each) until desired diameter.
• Facing: cross slide feed, carriage locked → flat circular section used as datum for lengths.
• Taper turning: conical surface by gradual diameter reduction; tool moves along a line inclined to the work axis; taper defined by half angle α. Methods: compound rest swivelled by α; tailstock set-over (small tapers, not accurately measurable); taper turning attachment on backside of cross slide (accurate, wide range); form tool (very short tapers; keep profile short to avoid vibration).
• Parting: plunge cut, carriage locked, job parts at centre line. Profile/form turning: radius/semicircular forms with a form tool + plunge cut.
• Boring: enlarges an existing hole (drill first via tailstock spindle); boring bar smaller than the hole; internal turning — delicate because you cannot see the cut.
• Threading: helical grooves; carriage connected to lead screw; thread pitch = (lead screw r.p.m. ÷ work r.p.m.) × lead screw pitch; standard thread profile; reversible motors; spindle r.p.m. kept very low.
• Knurling: diamond pattern etched by hardened knurling rollers for better grip.
Exam tips: calculations use v = πdN, feed/min = N × f, and the thread pitch ratio formula — keep units consistent (mm, m/min, r.p.m.).`,
  'fs-shapers-planers': `SHAPERS & PLANERS — First Shared Slide overview:
• Both produce flat surfaces (horizontal, vertical or inclined) with single-point tools like lathe tools; cutting is intermittent — tool cuts forward, idle on return.
• Shaper: hollow cast iron bed houses the slotted lever quick return mechanism driving a horizontal ram in guide ways. Tool post on ram front (raised/lowered by hand wheel; slide swivels in a vertical plane, scale in degrees — incline it for inclined surfaces). Table raises/lowers and moves left/right; vice on top. Clapper box lifts the tool tip on the return stroke so the machined surface is not spoiled.
• Quick return: return stroke takes much less time than the forward stroke. Crank AB (adjustable length R) rotates uniformly; crank pin A is a die block sliding in the slotted lever's slot; lever pivoted at O, connected to the ram by a short link arm. Forward AB₁→AB₂; forward time ∝ α, return time ∝ β.
• Shaper tools: HSS solid or brazed tips, sturdy; tungsten carbide not preferred (intermittent cuts).
• Using the shaper: size = max stroke of ram; stroke 60–70 mm longer than the job (30–35 mm before and beyond); stroke length via crank AB; depth of cut by lowering the tool slide (not the table); feed = lateral table shift during the return stroke; contour cutting = simultaneous table feed + vertical hand feed (very skilled work).
• Planer: for work too large/heavy for a shaper. Tool stationary, table moves past it; feed is given to the tool; more than one tool post; simultaneous horizontal + vertical machining ensures squareness. Cast iron bed with Vee guide ways, grouted base; rack in the table centre for reciprocation; T-slots for clamping; cross rail on two columns; one or two tool heads on the cross rail + one side tool head per column.
• Planer drive: return stroke faster via variable speed reversible motor + limit switches (actuated at stroke ends); stroke length set by limit switch position; cutting speed based on average speed in the forward stroke; feed = lateral distance moved by the tool on the cross rail per cutting stroke (mm). Tools: HSS (occasionally tipped carbide); special tools for T-slot and dove tail slide cutting.`,
  'fs-drilling': `DRILLING MACHINES — First Shared Slide overview:
• Drilling = making a hole in a solid piece with a rotating tool (drill). Flat drill (old) → twist drill (universal). Two cutting edges → multiple point cutting tool.
• Twist drill: taper shank fits a matching tapered sleeve (friction drives it); parallel shank needs a special collet chuck. Two lips at the cutting end; lip angle usually 118°. Chips are guided up the helical flutes.
• Forces: torque rotates the drill; axial force (machine feed, mm per revolution of the drill) pushes it deeper. The chisel edge prevents cutting until it penetrates about 1 mm — make a centre-punch depression to start. Drills: solid HSS hardened and ground; carbide inserts available.
• Machines: Sensitive (12 mm max, high speeds, hand-wheel feed, align hole exactly below spindle); Pillar (heavier; rectangular column lets the table swing aside for base mounting); Radial (heavy workpieces — arm rotates round the column, head moves in/out; polar θ, r reach without shifting the work); Multispindle (mass production).
• Allied operations: core drilling (clean cast holes); step drilling (several diameters on one drill); counter boring (flat seat for washers/nuts/bolt heads; pilot keeps it concentric); counter sinking (tapered entrance; pilot); reaming (sizing + geometry + finish; machine reamer with the drilling machine; 0.38–0.4 mm allowance for holes up to 12.5 mm; follows the original hole); tapping (internal threads; flexible adapter; rough then finish tap; low r.p.m. + good lubricant).
Exam tips: remember the 118° lip angle, the four machine types and their use cases, and the 0.38–0.4 mm reaming allowance.`,
  'fs-milling': `MILLING PROCESS — First Shared Slide overview:
• Milling: rotary cutter with several cutting edges on the periphery — a multiple point cutting tool. Generates flat surfaces, curved profiles and intricate shapes with great accuracy and fine finish.
• Up milling (conventional): cutter and feed in opposite directions; chip thickness nil at start, maximum at exit; teeth try to lift the work from the table. Down milling (climb): same direction at contact; chip maximum at entry; technically superior but needs a backlash eliminator.
• Speeds & feeds: cutting speed = πDN m/min; cutter usually wider than the work → one pass; correct feed measure = mm of work per revolution per tooth = f/(NZ) (f = table feed mm/min, N = cutter r.p.m., Z = teeth); minimum traverse = L + D (D/2 overlap each side); MRR much higher than shaping/planing; intermittent cutting → impact loads, vibration and chatter.
• Peripheral vs face milling: peripheral = edges on the circumference, surface parallel to cutter axis, long arbor deflection limits accuracy, horizontal machines; face = surface perpendicular to cutter axis, limited overhang → better dimensional control and flatness, vertical machines. Face milling combines up cut and down cut; cutter position may be symmetrical or asymmetrical (entry/exit side); asymmetric with larger chip at entry and smaller at exit is ideal.
• Operations: slab (flat surfaces), slot (precision slots), side & face (adjacent horizontal + vertical), form (prismatic shapes, e.g. involute gear form), straddle (two parallel vertical faces), gang (several surfaces with a set of cutters). Central hole + keyway mount cutters on the arbor.
• End mills: peripheral + face milling simultaneously; edges on bottom face and periphery; used for edges, shoulders, grooves, slots, keyway pockets, die sinking, sculpted surfaces; materials — cobalt HSS (super), coated HSS, solid carbide, indexable carbide inserts; taper shank into a vertical machine spindle.
• Machines: horizontal, vertical, universal. Knee type (knee carries saddle + table); universal table swivels for helix cutting + dividing head for indexing; plain = robust, production. Arbor fits spindle nose, extends beyond the supporting bracket; taper-shank cutters go into the hollow spindle for vertical faces; table hand/auto feed + high-speed traverse. Vertical machine: no arbor, vertical spindle for end mills/face cutters/drills.
Exam tips: feed per tooth = f/(NZ); traverse = L + D; down milling ↔ backlash eliminator; face milling → perpendicular surface, better flatness.`,
  'fs-grinding': `GRINDING PROCESS — First Shared Slide overview:
• Grinding uses an emery/corundum wheel (impure Al₂O₃) — thousands of abrasive particles embedded in a bond matrix. Abrasive is second in hardness only to diamond; each particle acts like a tiny cutting tool; grinding is truly chip producing. It gives very accurate size, geometry and roundness, extremely good finish, and machines hardened steel/HSS which other processes cannot.
• Dull grains should split or break away; grains that stay and rub without cutting = glazing defect; premature breaking/splitting = reduced wheel life.
• Modern abrasives: silicon carbide (C) — greenish black, harder and more brittle → low-resistance materials (cast iron, brass, copper); aluminium oxide (A) — brownish, tougher → steel.
• Classification: grit (higher number = finer; >200 = 'flours' F/FF/FFF for jewellers); bond (vitrified V ≈ 80% of industry, silicate S, shellac E, rubber R, resinoid B); grade = bond hardness (A very soft → Z very hard; M, N medium); structure = % of bond material (10–30% of volume; 1 = very closed → 15 = very open). Markings: abrasive, grit, grade, structure, bond.
• Selection & care: follow the manufacturer; thumb rule — hard wheel for soft material, soft wheel for hard material. Balance correctly (many thousand r.p.m.; unbalanced centrifugal forces crack the wheel or spoil bearings). True a fresh wheel (square to the work) and dress to correct wear or open the face — done with a diamond tool.
• Cylindrical grinding: plain vs universal (universal also does internal grinding); work between two centres; wheel at much higher r.p.m.; table traverses the whole length to and fro; depth of cut ≈ 0.015 mm per pass until the desired diameter is reached → perfectly circular profile with very fine finish.
Exam tips: C for carbide/abrasive code C = silicon carbide (cast iron, brass, copper) vs A = aluminium oxide (steel); 0.015 mm depth per pass; vitrified bond ≈ 80%.`,
  'pq-measurement': `MEASUREMENT, PRECISION & TOLERANCE — Past-question overview:
• Vernier caliper: main scale + sliding vernier scale; more precise than a ruler (reads to about 0.02 mm).
• Micrometer screw gauge: C-shaped frame (resembles a C-clamp); parts: frame, anvil, spindle, thimble, barrel, ratchet — 'beam' belongs to a vernier caliper, NOT a micrometer.
• Steel rule: measures linear dimensions with an accuracy of about 0.20 mm.
• Callipers: inside and outside callipers transfer sizes (internal/external diameters) and are read on a rule. For both inside AND outside diameters at once (e.g. a hollow pipe), use the vernier caliper.
• Datum: the surface plate — the reference plane for marking out and measurement (used with a scribing block).
• Workshop measurement types: linear and angular.
• Tolerances: tolerance = upper deviation − lower deviation. Bilateral tolerance varies on BOTH sides of the basic size (e.g. +0.05/−0.01). Maximum variation = +0.05 − (−0.01) = 0.06 mm. Minimum size = basic + lower deviation. Allowance = minimum hole − maximum shaft (tightest fit); clearance = maximum hole − minimum shaft (loosest fit).
• 18 ± 2 mm → minimum 16 mm, maximum 20 mm.
• Accuracy = closeness to the TRUE value; Precision = closeness of repeated measurements to each other.
Exam tips: keep deviations signed when subtracting; always take upper−lower for tolerance, hole−shaft for allowance/clearance.`,
  'pq-benchwork': `MARKING OUT & BENCHWORK — Past-question overview:
• Marking out = scribing guide lines on the work (defines shape, guides the machinist, shows exact positions) — it does NOT remove material.
• Tools: surface plate (datum), scriber, punch, V-block (supports round bars, locates centres), scribing block (locates centres of round bars), angle plate, try-square.
• Benchwork: rigid bench of hard solid wood or steel; 'fitting' and 'assembling' are used interchangeably and are interdependent (bench operations).
• Vice = work-holding tool. Types (BPHP): Bench vice (fixed on bench), Pipe vice (round objects — pipes/shafts), Hand vice (holds workpieces steady), Pin vice (tiny objects). Bench vice has fixed + movable jaw — the movable jaw adjusts to the job. Vice size = width of jaw + maximum opening between jaws.
• First step in laying out a drilled hole: centre-punch the point before drawing the circle.
• Deburring (removing sharp/rough edges) can be done by scraping (hand scraper) among the listed methods.
• Workbench operations include hammering.
Exam tips: memorise the BPHP vice types and what each holds; marking out = scribing, never cutting.`,
  'pq-hand-tools': `HAMMERS, CHISELS, FILES & HACKSAW — Past-question overview:
• Hammers: types ball peen, straight pein, cross pein (no 'rectangular pein'). Parts: head (face + pein), eye, handle (no 'trunk'). Made of forged steel. Masses: light jobs 0.11–0.33 kg; moderate 0.33–0.45 kg; heavy 0.45 kg and above.
• Chisels: hand cutting tools made by forging, from cast tool steel, usually octagonal in cross-section. Diamond-point chisel cuts V-shaped grooves. Chisel removes thick layers (edges more than about 0.6 mm); file removes thin layers.
• Files: slanting rows on the surface = the cut of teeth. Coarseness grades: rough (~20 teeth/25 mm), bastard, second cut, smooth, dead smooth. Single cut teeth at 45° (per the paper). Cuts only on the forward stroke. Cleared with a file card when pinned. After sawing, the file cleans the surface. Wood work → rasp-cut file. Filing methods: straight, cross, draw (draw filing = moving to and fro over the work). Sizes: 100–250 mm and 250–450 mm.
• Hacksaw: cutting tool; cuts on the forward stroke (most active — removes max metal in one stroke). Teeth set alternately right/left, every 3rd or 4th straight (prevents jamming). Blade specified by its length. Stroke = linear distance the tool moves back and forth. Cutting operations: sawing, filing, chipping. Sawing functions: cut into parts + remove layers.
Exam tips: hammer mass ranges and file coarseness grades are favourite past questions — learn the numbers.`,
  'pq-drilling-lathe': `DRILLING & LATHE OPERATIONS — Past-question overview:
• Drill types: flat drill, straight fluted drill, twist drill — pillar drill is a drilling MACHINE, not a drill type.
• Drilling machine size is determined by the range of spindle speeds (with the largest drill capacity).
• Spindle speed in drilling is based on the diameter of the metal piece (with the recommended cutting speed: N = v/πd).
• Pillar drilling machine: the drill spindle is attached to the column.
• Drilling safety: know the correct speed and feed, and never hold a revolving drill.
• Hole layout: punch the centre point first, then draw the circle.
• Lathe: workpiece held between the headstock and tailstock; the lathe bed provides the sitting position for the tailstock and the sliding guide ways.
Exam tips: pillar drill = column; lathe holding = headstock + tailstock; drill speed depends on diameter + cutting speed.`,
  'pq-materials': `MATERIALS & ENGINEERING PRODUCTS — Past-question overview:
• Material selection is based on availability, cost and suitability — NOT the size of the material.
• Physical property of metals: density (ductility, malleability and elasticity are mechanical properties).
• Stiffness = ability to resist deformation under stress (elasticity = regain original shape; plasticity = retain deformation).
• Cast iron is obtained by melting pig iron with limestone and coke.
• Engineering products = products of ingenuity: conceptualise the idea, translate it into design, transform the design into a product in the workshop.
• Manufacturing = 'bringing new materials to life'.
Exam tips: learn the physical vs mechanical property split and the cast-iron cupola charge.`,
  'pq-joining-safety': `JOINING, WELDING & WORKSHOP SAFETY — Past-question overview:
• Safety: 'Safety first, work next'; PPE = Personal Protective Equipment(s). Footwear protects against heavy objects falling on the feet. Gloves protect against electric shock, corrosive fluids, hot material and horseplay. UV rays and flying splinters endanger the EYES most. A good workshop floor resists wear, carries loads and is non-slip (chemical resistance is not a stated requirement).
• Joining: temporary = bolting; permanent = soldering, riveting and welding. Electronic circuit-board terminals are joined by SOLDERING.
• Threads: external threads = dyeing (with a die); internal threads = tapping.
• Welding: two types — arc (heat from electricity) and gas (oxy-acetylene combustion). C + O₂ → CO₂. Oxygen cylinder = black; acetylene cylinder = brownish (maroon). Acetylene is absorbed by ACETONE inside the cylinder. Three flames: neutral, carburizing/reducing (excess acetylene), oxidizing (excess oxygen). Hottest zone = primary combustion zone (~3300°C). Five joints: tee, butt, corner, lap and edge.
Exam tips: oxidising ↔ excess oxygen; carburizing ↔ excess acetylene; cylinder colours and the five joints are repeated favourites.`,

}


// Image mapping for AEE topics that need diagrams — prioritised for AEE
const TOPIC_IMAGES = {
  'welding-processes-defects': '/images/welding-defects.png',
  'metal-working': '/images/anvil-diagram.png',
  'cutting-tools': '/images/hacksaw-tpi.png',
  'jigs-fixtures': '/images/jig-vs-fixture.png',
}


export default function StudyRunner() {
  const navigate = useNavigate()
  const [session, setSession] = useState(() => loadStudySession())
  const [index, setIndex] = useState(session?.index ?? 0)
  const [showSolution, setShowSolution] = useState(false)
  const [revealed, setRevealed] = useState({})

  if (!session) return <Navigate to="/dashboard" replace />

  const questions = session.questionSet
  const total = questions.length
  const q = questions[index]
  const topicNote = ((topicMeta[session.courseId] || []).find((t) => t.id === q.topicId) || {}).summaryNotes
  const deepDive = topicNote || TOPIC_DEEP_DIVE[q.topicId] || `This topic covers ${q.topicId.replace(/-/g, ' ')}. Review the core definitions, formulas, and typical exam traps for this topic. Focus on understanding the *why* behind each option, not just memorizing the answer.`

  useEffect(() => {
    if (!session) return
    const next = { ...session, index }
    saveStudySession(next)
    setSession(next)
    setShowSolution(false)
  }, [index])

  function go(i) {
    if (i < 0 || i >= total) return
    setIndex(i)
  }

  function handleSeeExplanation() {
    setShowSolution(true)
    setRevealed(r => ({ ...r, [q.id]: true }))
  }

  function exitToDashboard() {
    navigate('/dashboard')
  }

  const pct = Math.round(((index + 1) / total) * 100)
  const topicImage = TOPIC_IMAGES[q.topicId]

  return (
    <div className="test-shell">
      <div className="test-topbar" style={{ background: 'linear-gradient(135deg, rgba(193,18,31,0.06), rgba(180,83,9,0.04))' }}>
        <div className="test-meta">
          <div>
            <div className="tm-title">{session.courseCode}{session.topicName ? ` · ${session.topicName}` : ' · Study Mode'} <span style={{ fontSize: 11, background: 'var(--primary)', color: '#fff', padding: '3px 8px', borderRadius: 999, marginLeft: 8, verticalAlign: 'middle' }}>STUDY MODE</span></div>
            <div className="tm-sub">Question {index + 1} of {total} · Correct answer already ticked · No timer</div>
          </div>
        </div>
        <div className="progress-wrap" style={{ minWidth: 180 }}>
          <div style={{ fontSize: 12, color: 'var(--muted)', fontWeight: 600 }}>PROGRESS</div>
          <div className="progress-bar"><div className="progress-fill" style={{ width: `${pct}%` }} /></div>
          <div style={{ fontSize: 11, color: 'var(--muted)', marginTop: 4 }}>{index + 1} / {total} · {Object.keys(revealed).length} explanations viewed</div>
        </div>
        <div className="flex gap-8">
          <button className="btn btn-ghost btn-sm" onClick={exitToDashboard}>Exit Study</button>
          <Link to="/dashboard" className="btn btn-primary btn-sm">New Study Set →</Link>
        </div>
      </div>

      <div className="test-body">
        <div className="qcard" style={{ borderLeft: '4px solid var(--primary)' }}>
          <div className="qhead">
            <span className="qindex">Study Question {index + 1} / {total}</span>
            <span className="qtopic">{q.topicId ? q.topicId.replace(/-/g, ' ') : 'Mixed topics'}</span>
          </div>
          <RichText text={q.question} className="qtext" />

          {q.image && (
            <div style={{ margin: '16px 0', padding: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)', borderRadius: 12, textAlign: 'center' }}>
              <img src={q.image} alt="Question diagram" style={{ maxWidth: '100%', maxHeight: 320, borderRadius: 8, border: '1px solid var(--border)' }} />
              <div style={{ fontSize: 12, color: 'var(--muted)', marginTop: 8 }}>Diagram for visual understanding — tap to zoom</div>
            </div>
          )}

          {topicImage && !q.image && (
            <div style={{ margin: '16px 0', padding: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)', borderRadius: 12, textAlign: 'center', opacity: 0.9 }}>
              <div style={{ fontSize: 12, color: 'var(--muted)', marginBottom: 8, fontWeight: 600 }}>📐 Topic Diagram — {q.topicId.replace(/-/g, ' ')}</div>
              <img src={topicImage} alt={`${q.topicId} diagram`} style={{ maxWidth: '100%', maxHeight: 260, borderRadius: 8, border: '1px solid var(--border)' }} />
            </div>
          )}

          <div className="options">
            {q.options.map((opt, i) => {
              const isCorrect = i === q.correct
              return (
                <div
                  key={i}
                  className={`option ${isCorrect ? 'selected' : ''}`}
                  style={isCorrect ? { borderColor: 'var(--green)', background: 'var(--green-soft)', cursor: 'default' } : { cursor: 'default', opacity: 0.9 }}
                >
                  <span className="opt-key" style={isCorrect ? { background: 'var(--green)', color: '#fff', borderColor: 'var(--green)' } : {}}>{LETTERS[i]}</span>
                  <RichText text={opt} className="rt-opt" />
                  {isCorrect && <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--green)', background: '#fff', padding: '3px 8px', borderRadius: 999, border: '1px solid var(--green)' }}>✓ Correct</span>}
                </div>
              )
            })}
          </div>

          <div style={{ marginTop: 22, display: 'flex', gap: 12, flexWrap: 'wrap' }}>
            <button className="btn btn-primary" onClick={handleSeeExplanation} style={{ flex: 1, minWidth: 200 }}>
              {showSolution ? '✓ Explanation below — scroll down' : 'See Detailed Explanation →'}
            </button>
            <button className="btn btn-ghost" onClick={() => go(index + 1)} disabled={index === total - 1}>
              Next Question →
            </button>
          </div>

          <div className="ri-short" style={{ marginTop: 18, background: 'var(--card-2)' }}>
            <RichText text={'**Quick tip:** ' + q.short} className="rt-inline" />
          </div>

          {showSolution && (
            <div style={{ marginTop: 18, padding: 20, background: 'linear-gradient(135deg, rgba(193,18,31,0.06), rgba(180,83,9,0.04))', border: '1px solid var(--border)', borderRadius: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>📖 Study Mode — Very Detailed Explanation</div>
                <span className="qtopic" style={{ background: 'var(--green-soft)', color: 'var(--green)', borderColor: 'rgba(12,122,84,0.2)' }}>Correct: {LETTERS[q.correct]}. {q.options[q.correct]}</span>
              </div>
              <div className="panel-sol" style={{ background: '#fff' }}>
                <RichText text={q.solution} className="rt-block" />
                <div style={{ marginTop: 18, paddingTop: 18, borderTop: '1px dashed var(--border)' }}>
                  <div style={{ fontWeight: 700, color: 'var(--text)', marginBottom: 8 }}>
                    {topicNote
                      ? '📐 Topic Notes — Key Formulas, Abstractions & Exam Traps:'
                      : `📚 Deep Dive — More on ${q.topicId.replace(/-/g, ' ')}:`}
                  </div>
                  <RichText text={deepDive} className="rt-block" />
                </div>
              </div>
              {(q.image || topicImage) && (
                <div style={{ marginTop: 16, padding: 12, background: '#fff', border: '1px solid var(--border)', borderRadius: 10, textAlign: 'center' }}>
                  <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--muted)', marginBottom: 8 }}>🖼️ Visual Reference — {q.topicId.replace(/-/g, ' ')}</div>
                  <img src={q.image || topicImage} alt="Deep dive diagram" style={{ maxWidth: '100%', maxHeight: 320, borderRadius: 8 }} />
                </div>
              )}
              <div style={{ marginTop: 14, display: 'flex', gap: 10 }}>
                <button className="btn btn-ghost btn-sm" onClick={() => setShowSolution(false)}>Hide explanation</button>
                <button className="btn btn-primary btn-sm" onClick={() => go(index + 1)} disabled={index === total - 1}>Next →</button>
              </div>
            </div>
          )}

          <div className="qnav" style={{ marginTop: 24, borderTop: '1px solid var(--border)', paddingTop: 16 }}>
            <button className="btn btn-ghost" onClick={() => go(index - 1)} disabled={index === 0}>← Previous</button>
            <span style={{ fontSize: 12, color: 'var(--muted)' }}>Study Mode · No timer · Correct already ticked</span>
            {index < total - 1 ? (
              <button className="btn btn-primary" onClick={() => go(index + 1)}>Next →</button>
            ) : (
              <button className="btn btn-ghost" onClick={exitToDashboard}>Back to Dashboard</button>
            )}
          </div>
        </div>

        <div className="palette">
          <h4>Study Navigator</h4>
          <div className="palette-grid">
            {questions.map((qq, i) => {
              const cls = [
                'pcell',
                revealed[qq.id] ? 'answered' : '',
                i === index ? 'current' : ''
              ].filter(Boolean).join(' ')
              return (
                <button key={qq.id} className={cls} onClick={() => go(i)} title={`Question ${i + 1} ${revealed[qq.id] ? '(viewed)' : ''}`}>
                  {i + 1}
                </button>
              )
            })}
          </div>
          <div className="palette-legend">
            <span><span className="legend-dot" style={{ background: 'var(--green-soft)', border: '1px solid rgba(12,122,84,0.4)' }} />Viewed</span>
            <span><span className="legend-dot" style={{ background: 'var(--primary)' }} />Current</span>
          </div>
          <div style={{ marginTop: 18, padding: 12, background: 'var(--primary-soft)', borderRadius: 10, border: '1px solid rgba(193,18,31,0.12)' }}>
            <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)' }}>💡 How Study Mode works</div>
            <div style={{ fontSize: 12, color: 'var(--muted)', marginTop: 6, lineHeight: 1.5 }}>
              No timer. Correct answer is pre-ticked in green. Tap <strong>See Detailed Explanation</strong> for the very long, topic-focused deep dive — longer than Test Mode — with diagrams where needed.
            </div>
          </div>
          <p className="muted" style={{ fontSize: 12, marginTop: 12, lineHeight: 1.5 }}>
            Go at your own pace. No auto-save timer, no pressure.
          </p>
        </div>
      </div>
    </div>
  )
}
