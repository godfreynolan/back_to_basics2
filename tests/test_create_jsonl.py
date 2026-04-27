import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "create_jsonl.py"
OUTPUT = ROOT / "input_data.jsonl"
TESTS_DIR = ROOT / "tests"


class CreateJsonlTests(unittest.TestCase):
    def test_runs_from_outside_repo_directory(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=TESTS_DIR,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Conversion to JSONL complete.", result.stdout)
        self.assertTrue(OUTPUT.exists())


if __name__ == "__main__":
    unittest.main()
