"""Exercise structural-checker failures; these are not model behavior tests."""

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "scripts"))

from check_agent_design_skills import CASE_PATH, SKILLS, check_repository


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


if __name__ == "__main__":
    unittest.main()
