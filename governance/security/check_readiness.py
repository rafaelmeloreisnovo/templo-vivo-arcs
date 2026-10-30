"""Stdlib-only fail-closed validation of SECURITY READINESS V1 (structure, NOT enforcement)."""
import json
import pathlib
import sys

REQUIRED = {
    "G01": "P0", "G02": "P0", "G03": "P0", "G04": "P0",
    "G05": "P1", "G06": "P1", "G07": "P1", "G08": "P1", "G09": "P1",
}
FIELDS = {"id", "priority", "topic", "state", "evidence_ref", "owner", "verified_at"}


def validate(data):
    must = {"schema", "date", "status", "scope", "release_allowed",
            "claim_allowed", "authority", "evidence_rule", "source_ref", "gates"}
    if not isinstance(data, dict) or set(data) != must:
        raise ValueError("invalid top-level schema")
    if data["schema"] != "TVARCS_SECURITY_READINESS_V1":
        raise ValueError("schema revision mismatch")
    if data["status"] != "DRAFT_HOLD":
        raise ValueError("promotion status must remain HOLD in this registry")
    if data["release_allowed"] is not False or data["claim_allowed"] is not False:
        raise ValueError("registry is non-authoritative: cannot promote release/claims")
    for field in ("date", "scope", "authority", "evidence_rule", "source_ref"):
        if not isinstance(data[field], str) or not data[field].strip() or data[field] == "TOKEN_VAZIO":
            raise ValueError("missing governance field " + field)
    gates = data["gates"]
    if not isinstance(gates, list) or len(gates) != len(REQUIRED):
        raise ValueError("missing or extra gates")
    seen = set()
    for gate in gates:
        if not isinstance(gate, dict) or set(gate) != FIELDS:
            raise ValueError("invalid gate fields")
        gid = gate["id"]
        if not isinstance(gid, str) or gid in seen or gid not in REQUIRED:
            raise ValueError("duplicate or unknown gate")
        seen.add(gid)
        if gate["priority"] != REQUIRED[gid]:
            raise ValueError("severity downgrade/upgrade")
        if not isinstance(gate["topic"], str) or not gate["topic"].strip():
            raise ValueError("missing topic")
        if gate["state"] not in ("TOKEN_VAZIO", "FAIL_OBSERVED", "VERIFIED"):
            raise ValueError("unrecognized state")
        for field in ("evidence_ref", "owner", "verified_at"):
            if not isinstance(gate[field], str) or not gate[field].strip():
                raise ValueError("empty evidence field")
        if gate["state"] == "VERIFIED":
            if any(gate[field].startswith("TOKEN_VAZIO") for field in ("evidence_ref", "owner", "verified_at")):
                raise ValueError("evidence/owner/time mandatory to declare VERIFIED")
        # This script cannot authenticate any declared evidence; VERIFIED is NOT a release grant.
    if seen != set(REQUIRED):
        raise ValueError("missing required gate")
    return True


def main():
    path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).with_name("readiness_v1.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    validate(data)
    print("PASS STRUCTURAL_ONLY / PROMOTION_HOLD / CLAIM_ALLOWED=false / 9 gates")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print("FAIL_CLOSED:", exc, file=sys.stderr)
        sys.exit(1)
