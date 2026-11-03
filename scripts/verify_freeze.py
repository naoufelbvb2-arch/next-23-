#!/usr/bin/env python3
"""Check the published Next 23 v0.1.1 documentary freeze (NOT a model test)."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "governance" / "NEXT23-FREEZE-MANIFEST.json"


def inspect(path_text: str, expected_sha: str, expected_bytes: int | None = None) -> str | None:
    candidate = (ROOT / path_text).resolve()
    if not candidate.is_relative_to(ROOT):
        return f"INVALID PATH: {path_text}"
    if not candidate.is_file():
        return f"MISSING: {path_text}"
    content = candidate.read_bytes()
    digest = hashlib.sha256(content).hexdigest()
    if digest != expected_sha:
        return f"HASH MISMATCH: {path_text} expected={expected_sha} actual={digest}"
    if expected_bytes is not None and len(content) != expected_bytes:
        return f"SIZE MISMATCH: {path_text} expected={expected_bytes} actual={len(content)}"
    return None


def main() -> int:
    if not MANIFEST.is_file():
        print(f"ERROR: missing manifest {MANIFEST}", file=sys.stderr)
        return 2
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = list(data["files"])
    records.append(data["review_report"])
    records.extend(data["historic_drafts"])
    errors = []
    for item in records:
        problem = inspect(item["path"], item["sha256"], item.get("bytes"))
        if problem:
            errors.append(problem)
        else:
            print(f"OK  {item['path']}")
    if errors:
        for problem in errors:
            print(f"FAIL  {problem}", file=sys.stderr)
        print(f"FREEZE INTEGRITY: FAIL ({len(errors)} errors)", file=sys.stderr)
        return 1
    print(f"FREEZE INTEGRITY: PASS ({len(records)}/{len(records)} document files)")
    print("NOTE: documentary hash check only; T3-A tests have NOT been run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
