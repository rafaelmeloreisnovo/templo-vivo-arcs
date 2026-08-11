#!/usr/bin/env python3
"""Deterministically search tracked text files for evidence supporting POC-10 metrics."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

CLAIM_TERMS = [
    "98%",
    "0.0005",
    "accuracidade",
    "accuracy",
    "30 ativos",
    "10 ativos",
    "10 vendas",
]
DISCOVERY_TERMS = CLAIM_TERMS + ["hashing times"]
EVIDENCE_MARKERS = [
    "dataset", "receipt", ".csv", ".json", "amostra", "sample",
    "dados", "observa", "calculo", "cálculo", "benchmark", "raw",
]
DERIVED_PREFIXES = (
    "docs/auditoria/",
    "docs/legal/",
    "evidence/custody/",
    "scripts/audit/",
)
MAX_BYTES = 8 * 1024 * 1024


def tracked_paths() -> list[Path]:
    raw = subprocess.check_output(["git", "ls-files", "-z"])
    return [Path(p.decode("utf-8", "surrogateescape")) for p in raw.split(b"\0") if p]


def main() -> int:
    matches = []
    strong_candidates = []
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
        found = [term for term in DISCOVERY_TERMS if term.casefold() in low]
        if not found:
            continue
        markers = [m for m in EVIDENCE_MARKERS if m.casefold() in low]
        path_s = path.as_posix()
        derived = path_s.startswith(DERIVED_PREFIXES)
        claim_hits = [term for term in CLAIM_TERMS if term.casefold() in low]
        strong = (
            path_s != "Hashing times"
            and not derived
            and ("0.0005" in claim_hits or len(claim_hits) >= 3)
            and len(markers) >= 2
        )
        rec = {
            "path": path_s,
            "terms": found,
            "claim_terms": claim_hits,
            "evidence_markers": markers,
            "derived_audit_or_legal": derived,
            "strong_support_candidate": strong,
            "size": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }
        matches.append(rec)
        if strong:
            strong_candidates.append(rec)

    out = {
        "scope": "tracked UTF-8 text files in current repository snapshot",
        "discovery_terms": DISCOVERY_TERMS,
        "claim_terms": CLAIM_TERMS,
        "evidence_markers": EVIDENCE_MARKERS,
        "derived_prefixes_excluded_from_support": list(DERIVED_PREFIXES),
        "scanned_text_files": scanned,
        "skipped_large": skipped_large,
        "skipped_binary_or_non_utf8": skipped_binary,
        "matches": matches,
        "strong_support_candidates": strong_candidates,
        "supporting_artifact_rule": "Candidate must be distinct from Hashing times, not be a derived audit/legal artifact, contain rare or co-occurring claim terms, and contain at least two data/receipt/calculation markers. Passing this lexical gate still requires human/source review before any metric claim is promoted.",
    }
    payload = json.dumps(out, ensure_ascii=False, indent=2) + "\n"
    Path("poc10-search-receipt.json").write_text(payload, encoding="utf-8")

    print(f"scanned_text_files={scanned}")
    print(f"matching_files={len(matches)}")
    print(f"strong_support_candidates={len(strong_candidates)}")
    for m in strong_candidates:
        print(f"STRONG_CANDIDATE {m['path']} claim_terms={','.join(m['claim_terms'])} markers={','.join(m['evidence_markers'])} sha256={m['sha256']}")
    print(f"receipt_sha256={hashlib.sha256(payload.encode('utf-8')).hexdigest()}")
    if strong_candidates:
        print("POC10_SUPPORT_SEARCH=STRONG_CANDIDATES_FOUND_REVIEW_REQUIRED")
    else:
        print("POC10_SUPPORT_SEARCH=NO_STRONG_SUPPORT_CANDIDATE_FOUND")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
