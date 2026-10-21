#!/usr/bin/env python3
"""Generate/check a bounded, downstream evidence dashboard from existing evidence authority.

Do not conflate declared evidence classes with upstream lifecycle or external
interoperability. Missing rows are explicit; this is a projection, not a new registry.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("docs/implementation-guide/conformance")
SOURCE = BASE / "evidence-promotion-gates.json"
OUTPUT = BASE / "evidence-dashboard.md"
REQUIRED = ("003", "006", "007", "008", "009", "010", "021")
CLASSES = ("deterministic_semantic", "cryptographic_execution", "independent_reproduction",
           "cross_implementation", "privacy_adversarial", "currentness_status", "performance",
           "audit_security_review")


def render(data: dict) -> str:
    if data.get("schema_version") != "1.0" or "current_evidence" not in data:
        raise ValueError("unsupported evidence source")
    by_record = {}
    for row in data["current_evidence"]:
        key = row["record"]
        if key in by_record:
            raise ValueError(f"duplicate evidence row {key}")
        if not set(row["classes"]).issubset(set(CLASSES)):
            raise ValueError(f"unknown evidence class for {key}")
        by_record[key] = row
    extra = set(by_record) - set(REQUIRED)
    if extra:
        raise ValueError(f"new records require reviewed dashboard coverage: {sorted(extra)}")
    lines = [
        "---", "layout: default", 'title: "Evidence Dashboard"',
        'parent: "Conformance"', "nav_order: 55", "---", "",
        "# Downstream construction evidence dashboard", "",
        "**Source:** [Evidence-promotion gates](evidence-promotion-gates.json). This is a generated view, not upstream normative lifecycle or a claim of verified interoperability.",
        "", "Run `python3 scripts/generate_evidence_dashboard.py` after changing the evidence-promotion register; `--check` rejects stale output.", "",
        "| Canonical record | Declared evidence classes | Local labels | Gaps / next evidence |",
        "|---|---|---|---|",
    ]
    for key in REQUIRED:
        row = by_record.get(key)
        if row is None:
            lines.append(f"| {key} | no registered evidence | none | **missing evidence registration** |")
            continue
        cls = ", ".join(f"`{v}`" for v in row["classes"]) or "none"
        labels = ", ".join(f"`{v}`" for v in row["labels"]) or "none"
        gaps = ", ".join(row["gaps"]) or "no gaps declared; requires review"
        lines.append(f"| {key} | {cls} | {labels} | {gaps} |")
    lines.extend([
        "", "## Interpretation", "",
        "- These are declared evidence classes and downstream labels from the existing register; they are **not** independently substantiated by this projection.",
        "- A missing row is not a failed proof, nor a proof of absence: it is **unregistered**.",
        "- No downstream label advances canonical upstream `requested/specified/constructed/run/vetted/published` states.",
        "- The CAP component experiments remain insufficient for complete record-010 cryptographic execution or independent reproduction.",
        "- Missing upstream Credential/Registry authority or independent operator evidence cannot be silently upgraded by CI.",
        "",
    ])
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        source = json.loads((ROOT / SOURCE).read_text(encoding="utf-8"))
        expected = render(source)
        destination = ROOT / OUTPUT
        if args.check:
            if not destination.is_file() or destination.read_text(encoding="utf-8") != expected:
                raise ValueError("generated evidence dashboard is missing/stale")
        else:
            destination.write_text(expected, encoding="utf-8")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Evidence dashboard failed: {exc}", file=sys.stderr)
        return 1
    print("Evidence dashboard generated/verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
