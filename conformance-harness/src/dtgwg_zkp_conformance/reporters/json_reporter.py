import json
from pathlib import Path
def write(path: Path, payload: dict): path.write_text(json.dumps(payload,indent=2)+"\n")
