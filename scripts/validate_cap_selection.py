#!/usr/bin/env python3
"""Validate that CAP construction selection does not silently claim a frozen design."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "docs/implementation-guide/conformance"


def validate(selection: dict, baseline: dict) -> None:
    if selection.get("schema_version") != "1.0" or selection.get("record") != "010":
        raise ValueError("unsupported CAP selection contract")
    if selection.get("authority") != "downstream-experimental-selection-only":
        raise ValueError("selection cannot claim canonical upstream authority")
    if selection.get("upstream_commit") != baseline.get("upstream_commit"):
        raise ValueError("upstream authority baseline drift")
    if selection.get("decision") != "not_frozen":
        raise ValueError("frozen selection requires a distinct evidence-backed decision contract")
    req_ids = {r["id"] for r in baseline["requirements"]}
    candidates = selection.get("candidates", [])
    names = [c["id"] for c in candidates]
    if len(names) < 2 or len(names) != len(set(names)):
        raise ValueError("selection must compare distinct candidates")
    for c in candidates:
        if c.get("status") != "candidate" or not all(c.get(k) for k in ("benefit", "risks", "requires")):
            raise ValueError(f"unsubstantiated candidate: {c.get('id')}")
    gates = selection.get("gates", [])
    ids = [g["id"] for g in gates]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate selection gate")
    covered = set()
    for gate in gates:
        if not gate.get("check"):
            raise ValueError("empty gate check")
        group = gate["requirement"]
        if "-" not in group:
            raise ValueError("expected requirement range")
        start, end = group.split("-", 1)
        if start[0] != end[0] or not start[1:].isdigit() or not end[1:].isdigit():
            raise ValueError("invalid requirement range")
        covered.update(f"{start[0]}{n}" for n in range(int(start[1:]), int(end[1:]) + 1))
    if covered != req_ids:
        raise ValueError(f"requirement coverage mismatch: missing={sorted(req_ids-covered)} extra={sorted(covered-req_ids)}")
    if len(selection.get("selection_requirements", [])) < 4:
        raise ValueError("selection exit criteria incomplete")


def main() -> int:
    try:
        selection = json.loads((DIRECTORY / "cap-construction-selection.json").read_text())
        baseline = json.loads((DIRECTORY / "record-010-requirement-matrix.json").read_text())
        validate(selection, baseline)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"CAP selection gate failed: {exc}", file=sys.stderr)
        return 1
    print("CAP selection candidate and canonical-clause coverage gate passed (decision not frozen)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
