#!/usr/bin/env python3
"""Validate downstream claim boundaries and reject forbidden inference requests.

This is a deterministic *semantic* guard over an explicitly curated vocabulary.
It neither verifies a zero-knowledge proof nor establishes upstream authority.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("docs/implementation-guide/conformance")
DATA = BASE / "proof-claim-boundaries.json"
SCHEMA = BASE / "schemas/proof-claim-boundaries.schema.json"
PROMOTION = BASE / "evidence-promotion-gates.json"


class BoundaryError(ValueError):
    """Invalid or unsupported claim-boundary contract."""


def load(root: Path = ROOT) -> dict:
    model = json.loads((root / DATA).read_text(encoding="utf-8"))
    schema = json.loads((root / SCHEMA).read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(model)
    promotion = json.loads((root / PROMOTION).read_text(encoding="utf-8"))
    known = {row["record"] for row in promotion["current_evidence"]}
    seen = set()
    for record in model["records"]:
        rid = record["record"]
        if rid in seen or rid not in known:
            raise BoundaryError(f"duplicate or unknown canonical record: {rid}")
        seen.add(rid)
        establishes = set(record["establishes"])
        forbidden = [v["claim"] for v in record["does_not_establish"]]
        if len(forbidden) != len(set(forbidden)) or establishes.intersection(forbidden):
            raise BoundaryError(f"{rid}: ambiguous or contradictory claim classification")
    return model


def decide(model: dict, record: str, established: str, requested: str) -> str:
    """Return ALLOWED, REJECTED, or INDETERMINATE; never infer extra claims."""
    rows = [r for r in model["records"] if r["record"] == record]
    if len(rows) != 1:
        return "INDETERMINATE"
    row = rows[0]
    if established not in row["establishes"]:
        return "INDETERMINATE"
    if requested in {entry["claim"] for entry in row["does_not_establish"]}:
        return "REJECTED"
    if requested == established:
        return "ALLOWED"
    return "INDETERMINATE"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", help="canonical record ID, e.g. 010")
    parser.add_argument("--established", help="exact demonstrated semantic claim identifier")
    parser.add_argument("--requested", help="claim a consumer seeks to infer")
    args = parser.parse_args(argv)
    try:
        model = load()
        specified = (args.record, args.established, args.requested)
        if any(specified) and not all(specified):
            raise BoundaryError("all of --record, --established and --requested are required together")
        if all(specified):
            outcome = decide(model, *specified)
            print(json.dumps({"record": args.record, "established": args.established,
                              "requested": args.requested, "outcome": outcome}, sort_keys=True))
            return 0 if outcome == "ALLOWED" else 1
        for row in model["records"]:
            for source in row["establishes"]:
                for forbidden in row["does_not_establish"]:
                    if decide(model, row["record"], source, forbidden["claim"]) != "REJECTED":
                        raise BoundaryError(f"{row['record']}: failed negative inference: {forbidden['claim']}")
        print(f"Proof claim boundaries valid: {len(model['records'])} records; all negative inferences rejected")
        return 0
    except (BoundaryError, OSError, KeyError, ValueError, jsonschema.ValidationError) as exc:
        print(f"Proof claim boundary validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
