#!/usr/bin/env python3
"""Fail-closed structural validation of Templo Vivo human/AI routes. Stdlib only."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SOURCE = ROOT / "001_PONTEIRO" / "routes_v1.json"
VALID_STATUS = {"ENTRY", "HISTORICAL", "HOLD", "REFERENCE_ONLY", "RESEARCH_ONLY", "SCOPED_ONLY"}
VALID_REL = {"NAVIGATES", "GATES", "HISTORICAL_REFERENCE", "SCOPES", "DISTINGUISHES", "SUPPORTS", "REFERENCES", "RESEARCH_EXTENDS"}
VALID_DOMAINS = {"NAVIGATION", "HUMAN", "RIGHTS", "SAFETY", "LEGAL"}

def validate(data, root=ROOT):
    errors = []
    def fail(msg):
        errors.append(msg)
    if not isinstance(data, dict):
        return ["root must be object"]
    for key, value in {"schema_version": "tvarcs-nav-v1", "status": "RESEARCH_ONLY", "promotion": "HOLD"}.items():
        if data.get(key) != value:
            fail("invalid " + key)
    if data.get("claim_allowed") is not False or data.get("sovereignty_claim_allowed") is not False:
        fail("claim elevation blocked")
    if data.get("producer_repo") != "rafaelmeloreisnovo/templo-vivo-arcs":
        fail("wrong producer authority")
    if data.get("default_depth") != 1 or data.get("default_roots") != 3:
        fail("unbounded traversal not allowed")
    allowed_expansion = {"missing_source", "contradiction", "unresolved_authority", "missing_evidence", "explicit_request"}
    if set(data.get("expand_only", [])) != allowed_expansion:
        fail("expansion permission drift")
    invariants = data.get("invariants", [])
    if not isinstance(invariants, list) or not any("DIGITAL_INFRASTRUCTURE != TERRITORIAL_SOVEREIGNTY" == x for x in invariants):
        fail("physical/digital sovereignty boundary removed")
    if not {"G01", "G02", "G03", "G04"}.issubset(set(data.get("priority_gates", []))):
        fail("P0 safeguards removed")
    nodes = data.get("nodes")
    edges = data.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        return errors + ["nodes and edges must be lists"]
    ids, paths = set(), set()
    safe_root = pathlib.Path(root).resolve()
    for n in nodes:
        if not isinstance(n, dict):
            fail("node not object")
            continue
        nid, path = n.get("id"), n.get("path")
        if not isinstance(nid, str) or not re.fullmatch(r"[a-z][a-z0-9_]{1,63}", nid):
            fail("invalid node id")
            continue
        if nid in ids:
            fail("duplicate node id: " + nid)
        ids.add(nid)
        if n.get("status") not in VALID_STATUS or n.get("domain") not in VALID_DOMAINS:
            fail("invalid node domain/status: " + nid)
        if not isinstance(path, str) or path.startswith("/") or "\\" in path or ".." in pathlib.PurePosixPath(path).parts or "://" in path:
            fail("invalid local path: " + nid)
            continue
        if path in paths:
            fail("duplicate path: " + path)
        paths.add(path)
        target = (safe_root / path).resolve()
        if not target.is_relative_to(safe_root) or not target.is_file():
            fail("missing/outside file: " + path)
    if "start" not in ids:
        fail("missing root start")
    seen_edges, graph = set(), {}
    for e in edges:
        if not isinstance(e, dict):
            fail("edge not object")
            continue
        a, b, kind = e.get("from"), e.get("to"), e.get("type")
        if a not in ids or b not in ids or a == b or kind not in VALID_REL:
            fail("invalid edge")
            continue
        triple = (a, b, kind)
        if triple in seen_edges:
            fail("duplicate edge")
        seen_edges.add(triple)
        graph.setdefault(a, set()).add(b)
    visited, frontier = set(), ["start"]
    while frontier:
        current = frontier.pop()
        if current in visited:
            continue
        visited.add(current)
        frontier.extend(graph.get(current, ()))
    if ids - visited:
        fail("unreachable nodes: " + ",".join(sorted(ids - visited)))
    checks = data.get("adversarial_checks")
    if not isinstance(checks, list) or len(checks) < 6:
        fail("missing adverse controls")
    elif any(not isinstance(c, dict) or c.get("expected") != "NO" for c in checks):
        fail("false-positive adversarial expectation")
    return errors

def main():
    try:
        data = json.loads(SOURCE.read_text(encoding="utf-8"))
        errors = validate(data)
    except (OSError, ValueError) as exc:
        errors = ["parse/read failure: " + str(exc)]
    if errors:
        for error in errors:
            print("NAV_FAIL_CLOSED:", error, file=sys.stderr)
        return 1
    print("PASS_SCOPED_NAVIGATION_ONLY; LEGAL_CLAIM=false; SOVEREIGNTY_CLAIM=false")
    return 0

if __name__ == "__main__":
    sys.exit(main())
