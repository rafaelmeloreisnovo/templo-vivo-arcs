#!/usr/bin/env python3
"""Deterministically search tracked text files for evidence supporting POC-10 metrics."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

TERMS = [
    "98%",
    "0.0005",
    "accuracidade",
    "accuracy",
    "30 ativos",
    "10 ativos",
    "10 vendas",
    "hashing times",
]
MAX_BYTES = 8 * 1024 * 1024


def tracked_paths() -> list[Path]:
    raw = subprocess.check_output(["git", "ls-files", "-z"])
    return [Path(p.decode("utf-8", "surrogateescape")) for p in raw.split(b"\0") if p]


def main() -> int:
    matches = []
    scanned = 0
    skipped_large = 0
    skipped_binary = 0

    for path in tracked_paths():
        try:
            st = path.stat()
        except OSError:
            continue
        if st.st_size > MAX_BYTES:
            skipped_large += 1
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if b"\x00" in data[:4096]:
            skipped_binary += 1
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            skipped_binary += 1
            continue
        scanned += 1
        low = text.casefold()
        found = [term for term in TERMS if term.casefold() in low]
        if found:
            matches.append({
                "path": path.as_posix(),
                "terms": found,
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            })

    out = {
        "scope": "tracked UTF-8 text files in current repository snapshot",
        "terms": TERMS,
        "scanned_text_files": scanned,
        "skipped_large": skipped_large,
        "skipped_binary_or_non_utf8": skipped_binary,
        "matches": matches,
        "supporting_artifact_rule": "A supporting artifact must be distinct from the POC-10 claim file and contain dataset, raw observations, calculation code, or a reproducible receipt tied to the claimed metrics.",
    }
    payload = json.dumps(out, ensure_ascii=False, indent=2) + "\n"
    Path("poc10-search-receipt.json").write_text(payload, encoding="utf-8")

    supporting = [m for m in matches if m["path"] != "Hashing times"]
    print(f"scanned_text_files={scanned}")
    print(f"matching_files={len(matches)}")
    print(f"distinct_support_candidates={len(supporting)}")
    for m in matches:
        print(f"MATCH {m['path']} terms={','.join(m['terms'])} sha256={m['sha256']}")
    print(f"receipt_sha256={hashlib.sha256(payload.encode('utf-8')).hexdigest()}")
    if supporting:
        print("POC10_SUPPORT_SEARCH=CANDIDATES_FOUND_REVIEW_REQUIRED")
    else:
        print("POC10_SUPPORT_SEARCH=NO_DISTINCT_SUPPORT_CANDIDATE_FOUND")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
