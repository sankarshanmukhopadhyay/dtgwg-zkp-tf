"""Negative-space evidence for policy oracles, fairness, replay and asymmetry."""
import unittest

from scripts.record013_pressure import LocalDecision, leakage_example, mutual_observation


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

    def test_two_rejections_do_not_become_mutual_acceptance(self):
        self.assertEqual(mutual_observation(self.decision(False), self.decision(False),
                                            expected_epoch=5, negotiation="n-1"), "NOT_MUTUALLY_ACCEPTED")


if __name__ == "__main__":
    unittest.main()
