# 001_PONTEIRO — Templo Vivo ARCS: autoria e licenças

**Status:** READ_ONLY_SOURCE_AUDIT / PRIVATE_HUMAN_REVIEW_NEEDED / NO_NEW_LICENSE_GRANT
**Source HEAD:** `main@e5468415e22d26668c0094522eac5b33f0079669` (2026-10-30 snapshot). **Audit branch:** `audit/templo-rights-chain-373-20261030-v1`. Do not assume branch documents were merged.

## Read route
1. [FINDINGS — findings and decisions](2026-10-30_TVARCS_RIGHTS_AUDIT_FINDINGS_V1.md) — actual observed risks and source citations.
2. [FILE RIGHTS CENSUS — 373 records](2026-10-30_TVARCS_FILE_RIGHTS_CENSUS_373_V1.jsonl) — exactly one path record per file with blob SHA and typed unknown title/grant.
3. [EXISTING V3 — 24 jurisdiction legal matrix](../2026-10-30_TVARCS_COMPARATIVE_LAW_24_JURISDICTIONS_V3.md) — research routes, **not** 24 expert opinions.
4. [LICENSE POLICY](../../../LICENSE_POLICY.md) and [SOFTWARE LICENSE DECISION](../../../LICENSES/SOFTWARE_LICENSE_DECISION.md) — existing policy sources; broad grant still unresolved.
5. [HISTORICAL RIGHTS MATRIX](../../../docs/legal/LICENSING_AND_RIGHTS_MATRIX_V1.md) — precedent/historical language **not adopted** for every individual file without proof.

## Evidence boundary
`GIT_BLOB_SHA != human_creator != lawful_owner != permission`.
An asset is not cleared solely because commit author equals repository owner, because it sits in `LICENSES/`, or because two copies have the same SHA.
`SOURCE != ARTIFACT != EXECUTION != EVIDENCE != CLAIM`.
A document named `LICENSE` is not by itself proof of an asset-specific grant.

## Remaining gates
- Identify original human author, any joint author, possible assignment and prior permissions for each actual asset; store sensitive evidence privately, not in this public repo.
- Verify third-party and transitive dependency licenses from exact release artifacts and a reproducible SBOM.
- Inspect media and archives for permission/privacy/child-safety issues under lawful authority.
- Country-specific jurisdiction and controlling authority checked and attested by local counsel before legal action or broad enforcement claim.
- **No auto-merge or license switch** from this inventory. `TOKEN_VAZIO` is a required auditable state, not a negative ownership determination.

**Rollback:** leave main unchanged; close/discard unmerged branch only with authorized confirmation. Future corrections append successor records.
