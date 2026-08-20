#!/usr/bin/env python3
from pathlib import Path
import json
import sys

from jsonschema import FormatChecker, validate
import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs/implementation-guide/interoperability/external-evidence-register.yaml"
SCHEMA = ROOT / "docs/implementation-guide/conformance/schemas/external-evidence-register.schema.json"

data = yaml.safe_load(REGISTER.read_text())
schema = json.loads(SCHEMA.read_text())
validate(data, schema, format_checker=FormatChecker())

errors = []
ids = [source["id"] for source in data["sources"]]
if len(ids) != len(set(ids)):
    errors.append("external evidence IDs must be unique")
for source in data["sources"]:
    if source["licenseStatus"] != "verified":
        if source["vendoringPermitted"]:
            errors.append(f"{source['id']}: unverified source cannot be vendored")
        if source["ciDependency"]:
            errors.append(f"{source['id']}: unverified source cannot be a CI dependency")
        if source["conformanceCredit"] != "none":
            errors.append(f"{source['id']}: unverified source cannot receive conformance credit")
        if source["permittedUse"] != "reference-and-independent-observation-only":
            errors.append(f"{source['id']}: unverified source must remain reference-only")

if errors:
    print("External evidence validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"External evidence validation passed: {len(data['sources'])} governed source(s).")
