"""Falsifiers for evidence promotion, dependency handling and append-only custody."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/audit/check_append_only.py"
spec = importlib.util.spec_from_file_location("omega", ROOT / "scripts/audit/omega_pipeline.py")
omega = importlib.util.module_from_spec(spec)
spec.loader.exec_module(omega)


class AppendOnlyFalsifiers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Test fixture")
        self.git("config", "user.email", "test@example.invalid")
        self.path = self.root / "ledger.jsonl"
        self.path.write_bytes(b'{"id":"0001123"}\n{"id":"second"}\n')
        self.git("add", ".")
        self.git("commit", "-qm", "fixture baseline")
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, stderr=subprocess.DEVNULL, text=True)

    def check(self, base=None):
        return subprocess.run([sys.executable, str(SCRIPT), base or self.base, "ledger.jsonl"],
                              cwd=self.root, capture_output=True, text=True)

    def test_invalid_base_is_failure_not_new_ledger(self):
        self.assertEqual(self.check("0" * 40).returncode, 2)

    def test_existing_bytes_pass(self):
        self.assertEqual(self.check().returncode, 0)

    def test_append_new_record_passes(self):
        with self.path.open("ab") as stream:
            stream.write(b'{"id":"third"}\n')
        self.assertEqual(self.check().returncode, 0)

    def test_zero_prefix_is_identity_and_must_not_be_normalized(self):
        self.path.write_bytes(self.path.read_bytes().replace(b'0001123', b'1123'))
        self.assertNotEqual(self.check().returncode, 0)

    def test_reordering_rejected(self):
        self.path.write_bytes(b'{"id":"second"}\n{"id":"0001123"}\n')
        self.assertNotEqual(self.check().returncode, 0)

    def test_line_ending_rewrite_rejected(self):
        self.path.write_bytes(self.path.read_bytes().replace(b'\n', b'\r\n'))
        self.assertNotEqual(self.check().returncode, 0)

    def test_deletion_rejected(self):
        self.path.unlink()
        self.assertEqual(self.check().returncode, 2)

    def test_genuinely_new_ledger_requires_valid_base(self):
        self.git("rm", "-q", "ledger.jsonl")
        self.git("commit", "-qm", "fixture without ledger")
        base = self.git("rev-parse", "HEAD").strip()
        self.path.write_bytes(b'{"id":"new"}\n')
        self.assertEqual(self.check(base).returncode, 0)

    def test_unterminated_record_cannot_be_appended_in_place(self):
        self.path.write_bytes(b'{"id":"old"}')
        self.git("add", ".")
        self.git("commit", "-qm", "unterminated fixture")
        base = self.git("rev-parse", "HEAD").strip()
        self.path.write_bytes(b'{"id":"old"}\n{"id":"new"}\n')
        self.assertNotEqual(self.check(base).returncode, 0)


class PipelineFalsifiers(unittest.TestCase):
    def setUp(self):
        self.contract = omega.read_json(ROOT / "governance/omega-pipeline.v1.json")

    def test_contract_is_valid(self):
        omega.validate_contract(self.contract)

    def test_claim_promotion_rejected(self):
        self.contract["claim_allowed"] = True
        with self.assertRaises(ValueError):
            omega.validate_contract(self.contract)

    def test_missing_gate_rejected(self):
        self.contract["gates"].pop()
        with self.assertRaises(ValueError):
            omega.validate_contract(self.contract)

    def test_cycle_rejected(self):
        self.contract["gates"][0]["needs"] = ["rollback"]
        with self.assertRaises(ValueError):
            omega.validate_contract(self.contract)

    def test_failure_blocks_dependents_but_keeps_independent_exam(self):
        called = []
        def execute(key):
            called.append(key)
            if key == "provenance":
                raise ValueError("missing bytes")
            return {"verified": key}
        result = {row["id"]: row for row in omega.schedule(self.contract["gates"], execute)}
        self.assertEqual(result["provenance"]["status"], "FAIL")
        self.assertEqual(result["custody"]["status"], "BLOCKED")
        self.assertEqual(result["reproduction"]["status"], "BLOCKED")
        self.assertEqual(result["uncertainty"]["status"], "PASS")
        self.assertNotIn("custody", called)
        self.assertTrue(all(row["claim_allowed"] is False for row in result.values()))

    def test_missing_legacy_exam_rejected(self):
        routes = omega.read_json(ROOT / "governance/omega-exams.v1.json")
        legacy = omega.read_json(ROOT / "evidence/custody/gaps/gap-router.v1.json")
        omega.validate_routes(routes, legacy)
        routes["exams"].pop(0)
        with self.assertRaises(ValueError):
            omega.validate_routes(routes, legacy)

    def test_duplicate_json_key_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"claim_allowed":true,"claim_allowed":false}', object_pairs_hook=omega.unique_keys)

    def test_malformed_input_still_emits_failure_receipt(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "governance").mkdir()
            (root / "governance/omega-pipeline.v1.json").write_text('{broken')
            out = root / "output"
            self.assertEqual(omega.run(root, out, "0" * 40, "0" * 40), 1)
            receipt = omega.read_json(out / "receipt.json")
            self.assertEqual(receipt["pipeline_status"], "FAIL_CLOSED")
            self.assertFalse(receipt["claim_allowed"])
            self.assertEqual(len(receipt["gates"]), 7)
            self.assertTrue((out / "SHA256SUMS").is_file())
            with self.assertRaises(FileExistsError):
                omega.run(root, out, "0" * 40, "0" * 40)

    def test_nonzero_command_and_timeout_preserve_logs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            audit = omega.Audit(root, root, "0" * 40, "0" * 40, "unused")
            with self.assertRaises(RuntimeError):
                audit.command([sys.executable, "-c", "import sys; print('failure witness'); sys.exit(9)"])
            self.assertEqual(audit.commands[-1]["exit_code"], 9)
            self.assertIn(b"failure witness", (root / "01.stdout.log").read_bytes())
            with self.assertRaises(RuntimeError):
                audit.command([sys.executable, "-c", "import time; time.sleep(5)"], timeout=0.1)
            self.assertEqual(audit.commands[-1]["status"], "TIMEOUT")
            self.assertEqual(audit.commands[-1]["stderr_sha256"], omega.digest(b""))

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            omega.checked_path(ROOT, "../outside")

    def test_receipt_manifest_binds_final_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            omega.write_bundle(out, {"pipeline_status":"FAIL_CLOSED","source_sha":"TOKEN_VAZIO",
                                    "gates":[],"F_next":[]})
            for line in (out / "SHA256SUMS").read_text().splitlines():
                expected, name = line.split("  ")
                self.assertEqual(expected, omega.digest((out / name).read_bytes()))


if __name__ == "__main__":
    unittest.main()
