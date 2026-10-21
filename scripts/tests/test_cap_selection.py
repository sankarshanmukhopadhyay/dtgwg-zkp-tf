"""Regression checks for CAP selection authority and requirement completeness."""
import copy
import json
from pathlib import Path
import unittest

from scripts.validate_cap_selection import validate

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "docs/implementation-guide/conformance"


class SelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.selection = json.loads((DIR / "cap-construction-selection.json").read_text())
        cls.baseline = json.loads((DIR / "record-010-requirement-matrix.json").read_text())

    def test_current_selection_is_valid_and_not_frozen(self):
        validate(self.selection, self.baseline)

    def test_cannot_claim_premature_freeze(self):
        altered = copy.deepcopy(self.selection)
        altered["decision"] = "frozen"
        with self.assertRaises(ValueError):
            validate(altered, self.baseline)

    def test_upstream_mismatch_fails(self):
        altered = copy.deepcopy(self.selection)
        altered["upstream_commit"] = "invalid"
        with self.assertRaises(ValueError):
            validate(altered, self.baseline)

    def test_missing_clause_is_rejected(self):
        altered = copy.deepcopy(self.selection)
        altered["gates"].pop()
        with self.assertRaises(ValueError):
            validate(altered, self.baseline)

    def test_duplicate_candidate_is_rejected(self):
        altered = copy.deepcopy(self.selection)
        altered["candidates"].append(copy.deepcopy(altered["candidates"][0]))
        with self.assertRaises(ValueError):
            validate(altered, self.baseline)


if __name__ == "__main__":
    unittest.main()
