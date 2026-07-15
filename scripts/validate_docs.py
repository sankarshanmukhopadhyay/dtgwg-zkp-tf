#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "implementation-guide"
required = [
    GUIDE / "README.md",
    GUIDE / "adr" / "ADR-TEMPLATE.md",
    GUIDE / "scenarios" / "SCENARIO-TEMPLATE.md",
    GUIDE / "taxonomy" / "predicates.md",
    GUIDE / "conformance" / "README.md",
    GUIDE / "conformance" / "levels.md",
    GUIDE / "conformance" / "test-matrix.md",
    GUIDE / "guide" / "implementation-interoperability-guide.md",
    GUIDE / "editorial" / "STYLE-GUIDE.md",
    GUIDE / "appendices" / "ERROR-CATALOGUE.md",
    GUIDE / "architecture" / "11-operational-viewpoint.md",
]
errors = []
for path in required:
    if not path.exists():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")
for path in GUIDE.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    if "\t" in text:
        errors.append(f"Tab character found: {path.relative_to(ROOT)}")
    if text and not text.endswith("\n"):
        errors.append(f"Missing final newline: {path.relative_to(ROOT)}")
if errors:
    print("Documentation validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Documentation validation passed.")
