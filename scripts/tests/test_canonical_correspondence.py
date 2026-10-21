import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_canonical_correspondence import validate, MAPPING, DELTA

@pytest.fixture
def data():
    return json.loads(MAPPING.read_text()), json.loads(DELTA.read_text())

def test_reviewed_mapping_is_sound_and_explicit(data):
    mapping, delta = data
    assert validate(mapping, delta) == 2
    assert any(row["coverage"] == "uncovered"
               for record in mapping["records"] for row in record["mapping"])

def test_canonical_revision_drift_fails(data):
    mapping, delta = data
    mapping["canonical_revision"] = "0" * 40
    with pytest.raises(ValueError, match="revision differs"):
        validate(mapping, delta)

def test_disposition_cannot_be_promoted_by_correspondence(data):
    mapping, delta = data
    mapping["records"][0]["disposition"] = "current"
    with pytest.raises(ValueError):
        validate(mapping, delta)

def test_duplicate_record_rejected(data):
    mapping, delta = data
    mapping["records"].append(copy.deepcopy(mapping["records"][0]))
    with pytest.raises(ValueError, match="Duplicate"):
        validate(mapping, delta)

def test_missing_negative_space_rejected(data):
    mapping, delta = data
    mapping["records"][0]["gaps"] = []
    with pytest.raises(ValueError, match="gaps"):
        validate(mapping, delta)

def test_uncovered_clause_cannot_claim_test(data):
    mapping, delta = data
    uncovered = next(r for r in mapping["records"][1]["mapping"] if r["coverage"] == "uncovered")
    uncovered["downstream_test"] = "unsupported-PASS"
    with pytest.raises(ValueError, match="cannot claim"):
        validate(mapping, delta)

def test_lost_downstream_asset_fails(data):
    mapping, delta = data
    mapping["records"][0]["downstream"] = "docs/implementation-guide/nonexistent.md"
    with pytest.raises(ValueError, match="Missing evidence asset"):
        validate(mapping, delta)

def test_mapping_cannot_escape_repo(data):
    mapping, delta = data
    mapping["records"][0]["downstream"] = "../escape"
    with pytest.raises(ValueError, match="escapes repository"):
        validate(mapping, delta)
