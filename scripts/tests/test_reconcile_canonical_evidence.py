import json
import sys
import unittest
import tempfile
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from reconcile_canonical_evidence import reconcile, fingerprint_assets

class EvidenceReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.delta = json.loads((ROOT / "docs/implementation-guide/conformance/canonical-reconciliation.json").read_text())
        self.gates = json.loads((ROOT / "docs/implementation-guide/conformance/evidence-promotion-gates.json").read_text())

    def test_every_legacy_evidence_record_is_assessed(self):
        out = reconcile(self.delta, self.gates)
        self.assertTrue(out["assessments"])
        self.assertTrue(all(r["state"] != "current" for r in out["assessments"]))

    def test_missing_record_is_not_silently_current(self):
        delta = json.loads(json.dumps(self.delta))
        delta["record_impacts"] = [x for x in delta["record_impacts"] if x["record"] != "003"]
        result = reconcile(delta, self.gates)
        self.assertEqual(next(x for x in result["assessments"] if x["record"] == "003")["state"], "not_assessed")

    def test_asset_fingerprint_matches_bytes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "proof.json").write_bytes(b"evidence")
            fingerprints = fingerprint_assets(["proof.json"], root=root)
            self.assertEqual(fingerprints[0]["sha256"], hashlib.sha256(b"evidence").hexdigest())
            self.assertEqual(fingerprints[0]["bytes"], 8)

    def test_missing_asset_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaisesRegex(ValueError, "Missing evidence asset"):
                fingerprint_assets(["missing.json"], root=Path(folder))

    def test_path_escape_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaisesRegex(ValueError, "escapes repository"):
                fingerprint_assets(["../outside"], root=Path(folder))

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "link").symlink_to("/etc/hosts")
            with self.assertRaisesRegex(ValueError, "escapes repository"):
                fingerprint_assets(["link"], root=root)

    def test_duplicate_record_fails(self):
        delta = json.loads(json.dumps(self.delta))
        delta["record_impacts"].append(delta["record_impacts"][0])
        with self.assertRaises(ValueError):
            reconcile(delta, self.gates)

    def test_unrecognized_disposition_fails(self):
        delta = json.loads(json.dumps(self.delta))
        delta["record_impacts"][0]["disposition"] = "pass"
        with self.assertRaises(ValueError):
            reconcile(delta, self.gates)

if __name__ == "__main__":
    unittest.main()
