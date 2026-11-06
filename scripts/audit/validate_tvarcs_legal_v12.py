#!/usr/bin/env python3
"""TVARCS V12: structural research gate; NEVER a legal compliance certificate."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "governance/legal/v12/eight_axes_registry_v1.json"
LICENSE_SHA1_BLOB = "58f28b2e172d7e3e9344f0c34c530b84b63e1f55"
HOSTS = {
    "HUMAN_RIGHTS_BELIEF": "www.un.org",
    "CHILD_SAFEGUARDING": "www.unicef.org",
    "CULTURE_EDUCATION": "www.unesco.org",
    "HEALTH_CLAIMS": "www.who.int",
    "PRIVACY_CHILD_DIGITAL": "www.planalto.gov.br",
    "COPYRIGHT_LICENSING": "www.wipo.int",
    "AI_RESEARCH_ETHICS": "www.unesco.org",
    "RULE_OF_LAW": "www.un.org",
}


class GateError(ValueError):
    pass


def demand(ok, why):
    if not ok:
        raise GateError(why)


def unique_pairs(pairs):
    output = {}
    for key, value in pairs:
        demand(key not in output, "duplicate JSON key: " + key)
        output[key] = value
    return output


def load(path=REGISTRY):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def git_blob_sha(data):
    return hashlib.sha1(("blob " + str(len(data)) + "\0").encode() + data).hexdigest()


def check_registry(data):
    demand(isinstance(data, dict), "registry must be object")
    expected = {
        "schema_version": "tvarcs-eight-axes-v1",
        "producer": "rafaelmeloreisnovo/templo-vivo-arcs",
        "status": "DRAFT_RESEARCH_ONLY",
        "promotion": "HOLD",
        "child_safety_gate": "TOKEN_VAZIO",
        "human_legal_reviewer": "TOKEN_VAZIO",
    }
    for key, value in expected.items():
        demand(data.get(key) == value, "gate mismatch: " + key)
    demand(data.get("claim_allowed") is False, "global claim escalation")
    demand(data.get("license_change") is False, "license change unapproved")
    demand(bool(re.fullmatch("[0-9a-f]{40}", str(data.get("source_main_sha", "")))),
           "unverified source main SHA format")
    axes = data.get("axes")
    demand(isinstance(axes, list) and len(axes) == 8, "eight axes required")
    ids = [a.get("id") for a in axes if isinstance(a, dict)]
    demand(len(ids) == 8 and set(ids) == set(HOSTS), "unknown/duplicate/missing axis")
    for axis in axes:
        label = axis["id"]
        demand(axis.get("claim_allowed") is False, label + ": unsupported claim")
        demand(axis.get("qualified_review") == "TOKEN_VAZIO",
               label + ": legal review must remain unknown")
        demand(axis.get("evidence") == "SOURCE_REFERENCE_ONLY",
               label + ": source is not execution evidence")
        demand(axis.get("application") == "REQUIRES_SCOPE_REVIEW",
               label + ": jurisdiction not verified")
        demand(axis.get("source_class") == "PRIMARY_OR_INSTITUTIONAL",
               label + ": source class altered")
        source = axis.get("source")
        demand(isinstance(source, str), label + ": no source URL")
        url = urlsplit(source)
        demand(url.scheme == "https" and url.hostname == HOSTS[label]
               and url.username is None and url.password is None
               and url.port is None and bool(url.path) and not url.fragment,
               label + ": wrong source origin")
        demand(bool(str(axis.get("body", "")).strip()), label + ": missing body")
    return {"status": "PASS_SCOPED_STRUCTURE_ONLY", "axes": 8,
            "claim_allowed": False, "promotion": "HOLD"}


def check_documents(root=ROOT):
    names = [
        "README.md", "001_PONTEIRO/START_HERE.md", "LICENSE_POLICY.md",
        "LICENSES/SOFTWARE_LICENSE_DECISION.md",
        "LICENSES/LEGAL_INTERPRETATION_EIGHT_AREAS_V1.md",
        "docs/posdoc_estrutura/05_DOSSIE_JURIDICO_OITO_EIXOS_V1.md",
    ]
    docs = {}
    for name in names:
        path = root / name
        demand(path.is_file() and not path.is_symlink(), "missing: " + name)
        docs[name] = path.read_text(encoding="utf-8")
    license_path = root / "LICENSE"
    demand(license_path.is_file() and not license_path.is_symlink(),
           "missing historical license")
    demand(git_blob_sha(license_path.read_bytes()) == LICENSE_SHA1_BLOB,
           "historical LICENSE changed; requires separate review")
    readme = docs["README.md"]
    for needle in ("05_DOSSIE_JURIDICO_OITO_EIXOS_V1.md",
                   "LEGAL_INTERPRETATION_EIGHT_AREAS_V1.md",
                   "eight_axes_registry_v1.json", "claim_allowed=false"):
        demand(needle in readme, "README missing: " + needle)
    demand("parceria" in readme.casefold(), "README: non-affiliation absent")
    start = docs["001_PONTEIRO/START_HERE.md"]
    for needle in ("05_DOSSIE_JURIDICO_OITO_EIXOS_V1.md",
                   "LEGAL_INTERPRETATION_EIGHT_AREAS_V1.md"):
        demand(needle in start, "START_HERE missing: " + needle)
    demand("LEGAL_INTERPRETATION_EIGHT_AREAS_V1.md" in docs["LICENSE_POLICY.md"],
           "LICENSE_POLICY navigation missing")
    demand("TOKEN_VAZIO / DECISION_REQUIRED" in
           docs["LICENSES/SOFTWARE_LICENSE_DECISION.md"],
           "general software license silently promoted")
    explanatory = docs["LICENSES/LEGAL_INTERPRETATION_EIGHT_AREAS_V1.md"]
    demand("NO_NEW_GRANT" in explanatory and "PROMOTION=HOLD" in explanatory,
           "license interpretation has lost non-grant/HOLD")
    dossier = docs["docs/posdoc_estrutura/05_DOSSIE_JURIDICO_OITO_EIXOS_V1.md"]
    for number in range(1, 9):
        demand("Eixo " + str(number) in dossier, "dossier missing an axis")
    demand("claim_allowed=false" in dossier and "TOKEN_VAZIO" in dossier,
           "dossier lost epistemic boundaries")


if __name__ == "__main__":
    try:
        receipt = check_registry(load())
        check_documents()
        print(json.dumps(receipt, sort_keys=True))
    except (GateError, OSError, ValueError, json.JSONDecodeError) as error:
        print("FAIL_CLOSED: " + str(error), file=sys.stderr)
        raise SystemExit(1)
