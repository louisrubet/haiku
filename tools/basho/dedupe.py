# /// script
# dependencies = ["pykakasi"]
# ///
"""Spelling-insensitive duplicate detection: compare hiragana readings with a fuzzy ratio.

Run alone to list every pair of works in the database whose originals read alike.
"""
import difflib
import itertools
import re

import pykakasi

from common import WORKS, key

_k = pykakasi.kakasi()
# Historical kana spellings folded to a common form.
_FOLD = str.maketrans({"ゐ": "い", "ゑ": "え", "を": "お", "づ": "ず", "ぢ": "じ", "っ": "つ", "ゃ": "や", "ゅ": "ゆ", "ょ": "よ"})


def reading(s: str) -> str:
    h = "".join(x["hira"] for x in _k.convert(key(s))).translate(_FOLD)
    h = re.sub(r"(?<=.)[はひふへほ]", lambda m: "わいうえお"["はひふへほ".index(m.group())], h)
    return re.sub(r"[^ぁ-ゖ]", "", h)


def existing_readings():
    out = {}
    for p in WORKS.glob("*.yaml"):
        m = re.search(r"original:\n  language: ja-Jpan\n  text: \|-\n((?:    .*\n)+)", p.read_text())
        if m:
            out[p.stem] = reading(m.group(1).replace(" ", "").replace("\n", ""))
    return out


def find_dup(texts, existing, threshold=0.8):
    best = (0, None)
    for t in texts:
        r = reading(t)
        for wid, e in existing.items():
            q = difflib.SequenceMatcher(None, r, e).ratio()
            if q > best[0]:
                best = (q, wid)
    return best if best[0] >= threshold else None


if __name__ == "__main__":
    ex = existing_readings()
    n = 0
    for (a, ra), (b, rb) in itertools.combinations(ex.items(), 2):
        q = difflib.SequenceMatcher(None, ra, rb).ratio()
        if q >= 0.75:
            n += 1
            print(round(q, 2), a, b)
    print(len(ex), "works checked,", n, "suspected duplicates")
