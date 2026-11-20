#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "jsonschema>=4.18"]
# ///
"""Validate the haiku database and generate the static JSON API.

    uv run scripts/build.py check            validate works/ and people/
    uv run scripts/build.py build [--out D]  validate, then write the API to D (default: public)
"""

from __future__ import annotations

import argparse
import datetime
import json
import shutil
import sys
import unicodedata
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
API_VERSION = "v1"
PUBLIC_DOMAIN_YEARS = 70  # EU rule: author's death + 70 years, counted from 1 January of the following year

# Letters allowed per script subtag. Punctuation, digits and spaces are always allowed.
SCRIPT_LETTER_PREFIXES = {
    "Latn": ("LATIN",),
    "Jpan": ("CJK", "HIRAGANA", "KATAKANA", "IDEOGRAPHIC"),
}


class Errors(list):
    def add(self, where: str, message: str) -> None:
        self.append(f"{where}: {message}")


def load_yaml_dir(directory: Path, errors: Errors) -> dict[str, tuple[Path, dict]]:
    entries: dict[str, tuple[Path, dict]] = {}
    for path in sorted(directory.glob("*.yaml")):
        rel = path.relative_to(ROOT)
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.add(str(rel), f"invalid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors.add(str(rel), "top level must be a mapping")
            continue
        entries[path.stem] = (rel, data)
    return entries


def validate_schema(entries, schema_file: str, errors: Errors) -> None:
    schema = json.loads((ROOT / "schema" / schema_file).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for stem, (rel, data) in entries.items():
        for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            location = "/".join(str(p) for p in err.path) or "(root)"
            errors.add(str(rel), f"{location}: {err.message}")
        if data.get("id") != stem:
            errors.add(str(rel), f"id {data.get('id')!r} must match the file name {stem!r}")


def year_of(value: str) -> int:
    return int(value.lstrip("~")[:4])


def check_text(where: str, text: str, language: str, errors: Errors) -> None:
    if unicodedata.normalize("NFC", text) != text:
        errors.add(where, "text must be Unicode NFC")
    lines = text.split("\n")
    if any(not line.strip() for line in lines):
        errors.add(where, "no empty verse allowed")
    if any(line != line.strip() for line in lines):
        errors.add(where, "no leading or trailing spaces in a verse")
    script = language.split("-")[1]
    prefixes = SCRIPT_LETTER_PREFIXES.get(script)
    if prefixes is None:
        errors.add(where, f"script {script} has no character check yet, add it to SCRIPT_LETTER_PREFIXES")
        return
    for char in text:
        if unicodedata.category(char).startswith("L") and not unicodedata.name(char, "").startswith(prefixes):
            errors.add(where, f"character {char!r} (U+{ord(char):04X}) is not {script} script")
            return


def check_public_domain(where: str, rights: dict, person: dict | None, errors: Errors) -> None:
    if rights.get("status") != "public-domain":
        return
    if person is None or person.get("kind") != "person" or not person.get("died"):
        errors.add(where, "public-domain needs a person with a known death date")
        return
    free_from = year_of(person["died"]) + PUBLIC_DOMAIN_YEARS + 1
    if datetime.date.today().year < free_from:
        errors.add(where, f"{person['name']} died in {person['died']}: public domain in the EU only from {free_from}")


def check_rights(where: str, rights: dict, errors: Errors) -> None:
    if rights.get("license", "").startswith("CC-BY") and not rights.get("attribution"):
        errors.add(where, f"{rights['license']} requires an attribution text")


def validate() -> tuple[dict, dict, Errors]:
    errors = Errors()
    people = load_yaml_dir(ROOT / "people", errors)
    works = load_yaml_dir(ROOT / "works", errors)
    validate_schema(people, "person.schema.json", errors)
    validate_schema(works, "work.schema.json", errors)
    if errors:  # cross checks assume schema-valid data
        return people, works, errors

    persons = {pid: data for pid, (_, data) in people.items()}
    for stem, (rel, work) in works.items():
        where = str(rel)
        author = persons.get(work["author"])
        if author is None:
            errors.add(where, f"unknown author {work['author']!r}")
        original = work["original"]
        check_text(f"{where}: original", original["text"], original["language"], errors)
        check_public_domain(f"{where}: original", original["rights"], author, errors)
        check_rights(f"{where}: original", original["rights"], errors)
        romanization = original.get("romanization")
        if romanization:
            check_text(f"{where}: romanization", romanization["text"], romanization["language"], errors)
            if romanization["text"].count("\n") != original["text"].count("\n"):
                errors.add(where, "romanization must have as many verses as the original")
        languages = set()
        for i, translation in enumerate(work["translations"]):
            twhere = f"{where}: translations/{i}"
            translator = persons.get(translation["translator"])
            if translator is None:
                errors.add(twhere, f"unknown translator {translation['translator']!r}")
            if translation["language"] == original["language"]:
                errors.add(twhere, "a translation must not be in the language of the original")
            check_text(twhere, translation["text"], translation["language"], errors)
            check_public_domain(twhere, translation["rights"], translator, errors)
            check_rights(twhere, translation["rights"], errors)
            languages.add(translation["language"])
        if len(languages) != len(work["translations"]):
            errors.add(where, "one translation per language at most")
    return persons, {stem: data for stem, (_, data) in works.items()}, errors


def person_summary(person: dict) -> dict:
    return {k: person[k] for k in ("id", "name", "name_original", "born", "died", "wikidata", "url") if k in person}


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")


def build(persons: dict, works: dict, out: Path) -> dict[str, int]:
    if out.exists():
        shutil.rmtree(out)
    api = out / API_VERSION
    published = sorted((w for w in works.values() if w["status"] == "published"), key=lambda w: w["id"])

    by_language: dict[str, list[dict]] = {}
    for work in published:
        author = persons[work["author"]]
        write_json(
            api / "works" / f"{work['id']}.json",
            {
                **{k: v for k, v in work.items() if k not in ("author", "translations")},
                "author": person_summary(author),
                "translations": [
                    {**t, "translator": person_summary(persons[t["translator"]])} for t in work["translations"]
                ],
            },
        )
        for t in work["translations"]:
            by_language.setdefault(t["language"], []).append(
                {
                    "id": work["id"],
                    "text": t["text"],
                    "author": author["name"],
                    "translator": persons[t["translator"]]["name"],
                    "license": t["rights"].get("license", "public-domain"),
                    **({"attribution": t["rights"]["attribution"]} if "attribution" in t["rights"] else {}),
                    "season": work["season"],
                    **({"composed": work["original"]["composed"]} if "composed" in work["original"] else {}),
                }
            )
    # Items are numbered per language in id order; a client picks one with (day-dependent value) mod count.
    for language, items in by_language.items():
        write_json(api / language / "count.json", {"count": len(items)})
        for index, item in enumerate(items):
            write_json(api / language / f"{index:04d}.json", item)

    counts = {language: len(items) for language, items in sorted(by_language.items())}
    write_json(api / "index.json", {"version": 1, "works": len(published), "languages": counts})
    write_json(api / "works.json", {"ids": [w["id"] for w in published]})
    shutil.copytree(ROOT / "schema", out / "schema")
    shutil.copy(ROOT / "site" / "index.html", out / "index.html")
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["check", "build"])
    parser.add_argument("--out", type=Path, default=ROOT / "public")
    args = parser.parse_args()

    persons, works, errors = validate()
    if errors:
        print(f"{len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    published = sum(w["status"] == "published" for w in works.values())
    print(f"OK: {len(works)} works ({published} published), {len(persons)} people")
    if args.command == "build":
        counts = build(persons, works, args.out)
        print(f"Built {args.out}: " + ", ".join(f"{lang} {n}" for lang, n in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
