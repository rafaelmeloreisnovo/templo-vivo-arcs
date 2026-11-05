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
