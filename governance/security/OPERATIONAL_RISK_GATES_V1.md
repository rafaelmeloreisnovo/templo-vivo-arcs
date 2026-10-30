# Templo Vivo ARCS — P0/P1 operational hardening gates V1

**Date:** 2026-10-30 · **Status:** DRAFT / BRANCH_ONLY / PROMOTION_HOLD
**Scope:** safety and security governance only. No license, runtime, privacy records, secrets, provider settings, or deployment are changed by this proposal.

## Boundary

A GitHub document, legal comparison, or green structural test is **not** evidence that a security control is deployed. Source ≠ artifact ≠ execution ≠ evidence ≠ claim. This V1 JSON is a fail-closed **readiness register**, not a registry of real user reports.

| Gate | Priority | Release blocker until verified | Evidence required privately or publicly only when sanitized |
|---|---|---|---|
| G01 | P0 | Credential exposure/revocation and scope | Responsible admin attests token revoked/rotated, scope minimized, date and private receipt; never reveal secret |
| G02 | P0 | GitHub main rules/protection | Provider readback for required review, required checks, block force-push/delete, admin bypass policy; no destructive test on production |
| G03 | P0 | Child-safety policy and response ownership | Named authorized safeguarding role, abuse reporting/escalation drill, no unsupervised adult–minor contact |
| G04 | P0 | Religious-belief and minor-data processing | Data-flow inventory, no-collection default, lawfully reviewed legal basis, retention/deletion, child best-interests review |
| G05 | P1 | Coordinated security disclosure | Private vulnerability reporting or another independently verified **private** channel; only then publish channel |
| G06 | P1 | Software supply chain | SBOM/license inventory, dependency and binary provenance, secret scanning, credential hygiene |
| G07 | P1 | Authorization and rights | Per-asset ownership and upstream-license audit; no retroactive relicensing, 186-country certification or patent monopoly |
| G08 | P1 | Exact-version gates | Reproducible tests, review, security scan, version/ref and evidence for the exact release candidate |
| G09 | P1 | Incident and recovery procedure | Containment owner, private evidence chain, restore drill, rollback route and corrective record |

**Current**: status values are `TOKEN_VAZIO` for unobserved control implementation. Earlier research reported unprotected `main`, but the latest connector read returned HTTP 403, so **current protection must remain unverified** rather than being promoted to secure or assumed absent. An earlier credential risk is documented by project records but no private secret value is copied here.

## Required workflow

1. Resolve **actual operator, services, users, jurisdictions and asset versions**; unknown facts are not treated as zero.
2. Use independent sources to establish implementation. Record artifact ID, source, observation time, observer, test and limitations. Do **not** put secrets, religious beliefs or child records in a public receipt.
3. Apply only the minimum reversible change with a separately authorized provider/admin operator; changes to branch rules, secrets, user data, or enforcement are **outside** this PR.
4. Test the exact changed state with positive/negative paths. A failed test, inaccessible provider status or missing evidence means `HOLD`.
5. Obtain human legal/privacy/safeguarding sign-off *where applicable*. Never infer legal compliance from CI success.
6. Write an append-only successor with `parent/supersedes` and evidence. Revalidate after the change; do not erase the predecessor.

## Threats and falsifiers

- **False PASS:** edit JSON to `release_allowed=true` without owner/provider/independent evidence ⇒ validator **rejects**.
- **Claim laundering:** mark `claim_allowed=true` because a markdown check passed ⇒ validator **rejects**.
- **Schema drift:** remove/duplicate a P0 control, rename ID, downgrade severity ⇒ validator **rejects**.
- **Evidence laundering:** set `VERIFIED` without evidence_ref/owner/verified_at ⇒ validator **rejects**.
- **Untrusted public report:** add security disclosure text with real secrets or private child data ⇒ must be withheld privately and reviewed, not entered in this register.
- **Provider 403:** interpret access denial as successful protection ⇒ invalid conclusion; remain TOKEN_VAZIO until authoritative readback.
- **Jurisdiction claim:** counting URLs or translated clauses as 186 verified legal opinions ⇒ invalid; counsel review remains a separate gate.

## Rollback, authority and acceptance

**Rollback**: close unmerged draft PR, or use an additive corrective successor after independently authorized merge; no force-push or history erasure.

**Accept this proposal only if:** security policy and 9 unique gates exist; tests reject false elevation and incomplete evidence; source files read back at a specific Git commit; PR remains unmerged pending human operator approval. **Do not claim operational risk reduction was enforced** until provider settings, response ownership, data processing and secrets are actually verified.

Related: [LICENSE_POLICY.md](../../LICENSE_POLICY.md), [legal evidence V5](../legal/v5/README.md), [constitutional research V6](../legal/v6/README.md).

R3 = <F_ok: proposed scoped fail-closed procedure; F_gap: owner/provider/secret/child/data/release verification; F_next: human-approved implementation and exact-state readback>.
