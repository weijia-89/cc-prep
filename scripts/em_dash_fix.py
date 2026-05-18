#!/usr/bin/env python3
"""Replace em-dashes ( - ) with hyphen-space ( - ) in CC-prep files."""
import pathlib, sys

ROOT = pathlib.Path("/Users/wjia/Projects/cc-prep")
patterns = ["**/*.md", "**/*.html", "**/*.py", "**/*.css", "**/*.txt"]
exclude_dirs = {"sources"}  # NIST sources may have legitimate en-dashes; leave alone

total = 0
files_changed = 0
for pat in patterns:
    for f in ROOT.glob(pat):
        if any(d in f.parts for d in exclude_dirs):
            continue
        try:
            t = f.read_text()
        except Exception:
            continue
        c = t.count(" - ")
        if c:
            t = t.replace(" - ", " - ")
            t = t.replace(" - ", " - ").replace(" - ", " - ").replace(" - ", " - ")
            f.write_text(t)
            total += c
            files_changed += 1
            print(f"{f.relative_to(ROOT)}: {c} replaced")

print(f"\nTotal: {total} em-dashes in {files_changed} files")
