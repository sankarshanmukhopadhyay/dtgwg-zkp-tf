"""Experimental record-010 issuance-bound receipt feasibility spike.

Uses Ed25519 signature integrity and explicit cross-statement consistency.
NOT a zero-knowledge proof, privacy-preserving construction, or CAP prover.
Never use production personal data or secrets with this experiment.
"""
from __future__ import annotations

import base64
import json
from dataclasses import dataclass
from typing import Mapping

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

DOMAIN = b"dtg-cap-010-feasibility-v1\x00"


def canonical(document: Mapping[str, object]) -> bytes:
    """Serialize a restricted ASCII-only experimental statement."""
    fields = {"profile", "community_root", "holder", "voucher", "transcript", "kind"}
    if set(document) != fields or not all(type(v) is str and v.isascii() and v for v in document.values()):
        raise ValueError("invalid statement fields")
    if document["profile"] != "cap-010-offline-spike-v1" or document["kind"] not in {"membership", "linkage"}:
        raise ValueError("unsupported receipt profile or kind")
    return DOMAIN + json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


@dataclass(frozen=True)
class Receipt:
    statement: dict[str, str]
    signature: str


def issue(key: Ed25519PrivateKey, statement: dict[str, str]) -> Receipt:
    return Receipt(dict(statement), base64.b64encode(key.sign(canonical(statement))).decode("ascii"))


def verify(key: Ed25519PublicKey, receipt: Receipt) -> bool:
    try:
        key.verify(base64.b64decode(receipt.signature, validate=True), canonical(receipt.statement))
        return True
    except (InvalidSignature, ValueError, TypeError):
        return False


def assess(
    membership_key: Ed25519PublicKey,
    linkage_key: Ed25519PublicKey,
    membership: Receipt,
    linkage: Receipt,
    *,
    expected_root: str,
    expected_holder: str,
    expected_transcript: str,
) -> str:
    """Validate receipt integrity/binding, not authority, freshness or hidden witnesses."""
    if not verify(membership_key, membership) or not verify(linkage_key, linkage):
        return "REJECTED_SIGNATURE"
    m, l = membership.statement, linkage.statement
    if m["kind"] != "membership" or l["kind"] != "linkage":
        return "REJECTED_KIND"
    if any(m[field] != l[field] for field in ("community_root", "voucher", "holder", "transcript")):
        return "REJECTED_BINDING"
    if m["holder"] == m["voucher"]:
        return "REJECTED_SELF_VOUCH"
    if (m["community_root"], m["holder"], m["transcript"]) != (expected_root, expected_holder, expected_transcript):
        return "REJECTED_CONTEXT"
    return "RECEIPTS_CONSISTENT_ONLY"
