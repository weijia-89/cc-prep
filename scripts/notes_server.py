#!/usr/bin/env python3
"""CC-prep notes backend. Single-file stdlib http.server.

Serves study_guide/daily/ statically AND accepts POST/PUT/DELETE /api/note
to write user notes into CC_Study_Guide.md or daily_notes.md as
attrs-plugin asides inside delimiter blocks.

Run from cc-prep root:
    python3 scripts/notes_server.py

Then open http://localhost:8765/index.html
"""
from __future__ import annotations
import json
import re
import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = ROOT / "study_guide" / "daily"
CC_STUDY_GUIDE = ROOT / "study_guide" / "CC_Study_Guide.md"
DAILY_NOTES = ROOT / "study_guide" / "daily_notes.md"
HOST = "127.0.0.1"
PORT = 8765

DAY_ANCHOR_RE = re.compile(r"^day-\d+-(focus|citations|links)$")
SAFE_ANCHOR_RE = re.compile(r"^[a-z0-9-]+$")
NOTE_ID_RE = re.compile(r"^note-[a-z0-9-]+-\d+$")

MAX_TEXT_LEN = 2000


def target_file_for_anchor(anchor: str) -> Path:
    """Return DAILY_NOTES for day-page anchors, CC_STUDY_GUIDE otherwise."""
    if DAY_ANCHOR_RE.match(anchor):
        return DAILY_NOTES
    return CC_STUDY_GUIDE


def escape_attrs_text(text: str) -> str:
    """Escape backslash, star, open-brace, close-brace so attrs-plugin parses
    our intent. Order matters: escape backslash first."""
    text = text.replace("\\", "\\\\")
    text = text.replace("*", "\\*")
    text = text.replace("{", "\\{")
    text = text.replace("}", "\\}")
    return text


def _open_close_patterns(anchor: str) -> tuple[str, str]:
    """Return the exact open and close delimiter comment strings for anchor."""
    open_pat = f"<!-- user-notes:{anchor} -->"
    close_pat = f"<!-- /user-notes:{anchor} -->"
    return open_pat, close_pat


def find_delimiter_block(md_path: Path, anchor: str) -> Optional[tuple[int, int]]:
    """Return (start_line_idx, end_line_idx) of delimiter block contents, or
    None if not found. start_line_idx is the line AFTER the open comment;
    end_line_idx is the line BEFORE the close comment. 0-indexed.

    Raises FileNotFoundError if md_path does not exist.
    """
    if not md_path.exists():
        raise FileNotFoundError(str(md_path))
    open_pat, close_pat = _open_close_patterns(anchor)
    lines = md_path.read_text(encoding="utf-8").splitlines()
    open_idx = None
    close_idx = None
    for i, line in enumerate(lines):
        if open_idx is None and line.strip() == open_pat:
            open_idx = i
            continue
        if open_idx is not None and line.strip() == close_pat:
            close_idx = i
            break
    if open_idx is None or close_idx is None:
        return None
    return (open_idx + 1, close_idx - 1)


NOTE_LINE_RE = re.compile(
    r"^\*(?P<text>.*)\*\{\.user-note\s+#(?P<id>note-[a-z0-9-]+-\d+)\}\s*$"
)


def _unescape_attrs_text(text: str) -> str:
    """Inverse of escape_attrs_text. Order matters: process escapes left to
    right via a single pass to avoid double-decoding."""
    out = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt in ("\\", "*", "{", "}"):
                out.append(nxt)
                i += 2
                continue
        out.append(ch)
        i += 1
    return "".join(out)


def list_notes_in_block(md_path: Path, anchor: str) -> list[tuple[str, str]]:
    """Return [(note_id, text), ...] of existing notes in the delimiter block.

    Each note in the block has shape:
        *<escaped text>*{.user-note #note-<anchor>-<n>}
    Order in the returned list matches order in the file. Returns empty list
    if block exists but contains no notes.

    Raises FileNotFoundError if md_path does not exist.
    Raises ValueError if delimiter block for anchor is missing.
    """
    block = find_delimiter_block(md_path, anchor)
    if block is None:
        raise ValueError(f"delimiter block missing: {anchor}")
    start, end = block
    if end < start:
        return []
    lines = md_path.read_text(encoding="utf-8").splitlines()
    notes: list[tuple[str, str]] = []
    for line in lines[start : end + 1]:
        m = NOTE_LINE_RE.match(line)
        if m:
            notes.append((m.group("id"), _unescape_attrs_text(m.group("text"))))
    return notes


def _read_lines(md_path: Path) -> list[str]:
    return md_path.read_text(encoding="utf-8").splitlines()


def _write_lines(md_path: Path, lines: list[str]) -> None:
    # Preserve trailing newline if original had one.
    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    md_path.write_text(text, encoding="utf-8")


def add_note(anchor: str, text: str) -> dict:
    """Add a new note. Auto-assign note_id = note-<anchor>-<N+1> where N is
    the count of existing notes in the block."""
    if not SAFE_ANCHOR_RE.match(anchor):
        return {"ok": False, "error": "invalid anchor"}
    if not text or not text.strip():
        return {"ok": False, "error": "empty text"}
    if len(text) > MAX_TEXT_LEN:
        return {"ok": False, "error": "text too long"}
    md_path = target_file_for_anchor(anchor)
    try:
        existing = list_notes_in_block(md_path, anchor)
    except FileNotFoundError:
        return {"ok": False, "error": "target file missing"}
    except ValueError:
        return {"ok": False, "error": "anchor not found"}
    n = len(existing) + 1
    note_id = f"note-{anchor}-{n}"
    escaped = escape_attrs_text(text.strip())
    new_line = f"*{escaped}*{{.user-note #{note_id}}}"
    # Insert before the close-delimiter line.
    block = find_delimiter_block(md_path, anchor)
    # block must exist (list_notes_in_block already verified). Recompute close
    # index from the raw file.
    open_pat, close_pat = _open_close_patterns(anchor)
    lines = _read_lines(md_path)
    insert_at = None
    for i, line in enumerate(lines):
        if line.strip() == close_pat:
            insert_at = i
            break
    if insert_at is None:
        return {"ok": False, "error": "anchor not found"}
    lines.insert(insert_at, new_line)
    _write_lines(md_path, lines)
    return {"ok": True, "note_id": note_id}


