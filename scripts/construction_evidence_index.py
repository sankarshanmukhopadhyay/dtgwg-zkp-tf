#!/usr/bin/env python3
"""Build or verify a deterministic, non-authoritative index of construction evidence.

The construction manifest is authoritative for local profile declarations. This
index never promotes an evidence state and never infers upstream lifecycle state.
A change to a source artifact invalidates the prior index until regenerated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path("docs/implementation-guide/conformance/construction-evidence-manifest.json")
INDEX = Path("docs/implementation-guide/conformance/construction-evidence-index.json")
VERSION = "1.0"


class EvidenceIndexError(ValueError):
    """An evidence input is missing, malformed, or unsafe to index."""


def sha256(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def file_digest(root: Path, relative: str) -> str:
    """Resolve only repository-contained files; reject URLs and traversal."""
    if not isinstance(relative, str) or not relative or relative.startswith(("http://", "https://")):
        raise EvidenceIndexError(f"not a local evidence path: {relative!r}")
    base = root.resolve()
    target = (base / relative).resolve()
    if not target.is_relative_to(base) or not target.is_file():
        raise EvidenceIndexError(f"missing or out-of-repository evidence: {relative}")
    return sha256(target.read_bytes())


def build(root: Path) -> dict:
    raw = (root / MANIFEST).read_bytes()
    try:
        manifest = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise EvidenceIndexError(f"invalid construction manifest: {exc}") from exc
    if manifest.get("schema_version") != "1.0" or not isinstance(manifest.get("profiles"), list):
        raise EvidenceIndexError("unsupported construction manifest contract")
    profiles = []
    seen = set()
    for profile in manifest["profiles"]:
        identifier = profile.get("profile_id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise EvidenceIndexError(f"missing or repeated profile id: {identifier!r}")
        seen.add(identifier)
        paths = list(profile.get("provenance", []))
        execution = profile.get("execution", {})
        if execution.get("evidence_file"):
            paths.append(execution["evidence_file"])
        if not paths:
            raise EvidenceIndexError(f"{identifier}: no local evidence paths")
        digests = {p: file_digest(root, p) for p in sorted(set(paths))}
        interop = profile.get("interoperability", {})
        state = interop.get("state")
        if state in {"verified", "complete"} and interop.get("independent") is not True:
            raise EvidenceIndexError(f"{identifier}: independent interoperability is not established")
        if profile.get("evidence_state") == "complete" and state != "complete":
            raise EvidenceIndexError(f"{identifier}: complete local evidence has incomplete interoperability")
        profiles.append({
            "profile_id": identifier,
            "claim_layer": profile["claim_layer"],
            "evidence_state": profile["evidence_state"],
            "interoperability_state": state,
            "source_digests": digests,
            "claim_boundary": profile["claim_boundary"],
        })
    return {
        "schema_version": VERSION,
        "authority": "derived-index-only",
        "source_manifest": str(MANIFEST),
        "manifest_digest": sha256(raw),
        "profiles": sorted(profiles, key=lambda item: item["profile_id"]),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="reject stale or absent generated index")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    target = args.root / INDEX
    try:
        result = build(args.root)
        canonical = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != canonical:
                raise EvidenceIndexError("construction evidence index missing or stale; regenerate first")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(canonical, encoding="utf-8")
    except (EvidenceIndexError, KeyError, TypeError, OSError) as exc:
        print(f"Evidence index validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Evidence index {'verified' if args.check else 'generated'}: {len(result['profiles'])} profiles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
