"""Adversarial tests; success does not validate real-world provider controls."""
import copy
import json
import pathlib
import unittest

from check_readiness import validate

SOURCE = pathlib.Path(__file__).with_name("readiness_v1.json")


class ReadinessTests(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(SOURCE.read_text(encoding="utf-8"))

    def fails(self, mutate):
        sample = copy.deepcopy(self.doc)
        mutate(sample)
        with self.assertRaises(ValueError):
            validate(sample)

    def test_valid_hold(self):
        self.assertTrue(validate(self.doc))

    def test_false_release(self):
        self.fails(lambda d: d.update(release_allowed=True))

    def test_false_claim(self):
        self.fails(lambda d: d.update(claim_allowed=True))

    def test_false_promotion(self):
        self.fails(lambda d: d.update(status="APPROVED"))

    def test_missing_gate(self):
        self.fails(lambda d: d["gates"].pop())

    def test_duplicate_gate(self):
        self.fails(lambda d: d["gates"].__setitem__(1, copy.deepcopy(d["gates"][0])))

    def test_severity_downgrade(self):
        self.fails(lambda d: d["gates"][0].update(priority="P1"))

    def test_false_verified_without_receipt(self):
        self.fails(lambda d: d["gates"][0].update(state="VERIFIED"))

    def test_invalid_state(self):
        self.fails(lambda d: d["gates"][0].update(state="PASS"))

    def test_schema_drift(self):
        self.fails(lambda d: d.update(schema="TVARCS_SECURITY_READINESS_V2"))

    def test_extra_key(self):
        self.fails(lambda d: d.update(unreviewed_grant=True))

    def test_empty_topic(self):
        self.fails(lambda d: d["gates"][0].update(topic=""))


if __name__ == "__main__":
    unittest.main()
