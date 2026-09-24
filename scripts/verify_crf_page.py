#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/"crf"/"page_data.json"
HTML=ROOT/"crf"/"index.html"
JS=ROOT/"crf"/"crf.js"
EXPECTED_SHA="9e73e19a231df145dfa22d81814eea2a3dca14ab053402f0bb6a56d092a61bc1"
EXPECTED_BLOB="c0419c91b213773377518752a15983416773f1c7"

errors=[]
for p in (DATA,HTML,JS,ROOT/"crf"/"crf.css"):
    if not p.is_file(): errors.append(f"missing:{p.relative_to(ROOT)}")
if DATA.is_file():
    digest=hashlib.sha256(DATA.read_bytes()).hexdigest()
    if digest!=EXPECTED_SHA: errors.append(f"page_data_sha256:{digest}")
    try:
        obj=json.loads(DATA.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"json:{exc.__class__.__name__}")
        obj={}
    if obj.get("schema")!="rll.crf_page_data.v2": errors.append("schema")
    if obj.get("claim_allowed") is not False: errors.append("claim_allowed")
    if obj.get("counts")!={"A":25,"B":8,"C":1,"total":34}: errors.append("counts")
    if obj.get("formalization_counts")!={"A_fail":0,"A_pass":25,"A_total":25}: errors.append("formalization_counts")
    items=obj.get("items",[])
    ids=[x.get("id") for x in items] if isinstance(items,list) else []
    if ids!=[f"CRF-{i:03d}" for i in range(1,35)]: errors.append("ids")
    for item in items:
        fm=item.get("formalization",{})
        if item.get("readiness")=="A":
            if fm.get("ci_test_status")!="PASS" or not fm.get("definition") or not fm.get("lemma") or not fm.get("theorem") or not fm.get("proof"): errors.append("formalization:"+str(item.get("id")))
        elif fm.get("ci_test_status")!="NOT_RUN": errors.append("non_A_status:"+str(item.get("id")))
    if obj.get("source",{}).get("git_blob_sha1")!=EXPECTED_BLOB: errors.append("source_blob")
if HTML.is_file():
    h=HTML.read_text(encoding="utf-8")
    if 'src="crf.js"' not in h or 'crf.css' not in h: errors.append("html_assets")
if JS.is_file():
    j=JS.read_text(encoding="utf-8")
    if 'fetch("page_data.json"' not in j: errors.append("artifact_fetch")
    for forbidden in ("api.github.com","raw.githubusercontent.com","/repos/"):
        if forbidden in j: errors.append("repo_scrape:"+forbidden)

result={"artifact":"TEMPLO_VIVO_CRF_PAGE_V1","status":"PASS" if not errors else "FAIL","page_data_sha256":EXPECTED_SHA,"items":34,"readiness":{"A":25,"B":8,"C":1},"errors":errors}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
sys.exit(0 if not errors else 1)
