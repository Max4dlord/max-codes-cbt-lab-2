#!/usr/bin/env python3
"""Assemble the EEE 202 bank (topics + questions A/B) and emit .eee202_out.json.
Compliance normalisation (senior-examiner format):
- every solution opens with '### Step-by-Step Derivation & Solution'
- step headings are bold '**Step N: ...**' paragraphs
- calc solutions must contain $$ display math; all solutions must contain $
- banned truncation phrases are rejected"""
import json
import re
from eee_topics import TOPICS
from eee_questions_a import QUESTIONS_A
from eee_questions_b import QUESTIONS_B

UMBRELLA = "### Step-by-Step Derivation & Solution"

# Legacy plain-text tokens (programming notation) -> inline LaTeX.
# Applied to question stems, options, shorts and solutions (outside existing
# $...$ / $$...$$ math segments, which are protected).
TOKENS = [
    (r'\bX_L\b', r'$X_L$'),
    (r'\bX_C\b', r'$X_C$'),
    (r'\bV_rms\b', r'$V_{rms}$'),
    (r'\bV_max\b', r'$V_{max}$'),
    (r'\bV_avg\b', r'$V_{avg}$'),
    (r'\bI_max\b', r'$I_{max}$'),
    (r'\bR_m\b', r'$R_m$'),
    (r'\bR_t\b', r'$R_t$'),
    (r'\bR_sh\b', r'$R_{sh}$'),
    (r'\bR_shunt\b', r'$R_{shunt}$'),
    (r'\bR_total\b', r'$R_{total}$'),
    (r'\bI_m\b', r'$I_m$'),
    (r'\bI_fsd\b', r'$I_{fsd}$'),
    (r'\bI_N\b', r'$I_N$'),
    (r'\bZ_N\b', r'$Z_N$'),
    (r'\bV_th\b', r'$V_{th}$'),
    (r'\bZ_th\b', r'$Z_{th}$'),
    (r'\bZ_load\b', r'$Z_{load}$'),
    (r'\bZ_eq\b', r'$Z_{eq}$'),
]

MATH_SEG = re.compile(r'(\$\$.*?\$\$|\$[^$\n]*\$)', re.S)

def tolatex(s):
    parts = MATH_SEG.split(s)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:          # inside an existing math segment — untouched
            out.append(p)
            continue
        for pat, rep in TOKENS:
            p = re.sub(pat, rep, p)
        out.append(p)
    return "".join(out)

def normalize_solution(sol):
    s = sol.strip()
    if s.startswith("### Step-by-Step Derivation & Solution"):
        body = s[len(UMBRELLA):].lstrip("\n")
    else:
        body = s
    # convert '### Step N: ...' heading lines to bold '**Step N: ...**'
    body = re.sub(r"(?m)^### (Step \d+:[^\n]*)$", r"**\1**", body)
    # blank line after each bold step line for clean rendering
    body = re.sub(r"(?m)^(\*\*Step \d+:.*?\*\*)\n(?!\n)", r"\1\n\n", body)
    return UMBRELLA + "\n\n" + body

QUESTIONS = []
for q in QUESTIONS_A + QUESTIONS_B:
    q = dict(q)
    q["solution"] = tolatex(normalize_solution(q["solution"]))
    q["question"] = tolatex(q["question"])
    q["short"] = tolatex(q["short"])
    q["options"] = [tolatex(o) for o in q["options"]]
    QUESTIONS.append(q)

TOPICS_OUT = []
for t in TOPICS:
    t = dict(t)
    t["summaryNotes"] = tolatex(t["summaryNotes"])
    TOPICS_OUT.append(t)

# validate structure
errors = []
seen = set()
counters = {}
for q in QUESTIONS:
    if q["correct"] < 0 or q["correct"] >= len(q["options"]):
        errors.append(f"{q['topicId']}: bad correct index")
    if len(q["options"]) < 4:
        errors.append(f"{q['topicId']}: too few options")
    if q["kind"] not in ("calc", "theory"):
        errors.append(f"{q['topicId']}: bad kind")
    if q["kind"] == "calc" and "$$" not in q["solution"]:
        errors.append(f"{q['topicId']}: calc solution missing $$ display math")
    if "$" not in q["solution"]:
        errors.append(f"{q['topicId']}: solution missing LaTeX math")
    if not q["solution"].startswith(UMBRELLA):
        errors.append(f"{q['topicId']}: missing umbrella header")
    if not re.search(r"\*\*Step 1:", q["solution"]):
        errors.append(f"{q['topicId']}: missing bold Step 1 heading")
    for banned in ["simplifying yields", "similarly", "by inspection", "it follows that"]:
        if banned in q["solution"] + " " + q["short"]:
            errors.append(f"{q['topicId']}: banned phrase '{banned}'")
    # no legacy programming notation in PLAIN text (outside $...$ math)
    for field in ("question", "short"):
        plain = MATH_SEG.sub(" ", q[field])
        if re.search(r'\b(?:X_L|X_C|V_rms|V_max|V_avg|I_max|R_m|R_t|R_sh|I_m|I_fsd|R_total|V_th|Z_th|Z_load|Z_eq)\b', plain):
            errors.append(f"{q['topicId']}: legacy token in {field}")
    for o in q["options"]:
        plain = MATH_SEG.sub(" ", o)
        if re.search(r'\b(?:X_L|X_C|V_rms|V_max|V_avg|I_max|R_m|R_t|R_sh|I_m|I_fsd|R_total|V_th|Z_th|Z_load|Z_eq)\b', plain):
            errors.append(f"{q['topicId']}: legacy token in options")
    counters[q["topicId"]] = counters.get(q["topicId"], 0) + 1
    q["id"] = f"eee_{q['topicId'].replace('eee-','')}_{counters[q['topicId']]:02d}"
    if q["id"] in seen:
        errors.append(f"duplicate id {q['id']}")
    seen.add(q["id"])

if errors:
    print("ERRORS:")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

calc_n = sum(1 for q in QUESTIONS if q["kind"] == "calc")
theory_n = sum(1 for q in QUESTIONS if q["kind"] == "theory")
print(f"TOTAL: {len(QUESTIONS)} | calc: {calc_n} | theory: {theory_n}")
for t in TOPICS_OUT:
    print(" ", t["id"], "->", counters.get(t["id"], 0))

json.dump({"topics": TOPICS_OUT, "questions": QUESTIONS},
          open(".eee202_out.json", "w"), ensure_ascii=False, indent=2)
print("emitted .eee202_out.json")
