"""Negative-space evidence for policy oracles, fairness, replay and asymmetry."""
import unittest

from scripts.record013_pressure import (LocalDecision, leakage_example, mutual_observation,
                                        cross_epoch_oracle, assess_concurrent_negotiations,
                                        coalition_view)


class PressureTests(unittest.TestCase):
    def decision(self, accepted=True, epoch=5, negotiation="n-1", committed=True):
        return LocalDecision(accepted, epoch, negotiation, committed)

    def test_valid_local_admission_does_not_prove_publication(self):
        self.assertEqual(mutual_observation(self.decision(), self.decision(),
                                            expected_epoch=5, negotiation="n-1"),
                         "LOCALLY_ACCEPTED_NOT_PUBLISHED")

    def test_adaptive_boolean_oracle_leaks_threshold(self):
        result = leakage_example(37, range(64))
        self.assertEqual(result["remaining"], {37})
        self.assertLessEqual(len(result["probes"]), 7)
        self.assertGreater(result["domain_size"], 1)

    def test_two_candidate_oracle_terminates(self):
        result = leakage_example(1, range(2))
        self.assertEqual(result['remaining'], {1})
        self.assertEqual(len(result['probes']), 1)

    def test_abort_after_result_never_implies_fair_exchange(self):
        self.assertEqual(mutual_observation(self.decision(), self.decision(committed=False),
                                            expected_epoch=5, negotiation="n-1"), "INCOMPLETE_EXCHANGE")

    def test_cross_negotiation_replay(self):
        self.assertEqual(mutual_observation(self.decision(), self.decision(negotiation="n-0"),
                                            expected_epoch=5, negotiation="n-1"), "REJECTED_REPLAY")

    def test_policy_epoch_mismatch(self):
        self.assertEqual(mutual_observation(self.decision(), self.decision(epoch=4),
                                            expected_epoch=5, negotiation="n-1"), "INDETERMINATE_STALE_POLICY")

    def test_asymmetric_community_admission(self):
        self.assertEqual(mutual_observation(self.decision(), self.decision(accepted=False),
                                            expected_epoch=5, negotiation="n-1"), "NOT_MUTUALLY_ACCEPTED")

    def test_cross_epoch_oracle_exposes_policy_delta(self):
        results = cross_epoch_oracle({5: 19, 6: 31}, range(64))
        self.assertEqual(results[5]["remaining"], {19})
        self.assertEqual(results[6]["remaining"], {31})
        self.assertNotEqual(results[5]["remaining"], results[6]["remaining"])

    def test_concurrent_positive_negotiations_do_not_establish_atomicity(self):
        conversations = [
            (self.decision(negotiation="n-1"), self.decision(negotiation="n-1")),
            (self.decision(negotiation="n-2"), self.decision(negotiation="n-2")),
        ]
        self.assertEqual(assess_concurrent_negotiations(conversations), "NO_ATOMIC_PUBLICATION_ASSURANCE")

    def test_concurrent_reuse_of_negotiation_identifier_is_rejected(self):
        pair = (self.decision(), self.decision())
        self.assertEqual(assess_concurrent_negotiations([pair, pair]), "REJECTED_CONTEXT_COLLISION")

    def test_colluding_observers_pool_yes_no_results(self):
        view = coalition_view([("v1", "n-1", True), ("v2", "n-1", False)])
        self.assertEqual(len(view["n-1"]), 2)
        self.assertIn(("v2", False), view["n-1"])

    def test_cross_epoch_invalid_threshold_rejected(self):
        with self.assertRaises(ValueError):
            cross_epoch_oracle({1: 99}, range(64))

    def test_two_rejections_do_not_become_mutual_acceptance(self):
        self.assertEqual(mutual_observation(self.decision(False), self.decision(False),
                                            expected_epoch=5, negotiation="n-1"), "NOT_MUTUALLY_ACCEPTED")


if __name__ == "__main__":
    unittest.main()
