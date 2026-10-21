"""Fail-closed provenance and absence tests for the downstream evidence projection."""
import json
from pathlib import Path
import tempfile
import unittest

from scripts.evidence_registry import ROOT, SRC, RegistryError, build, digest_local


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

    def test_path_traversal_rejected(self):
        with self.assertRaises(RegistryError):
            digest_local(ROOT, "../../etc/passwd")

    def test_missing_path_rejected(self):
        with self.assertRaises(RegistryError):
            digest_local(ROOT, "does-not-exist-zkp-artifact.json")
