#!/usr/bin/env python3
"""Splice pruned AEE bank + categories into src/data.js."""
import json, re, sys

SRC = "src/data.js"
text = open(SRC).read()

questions = json.load(open(".prune_out_questions.json"))
topics = json.load(open(".prune_out_topics.json"))
categories = json.load(open(".prune_out_categories.json"))

def find_bracket_end(s, start):
    """start points at '['; return index just after matching ']' (string-aware)."""
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
                entries.append(f'    "{key}": [\n' + ",\n".join(f'      "{o}"' for o in val) + "\n    ]")
            elif key == "correct":
                entries.append(f'    "{key}": {val}')
            else:
                entries.append(f'    "{key}": {json.dumps(val, ensure_ascii=False)}')
        lines.append(",\n".join(entries))
        lines.append("  }")
        out.append("\n".join(lines))
    return ",\n".join(out)

if __name__ == "__main__":
    # ---- 1) Replace topicMeta.aee202 ----
    i_tm = text.find("export const topicMeta = {")
    if i_tm < 0:
        sys.exit("topicMeta not found")
    i_a = text.find('"aee202": [', i_tm)
    if i_a < 0:
        sys.exit("topicMeta aee202 not found")
    open_b = text.find("[", i_a)
    end = find_bracket_end(text, open_b)
    new_topics = "[\n" + fmt_topics(topics) + "\n  ]"
    text = text[:open_b] + new_topics + text[end:]

    # ---- 2) Insert categoryMeta before questionBank ----
    i_qb = text.find("export const questionBank = {")
    if i_qb < 0:
        sys.exit("questionBank not found")
    cat_out = []
    for c in categories:
        c_lines = ["    {"]
        c_entries = [f'      "id": "{c["id"]}"', f'      "name": "{c["name"]}"']
        c_lines.append(",\n".join(c_entries))
        c_lines.append("    }")
        cat_out.append("\n".join(c_lines))
    cat_block = (
        "// ===========================================================================\n"
        "// MAIN CATEGORIES (per course) — questions are grouped under these.\n"
        "// A topic belongs to exactly one category (categoryId on the topic).\n"
        "// ===========================================================================\n"
        "export const categoryMeta = {\n"
        '  "aee202": [\n'
        + ",\n".join(cat_out) +
        "\n  ]\n"
        "}\n\n"
    )
    text = text[:i_qb] + cat_block + text[i_qb:]

    # ---- 3) Replace questionBank.aee202 ----
    i_qb = text.find("export const questionBank = {")
    i_a2 = text.find("aee202: [", i_qb)
    if i_a2 < 0:
        sys.exit("questionBank aee202 not found")
    open_b2 = text.find("[", i_a2)
    end2 = find_bracket_end(text, open_b2)
    new_qs = "[\n" + fmt_questions(questions) + "\n]"
    text = text[:open_b2] + new_qs + text[end2:]

    open(SRC, "w").write(text)
    print(f"spliced: {len(topics)} topics, {len(categories)} categories, {len(questions)} questions")
