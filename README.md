# cc-prep

ISC2 Certified in Cybersecurity (CC) cram tool. A markdown study guide and ten daily HTML pages rendered in a parchment-themed solarpunk style, with a memory-palace elicitation framework and a hybrid local/static notes feature.

Exam date: 2026-05-30. The tool ships within the cram window.

## Quick start

```bash
# Render daily pages + corpus pages.
/Users/wjia/Projects/.venv-pdf/bin/python scripts/render_html.py

# Run the notes backend (optional, enables markdown writeback).
python3 scripts/notes_server.py
# Then open http://localhost:8765/
```

The render step is required. The backend is optional. See [Notes feature](#notes-feature) below.

## Layout

| Path | Purpose |
|---|---|
| `study_guide/CC_Study_Guide.md` | Five-domain study guide with memory-palace elicitation prompts |
| `study_guide/PRACTICE_EXAMS.md` | Mock 1 and Mock 2, ISC2-weighted |
| `study_guide/PRACTICE_EXAMS_2.md` | Mock 3 and Mock 4, weighted to weak domains |
| `study_guide/glossary.md` | Initialism reference |
| `study_guide/daily_notes.md` | Persistent store for user notes on day pages (30 delimiter blocks) |
| `study_guide/daily/*.html` | Rendered output (gitignored intermediate, but day pages tracked) |
| `study_guide/daily/style.css` | Solarpunk parchment styles |
| `study_guide/daily/notes.js` | Hybrid LS/BE notes client |
| `scripts/render_html.py` | Markdown-to-HTML renderer with anchor slugging and baked-in notes |
| `scripts/notes_server.py` | Stdlib HTTP server: static files + `/api/note` CRUD |
| `index.html` | Root-level redirect to `study_guide/daily/index.html` (for GH Pages) |

## Notes feature

Three modes:

**BE mode** — backend running on localhost. Add/edit/delete notes via the inline `+ note` affordance under each notable section. Writes go through `POST/PUT/DELETE /api/note` and land in `daily_notes.md` (day pages) or `CC_Study_Guide.md` (corpus pages) inside `<!-- user-notes:ANCHOR -->` delimiter blocks. The renderer reads those blocks at build time and bakes the notes back into the HTML.

**LS mode** — localhost without the backend running, or `file://` open. Notes save to your browser's localStorage. Same UI affordances; new notes appear immediately. They never reach `daily_notes.md` until you run the backend or use the export/import tools.

**Pages mode** — non-localhost deployment (e.g. GitHub Pages). Same as LS mode plus a read-only banner. Baked-in notes from `daily_notes.md` display correctly; new notes are LS-only.

### Anchor scheme

Day pages expose three anchors each: `day-N-focus`, `day-N-citations`, `day-N-links`. Notes attach to one of these. Corpus pages expose every heading id via `markdown-it-anchors` (current `notes.js` only wires day pages by default; corpus support is a future extension).

### Sync via export/import

The index page has an **Export** button (downloads all your browser-stored notes as a `daily_notes_export_YYYY-MM-DD.md` file in the same format as `daily_notes.md`) and an **Import** button (parses an export file and either POSTs to the backend or merges into localStorage, depending on mode).

Typical sync workflow:

1. Take notes on Pages from your phone (LS mode). Notes accumulate in browser storage.
2. Back at your laptop, open the index page on Pages, click **Export**, get the markdown file.
3. Run the backend locally, open `http://localhost:8765/`, click **Import**, select the file. Notes land in `daily_notes.md`. Commit that file.
4. Next render rebakes the notes into the HTML.

### Backend API contract

```
POST   /api/note            body: {anchor, text}    → {ok, note_id}
PUT    /api/note/<note_id>  body: {text}            → {ok, note_id}
DELETE /api/note/<note_id>                          → {ok, note_id}
```

Anchors must match `^[a-z0-9-]+$`. Note IDs are auto-assigned as `note-<anchor>-<N>` in source order. Text must be non-empty and ≤ 2000 characters.

## GitHub Pages

The root `index.html` is a meta-refresh redirect to `study_guide/daily/index.html`, so when Pages serves the repo from `/`, the entry point lands on the daily index. To enable Pages: repo settings → Pages → source = "Deploy from a branch" → main / `/`.

## Memory-palace pedagogy

The study guide is built around a five-room memory palace, one room per domain. Each Part-level blockquote is an elicitation prompt (you pick your own room and anchors) rather than a dictation. Appendix B lists fifteen high-frequency miss patterns; each gets its own per-section elicitation prompt. Appendix D.2 walks you through building your own palace, with a fallback pre-built palace for time pressure.

## Voice and style

Prose passes through the [deai](../deai/) voice scan as a gate. No em-dashes, no tricolon-after-colon, active voice, no theatrical mic-drop fragments. See `wei-voice` rules.
