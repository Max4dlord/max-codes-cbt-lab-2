#!/usr/bin/env python3
"""Replace EEE 202 in data.js:
1. REPLACE topicMeta.eee202 (now with summaryNotes LaTeX notes)
2. REPLACE questionBank.eee202 (senior-examiner bank)
3. Remove the old plain-text EEE entries from TOPIC_DEEP_DIVE in StudyRunner
   (topic summaryNotes now serve as the study notes drawer)."""
import json
import re

DATA = json.load(open(".eee202_out.json"))
TOPICS = DATA["topics"]
QUESTIONS = DATA["questions"]

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

def replace_array(src, anchor, new_content):
    """Replace the array that follows `anchor` ('"eee202": [') with new_content."""
    i = src.find(anchor)
    if i < 0:
        raise SystemExit(f"anchor not found: {anchor}")
    open_b = src.find("[", i)
    end = find_bracket_end(src, open_b)
    return src[:open_b] + new_content + src[end:]

def main():
    # ---- 1) topicMeta.eee202 ----
    src = open("src/data.js").read()
    src = replace_array(src, '"eee202": [', "[\n" + fmt_topics(TOPICS) + "\n  ]")

    # ---- 2) questionBank.eee202 ----
    src = replace_array(src, "eee202: [", "[\n" + fmt_questions(QUESTIONS) + "\n]")

    open("src/data.js", "w").write(src)
    print(f"data.js: replaced topics ({len(TOPICS)}) + questions ({len(QUESTIONS)})")

    # ---- 3) StudyRunner: drop old EEE TOPIC_DEEP_DIVE entries ----
    sr = open("src/components/StudyRunner.jsx").read()
    before = sr
    sr = re.sub(r"\n  'eee-[a-z-]+': `.*?`,\n", "\n", sr, flags=re.S)
    removed = before.count("'eee-") - sr.count("'eee-")
    open("src/components/StudyRunner.jsx", "w").write(sr)
    print(f"StudyRunner: removed {removed} legacy EEE deep-dive entries")

if __name__ == "__main__":
    main()
