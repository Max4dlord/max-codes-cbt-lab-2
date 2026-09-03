#!/usr/bin/env python3
"""Splice the First Shared Slide questions & topics into src/data.js and add
StudyRunner deep dives for the 5 new topics."""
import json
import re

QUESTIONS = json.load(open(".first_slides_out.json"))
TOPICS = [
    {"id": "fs-centre-lathe", "name": "Centre Lathe & Lathe Operations", "categoryId": "first-slides"},
    {"id": "fs-shapers-planers", "name": "Shapers & Planers", "categoryId": "first-slides"},
    {"id": "fs-drilling", "name": "Drilling Machines", "categoryId": "first-slides"},
    {"id": "fs-milling", "name": "Milling Process", "categoryId": "first-slides"},
    {"id": "fs-grinding", "name": "Grinding Process", "categoryId": "first-slides"},
]

# Study Mode deep dives for the new topics (summary of the slide sections)
DEEP_DIVES = [
    ("fs-centre-lathe",
     """CENTRE LATHE & LATHE OPERATIONS — First Shared Slide overview:
• Cutting speed: recommended 35 m/min for cast iron/mild steel with HSS tools; 65\u201370 m/min with tungsten carbide; non-ferrous materials allow much higher speeds. Cutting fluid removes heat and lubricates the tool face (reduces chip\u2013tool friction) \u2014 use it for efficiency and longer tool life.
• The lathe: centre lathe = engine lathe; main function is producing cylindrical surfaces. Bed holds/supports all parts (machined guide ways on top). Headstock (extreme left) has shafts/gears in oil, motor-driven shaft, hollow spindle driven at various r.p.m. by changing gears, chuck (3/4 jaw). Tailstock (right end) slides on guide ways, spindle axis coincides with headstock spindle axis; carries the dead centre (live centre if it rotates with the work). Carriage slides bed-length, driven by hand wheel or feed rod/shaft; cross slide moves crosswise; compound rest rotates in a horizontal plane (protractor reading, used for taper turning, manual only); apron hides the gears. Lead screw (screwed) = screw cutting; feed shaft (plain) = turning etc.; engaged one at a time.
• Size of lathe = distance between headstock chuck and tailstock centre (longest job). Swing = vertical distance chuck centre to bed = radius of largest work piece.
• Work holding: 3-jaw self-centering (round stock); 4-jaw for irregular jobs (each jaw independent); centering = work centre line coincides with spindle centre line.
• Turning: v = \u03c0dN; tool tip at job centre height; depth of cut 1\u20131.5 mm via cross slide; traverse by carriage (right to left); feed in mm/rev; feed per minute = N \u00d7 f; repeat passes (1\u20131.5 mm each) until desired diameter.
• Facing: cross slide feed, carriage locked \u2192 flat circular section used as datum for lengths.
• Taper turning: conical surface by gradual diameter reduction; tool moves along a line inclined to the work axis; taper defined by half angle \u03b1. Methods: compound rest swivelled by \u03b1; tailstock set-over (small tapers, not accurately measurable); taper turning attachment on backside of cross slide (accurate, wide range); form tool (very short tapers; keep profile short to avoid vibration).
• Parting: plunge cut, carriage locked, job parts at centre line. Profile/form turning: radius/semicircular forms with a form tool + plunge cut.
• Boring: enlarges an existing hole (drill first via tailstock spindle); boring bar smaller than the hole; internal turning \u2014 delicate because you cannot see the cut.
• Threading: helical grooves; carriage connected to lead screw; thread pitch = (lead screw r.p.m. \u00f7 work r.p.m.) \u00d7 lead screw pitch; standard thread profile; reversible motors; spindle r.p.m. kept very low.
• Knurling: diamond pattern etched by hardened knurling rollers for better grip.
Exam tips: calculations use v = \u03c0dN, feed/min = N \u00d7 f, and the thread pitch ratio formula \u2014 keep units consistent (mm, m/min, r.p.m.)."""),
    ("fs-shapers-planers",
     """SHAPERS & PLANERS — First Shared Slide overview:
• Both produce flat surfaces (horizontal, vertical or inclined) with single-point tools like lathe tools; cutting is intermittent \u2014 tool cuts forward, idle on return.
• Shaper: hollow cast iron bed houses the slotted lever quick return mechanism driving a horizontal ram in guide ways. Tool post on ram front (raised/lowered by hand wheel; slide swivels in a vertical plane, scale in degrees \u2014 incline it for inclined surfaces). Table raises/lowers and moves left/right; vice on top. Clapper box lifts the tool tip on the return stroke so the machined surface is not spoiled.
• Quick return: return stroke takes much less time than the forward stroke. Crank AB (adjustable length R) rotates uniformly; crank pin A is a die block sliding in the slotted lever's slot; lever pivoted at O, connected to the ram by a short link arm. Forward AB\u2081\u2192AB\u2082; forward time \u221d \u03b1, return time \u221d \u03b2.
• Shaper tools: HSS solid or brazed tips, sturdy; tungsten carbide not preferred (intermittent cuts).
• Using the shaper: size = max stroke of ram; stroke 60\u201370 mm longer than the job (30\u201335 mm before and beyond); stroke length via crank AB; depth of cut by lowering the tool slide (not the table); feed = lateral table shift during the return stroke; contour cutting = simultaneous table feed + vertical hand feed (very skilled work).
• Planer: for work too large/heavy for a shaper. Tool stationary, table moves past it; feed is given to the tool; more than one tool post; simultaneous horizontal + vertical machining ensures squareness. Cast iron bed with Vee guide ways, grouted base; rack in the table centre for reciprocation; T-slots for clamping; cross rail on two columns; one or two tool heads on the cross rail + one side tool head per column.
• Planer drive: return stroke faster via variable speed reversible motor + limit switches (actuated at stroke ends); stroke length set by limit switch position; cutting speed based on average speed in the forward stroke; feed = lateral distance moved by the tool on the cross rail per cutting stroke (mm). Tools: HSS (occasionally tipped carbide); special tools for T-slot and dove tail slide cutting.""")
    ,
    ("fs-drilling",
     """DRILLING MACHINES — First Shared Slide overview:
• Drilling = making a hole in a solid piece with a rotating tool (drill). Flat drill (old) \u2192 twist drill (universal). Two cutting edges \u2192 multiple point cutting tool.
• Twist drill: taper shank fits a matching tapered sleeve (friction drives it); parallel shank needs a special collet chuck. Two lips at the cutting end; lip angle usually 118\u00b0. Chips are guided up the helical flutes.
• Forces: torque rotates the drill; axial force (machine feed, mm per revolution of the drill) pushes it deeper. The chisel edge prevents cutting until it penetrates about 1 mm \u2014 make a centre-punch depression to start. Drills: solid HSS hardened and ground; carbide inserts available.
• Machines: Sensitive (12 mm max, high speeds, hand-wheel feed, align hole exactly below spindle); Pillar (heavier; rectangular column lets the table swing aside for base mounting); Radial (heavy workpieces \u2014 arm rotates round the column, head moves in/out; polar \u03b8, r reach without shifting the work); Multispindle (mass production).
• Allied operations: core drilling (clean cast holes); step drilling (several diameters on one drill); counter boring (flat seat for washers/nuts/bolt heads; pilot keeps it concentric); counter sinking (tapered entrance; pilot); reaming (sizing + geometry + finish; machine reamer with the drilling machine; 0.38\u20130.4 mm allowance for holes up to 12.5 mm; follows the original hole); tapping (internal threads; flexible adapter; rough then finish tap; low r.p.m. + good lubricant).
Exam tips: remember the 118\u00b0 lip angle, the four machine types and their use cases, and the 0.38\u20130.4 mm reaming allowance."""),
    ("fs-milling",
     """MILLING PROCESS — First Shared Slide overview:
• Milling: rotary cutter with several cutting edges on the periphery \u2014 a multiple point cutting tool. Generates flat surfaces, curved profiles and intricate shapes with great accuracy and fine finish.
• Up milling (conventional): cutter and feed in opposite directions; chip thickness nil at start, maximum at exit; teeth try to lift the work from the table. Down milling (climb): same direction at contact; chip maximum at entry; technically superior but needs a backlash eliminator.
• Speeds & feeds: cutting speed = \u03c0DN m/min; cutter usually wider than the work \u2192 one pass; correct feed measure = mm of work per revolution per tooth = f/(NZ) (f = table feed mm/min, N = cutter r.p.m., Z = teeth); minimum traverse = L + D (D/2 overlap each side); MRR much higher than shaping/planing; intermittent cutting \u2192 impact loads, vibration and chatter.
• Peripheral vs face milling: peripheral = edges on the circumference, surface parallel to cutter axis, long arbor deflection limits accuracy, horizontal machines; face = surface perpendicular to cutter axis, limited overhang \u2192 better dimensional control and flatness, vertical machines. Face milling combines up cut and down cut; cutter position may be symmetrical or asymmetrical (entry/exit side); asymmetric with larger chip at entry and smaller at exit is ideal.
• Operations: slab (flat surfaces), slot (precision slots), side & face (adjacent horizontal + vertical), form (prismatic shapes, e.g. involute gear form), straddle (two parallel vertical faces), gang (several surfaces with a set of cutters). Central hole + keyway mount cutters on the arbor.
• End mills: peripheral + face milling simultaneously; edges on bottom face and periphery; used for edges, shoulders, grooves, slots, keyway pockets, die sinking, sculpted surfaces; materials \u2014 cobalt HSS (super), coated HSS, solid carbide, indexable carbide inserts; taper shank into a vertical machine spindle.
• Machines: horizontal, vertical, universal. Knee type (knee carries saddle + table); universal table swivels for helix cutting + dividing head for indexing; plain = robust, production. Arbor fits spindle nose, extends beyond the supporting bracket; taper-shank cutters go into the hollow spindle for vertical faces; table hand/auto feed + high-speed traverse. Vertical machine: no arbor, vertical spindle for end mills/face cutters/drills.
Exam tips: feed per tooth = f/(NZ); traverse = L + D; down milling \u2194 backlash eliminator; face milling \u2192 perpendicular surface, better flatness."""),
    ("fs-grinding",
     """GRINDING PROCESS — First Shared Slide overview:
• Grinding uses an emery/corundum wheel (impure Al\u2082O\u2083) \u2014 thousands of abrasive particles embedded in a bond matrix. Abrasive is second in hardness only to diamond; each particle acts like a tiny cutting tool; grinding is truly chip producing. It gives very accurate size, geometry and roundness, extremely good finish, and machines hardened steel/HSS which other processes cannot.
• Dull grains should split or break away; grains that stay and rub without cutting = glazing defect; premature breaking/splitting = reduced wheel life.
• Modern abrasives: silicon carbide (C) \u2014 greenish black, harder and more brittle \u2192 low-resistance materials (cast iron, brass, copper); aluminium oxide (A) \u2014 brownish, tougher \u2192 steel.
• Classification: grit (higher number = finer; >200 = 'flours' F/FF/FFF for jewellers); bond (vitrified V \u2248 80% of industry, silicate S, shellac E, rubber R, resinoid B); grade = bond hardness (A very soft \u2192 Z very hard; M, N medium); structure = % of bond material (10\u201330% of volume; 1 = very closed \u2192 15 = very open). Markings: abrasive, grit, grade, structure, bond.
• Selection & care: follow the manufacturer; thumb rule \u2014 hard wheel for soft material, soft wheel for hard material. Balance correctly (many thousand r.p.m.; unbalanced centrifugal forces crack the wheel or spoil bearings). True a fresh wheel (square to the work) and dress to correct wear or open the face \u2014 done with a diamond tool.
• Cylindrical grinding: plain vs universal (universal also does internal grinding); work between two centres; wheel at much higher r.p.m.; table traverses the whole length to and fro; depth of cut \u2248 0.015 mm per pass until the desired diameter is reached \u2192 perfectly circular profile with very fine finish.
Exam tips: C for carbide/abrasive code C = silicon carbide (cast iron, brass, copper) vs A = aluminium oxide (steel); 0.015 mm depth per pass; vitrified bond \u2248 80%."""),
]


