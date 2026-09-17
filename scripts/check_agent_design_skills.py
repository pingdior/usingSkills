#!/usr/bin/env python3
"""Check the v2 agent-design bundle's structural contracts using only stdlib.

This checks the simple single-line frontmatter fields used in this bundle, not
arbitrary YAML. It does not evaluate prose semantics or execute model scenarios.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


SKILLS = (
    "seed-extraction",
    "seed-convergence",
    "digital-life-service-design",
    "harness-design",
    "retention-diagnosis-loop",
)
CASE_PATH = Path("evals/agent-design/cases.json")
EVIDENCE_PATH = Path("harness-design/references/mechanism-evidence.json")
MECHANISM_PATH = Path("harness-design/references/mechanisms.md")
EVIDENCE_STATUSES = {
    "source_behavior": {"design_recommendation", "article_reported"},
    "existing_tests": {"not_identified", "article_reported"},
    "runtime_benefit": {"unmeasured"},
}
CONTRACT_PATHS = (
    "seed-extraction/references/seed-contract.md",
    "harness-design/references/runtime-contract.md",
    "retention-diagnosis-loop/references/measurement.md",
    "retention-diagnosis-loop/references/memory-lifecycle.md",
)
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    skill_count: int = 0
    link_count: int = 0
    mechanism_count: int = 0
    source_count: int = 0
    related_method_count: int = 0
    case_count: int = 0


def check_entrypoint(path: Path, expected_name: str, report: Report) -> None:
    if not path.is_file():
        report.errors.append(f"Missing entrypoint: {expected_name}/SKILL.md")
        return
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        report.errors.append(f"Missing frontmatter boundaries: {expected_name}")
        return
    header = "\n".join(lines[1:lines.index("---", 1)])
    for key in ("name", "description"):
        matches = re.findall(rf"^{key}: (.+)$", header, re.MULTILINE)
        if len(matches) != 1:
            report.errors.append(f"Expected one single-line {key}: {expected_name}")
            continue
        value = matches[0].strip()
        if key == "name" and value != expected_name:
            report.errors.append(f"Name/directory mismatch: {expected_name}")
        if key == "description" and (
            not value or len(value) > 1024 or "<" in value or ">" in value
        ):
            report.errors.append(f"Invalid description length or tags: {expected_name}")
    versions = re.findall(r"^  version: (.+)$", header, re.MULTILINE)
    if len(versions) != 1 or not re.fullmatch(r"2\.\d+\.\d+", versions[0]):
        report.errors.append(f"Expected a v2 semantic version: {expected_name}")
    report.skill_count += 1


def check_links(root: Path, path: Path, report: Report) -> None:
    for raw_target in LINK.findall(path.read_text(encoding="utf-8")):
        parsed = urlsplit(raw_target.strip("<>"))
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        source = path.relative_to(root)
        if not target.is_relative_to(root):
            report.errors.append(f"Reference escapes repository: {source}: {raw_target}")
        elif not target.is_file():
            report.errors.append(f"Broken file reference: {source}: {raw_target}")
        else:
            report.link_count += 1


def check_cases(root: Path, report: Report) -> None:
    path = root / CASE_PATH
    if not path.is_file():
        report.errors.append(f"Missing scenario specification: {CASE_PATH}")
        return
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        report.errors.append(f"Invalid scenario JSON: {exc}")
        return
    if not isinstance(spec, dict):
        report.errors.append("Scenario specification must be an object")
        return
    if spec.get("schema_version") != "agent-design-eval/v1":
        report.errors.append("Unknown scenario schema_version")
    if spec.get("evaluation_kind") != "design_responses":
        report.errors.append("Scenario suite must identify its design-response scope")
    cases = spec.get("cases")
    if not isinstance(cases, list) or not cases:
        report.errors.append("Scenario cases must be a nonempty list")
        return
    ids: list[str] = []
    covered: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            report.errors.append(f"Case {index} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9-]+", case_id):
            report.errors.append(f"Invalid case id at index {index}")
        else:
            ids.append(case_id)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            report.errors.append(f"Missing prompt: {case_id}")
        if "setup" in case and (
            not isinstance(case["setup"], str) or not case["setup"].strip()
        ):
            report.errors.append(f"Invalid setup: {case_id}")
        skills = case.get("skills")
        if not isinstance(skills, list) or not skills:
            report.errors.append(f"Missing skills: {case_id}")
        else:
            for skill in skills:
                if not isinstance(skill, str) or skill not in SKILLS:
                    report.errors.append(f"Unknown skill in {case_id}: {skill!r}")
                else:
                    covered.add(skill)
        for key in ("expected", "hard_failures"):
            items = case.get(key)
            if not isinstance(items, list) or not items or any(
                not isinstance(item, str) or not item.strip() for item in items
            ):
                report.errors.append(f"Missing behavioral criteria {key}: {case_id}")
    for case_id, count in Counter(ids).items():
        if count > 1:
            report.errors.append(f"Duplicate case id: {case_id}")
    for skill in sorted(set(SKILLS) - covered):
        report.errors.append(f"No scenario covers skill: {skill}")
    report.case_count = len(cases)


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_date(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def indexed_records(value: object, label: str, pattern: str, report: Report) -> dict:
    """Reject malformed entries without crashing the rest of the audit."""
    records = {}
    if not isinstance(value, list) or not value:
        report.errors.append(f"{label} must be a nonempty list")
        return records
    for index, record in enumerate(value):
        if not isinstance(record, dict):
            report.errors.append(f"{label}[{index}] must be an object")
            continue
        record_id = record.get("id")
        if not isinstance(record_id, str) or not re.fullmatch(pattern, record_id):
            report.errors.append(f"Invalid {label} id at index {index}")
            continue
        if record_id in records:
            report.errors.append(f"Duplicate {label} id: {record_id}")
        records[record_id] = record
    return records


def check_evidence_dimensions(record: dict, label: str, sources: dict, report: Report) -> None:
    for dimension, allowed_statuses in EVIDENCE_STATUSES.items():
        evidence = record.get(dimension)
        location = f"{label}.{dimension}"
        if not isinstance(evidence, dict) or not evidence:
            report.errors.append(f"Missing evidence dimension: {location}")
            continue
        status = evidence.get("status")
        if not isinstance(status, str) or status not in allowed_statuses:
            report.errors.append(f"Unsupported evidence status: {location}: {status!r}")
        if not nonempty_string(evidence.get("summary")):
            report.errors.append(f"Missing evidence summary: {location}")
        if dimension == "runtime_benefit":
            metrics = evidence.get("metrics")
            if not isinstance(metrics, list) or not metrics or not all(map(nonempty_string, metrics)):
                report.errors.append(f"Missing benefit metrics: {location}")
            continue
        refs = evidence.get("source_ids")
        if not isinstance(refs, list):
            report.errors.append(f"Evidence source_ids must be a list: {location}")
            continue
        if status == "article_reported" and not refs:
            report.errors.append(f"Article-reported evidence requires sources: {location}")
        seen = set()
        for ref in refs:
            if not isinstance(ref, str) or ref not in sources:
                report.errors.append(f"Unknown evidence source: {location}: {ref!r}")
                continue
            if ref in seen:
                report.errors.append(f"Duplicate evidence source reference: {location}: {ref}")
            seen.add(ref)


def check_mechanism_evidence(root: Path, report: Report) -> None:
    path = root / EVIDENCE_PATH
    if not path.is_file():
        report.errors.append(f"Missing mechanism evidence: {EVIDENCE_PATH}")
        return
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        report.errors.append(f"Invalid evidence JSON: {exc}")
        return
    if not isinstance(spec, dict):
        report.errors.append("Evidence registry must be an object")
        return
    if spec.get("schema_version") != "harness-mechanism-evidence/v1":
        report.errors.append("Unknown evidence schema_version")
    if not valid_date(spec.get("reviewed_at")):
        report.errors.append("Invalid evidence reviewed_at date")
    if not nonempty_string(spec.get("local_validation_scope")):
        report.errors.append("Missing local_validation_scope")
    sources = indexed_records(spec.get("sources"), "evidence source", r"[a-z0-9-]+", report)
    for source_id, source in sources.items():
        for key in ("title", "verification_boundary"):
            if not nonempty_string(source.get(key)):
                report.errors.append(f"Missing source {key}: {source_id}")
        for key in ("published_at", "reviewed_at"):
            if not valid_date(source.get(key)):
                report.errors.append(f"Invalid source {key}: {source_id}")
        if source.get("kind") != "implementation_walkthrough":
            report.errors.append(f"Unsupported source kind: {source_id}")
        url = source.get("url")
        try:
            parsed = urlsplit(url) if isinstance(url, str) else None
            valid_url = parsed is not None and parsed.scheme == "https" and bool(parsed.hostname)
            valid_url = valid_url and parsed.username is None and parsed.password is None
        except ValueError:
            valid_url = False
        if not valid_url:
            report.errors.append(f"Invalid source URL: {source_id}")
    mechanisms = indexed_records(spec.get("mechanisms"), "mechanism evidence", r"[0-9]{3}", report)
    related = indexed_records(spec.get("related_methods"), "related method", r"[a-z0-9-]+", report)
    for label, records in (("mechanism", mechanisms), ("related method", related)):
        for record_id, record in records.items():
            if not nonempty_string(record.get("name")):
                report.errors.append(f"Missing evidence name: {label} {record_id}")
            check_evidence_dimensions(record, f"{label} {record_id}", sources, report)
    for method_id, method in related.items():
        if method.get("owner_skill") not in SKILLS:
            report.errors.append(f"Unknown related method owner_skill: {method_id}")
    table = root / MECHANISM_PATH
    if not table.is_file():
        report.errors.append(f"Missing mechanism table: {MECHANISM_PATH}")
    else:
        rows = re.findall(r"^\| (\d+) \| ([^|\n]+) \|", table.read_text(encoding="utf-8"), re.MULTILINE)
        table_entries = {key: name.strip() for key, name in rows}
        if len(rows) != len(table_entries):
            report.errors.append("Mechanism registry table contains duplicate ids")
        evidence_entries = {key: record.get("name") for key, record in mechanisms.items()}
        if table_entries != evidence_entries:
            report.errors.append("Mechanism registry table and evidence ids/names must match one-to-one")
    report.mechanism_count = len(mechanisms)
    report.source_count = len(sources)
    report.related_method_count = len(related)


def check_repository(root: Path) -> Report:
    root = root.resolve()
    report = Report()
    for skill in SKILLS:
        check_entrypoint(root / skill / "SKILL.md", skill, report)
        for path in sorted((root / skill).rglob("*.md")):
            check_links(root, path, report)
    for relative in CONTRACT_PATHS:
        if not (root / relative).is_file():
            report.errors.append(f"Missing shared contract: {relative}")
    check_mechanism_evidence(root, report)
    check_cases(root, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    report = check_repository(args.root)
    if report.errors:
        for error in report.errors:
            print(f"ERROR: {error}")
        return 1
    print(
        f"OK: {report.skill_count} entrypoints, {report.link_count} local file links, "
        f"{report.mechanism_count} mechanisms, {report.related_method_count} related methods, "
        f"{report.source_count} evidence sources, {report.case_count} scenario specifications."
    )
    print("Structural checks only; model behavior and runtime side effects were not evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
