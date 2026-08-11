#!/usr/bin/env python3
"""Apply append-only evidence resolutions and materialize the effective custody state."""

from __future__ import annotations

import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path

from validate_custody import load_jsonl, validate_record

BASE = Path("evidence/custody/ledger/evidence-ledger.v1.jsonl")
RESOLUTIONS = Path("evidence/custody/ledger/evidence-resolutions.v1.jsonl")
OUT = Path("evidence/custody/generated/custody-effective-v1.jsonl")

ALLOWED_PATCH_FIELDS = {
    "path", "blob_sha", "commit_sha", "committed_at", "author_account",
    "committer_account", "agent_identity", "agent_evidence",
    "capability_class", "limitation",
}

CAP_RANK = {
    "TOKEN_VAZIO": -1,
    "C0_TEXTUAL": 0,
    "C1_FORMAL": 1,
    "C2_STRUCTURED": 2,
    "C3_EXECUTABLE_PARTIAL": 3,
    "C4_EXECUTABLE": 4,
    "C5_REPRODUCED": 5,
    "C6_INDEPENDENT": 6,
}


def load_resolution_rows(path: Path):
    rows = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"resolution line {lineno}: invalid JSON: {exc}") from exc
        rows.append((lineno, obj))
    return rows


def is_safe_fill(field: str, old, new) -> bool:
    if old == "TOKEN_VAZIO":
        return True
    if old == new:
        return True
    if field == "committed_at" and isinstance(old, str) and isinstance(new, str):
        return len(old) == 10 and new.startswith(old + "T")
    return False


def main() -> int:
    if not BASE.is_file() or not RESOLUTIONS.is_file():
        print("ERROR: missing base or resolution ledger", file=sys.stderr)
        return 2

    base_rows = load_jsonl(BASE)
    resolution_rows = load_resolution_rows(RESOLUTIONS)
    effective = {rec["proof_id"]: deepcopy(rec) for _, rec in base_rows}
    order = [rec["proof_id"] for _, rec in base_rows]

    seen_resolution_ids: set[str] = set()
    errors: list[str] = []
    applied = 0

    required_resolution = {
        "resolution_id", "target_proof_id", "mode", "fields", "evidence_delta",
        "source_basis", "remaining_uncertainty", "audit_timestamp",
    }

    for lineno, res in resolution_rows:
        missing = required_resolution - res.keys()
        extra = res.keys() - required_resolution
        if missing:
            errors.append(f"resolution line {lineno}: missing {sorted(missing)}")
            continue
        if extra:
            errors.append(f"resolution line {lineno}: unexpected {sorted(extra)}")
            continue

        rid = res["resolution_id"]
        target = res["target_proof_id"]
        mode = res["mode"]
        if rid in seen_resolution_ids:
            errors.append(f"resolution line {lineno}: duplicate resolution_id {rid}")
            continue
        seen_resolution_ids.add(rid)

        if target not in effective:
            errors.append(f"resolution line {lineno}: unknown target {target}")
            continue
        if mode not in {"FILL_TOKEN_VAZIO", "CORRECT_WITH_EVIDENCE"}:
            errors.append(f"resolution line {lineno}: invalid mode {mode}")
            continue
        if not isinstance(res["fields"], dict) or not res["fields"]:
            errors.append(f"resolution line {lineno}: fields must be non-empty object")
            continue
        if not isinstance(res["evidence_delta"], list) or not res["evidence_delta"]:
            errors.append(f"resolution line {lineno}: evidence_delta required")
            continue
        if not isinstance(res["source_basis"], list) or not res["source_basis"]:
            errors.append(f"resolution line {lineno}: source_basis required")
            continue
        if not isinstance(res["remaining_uncertainty"], list):
            errors.append(f"resolution line {lineno}: remaining_uncertainty must be list")
            continue

        rec = effective[target]
        for field, new in res["fields"].items():
            if field not in ALLOWED_PATCH_FIELDS:
                errors.append(f"resolution line {lineno}: field not patchable: {field}")
                continue
            old = rec[field]
            if mode == "FILL_TOKEN_VAZIO" and not is_safe_fill(field, old, new):
                errors.append(
                    f"resolution line {lineno}: FILL cannot overwrite {field}: {old!r} -> {new!r}"
                )
                continue
            if field == "capability_class":
                if new not in CAP_RANK:
                    errors.append(f"resolution line {lineno}: invalid capability {new}")
                    continue
                if CAP_RANK[new] > CAP_RANK.get(old, -1):
                    errors.append(
                        f"resolution line {lineno}: capability promotion requires a new proof record, not resolution"
                    )
                    continue
            rec[field] = new

        rec["source_basis"] = list(dict.fromkeys([
            *rec["source_basis"],
            *res["source_basis"],
            f"resolution:{rid}",
        ]))
        applied += 1

    for idx, proof_id in enumerate(order, 1):
        errors.extend(validate_record(idx, effective[proof_id]))

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    materialized = "".join(
        json.dumps(effective[proof_id], ensure_ascii=False, separators=(",", ":")) + "\n"
        for proof_id in order
    )
    OUT.write_text(materialized, encoding="utf-8")

    token_vazio = sum(
        1 for proof_id in order for value in effective[proof_id].values()
        if value == "TOKEN_VAZIO"
    )
    agent_unknown = sum(
        effective[proof_id].get("agent_identity") == "AGENT_UNKNOWN" for proof_id in order
    )
    authored_at_unresolved = sum(
        effective[proof_id].get("authored_at") == "TOKEN_VAZIO" for proof_id in order
    )
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()

    print(f"base_records={len(order)}")
    print(f"resolution_records={len(resolution_rows)}")
    print(f"resolutions_applied={applied}")
    print(f"effective_token_vazio_scalar_fields={token_vazio}")
    print(f"agent_unknown={agent_unknown}")
    print(f"authored_at_unresolved={authored_at_unresolved}")
    print(f"effective_state={OUT}")
    print(f"effective_sha256={digest}")
    print("RESOLUTION_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
