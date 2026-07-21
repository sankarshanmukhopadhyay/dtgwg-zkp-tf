from pathlib import Path
def write(path: Path, payload: dict):
    rows=["# Conformance execution report","",f"Profile: `{payload['profile']}`","","| Test | Verdict | Expected | Observed | Reason |","|---|---|---|---|---|"]
    rows += [f"| {r['test_id']} | {r['status']} | {r['expected_status']} | {r['observed_status']} | {r['reason_code']} |" for r in payload['results']]
    path.write_text("\n".join(rows)+"\n")
