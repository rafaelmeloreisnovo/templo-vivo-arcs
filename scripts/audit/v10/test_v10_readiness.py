#!/usr/bin/env python3
"""Adversarial tests against false closure; no external services."""
import copy
import json
import unittest
from validate_v10_readiness import PATH, validate

class SafetyGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ground = json.loads(PATH.read_text(encoding="utf-8"))
    def mutate(self, fn):
        x = copy.deepcopy(self.ground)
        fn(x)
        self.assertTrue(validate(x), "false PASS escaped fail-closed validator")
    def test_baseline(self):
        self.assertEqual([], validate(self.ground))
    def test_release_true(self):
        self.mutate(lambda x: x.__setitem__("release_allowed", True))
    def test_legal_claim_true(self):
        self.mutate(lambda x: x.__setitem__("legal_claim_allowed", True))
    def test_operational_claim_true(self):
        self.mutate(lambda x: x.__setitem__("operational_controls_claim_allowed", True))
    def test_false_promotion(self):
        self.mutate(lambda x: x.__setitem__("promotion", "PASS"))
    def test_drop_p0(self):
        self.mutate(lambda x: x["p0_gates"].pop())
    def test_false_provider_evidence(self):
        self.mutate(lambda x: x["p0_gates"][1].__setitem__("evidence_ref", "fake"))
    def test_claim_security_owner(self):
        self.mutate(lambda x: x["p0_gates"][2].__setitem__("owner", "unknown-owner"))
    def test_fake_live_site(self):
        self.mutate(lambda x: x["real_world_operations"][-1].__setitem__("observation", "SOURCE_OBSERVED"))
    def test_replace_observation_ids(self):
        self.mutate(lambda x: x["real_world_operations"][0].__setitem__("id", "OP06"))
    def test_remove_country(self):
        self.mutate(lambda x: x["jurisdiction_review"].pop())
    def test_invent_lawyer(self):
        self.mutate(lambda x: x["jurisdiction_review"][0].__setitem__("counsel", "approved"))
    def test_fake_country_certification(self):
        self.mutate(lambda x: x["jurisdiction_review"][0].__setitem__("legal_status", "CERTIFIED"))
    def test_downgrade_release_gate(self):
        self.mutate(lambda x: x["release_predicate"].__setitem__("never_promote_from_ci_alone", False))

if __name__ == "__main__":
    unittest.main()
