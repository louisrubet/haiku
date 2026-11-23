"""Add the English translations of Chamberlain 1902 (chamberlain.py) to the works of the database.

Usage: python3 add_chamberlain.py   (idempotent: works that already have en-Latn are left alone)
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from chamberlain import CH  # noqa: E402

WORKS = pathlib.Path(__file__).resolve().parents[2] / "works"
SOURCE = ("Basil Hall Chamberlain, “Bashō and the Japanese Poetical Epigram”, Transactions of the Asiatic "
          "Society of Japan, vol. 30, part 2, 1902")
SCAN = "https://archive.org/details/transactionsasi20japagoog/page/n{leaf}/mode/1up"
LEAF_OFFSET = 27  # scan leaf = printed page + 27

added = 0
for wid, (number, page, text) in CH.items():
    path = WORKS / f"{wid}.yaml"
    s = path.read_text()
    if "language: en-Latn" in s:
        continue
    where = f", p. {page}" + (f", no. {number}" if number else "") + "."
    block = "\n".join([
        "  - language: en-Latn",
        "    text: |-",
        *("      " + line for line in text.split("\n")),
        "    translator: basil-hall-chamberlain",
        '    translated: "1902"',
        "    source: " + json.dumps(SOURCE + where, ensure_ascii=False),
        "    source_url: " + SCAN.format(leaf=page + LEAF_OFFSET),
        "    rights:",
        "      status: public-domain",
        "      basis: Translator died in 1935.",
    ])
    path.write_text(s.rstrip("\n") + "\n" + block + "\n")
    added += 1
print(added, "English translations added")
