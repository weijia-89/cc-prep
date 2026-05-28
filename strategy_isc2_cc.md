# ISC2 Certified in Cybersecurity (CC) — Study Strategy

**Exam target:** 2026-05-30 [operator-confirmed in legacy app header]  
**Deliverable:** `ISC2_CC_Mastery.html` (kalr Stage D) + Piranesi waves in `isc2_cc_prep_prompts.md`  
**Canonical skill:** `toren/kalr.skill/SKILL.md`

---

## Exam context [verified public]

Source: [ISC2 CC certification page](https://www.isc2.org/certifications/cc) (fetched 2026-05-27).

| Domain | Weight | Notes |
|--------|--------|--------|
| 1. Security Principles | 26% | CIA, risk, governance, ethics |
| 2. Business Continuity (BC), Disaster Recovery (DR) & Incident Response | 10% | RTO/RPO, IR phases |
| 3. Access Controls Concepts | 22% | RBAC, ABAC, MAC, DAC, IAM |
| 4. Network Security | 24% | Largest weight; operator weak area in legacy tracker |
| 5. Security Operations | 18% | Crypto, logging, awareness, sanitization |

- **Entry-level:** no experience required [verified public].  
- **Outline change:** effective **2026-09-01** ISC2 may use a new exam outline — re-check isc2.org before a later sit [verified public notice on CC page].  
- **Format:** [TBD] item count, CAT vs linear, time limit — confirm in official candidate guide / Pearson scheduling email.

---

## Weak areas (operator placeholders)

| Domain | Legacy tracker | Target | Notes |
|--------|----------------|--------|--------|
| D4 Network | ~55% | ≥78% | Highest expected-point lift |
| D2 BC/DR/IR | ~60% | ≥82% | Build while holding D4 retrieval |
| D3 Access | ~75% | ≥88% | [TBD] refresh after practice exams |
| D5 Sec Ops | ~75% | ≥88% | [TBD] |
| D1 Principles | ~87% | maintain | Warm retrieval only |

Update rows after each full practice exam export from Calibration tab / JSON export.

---

## Study tracks

### 48-hour cram

| Block | Hours | Activity |
|-------|-------|----------|
| 0–8h | 4h | D4 textbook + diagram trace + 20 D4 flashcards |
| 8–16h | 4h | D2 textbook + mixed D4/D2 cards |
| 16–24h | 3h | D3/D5 weak glossary + 30 mixed cards |
| 24–36h | 4h | Two timed practice exam modes (weak + full) |
| 36–44h | 3h | Calibration review — high-confidence misses only |
| 44–48h | — | Sleep, logistics; cards only |

### 2-week plan

| Week | Focus | Exit criteria |
|------|--------|----------------|
| 1 | D4 schema → D2 → D3 | D4 quiz acc ≥70%; D2 ≥75% |
| 2 | D5 + full sims + taper | Two full practice sessions; no conf≥3 misses on D4 |

Day-by-day detail lives in the HTML **Start Here** section.

---

## Metrics & progress

| Metric | UI | Storage |
|--------|-----|---------|
| Cards mastered | `#cmast` / `#ctot` | `prog.cards[id].conf >= 3` |
| Quiz accuracy | `#qacc` | `prog.exam[*].correct` |
| Calibration | `#ccal` | accuracy when `conf === 4` |
| Export | header button | `isc2cc-progress.json` |

**Do not reset** `localStorage` key `isc2cc-progress-v1` when opening the kalr rebuild.

---

## Pipeline (kalr)

1. Optional Piranesi producers (`isc2_cc_prep_prompts.md`) for domain deep-dives.  
2. Stage C ingest ≤1200 tokens if merging external research.  
3. Stage D HTML refresh when outline or weak areas change.  
4. **deai** pass on new narrative blocks before sharing externally.
