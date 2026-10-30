import copy
import json
import pathlib
import unittest
from validate_i18n import (
    ALLOWED, HERE, LOCALES, changed_files_allowed, clauses, run, validate_manifest,
    validate_translation, verify_english_reference,
)

DATA=json.loads((HERE/"manifest.json").read_text(encoding="utf-8"))
PT=(HERE/"pt-BR.md").read_text(encoding="utf-8")
JA=(HERE/"ja-JP.md").read_text(encoding="utf-8")
ZH=(HERE/"zh-CN.md").read_text(encoding="utf-8")
class TranslationFalsifiers(unittest.TestCase):
    def broken(self,fn):
        with self.assertRaises(AssertionError): fn()
    def test_full_registered_gate(self): self.assertTrue(run())
    def test_english_exact_source_parity(self): self.assertTrue(verify_english_reference())
    def test_all_locales(self):
        for loc in LOCALES:
            self.assertTrue(validate_translation(loc,(HERE/(loc+".md")).read_text(encoding="utf-8")))
    def test_removed_clause_rejected(self):
        self.broken(lambda: validate_translation("pt-BR",PT.replace("### POLICY P09","### POLICY P08")))
    def test_duplicate_clause_rejected(self):
        self.broken(lambda: validate_translation("pt-BR",PT.replace("### PROPRIETARY L11","### PROPRIETARY L10")))
    def test_empty_clause_rejected(self):
        out=PT.replace(clauses(PT,"PROPRIETARY")[0][1], "x")
        self.broken(lambda: validate_translation("pt-BR",out))
    def test_unsupported_grant_flag_rejected(self):
        self.broken(lambda:validate_translation("pt-BR",PT.replace("NEW_GRANT=false","NEW_GRANT=true")))
    def test_unsupported_legal_certification_rejected(self):
        x=copy.deepcopy(DATA);x["certified_legal_translation"]=True
        self.broken(lambda:validate_manifest(x))
    def test_forced_promotion_rejected(self):
        x=copy.deepcopy(DATA);x["promotion"]="APPROVED"
        self.broken(lambda:validate_manifest(x))
    def test_missing_legal_review_gap_rejected(self):
        x=copy.deepcopy(DATA);x["per_locale"]["ja-JP"]["human_legal_review"]="APPROVED"
        self.broken(lambda:validate_manifest(x))
    def test_source_blob_mismatch_rejected(self):
        self.broken(lambda:validate_translation("pt-BR",PT.replace("6e83eca92b4546ad5006efc08aaa5abd7114b41c","0"*40)))
    def test_untranslated_placeholder_rejected(self):
        self.broken(lambda:validate_translation("pt-BR",PT.replace("Aplica-se somente","TODO TRANSLATE Aplica-se somente")))
    def test_japanese_script_missing_rejected(self):
        damaged="".join("x" if ("\\u3040"<=c<="\\u9fff") else c for c in JA)
        self.broken(lambda:validate_translation("ja-JP",damaged))
    def test_chinese_script_missing_rejected(self):
        self.broken(lambda:validate_translation("zh-CN",ZH.translate(str.maketrans({c:"x" for c in set(ZH) if "\u4e00"<=c<="\u9fff"}))))
    def test_license_root_mutation_rejected(self):
        self.broken(lambda:changed_files_allowed(list(ALLOWED)+["LICENSE"]))
    def test_wrong_file_scope_rejected(self):
        self.broken(lambda:changed_files_allowed(list(ALLOWED)+["android/app/src/AndroidManifest.xml"]))
    def test_missing_expected_file_rejected(self):
        self.broken(lambda:changed_files_allowed(list(ALLOWED)[:-1]))
    def test_all_and_only_expected_files(self): self.assertTrue(changed_files_allowed(sorted(ALLOWED)))

if __name__=="__main__": unittest.main()
