#!/usr/bin/env python3
"""Fail-closed contract checks for the Templo Vivo ARCS GitHub Pages portal."""
from __future__ import annotations

import json
import pathlib
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "/templo-vivo-arcs/"
ORIGIN = "https://rafaelmeloreisnovo.github.io"
CANONICAL = ORIGIN + BASE

required = [
    "index.html",
    "_config.yml",
    "robots.txt",
    "sitemap.xml",
    "manifest.webmanifest",
    "404.html",
    "assets/site.css",
    "assets/favicon.svg",
]

errors: list[str] = []

for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing:{rel}")

def read(rel: str) -> str:
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.is_file() else ""

index = read("index.html")
config = read("_config.yml")
robots = read("robots.txt")
not_found = read("404.html")

checks = {
    "canonical": f'<link rel="canonical" href="{CANONICAL}">' in index,
    "manifest_link": 'href="manifest.webmanifest"' in index,
    "favicon_link": 'href="assets/favicon.svg"' in index,
    "jsonld_website": '"@type": "WebSite"' in index,
    "config_url": f'url: "{ORIGIN}"' in config,
    "config_baseurl": f'baseurl: "{BASE.rstrip("/")}"' in config,
    "robots_sitemap": f"Sitemap: {CANONICAL}sitemap.xml" in robots,
    "project_404": BASE in not_found,
}

for key, ok in checks.items():
    if not ok:
        errors.append(f"check:{key}")

try:
    manifest = json.loads(read("manifest.webmanifest"))
    if manifest.get("start_url") != BASE:
        errors.append("manifest:start_url")
    if manifest.get("scope") != BASE:
        errors.append("manifest:scope")
except Exception as exc:
    errors.append(f"manifest:parse:{exc.__class__.__name__}")

try:
    tree = ET.parse(ROOT / "sitemap.xml")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [x.text for x in tree.findall(".//sm:loc", ns)]
    if CANONICAL not in locs:
        errors.append("sitemap:canonical-root")
except Exception as exc:
    errors.append(f"sitemap:parse:{exc.__class__.__name__}")

result = {
    "artifact": "TEMPLO_VIVO_PAGES_CONTRACT_V1",
    "status": "PASS" if not errors else "FAIL",
    "canonical": CANONICAL,
    "required_files": required,
    "checks": checks,
    "errors": errors,
}

print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
sys.exit(0 if not errors else 1)
