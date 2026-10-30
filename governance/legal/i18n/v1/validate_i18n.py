#!/usr/bin/env python3
"""Templo Vivo V7: structural falsification, NOT certification of translations or law."""
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
LOCALES = ("pt-BR","en-US","es-ES","fr-FR","de-DE","it-IT","ja-JP","zh-CN")
EXACT_SOURCE = {
    "LICENSE_POLICY.md":"6e83eca92b4546ad5006efc08aaa5abd7114b41c",
    "LICENSE-RAFCODE-PROPRIETARY-V1.md":"d89df5b35aacee581b30d28276d1e700eca6564a",
    "LICENSES/RIGHTS_NOTICE_AND_LICENSE_BOUNDARIES_V3.md":"7cd8d8a2d68d9312f864c5d2c3f3b2826be58b46",
}
BASE = "governance/legal/i18n/v1/"
ALLOWED = {BASE + f"{v}.md" for v in LOCALES} | {
    BASE+"README.md",BASE+"manifest.json",BASE+"validate_i18n.py",BASE+"test_validate_i18n.py",
    ".github/workflows/tvarcs-license-i18n-v7.yml",
}
KEYWORDS = {
    "pt-BR":("terceiros","crianças","licença","lei","comercial"),
    "es-ES":("terceros","menores","licencia","ley","comercial"),
    "fr-FR":("tiers","mineurs","licence","loi","commercial"),
    "de-DE":("Dritter","Minderjährige","Lizenz","gesetzlich","kommerziell"),
    "it-IT":("terzi","minori","licenza","legge","commercial"),
    "ja-JP":("第三者","未成年者","ライセンス","法律","商業"),
    "zh-CN":("第三方","未成年人","许可","法律","商业"),
}
def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def clauses(text, tag):
    pat = r"(?m)^### "+tag+r" ([PLS]\d{2}) — [^\n]+\n"
    matches = list(re.finditer(pat,text))
    result = []
    for i,m in enumerate(matches):
        nxt = matches[i+1].start() if i+1<len(matches) else len(text)
        body = text[m.end():nxt].split("\n## ")[0].split("\n### ")[0].strip()
        result.append((m.group(1),body))
    return result

def expected_ids(letter, n):
    return [f"{letter}{i:02d}" for i in range(1,n+1)]

def original_sections(raw):
    return [x.partition("\n")[2].strip() for x in re.split(r"(?m)^## ",raw)[1:]]

def validate_manifest(data):
    assert data["schema"]=="TVARCS-LICENSE-I18N-V1"
    assert data["language_codes"]==list(LOCALES)
    assert data["policy_clauses"]==13 and data["proprietary_clauses"]==13 and data["safeguards"]==5
    assert data["human_legal_review_completed"] is False
    assert data["certified_legal_translation"] is False
    assert data["operative_grants_changed"] is False
    assert data["claim_allowed"] is False and data["promotion"]=="HOLD"
    assert data["automated_merging"] is False
    assert data["source_files"]==EXACT_SOURCE
    assert set(data["per_locale"])==set(LOCALES)
    for loc in LOCALES:
        v = data["per_locale"][loc]
        assert v["path"]==BASE+loc+".md"
        assert v["human_legal_review"]=="TOKEN_VAZIO"
        assert v["backtranslation_review"]=="TOKEN_VAZIO"
        assert v["release_authorized"] is False
    return True

def validate_translation(locale,txt):
    assert locale in LOCALES
    for flag in ("TRANSLATION_NON_AUTHORITATIVE","CLAIM_ALLOWED=false","NEW_GRANT=false","PROMOTION=HOLD","LOCAL_COUNSEL=TOKEN_VAZIO"):
        assert flag in txt, (locale,flag)
    for source,blob in EXACT_SOURCE.items():
        assert blob in txt and source.split("/")[-1] in txt, (locale,source)
    assert "Copyright © 2025–2026 Rafael Melo Reis" in txt
    assert "LicenseRef-RAFCODE-PROPRIETARY-1.0" in txt
    for label,number,letter,count in (("POLICY",13,"P",13),("PROPRIETARY",13,"L",13),("SAFEGUARD",5,"S",5)):
        items=clauses(txt,label)
        assert len(items)==number,(locale,label,len(items))
        assert [i for i,b in items]==expected_ids(letter,count),(locale,label)
        for tag,body in items:
            assert len(body)>=30,(locale,tag,"short or missing content")
            assert not any(x in body for x in ("TODO TRANSLATE","[TRANSLATE]","Lorem ipsum")),(locale,tag)
    for word in KEYWORDS.get(locale,()):
        assert word.lower() in txt.lower(),(locale,"missing risk term",word)
    if locale=="ja-JP":
        assert len(re.findall("[ぁ-んァ-ヶ一-龯]",txt))>250
    if locale=="zh-CN":
        assert len(re.findall("[一-龯]",txt))>350
    return True

def verify_english_reference():
    txt=(HERE/"en-US.md").read_text(encoding="utf-8")
    for source,label in (("LICENSE_POLICY.md","POLICY"),("LICENSE-RAFCODE-PROPRIETARY-V1.md","PROPRIETARY")):
        source_bodies=original_sections((ROOT/source).read_text(encoding="utf-8"))
        translated_bodies=[b for _,b in clauses(txt,label)]
        assert source_bodies==translated_bodies,(source,"English source/body mismatch")
    return True

def changed_files_allowed(paths):
    assert paths,"empty PR diff"
    assert len(paths)==len(set(paths)),"duplicate changes"
    unexpected=set(paths)-ALLOWED
    assert not unexpected,("unrelated changes",sorted(unexpected))
    assert set(paths)==ALLOWED,("missing expected",sorted(ALLOWED-set(paths)))
    assert not any(x in paths for x in ("LICENSE","LICENSE_POLICY.md","LICENSE-RAFCODE-PROPRIETARY-V1.md","README.md"))
    return True

def run():
    data=json.loads((HERE/"manifest.json").read_text(encoding="utf-8"))
    validate_manifest(data)
    for path,sha in EXACT_SOURCE.items():
        assert git_blob_sha(ROOT/path)==sha,(path,"SOURCE_DRIFT_HOLD")
    for loc in LOCALES:
        validate_translation(loc,(HERE/(loc+".md")).read_text(encoding="utf-8"))
    verify_english_reference()
    print("PASS structural source identity + 8 locales + 13 policy + 13 proprietary clauses + 5 safeguards each")
    print("LEGAL_EQUIVALENCE=TOKEN_VAZIO; HUMAN_COUNSEL=TOKEN_VAZIO; CLAIM_ALLOWED=false")
    return True

if __name__=="__main__":
    run()
