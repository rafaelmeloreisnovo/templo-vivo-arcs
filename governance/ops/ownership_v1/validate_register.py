#!/usr/bin/env python3
"""Evidential human-responsibility register. Checks documentary shape, NOT real appointment."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
VOID="TOKEN_VAZIO"
P0={"R01","R02","R03","R04","R15"}
EXPECTED={f"R{x:02d}" for x in range(1,16)}
GATES={f"G{x:02d}" for x in range(1,10)}|{"L10N","JUR6","CONST186","CHAIN","NAV","LIVE"}
PINNED={
    "governance/legal/v10/REVIEW_REQUESTS.md":"748543f4ffe7c124e5163cca465fa934301b2311",
    "governance/security/v10/operational_facts_v10.json":"8938029743a49bf4169f4a3a6700998d5712e709",
    "governance/legal/i18n/v1/manifest.json":"fdee49944f829d1cba2bf16ea6ce7ac0145ddb23",
    "001_PONTEIRO/START_HERE.md":"ea7c4f44952b161ac8da75c63c1f738838088f62",
}
ALLOWED_FILES={
    "governance/ops/ownership_v1/README.md",
    "governance/ops/ownership_v1/responsibility_register.json",
    "governance/ops/ownership_v1/validate_register.py",
    "governance/ops/ownership_v1/test_validate_register.py",
    ".github/workflows/tvarcs-owner-review-v11.yml",
}
class GateError(ValueError): pass
def require(predicate, message):
    if not predicate: raise GateError(message)
def git_blob_sha(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode("ascii")+b"\0"+data).hexdigest()
def source_integrity():
    for path,hashv in PINNED.items():
        p=ROOT/path
        require(p.is_file(),"MISSING_SOURCE: "+path)
        require(git_blob_sha(p.read_bytes())==hashv,"SOURCE_DRIFT: "+path)
    return True
def validate(doc):
    require(doc.get("schema")=="TVARCS_OWNER_REVIEW_GATE_V1","schema")
    require(doc.get("producer_repo")=="rafaelmeloreisnovo/templo-vivo-arcs","authority")
    require(doc.get("provenance_sources")==PINNED,"sources")
    require(doc.get("main_at_observation")=="8b002de05dd01862b1f1ca7a2d3702afe06e4d9b","observed main")
    require(doc.get("historic_period_utc")==["2026-10-25T00:00:00Z","2026-10-31T00:00:00Z"],"period")
    mi=doc.get("observed_merge_inventory",{})
    require(mi.get("prs_merged")==[43,44,45,46,47,48,49,50,51,52,53,55] and mi.get("prs_not_merged")==[54],"PR audit")
    require(mi.get("github_reviews_observed")==0 and mi.get("observation_only") is True,"review evidence")
    claims=doc.get("source_claims",{})
    require(claims.get("verified_constitutional_compliance_count")==0 and claims.get("constitutional_target")==186,"constitutional false claim")
    require(claims.get("locale_versions")==8 and claims.get("qualified_translation_reviews")==0 and claims.get("licensed_country_opinions")==0,"legal review false claim")
    require(claims.get("security_controls_enforced") is False,"provider control not proven")
    for key in ("release_allowed","legal_claim_allowed","security_compliant_claim_allowed","auto_assign_people","auto_contact_people","auto_merge"):
        require(doc.get(key) is False,"unsafe flag "+key)
    require(doc.get("promotion")=="HOLD","promotion")
    identities=doc.get("human_identity",{})
    require(identities.get("declared_author")=="Rafael Melo Reis","declared attribution")
    require(identities.get("github_account")=="rafaelmeloreisnovo","account attribution")
    require(identities.get("identities_are_not_assignments") is True,"identity-role distinction")
    for key in ("verified_operational_owner","qualified_counsel_engaged","independent_reviewers_identified"):
        require(identities.get(key)==VOID,"invented human identity: "+key)
    st=doc.get("statuses",{})
    for k in ("human_assignment","independent_review","provider_enforcement"):
        require(st.get(k)==VOID,"status cannot be promoted")
    require(st.get("project_legal_certification")=="NOT_CERTIFIED","certification")
    records=doc.get("records")
    require(isinstance(records,list) and len(records)==15,"record count")
    ids=[r.get("id") for r in records if isinstance(r,dict)]
    require(set(ids)==EXPECTED and len(ids)==len(set(ids)),"missing/duplicate ID")
    require(set(x.get("gate") for x in records)==GATES,"gate coverage")
    for rec in records:
        id=rec["id"]
        require(rec.get("priority")==("P0" if id in P0 else "P2" if id=="R14" else "P1"),"priority drift: "+id)
        for key in ("area","requested_owner_role","acceptance_evidence_required","review_type"):
            require(isinstance(rec.get(key),str) and len(rec[key].strip())>=7,"missing description: "+id+":"+key)
        for key in ("owner","owner_authorization_ref","reviewer","reviewer_qualification_ref","reviewer_independent_from_owner","evidence_ref"):
            require(rec.get(key)==VOID,"unapproved assignment/evidence: "+id+":"+key)
        require(rec.get("gate") in GATES,"unknown gate")
        require(rec.get("control_state")=="UNVERIFIED","control not verified: "+id)
        require(rec.get("review_state")=="NOT_REVIEWED","review not evidenced: "+id)
        require(rec.get("source_state")=="SOURCE_PATH_OBSERVED","source state")
        require(rec.get("action_state")=="UNASSIGNED_HOLD" and rec.get("risk_retained") is True,"non-consensual risk promotion")
        a=rec.get("asset_ref","")
        require(isinstance(a,str) and a and not a.startswith("/") and ".." not in Path(a).parts and (ROOT/a).is_file(),"ungrounded asset: "+id)
    return True
def validate_diff(paths):
    require(len(paths)==len(set(paths)) and set(paths)==ALLOWED_FILES,"unexpected or missing files; no license/provider/main mutations")
    return True
def run():
    source_integrity()
    doc=json.loads((HERE/"responsibility_register.json").read_text(encoding="utf-8"))
    validate(doc)
    print("PASS: exact source blobs, 15 gated areas, 5 P0 retained, all human slots TOKEN_VAZIO, false-approval gates")
    print("LEGAL_STATUS=HOLD | PROVIDER_ENFORCEMENT=TOKEN_VAZIO | CLAIM_ALLOWED=false")
if __name__=="__main__":
    run()
