"""List published works without an English translation, for one season, with context for translating.

Usage: uv run --with pyyaml python tools/english/prep_en.py <season> [start] [count]
"""
import pathlib
import sys

import yaml

WORKS = pathlib.Path(__file__).resolve().parents[2] / "works"

season = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
count = int(sys.argv[3]) if len(sys.argv) > 3 else 40

todo = []
for path in sorted(WORKS.glob("*.yaml")):
    w = yaml.safe_load(path.read_text())
    if w.get("status") != "published" or w.get("season") != season:
        continue
    langs = {t["language"] for t in w.get("translations", [])}
    if "en-Latn" in langs:
        continue
    todo.append(w)

print(f"# {season}: {len(todo)} without English; showing {start}..{start + count - 1}")
for w in todo[start:start + count]:
    fr = next(t for t in w["translations"] if t["language"] == "fr-Latn")
    print(f"\n## {w['id']}  ({w['author']}, kigo {w.get('kigo', '-')})")
    print(w["original"]["text"])
    print("fr: " + fr["text"].replace("\n", " / ") + f"  [{fr['translator']}]")
    if fr.get("notes"):
        print("note: " + " ".join(str(fr["notes"]).split()))
