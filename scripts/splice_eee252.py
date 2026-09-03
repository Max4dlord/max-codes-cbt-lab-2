#!/usr/bin/env python3
"""Splice EEE 252 into data.js: course entry, topicMeta.eee252 (with
summaryNotes — Part A), questionBank.eee252 (Part B solved past questions)."""
import json
import re

DATA = json.load(open(".eee252_out.json"))
TOPICS = DATA["topics"]
QUESTIONS = DATA["questions"]

COURSE = {
    "id": "eee252",
    "code": "EEE 252",
    "title": "Analog Electronics & Circuit Analysis",
    "blurb": "Diode circuits & I-V characteristics, rectification & power supplies, MOSFETs, BJTs, small-signal models and op-amps. Built to the senior-examiner standard: every past question solved step-by-step with zero skipping, full LaTeX mathematics, and per-option distractor analysis.",
    "accent": "#dc2626",
    "available": True,
}

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
        for key in ["id", "topicId", "kind", "question", "options", "correct", "short", "solution", "image"]:
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
            f'      "summaryNotes": {json.dumps(t["summaryNotes"], ensure_ascii=False)}',
        ]
        lines.append(",\n".join(entries))
        lines.append("    }")
        out.append("\n".join(lines))
    return ",\n".join(out)

def main():
    src = open("src/data.js").read()

    # ---- 0) make idempotent: strip any previous eee252 blocks ----
    def strip_array(anchor):
        nonlocal src
        while True:
            i = src.find(anchor)
            if i < 0:
                return
            open_b = src.find("[", i)
            end = find_bracket_end(src, open_b)
            j = i
            while j > 0 and src[j - 1] in " \n\t":
                j -= 1
            if j > 0 and src[j - 1] == ",":
                j -= 1
            src = src[:j] + src[end:]

    strip_array('"eee252": [')
    strip_array('eee252: [')

    # remove a previously inserted course object
    i_course = src.find('"id": "eee252"')
    if i_course >= 0:
        obj_start = src.rfind("{", 0, i_course)
        obj_end = src.find("}", i_course) + 1
        k = obj_end
        while k < len(src) and src[k] in " \n\t":
            k += 1
        if k < len(src) and src[k] == ",":
            obj_end = k + 1
        src = src[:obj_start] + src[obj_end:]

    # ---- 1) course entry before mee206 ----
    i_mee = src.find('"mee206"')
    if i_mee < 0:
        raise SystemExit("mee206 not found")
    obj_start = src.rfind("{", 0, i_mee)
    course_lines = ["  {"]
    entries = [
        f'    "id": "{COURSE["id"]}"',
        f'    "code": "{COURSE["code"]}"',
        f'    "title": "{COURSE["title"]}"',
        f'    "blurb": {json.dumps(COURSE["blurb"], ensure_ascii=False)}',
        f'    "accent": "{COURSE["accent"]}"',
        '    "available": true',
    ]
    course_lines.append(",\n".join(entries))
    course_lines.append("  },")
    block = "\n".join(course_lines) + "\n"
    src = src[:obj_start] + block + src[obj_start:]

    # ---- 2) topicMeta.eee252 (before closing brace of topicMeta) ----
    i_tm = src.find("export const topicMeta = {")
    i_close = src.find("\n}", i_tm)
    if i_close < 0:
        raise SystemExit("topicMeta close not found")
    topic_block = ',\n  "eee252": [\n' + fmt_topics(TOPICS) + "\n  ]\n"
    src = src[:i_close] + topic_block + src[i_close:]

    # ---- 3) questionBank.eee252 ----
    i_qb = src.find("export const questionBank = {")
    i_close2 = src.find("\n}", i_qb)
    if i_close2 < 0:
        raise SystemExit("questionBank close not found")
    q_block = ',\n  eee252: [\n' + fmt_questions(QUESTIONS) + "\n  ]\n"
    src = src[:i_close2] + q_block + src[i_close2:]

    open("src/data.js", "w").write(src)
    print(f"data.js: course + {len(TOPICS)} topics + {len(QUESTIONS)} questions")

if __name__ == "__main__":
    main()
