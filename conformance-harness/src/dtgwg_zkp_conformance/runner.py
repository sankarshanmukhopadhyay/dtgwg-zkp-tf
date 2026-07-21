from datetime import datetime, timezone
from .models import TestResult

def run_manifest(manifest, adapter):
    results=[]
    capabilities=adapter.describe_capabilities()
    for case in manifest["tests"]:
        required=case.get("required_capability")
        if required and required not in capabilities:
            results.append(TestResult(case["test_id"],"BLOCKED",case["expected_status"],"blocked","missing-capability",{})); continue
        response=adapter.execute(case["operation"],case["request"])
        verdict="PASS" if response.status==case["expected_status"] and (not case.get("expected_reason") or response.reason_code==case["expected_reason"]) else "FAIL"
        results.append(TestResult(case["test_id"],verdict,case["expected_status"],response.status,response.reason_code,response.output))
    return {"schemaVersion":"1.0","generatedAt":datetime.now(timezone.utc).isoformat(),"implementation":manifest["implementation"],"profile":manifest["profile"],"results":[r.__dict__ for r in results]}
