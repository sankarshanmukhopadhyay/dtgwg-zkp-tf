#!/usr/bin/env python3
"""Run the complete repository validation and deterministic evidence suite."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = (
    "validate_docs.py",
    "validate_conformance.py",
    "validate_style.py",
    "validate_links.py",
    "validate_fixtures.py",
    "validate_upstream_policy.py",
    "validate_interoperability.py",
    "validate_external_evidence.py",
    "validate_conformance_harness.py",
    "validate_threat_model.py",
    "validate_deployment_profiles.py",
    "validate_operations.py",
    "validate_navigation.py",
    "validate_learning_paths.py",
    "validate_diagrams.py",
    "validate_generated_counts.py",
    "validate_decision_governance.py",
    "validate_security_assurance.py",
    "validate_identifier_register.py",
    "validate_construction_evidence.py",
    "validate_external_dependencies.py",
)


def run(*args: str, env: dict[str, str] | None = None) -> None:
    print(f"+ {' '.join(args)}", flush=True)
    subprocess.run(args, cwd=ROOT, env=env, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--evidence-dir",
        type=Path,
        help="retain deterministic conformance evidence at this path",
    )
    args = parser.parse_args()

    for validator in VALIDATORS:
        run(sys.executable, str(ROOT / "scripts" / validator))

    run(sys.executable, "-m", "pytest", "-q", "conformance-harness/tests")

    if args.evidence_dir:
        evidence_dir = args.evidence_dir.resolve()
        evidence_dir.mkdir(parents=True, exist_ok=True)
        execute(evidence_dir)
    else:
        with tempfile.TemporaryDirectory(prefix="dtgwg-zkp-evidence-") as temporary:
            execute(Path(temporary))

    print(f"Complete validation passed: {len(VALIDATORS)} validators and harness evidence.")


def execute(evidence_dir: Path) -> None:
    env = os.environ.copy()
    source = str(ROOT / "conformance-harness" / "src")
    env["PYTHONPATH"] = source + os.pathsep + env.get("PYTHONPATH", "")
    manifests = sorted((ROOT / "conformance-harness" / "examples").glob("*-manifest.json"))
    for manifest in manifests:
        run(
            sys.executable,
            "-m",
            "dtgwg_zkp_conformance.cli",
            "--manifest",
            str(manifest.relative_to(ROOT)),
            "--schema",
            "docs/implementation-guide/conformance/schemas/conformance-test-manifest.schema.json",
            "--output",
            str(evidence_dir / manifest.stem),
            env=env,
        )


if __name__ == "__main__":
    main()
