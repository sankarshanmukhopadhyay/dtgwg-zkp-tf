#!/usr/bin/env python3
"""Derive machine-verifiable evidence asset inventory without promoting claims.

The existing evidence-promotion register owns downstream declarations. This
projection authenticates *local bytes*, retains unobserved facts as null, and
never manufactures operator independence, cryptographic outcomes or upstream
lifecycle. JSON is generated for consumers; --check is the CI gate.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

if __package__:
    from .reconcile_canonical_evidence import reconcile
else:
    from reconcile_canonical_evidence import reconcile

ROOT = Path(__file__).resolve().parents[1]
SRC = Path("docs/implementation-guide/conformance/evidence-promotion-gates.json")
RECONCILIATION = SRC.with_name("canonical-reconciliation.json")
SCHEMA_VERSION = "1.0"
EXPECTED = ("003", "006", "007", "008", "009", "010", "021")


class RegistryError(ValueError):
    """Cannot safely derive a downstream evidence inventory."""


def digest_local(root: Path, path: str) -> str:
    if not isinstance(path, str) or not path or "\\" in path or path.startswith(("/", "http:", "https:")):
        raise RegistryError(f"invalid local evidence path: {path!r}")
    origin = root.resolve()
    resolved = (origin / path).resolve()
    if not resolved.is_relative_to(origin) or not resolved.is_file():
        raise RegistryError(f"missing/outside evidence asset: {path}")
    return hashlib.sha256(resolved.read_bytes()).hexdigest()


def build(root: Path = ROOT) -> dict:
    raw = (root / SRC).read_bytes()
    source = json.loads(raw)
    if source.get("schema_version") != "1.0":
        raise RegistryError("unsupported evidence source schema")
    authority = source.get("authority", {})
    commit = authority.get("upstream_commit")
    if not isinstance(commit, str) or len(commit) != 40:
        raise RegistryError("missing immutable upstream semantic commit")
    classes = set(source.get("evidence_classes", {}))
    labels = set(source.get("downstream_labels", {}))
    result = {}
    for row in source.get("current_evidence", []):
        record = row["record"]
        if record in result or record not in EXPECTED:
            raise RegistryError(f"duplicate/unreviewed canonical record: {record}")
        if not set(row["classes"]) <= classes or not set(row["labels"]) <= labels:
            raise RegistryError(f"{record}: unsupported evidence label/class")
        assets = row.get("assets", [])
        if not isinstance(assets, list) or not assets or len(assets) != len(set(assets)):
            raise RegistryError(f"{record}: evidence asset list invalid")
        result[record] = {
            "record": record,
            "registration": "declared",
            "evidence_classes": row["classes"],
            "downstream_labels": row["labels"],
            "assets": [{"path": path, "sha256": digest_local(root, path)} for path in sorted(assets)],
            "gaps": row["gaps"],
            "producer_independence": "not_established",
            "observed_cryptographic_outcome": None,
            "reproduction_environment": None,
            "observation_time": None,
            "claim_boundary": "Declarations only; proof execution and external assurance require distinct attributable records.",
        }
    records = []
    for record in EXPECTED:
        if record in result:
            records.append(result[record])
        else:
            records.append({
                "record": record, "registration": "missing",
                "evidence_classes": [], "downstream_labels": [], "assets": [],
                "gaps": ["evidence_registration_missing"],
                "producer_independence": "not_established",
                "observed_cryptographic_outcome": None,
                "reproduction_environment": None,
                "observation_time": None,
                "claim_boundary": "No registered evidence, not a negative proof result.",
            })
    # The evidence register is a historical declaration, not a currentness decision.
    # Use the reviewed canonical-impact contract rather than deriving a second one.
    delta_raw = (root / RECONCILIATION).read_bytes()
    delta = json.loads(delta_raw)
    canonical = delta["canonical"]
    if (delta.get("schema_version") != "1.0"
            or canonical["repository"] != authority["upstream_repository"]
            or canonical["prior_revision"] != commit):
        raise RegistryError("canonical reconciliation does not match the evidence authority baseline")
    if any(not isinstance(canonical[key], str)
           or len(canonical[key]) != 40
           or any(ch not in "0123456789abcdef" for ch in canonical[key])
           for key in ("prior_revision", "current_revision", "last_semantic_revision")):
        raise RegistryError("canonical reconciliation requires full hexadecimal revisions")
    reviewed = reconcile(delta, source, root=root)
    assessments = {row["record"]: row for row in reviewed["assessments"]}
    for row in records:
        assessment = assessments.get(row["record"])
        row["canonical_disposition"] = assessment["state"] if assessment else "not_assessed"
        row["canonical_disposition_reason"] = (assessment["note"] if assessment
                                                else "No canonical delta assessment exists.")
    return {
        "schema_version": SCHEMA_VERSION,
        "source": SRC.as_posix(),
        "source_digest": "sha256:" + hashlib.sha256(raw).hexdigest(),
        "authority": {"upstream_repository": authority["upstream_repository"],
                      "upstream_commit": commit,
                      "downstream_only": True},
        "canonical_reconciliation": {
            "source": RECONCILIATION.as_posix(),
            "source_digest": "sha256:" + hashlib.sha256(delta_raw).hexdigest(),
            "repository": canonical["repository"],
            "prior_revision": canonical["prior_revision"],
            "current_revision": canonical["current_revision"],
        },
        "records": records,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate source and all referenced bytes")
    parser.add_argument("--output", type=Path, help="write derived JSON (never a replacement authority)")
    args = parser.parse_args(argv)
    try:
        data = build()
        if args.output:
            args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        elif not args.check:
            print(json.dumps(data, indent=2))
        print(f"Evidence registry verified: {len(data['records'])} canonical records", file=sys.stderr)
    except (RegistryError, KeyError, TypeError, ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Evidence registry validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
