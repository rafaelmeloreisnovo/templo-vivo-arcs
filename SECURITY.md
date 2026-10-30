# Security policy — Templo Vivo ARCS

> **DRAFT / NOT A PRODUCTION SECURITY CERTIFICATION** — 2026-10-30
> This policy is a proposed process. It does not prove that reporting, monitoring, encryption, deployment, or provider protections are configured. No incident response SLA is represented.

## Scope and supported versions

This repository contains software, research, documentation, historical material and binaries. **No release is presently attested as security-supported for production by this policy.** A specific, maintained version and support window require a separate published decision, owner, artifact hash, threat model and tests. Historical claims are not security assurances.

## Responsible vulnerability disclosure

1. **Do not publish vulnerabilities, access tokens, credentials, children's information, religious beliefs, exploit instructions against real users or personal data in public GitHub issues, PRs, discussions, screenshots or logs.**
2. If GitHub's **private vulnerability reporting** is enabled on this repository, use the repository's **Security → Advisories → Report a vulnerability** path. Availability has **not been verified**. Do not assume it is enabled merely because this file exists.
3. If there is no private reporting button, open only a **generic public request for a private security contact**, without vulnerability details, proofs of concept or personal information; alternatively use an independently verified private maintainer channel. The designated private contact remains **TOKEN_VAZIO** until the maintainer publishes an approved channel.
4. Do not perform intrusive testing, access other people's accounts, exfiltrate data or circumvent authorization. Coordinate testing in an authorized environment.

## Triage and response (proposed, not asserted as operating)

- **P0 — imminent harm / child safety / exposed active credential / live personal data:** stop further sharing, restrict access using authorized personnel, preserve minimum necessary evidence privately, contact the appropriate protective/emergency authorities where immediate safety requires it. Do not publish identifying details.
- **P1 — exploitable security vulnerability or high-risk privacy exposure:** privately record exact asset/commit, exploit preconditions, impact, operator and containment; request authorized owner review.
- **P2/P3 — lower severity:** track a sanitized case reference, affected version, mitigating controls and independent reproduction status.
- For every severity: separate **reported → reproduced → contained → remediated → regression-tested → authorized closed**, retaining evidence and disagreement. Never label a remediation PASS before readback and applicable tests.
- Reporters receive no promise of a fixed SLA until a responsible maintainer explicitly adopts one.

## Release and legal boundaries

See [operational risk gates](governance/security/OPERATIONAL_RISK_GATES_V1.md) and [machine-readable HOLD state](governance/security/readiness_v1.json). Documentation-only CI validates structure; **it does not switch on branch protection, secret scanning, private reporting, rotate secrets, or legally approve deployment**.

- No collection of religious beliefs, children's data or contact information by default. Establish operator identity, purpose, legal basis, minimization, retention, data-subject route and a child-safety escalation process **before** actual collection or contact.
- No unsolicited adult–minor contact, compulsory religious participation, discrimination for belief/non-belief, suppression of lawful criticism or revenge against reporters.
- Respect upstream licenses, lawful third-party rights and mandatory exceptions; this policy **does not grant or revoke a copyright, software, patent or trademark license**. The historical root `LICENSE` stays historical.
- No automatic merge, deploy, release or publication. Source ≠ artifact ≠ execution ≠ evidence ≠ claim.
- This policy is an accountable proposal, **not legal advice** and not a representation of compliance in 186 jurisdictions.

## Governance and rollback

Owner of technical implementation: this GitHub repository. Owner of memory/receipts: authorized Drive project ledger. Review and approval by a designated human operator are needed for activation. Proposed branch-only changes can be rolled back by closing its unmerged PR. Historic material and previous grants are retained. Unknown is **TOKEN_VAZIO, not PASS**.
