#!/usr/bin/env python3
import copy
import json
import unittest
from validate_register import (
    ALLOWED_FILES, GateError, HERE, validate, validate_diff, source_integrity, run
)
BASE=json.loads((HERE/"responsibility_register.json").read_text(encoding="utf-8"))
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
if __name__=="__main__":unittest.main()
