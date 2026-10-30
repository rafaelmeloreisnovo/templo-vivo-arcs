# Templo Vivo ARCS — Legal text accessibility in 8 languages (V7)

**STATUS:** `DRAFT_TRANSLATION / TRANSLATION_NON_AUTHORITATIVE / CLAIM_ALLOWED=false / PROMOTION=HOLD`

This collection is an accessibility aid to read the existing [license policy](../../../../LICENSE_POLICY.md), the existing [RAFCODE proprietary V1 license](../../../../LICENSE-RAFCODE-PROPRIETARY-V1.md) and an additional **non-binding** human rights/safeguarding notice. It does **not** grant new permissions, replace an existing contract, license upstream contributions, translate the historical root `LICENSE` into a new software grant or claim compliance in 186 jurisdictions.

## Language navigation

| Locale | Material | Status |
|---|---|---|
| [Português (Brasil)](pt-BR.md) | Policy, scoped license, safeguarding | Draft translation |
| [English (US)](en-US.md) | Embedded copies of source English, safeguarding | Original text reference |
| [Español](es-ES.md) | Policy, scoped license, safeguarding | Draft translation |
| [Français](fr-FR.md) | Policy, scoped license, safeguarding | Draft translation |
| [Deutsch](de-DE.md) | Policy, scoped license, safeguarding | Draft translation |
| [Italiano](it-IT.md) | Policy, scoped license, safeguarding | Draft translation |
| [日本語](ja-JP.md) | Policy, scoped license, safeguarding | Draft translation |
| [简体中文](zh-CN.md) | Policy, scoped license, safeguarding | Draft translation |

## Exact source and meaning boundary

- Source 1: `LICENSE_POLICY.md` Git blob `6e83eca92b4546ad5006efc08aaa5abd7114b41c`; includes V3 **proposal-only** appendix.
- Source 2: `LICENSE-RAFCODE-PROPRIETARY-V1.md` Git blob `d89df5b35aacee581b30d28276d1e700eca6564a`; `LicenseRef-RAFCODE-PROPRIETARY-1.0`, scoped **only** to legally covered original material.
- Source 3: `LICENSES/RIGHTS_NOTICE_AND_LICENSE_BOUNDARIES_V3.md` Git blob `7cd8d8a2d68d9312f864c5d2c3f3b2826be58b46`; informational **DRAFT**, linked in each locale but not fully translated here.
- `LICENSES/SOFTWARE_LICENSE_DECISION.md`: repository-wide software license decision is still `TOKEN_VAZIO / DECISION_REQUIRED`.
- English source texts and mandatory applicable law must be checked in the event of discrepancy. Translations do not resolve coauthor claims, prior agreements or third-party rights.
- Each locale contains 13 numbered policy clauses, 13 proprietary-license clauses, and five supplemental safeguarding clauses. **The supplemental section is not part of the license.**

## Falsification, security, completion gate

`validate_i18n.py` checks original Git blob SHA1, locale roster, section ordering/counts, disclaimer markers, minimum completeness and selected language tokens. The adversarial unit tests verify missing/duplicate sections, unverifiable approvals, unauthorized scope/grants, reference drift and unrelated PR files. CI runs on PR with read-only permissions, no secrets, deploy, administrative changes, signing or merge.

**Limits:** automated checks do not prove semantic equivalence, quality of legal terminology, enforceability, interpreter acceptance, laws or treaty status, translations in judicial proceedings, sanctions or international compliance. No official/notarial/certified translation is claimed. Humans fluent in each language and licensed local counsel must check every legally material clause, particularly disclaimers, liability limitations, copyright exceptions, moral rights, minors, religious data and jurisdictional disputes.

**Promotion gate:** source version pinned + 8 language/legal reviews + critical-clause back translation + changes resolved by successor + accessibility review + rights-holder explicit decision + release tag/receipt. Until all achieved: `TRANSLATIONS_FOR_REFERENCE_ONLY`, `CLAIM_ALLOWED=false`.

**Rollback:** close the DRAFT PR; if merged after review, correct via a successor commit, preserve original source and history.
