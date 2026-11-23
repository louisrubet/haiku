# haiku

An open database of haikus and their translations, served as a static JSON API at
<https://haiku.rubet.fr/>.

Each poem is kept in its original language with its translations, and every text carries its
rights: only public-domain originals and freely licensed translations are accepted.

## Repository layout

```
works/<id>.yaml      one original poem and its translations
people/<id>.yaml     authors and translators
schema/              JSON Schemas of both file kinds
scripts/build.py     validation and API generation
site/index.html      home page of haiku.rubet.fr
```

## Data model

A work holds:

- `id`: stable identifier, equal to the file name, never changed once published
- `status`: `draft`, `published` or `withdrawn` (withdraw, do not delete)
- `author`, `form` (hokku, haiku, senryu...), `season` and `kigo`, `tags`
- `original`: text in its own script, `romanization`, `composed`, `first_published`, `source_url`, `rights`
- `translations`: one per language, each with `text`, `translator`, `translated`, `source`, `notes`, `rights`

Languages are BCP 47 tags with a mandatory script subtag: `ja-Jpan`, `ja-Latn`, `fr-Latn`.
Verses are separated by line breaks, exactly as set by the author or the translator.

`rights` is either `status: public-domain` with a `basis`, or `status: licensed` with an SPDX
`license` (`CC0-1.0`, `CC-BY-4.0`, `CC-BY-SA-4.0`) and, for CC BY, the exact `attribution`.

A person has a `name`, `name_original`, `born`, `died` and `wikidata` id. The death date is required to
claim the public domain: the check applies the EU rule, death + 70 years.

Translations: a published translation by a named translator, in the public domain or freely licensed, comes
first, with its `source` and `source_url`. When none exists, a translation made by a language model is accepted,
credited to that model as translator (`people/<id>.yaml` with `kind: model`) and released under CC0.

## Validate and build

```shell
uv run scripts/build.py check            # validate works/ and people/
uv run scripts/build.py build            # validate, then generate public/
python3 -m http.server -d public 8000    # browse http://localhost:8000/
```

Validation covers the schemas, references to people, file names, Unicode NFC, the script of each
text against its language tag, public-domain dates and attribution requirements.
CI runs it on every pull request and publishes `public/` to GitHub Pages on every push to `main`.

## API

Base URL: `https://haiku.rubet.fr/v1/`. Read-only static files, UTF-8 JSON.

| Path | Content |
|---|---|
| `index.json` | number of published works, of translations per language, and per language and season |
| `works.json` | ids of the published works |
| `works/<id>.json` | a full work, people resolved |
| `<lang>/count.json` | `{"count": N}` for one language, e.g. `fr-Latn` |
| `<lang>/<NNNN>.json` | item `0000` to `N-1`: `text`, `author`, `translator`, `license`, `attribution`, `season`, `composed`, `id` |
| `<lang>/<season>/count.json`, `<lang>/<season>/<NNNN>.json` | the same, restricted to one season: `new-year`, `spring`, `summer`, `autumn`, `winter` |

Haiku of the day: `day mod N`, where `day` is the number of days since 1970-01-01 in the client's local
calendar (so it changes at local midnight) and `N` comes from `count.json`. Clients compute it themselves, so
the published files never expire.
A seasonal client picks the season of the local date itself (traditional Japanese or meteorological calendar,
northern hemisphere) and uses the files of that season. Works without a season are only in the full list.
Items are numbered in a shuffled order, stable between builds, that spreads each author over the cycle: following
days show unrelated haikus. Adding a work renumbers items and shifts the cycle, which is harmless for this use.

`v1` stays backward compatible; a breaking change gets `v2`.

## Contributing

Add `works/<id>.yaml` (and `people/<id>.yaml` if needed), run `uv run scripts/build.py check`,
open a pull request. Give the source of every text and the basis of its rights.

## Licenses

- Data (`works/`, `people/`) and the translations credited to a language model: CC0 1.0, see `LICENSE-DATA`.
- Other translations: the rights stated in their `rights`.
- Code (`scripts/`, `site/`, `schema/`): MIT, see `LICENSE`.