def find_bracket_end(s, start):
    depth = 0
    i = start
    in_str = False
    esc = False
    while i < len(s):
        c = s[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    raise ValueError("unbalanced brackets")


def fmt_questions(qs):
    out = []
    for q in qs:
        lines = ["  {"]
        entries = []
        for key in ["id", "topicId", "question", "options", "correct", "short", "solution", "image"]:
            if key not in q:
                continue
            val = q[key]
            if key == "options":
                entries.append(f'    "{key}": [\n' + ",\n".join(json.dumps(o, ensure_ascii=False) for o in val) + "\n    ]")
            elif key == "correct":
                entries.append(f'    "{key}": {val}')
            else:
                entries.append(f'    "{key}": {json.dumps(val, ensure_ascii=False)}')
        lines.append(",\n".join(entries))
        lines.append("  }")
        out.append("\n".join(lines))
    return ",\n".join(out)


def fmt_topics(topics):
    out = []
    for t in topics:
        lines = ["    {"]
        entries = [
            f'      "id": "{t["id"]}"',
            f'      "name": "{t["name"]}"',
            f'      "categoryId": "{t["categoryId"]}"',
        ]
        lines.append(",\n".join(entries))
        lines.append("    }")
        out.append("\n".join(lines))
    return ",\n".join(out)


def main():
    src = open("src/data.js").read()

    # ---- 1) append topics to topicMeta.aee202 ----
    i_tm = src.find("export const topicMeta = {")
    i_a = src.find('"aee202": [', i_tm)
    open_b = src.find("[", i_a)
    end = find_bracket_end(src, open_b)  # index just after closing ]
    # insert before the closing bracket: find the last "\n  ]" before `end`
    insert_at = end - 1  # position of the closing ']'
    new_topics = ",\n" + fmt_topics(TOPICS) + "\n  "
    src = src[:insert_at] + new_topics + src[insert_at:]

    # ---- 2) append questions to questionBank.aee202 ----
    i_qb = src.find("export const questionBank = {")
    i_a2 = src.find("aee202: [", i_qb)
    open_b2 = src.find("[", i_a2)
    end2 = find_bracket_end(src, open_b2)
    insert_at2 = end2 - 1
    new_qs = ",\n" + fmt_questions(QUESTIONS) + "\n"
    src = src[:insert_at2] + new_qs + src[insert_at2:]

    open("src/data.js", "w").write(src)
    print(f"data.js: +{len(TOPICS)} topics, +{len(QUESTIONS)} questions")

    # ---- 3) StudyRunner deep dives ----
    sr = open("src/components/StudyRunner.jsx").read()
    marker = "const TOPIC_DEEP_DIVE = {"
    i_dd = sr.find(marker)
    if i_dd < 0:
        raise SystemExit("TOPIC_DEEP_DIVE not found")
    # find closing "}\n" just before TOPIC_IMAGES
    i_imgs = sr.find("const TOPIC_IMAGES", i_dd)
    close = sr.rfind("\n}", i_dd, i_imgs)
    if close < 0:
        raise SystemExit("deep dive closing brace not found")
    entries = []
    for key, text in DEEP_DIVES:
        entries.append(f"  '{key}': `{text}`")
    insertion = ",\n".join(entries) + ",\n"
    sr = sr[:close] + insertion + sr[close:]
    open("src/components/StudyRunner.jsx", "w").write(sr)
    print(f"StudyRunner: +{len(DEEP_DIVES)} deep dives")


if __name__ == "__main__":
    main()
