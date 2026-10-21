import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from record013_pressure_tests import Offer, accept_pair, completed_relationship, oracle_trace

class Record013PressureTests(unittest.TestCase):
    def setUp(self):
        self.a = Offer("session-1", 7, "commit-a")
        self.b = Offer("session-1", 7, "commit-b")

    def check(self, a=None, b=None, **options):
        args = {"expected_negotiation": "session-1", "current_epoch": 7,
                "a_allowed": True, "b_allowed": True}
        args.update(options)
        return accept_pair(a or self.a, b or self.b, **args)

    def test_mutual_admissibility(self):
        self.assertTrue(self.check())

    def test_asymmetric_community_policy(self):
        self.assertFalse(self.check(b_allowed=False))
        self.assertFalse(self.check(a_allowed=False))

    def test_replay_new_negotiation(self):
        self.assertFalse(self.check(expected_negotiation="session-2"))

    def test_stale_policy_or_mismatched_epoch(self):
        self.assertFalse(self.check(current_epoch=8))
        self.assertFalse(self.check(b=Offer("session-1", 6, "commit-b")))

    def test_substitution_and_mixed_negotiation(self):
        self.assertFalse(self.check(b=Offer("session-2", 7, "commit-b")))
        self.assertFalse(self.check(b=Offer("session-1", 7, "")))

    def test_abort_after_both_are_admissible(self):
        self.assertFalse(completed_relationship(both_admissible=True,
                                               a_published=True,b_published=False))
        self.assertFalse(completed_relationship(both_admissible=True,
                                               a_published=False,b_published=False))
        self.assertTrue(completed_relationship(both_admissible=True,
                                              a_published=True,b_published=True))

    def test_boolean_policy_oracle_leakage(self):
        # Binary probing a private cut point can narrow it even if proofs reveal no witness.
        observations = oracle_trace(5, [2, 4, 6, 5])
        self.assertEqual(observations, [False, False, True, True])

if __name__ == "__main__":
    unittest.main()
