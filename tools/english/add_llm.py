"""Add LLM English translations from batches/enN.py (EN: dict id -> text; NOTES: optional id -> note).

Usage: python3 tools/english/add_llm.py N
Checks glyphs (display font range), at most 5 lines and 400 characters; skips works that already have English.
"""
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "basho"))
from common import glyph_ok  # noqa: E402  # pyright: ignore[reportMissingImports]

WORKS = HERE.parents[1] / "works"
n = sys.argv[1]
spec = importlib.util.spec_from_file_location("batch", HERE / "batches" / f"en{n}.py")
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
EN, NOTES = mod.EN, getattr(mod, "NOTES", {})

problems = []
for wid, text in EN.items():
    if not (WORKS / f"{wid}.yaml").exists():
        problems.append(f"{wid}: unknown work")
    if not glyph_ok(text) or not glyph_ok(NOTES.get(wid, "")):
        problems.append(f"{wid}: glyph outside the display font")
    if text.count("\n") > 4 or len(text) > 400:
        problems.append(f"{wid}: too long")
if set(NOTES) - set(EN):
    problems.append(f"notes for unknown ids: {set(NOTES) - set(EN)}")
if problems:
    sys.exit("\n".join(problems))

added = 0
for wid, text in EN.items():
    path = WORKS / f"{wid}.yaml"
    s = path.read_text()
    if "language: en-Latn" in s:
        print("skip (already English):", wid)
        continue
    lines = ["  - language: en-Latn", "    text: |-", *("      " + l for l in text.split("\n")),
             '    translator: "claude-opus-5-5"', '    translated: "2026"']
    # The context note of the French translation applies to the poem: reuse it unless the batch gives one.
    fr_note = re.search(r"^    notes: (.*)$", s, re.M)
    if wid in NOTES:
        lines.append(f"    notes: {json.dumps(NOTES[wid], ensure_ascii=False)}")
    elif fr_note:
        lines.append(f"    notes: {fr_note.group(1)}")
    lines += ["    rights:", "      status: licensed", "      license: CC0-1.0",
              '      basis: "Machine translation by Claude Opus 5.5 for this database, released under CC0."']
    path.write_text(s.rstrip("\n") + "\n" + "\n".join(lines) + "\n")
    added += 1
print(added, "English translations added")
