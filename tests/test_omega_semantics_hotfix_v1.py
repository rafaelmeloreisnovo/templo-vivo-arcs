"""Ω00–Ω15 adversarial hotfix: all claims fail-closed; original spellings preserved.

The 16 seeds are a bounded PUBLIC/SANITIZED lexical sample from the user's
symbolic Ω00..Ω15 message, NOT a claim about physical objects or translations.
No production runtime, legal policy, licensing or child safeguarding is changed.
"""
import copy
import json
import sys
import unicodedata
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/audit"))
from omega_semantics_hotfix_v1 import (  # noqa: E402
    MISSING, SOURCE_REF, SemanticGateError, observe, verify_cases
)

CASES = json.loads(r'''[
  {
    "id": "Ω00",
    "literal": "molho",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Homônimo isolado não demonstra alimento, feixe ou ação verbal.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω01",
    "literal": "molho de chaves",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Contexto lexical não comprova existência de chaves ou fechadura.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω02",
    "literal": "0x00",
    "expected_kind": "HEX_NOTATION_TEXT_NOT_BYTES",
    "falsifier": "A notação 0x00 não é byte NUL nem variável inicializada.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω03",
    "literal": "ש + 空 + λ + molho_de_lenha",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Escritas distintas não autorizam tradução ou execução.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω04",
    "literal": "∅",
    "expected_kind": "SYMBOLIC_EMPTY",
    "falsifier": "Símbolo ∅ não equivale a None, zero ou string vazia.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω05",
    "literal": "антиреверс",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Palavra transliterada não confirma operação de rollback.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω06",
    "literal": "{aborto:antes} ↔ {depois:reverso}",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Notação antes/depois não prova reversibilidade de ação.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω07",
    "literal": "molho",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "O mesmo lexema noutro contexto não é uma identidade semântica.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω08",
    "literal": "τ³ ⊗ あ ⊗ Ω ⊗ ก ⊗ ∅",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Operadores e ideogramas não provam cálculo nem semântica.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω09",
    "literal": "    ",
    "expected_kind": "WHITESPACE_ONLY",
    "falsifier": "Quatro espaços não podem ser colapsados em string vazia.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω10",
    "literal": "código de tomate",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Texto sobre tomate não demonstra abertura de fechadura.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω11",
    "literal": "panela sem panela",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Contradição textual não comprova um objeto ausente.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω12",
    "literal": "reversão de uma origem que nunca existiu",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Não criar fonte histórica para sustentar reversão impossível.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω13",
    "literal": "[ruído][ruído][verdade?][ruído]",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Padrão ruído/verdade? não estabelece veracidade externa.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω14",
    "literal": "𓂀",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Um glifo não demonstra sua origem, autoria ou tradução.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  },
  {
    "id": "Ω15",
    "literal": "token_abortado",
    "expected_kind": "TEXT_LITERAL_UNINTERPRETED",
    "falsifier": "Token abortado não demonstra exclusão, erro ou restauração.",
    "source_ref": "USER_PROMPT_OMEGA00_OMEGA15_20261105",
    "evidence_status": "USER_INPUT_ONLY",
    "semantic_status": "TOKEN_VAZIO_CONTEXT",
    "forecast_status": "TOKEN_VAZIO_FORECAST",
    "claim_allowed": false
  }
]''')


