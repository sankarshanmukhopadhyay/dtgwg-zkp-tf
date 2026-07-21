import argparse, json
from pathlib import Path
from .manifest import load_manifest
from .runner import run_manifest
from .adapters.mock import MockAdapter
from .reporters import json_reporter, markdown_reporter

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--schema",required=True)
    ap.add_argument("--output",default="results")
    args=ap.parse_args()
    result=run_manifest(load_manifest(Path(args.manifest),Path(args.schema)),MockAdapter())
    out=Path(args.output); out.mkdir(parents=True,exist_ok=True)
    json_reporter.write(out/"conformance-results.json",result)
    markdown_reporter.write(out/"conformance-report.md",result)
    failed=sum(r["status"]=="FAIL" for r in result["results"]); blocked=sum(r["status"]=="BLOCKED" for r in result["results"])
    print(f"executed={len(result['results'])} failed={failed} blocked={blocked}")
    raise SystemExit(1 if failed else 0)

if __name__ == "__main__": main()
