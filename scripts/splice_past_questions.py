#!/usr/bin/env python3
"""Splice Category 2 (Actual Past Questions) topics & questions into data.js,
and add StudyRunner deep dives."""
import json

DATA = json.load(open(".past_questions_out.json"))
TOPICS = DATA["topics"]
QUESTIONS = DATA["questions"]

DEEP_DIVES = [
    ("pq-measurement",
     """MEASUREMENT, PRECISION & TOLERANCE — Past-question overview:
• Vernier caliper: main scale + sliding vernier scale; more precise than a ruler (reads to about 0.02 mm).
• Micrometer screw gauge: C-shaped frame (resembles a C-clamp); parts: frame, anvil, spindle, thimble, barrel, ratchet — 'beam' belongs to a vernier caliper, NOT a micrometer.
• Steel rule: measures linear dimensions with an accuracy of about 0.20 mm.
• Callipers: inside and outside callipers transfer sizes (internal/external diameters) and are read on a rule. For both inside AND outside diameters at once (e.g. a hollow pipe), use the vernier caliper.
• Datum: the surface plate — the reference plane for marking out and measurement (used with a scribing block).
• Workshop measurement types: linear and angular.
• Tolerances: tolerance = upper deviation − lower deviation. Bilateral tolerance varies on BOTH sides of the basic size (e.g. +0.05/−0.01). Maximum variation = +0.05 − (−0.01) = 0.06 mm. Minimum size = basic + lower deviation. Allowance = minimum hole − maximum shaft (tightest fit); clearance = maximum hole − minimum shaft (loosest fit).
• 18 ± 2 mm → minimum 16 mm, maximum 20 mm.
• Accuracy = closeness to the TRUE value; Precision = closeness of repeated measurements to each other.
Exam tips: keep deviations signed when subtracting; always take upper−lower for tolerance, hole−shaft for allowance/clearance."""),
    ("pq-benchwork",
     """MARKING OUT & BENCHWORK — Past-question overview:
• Marking out = scribing guide lines on the work (defines shape, guides the machinist, shows exact positions) — it does NOT remove material.
• Tools: surface plate (datum), scriber, punch, V-block (supports round bars, locates centres), scribing block (locates centres of round bars), angle plate, try-square.
• Benchwork: rigid bench of hard solid wood or steel; 'fitting' and 'assembling' are used interchangeably and are interdependent (bench operations).
• Vice = work-holding tool. Types (BPHP): Bench vice (fixed on bench), Pipe vice (round objects — pipes/shafts), Hand vice (holds workpieces steady), Pin vice (tiny objects). Bench vice has fixed + movable jaw — the movable jaw adjusts to the job. Vice size = width of jaw + maximum opening between jaws.
• First step in laying out a drilled hole: centre-punch the point before drawing the circle.
• Deburring (removing sharp/rough edges) can be done by scraping (hand scraper) among the listed methods.
• Workbench operations include hammering.
Exam tips: memorise the BPHP vice types and what each holds; marking out = scribing, never cutting."""),
    ("pq-hand-tools",
     """HAMMERS, CHISELS, FILES & HACKSAW — Past-question overview:
• Hammers: types ball peen, straight pein, cross pein (no 'rectangular pein'). Parts: head (face + pein), eye, handle (no 'trunk'). Made of forged steel. Masses: light jobs 0.11–0.33 kg; moderate 0.33–0.45 kg; heavy 0.45 kg and above.
• Chisels: hand cutting tools made by forging, from cast tool steel, usually octagonal in cross-section. Diamond-point chisel cuts V-shaped grooves. Chisel removes thick layers (edges more than about 0.6 mm); file removes thin layers.
• Files: slanting rows on the surface = the cut of teeth. Coarseness grades: rough (~20 teeth/25 mm), bastard, second cut, smooth, dead smooth. Single cut teeth at 45° (per the paper). Cuts only on the forward stroke. Cleared with a file card when pinned. After sawing, the file cleans the surface. Wood work → rasp-cut file. Filing methods: straight, cross, draw (draw filing = moving to and fro over the work). Sizes: 100–250 mm and 250–450 mm.
• Hacksaw: cutting tool; cuts on the forward stroke (most active — removes max metal in one stroke). Teeth set alternately right/left, every 3rd or 4th straight (prevents jamming). Blade specified by its length. Stroke = linear distance the tool moves back and forth. Cutting operations: sawing, filing, chipping. Sawing functions: cut into parts + remove layers.
Exam tips: hammer mass ranges and file coarseness grades are favourite past questions — learn the numbers."""),
    ("pq-drilling-lathe",
     """DRILLING & LATHE OPERATIONS — Past-question overview:
• Drill types: flat drill, straight fluted drill, twist drill — pillar drill is a drilling MACHINE, not a drill type.
• Drilling machine size is determined by the range of spindle speeds (with the largest drill capacity).
• Spindle speed in drilling is based on the diameter of the metal piece (with the recommended cutting speed: N = v/πd).
• Pillar drilling machine: the drill spindle is attached to the column.
• Drilling safety: know the correct speed and feed, and never hold a revolving drill.
• Hole layout: punch the centre point first, then draw the circle.
• Lathe: workpiece held between the headstock and tailstock; the lathe bed provides the sitting position for the tailstock and the sliding guide ways.
Exam tips: pillar drill = column; lathe holding = headstock + tailstock; drill speed depends on diameter + cutting speed."""),
    ("pq-materials",
     """MATERIALS & ENGINEERING PRODUCTS — Past-question overview:
• Material selection is based on availability, cost and suitability — NOT the size of the material.
• Physical property of metals: density (ductility, malleability and elasticity are mechanical properties).
• Stiffness = ability to resist deformation under stress (elasticity = regain original shape; plasticity = retain deformation).
• Cast iron is obtained by melting pig iron with limestone and coke.
• Engineering products = products of ingenuity: conceptualise the idea, translate it into design, transform the design into a product in the workshop.
• Manufacturing = 'bringing new materials to life'.
Exam tips: learn the physical vs mechanical property split and the cast-iron cupola charge."""),
    ("pq-joining-safety",
     """JOINING, WELDING & WORKSHOP SAFETY — Past-question overview:
• Safety: 'Safety first, work next'; PPE = Personal Protective Equipment(s). Footwear protects against heavy objects falling on the feet. Gloves protect against electric shock, corrosive fluids, hot material and horseplay. UV rays and flying splinters endanger the EYES most. A good workshop floor resists wear, carries loads and is non-slip (chemical resistance is not a stated requirement).
• Joining: temporary = bolting; permanent = soldering, riveting and welding. Electronic circuit-board terminals are joined by SOLDERING.
• Threads: external threads = dyeing (with a die); internal threads = tapping.
• Welding: two types — arc (heat from electricity) and gas (oxy-acetylene combustion). C + O₂ → CO₂. Oxygen cylinder = black; acetylene cylinder = brownish (maroon). Acetylene is absorbed by ACETONE inside the cylinder. Three flames: neutral, carburizing/reducing (excess acetylene), oxidizing (excess oxygen). Hottest zone = primary combustion zone (~3300°C). Five joints: tee, butt, corner, lap and edge.
Exam tips: oxidising ↔ excess oxygen; carburizing ↔ excess acetylene; cylinder colours and the five joints are repeated favourites."""),
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
    end = find_bracket_end(src, open_b)
    insert_at = end - 1
    src = src[:insert_at] + ",\n" + fmt_topics(TOPICS) + "\n  " + src[insert_at:]

    # ---- 2) append questions to questionBank.aee202 ----
    i_qb = src.find("export const questionBank = {")
    i_a2 = src.find("aee202: [", i_qb)
    open_b2 = src.find("[", i_a2)
    end2 = find_bracket_end(src, open_b2)
    insert_at2 = end2 - 1
    src = src[:insert_at2] + ",\n" + fmt_questions(QUESTIONS) + "\n" + src[insert_at2:]

    open("src/data.js", "w").write(src)
    print(f"data.js: +{len(TOPICS)} topics, +{len(QUESTIONS)} questions")

    # ---- 3) StudyRunner deep dives ----
    sr = open("src/components/StudyRunner.jsx").read()
    marker = "const TOPIC_DEEP_DIVE = {"
    i_dd = sr.find(marker)
    if i_dd < 0:
        raise SystemExit("TOPIC_DEEP_DIVE not found")
    i_imgs = sr.find("const TOPIC_IMAGES", i_dd)
    close = sr.rfind("\n}", i_dd, i_imgs)
    if close < 0:
        raise SystemExit("deep dive closing brace not found")
    entries = [f"  '{key}': `{text}`" for key, text in DEEP_DIVES]
    insertion = ",\n".join(entries) + ",\n"
    sr = sr[:close] + insertion + sr[close:]
    open("src/components/StudyRunner.jsx", "w").write(sr)
    print(f"StudyRunner: +{len(DEEP_DIVES)} deep dives")


if __name__ == "__main__":
    main()
