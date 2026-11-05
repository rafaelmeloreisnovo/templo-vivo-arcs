#!/usr/bin/env python3
"""Ω semantic hotfix V1: preserve observations; NEVER infer referents from glyphs.

Source: user-supplied Ω00..Ω15 symbolic pseudocode, 2026-11-05.
This library provides byte-reconstructible typed observations, not natural
language disambiguation, safety approval, physical effects or legal claims.
Stdlib-only; no external network and no auto-promotion of TOKEN_VAZIO.
"""
from __future__ import annotations

import hashlib
import math
import re

MISSING = object()
EXPECTED_CASE_IDS = frozenset(f"Ω{index:02d}" for index in range(16))
SOURCE_REF = "USER_PROMPT_OMEGA00_OMEGA15_20261105"

# Frozen literal UTF-8 fingerprints; not provenance or semantic proof.
SEED_UTF8_SHA256 = {
    "Ω00": "62edc7722a1f6117e52963676d1ab01e46beb410f316fc55615457b76e713331",
    "Ω01": "2a0cbe606f658a1a46bea89ccaea15a258f04655dc36878b791f5ba37a1297da",
    "Ω02": "c4dd67368286d02d62bdaa7a775b7594765d5210c9ad20cc3c24148d493353d7",
    "Ω03": "78b8de92ede47b0c168012d627b911294ce2da7ae8824fde77a0290be15b71e5",
    "Ω04": "73c8ffe9553f8c24730219e392209eaa97d52ee18633550b3ce8526c9955e6e0",
    "Ω05": "ac5a7b838a9549ddcd9a53d98e7a3147d872e8f27be1ea85b6fbac01609320dc",
    "Ω06": "ddce9439cc3e31d942167bae761f2b181daab006d6a0df1ff821568a1e563fd3",
    "Ω07": "62edc7722a1f6117e52963676d1ab01e46beb410f316fc55615457b76e713331",
    "Ω08": "cdaa27d976cdadc8a36b690c8be8661b1fa9932b59d3de09b724d7613ccdcaac",
    "Ω09": "1a0f564ddc6039457b2fb26b3d6a316c15eba20a886449847c3210c35821a693",
    "Ω10": "173b6275a5500442958b5ce18449880dc1f4d4adfe84f376ed331a994fa0005f",
    "Ω11": "abf7d9f5d79f314e3171a446a50c117fcaf1b69ce810e94e2887ebb017f4aeb4",
    "Ω12": "5e642081894886f4f74a2eb7c0b202786bf1e0e4499cad007a089ce7e428221d",
    "Ω13": "6a6ea5bad9154044024d03f195592048f26643cc70f6121255fdb9b7016cd575",
    "Ω14": "840ce7db9eb471fc8dca7cb202a9591e882e04c2f3533188cb0017c2d599cdbe",
    "Ω15": "c809a304e5af2ec0397905f4e732492f5ac639b4c7c43367bc3b10c934a437a4",
}


class SemanticGateError(ValueError):
    """Fail-closed: lost provenance, collapsed types or unsupported claims."""


def require(predicate: bool, reason: str) -> None:
    if not predicate:
        raise SemanticGateError(reason)


def observe(value=MISSING):
    """No trimming, case folding, Unicode normalization or homonym guessing."""
    if value is MISSING:
        return {"kind": "ABSENT", "claim_allowed": False,
                "meaning": "TOKEN_VAZIO_CONTEXT"}
    if value is None:
        return {"kind": "NULL", "raw": None, "claim_allowed": False,
                "meaning": "TOKEN_VAZIO_CONTEXT"}
    if type(value) is bool:
        return {"kind": "BOOLEAN", "raw": value, "claim_allowed": False,
                "meaning": "TOKEN_VAZIO_CONTEXT"}
    if type(value) is int:
        return {"kind": "INTEGER_ZERO" if value == 0 else "INTEGER",
                "raw": value, "claim_allowed": False,
                "meaning": "TOKEN_VAZIO_CONTEXT"}
    if type(value) is float:
        require(math.isfinite(value), "non-finite number is not JSON-safe")
        return {"kind": "FLOAT_ZERO" if value == 0 else "FLOAT",
                "raw": value, "claim_allowed": False,
                "meaning": "TOKEN_VAZIO_CONTEXT"}
    require(type(value) is str, "unsupported or mutable input type")
    if value == "":
        kind = "EMPTY_STRING"
    elif value == "∅":
        kind = "SYMBOLIC_EMPTY"
    elif value == "TOKEN_VAZIO":
        kind = "UNKNOWN_TYPED_LITERAL"
    elif value.isspace():
        kind = "WHITESPACE_ONLY"
    elif re.fullmatch(r"0x[0-9a-fA-F]+", value):
        kind = "HEX_NOTATION_TEXT_NOT_BYTES"
    elif any(ord(char) < 32 for char in value):
        kind = "CONTROL_TEXT_NOT_NULL"
    else:
        kind = "TEXT_LITERAL_UNINTERPRETED"
    data = value.encode("utf-8")
    return {
        "kind": kind,
        "raw": value,
        "utf8_sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "codepoints": len(value),
        "claim_allowed": False,
        "meaning": "TOKEN_VAZIO_CONTEXT",
    }


def verify_cases(cases):
    """Structural falsifiers only; distinct IDs may have identical lexemes."""
    require(type(cases) is list and len(cases) == 16, "exactly 16 seed cases")
    seen = set()
    for case in cases:
        require(type(case) is dict, "case must be an object")
        case_id = case.get("id")
        require(type(case_id) is str and case_id in EXPECTED_CASE_IDS,
                "unknown case ID")
        require(case_id not in seen, "duplicate case ID")
        seen.add(case_id)
        require(case.get("source_ref") == SOURCE_REF, "unbound source label")
        require(case.get("evidence_status") == "USER_INPUT_ONLY",
                "source promoted to execution evidence")
        require(case.get("semantic_status") == "TOKEN_VAZIO_CONTEXT",
                "semantic interpretation without independent proof")
        require(case.get("forecast_status") == "TOKEN_VAZIO_FORECAST",
                "uncalibrated prediction promoted")
        require(case.get("claim_allowed") is False, "unsupported claim")
        require(type(case.get("literal")) is str, "seed must retain source spelling")
        require(type(case.get("expected_kind")) is str, "missing exact type")
        require(observe(case["literal"])["kind"] == case["expected_kind"],
                "type collapse or changed input bytes")
        require(observe(case["literal"])["utf8_sha256"] == SEED_UTF8_SHA256[case_id],
                "seed bytes changed even if type label was also altered")
        require(type(case.get("falsifier")) is str
                and len(case["falsifier"].strip()) >= 12,
                "falsifier not specified")
    require(seen == EXPECTED_CASE_IDS, "some Ω seed was omitted")
    return {
        "scope": "USER_INPUT_LITERAL_STRUCTURE_ONLY",
        "cases": len(seen),
        "type_distinctions": True,
        "source_ref": SOURCE_REF,
        "claim_allowed": False,
        "promotion": "HOLD",
        "semantic_truth": "TOKEN_VAZIO_CONTEXT",
        "forecast_accuracy": "TOKEN_VAZIO_FORECAST",
    }
