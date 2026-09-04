#!/usr/bin/env python3
"""Fail-closed validator for RAFAELIA formula/authorship lineage registry.

This validator checks repository governance invariants only. It does not prove
copyright, inventorship, world novelty, scientific truth, or physical validity.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "data/autoria/rafaelia_formula_authorship_lineage_omega.v1.json"
EXPECTED_SCHEMA = "rafaelia.formula-authorship-lineage-omega.v1"
EXPECTED_SOURCES = {
    "rafaelmeloreisnovo/papers",
    "rafaelmeloreisnovo/Matem-tica-",
    "rafaelmeloreisnovo/ChipQuantum",
    "instituto-Rafael/relativity-living-light",
    "rafaelmeloreisnovo/templo-vivo-arcs",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))

    if data.get("schema") != EXPECTED_SCHEMA:
        fail("unexpected schema")
    if data.get("append_only") is not True:
        fail("append_only must remain true")
    if data.get("claim_allowed") is not False:
        fail("registry-level claim_allowed must remain false")

    invariants = set(data.get("invariants", []))
    required_invariants = {
        "zero != unknown",
        "classical_primitive != authorial_structure",
        "agent_identity_requires_specific_documentary_evidence",
        "negative_results_are_evidence",
    }
    if not required_invariants.issubset(invariants):
        fail("required epistemic invariants missing")

    snapshots = data.get("source_snapshots", [])
    repos = {row.get("repository") for row in snapshots}
    if repos != EXPECTED_SOURCES:
        fail(f"source repository set mismatch: {repos!r}")
    for row in snapshots:
        head = row.get("head") or row.get("base_head")
        if not isinstance(head, str) or len(head) != 40:
            fail(f"unpinned source head: {row!r}")

    records = data.get("formula_records", [])
    ids = [row.get("id") for row in records]
    if len(ids) != len(set(ids)) or any(not item for item in ids):
        fail("formula record ids must be unique and non-empty")
    if set(ids) != {f"AUTH-F{i:02d}" for i in range(1, 9)}:
        fail("AUTH-F01..AUTH-F08 registry must be complete in V1")

    f03 = next(row for row in records if row["id"] == "AUTH-F03")
    if f03.get("physical_attractor_claim") != "TOKEN_VAZIO":
        fail("Omega-CUBE-42 physical attractor claim must remain TOKEN_VAZIO")

    f06 = next(row for row in records if row["id"] == "AUTH-F06")
    if f06.get("single_universal_scalar_equation") != "TOKEN_VAZIO":
        fail("PG-Omega7 universal scalar equation must remain TOKEN_VAZIO")
    if f06.get("physical_claim") is not False:
        fail("PG-Omega7 physical claim must remain false")

    f07 = next(row for row in records if row["id"] == "AUTH-F07")
    if f07.get("superiority_claim") is not False:
        fail("RLL superiority claim must remain false")

    negatives = data.get("negative_evidence", [])
    rll_negative = next((row for row in negatives if row.get("id") == "RLL-FASE20-NEGATIVE-001"), None)
    if rll_negative is None:
        fail("RLL FASE20 negative evidence must be preserved")
    if not (float(rll_negative["lnB10"]) < 0):
        fail("RLL FASE20 lnB10 sign changed; investigate before promotion")

    claims = {row.get("id"): row for row in data.get("agent_lineage_claims", [])}
    world = claims.get("CLM-WORLD-FIRST-001")
    if not world:
        fail("global world-first claim record missing")
    if world.get("claim_allowed") is not False:
        fail("world-first claim cannot be allowed without external prior-art closure")
    if world.get("state") != "BLOCKED_PENDING_PRIOR_ART":
        fail("world-first claim must remain blocked pending prior art")

    copilot = claims.get("CLM-AGENT-COPILOT-002")
    if not copilot or copilot.get("scope") != "templo-vivo-arcs audited interval":
        fail("Copilot chronology claim must remain explicitly scope-bounded")

    prohibited = set(data.get("prohibited_promotions", []))
    if not any("internal chronology -> world-first" == x for x in prohibited):
        fail("internal chronology/world-first boundary missing")
    if not any("symbolic parable -> physical law" == x for x in prohibited):
        fail("parable/physical-law boundary missing")

    print(f"FORMULA_AUTHORSHIP_LINEAGE_GATE=PASS records={len(records)} sources={len(snapshots)}")
    print("WORLD_FIRST=BLOCKED_PENDING_PRIOR_ART")
    print("RLL_NEGATIVE_EVIDENCE=PRESERVED")
    print("claim_allowed=false")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"FORMULA_AUTHORSHIP_LINEAGE_GATE=FAIL reason={exc}", file=sys.stderr)
        raise SystemExit(1)
