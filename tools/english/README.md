# English translations

Published translations first, LLM translations from the Japanese for the rest.

- `chamberlain.py`, `add_chamberlain.py`: Basil Hall Chamberlain, 1902 (public domain), checked on the scan.
  Kept as published, prose renderings included.
- `prep_en.py <season> [start] [count]`: published works of a season without English, with the
  original, the French translation and its context note.
- `batches/enN.py` (`EN`, optional `NOTES`) and `add_llm.py N`: add LLM translations credited to
  `claude-opus-5-5` under CC0. The French context note is reused unless the batch gives one.
  Checks the display font glyphs, 5 lines and 400 characters at most.

Run with `uv run --with pyyaml python tools/english/prep_en.py winter`.