class OmegaAmbiguityHotfixTests(unittest.TestCase):
    def test_complete_16_seed_registry(self):
        receipt = verify_cases(copy.deepcopy(CASES))
        self.assertEqual(receipt["cases"], 16)
        self.assertFalse(receipt["claim_allowed"])
        self.assertEqual(receipt["forecast_accuracy"], "TOKEN_VAZIO_FORECAST")

    def test_empty_null_absent_zero_are_distinct(self):
        tokens = [MISSING, None, "", "    ", "∅", 0, False, "TOKEN_VAZIO"]
        kinds = [observe(x)["kind"] for x in tokens]
        self.assertEqual(len(set(kinds)), len(tokens))

    def test_lexeme_hex_is_not_actual_nul(self):
        self.assertEqual(observe("0x00")["kind"], "HEX_NOTATION_TEXT_NOT_BYTES")
        self.assertEqual(observe("\x00")["kind"], "CONTROL_TEXT_NOT_NULL")
        self.assertNotEqual(observe("0x00")["utf8_sha256"],
                            observe("\x00")["utf8_sha256"])

    def test_whitespace_has_four_codepoints(self):
        observation = observe("    ")
        self.assertEqual(observation["bytes"], 4)
        self.assertEqual(observation["codepoints"], 4)
        self.assertEqual(observation["raw"], "    ")
        self.assertNotEqual(observation["utf8_sha256"], observe("")["utf8_sha256"])

    def test_unknown_is_not_missing(self):
        self.assertNotEqual(observe("TOKEN_VAZIO")["kind"], observe()["kind"])
        self.assertNotEqual(observe("∅")["kind"], observe(None)["kind"])

    def test_preserve_multiscript_bytes(self):
        token = "ש + 空 + λ + τ³ ⊗ あ ⊗ ก ⊗ ∅"
        observation = observe(token)
        self.assertEqual(observation["raw"], token)
        self.assertEqual(observation["codepoints"], len(token))
        self.assertEqual(observation["raw"].encode().decode(), token)

    def test_no_silent_unicode_nfc(self):
        composed, decomposed = "ç", "c\u0327"
        self.assertEqual(unicodedata.normalize("NFC", composed),
                         unicodedata.normalize("NFC", decomposed))
        self.assertNotEqual(observe(composed)["utf8_sha256"],
                            observe(decomposed)["utf8_sha256"])

    def test_phoneme_variants_stay_distinct(self):
        variants = ("c", "ss", "ç", "z", "sh", "x")
        hashes = [observe(word)["utf8_sha256"] for word in variants]
        self.assertEqual(len(set(hashes)), len(variants))
        for word in variants:
            self.assertEqual(observe(word)["meaning"], "TOKEN_VAZIO_CONTEXT")

    def test_duplicate_literal_with_separate_case_ids_allowed(self):
        self.assertEqual(CASES[0]["literal"], CASES[7]["literal"])
        self.assertNotEqual(CASES[0]["id"], CASES[7]["id"])
        self.assertEqual(verify_cases(CASES)["cases"], 16)

    def test_duplicate_id_rejected(self):
        x = copy.deepcopy(CASES)
        x[7]["id"] = x[0]["id"]
        with self.assertRaises(SemanticGateError):
            verify_cases(x)

    def test_missing_case_rejected(self):
        with self.assertRaises(SemanticGateError):
            verify_cases(copy.deepcopy(CASES)[:-1])

    def test_untrusted_source_cannot_promote(self):
        x = copy.deepcopy(CASES)
        x[13]["source_ref"] = "TRUSTED_ORIGIN"
        with self.assertRaises(SemanticGateError):
            verify_cases(x)

    def test_pseudo_evidence_cannot_be_execution(self):
        x = copy.deepcopy(CASES)
        x[10]["evidence_status"] = "PROVEN_PHYSICAL_EFFECT"
        with self.assertRaises(SemanticGateError):
            verify_cases(x)

    def test_meaning_without_context_cannot_be_approved(self):
        x = copy.deepcopy(CASES)
        x[1]["semantic_status"] = "KEYS_EXIST_PROVEN"
        with self.assertRaises(SemanticGateError):
            verify_cases(x)

    def test_prediction_without_calibration_rejected(self):
        x = copy.deepcopy(CASES)
        x[2]["forecast_status"] = "PREDICTS_WITH_99_PERCENT_PRECISION"
        with self.assertRaises(SemanticGateError):
            verify_cases(x)

    def test_claim_escalation_rejected(self):
        x = copy.deepcopy(CASES)
        x[14]["claim_allowed"] = True
        with self.assertRaises(SemanticGateError):
            verify_cases(x)

    def test_joint_mutation_of_literal_and_type_still_rejected(self):
        rowset = copy.deepcopy(CASES)
        rowset[9]["literal"] = "changed literal"
        rowset[9]["expected_kind"] = "TEXT_LITERAL_UNINTERPRETED"
        with self.assertRaises(SemanticGateError):
            verify_cases(rowset)

    def test_four_space_seed_tamper_rejected(self):
        x = copy.deepcopy(CASES)
        x[9]["literal"] = ""
        with self.assertRaises(SemanticGateError):
            verify_cases(x)

    def test_float_zero_not_integer_zero(self):
        self.assertNotEqual(observe(0.0)["kind"], observe(0)["kind"])

    def test_nonfinite_number_fail_closed(self):
        with self.assertRaises(SemanticGateError):
            observe(float("nan"))

    def test_receipt_is_serializable(self):
        receipt = verify_cases(CASES)
        self.assertEqual(json.loads(json.dumps(receipt))["scope"],
                         "USER_INPUT_LITERAL_STRUCTURE_ONLY")

    def test_no_auto_publication_semantic_or_forecast(self):
        receipt = verify_cases(CASES)
        self.assertEqual(receipt["promotion"], "HOLD")
        self.assertEqual(receipt["semantic_truth"], "TOKEN_VAZIO_CONTEXT")
        for row in CASES:
            self.assertFalse(observe(row["literal"])["claim_allowed"])


def make_literal_test(index):
    def test(self):
        row = CASES[index]
        actual = observe(row["literal"])
        self.assertEqual(actual["raw"], row["literal"])
        self.assertEqual(actual["kind"], row["expected_kind"])
        self.assertEqual(actual["meaning"], "TOKEN_VAZIO_CONTEXT")
        self.assertFalse(actual["claim_allowed"])
    return test


for _i in range(16):
    setattr(OmegaAmbiguityHotfixTests,
            f"test_omega{_i:02d}_literal_preserved", make_literal_test(_i))


if __name__ == "__main__":
    unittest.main()
