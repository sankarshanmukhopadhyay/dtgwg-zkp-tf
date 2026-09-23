from dtgwg_zkp_conformance.adapters.transcript import TranscriptBindingAdapter


def run(**kwargs):
    base = {
        "proof_transcript_digest": "sha256:abc",
        "supplied_transcript_digest": "sha256:abc",
        "canonical_encoding_valid": True,
        "predicate_accepted": True,
        "audience_match": True,
        "context_match": True,
        "challenge_match": True,
        "expired": False,
        "replay_seen": False,
    }
    base.update(kwargs)
    return TranscriptBindingAdapter().execute("evaluate_transcript_binding", base)


def test_accepts_fully_bound_transcript():
    r = run()
    assert r.status == "accepted"
    assert r.reason_code == "transcript-bound-and-policy-accepted"


def test_rejects_digest_substitution():
    r = run(supplied_transcript_digest="sha256:def")
    assert (r.status, r.reason_code) == ("rejected", "transcript-digest-mismatch")


def test_binding_does_not_bypass_canonicalization():
    r = run(canonical_encoding_valid=False)
    assert (r.status, r.reason_code) == ("rejected", "canonical-encoding-invalid")
    assert r.output["proofBindingValid"] is True


def test_binding_does_not_bypass_predicate_policy():
    r = run(predicate_accepted=False)
    assert (r.status, r.reason_code) == ("rejected", "predicate-not-accepted")


def test_rejects_audience_context_and_challenge_mismatch():
    assert run(audience_match=False).reason_code == "audience-mismatch"
    assert run(context_match=False).reason_code == "context-mismatch"
    assert run(challenge_match=False).reason_code == "challenge-mismatch"


def test_rejects_expiry_and_replay_separately():
    assert run(expired=True).reason_code == "transcript-expired"
    assert run(replay_seen=True).reason_code == "transcript-replay"
