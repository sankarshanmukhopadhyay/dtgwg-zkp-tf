"""Conservative, fail-closed evidence impact tests."""
import copy
import unittest

from scripts.evidence_change_impact import impact
from scripts.evidence_registry import build


class ChangeImpactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base=build()

    def test_unmodified_snapshot_is_unchanged(self):
        result=impact(self.base,copy.deepcopy(self.base))
        self.assertFalse(any(r["retest_required"] for r in result["records"]))

    def test_artifact_mutation_invalidates_record(self):
        future=copy.deepcopy(self.base)
        next(r for r in future["records"] if r["record"]=="010")["assets"][0]["sha256"]="0"*64
        result=impact(self.base,future)
        record=next(r for r in result["records"] if r["record"]=="010")
        self.assertIn("evidence_artifact_changed",record["triggers"])
        self.assertEqual(record["status"],"RETEST_REQUIRED")

    def test_upstream_revision_invalidates_all(self):
        later=copy.deepcopy(self.base)
        later["authority"]["upstream_commit"]="1"*40
        result=impact(self.base,later)
        self.assertTrue(result["upstream_drift"])
        self.assertTrue(all(row["retest_required"] for row in result["records"]))

    def test_source_manifest_revision_triggers_review(self):
        later=copy.deepcopy(self.base)
        later["source_digest"]="sha256:"+"f"*64
        result=impact(self.base,later)
        self.assertTrue(result["source_register_drift"])
        self.assertTrue(all(row["retest_required"] for row in result["records"]))

    def test_unreviewed_record_rejected(self):
        later=copy.deepcopy(self.base)
        later["records"].append(dict(later["records"][0],record="999"))
        with self.assertRaises(ValueError):
            impact(self.base,later)

    def test_new_source_rejected(self):
        later=copy.deepcopy(self.base)
        later["source"]="other-registry.json"
        with self.assertRaises(ValueError):
            impact(self.base,later)

    def test_independence_claim_change_triggers_review(self):
        later=copy.deepcopy(self.base)
        later["records"][0]["producer_independence"]="claimed"
        result=impact(self.base,later)
        self.assertIn("independence_claim_changed",result["records"][0]["triggers"])
