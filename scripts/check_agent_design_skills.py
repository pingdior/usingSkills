#!/usr/bin/env python3
"""Check the v2 agent-design bundle's structural contracts using only stdlib.

This checks the simple single-line frontmatter fields used in this bundle, not
arbitrary YAML. It does not evaluate prose semantics or execute model scenarios.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
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
    mechanisms = root / "harness-design/references/mechanisms.md"
    if mechanisms.is_file():
        ids = re.findall(r"^\| (\d{3}) \|", mechanisms.read_text(encoding="utf-8"), re.MULTILINE)
        expected = {f"{number:03}" for number in range(1, 22)}
        if set(ids) != expected or len(ids) != len(expected):
            report.errors.append("Mechanism registry must define 001–021 exactly once")
        report.mechanism_count = len(ids)
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
        f"{report.mechanism_count} mechanisms, {report.case_count} scenario specifications."
    )
    print("Structural checks only; model behavior and runtime side effects were not evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
