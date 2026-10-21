#!/usr/bin/env python3
"""Run-scoped downstream execution evidence with explicit dependency invalidation.

A successful execution establishes only the declared local command result. It does
not promote upstream lifecycle state or establish independent reproduction.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

from reconcile_canonical_evidence import ROOT, DELTA, fingerprint_assets

def _digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def _required(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Missing " + label)
    return value

def execute(*, record, command, dependencies, output, root=ROOT, operator, implementation):
    _required(record, "record")
    if not (len(record) == 3 and record.isdigit()):
        raise ValueError("Invalid record identifier")
    _required(operator, "operator")
    _required(implementation, "implementation")
    if not command or not all(isinstance(x, str) and x for x in command):
        raise ValueError("Command must be a nonempty argument vector")
    if not dependencies:
        raise ValueError("At least one named dependency is required")
    # Record provenance from a frozen pre-execution snapshot.
    delta = json.loads((root / DELTA.relative_to(ROOT)).read_text())
    row = next((r for r in delta["record_impacts"] if r["record"] == record), None)
    if row is None:
        raise ValueError("Canonical impact for record not assessed: " + record)
    paths = [str(DELTA.relative_to(ROOT))] + dependencies
    before = fingerprint_assets(paths, root=root)
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    completed = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    finished = datetime.datetime.now(datetime.timezone.utc).isoformat()
    after = fingerprint_assets(paths, root=root)
    drift = before != after
    canonical_revision = delta["canonical"]["current_revision"]
    report = {
        "schema_version": "1.0", "record": record, "canonical_revision": canonical_revision,
        "canonical_disposition": row["disposition"],
        "run": {"started_at": started, "finished_at": finished, "operator": operator,
                "implementation": implementation, "argv": command,
                "exit_code": completed.returncode, "dependency_drift_during_run": drift,
                "python": platform.python_version(), "platform": platform.platform()},
        "dependencies": before,
        "execution": {
            "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
            "stderr_sha256": hashlib.sha256(completed.stderr.encode()).hexdigest(),
            "stdout": completed.stdout[-4000:], "stderr": completed.stderr[-4000:]},
    }
    report["result"] = "execution_passed" if completed.returncode == 0 and not drift else "execution_failed"
    report["snapshot_sha256"] = _digest(report)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Refuse to silently overwrite a prior run.
    with output.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    return report

def verify(report, *, root=ROOT):
    if not isinstance(report, dict) or report.get("schema_version") != "1.0":
        return ["invalid evidence report"]
    expected = _digest({key: value for key, value in report.items() if key != "snapshot_sha256"})
    reasons = []
    if report.get("snapshot_sha256") != expected:
        reasons.append("report_digest_changed")
    try:
        delta = json.loads((root / DELTA.relative_to(ROOT)).read_text())
        if report["canonical_revision"] != delta["canonical"]["current_revision"]:
            reasons.append("canonical_revision_changed")
        row = next((r for r in delta["record_impacts"] if r["record"] == report["record"]), None)
        if row is None or row["disposition"] != report.get("canonical_disposition"):
            reasons.append("canonical_impact_changed")
        for old in report["dependencies"]:
            actual = fingerprint_assets([old["path"]], root=root)[0]
            if actual["sha256"] != old["sha256"] or actual["bytes"] != old["bytes"]:
                reasons.append("dependency_changed:" + old["path"])
    except (KeyError, ValueError, OSError, TypeError) as exc:
        reasons.append("unverifiable_dependency:" + str(exc))
    if report.get("result") != "execution_passed" or report.get("run", {}).get("exit_code") != 0:
        reasons.append("execution_not_passed")
    if report.get("run", {}).get("dependency_drift_during_run") is not False:
        reasons.append("dependency_drift_during_run")
    if report.get("canonical_disposition") != "current":
        reasons.append("canonical_evidence_not_current")
    return reasons

def main():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest="action", required=True)
    run = subs.add_parser("run")
    run.add_argument("--record", required=True)
    run.add_argument("--operator", required=True)
    run.add_argument("--implementation", required=True)
    run.add_argument("--dependency", action="append", required=True)
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("command", nargs=argparse.REMAINDER)
    check = subs.add_parser("verify")
    check.add_argument("report", type=Path)
    args = parser.parse_args()
    if args.action == "run":
        cmd = args.command[1:] if args.command and args.command[0] == "--" else args.command
        result = execute(record=args.record, operator=args.operator,
                         implementation=args.implementation, dependencies=args.dependency,
                         command=cmd, output=args.output)
        print("Recorded", result["result"], "at", args.output)
        return 0 if result["result"] == "execution_passed" else 1
    reasons = verify(json.loads(args.report.read_text()))
    print(json.dumps({"state": "current" if not reasons else "invalidated_or_unproven",
                      "reasons": reasons}, indent=2))
    return 0 if not reasons else 1

if __name__ == "__main__":
    sys.exit(main())
