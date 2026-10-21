"""Generated claim documentation never upgrades consumer inference."""
import copy
import unittest

from scripts.generate_claim_boundary_guide import render
from scripts.validate_proof_claim_boundaries import load, decide


class GuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load()

    def test_cap_nonimplication_is_visible(self):
        output = render(self.data)
        self.assertIn("`voucher_consent`", output)
        self.assertIn("`unique_human`", output)
        self.assertIn("INDETERMINATE", output)

    def test_valid_premise_followed_by_denied_stronger_claim(self):
        self.assertEqual(decide(self.data, "010", "cap_semantic_composition", "cap_semantic_composition"), "ALLOWED")
        self.assertEqual(decide(self.data, "010", "cap_semantic_composition", "voucher_consent"), "REJECTED")

    def test_unknown_claim_fails_closed(self):
        self.assertEqual(decide(self.data, "010", "cap_semantic_composition", "verified_personhood"), "INDETERMINATE")

    def test_generated_view_preserves_all_forbidden_claims(self):
        page = render(self.data)
        for record in self.data["records"]:
            for forbidden in record["does_not_establish"]:
                self.assertIn("`" + forbidden["claim"] + "`", page)
