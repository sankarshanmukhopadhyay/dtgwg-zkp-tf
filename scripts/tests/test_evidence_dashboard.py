"""Regression tests for source-derived evidence dashboard invariants."""
import copy
import json
from pathlib import Path
import unittest

from scripts.generate_evidence_dashboard import ROOT, SOURCE, render


class DashboardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((ROOT / SOURCE).read_text(encoding="utf-8"))

    def test_missing_record_explicit(self):
        output = render(self.source)
        self.assertIn("| 009 | no registered evidence | none | **missing evidence registration** |", output)

    def test_no_upstream_promotion(self):
        result = render(self.source)
        self.assertIn("not** independently substantiated", result)
        self.assertIn("No downstream label advances", result)

    def test_unknown_class_rejected(self):
        altered = copy.deepcopy(self.source)
        altered["current_evidence"][0]["classes"].append("magic_interoperability")
        with self.assertRaises(ValueError):
            render(altered)

    def test_duplicate_record_rejected(self):
        altered = copy.deepcopy(self.source)
        altered["current_evidence"].append(copy.deepcopy(altered["current_evidence"][0]))
        with self.assertRaises(ValueError):
            render(altered)

    def test_no_unreviewed_new_record(self):
        altered = copy.deepcopy(self.source)
        altered["current_evidence"][0]["record"] = "999"
        with self.assertRaises(ValueError):
            render(altered)
