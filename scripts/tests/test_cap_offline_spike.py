"""Negative and positive cryptographic receipt feasibility tests."""
from __future__ import annotations
import unittest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from scripts.cap_offline_spike import Receipt, assess, canonical, issue


class OfflineVoucherSpikeTests(unittest.TestCase):
    def setUp(self):
        self.mk = Ed25519PrivateKey.generate()
        self.lk = Ed25519PrivateKey.generate()
        self.statement = dict(profile="cap-010-offline-spike-v1", community_root="root-A", holder="alice",
                              voucher="bob", transcript="challenge-1", kind="membership")
        self.m = issue(self.mk, self.statement)
        self.l = issue(self.lk, dict(self.statement, kind="linkage"))

    def outcome(self, m=None, l=None, root="root-A", holder="alice", transcript="challenge-1"):
        return assess(self.mk.public_key(), self.lk.public_key(), m or self.m, l or self.l,
                      expected_root=root, expected_holder=holder, expected_transcript=transcript)

    def test_offline_consistent_receipts(self):
        self.assertEqual(self.outcome(), "RECEIPTS_CONSISTENT_ONLY")

    def test_swapped_voucher(self):
        self.assertEqual(self.outcome(l=issue(self.lk, dict(self.l.statement, voucher="charlie"))), "REJECTED_BINDING")

    def test_wrong_root(self):
        self.assertEqual(self.outcome(root="root-B"), "REJECTED_CONTEXT")

    def test_replayed_transcript(self):
        self.assertEqual(self.outcome(transcript="challenge-2"), "REJECTED_CONTEXT")

    def test_signature_tampering(self):
        changed = Receipt(dict(self.l.statement, holder="mallory"), self.l.signature)
        self.assertEqual(self.outcome(l=changed), "REJECTED_SIGNATURE")

    def test_wrong_verifier_key(self):
        other = Ed25519PrivateKey.generate()
        self.assertEqual(assess(self.mk.public_key(), other.public_key(), self.m, self.l,
                                expected_root="root-A", expected_holder="alice", expected_transcript="challenge-1"),
                         "REJECTED_SIGNATURE")

    def test_self_vouch(self):
        m = issue(self.mk, dict(self.m.statement, holder="bob"))
        l = issue(self.lk, dict(self.l.statement, holder="bob"))
        self.assertEqual(self.outcome(m=m, l=l, holder="bob"), "REJECTED_SELF_VOUCH")

    def test_non_ascii_input(self):
        with self.assertRaises(ValueError):
            canonical(dict(self.statement, holder="alíce"))

    def test_extra_field(self):
        with self.assertRaises(ValueError):
            canonical(dict(self.statement, privileged=True))

    def test_swapped_receipt_roles(self):
        self.assertEqual(self.outcome(m=self.l, l=self.m), "REJECTED_SIGNATURE")


if __name__ == "__main__":
    unittest.main()
