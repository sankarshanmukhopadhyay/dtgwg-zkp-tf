import json

from dtgwg_zkp_conformance.adapters.fixture import FixtureAdapter


def write_fixture(tmp_path, operation, data):
    path = tmp_path / "fixture.json"
    path.write_text(
        json.dumps(
            {"schemaVersion": "1.0", "operation": operation, "input": data}
        )
    )
    return path


def test_context_fixture_derives_acceptance(tmp_path):
    write_fixture(
        tmp_path,
        "evaluate_context_governance",
        {
            "authority": "governance.example",
            "purpose": "account access",
            "verifierSet": ["verifier.example"],
            "epoch": "2026-Q3",
            "permittedLinkage": "within account-access",
            "prohibitedLinkage": "cross-purpose",
            "humanLegibleBoundary": "Used only for account access",
            "collusionTarget": "issuer-verifier",
        },
    )
    response = FixtureAdapter(tmp_path).execute(
        "evaluate_context_governance", {"fixture": "fixture.json"}
    )
    assert response.status == "accepted"
    assert response.reason_code == "context-governance-complete"
    assert response.output["fixtureDigest"].startswith("sha256:")


def test_lifecycle_fixture_derives_rejection(tmp_path):
    write_fixture(
        tmp_path,
        "evaluate_lifecycle",
        {
            "nullifierEpochDays": 30,
            "retentionPolicy": "indefinite",
            "assuranceHorizonDays": 365,
        },
    )
    response = FixtureAdapter(tmp_path).execute(
        "evaluate_lifecycle", {"fixture": "fixture.json"}
    )
    assert response.status == "rejected"
    assert response.reason_code == "lifecycle-unbounded"
    assert "rootCryptoperiodDays" in response.output["invalid"]


def test_fixture_cannot_escape_root(tmp_path):
    response = FixtureAdapter(tmp_path).execute(
        "evaluate_lifecycle", {"fixture": "../outside.json"}
    )
    assert response.status == "blocked"
    assert response.reason_code == "fixture-outside-root"
