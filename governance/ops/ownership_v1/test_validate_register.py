#!/usr/bin/env python3
import copy
import json
import unittest
from validate_register import (
    ALLOWED_FILES, GateError, HERE, validate, validate_diff, validate_p0_handoff, source_integrity, run
)
BASE=json.loads((HERE/"responsibility_register.json").read_text(encoding="utf-8"))
HANDOFF=json.loads((HERE/"p0_handoff_g02.json").read_text(encoding="utf-8"))
class Falsifiers(unittest.TestCase):
    def bad(self,fn):
        with self.assertRaises(GateError): fn()
    def mutate(self, fn):
        d=copy.deepcopy(BASE)
        fn(d)
        return d
    def test_valid_baseline(self): self.assertTrue(validate(BASE))
    def test_exact_source_hashes(self): self.assertTrue(source_integrity())
    def test_full_readback(self): self.assertIsNone(run())
    def test_fake_owner_without_authorization_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["records"][0].update(owner="Rafael Melo Reis"))))
    def test_fake_reviewer_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["records"][2].update(reviewer="Sample Counsel"))))
    def test_false_independent_reviewer_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["human_identity"].update(independent_reviewers_identified=True))))
    def test_false_counsel_opinion_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["source_claims"].update(licensed_country_opinions=6))))
    def test_fake_constitutional_certification_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["source_claims"].update(verified_constitutional_compliance_count=186))))
    def test_release_promotion_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d.update(release_allowed=True))))
    def test_legal_promotion_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d.update(legal_claim_allowed=True))))
    def test_security_compliance_promotion_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d.update(security_compliant_claim_allowed=True))))
    def test_p0_priority_downgrade_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["records"][0].update(priority="P2"))))
    def test_p0_absence_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["records"].pop(2))))
    def test_duplicate_record_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["records"].append(copy.deepcopy(d["records"][0])))))
    def test_fake_provider_gate_pass_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["records"][1].update(control_state="VERIFIED"))))
    def test_wrong_source_reference_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["records"][4].update(asset_ref="../secrets"))))
    def test_auto_assignment_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d.update(auto_assign_people=True))))
    def test_auto_contact_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d.update(auto_contact_people=True))))
    def test_fake_github_reviews_rejected(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["observed_merge_inventory"].update(github_reviews_observed=13))))
    def test_scope_gate_positive(self): self.assertTrue(validate_diff(sorted(ALLOWED_FILES)))
    def test_license_mutation_rejected(self):
        self.bad(lambda:validate_diff(sorted(ALLOWED_FILES|{"LICENSE"})))
    def test_provider_workflow_mutation_rejected(self):
        self.bad(lambda:validate_diff(sorted(ALLOWED_FILES|{".github/workflows/jekyll-gh-pages.yml"})))
    def test_missing_file_rejected(self):
        self.bad(lambda:validate_diff(sorted(ALLOWED_FILES-{"governance/ops/ownership_v1/README.md"})))
    def test_not_claiming_8_certified_translations(self):
        self.bad(lambda:validate(self.mutate(lambda d:d["source_claims"].update(qualified_translation_reviews=8))))
    def test_p0_handoff_source_state(self):
        self.assertTrue(validate_p0_handoff(HANDOFF))
    def test_g02_false_protection_pass_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["gates"][1]["observation_state"]="VERIFIED_PROTECTED"
        self.bad(lambda:validate_p0_handoff(d))
    def test_g02_403_as_security_evidence_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["source_endpoints"][1]["readback"]="OBSERVED_PROTECTED"
        self.bad(lambda:validate_p0_handoff(d))
    def test_g02_ruleset_empty_claim_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["source_endpoints"][2]["observation"]="[] means no protection anywhere"
        self.bad(lambda:validate_p0_handoff(d))
    def test_g02_readback_mutation_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["source_endpoints"][0]["observation"]="protected=true"
        self.bad(lambda:validate_p0_handoff(d))
    def test_admin_auto_assignment_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["gates"][0]["owner"]="rafaelmeloreisnovo"
        self.bad(lambda:validate_p0_handoff(d))
    def test_secret_receipt_forgery_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["gates"][0]["private_receipt_ref"]="approved"
        self.bad(lambda:validate_p0_handoff(d))
    def test_child_guardian_forgery_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["gates"][2]["owner_acceptance_ref"]="assumed"
        self.bad(lambda:validate_p0_handoff(d))
    def test_p0_release_flag_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["release_allowed"]=True
        self.bad(lambda:validate_p0_handoff(d))
    def test_p0_false_write_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["provider_write_performed"]=True
        self.bad(lambda:validate_p0_handoff(d))
    def test_p0_duplicate_gate_rejected(self):
        d=copy.deepcopy(HANDOFF)
        d["gates"][3]["gate"]="G03"
        self.bad(lambda:validate_p0_handoff(d))
if __name__=="__main__":unittest.main()
