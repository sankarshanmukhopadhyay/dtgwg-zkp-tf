"""Fail-closed provenance and absence tests for the downstream evidence projection."""
import hashlib
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest

from scripts.evidence_registry import ROOT, SRC, RECONCILIATION, RegistryError, build, digest_local
from scripts.evidence_change_impact import impact


class EvidenceRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = build()

    def test_missing_record_is_explicit(self):
        missing = [v for v in self.registry["records"] if v["record"] == "009"]
        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0]["registration"], "missing")
        self.assertEqual(missing[0]["downstream_labels"], [])

    def test_artifact_digests_are_hex(self):
        for record in self.registry["records"]:
            for asset in record["assets"]:
                self.assertRegex(asset["sha256"], r"^[0-9a-f]{64}$")

    def test_no_invented_execution_or_independence(self):
        for record in self.registry["records"]:
            self.assertIsNone(record["observed_cryptographic_outcome"])
            self.assertIsNone(record["reproduction_environment"])
            self.assertEqual(record["producer_independence"], "not_established")
        self.assertTrue(self.registry["authority"]["downstream_only"])

    def copy_inputs(self, root):
        source = json.loads((ROOT / SRC).read_text())
        paths = {SRC, RECONCILIATION}
        paths.update(Path(asset) for row in source["current_evidence"] for asset in row["assets"])
        for path in paths:
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / path).read_bytes())

    def test_canonical_reconciliation_is_visible_without_promoting_labels(self):
        delta_raw = (ROOT / RECONCILIATION).read_bytes()
        delta = json.loads(delta_raw)
        source = json.loads((ROOT / SRC).read_text())
        checkpoint = self.registry["canonical_reconciliation"]
        self.assertEqual(checkpoint["current_revision"], delta["canonical"]["current_revision"])
        self.assertEqual(checkpoint["prior_revision"], self.registry["authority"]["upstream_commit"])
        self.assertEqual(checkpoint["source_digest"], "sha256:" + hashlib.sha256(delta_raw).hexdigest())
        self.assertNotEqual(checkpoint["current_revision"], checkpoint["prior_revision"])
        expected = {row["record"]: row for row in delta["record_impacts"]}
        labels = {row["record"]: row["labels"] for row in source["current_evidence"]}
        for record in self.registry["records"]:
            rid = record["record"]
            self.assertEqual(record["canonical_disposition"], expected[rid]["disposition"])
            self.assertEqual(record["canonical_disposition_reason"], expected[rid]["reason"])
            self.assertEqual(record["downstream_labels"], labels.get(rid, []))
        self.assertEqual(next(r for r in self.registry["records"] if r["record"] == "006")[
            "canonical_disposition"], "retest_required")
        self.assertEqual(next(r for r in self.registry["records"] if r["record"] == "010")[
            "canonical_disposition"], "stale")

    def test_missing_assessment_and_changed_delta_trigger_retest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_inputs(root)
            delta = json.loads((root / RECONCILIATION).read_text())
            delta["record_impacts"] = [row for row in delta["record_impacts"]
                                       if row["record"] not in {"006", "009"}]
            (root / RECONCILIATION).write_text(json.dumps(delta))
            current = build(root)
            for rid in ("006", "009"):
                row = next(r for r in current["records"] if r["record"] == rid)
                self.assertEqual(row["canonical_disposition"], "not_assessed")
            result = impact(self.registry, current)
            self.assertTrue(result["canonical_reconciliation_drift"])
            self.assertTrue(all(row["retest_required"] for row in result["records"]))
            row = next(r for r in result["records"] if r["record"] == "006")
            self.assertIn("canonical_disposition_changed", row["triggers"])
            self.assertEqual(row["canonical_disposition"], "not_assessed")

    def test_reconciliation_mismatch_and_unknown_disposition_fail_closed(self):
        for key, value in (("repository", "other/spec"), ("prior_revision", "1" * 40),
                           ("current_revision", "z" * 40)):
            with self.subTest(key=key), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self.copy_inputs(root)
                delta = json.loads((root / RECONCILIATION).read_text())
                delta["canonical"][key] = value
                (root / RECONCILIATION).write_text(json.dumps(delta))
                with self.assertRaises(RegistryError):
                    build(root)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_inputs(root)
            delta = json.loads((root / RECONCILIATION).read_text())
            delta["record_impacts"][0]["disposition"] = "pass"
            (root / RECONCILIATION).write_text(json.dumps(delta))
            with self.assertRaises(ValueError):
                build(root)
            (root / RECONCILIATION).unlink()
            with self.assertRaises(FileNotFoundError):
                build(root)

    def test_consumer_cli_emits_reconciled_projection(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "projection.json"
            subprocess.run([sys.executable, "scripts/evidence_registry.py", "--output", str(output)],
                           cwd=ROOT, check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(output.read_text()), self.registry)

    def test_path_traversal_rejected(self):
        with self.assertRaises(RegistryError):
            digest_local(ROOT, "../../etc/passwd")

    def test_missing_path_rejected(self):
        with self.assertRaises(RegistryError):
            digest_local(ROOT, "does-not-exist-zkp-artifact.json")
