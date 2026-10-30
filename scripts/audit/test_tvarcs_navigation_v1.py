#!/usr/bin/env python3
"""Adversarial tests for Templo Vivo route graph; never certify legal compliance."""
import copy
import json
import pathlib
import unittest
from validate_tvarcs_navigation_v1 import SOURCE, ROOT, validate

class NavigationFalsifiers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(SOURCE.read_text(encoding="utf-8"))
    def check_invalid(self, change):
        d = copy.deepcopy(self.base)
        change(d)
        self.assertTrue(validate(d, ROOT), "false PASS on adversarial mutation")
    def test_valid_scope_only(self):
        self.assertEqual([], validate(self.base, ROOT))
    def test_sovereignty_elevation(self):
        self.check_invalid(lambda d: d.__setitem__("sovereignty_claim_allowed", True))
    def test_claim_elevation(self):
        self.check_invalid(lambda d: d.__setitem__("claim_allowed", True))
    def test_disguised_pass(self):
        self.check_invalid(lambda d: d.__setitem__("promotion", "PASS"))
    def test_duplicate_node(self):
        self.check_invalid(lambda d: d["nodes"].append(copy.deepcopy(d["nodes"][0])))
    def test_orphan_node(self):
        self.check_invalid(lambda d: d["nodes"].append({"id":"orphan","path":"SECURITY.md","status":"HOLD","domain":"SAFETY"}))
    def test_missing_file(self):
        self.check_invalid(lambda d: d["nodes"][0].__setitem__("path","001_PONTEIRO/MISSING.md"))
    def test_path_traversal(self):
        self.check_invalid(lambda d: d["nodes"][0].__setitem__("path","../../secrets"))
    def test_unknown_edge(self):
        self.check_invalid(lambda d: d["edges"].append({"from":"start","to":"unknown","type":"NAVIGATES"}))
    def test_remove_child_safety(self):
        self.check_invalid(lambda d: d["priority_gates"].remove("G03"))
    def test_erase_boundary(self):
        self.check_invalid(lambda d: d["invariants"].remove("DIGITAL_INFRASTRUCTURE != TERRITORIAL_SOVEREIGNTY"))
    def test_wrong_adverse_expectation(self):
        self.check_invalid(lambda d: d["adversarial_checks"][0].__setitem__("expected","YES"))
    def test_unbounded_depth(self):
        self.check_invalid(lambda d: d.__setitem__("default_depth", 100))
    def test_status_legal_certified(self):
        self.check_invalid(lambda d: d["nodes"][0].__setitem__("status", "LEGAL_CERTIFIED"))

if __name__ == "__main__":
    unittest.main()
