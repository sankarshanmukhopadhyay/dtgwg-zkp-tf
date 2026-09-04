#!/usr/bin/env python3
"""Validate normalized construction/profile evidence and anti-overclaim invariants."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/implementation-guide/conformance/construction-evidence-manifest.json"
SCHEMA = ROOT / "docs/implementation-guide/conformance/schemas/construction-evidence-manifest.schema.json"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(manifest)

    profile_ids: set[str] = set()
    for profile in manifest["profiles"]:
        profile_id = profile["profile_id"]
        if profile_id in profile_ids:
            raise SystemExit(f"duplicate construction evidence profile_id: {profile_id}")
        profile_ids.add(profile_id)

        for source in profile["provenance"]:
            if source.startswith(("http://", "https://")):
                continue
            if not (ROOT / source).exists():
                raise SystemExit(f"{profile_id}: missing provenance path: {source}")

        evidence_file = profile["execution"].get("evidence_file")
        if evidence_file and not (ROOT / evidence_file).exists():
            raise SystemExit(f"{profile_id}: missing evidence_file: {evidence_file}")

        interoperability = profile["interoperability"]
        if interoperability["state"] in {"verified", "complete"} and not interoperability["independent"]:
            raise SystemExit(
                f"{profile_id}: interoperability cannot be {interoperability['state']} without independent evidence"
            )

        if profile["evidence_state"] == "complete" and interoperability["state"] != "complete":
            raise SystemExit(
                f"{profile_id}: complete evidence requires complete interoperability evidence"
            )

    print(f"Construction evidence manifest valid: {len(profile_ids)} profiles; anti-overclaim invariants passed.")


if __name__ == "__main__":
    main()
