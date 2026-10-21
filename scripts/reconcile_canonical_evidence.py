#!/usr/bin/env python3
"""Validate canonical change impact and produce conservative downstream evidence views.

This uses the pinned, reviewed upstream delta; it never treats a changed record
as current solely because an older local test once passed.
"""
import argparse
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "docs/implementation-guide/conformance/canonical-reconciliation.json"
GATES = ROOT / "docs/implementation-guide/conformance/evidence-promotion-gates.json"
ALLOWED = {"current", "retest_required", "stale", "superseded", "not_assessed"}

def fingerprint_assets(paths, *, root=ROOT):
    """Fingerprint only repository-contained regular files; never claim semantic freshness."""
    out = []
    for path in paths:
        if not isinstance(path, str) or not path or "\\x00" in path:
            raise ValueError("Invalid evidence asset path")
        candidate = root / path
        resolved_root = root.resolve()
        resolved = candidate.resolve()
        if not resolved.is_relative_to(resolved_root):
            raise ValueError("Evidence asset escapes repository: " + path)
        if not candidate.is_file():
            raise ValueError("Missing evidence asset: " + path)
        data = resolved.read_bytes()
        out.append({"path": path, "sha256": hashlib.sha256(data).hexdigest(),
                    "bytes": len(data)})
    return out

def reconcile(delta, gates, *, root=ROOT):
    canonical = delta["canonical"]
    if canonical["prior_revision"] == canonical["current_revision"]:
        raise ValueError("Current and prior canonical revisions are identical")
    if len(canonical["current_revision"]) != 40 or len(canonical["last_semantic_revision"]) != 40:
        raise ValueError("Canonical revision must be an immutable full commit SHA")
    records = {}
    for row in delta["record_impacts"]:
        rid = row["record"]
        if not (isinstance(rid, str) and len(rid) == 3 and rid.isdigit()):
            raise ValueError("Invalid canonical record ID")
        if rid in records:
            raise ValueError("Duplicate canonical record ID: " + rid)
        if row["disposition"] not in ALLOWED:
            raise ValueError("Unknown disposition: " + str(row["disposition"]))
        if not row.get("reason"):
            raise ValueError("Every impact disposition needs a rationale")
        records[rid] = row
    result = []
    seen_assets = set()
    for entry in gates["current_evidence"]:
        if entry["record"] in seen_assets:
            raise ValueError("Duplicate evidence inventory record: " + entry["record"])
        seen_assets.add(entry["record"])
        rid = entry["record"]
        row = records.get(rid)
        # A missing assessment is UNKNOWN, not current/PASS.
        state = row["disposition"] if row else "not_assessed"
        result.append({"record":rid, "state":state, "evidence_assets":entry["assets"],
                       "prior_labels":entry["labels"],
                       "asset_fingerprints":fingerprint_assets(entry["assets"], root=root),
                       "note":row["reason"] if row else "No canonical delta assessment exists."})
    for rid, row in records.items():
        if rid not in {e["record"] for e in gates["current_evidence"]}:
            result.append({"record":rid, "state":row["disposition"], "evidence_assets":[],
                           "prior_labels":[], "asset_fingerprints":[], "note":row["reason"]})
    return {"canonical_revision":canonical["current_revision"],
            "prior_revision":canonical["prior_revision"],
            "assessments":sorted(result, key=lambda x:x["record"])}

def markdown(report):
    lines = ["# Canonical ZKP evidence reconciliation", "",
             "Canonical revision: `" + report["canonical_revision"] + "`", "",
             "| Record | Disposition | Prior evidence assets |", "|---|---|---|"]
    for row in report["assessments"]:
        lines.append("| " + row["record"] + " | " + row["state"] + " | " +
                     str(len(row["evidence_assets"])) + " |")
    lines += ["", "These dispositions are conservative; they do not assert tests were rerun.",
              "Existing upstream lifecycle and downstream labels are not promoted by this report.", ""]
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", type=Path)
    args = ap.parse_args()
    report = reconcile(json.loads(DELTA.read_text()), json.loads(GATES.read_text()))
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "canonical-reconciliation.json").write_text(json.dumps(report, indent=2)+"\n")
        (args.output_dir / "canonical-reconciliation.md").write_text(markdown(report))
    print("Canonical evidence reconciliation valid:", len(report["assessments"]), "records")

if __name__ == "__main__":
    main()
