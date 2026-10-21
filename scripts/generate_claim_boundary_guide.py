#!/usr/bin/env python3
"""Generate reader-facing non-implication documentation from the validated claim data."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from scripts.validate_proof_claim_boundaries import ROOT, load

TARGET = ROOT / "docs/implementation-guide/conformance/proof-claim-generated.md"


def render(model: dict) -> str:
    lines = [
        "---", "layout: default", 'title: "Proof Claim Matrix (Generated)"',
        'parent: "Conformance"', "nav_order: 58", "---", "",
        "# Proof-claim boundary matrix", "",
        "Generated from [the bounded claim catalogue](proof-claim-boundaries.json). The table expresses permitted **semantic inference given an independently established premise**, never proof validity or governance authorization.",
        "",
        "| Canonical record | Established premise | Forbidden stronger claim | Reason |",
        "|---|---|---|---|",
    ]
    for entry in sorted(model["records"], key=lambda x: x["record"]):
        for established in sorted(entry["establishes"]):
            for forbidden in sorted(entry["does_not_establish"], key=lambda x: x["claim"]):
                lines.append(
                    f"| {entry['record']} | `{established}` | `{forbidden['claim']}` | {forbidden['reason']} |"
                )
    lines.extend([
        "", "## Consumer contract", "",
        "- A positive semantic match does not authenticate an input or establish successful cryptographic verification.",
        "- Prohibited claims return `REJECTED`; unknown or unproven claims return `INDETERMINATE` rather than authorization.",
        "- No downstream assurance finding promotes an upstream construction lifecycle.",
        "- CAP record 010 remains a semantic/construction-feasibility track without an accepted end-to-end prover.",
        "", "Regenerate with `python3 -m scripts.generate_claim_boundary_guide`; validate with `--check`.", "",
    ])
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    args = p.parse_args(argv)
    try:
        content = render(load())
        if args.check:
            if not TARGET.is_file() or TARGET.read_text(encoding="utf-8") != content:
                raise ValueError("generated claim guide is missing or stale")
        else:
            TARGET.write_text(content, encoding="utf-8")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Claim guide error: {exc}", file=sys.stderr)
        return 1
    print("Generated claim guide verified" if args.check else "Generated claim guide written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
