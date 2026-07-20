#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "implementation-guide"
errors = []
required = {"layout", "title", "nav_order"}

for path in sorted(GUIDE.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if not text.startswith("---\n"):
        errors.append(f"Missing front matter: {rel}")
        continue
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"Unclosed front matter: {rel}")
        continue
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    for key in sorted(required):
        if not fields.get(key):
            errors.append(f"Missing {key} in front matter: {rel}")
    if path != GUIDE / "README.md" and path.parent != GUIDE:
        section_index = GUIDE / path.relative_to(GUIDE).parts[0] / "README.md"
        if not section_index.exists():
            errors.append(f"Missing section landing page for {rel}: {section_index.relative_to(ROOT)}")
        if path.name != "README.md" and not fields.get("parent"):
            errors.append(f"Missing parent in front matter: {rel}")

if errors:
    print("Navigation validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"Navigation validation passed for {sum(1 for _ in GUIDE.rglob('*.md'))} rendered Markdown pages.")
