"""Exercise structural-checker failures; these are not model behavior tests."""

import json
from copy import deepcopy
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "scripts"))

from check_agent_design_skills import CASE_PATH, EVIDENCE_PATH, MECHANISM_PATH, SKILLS, check_repository


class ContractCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for skill in SKILLS:
            shutil.copytree(REPOSITORY / skill, self.root / skill)
        (self.root / CASE_PATH).parent.mkdir(parents=True)
        shutil.copyfile(REPOSITORY / CASE_PATH, self.root / CASE_PATH)

    def change_cases(self, change):
        path = self.root / CASE_PATH
        spec = json.loads(path.read_text(encoding="utf-8"))
        change(spec)
        path.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")

    def change_evidence(self, change):
        path = self.root / EVIDENCE_PATH
        spec = json.loads(path.read_text(encoding="utf-8"))
        change(spec)
        path.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")

    def assert_error(self, fragment):
        errors = check_repository(self.root).errors
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_current_bundle_passes(self):
        report = check_repository(self.root)
        self.assertEqual([], report.errors)
        self.assertEqual(len(SKILLS), report.skill_count)

    def test_missing_cross_skill_contract_fails(self):
        (self.root / "seed-extraction/references/seed-contract.md").unlink()
        errors = check_repository(self.root).errors
        self.assertTrue(any("Broken file reference" in error for error in errors))
        self.assertTrue(any("Missing shared contract" in error for error in errors))

    def test_reference_outside_repository_fails(self):
        path = self.root / "seed-convergence/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[escape](../../outside.md)\n", encoding="utf-8")
        self.assertTrue(any("escapes repository" in error for error in check_repository(self.root).errors))

    def test_duplicate_mechanism_fails(self):
        path = self.root / "harness-design/references/mechanisms.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n| 008 | duplicate |\n", encoding="utf-8")
        self.assertTrue(any("Mechanism registry" in error for error in check_repository(self.root).errors))

    def test_duplicate_case_fails(self):
        self.change_cases(lambda spec: spec["cases"].append(spec["cases"][0]))
        self.assertTrue(any("Duplicate case id" in error for error in check_repository(self.root).errors))

    def test_unknown_case_skill_fails(self):
        self.change_cases(lambda spec: spec["cases"][0]["skills"].append("missing-skill"))
        self.assertTrue(any("Unknown skill" in error for error in check_repository(self.root).errors))

    def test_missing_behavioral_criteria_fails(self):
        self.change_cases(lambda spec: spec["cases"][0].update(expected=[]))
        self.assertTrue(any("Missing behavioral criteria" in error for error in check_repository(self.root).errors))

    def test_name_mismatch_fails(self):
        path = self.root / "seed-extraction/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace("name: seed-extraction", "name: wrong-name", 1), encoding="utf-8")
        self.assertTrue(any("Name/directory mismatch" in error for error in check_repository(self.root).errors))

    def test_invalid_case_document_fails(self):
        (self.root / CASE_PATH).write_text("[]", encoding="utf-8")
        self.assertTrue(any("must be an object" in error for error in check_repository(self.root).errors))

    def test_missing_evidence_registry_fails(self):
        (self.root / EVIDENCE_PATH).unlink()
        self.assert_error("Missing mechanism evidence")

    def test_missing_mechanism_evidence_fails(self):
        self.change_evidence(lambda spec: spec["mechanisms"].pop())
        self.assert_error("must match one-to-one")

    def test_every_evidence_dimension_is_required(self):
        baseline = (self.root / EVIDENCE_PATH).read_text(encoding="utf-8")
        for collection in ("mechanisms", "related_methods"):
            for dimension in ("source_behavior", "existing_tests", "runtime_benefit"):
                with self.subTest(collection=collection, dimension=dimension):
                    (self.root / EVIDENCE_PATH).write_text(baseline, encoding="utf-8")
                    self.change_evidence(lambda spec: spec[collection][0].pop(dimension))
                    self.assert_error("Missing evidence dimension")

    def test_duplicate_evidence_ids_fail(self):
        baseline = (self.root / EVIDENCE_PATH).read_text(encoding="utf-8")
        for collection, label in (("mechanisms", "mechanism evidence"), ("sources", "evidence source"), ("related_methods", "related method")):
            with self.subTest(collection=collection):
                (self.root / EVIDENCE_PATH).write_text(baseline, encoding="utf-8")
                self.change_evidence(lambda spec: spec[collection].append(spec[collection][0]))
                self.assert_error(f"Duplicate {label} id")

    def test_unknown_evidence_source_fails(self):
        self.change_evidence(lambda spec: spec["mechanisms"][0]["source_behavior"].update(source_ids=["unknown-source"]))
        self.assert_error("Unknown evidence source")

    def test_article_report_requires_source(self):
        baseline = (self.root / EVIDENCE_PATH).read_text(encoding="utf-8")
        for dimension in ("source_behavior", "existing_tests"):
            with self.subTest(dimension=dimension):
                (self.root / EVIDENCE_PATH).write_text(baseline, encoding="utf-8")
                self.change_evidence(lambda spec: spec["mechanisms"][0][dimension].update(status="article_reported", source_ids=[]))
                self.assert_error("Article-reported evidence requires sources")

    def test_table_registry_name_mismatch_fails(self):
        self.change_evidence(lambda spec: spec["mechanisms"][0].update(name="another mechanism"))
        self.assert_error("must match one-to-one")

    def test_registered_extra_mechanism_passes(self):
        # The registry, not a hard-coded maximum, controls table membership.
        spec = json.loads((self.root / EVIDENCE_PATH).read_text(encoding="utf-8"))
        extra = deepcopy(spec["mechanisms"][0])
        extra.update(id="028", name="New registered mechanism")
        self.change_evidence(lambda value: value["mechanisms"].append(extra))
        path = self.root / MECHANISM_PATH
        path.write_text(path.read_text(encoding="utf-8") + "\n| 028 | New registered mechanism |\n", encoding="utf-8")
        report = check_repository(self.root)
        self.assertEqual([], report.errors)
        self.assertEqual(len(spec["mechanisms"]) + 1, report.mechanism_count)

    def test_malformed_evidence_document_fails(self):
        for text, error in (("{", "Invalid evidence JSON"), ("[]", "must be an object")):
            with self.subTest(text=text):
                (self.root / EVIDENCE_PATH).write_text(text, encoding="utf-8")
                self.assert_error(error)

    def test_wrong_evidence_types_fail_without_crashing(self):
        baseline = (self.root / EVIDENCE_PATH).read_text(encoding="utf-8")
        changes = [
            lambda spec: spec.update(sources={}),
            lambda spec: spec["mechanisms"].append([]),
            lambda spec: spec["mechanisms"][0].update(id=[]),
            lambda spec: spec["mechanisms"][0]["source_behavior"].update(status=[]),
            lambda spec: spec["mechanisms"][0]["source_behavior"].update(source_ids="event-index"),
            lambda spec: spec["mechanisms"][0]["source_behavior"].update(source_ids=[[]]),
            lambda spec: spec["mechanisms"][0]["existing_tests"].update(summary=[]),
            lambda spec: spec["mechanisms"][0]["runtime_benefit"].update(metrics=[]),
        ]
        for index, change in enumerate(changes):
            with self.subTest(index=index):
                (self.root / EVIDENCE_PATH).write_text(baseline, encoding="utf-8")
                self.change_evidence(change)
                self.assertTrue(check_repository(self.root).errors)

    def test_unsubstantiated_evidence_status_upgrade_fails(self):
        baseline = (self.root / EVIDENCE_PATH).read_text(encoding="utf-8")
        for dimension, status in (("source_behavior", "directly_verified"), ("existing_tests", "locally_passed"), ("runtime_benefit", "measured")):
            with self.subTest(dimension=dimension):
                (self.root / EVIDENCE_PATH).write_text(baseline, encoding="utf-8")
                self.change_evidence(lambda spec: spec["mechanisms"][0][dimension].update(status=status))
                self.assert_error("Unsupported evidence status")

    def test_invalid_source_metadata_and_method_owner_fail(self):
        baseline = (self.root / EVIDENCE_PATH).read_text(encoding="utf-8")
        changes = [
            (lambda spec: spec["sources"][0].update(url="file:///tmp/source"), "Invalid source URL"),
            (lambda spec: spec["sources"][0].update(url="https://["), "Invalid source URL"),
            (lambda spec: spec["sources"][0].update(reviewed_at="2026-02-30"), "Invalid source reviewed_at"),
            (lambda spec: spec["sources"][0].update(verification_boundary=""), "Missing source verification_boundary"),
            (lambda spec: spec["related_methods"][0].update(owner_skill="unknown"), "Unknown related method owner_skill"),
        ]
        for index, (change, error) in enumerate(changes):
            with self.subTest(index=index):
                (self.root / EVIDENCE_PATH).write_text(baseline, encoding="utf-8")
                self.change_evidence(change)
                self.assert_error(error)


if __name__ == "__main__":
    unittest.main()
