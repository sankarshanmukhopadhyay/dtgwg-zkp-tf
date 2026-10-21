#!/usr/bin/env python3
"""Validate local engineering dispositions against real, existing repository evidence.

A disposition is *not* a proof outcome. It prevents a documented local gap
from being silently reclassified as a completed or externally blocked task.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/implementation-guide/conformance/zkp-local-disposition.json"
REQUIRED = {32,54,67}
STATUSES = {"local_unmet","local_partial","externally_blocked","completed"}


def validate(data: dict, root: Path = ROOT) -> None:
    if data.get("schema_version") != "1.0":
        raise ValueError("unsupported disposition version")
    authority = data.get("authority", {})
    if authority.get("downstream_only") is not True or authority.get("control_issue") != 30:
        raise ValueError("upstream authority must remain externally controlled")
    if len(authority.get("canonical_revision","")) != 40:
        raise ValueError("canonical checkpoint must be pinned")
    release = data.get("release", {})
    if release.get("target") != "v0.7.0" or release.get("disposition") != "defer" or not release.get("reason"):
        raise ValueError("release gate must explicitly defer while criteria remain open")
    issues = data.get("issues", [])
    if {r.get("issue") for r in issues} != REQUIRED or len(issues) != len(REQUIRED):
        raise ValueError("issue disposition set incomplete/duplicated")
    for row in issues:
        issue, status = row["issue"], row["status"]
        if status not in STATUSES:
            raise ValueError(f"{issue}: unknown state")
        if status == "completed" and row.get("unmet"):
            raise ValueError(f"{issue}: cannot complete with unmet gates")
        if status == "externally_blocked" and not row.get("external_dependencies"):
            raise ValueError(f"{issue}: external blocker requires declared external authority")
        for field in ("statement","next_action"):
            if not row.get(field):
                raise ValueError(f"{issue}: missing {field}")
        if not row.get("unmet") and status in {"local_unmet","local_partial"}:
            raise ValueError(f"{issue}: incomplete status requires unmet gates")
        if not row.get("forbidden_claims"):
            raise ValueError(f"{issue}: mandatory non-claims absent")
        if len(row.get("evidence",[])) != len(set(row["evidence"])):
            raise ValueError(f"{issue}: duplicate evidence path")
        for path in row.get("evidence",[]):
            if not isinstance(path,str) or not path or path.startswith(("http:","https:","/")):
                raise ValueError(f"{issue}: invalid evidence path")
            resolved=(root/path).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                raise ValueError(f"{issue}: missing/unsafe evidence path: {path}")
    if any(row["status"] == "completed" for row in issues):
        raise ValueError("current tranche has no issue that satisfies all its acceptance gates")


def main() -> int:
    try:
        validate(json.loads(SOURCE.read_text(encoding="utf-8")))
    except (ValueError,KeyError,OSError,TypeError,json.JSONDecodeError) as error:
        print(f"ZKP disposition validation failed: {error}",file=sys.stderr)
        return 1
    print("ZKP tranche dispositions verified: 3 local issue gates, release deferred")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
