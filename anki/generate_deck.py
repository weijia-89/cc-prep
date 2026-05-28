#!/usr/bin/env python3

from __future__ import annotations

import csv
import hashlib
import os
from dataclasses import dataclass
from pathlib import Path

import genanki


ROOT = Path(__file__).resolve().parent
TSV_PATH = ROOT / "isc2_cc_mastery.tsv"
OUT_APKG = ROOT / "ISC2_CC_Mastery.apkg"


@dataclass(frozen=True)
class CardRow:
    note_type: str
    front: str
    back: str
    tags: list[str]


def _stable_int_id(s: str) -> int:
    # genanki IDs must be int; keep stable across runs.
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()[:15]
    return int(h, 16)


def _read_tsv(path: Path) -> list[CardRow]:
    rows: list[CardRow] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, r in enumerate(reader, start=1):
            if not r:
                continue
            if len(r) != 4:
                raise SystemExit(f"Bad TSV row {i}: expected 4 columns, got {len(r)}")
            note_type, front, back, tags = (c.strip() for c in r)
            tag_list = [t for t in tags.split() if t]
            rows.append(CardRow(note_type=note_type, front=front, back=back, tags=tag_list))
    return rows


def main() -> None:
    if not TSV_PATH.exists():
        raise SystemExit(f"Missing TSV: {TSV_PATH}")

    deck_name = "ISC2 CC Mastery"
    deck_id = _stable_int_id(deck_name)

    model_basic = genanki.Model(
        model_id=_stable_int_id(deck_name + "::basic"),
        name="ISC2 Basic",
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Front}}",
                "afmt": "{{Front}}<hr id='answer'>{{Back}}",
            }
        ],
    )

    model_scenario = genanki.Model(
        model_id=_stable_int_id(deck_name + "::scenario"),
        name="ISC2 Scenario → Response",
        fields=[{"name": "Scenario"}, {"name": "Response"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Scenario}}",
                "afmt": "{{Scenario}}<hr id='answer'>{{Response}}",
            }
        ],
    )

    model_cloze = genanki.Model(
        model_id=_stable_int_id(deck_name + "::cloze"),
        name="ISC2 Cloze",
        fields=[{"name": "Text"}, {"name": "Extra"}],
        templates=[
            {
                "name": "Cloze",
                "qfmt": "{{cloze:Text}}",
                "afmt": "{{cloze:Text}}<hr id='answer'>{{Extra}}",
            }
        ],
        model_type=genanki.Model.CLOZE,
    )

    deck = genanki.Deck(deck_id=deck_id, name=deck_name)

    for row in _read_tsv(TSV_PATH):
        nt = row.note_type.lower()
        if nt == "basic":
            note = genanki.Note(model=model_basic, fields=[row.front, row.back], tags=row.tags)
        elif nt == "scenario":
            note = genanki.Note(model=model_scenario, fields=[row.front, row.back], tags=row.tags)
        elif nt == "cloze":
            note = genanki.Note(model=model_cloze, fields=[row.front, row.back], tags=row.tags)
        else:
            raise SystemExit(f"Unknown note_type: {row.note_type}")
        deck.add_note(note)

    pkg = genanki.Package(deck)
    pkg.write_to_file(str(OUT_APKG))

    print(f"Wrote {OUT_APKG}")
    print(f"Cards: {len(deck.notes)}")


if __name__ == "__main__":
    # Avoid genanki warning about local timezone env on some systems.
    os.environ.setdefault("TZ", "UTC")
    main()

