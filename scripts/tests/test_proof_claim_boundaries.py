"""Executable positive, negative, unknown, and malformed proof-claim tests."""
import copy
import unittest

from scripts.validate_proof_claim_boundaries import BoundaryError, decide, load


class ClaimBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load()

    def test_valid_semantic_self_claim(self):
        self.assertEqual(decide(self.model, "003", "transcript_binding", "transcript_binding"), "ALLOWED")

    def test_valid_proof_cannot_expand_authority(self):
        probes = [
            ("003", "transcript_binding", "policy_acceptance"),
            ("006", "status_proof_validity", "authoritative_freshness"),
            ("008", "hidden_value_commitment", "presentation_unlinkability"),
            ("010", "cap_semantic_composition", "voucher_consent"),
            ("010", "cap_semantic_composition", "unique_human"),
            ("010", "cap_semantic_composition", "cryptographic_cap_execution"),
            ("021", "vac_chain_semantics", "delegation"),
            ("021", "vac_chain_semantics", "task_completion"),
        ]
        for record, demonstrated, proposed in probes:
            with self.subTest(record=record, proposed=proposed):
                self.assertEqual(decide(self.model, record, demonstrated, proposed), "REJECTED")

    def test_unknown_claim_fails_closed(self):
        self.assertEqual(decide(self.model, "003", "transcript_binding", "new_capability"), "INDETERMINATE")

    def test_unknown_record_fails_closed(self):
        self.assertEqual(decide(self.model, "999", "transcript_binding", "transcript_binding"), "INDETERMINATE")

    def test_unproven_input_fails_closed(self):
        self.assertEqual(decide(self.model, "010", "cryptographic_cap_execution", "cryptographic_cap_execution"), "INDETERMINATE")

    def test_no_cross_record_transitive_inference(self):
        self.assertEqual(decide(self.model, "006", "transcript_binding", "transcript_binding"), "INDETERMINATE")

    def test_catalogue_has_unique_claims(self):
        for row in self.model["records"]:
            claims = [x["claim"] for x in row["does_not_establish"]]
            self.assertEqual(len(claims), len(set(claims)))
            self.assertFalse(set(claims) & set(row["establishes"]))


if __name__ == "__main__":
    unittest.main()
