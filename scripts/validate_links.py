#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
errors = []


def heading_anchors(path: Path) -> set[str]:
    """Approximate GitHub/Jekyll heading anchors and include explicit Kramdown IDs."""
    text = path.read_text(encoding="utf-8")
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            explicit = re.search(r"\{:\s*#([A-Za-z0-9_.:-]+)", line)
            if explicit:
                anchors.add(explicit.group(1))
            continue
        heading = re.sub(r"<[^>]+>", "", match.group(1))
        heading = re.sub(r"[`*_~]", "", heading)
        slug = heading.strip().lower()
        slug = re.sub(r"[^\w\- ]", "", slug, flags=re.UNICODE)
        slug = re.sub(r"\s+", "-", slug)
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    for explicit in re.findall(r"\{:\s*#([A-Za-z0-9_.:-]+)", text):
        anchors.add(explicit)
    return anchors


for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    text = p.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:")):
            continue

        path_part, sep, fragment = target.partition("#")
        raw = urllib.parse.unquote(path_part)
        if not raw:
            dest = p
        else:
            dest = (p.parent / raw).resolve()
            try:
                dest.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{p.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not dest.exists():
                errors.append(f"{p.relative_to(ROOT)}: missing target {target}")
                continue

        if sep and fragment and dest.suffix.lower() == ".md":
            decoded_fragment = urllib.parse.unquote(fragment)
            if decoded_fragment not in heading_anchors(dest):
                errors.append(
                    f"{p.relative_to(ROOT)}: missing anchor #{decoded_fragment} in {dest.relative_to(ROOT)}"
                )

if errors:
    print("Link validation failed:")
    for error in errors:
        print("- " + error)
    sys.exit(1)
print("Link validation passed (targets and internal Markdown anchors).")
