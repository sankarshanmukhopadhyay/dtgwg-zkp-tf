#!/usr/bin/env python3
"""Validate repository-local external dependency state invariants."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "docs/governance/external-dependencies.yaml"
ALLOWED_STATES = {
    "ready", "in_progress", "waiting_internal", "waiting_external",
    "needs_judgment", "evidence_required", "superseded",
    "stale_candidate", "completed",
}


def main() -> None:
    data = yaml.safe_load(PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0":
        raise SystemExit("external dependency schema_version must be 1.0")
    items = data.get("items") or []
    if not items:
        raise SystemExit("external dependency register must contain at least one item")

    seen: set[int] = set()
    for item in items:
        issue = item.get("issue")
        state = item.get("state")
        if not isinstance(issue, int) or issue in seen:
            raise SystemExit(f"invalid or duplicate issue: {issue}")
        seen.add(issue)
        if state not in ALLOWED_STATES:
            raise SystemExit(f"issue #{issue}: unsupported state {state}")

        dep = item.get("dependency") or {}
        authorities = dep.get("authority") or []
        if state == "waiting_external":
            if dep.get("kind") != "external" or not authorities:
                raise SystemExit(f"issue #{issue}: waiting_external requires explicit external authority")
            if not dep.get("unblock_conditions"):
                raise SystemExit(f"issue #{issue}: waiting_external requires unblock_conditions")
        if state == "ready" and dep.get("kind") == "external" and authorities:
            raise SystemExit(f"issue #{issue}: READY cannot retain unresolved external blockers")

        evidence = item.get("evidence") or {}
        if evidence.get("state") not in {"verified", "complete"}:
            raise SystemExit(f"issue #{issue}: dependency classification lacks verified evidence")

    print(f"External dependency register valid: {len(items)} item(s); lifecycle invariants passed.")


if __name__ == "__main__":
    main()
