#!/usr/bin/env python3
"""Public-only readiness evidence gate. Never certifies deployed controls."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT / "governance/security/v10/operational_facts_v10.json"
VALID_OBS = {"REPO_METADATA_OBSERVED", "SOURCE_OBSERVED", "HISTORICAL_RECEIPT_OBSERVED", "SOURCE_COMPONENTS_ONLY", "NOT_VERIFIED"}
REQUIRED = {"G01", "G02", "G03", "G04"}
VOID = "TOKEN_VAZIO"

def validate(d):
    errors = []
    def bad(value):
        errors.append(value)
    if d.get("schema") != "TVARCS_OPERATIONS_P0_V10" or d.get("promotion") != "HOLD":
        bad("schema or promotion altered")
    if any(d.get(k) is not False for k in ("release_allowed", "legal_claim_allowed", "operational_controls_claim_allowed")):
        bad("false elevation of claim")
    if d.get("source_repo") != "rafaelmeloreisnovo/templo-vivo-arcs":
        bad("source authority drift")
    facts = d.get("real_world_operations", [])
    if not isinstance(facts, list) or len(facts) != 6:
        bad("incomplete fact census")
    else:
        ids = [x.get("id") for x in facts]
        if ids != ["OP01","OP02","OP03","OP04","OP05","OP06"]:
            bad("fact sequence or duplicate")
        for f in facts:
            if f.get("observation") not in VALID_OBS:
                bad("illegal observation state")
            if not f.get("source_scope") or not f.get("unknown"):
                bad("missing boundary")
        if facts[-1].get("observation") != "NOT_VERIFIED" or facts[-1].get("evidence_ref") != VOID:
            bad("live site not independently verified")
    gates = d.get("p0_gates", [])
    if not isinstance(gates, list) or {x.get("id") for x in gates} != REQUIRED or len(gates) != 4:
        bad("P0 exact set mismatch")
    else:
        for item in gates:
            if any(item.get(k) != VOID for k in ("state", "owner", "evidence_ref")):
                bad("unsupported P0 closure")
            if not item.get("required"):
                bad("evidence criterion missing")
    reviews = d.get("jurisdiction_review", [])
    if not isinstance(reviews, list) or {x.get("id") for x in reviews} != {"BR","US","UK","FR","DE","MX"} or len(reviews) != 6:
        bad("country scope drift")
    else:
        for r in reviews:
            if any(r.get(k) != VOID for k in ("operator_nexus", "counsel")) or r.get("legal_status") != "HOLD":
                bad("uncertified jurisdiction escalation")
            if not str(r.get("source", "")).startswith("https://") or not r.get("issue"):
                bad("missing source/issues")
    pred = d.get("release_predicate", {})
    if not isinstance(pred, dict) or not pred or not all(value is True for value in pred.values()):
        bad("release gate incomplete")
    return errors

if __name__ == "__main__":
    try:
        obj = json.loads(PATH.read_text(encoding="utf-8"))
        errs = validate(obj)
    except (OSError, ValueError, TypeError) as e:
        errs = [str(e)]
    if errs:
        for err in errs:
            print("HOLD:" + err)
        raise SystemExit(1)
    print("PASS_SCOPED_RESEARCH_GATE; P0_UNCLOSED; LEGAL_UNREVIEWED; RELEASE_HOLD")
