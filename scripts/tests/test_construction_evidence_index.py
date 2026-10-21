"""Fail-closed tests for the downstream construction evidence index."""
import json
from pathlib import Path
import tempfile
import unittest

from scripts.construction_evidence_index import (
    EvidenceIndexError, INDEX, MANIFEST, build, main,
)


class EvidenceIndexTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / MANIFEST).parent.mkdir(parents=True)
        (self.root / "evidence").mkdir()
        (self.root / "evidence" / "fixture.txt").write_text("valid", encoding="utf-8")
        self.profile = {
            "profile_id": "EXP-TEST",
            "claim_layer": "construction",
            "evidence_state": "partially_verified",
            "interoperability": {"state": "evidence_required", "independent": False},
            "execution": {"evidence_file": "evidence/fixture.txt"},
            "provenance": ["evidence/fixture.txt"],
            "claim_boundary": "Fixture does not establish cryptographic validity.",
        }
        self.write_manifest([self.profile])

    def write_manifest(self, profiles):
        (self.root / MANIFEST).write_text(
            json.dumps({"schema_version": "1.0", "profiles": profiles}), encoding="utf-8"
        )

    def test_repeatable_index_and_check(self):
        self.assertEqual(main(["--root", str(self.root)]), 0)
        self.assertEqual(main(["--root", str(self.root), "--check"]), 0)
        self.assertEqual(len(build(self.root)["profiles"]), 1)

    def test_source_mutation_invalidates_index(self):
        self.assertEqual(main(["--root", str(self.root)]), 0)
        (self.root / "evidence" / "fixture.txt").write_text("changed", encoding="utf-8")
        self.assertEqual(main(["--root", str(self.root), "--check"]), 1)

    def test_missing_evidence_fails_closed(self):
        (self.root / "evidence" / "fixture.txt").unlink()
        with self.assertRaises(EvidenceIndexError):
            build(self.root)

    def test_traversal_rejected(self):
        self.profile["provenance"] = ["../../secret"]
        self.write_manifest([self.profile])
        with self.assertRaises(EvidenceIndexError):
            build(self.root)

    def test_duplicate_profile_rejected(self):
        self.write_manifest([self.profile, self.profile])
        with self.assertRaises(EvidenceIndexError):
            build(self.root)

    def test_false_independence_rejected(self):
        self.profile["interoperability"]["state"] = "verified"
        self.write_manifest([self.profile])
        with self.assertRaises(EvidenceIndexError):
            build(self.root)

    def test_no_promotion_of_source_claim(self):
        result = build(self.root)["profiles"][0]
        self.assertEqual(result["evidence_state"], "partially_verified")
        self.assertEqual(result["interoperability_state"], "evidence_required")
        self.assertNotIn("upstream_lifecycle", result)

    def test_index_missing_is_not_success(self):
        self.assertFalse((self.root / INDEX).exists())
        self.assertEqual(main(["--root", str(self.root), "--check"]), 1)


if __name__ == "__main__":
    unittest.main()
