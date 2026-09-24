# RECEIPT — TEMPLO VIVO ARCS SITE PORTAL V1

Date: 2026-09-24
Repository: rafaelmeloreisnovo/templo-vivo-arcs
Public Pages URL: https://rafaelmeloreisnovo.github.io/templo-vivo-arcs/

## Materialized

- index.html — landing portal
- assets/site.css — responsive visual system
- _config.yml — GitHub Pages/Jekyll canonical configuration
- robots.txt — crawler policy
- sitemap.xml — canonical root sitemap
- manifest.webmanifest — installable-web metadata
- assets/favicon.svg — vector favicon
- 404.html — project-aware missing-route page
- scripts/verify_pages_site.py — deterministic site contract
- .github/workflows/jekyll-gh-pages.yml — Pages deploy gated by verifier

## Key commits

- landing: e0cb50341d653f5dda7b373d618f6fbc01c6edb7
- stylesheet base: c6d700e9791d5b9f6fdc37e6f677200a49e5f706
- config: e9aae698e6603b4806f2f6f803c3ead84afa5670
- robots: e972173df46174042181cbc1baca9c38fc94ec20
- sitemap: 38efce23bb5bbec6e52f75d932e6321c95c4f88c
- manifest: 9df18e6de95b1017ea83fc98127e28b5e01432fd
- favicon: 658db0b3fabab942db19acf47d771e9ae546edfd
- 404: 4de63e303c2348c5847766c9e32df28cadc9be41
- metadata: 78b282fbc4ce3a0fdb61a32bc09a331f7a46a8c6
- error style: 4591e457ff4c7ff55dd2dd9d6378d50af45652ce
- verifier: 492873c37c9e7afe0a8622f02a1b1b901fd73351
- gated Pages workflow: 51c1c6cddfbba5eb566d4f6571611dff5734fb9c

## Evidence

Previous Pages deployment run 35971395789: SUCCESS.
Canonical public URL: https://rafaelmeloreisnovo.github.io/templo-vivo-arcs/

Readback checks after production-shell creation:
- canonical: PASS
- manifest link: PASS
- favicon link: PASS
- JSON-LD WebSite: PASS
- _config baseurl: PASS
- robots -> sitemap: PASS
- sitemap canonical root: PASS
- manifest scope: PASS
- project-aware 404: PASS
- favicon SVG: PASS

## Boundary

The special user-site repository rafaelmeloreisnovo/rafaelmeloreisnovo.github.io is still not observed/created by the available connector.
Current production URL remains the project-site route under /templo-vivo-arcs/.

The gated workflow commit exists; a workflow run for that exact commit was not yet observed at receipt creation.

## R3

F_ok: public project site exists; prior deployment PASS; production shell and deterministic contract gate materialized.

F_gap: root user-site repository; exact-run observation for gated workflow; custom domain remains TOKEN_VAZIO because none was specified.

F_next: observe gated deploy; then add only content/navigation modules backed by repository evidence, not duplicate corpus.
