#!/usr/bin/env python3
"""Bounded, dependency-aware evidence audit. Python standard library + Git only.

PASS means that the named audit completed, not that its audited claim is true.
Receipts and logs are written even when input validation or a subprocess fails.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = "rafaelmeloreisnovo/templo-vivo-arcs"
STAGES = ("context", "provenance", "custody", "contradiction", "uncertainty", "reproduction", "rollback")
DEPENDENCIES = {
    "context": [], "provenance": ["context"], "custody": ["provenance"],
    "contradiction": ["custody"], "uncertainty": ["context"],
    "reproduction": ["custody"], "rollback": ["provenance"],
}
LEDGERS = (
    "evidence/custody/ledger/evidence-ledger.v1.jsonl",
    "evidence/custody/ledger/evidence-resolutions.v1.jsonl",
    "evidence/custody/ledger/evidence-authored-at.v1.jsonl",
    "evidence/custody/ledger/evidence-blockers.v1.jsonl",
    "governance/interaction-feedback.jsonl",
)
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def checked_path(root, relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError("input must be a repository-relative path")
    resolved = (root / path).resolve(strict=True)
    if not resolved.is_relative_to(root.resolve()) or (root / path).is_symlink():
        raise ValueError("input cannot escape the repository or be a symlink")
    if not resolved.is_file():
        raise ValueError("input must be a regular file")
    return resolved


def validate_contract(data):
    if data.get("schema") != "rafaelia.omega-pipeline.v1":
        raise ValueError("unknown pipeline schema")
    if data.get("repository") != REPOSITORY or data.get("claim_allowed") is not False:
        raise ValueError("repository/claim boundary mismatch")
    if data.get("max_cycles") != 1 or data.get("stop") != "RECEIPT_AND_F_NEXT":
        raise ValueError("one bounded invocation is required")
    if not isinstance(data.get("objective"), str) or not data["objective"].strip():
        raise ValueError("objective missing")
    gates = data.get("gates", [])
    if len(gates) != len(STAGES) or {g.get("id") for g in gates} != set(STAGES):
        raise ValueError("exactly seven unique named gates required")
    for gate in gates:
        if gate.get("needs") != DEPENDENCIES[gate["id"]]:
            raise ValueError("unknown/cyclic/changed gate dependency")
        for field in ("ctq", "failure_condition", "next_probe"):
            if not isinstance(gate.get(field), str) or not gate[field].strip():
                raise ValueError(f"missing gate field: {field}")
    return data


def schedule(gates, execute):
    """Run independent lanes after failures; block only dependent lanes."""
    pending = list(gates)
    results = {}
    while pending:
        ready = [g for g in pending if all(dep in results for dep in g["needs"])]
        if not ready:
            raise ValueError("dependency cycle or missing dependency")
        for gate in ready:
            blocked = [dep for dep in gate["needs"] if results[dep]["status"] != "PASS"]
            if blocked:
                row = {"status": "BLOCKED", "reason": "dependency: " + ",".join(blocked)}
            else:
                try:
                    row = {"status": "PASS", "observation": execute(gate["id"])}
                except Exception as exc:
                    row = {"status": "FAIL", "reason": f"{type(exc).__name__}: {exc}"}
            results[gate["id"]] = {"id": gate["id"], **row,
                                  "failure_condition": gate["failure_condition"],
                                  "next_probe": gate["next_probe"], "claim_allowed": False}
            pending.remove(gate)
    return [results[key] for key in STAGES]


def validate_routes(data, legacy):
    rows = data.get("exams", [])
    if data.get("schema") != "rafaelia.omega-exams.v1" or data.get("claim_allowed") is not False:
        raise ValueError("exam schema/claim boundary mismatch")
    seen = set()
    for row in rows:
        for key in ("id", "owner", "trigger", "action", "evidence_out", "closure_gate", "failure_condition", "source_ref"):
            if not isinstance(row.get(key), str) or not row[key].strip() or row[key] == "TOKEN_VAZIO":
                raise ValueError(f"missing executable exam contract: {key}")
        if row["id"] in seen or row.get("priority") not in {"P0", "P1", "P2"}:
            raise ValueError("duplicate exam or invalid priority")
        if row.get("state") != "OPEN" or row.get("claim_allowed") is not False:
            raise ValueError("V1 registers open exams only; closure needs a successor receipt")
        seen.add(row["id"])
    legacy_ids = {row["gap_id"] for row in legacy["gaps"]}
    covered = {row.get("legacy_gap") for row in rows if row.get("legacy_gap")}
    if covered != legacy_ids:
        raise ValueError("legacy gap routes missing or invented")
    return sorted(rows, key=lambda row: (row["priority"], row["id"]))


class Audit:
    def __init__(self, root, output, base, expected_head, contract_path):
        self.root, self.output = root, output
        self.base, self.expected_head = base, expected_head
        self.contract_path = contract_path
        self.commands, self.sources, self.findings, self.exams = [], [], [], []
        self.head = self.base_sha = "TOKEN_VAZIO"
        self.effective_hash = None

    def command(self, argv, timeout=60):
        number = len(self.commands) + 1
        out = self.output / f"{number:02d}.stdout.log"
        err = self.output / f"{number:02d}.stderr.log"
        row = {"argv": argv, "timeout_seconds": timeout, "exit_code": None,
               "stdout": out.name, "stderr": err.name}
        self.commands.append(row)
        try:
            with out.open("wb") as stdout, err.open("wb") as stderr:
                proc = subprocess.run(argv, cwd=self.root, stdout=stdout, stderr=stderr,
                                      timeout=timeout, check=False)
            row["exit_code"] = proc.returncode
        except subprocess.TimeoutExpired:
            row["status"] = "TIMEOUT"
            raise RuntimeError(f"command {number} exceeded {timeout}s")
        except OSError as exc:
            row["status"] = "ERROR"
            raise RuntimeError(f"command {number} could not start: {exc}")
        finally:
            row["stdout_sha256"] = digest(out.read_bytes()) if out.exists() else None
            row["stderr_sha256"] = digest(err.read_bytes()) if err.exists() else None
        row["status"] = "PASS" if proc.returncode == 0 else "FAIL"
        if proc.returncode:
            raise RuntimeError(f"command {number} exit={proc.returncode}; see {err.name}")
        return out.read_bytes()

    def script(self, name, *args):
        return self.command([sys.executable, f"scripts/audit/{name}", *args])

    def execute(self, gate):
        return getattr(self, gate)()

    def context(self):
        self.head = self.command(["git", "rev-parse", "--verify", "HEAD^{commit}"]).decode().strip()
        if not SHA40.fullmatch(self.expected_head) or self.head != self.expected_head:
            raise ValueError("checkout does not match the explicitly requested commit")
        if not SHA40.fullmatch(self.base):
            raise ValueError("base must be an explicit full commit SHA")
        self.base_sha = self.command(["git", "rev-parse", "--verify", "--end-of-options", self.base + "^{commit}"]).decode().strip()
        self.command(["git", "merge-base", "--is-ancestor", self.base_sha, self.head])
        if self.command(["git", "diff", "--name-only", "HEAD", "--"]).strip():
            raise ValueError("tracked worktree changes are not bound to HEAD")
        provider_repo = os.environ.get("GITHUB_REPOSITORY", REPOSITORY)
        if provider_repo != REPOSITORY:
            raise ValueError("provider repository mismatch")
        return {"source_sha": self.head, "base_sha": self.base_sha, "scope": "repository audit only"}

    def provenance(self):
        paths = set(LEDGERS) | {
            self.contract_path, "governance/omega-exams.v1.json",
            "evidence/custody/gaps/gap-router.v1.json",
            "data/autoria/rafaelia_formula_authorship_lineage_omega.v1.json",
            "docs/auditoria/OPERATIONAL_ACTION_CONTRACT_V1.json",
            "docs/auditoria/FINALIZATION_ROUTE_CONTRACT_V1.json",
            ".github/workflows/omega-evidence-pipeline.yml",
        }
        paths |= {p.relative_to(self.root).as_posix() for p in (self.root / "scripts/audit").glob("*.py")}
        paths |= {p.relative_to(self.root).as_posix() for p in (self.root / "tests").glob("test_omega*.py")}
        for relative in sorted(paths):
            data = checked_path(self.root, relative).read_bytes()
            historical = self.command(["git", "show", f"{self.head}:{relative}"])
            if data != historical:
                raise ValueError(f"unbound source bytes: {relative}")
            self.sources.append({"path": relative, "bytes": len(data), "sha256": digest(data),
                                 "git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()})
        return {"inputs_bound": len(self.sources), "source_manifest_sha256": digest(canonical(self.sources))}

    def custody(self):
        self.script("validate_custody.py")
        self.script("resolve_custody.py")
        self.effective_hash = digest((self.root / "evidence/custody/generated/custody-effective-v1.jsonl").read_bytes())
        return {"ledger_validation": "PASS", "effective_state_sha256": self.effective_hash,
                "boundary": "schema and resolution validity do not close historical claims"}

    def contradiction(self):
        self.script("validate_formula_authorship_lineage.py")
        self.script("check_marte_historical_contract.py")
        self.script("find_hashing_claim_evidence.py")
        marte = read_json(self.root / "poc08-marte-contract-receipt.json")
        search = read_json(self.root / "poc10-search-receipt.json")
        self.findings = [
            {"id": "POC08-COMPLETE-APP", "observed": marte["runtime_bundle_state"],
             "parser": marte["parser_state"], "claim_allowed": False},
            {"id": "POC10-METRIC-SUPPORT", "candidate_count": len(search["strong_support_candidates"]),
             "boundary": "lexical candidate discovery is not metric validation", "claim_allowed": False},
        ]
        return {"findings": self.findings, "domain_state": "HOLD", "negative_evidence_preserved": True}

    def uncertainty(self):
        self.exams = validate_routes(read_json(self.root / "governance/omega-exams.v1.json"),
                                    read_json(self.root / "evidence/custody/gaps/gap-router.v1.json"))
        return {"open_exams": len(self.exams), "coverage": "legacy gaps plus current pipeline probes",
                "sigma_level": "TOKEN_VAZIO", "population_defect_rate": "TOKEN_VAZIO"}

    def reproduction(self):
        self.script("resolve_custody.py")
        replay = digest((self.root / "evidence/custody/generated/custody-effective-v1.jsonl").read_bytes())
        if replay != self.effective_hash:
            raise ValueError("effective custody replay changed bytes")
        return {"replay_sha256": replay, "class": "SAME_HOST_REPEAT", "independent_reproduction": "NOT_RUN"}

    def rollback(self):
        for ledger in LEDGERS:
            self.script("check_append_only.py", self.base_sha, ledger)
        return {"historical_ledgers_preserved": len(LEDGERS), "rollback_base": self.base_sha,
                "recovery": "revert implementation or append successor; retain receipts and historical bytes"}


def write_bundle(output, receipt):
    output.mkdir(parents=True, exist_ok=True)
    (output / "receipt.json").write_bytes(canonical(receipt))
    (output / "F_NEXT.json").write_bytes(canonical(receipt["F_next"]))
    summary = ["# Ω — receipt de execução", "", f"Estado técnico: **{receipt['pipeline_status']}**",
               "", "Promoção de claims: **HOLD / claim_allowed=false**", "",
               f"Source SHA: `{receipt['source_sha']}`", "", "| Gate | Estado |", "|---|---|"]
    summary += [f"| {r['id']} | {r['status']} |" for r in receipt["gates"]]
    summary += ["", "## Próximos exames", ""]
    summary += [f"- {r['id']}: {r.get('action', r.get('next_probe', 'consultar receipt'))}" for r in receipt["F_next"]]
    (output / "summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    files = sorted(p for p in output.iterdir() if p.is_file() and p.name != "SHA256SUMS")
    (output / "SHA256SUMS").write_text("".join(f"{digest(p.read_bytes())}  {p.name}\n" for p in files))


def run(root, output, base, expected_head, contract_path="governance/omega-pipeline.v1.json"):
    # Refuse to overwrite an older receipt, including a failed invocation.
    output.mkdir(parents=True, exist_ok=False)
    audit = Audit(root, output, base, expected_head, contract_path)
    error = None
    try:
        contract = validate_contract(read_json(checked_path(root, contract_path)))
        gates = schedule(contract["gates"], audit.execute)
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        gates = [{"id": key, "status": "BLOCKED", "reason": error,
                  "next_probe": "Restaurar contrato versionado e repetir em diretório novo.",
                  "claim_allowed": False} for key in STAGES]
    ok = all(row["status"] == "PASS" for row in gates)
    failures = [{"id": "EXAM-" + row["id"].upper(), "priority": "P0", "state": "OPEN",
                 "action": row["next_probe"], "failure_condition": row.get("reason", "gate failed"),
                 "claim_allowed": False} for row in gates if row["status"] != "PASS"]
    receipt = {
        "schema": "rafaelia.omega-execution-receipt.v1", "repository": REPOSITORY,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "pipeline_status": "PASS_SCOPED" if ok else "FAIL_CLOSED",
        "claim_allowed": False, "promotion_state": "HOLD", "source_sha": audit.head,
        "requested_sha": expected_head, "base_sha": audit.base_sha,
        "parent_ref": f"git:{base}", "error": error,
        "environment": {"python": platform.python_version(), "platform": platform.platform(),
                        "run_id": os.environ.get("GITHUB_RUN_ID", "LOCAL"),
                        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "1"),
                        "event_sha": os.environ.get("GITHUB_SHA", "TOKEN_VAZIO")},
        "sources": audit.sources, "commands": audit.commands, "gates": gates,
        "contradictions": audit.findings,
        "metrics": {"passed_gates": sum(row["status"] == "PASS" for row in gates),
                    "applicable_gates": len(STAGES), "open_exams": len(audit.exams),
                    "sigma_level": "TOKEN_VAZIO"},
        "F_ok": [row["id"] for row in gates if row["status"] == "PASS"],
        "F_gap": [r["id"] for r in failures + audit.exams],
        "F_next": failures + audit.exams, "stop": "RECEIPT_AND_F_NEXT",
    }
    artifacts = {
        "poc08-marte-contract-receipt.json": "check_marte_historical_contract.py",
        "poc10-search-receipt.json": "find_hashing_claim_evidence.py",
        "evidence/custody/generated/custody-effective-v1.jsonl": "resolve_custody.py",
    }
    for name, script in artifacts.items():
        # Never reuse a stale artifact from a failed/skipped command.
        if any(r["status"] == "PASS" and f"scripts/audit/{script}" in r["argv"] for r in audit.commands):
            try:
                (output / Path(name).name).write_bytes((root / name).read_bytes())
            except OSError as exc:
                ok = False
                receipt["pipeline_status"] = "FAIL_CLOSED"
                receipt["F_gap"].append("ARTIFACT_UNAVAILABLE:" + name)
                receipt["F_next"].append({"id":"EXAM-ARTIFACT", "priority":"P0",
                                           "action":f"Reexecutar {script} e conferir a saída {name}.",
                                           "reason":str(exc), "claim_allowed":False})
    write_bundle(output, receipt)
    print(json.dumps({"pipeline_status": receipt["pipeline_status"], "receipt": str(output / "receipt.json"),
                      "claim_allowed": False, "gates": receipt["metrics"]}))
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="full ancestor SHA; never inferred")
    parser.add_argument("--head", required=True, help="exact source SHA to audit")
    parser.add_argument("--out", required=True, type=Path, help="new output directory")
    args = parser.parse_args()
    return run(ROOT, args.out.resolve(), args.base, args.head)


if __name__ == "__main__":
    raise SystemExit(main())
