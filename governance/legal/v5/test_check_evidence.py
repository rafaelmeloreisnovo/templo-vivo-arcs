#!/usr/bin/env python3
"""Negative/falsification tests for the TVARCS research-only legal gate."""
import copy
import json
import unittest
from pathlib import Path

from check_evidence import check_changed_files, check_data, validate_file

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "evidence_register.json").read_text(encoding="utf-8"))


class LegalGateTests(unittest.TestCase):
    def clone(self):
        return copy.deepcopy(DATA)

    def test_00_verified_fixture(self):
        result = validate_file(ROOT / "evidence_register.json")
        self.assertEqual(result["status"], "PASS_SCOPED_RESEARCH_ONLY")
        self.assertGreaterEqual(result["case_records"], 13)
        self.assertEqual(result["claim_allowed"], False)
        self.assertEqual(len(result["sha256_register"]), 64)

    def test_01_false_legal_claim_fails(self):
        x = self.clone()
        x["claim_allowed"] = True
        with self.assertRaisesRegex(ValueError, "promotion forbidden"):
            check_data(x)

    def test_02_auto_penalty_fails(self):
        x = self.clone()
        x["sanctions"][0]["applied"] = True
        with self.assertRaisesRegex(ValueError, "sanction asserted"):
            check_data(x)

    def test_03_unmeasured_is_not_zero(self):
        x = self.clone()
        x["service_facts"]["personal_data_processing"] = "0"
        with self.assertRaisesRegex(ValueError, "falsely promoted"):
            check_data(x)

    def test_04_duplicate_case_fails(self):
        x = self.clone()
        x["cases"][1]["id"] = x["cases"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            check_data(x)

    def test_05_untrusted_case_source_fails(self):
        x = self.clone()
        x["cases"][0]["source_url"] = "https://example.com/fiction"
        with self.assertRaisesRegex(ValueError, "invalid case URL"):
            check_data(x)

    def test_06_missing_adverse_authority_fails(self):
        x = self.clone()
        x["cases"][0]["adverse_limit"] = ""
        with self.assertRaisesRegex(ValueError, "missing material"):
            check_data(x)

    def test_07_false_fully_reviewed_case_fails(self):
        x = self.clone()
        x["cases"][0]["pinpoint_verified"] = True
        with self.assertRaisesRegex(ValueError, "case promoted"):
            check_data(x)

    def test_08_retroactive_license_change_blocked(self):
        with self.assertRaisesRegex(ValueError, "out-of-scope"):
            check_changed_files(["LICENSE_POLICY.md"])

    def test_09_source_change_blocked(self):
        with self.assertRaisesRegex(ValueError, "out-of-scope"):
            check_changed_files(["README.md"])

    def test_10_limited_changes_allowed(self):
        check_changed_files(["governance/legal/v5/README.md",
                             "governance/legal/v5/evidence_register.json"])

    def test_11_unverified_protection_pass_fails(self):
        x = self.clone()
        x["service_facts"]["branch_protection"] = "PASS"
        with self.assertRaisesRegex(ValueError, "provider promotion"):
            check_data(x)

    def test_12_missing_child_safeguard_fails(self):
        x = self.clone()
        del x["controls"]["minor_protection"]
        with self.assertRaisesRegex(ValueError, "non-regression"):
            check_data(x)

    def test_13_historical_state_must_be_current(self):
        x = self.clone()
        x["historical_prs"]["PR47"] = "DRAFT"
        with self.assertRaisesRegex(ValueError, "historical PR"):
            check_data(x)

    def test_14_sanction_scope_fails_closed(self):
        x = self.clone()
        x["sanctions"][0]["scope"] = "APPLICABLE"
        with self.assertRaisesRegex(ValueError, "sanction asserted"):
            check_data(x)


if __name__ == "__main__":
    unittest.main(verbosity=2)
