import copy
import json
import pathlib
import unittest
from validate_sources import check

D=json.loads((pathlib.Path(__file__).parent/"constitutional_sources.json").read_text(encoding="utf-8"))

class ConstitutionRegisterTests(unittest.TestCase):
    def test_fixture(self): self.assertTrue(check(copy.deepcopy(D)))
    def test_cannot_claim(self):
        x=copy.deepcopy(D); x["claim_allowed"]=True
        with self.assertRaises(AssertionError): check(x)
    def test_no_fabricated_certifications(self):
        x=copy.deepcopy(D); x["verified_sovereign_constitutions_full"]=186
        with self.assertRaises(AssertionError): check(x)
    def test_scotland_not_sovereign(self):
        x=copy.deepcopy(D); x["jurisdictions"][-1]["classification"]="sovereign"
        with self.assertRaises(AssertionError): check(x)
    def test_missing_source(self):
        x=copy.deepcopy(D); x["jurisdictions"][0]["source_url"]=""
        with self.assertRaises(AssertionError): check(x)
    def test_dedup(self):
        x=copy.deepcopy(D); x["jurisdictions"][-1]["code"]="BR"
        with self.assertRaises(AssertionError): check(x)
    def test_mexico_present_exactly_once(self):
        self.assertEqual([j["code"] for j in D["jurisdictions"]].count("MX"), 1)
        x=copy.deepcopy(D)
        x["jurisdictions"]=[j for j in x["jurisdictions"] if j["code"]!="MX"]
        with self.assertRaises(AssertionError): check(x)
    def test_mexico_cannot_be_promoted(self):
        x=copy.deepcopy(D)
        next(j for j in x["jurisdictions"] if j["code"]=="MX")["article_text"]="artigo supostamente verificado"
        with self.assertRaises(AssertionError): check(x)
    def test_no_auto_license(self):
        x=copy.deepcopy(D); x["license_change"]=True
        with self.assertRaises(AssertionError): check(x)
    def test_fail_open_review(self):
        x=copy.deepcopy(D); x["promotion"]="APPROVED"
        with self.assertRaises(AssertionError): check(x)
    def test_unsupported_case_law(self):
        x=copy.deepcopy(D); x["jurisdictions"][0]["judicial_enforceability"]="PASS"
        with self.assertRaises(AssertionError): check(x)

if __name__=="__main__": unittest.main()
