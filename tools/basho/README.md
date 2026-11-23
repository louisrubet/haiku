# Bashō translation lots

Tools used to add Matsuo Bashō's hokku to the database, lot by lot, with machine translations credited to `claude-opus-5-5`.

## Sources

- `data/matched.json`: hokku of the 1903 collection 芭蕉俳句全集 on Japanese Wikisource (public domain), matched against Itō Yō's Bashō database at Yamanashi Prefectural University, with season and kigo heading. `dup: true` marks variants that are skipped.
- `data/ito_links.json`: poem -> commentary page in Itō Yō's database.

Itō Yō's commentary is fetched into `cache/` (not committed) and read to understand each poem: its allusions, its setting and the person it greets. Never copy its wording into the database.

## Workflow

```sh
cd tools/basho
uv run prep_lot.py summer 80 40 lot8      # skips poems already present, fetches commentary
# read cache/lot8_input.json, then write batches/batch8.py (B8 rows and NOTES)
python3 write_batch.py batch8 summer      # checks originals, ids, glyphs, verse count
uv run dedupe.py                           # spelling-insensitive duplicate check of the whole database
cd ../.. && uv run scripts/build.py check
```

Lot indexes are positions in `matched(seasons)`; batch1 used `new-year,winter`.

## Translation rules

- Read the commentary first; skip poems built on untranslatable puns, obscure titles, or a meaning that the commentary itself calls uncertain.
- Three verses, concise, no rhyme, no padding, no em dash, no final period. Only glyphs of the standby font (see `common.GLYPHS`).
- Add a short English note when an allusion, a place or a greeting context is needed to understand the poem.
- A published translation in the public domain (Revon) always wins over a machine translation.
