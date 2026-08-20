#!/usr/bin/env python3
from pathlib import Path
import re
import sys

R = Path(__file__).resolve().parents[1]
bad = []
patterns = [
    ("push to upstream remote", r"git\s+push\s+upstream(?:\s|$)"),
    ("GitHub operation targeting upstream variable", r"--repo[ =]+[\"\']?\$\{?UPSTREAM(?:_REPOSITORY)?\}?"),
    ("GitHub operation targeting upstream remote", r"--repo[ =]+[\"\']?upstream(?:[\"\']|\s|$)"),
]
for p in (R / ".github/workflows").glob("*.yml"):
    text = p.read_text()
    for label, pattern in patterns:
        if re.search(pattern, text, re.I):
            bad.append(f"{p.relative_to(R)}: {label}")

required = {
    "README.md": ["UPSTREAM_README.md", "maintained fork"],
    "UPSTREAM_README.md": ["DTG ZKP Task Force", "Mission", "Deliverable"],
    ".upstream/README.md": ["UPSTREAM_README.md", "checkpoint.json"],
    "docs/governance/upstream-synchronisation.md": ["UPSTREAM_README.md", "one-way"],
}
for rel, markers in required.items():
    p = R / rel
    if not p.exists():
        bad.append(f"{rel}: required upstream-governance file missing")
        continue
    text = p.read_text()
    for marker in markers:
        if marker.lower() not in text.lower():
            bad.append(f"{rel}: missing required marker '{marker}'")

monitor = (R / ".github/workflows/upstream-monitor.yml").read_text()
for marker in ("GITHUB_STEP_SUMMARY", "issues_enabled", "upstream-drift-evidence"):
    if marker not in monitor:
        bad.append(f".github/workflows/upstream-monitor.yml: missing resilient drift marker '{marker}'")
if "Issues are disabled" not in monitor or "exit 1" not in monitor:
    bad.append(".github/workflows/upstream-monitor.yml: disabled-Issues drift must fail visibly")

if bad:
    print("\n".join(bad), file=sys.stderr)
    sys.exit(1)
print("Upstream directionality and README preservation policy validated.")
