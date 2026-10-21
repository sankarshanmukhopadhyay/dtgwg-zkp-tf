#!/usr/bin/env python3
"""Conservatively compare two derived downstream evidence registry snapshots.

This is an invalidation/retest *impact calculator*, not an authoritative
execution ledger or a status-promoting conformance decision.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

from scripts.evidence_registry import EXPECTED, build

def impact(before: dict, after: dict) -> dict:
    if before.get("schema_version") != "1.0" or after.get("schema_version") != "1.0":
        raise ValueError("unsupported registry snapshot")
    if before.get("source") != after.get("source"):
        raise ValueError("cannot compare snapshots from unrelated source registries")
    def records(snapshot):
        rows = snapshot.get("records")
        if not isinstance(rows, list):
            raise ValueError("missing evidence records")
        result = {row["record"]: row for row in rows}
        if len(result) != len(rows) or set(result) != set(EXPECTED):
            raise ValueError("duplicate/missing/unreviewed record")
        return result
    old, new = records(before), records(after)
    old_authority, new_authority = before["authority"], after["authority"]
    if old_authority.get("downstream_only") is not True or new_authority.get("downstream_only") is not True:
        raise ValueError("cannot compare authoritative/lifecycle-promoting snapshots")
    drift = old_authority != new_authority
    source_drift = before.get("source_digest") != after.get("source_digest")
    result = []
    for record in EXPECTED:
        previous, current = old[record], new[record]
        triggers = []
        if drift:
            triggers.append("upstream_authority_changed")
        if source_drift:
            triggers.append("source_register_changed_requires_review")
        if previous.get("registration") != current.get("registration"):
            triggers.append("registration_changed")
        if previous.get("assets") != current.get("assets"):
            triggers.append("evidence_artifact_changed")
        for field in ("evidence_classes","downstream_labels","gaps"):
            if previous.get(field) != current.get(field):
                triggers.append(field+"_changed")
        if previous.get("producer_independence") != current.get("producer_independence"):
            triggers.append("independence_claim_changed")
        result.append({"record":record,
                       "retest_required":bool(triggers),
                       "triggers":triggers,
                       "status":"RETEST_REQUIRED" if triggers else "UNCHANGED"})
    return {"schema_version":"1.0","authority":"downstream-retest-impact-only",
            "upstream_drift":drift,"source_register_drift":source_drift,
            "records":result}


def main(argv=None) -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--before",type=Path,required=True,help="immutable prior registry projection JSON")
    parser.add_argument("--output",type=Path,help="write structured retest outcomes")
    args=parser.parse_args(argv)
    try:
        prior=json.loads(args.before.read_text(encoding="utf-8"))
        current=build()
        result=impact(prior,current)
        content=json.dumps(result,indent=2)+"\n"
        if args.output:
            args.output.write_text(content,encoding="utf-8")
        else:
            print(content,end="")
    except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as err:
        print(f"Evidence change-impact validation failed: {err}",file=sys.stderr)
        return 1
    return 0


if __name__=="__main__":
    raise SystemExit(main())
