"""Adversarial scope-limited tests for the Templo Vivo eight-axis legal registry."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/audit"))
from validate_tvarcs_legal_v12 import (  # noqa: E402
    GateError, check_documents, check_registry, git_blob_sha, load,
    unique_pairs, LICENSE_SHA1_BLOB,
)


class EightAxisGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = load()

    def mutation(self):
        return copy.deepcopy(self.original)

    def rejected(self, obj):
        with self.assertRaises(GateError):
            check_registry(obj)

    def test_01_valid_structure_only(self):
        result = check_registry(self.mutation())
        self.assertEqual(result["axes"], 8)
        self.assertFalse(result["claim_allowed"])
        self.assertEqual(result["status"], "PASS_SCOPED_STRUCTURE_ONLY")

    def test_02_readme_routes_and_historical_license(self):
        check_documents()
        self.assertEqual(git_blob_sha((ROOT / "LICENSE").read_bytes()),
                         LICENSE_SHA1_BLOB)

    def test_03_global_claim_escalation(self):
        row = self.mutation()
        row["claim_allowed"] = True
        self.rejected(row)

    def test_04_new_license_without_grant(self):
        row = self.mutation()
        row["license_change"] = True
        self.rejected(row)

    def test_05_fabricated_child_safety_approval(self):
        row = self.mutation()
        row["child_safety_gate"] = "PASS"
        self.rejected(row)

    def test_06_fabricated_human_legal_review(self):
        row = self.mutation()
        row["human_legal_reviewer"] = "SIGNED"
        self.rejected(row)

    def test_07_missing_axis(self):
        row = self.mutation()
        row["axes"].pop()
        self.rejected(row)

    def test_08_duplicate_axis(self):
        row = self.mutation()
        row["axes"][1]["id"] = row["axes"][0]["id"]
        self.rejected(row)

    def test_09_per_axis_claim_escalation(self):
        row = self.mutation()
        row["axes"][1]["claim_allowed"] = True
        self.rejected(row)

    def test_10_source_is_not_a_test_receipt(self):
        row = self.mutation()
        row["axes"][1]["evidence"] = "OPERATIONAL_PASS"
        self.rejected(row)

    def test_11_jurisdiction_cannot_be_inferred(self):
        row = self.mutation()
        row["axes"][4]["application"] = "GLOBAL_COMPLIANT"
        self.rejected(row)

    def test_12_no_invented_expert(self):
        row = self.mutation()
        row["axes"][1]["qualified_review"] = "APPROVED"
        self.rejected(row)

    def test_13_hostname_spoofing(self):
        row = self.mutation()
        row["axes"][1]["source"] = (
            "https://www.unicef.org.attacker.example/child-rights-convention")
        self.rejected(row)

    def test_14_http_downgrade(self):
        row = self.mutation()
        row["axes"][1]["source"] = "http://www.unicef.org/child-rights"
        self.rejected(row)

    def test_15_duplicate_json_key(self):
        with self.assertRaises(GateError):
            unique_pairs([("claim_allowed", False), ("claim_allowed", True)])

    def test_16_historical_license_tamper_detector(self):
        self.assertNotEqual(git_blob_sha(b"tampered LICENSE"), LICENSE_SHA1_BLOB)


if __name__ == "__main__":
    unittest.main()
