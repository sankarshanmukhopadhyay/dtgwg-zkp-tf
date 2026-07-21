from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class AdapterResponse:
    status: str
    reason_code: str
    output: dict[str, Any]

@dataclass(frozen=True)
class TestResult:
    test_id: str
    status: str
    expected_status: str
    observed_status: str
    reason_code: str
    evidence: dict[str, Any]
