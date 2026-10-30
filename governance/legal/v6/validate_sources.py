#!/usr/bin/env python3
"""V6 constitutional source register: structural checks only, never legal certification."""
import json
import pathlib

HERE = pathlib.Path(__file__).parent

def check(d):
    assert d["schema"] == "TVARCS-LEGAL-CONSTITUTION-SOURCES-V6"
    assert d["coverage_target_minimum_sovereign_jurisdictions"] == 186
    assert d["accepted_coverage_count"] == 0
    assert d["verified_sovereign_constitutions_full"] == 0
    assert d["claim_allowed"] is False and d["promotion"] == "HOLD"
    assert d["legal_counsel_signed_off"] is False and d["license_change"] is False
    assert "186" in d["gaps"][0]
    assert len(d["jurisdictions"]) >= 20
    codes = [j["code"] for j in d["jurisdictions"]]
    assert len(set(codes)) == len(codes)
    assert sum(j["classification"].startswith("sovereign") for j in d["jurisdictions"]) == 21
    assert codes.count("MX") == 1
    for j in d["jurisdictions"]:
        assert j["source_url"].startswith("https://")
        assert j["provision"] and j["article_text"] == "TOKEN_VAZIO"
        assert j["state"] == "RESEARCH_INDEX_ONLY"
        assert j["latest_consolidation_verified"] is False
        assert j["judicial_enforceability"] == "TOKEN_VAZIO"
        assert j["local_counsel"] == "TOKEN_VAZIO"
    assert len(d["treaty_links"]) >= 5
    assert len(d["gate_ids"]) >= 12
    return True

if __name__ == "__main__":
    obj = json.loads((HERE / "constitutional_sources.json").read_text(encoding="utf-8"))
    check(obj)
    print("PASS structural_source_index_only; never legal compliance")