def _find_note_line(note_id: str) -> Optional[tuple[Path, int, str]]:
    """Search both canonical files for a note line matching note_id.
    Return (md_path, line_idx, line_text) or None."""
    for md_path in (CC_STUDY_GUIDE, DAILY_NOTES):
        if not md_path.exists():
            continue
        lines = _read_lines(md_path)
        for i, line in enumerate(lines):
            m = NOTE_LINE_RE.match(line)
            if m and m.group("id") == note_id:
                return (md_path, i, line)
    return None


def update_note(note_id: str, text: str) -> dict:
    """Update an existing note's text. Search both CC_STUDY_GUIDE and
    DAILY_NOTES for the note_id; replace its escaped text in place."""
    if not NOTE_ID_RE.match(note_id):
        return {"ok": False, "error": "invalid note_id"}
    if not text or not text.strip():
        return {"ok": False, "error": "empty text"}
    if len(text) > MAX_TEXT_LEN:
        return {"ok": False, "error": "text too long"}
    found = _find_note_line(note_id)
    if found is None:
        return {"ok": False, "error": "note_id not found"}
    md_path, idx, _ = found
    escaped = escape_attrs_text(text.strip())
    new_line = f"*{escaped}*{{.user-note #{note_id}}}"
    lines = _read_lines(md_path)
    lines[idx] = new_line
    _write_lines(md_path, lines)
    return {"ok": True, "note_id": note_id}


def delete_note(note_id: str) -> dict:
    """Delete a note by id. Removes the entire `*...*{.user-note #note-id}`
    line."""
    if not NOTE_ID_RE.match(note_id):
        return {"ok": False, "error": "invalid note_id"}
    found = _find_note_line(note_id)
    if found is None:
        return {"ok": False, "error": "note_id not found"}
    md_path, idx, _ = found
    lines = _read_lines(md_path)
    del lines[idx]
    _write_lines(md_path, lines)
    return {"ok": True, "note_id": note_id}


class NotesHandler(SimpleHTTPRequestHandler):
    """Static-file + /api/note POST/PUT/DELETE handler."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def _read_json_body(self) -> Optional[dict]:
        length_header = self.headers.get("Content-Length")
        if not length_header:
            return None
        try:
            length = int(length_header)
        except ValueError:
            return None
        if length <= 0:
            return None
        try:
            raw = self.rfile.read(length).decode("utf-8")
            return json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _status_for_error(self, error: str) -> int:
        if error in ("anchor not found", "note_id not found", "target file missing"):
            return 404
        return 400

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/note":
            self._send_json(404, {"ok": False, "error": "not found"})
            return
        body = self._read_json_body()
        if body is None or not isinstance(body, dict):
            self._send_json(400, {"ok": False, "error": "invalid JSON body"})
            return
        anchor = body.get("anchor")
        text = body.get("text")
        if not isinstance(anchor, str) or not isinstance(text, str):
            self._send_json(400, {"ok": False, "error": "anchor and text required"})
            return
        try:
            result = add_note(anchor, text)
        except Exception as exc:
            self._send_json(500, {"ok": False, "error": f"server error: {exc}"})
            return
        status = 200 if result.get("ok") else self._status_for_error(result.get("error", ""))
        self._send_json(status, result)

    def do_PUT(self) -> None:
        parsed = urlparse(self.path)
        if not parsed.path.startswith("/api/note/"):
            self._send_json(404, {"ok": False, "error": "not found"})
            return
        note_id = parsed.path[len("/api/note/") :]
        body = self._read_json_body()
        if body is None or not isinstance(body, dict):
            self._send_json(400, {"ok": False, "error": "invalid JSON body"})
            return
        text = body.get("text")
        if not isinstance(text, str):
            self._send_json(400, {"ok": False, "error": "text required"})
            return
        try:
            result = update_note(note_id, text)
        except Exception as exc:
            self._send_json(500, {"ok": False, "error": f"server error: {exc}"})
            return
        status = 200 if result.get("ok") else self._status_for_error(result.get("error", ""))
        self._send_json(status, result)

    def do_DELETE(self) -> None:
        parsed = urlparse(self.path)
        if not parsed.path.startswith("/api/note/"):
            self._send_json(404, {"ok": False, "error": "not found"})
            return
        note_id = parsed.path[len("/api/note/") :]
        try:
            result = delete_note(note_id)
        except Exception as exc:
            self._send_json(500, {"ok": False, "error": f"server error: {exc}"})
            return
        status = 200 if result.get("ok") else self._status_for_error(result.get("error", ""))
        self._send_json(status, result)

    def log_message(self, fmt: str, *args) -> None:
        """Stdout-only logging, no syslog."""
        sys.stdout.write("notes_server: " + (fmt % args) + "\n")


def main() -> int:
    server = ThreadingHTTPServer((HOST, PORT), NotesHandler)
    print(f"notes_server: listening on http://{HOST}:{PORT}")
    print(f"  static dir: {STATIC_DIR}")
    print(f"  corpus notes go to: CC_Study_Guide.md")
    print(f"  day-page notes go to: daily_notes.md")
    print(f"  stop: Ctrl-C")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nshutting down")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
