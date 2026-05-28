# ISC2 CC — mastery prep (kalr)

**Cert:** ISC2 Certified in Cybersecurity (CC)  
**Cram site:** [`ISC2_CC_Mastery.html`](ISC2_CC_Mastery.html)  
**Archive (pre-kalr):** [`ISC2_CC_Mastery.archive.html`](ISC2_CC_Mastery.archive.html)

## Skill & template

| Resource | Path |
|----------|------|
| **kalr skill** | `toren/kalr.skill/SKILL.md` |
| **Pipeline** | `toren/kalr.skill/references/pipeline.md` |
| **Stage D IA** | `toren/kalr.skill/references/html-stage-d.md` |
| **Reference HTML** | `toren/applications/openmined/openmined_assessment_prep.html` |

## Artifacts (this folder)

| File | Purpose |
|------|---------|
| `ISC2_CC_Mastery.html` | Stage D textbook + flashcards + practice exam + calibration |
| `strategy_isc2_cc.md` | Domains, tracks, weak-area table |
| `isc2_cc_prep_prompts.md` | Piranesi packets (Stages A–C) forked from kalr templates |
| `piranesi/piranesi_validate_*.md` | Post-build validation prompts (Opus / GPT) |
| `ISC2_CC_Mastery.archive.html` | Legacy dark-theme app (1604 lines) — metrics-compatible |

## Waves (optional research refresh)

1. **Wave 0:** Read `strategy_isc2_cc.md`; paste any new ISC2 outline PDF into Evidence blocks.  
2. **Wave 1:** Run Master + P1–P3 in web chats (`isc2_cc_prep_prompts.md`).  
3. **Wave 2:** Adversarial ×3 → synthesizer ×3; pick best YAML ingest.  
4. **Wave 3:** Cursor Stage D — rebuild HTML sections from ingest; run `python3 ~/Projects/scripts/build_isc2_cc_kalr.py` if merging legacy body content.  
5. **Cram:** open HTML locally; use sidebar TOC + term tips.

## Metrics preservation

- **Key:** `localStorage['isc2cc-progress-v1']`  
- **Test:** open new HTML → header should show prior `cards mastered` / `quiz acc` if you studied in the archive app on the same origin (`file://` path must be consistent).

## Regenerate HTML

```bash
python3 ~/Projects/scripts/build_isc2_cc_kalr.py
```

Requires `ISC2_CC_Mastery.archive.html` as content source if sections are re-extracted.
