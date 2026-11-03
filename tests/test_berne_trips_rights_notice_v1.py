"""Scoped documentary checks for Berne/TRIPS rights-reservation notice.

This test validates navigation and explicit epistemic boundaries only.
It does not validate any jurisdictional legal opinion, license or title.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
NOTICE = ROOT / "LICENSES" / "BERNE_TRIPS_DEFAULT_RIGHTS_NOTICE_V1.md"


class RightsDefaultNoticeGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notice = NOTICE.read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.start = (ROOT / "001_PONTEIRO" / "START_HERE.md").read_text(encoding="utf-8")

    def test_strict_readme_anchor(self):
        self.assertIn("BERNE_TRIPS_DEFAULT_RIGHTS_NOTICE_V1.md", self.readme)
        self.assertIn("DIREITOS AUTORAIS RESERVADOS POR PADRÃO", self.readme)
        self.assertIn("Public access", self.readme)

    def test_router_anchor(self):
        self.assertIn("../LICENSES/BERNE_TRIPS_DEFAULT_RIGHTS_NOTICE_V1.md", self.start)

    def test_no_new_general_license(self):
        self.assertIn("SEM NOVA CONCESSÃO", self.notice)
        self.assertIn("claim_allowed:** false", self.notice)
        self.assertIn("SOFTWARE_LICENSE_DECISION.md", self.notice)
        self.assertIn("TOKEN_VAZIO / DECISION_REQUIRED", self.notice)

    def test_prior_grants_and_exceptions_visible(self):
        self.assertIn("Direitos e permissões já concedidos", self.notice)
        self.assertIn("exceções legais", self.notice)
        self.assertIn("direitos de terceiros", self.notice.lower())

    def test_sources_and_limits_present(self):
        for authority in (
            "Convenção de Berna", "TRIPS", "Lei 9.609/1998",
            "17 U.S.C.", "Diretiva 2009/24/CE", "REsp 991.721/PR"
        ):
            with self.subTest(authority=authority):
                self.assertIn(authority, self.notice)

    def test_unknown_is_typed_not_zero(self):
        for token in (
            "TOKEN_VAZIO_RIGHTSHOLDER", "TOKEN_VAZIO_UPSTREAM_LICENSE",
            "TOKEN_VAZIO_GRANT_SCOPE", "TOKEN_VAZIO_JURISDICTION",
            "TOKEN_VAZIO_COUNSEL_OPINION", "TOKEN_VAZIO_CASE_FACTS",
        ):
            with self.subTest(token=token):
                self.assertIn(token, self.notice)
        self.assertIn("Nenhum desses estados significa", self.notice)

    def test_rollback_and_custody_explicit(self):
        self.assertIn("Rollback", self.notice)
        self.assertIn("LICENSE_POLICY.md", self.notice)
        self.assertIn("LICENSE-RAFCODE-PROPRIETARY-V1.md", self.notice)


if __name__ == "__main__":
    unittest.main()
