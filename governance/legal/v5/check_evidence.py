#!/usr/bin/env python3
"""TVARCS V5: conservative, dependency-free structural legal-evidence gate.

PASS_SCOPED is not a legal opinion, valid license, jurisdiction determination
or approval to merge. Fail closed on absent, conflicting, or overstated data.
"""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

ALLOWED_HOSTS = {
    "portal.stf.jus.br", "scon.stj.jus.br", "legis.senado.gov.br",
    "www.planalto.gov.br", "www.supremecourt.gov", "www.supremecourt.uk",
    "www.law.cornell.edu", "www.legislation.gov.uk", "ico.org.uk",
}
ALLOWED_FILES = {
    ".github/workflows/tvarcs-legal-evidence-v5.yml",
    "governance/legal/v5/evidence_register.json",
    "governance/legal/v5/check_evidence.py",
    "governance/legal/v5/test_check_evidence.py",
    "governance/legal/v5/README.md",
}
SOURCE_CLASSES = {"OFFICIAL_COURT", "RELIABLE_TRANSCRIPTION"}
STATUSES = {"MERGED"}
BASE_SHA_LENGTH = 40


def require(test, message):
    if not test:
        raise ValueError(message)


def trustworthy_link(value):
    if not isinstance(value, str):
        return False
    try:
        u = urlsplit(value)
    except ValueError:
        return False
    return (u.scheme == "https" and u.hostname in ALLOWED_HOSTS
            and u.username is None and u.password is None and u.port is None)


def check_changed_files(paths):
    for name in paths:
        require(name in ALLOWED_FILES, "out-of-scope change: " + repr(name))


def check_data(data):
    require(isinstance(data, dict), "register must be a JSON object")
    require(data.get("schema") == "TVARCS_LEGAL_EVIDENCE_V5", "schema mismatch")
    require(data.get("as_of") == "2026-10-30", "review date mismatch")
    sha = data.get("base_sha")
    require(isinstance(sha, str) and len(sha) == BASE_SHA_LENGTH
            and all(c in "0123456789abcdef" for c in sha), "base SHA invalid")
    require(data.get("claim_allowed") is False and data.get("promotion") == "HOLD",
            "automatic legal claim/promotion forbidden")
    prs = data.get("historical_prs")
    require(isinstance(prs, dict) and set(prs) == {"PR44", "PR45", "PR46", "PR47"}
            and all(x in STATUSES for x in prs.values()), "historical PR state mismatch")

    facts = data.get("service_facts")
    needed = {
        "legal_operator", "minors_likely_access", "has_user_generated_content",
        "personal_data_processing", "religion_sensitive_data", "us_uk_nexus",
        "historical_credential_revoked", "independent_legal_review",
        "branch_protection",
    }
    require(isinstance(facts, dict) and set(facts) == needed, "missing operational facts")
    for name, value in facts.items():
        if name == "branch_protection":
            require(value == "FAIL_OBSERVED", "unverified provider promotion")
        else:
            require(isinstance(value, str) and value.startswith("TOKEN_VAZIO_"),
                    "unknown fact falsely promoted: " + name)

    cases = data.get("cases")
    require(isinstance(cases, list) and len(cases) >= 13, "too few case records")
    case_ids = set()
    by_jurisdiction = {"BR": 0, "US": 0, "UK-EW": 0, "UK": 0}
    for case in cases:
        require(isinstance(case, dict), "case must be an object")
        ident = case.get("id")
        require(isinstance(ident, str) and ident not in case_ids
                and len(ident) > 5, "duplicate or invalid case ID")
        case_ids.add(ident)
        j = case.get("jurisdiction")
        require(j in by_jurisdiction, "unknown jurisdiction")
        by_jurisdiction[j] += 1
        require(case.get("source_class") in SOURCE_CLASSES, "unclassified case source")
        require(trustworthy_link(case.get("source_url")), "invalid case URL")
        for key in ("authority", "decision_date", "holding_summary",
                    "adverse_limit", "application_gate"):
            require(isinstance(case.get(key), str) and len(case[key].strip()) > 12,
                    "missing material case field: " + key)
        require(case.get("case_fit") == "TOKEN_VAZIO_UNKNOWN"
                and case.get("pinpoint_verified") is False
                and case.get("counsel_review") == "NOT_DONE",
                "case promoted without counsel/pinpoint")
    require(by_jurisdiction["BR"] >= 6 and by_jurisdiction["US"] >= 4
            and by_jurisdiction["UK-EW"] + by_jurisdiction["UK"] >= 3,
            "insufficient case geography")

    sanctions = data.get("sanctions")
    require(isinstance(sanctions, list) and len(sanctions) >= 5,
            "sanction sources missing")
    sanction_ids = set()
    for sanction in sanctions:
        require(isinstance(sanction, dict), "sanction must be an object")
        ident = sanction.get("id")
        require(isinstance(ident, str) and ident not in sanction_ids
                and len(ident) > 5, "duplicate/invalid sanction ID")
        sanction_ids.add(ident)
        require(trustworthy_link(sanction.get("source_url")), "invalid sanction URL")
        for key in ("statute", "trigger", "statutory_maximum", "category"):
            require(isinstance(sanction.get(key), str) and len(sanction[key]) >= 8,
                    "sanction missing: " + key)
        require(sanction.get("applied") is False
                and sanction.get("scope") == "TOKEN_VAZIO_UNKNOWN"
                and sanction.get("authority_decision") == "NOT_OBSERVED"
                and sanction.get("estimated_fine") == "TOKEN_VAZIO_UNMEASURED",
                "sanction asserted without adjudication")
    controls = data.get("controls")
    require(isinstance(controls, dict) and len(controls) >= 6
            and all(v is True for v in controls.values()),
            "non-regression controls missing")
    require(isinstance(data.get("limitations"), list)
            and len(data["limitations"]) >= 5, "limitations omitted")
    return {"case_records": len(cases), "sanctions": len(sanctions),
            "unresolved_operational_gaps": len(facts) - 1,
            "claim_allowed": False, "status": "PASS_SCOPED_RESEARCH_ONLY"}


def validate_file(path, changed_files=()):
    raw = Path(path).read_bytes()
    require(len(raw) < 250_000, "register size over cap")
    obj = json.loads(raw.decode("utf-8"))
    receipt = check_data(obj)
    check_changed_files(changed_files)
    receipt["sha256_register"] = hashlib.sha256(raw).hexdigest()
    return receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default=str(Path(__file__).with_name("evidence_register.json")))
    parser.add_argument("--changed-file", action="append", default=[])
    args = parser.parse_args()
    try:
        result = validate_file(args.file, args.changed_file)
        print(json.dumps(result, sort_keys=True))
        return 0
    except (ValueError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL_CLOSED", "reason": str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
