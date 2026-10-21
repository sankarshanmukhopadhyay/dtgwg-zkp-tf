import copy
import json
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from evidence_run import execute, verify

DELTA = Path("docs/implementation-guide/conformance/canonical-reconciliation.json")

@pytest.fixture()
def local(tmp_path):
    (tmp_path / DELTA).parent.mkdir(parents=True)
    (tmp_path / DELTA).write_bytes((ROOT / DELTA).read_bytes())
    (tmp_path / "input.txt").write_text("initial")
    return tmp_path

def capture(root, *, command=None):
    output = root / "run.json"
    return execute(record="013", operator="local-ci", implementation="synthetic-policy-model",
                   dependencies=["input.txt"], command=command or [sys.executable, "-c", "print('ok')"],
                   root=root, output=output)

def test_successful_run_is_recorded_but_not_promoted(local):
    report = capture(local)
    assert report["result"] == "execution_passed"
    assert report["snapshot_sha256"]
    assert "canonical_evidence_not_current" in verify(report, root=local)
    assert json.loads((local / "run.json").read_text()) == report

def test_changed_dependency_invalidates(local):
    report = capture(local)
    (local / "input.txt").write_text("modified")
    assert "dependency_changed:input.txt" in verify(report, root=local)

def test_canonical_revision_invalidates(local):
    report = capture(local)
    delta = json.loads((local / DELTA).read_text())
    delta["canonical"]["current_revision"] = "1" * 40
    (local / DELTA).write_text(json.dumps(delta))
    reasons = verify(report, root=local)
    assert "canonical_revision_changed" in reasons

def test_tampering_invalidates(local):
    report = capture(local)
    mutated = copy.deepcopy(report)
    mutated["run"]["operator"] = "another-operator"
    assert "report_digest_changed" in verify(mutated, root=local)

def test_failed_command_does_not_pass(local):
    report = capture(local, command=[sys.executable, "-c", "raise SystemExit(9)"])
    assert report["result"] == "execution_failed"
    assert "execution_not_passed" in verify(report, root=local)

def test_unknown_record_fails(local):
    with pytest.raises(ValueError, match="not assessed"):
        execute(record="999", operator="ci", implementation="test",
                dependencies=["input.txt"], command=[sys.executable, "-c", "pass"],
                root=local, output=local / "run.json")

def test_missing_and_escaping_dependencies_fail(local):
    for dependency in ["missing.txt", "../outside"]:
        with pytest.raises(ValueError):
            execute(record="013", operator="ci", implementation="test",
                    dependencies=[dependency], command=[sys.executable, "-c", "pass"],
                    root=local, output=local / "run.json")

def test_run_file_not_overwritten(local):
    capture(local)
    with pytest.raises(FileExistsError):
        capture(local)
