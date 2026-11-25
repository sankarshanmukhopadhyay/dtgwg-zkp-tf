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
from scripts.reconcile_canonical_evidence import ALLOWED

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
    old_reconciliation = before.get("canonical_reconciliation")
    new_reconciliation = after.get("canonical_reconciliation")
    if not isinstance(new_reconciliation, dict) or not all(
            new_reconciliation.get(key) for key in
            ("source", "source_digest", "repository", "prior_revision", "current_revision")):
        raise ValueError("current snapshot missing canonical reconciliation")
    reconciliation_drift = old_reconciliation != new_reconciliation
    result = []
    for record in EXPECTED:
        previous, current = old[record], new[record]
        disposition = current.get("canonical_disposition")
        if disposition not in ALLOWED or not current.get("canonical_disposition_reason"):
            raise ValueError("current snapshot missing/invalid canonical disposition: " + record)
        triggers = []
        if old_reconciliation is None:
            triggers.append("prior_canonical_reconciliation_missing")
        elif reconciliation_drift:
            triggers.append("canonical_reconciliation_changed")
        if any(previous.get(field) != current.get(field)
               for field in ("canonical_disposition", "canonical_disposition_reason")):
            triggers.append("canonical_disposition_changed")
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
                       "canonical_disposition":disposition,
                       "canonical_disposition_reason":current["canonical_disposition_reason"],
                       "retest_required":bool(triggers),
                       "triggers":triggers,
                       "status":"RETEST_REQUIRED" if triggers else "UNCHANGED"})
    return {"schema_version":"1.0","authority":"downstream-retest-impact-only",
            "upstream_drift":drift,"source_register_drift":source_drift,
            "canonical_reconciliation_drift":reconciliation_drift,
            "canonical_reconciliation":new_reconciliation,
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
