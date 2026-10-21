#!/usr/bin/env python3
"""Validate source-reviewed canonical clause correspondence without promoting evidence."""
import json
from pathlib import Path
from reconcile_canonical_evidence import ROOT, DELTA, fingerprint_assets

MAPPING = ROOT / "docs/implementation-guide/conformance/canonical-correspondence-003-006.json"
ALLOWED = {"semantic_adapter", "policy_layer", "uncovered"}

def validate(mapping, delta, *, root=ROOT):
    if mapping.get("canonical_revision") != delta["canonical"]["current_revision"]:
        raise ValueError("Canonical correspondence revision differs from impact baseline")
    seen = set()
    for item in mapping["records"]:
        record = item["record"]
        if record in seen:
            raise ValueError("Duplicate correspondence record")
        seen.add(record)
        upstream_row = next((x for x in delta["record_impacts"] if x["record"] == record), None)
        if upstream_row is None or item["disposition"] != upstream_row["disposition"]:
            raise ValueError("Correspondence disposition differs from reviewed impact baseline: " + record)
        if item["disposition"] == "current":
            raise ValueError("Clause mapping does not establish current evidence")
        if item["canonical_path"] != "conformance/records/" + record + ".json":
            raise ValueError("Canonical record path does not match ID")
        sha = item["canonical_blob_sha"]
        if not (len(sha) == 40 and all(c in "0123456789abcdef" for c in sha)):
            raise ValueError("Invalid canonical blob pin")
        fingerprint_assets([item["downstream"]], root=root)
        if not item.get("gaps") or not item.get("mapping"):
            raise ValueError("Explicit coverage and gaps required")
        for clause in item["mapping"]:
            if clause["coverage"] not in ALLOWED:
                raise ValueError("Unsupported correspondence coverage")
            if not clause.get("canonical_field") or not clause.get("obligation"):
                raise ValueError("Missing clause grounding")
            if clause["coverage"] == "uncovered" and clause.get("downstream_test"):
                raise ValueError("Uncovered clause cannot claim downstream test")
            if clause["coverage"] != "uncovered" and not clause.get("downstream_test"):
                raise ValueError("Claimed coverage requires test identifier")
    return len(seen)

if __name__ == "__main__":
    print("Validated pinned canonical correspondence for",
          validate(json.loads(MAPPING.read_text()), json.loads(DELTA.read_text())),
          "records; no evidence promotion.")
