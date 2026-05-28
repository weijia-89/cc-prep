## ISC2 CC Mastery — Anki

Outputs in this folder:

- `ISC2_CC_Mastery.apkg`: Anki deck (import into Anki).
- `isc2_cc_mastery.tsv`: Source cards (tab-separated).
- `generate_deck.py`: Regeneration script.
- `requirements.txt`: Python dependency (only needed for `.apkg` generation).

### Import

- In Anki: **File → Import** → select `ISC2_CC_Mastery.apkg`.

### Regenerate the `.apkg`

```bash
python3 -m pip install --user -r "/Users/wjia/Projects/localonly/study/isc2-cc/anki/requirements.txt"
python3 "/Users/wjia/Projects/localonly/study/isc2-cc/anki/generate_deck.py"
```

### TSV format

Columns: `note_type`, `front`, `back`, `tags`

- `basic` | `cloze` | `scenario`
- Tags: `d1`–`d5`, `mnemonic`, `osi`, `ir`, `ports`, etc.

Synced from `ISC2_CC_Mastery.html` textbook modules (kalr spine).
