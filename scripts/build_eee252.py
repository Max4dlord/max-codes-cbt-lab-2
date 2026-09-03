#!/usr/bin/env python3
"""Assemble EEE 252 (Analog Electronics & Circuit Analysis) bank.
Normalises solutions to the senior-examiner format and validates everything."""
import json
import re
from eee252_topics import TOPICS
from eee252_questions_a import QUESTIONS_A
from eee252_questions_b import QUESTIONS_B

UMBRELLA = "### Step-by-Step Derivation & Solution"

def normalize_solution(sol):
    s = sol.strip()
    if s.startswith(UMBRELLA):
        body = s[len(UMBRELLA):].lstrip("\n")
    else:
        body = s
    body = re.sub(r"(?m)^### (Step \d+:[^\n]*)$", r"**\1**", body)
    body = re.sub(r"(?m)^(\*\*Step \d+:.*?\*\*)\n(?!\n)", r"\1\n\n", body)
    return UMBRELLA + "\n\n" + body

QUESTIONS = []
for q in QUESTIONS_A + QUESTIONS_B:
    q = dict(q)
    q["solution"] = normalize_solution(q["solution"])
    QUESTIONS.append(q)

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
        errors.append(f"{q['topicId']}: calc missing $$ math")
    if "$" not in q["solution"]:
        errors.append(f"{q['topicId']}: missing LaTeX")
    if not q["solution"].startswith(UMBRELLA):
        errors.append(f"{q['topicId']}: missing umbrella")
    if not re.search(r"\*\*Step 1:", q["solution"]):
        errors.append(f"{q['topicId']}: missing Step 1")
    for banned in ["simplifying yields", "similarly", "by inspection", "it follows that"]:
        if banned in q["solution"] + " " + q["short"]:
            errors.append(f"{q['topicId']}: banned phrase '{banned}'")
    counters[q["topicId"]] = counters.get(q["topicId"], 0) + 1
    q["id"] = f"eee252_{q['topicId'].replace('eee252-','')}_{counters[q['topicId']]:02d}"
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
for t in TOPICS:
    print(" ", t["id"], "->", counters.get(t["id"], 0))

json.dump({"topics": TOPICS, "questions": QUESTIONS},
          open(".eee252_out.json", "w"), ensure_ascii=False, indent=2)
print("emitted .eee252_out.json")
