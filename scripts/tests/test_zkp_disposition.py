"""Negative controls to prevent issue/release assurance overclaim."""
import copy
import json
from pathlib import Path
import unittest
from scripts.validate_zkp_disposition import SOURCE,validate


class DispositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_current_local_gates_fail_closed(self):
        validate(self.data)

    def test_cannot_complete_missing_cap(self):
        value=copy.deepcopy(self.data)
        value["issues"][0]["status"]="completed"
        with self.assertRaises(ValueError):
            validate(value)

    def test_cannot_release_when_unmet(self):
        value=copy.deepcopy(self.data)
        value["release"]["disposition"]="publish"
        with self.assertRaises(ValueError):
            validate(value)

    def test_missing_evidence_rejected(self):
        value=copy.deepcopy(self.data)
        value["issues"][1]["evidence"].append("does-not-exist.json")
        with self.assertRaises(ValueError):
            validate(value)

    def test_no_external_blocker_without_provenance(self):
        value=copy.deepcopy(self.data)
        value["issues"][2]["status"]="externally_blocked"
        value["issues"][2]["external_dependencies"]=[]
        with self.assertRaises(ValueError):
            validate(value)

    def test_duplicate_issue_rejected(self):
        value=copy.deepcopy(self.data)
        value["issues"].append(copy.deepcopy(value["issues"][0]))
        with self.assertRaises(ValueError):
            validate(value)
