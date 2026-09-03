#!/usr/bin/env python3
"""Replace TOPIC_DEEP_DIVE and TOPIC_IMAGES in StudyRunner.jsx with merged-topic versions."""
import re

SRC = "src/components/StudyRunner.jsx"
text = open(SRC).read()

NEW_DEEP_DIVE = """const TOPIC_DEEP_DIVE = {
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
Exam tip: Arc = #10/12, Gas = #4; acetylene ≤15 psi and ≤3/4 turn.`,
}
"""

NEW_IMAGES = """const TOPIC_IMAGES = {
  'welding-processes-defects': '/images/welding-defects.png',
  'metal-working': '/images/anvil-diagram.png',
  'heat-treatment': '/images/anvil-diagram.png',
  'cutting-tools': '/images/hacksaw-tpi.png',
  'drilling': '/images/taper-pin.png',
  'fasteners': '/images/taper-pin.png',
  'jigs-fixtures': '/images/jig-vs-fixture.png',
}
"""

# --- replace deep dive object ---
start = text.find("const TOPIC_DEEP_DIVE = {")
end_marker = "\n\n// Image mapping for AEE topics"
end = text.find(end_marker)
if start < 0 or end < 0:
    raise SystemExit("markers not found")
text = text[:start] + NEW_DEEP_DIVE.rstrip("\n") + "\n" + text[end:]

# --- replace images object ---
start2 = text.find("const TOPIC_IMAGES = {")
end_marker2 = "\n\nexport default function StudyRunner()"
end2 = text.find(end_marker2)
if start2 < 0 or end2 < 0:
    raise SystemExit("TOPIC_IMAGES markers not found")
text = text[:start2] + NEW_IMAGES.rstrip("\n") + "\n" + text[end2:]

open(SRC, "w").write(text)
print("StudyRunner updated: deep dives + topic images merged")
