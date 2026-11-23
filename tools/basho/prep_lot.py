# /// script
# dependencies = ["pykakasi"]
# ///
"""Prepare a translation lot: skip poems already in the database, fetch Ito Yo's commentary.

Usage: uv run prep_lot.py SEASONS START COUNT NAME   (e.g. summer 80 40 lot8)
Writes cache/NAME_input.json. The commentary is for understanding only: never copy it.
"""
import html
import json
import re
import subprocess
import sys
import time

from common import CACHE, DATA, ITO_BASE, USER_AGENT, matched
from dedupe import existing_readings, find_dup


def commentary(url: str, poem: str) -> str:
    raw = subprocess.run(["curl", "-s", "-m", "30", "-A", USER_AGENT, url], capture_output=True).stdout
    text = html.unescape(re.sub(r"<[^>]+>", "", raw.decode("shift_jis", errors="ignore")))
    dig = " ".join(l.strip() for l in text.splitlines() if l.strip() and "芭蕉db" not in l)
    k = dig.find(poem[:5])
    return dig[max(0, k - 150):][:700] if k >= 0 else dig[:700]


def main():
    seasons, start, count, name = sys.argv[1].split(","), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    links = json.load(open(DATA / "ito_links.json"))
    existing = existing_readings()
    out = []
    for pos, r in enumerate(matched(seasons)):
        if pos < start or len(out) >= count:
            continue
        d = find_dup([r["text"], r["ito"]], existing)
        if d:
            print("skip existing", pos, r["text"], d)
            continue
        href = links.get(r["ito"])
        url = ITO_BASE + href if href else None
        out.append(dict(pos=pos, text=r["text"], heading=r["heading"], ito=r["ito"], url=url,
                        comm=commentary(url, r["ito"]) if url else ""))
        if url:
            time.sleep(1.5)
    CACHE.mkdir(exist_ok=True)
    (CACHE / f"{name}_input.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    if out:
        print(len(out), "items; last pos", out[-1]["pos"], "; no commentary:", sum(1 for o in out if not o["comm"]))
    else:
        print("nothing left from position", start)


if __name__ == "__main__":
    main()
