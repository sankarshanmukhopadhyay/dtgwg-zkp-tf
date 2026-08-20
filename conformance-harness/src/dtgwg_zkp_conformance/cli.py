import argparse, json
from pathlib import Path
from .manifest import load_manifest
from .runner import run_manifest
from .adapters.fixture import FixtureAdapter
from .adapters.mock import MockAdapter
from .reporters import json_reporter, markdown_reporter

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--schema",required=True)
    ap.add_argument("--output",default="results")
    ap.add_argument("--fixture-root",default=".")
    args=ap.parse_args()
    manifest=load_manifest(Path(args.manifest),Path(args.schema))
    adapter_name=manifest["implementation"]["adapter"]
    adapters={
        "mock": MockAdapter,
        "semantic-fixture": lambda: FixtureAdapter(Path(args.fixture_root)),
    }
    if adapter_name not in adapters:
        ap.error(f"unsupported adapter: {adapter_name}")
    result=run_manifest(manifest,adapters[adapter_name]())
    out=Path(args.output); out.mkdir(parents=True,exist_ok=True)
    json_reporter.write(out/"conformance-results.json",result)
    markdown_reporter.write(out/"conformance-report.md",result)
    failed=sum(r["status"]=="FAIL" for r in result["results"]); blocked=sum(r["status"]=="BLOCKED" for r in result["results"])
    print(f"executed={len(result['results'])} failed={failed} blocked={blocked}")
    raise SystemExit(1 if failed else 0)

if __name__ == "__main__": main()
