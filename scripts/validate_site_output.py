#!/usr/bin/env python3
"""Verify that every implementation-guide Markdown source became a themed HTML page."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "implementation-guide"
SITE = ROOT / "_site"
errors = []

for source in sorted(GUIDE.rglob("*.md")):
    rel = source.relative_to(ROOT)
    expected = SITE / rel.with_suffix(".html")
    if not expected.is_file():
        errors.append(f"Missing rendered page: {expected.relative_to(ROOT)} (source: {rel})")
        continue
    html = expected.read_text(encoding="utf-8", errors="replace")
    if "<html" not in html.lower() or "<main" not in html.lower():
        errors.append(f"Output is not a complete themed HTML page: {expected.relative_to(ROOT)}")

mermaid_sources = []
for source in GUIDE.rglob("*.md"):
    if "```mermaid" in source.read_text(encoding="utf-8"):
        mermaid_sources.append(source)
if mermaid_sources:
    init = SITE / "assets" / "js" / "mermaid-init.js"
    if not init.is_file():
        errors.append("Mermaid initialization asset was not published.")
    head_matches = list(SITE.rglob("*.html"))
    if head_matches and not any("mermaid.min.js" in p.read_text(encoding="utf-8", errors="ignore") for p in head_matches[:20]):
        errors.append("Rendered pages do not include the Mermaid runtime.")

if errors:
    print("Site-output validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"Site-output validation passed for {sum(1 for _ in GUIDE.rglob('*.md'))} implementation-guide pages.")
