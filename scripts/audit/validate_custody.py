#!/usr/bin/env python3
"""Validate the append-only custody ledger without external dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED = {
    "proof_id", "concept_id", "repository", "path", "blob_sha", "commit_sha",
    "commit_prefix_observed", "authored_at", "committed_at", "author_account",
    "committer_account", "agent_identity", "agent_evidence", "capability_class",
    "capability_demonstrated", "limitation", "derived_from", "derived_into",
    "reproduction_status", "claim_status", "claim_allowed", "source_basis",
    "audit_timestamp",
}

CAPABILITIES = {
    "C0_TEXTUAL", "C1_FORMAL", "C2_STRUCTURED", "C3_EXECUTABLE_PARTIAL",
    "C4_EXECUTABLE", "C5_REPRODUCED", "C6_INDEPENDENT", "TOKEN_VAZIO",
}

REPRODUCTION = {
    "NOT_APPLICABLE", "NOT_REPRODUCED", "MECHANICS_REPRODUCED",
    "HISTORICAL_REPRODUCED", "INDEPENDENT_REPRODUCED", "TOKEN_VAZIO",
}

CLAIMS = {
    "PROVED_INTERNAL", "PROVED_PRE_AGENT", "PROVED_PRE_AGENT_PARTIAL",
    "PROVED_PRE_AGENT_STRUCTURE", "HISTORICAL_METHOD_RECORD",
    "HISTORICAL_CLAIM", "PARTIAL", "BLOCKED_PRIOR_ART", "TOKEN_VAZIO",
}

SHA40 = re.compile(r"^[0-9a-f]{40}$")
PREFIX = re.compile(r"^[0-9a-f]{8,40}$")
BLOCKED_CLAIMS = {"HISTORICAL_CLAIM", "BLOCKED_PRIOR_ART", "TOKEN_VAZIO"}


def load_jsonl(path: Path):
    records = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"line {lineno}: invalid JSON: {exc}") from exc
        records.append((lineno, obj))
    return records


def validate_record(lineno: int, rec: dict) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED - rec.keys()
    extra = rec.keys() - REQUIRED
    if missing:
        errors.append(f"line {lineno}: missing fields: {sorted(missing)}")
    if extra:
        errors.append(f"line {lineno}: unexpected fields: {sorted(extra)}")
    if missing:
        return errors

    if rec["repository"] != "rafaelmeloreisnovo/templo-vivo-arcs":
        errors.append(f"line {lineno}: unexpected repository")

    for field in ("blob_sha", "commit_sha"):
        value = rec[field]
        if value != "TOKEN_VAZIO" and not SHA40.fullmatch(value):
            errors.append(f"line {lineno}: {field} must be SHA-1(40 hex) or TOKEN_VAZIO")

    prefix = rec["commit_prefix_observed"]
    if prefix != "TOKEN_VAZIO" and not PREFIX.fullmatch(prefix):
        errors.append(f"line {lineno}: invalid commit_prefix_observed")
    if SHA40.fullmatch(rec["commit_sha"]) and prefix != "TOKEN_VAZIO":
        if not rec["commit_sha"].startswith(prefix):
            errors.append(f"line {lineno}: commit prefix does not match full SHA")

    if rec["capability_class"] not in CAPABILITIES:
        errors.append(f"line {lineno}: invalid capability_class")
    if rec["reproduction_status"] not in REPRODUCTION:
        errors.append(f"line {lineno}: invalid reproduction_status")
    if rec["claim_status"] not in CLAIMS:
        errors.append(f"line {lineno}: invalid claim_status")

    if rec["claim_status"] in BLOCKED_CLAIMS and rec["claim_allowed"] is not False:
        errors.append(f"line {lineno}: blocked/historical claim must keep claim_allowed=false")

    if rec["capability_class"] == "C5_REPRODUCED" and rec["reproduction_status"] != "HISTORICAL_REPRODUCED":
        errors.append(f"line {lineno}: C5 requires HISTORICAL_REPRODUCED")
    if rec["capability_class"] == "C6_INDEPENDENT" and rec["reproduction_status"] != "INDEPENDENT_REPRODUCED":
        errors.append(f"line {lineno}: C6 requires INDEPENDENT_REPRODUCED")

    if not isinstance(rec["derived_from"], list) or not isinstance(rec["derived_into"], list):
        errors.append(f"line {lineno}: derivation fields must be arrays")
    if not isinstance(rec["source_basis"], list) or not rec["source_basis"]:
        errors.append(f"line {lineno}: source_basis must be a non-empty array")
    if not isinstance(rec["claim_allowed"], bool):
        errors.append(f"line {lineno}: claim_allowed must be boolean")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "ledger",
        nargs="?",
        default="evidence/custody/ledger/evidence-ledger.v1.jsonl",
    )
    args = parser.parse_args()
    path = Path(args.ledger)
    if not path.is_file():
        print(f"ERROR: missing ledger: {path}", file=sys.stderr)
        return 2

    try:
        rows = load_jsonl(path)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    seen: set[str] = set()
    errors: list[str] = []
    token_vazio = 0
    claim_allowed = 0

    for lineno, rec in rows:
        proof_id = rec.get("proof_id")
        if proof_id in seen:
            errors.append(f"line {lineno}: duplicate proof_id {proof_id}")
        seen.add(proof_id)
        errors.extend(validate_record(lineno, rec))
        token_vazio += sum(1 for value in rec.values() if value == "TOKEN_VAZIO")
        claim_allowed += int(rec.get("claim_allowed") is True)

    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"ledger={path}")
    print(f"records={len(rows)}")
    print(f"claim_allowed={claim_allowed}")
    print(f"token_vazio_scalar_fields={token_vazio}")
    print(f"sha256={digest}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("CUSTODY_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
