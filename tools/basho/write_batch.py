"""Write the works of a lot from batches/batchN.py, checked against the 1903 texts, then add its notes.

Usage: python3 write_batch.py batchN SEASONS [--force]   (e.g. batch8 summer)
Each B line: index|id|original verses with /|kigo|French verses with /
NOTES: optional dict id -> short English context note.
"""
import importlib
import json
import sys
import unicodedata

from common import TOOLS, WORKS, glyph_ok, key, matched

EXTRA = {"瘦": "痩", "拜": "拝", "緖": "緒", "數": "数", "雞": "鶏", "盜": "盗", "簑": "蓑", "賴": "頼", "奧": "奥", "燒": "焼"}

TEMPLATE = """id: {wid}
status: published
added: "{added}"
author: matsuo-basho
form: hokku
season: {season}
kigo: {kigo}
original:
  language: ja-Jpan
  text: |-
{ja}
  source_url: https://ja.wikisource.org/wiki/芭蕉俳句全集
  rights:
    status: public-domain
    basis: Author died in 1694.
translations:
  - language: fr-Latn
    text: |-
{fr}
    translator: claude-opus-5-5
    translated: "2026"
{notes}    rights:
      status: licensed
      license: CC0-1.0
      basis: Machine translation by Claude Opus 5.5 for this database, released under CC0.
"""


def main():
    name, seasons = sys.argv[1], sys.argv[2].split(",")
    sys.path.insert(0, str(TOOLS / "batches"))
    mod = importlib.import_module(name)
    rows = getattr(mod, name.upper().replace("BATCH", "B"))
    notes = getattr(mod, "NOTES", {})
    entries = matched(seasons)
    ids, problems, works = set(), [], []
    for row in rows.strip().split("\n"):
        idx, wid, ja, kigo, fr = row.split("|")
        r = entries[int(idx)]
        src = "".join(EXTRA[c] if c in EXTRA else c for c in r["text"]).replace("きり〴〵す", "きりぎりす")
        if key(ja.replace("/", "")) != key(src):
            problems.append(f"{idx} {wid}: {ja} != {src}")
        if wid in ids or (WORKS / f"{wid}.yaml").exists():
            problems.append(f"{idx} duplicate id {wid}")
        if not glyph_ok(fr) or not glyph_ok(notes.get(wid, "")):
            problems.append(f"{idx} glyphs: {fr}")
        if len(ja.split("/")) != 3 or len(fr.split("/")) != 3:
            problems.append(f"{idx} verse count")
        ids.add(wid)
        works.append((wid, r["season"], kigo, ja, fr))
    if set(notes) - ids:
        problems.append(f"notes for unknown ids: {set(notes) - ids}")
    if problems:
        print("\n".join(problems))
        if "--force" not in sys.argv:
            sys.exit(1)

    added = getattr(mod, "ADDED", None) or __import__("datetime").date.today().isoformat()
    ind = lambda t, n: "\n".join(" " * n + l for l in t.split("/"))
    for wid, season, kigo, ja, fr in works:
        note = f"    notes: {json.dumps(notes[wid], ensure_ascii=False)}\n" if wid in notes else ""
        s = TEMPLATE.format(wid=wid, added=added, season=season, kigo=kigo, ja=ind(ja, 4), fr=ind(fr, 6), notes=note)
        (WORKS / f"{wid}.yaml").write_text(unicodedata.normalize("NFC", s))
    print(len(works), "works written,", len(notes), "notes")


if __name__ == "__main__":
    main()
