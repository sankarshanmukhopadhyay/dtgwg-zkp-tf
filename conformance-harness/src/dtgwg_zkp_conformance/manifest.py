import json
from pathlib import Path
from jsonschema import validate

def load_manifest(path: Path, schema_path: Path) -> dict:
    data=json.loads(path.read_text())
    schema=json.loads(schema_path.read_text())
    validate(data,schema)
    return data
