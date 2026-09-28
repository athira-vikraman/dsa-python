"""
Run every demo and the full test suite, in order.

    python3 run_all.py            # demos + tests
    python3 run_all.py --tests    # tests only
    python3 run_all.py --demos    # demos only
"""

import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
PYTHON = sys.executable


def banner(text):
    # flush so our headings stay interleaved with the subprocess output
    print("\n" + "=" * 72, flush=True)
    print(f"  {text}", flush=True)
    print("=" * 72, flush=True)


def run(args, label):
    banner(label)
    result = subprocess.run([PYTHON, *args], cwd=ROOT)
    return result.returncode == 0


def main():
    flag = sys.argv[1] if len(sys.argv) > 1 else ""
    run_demos = flag != "--tests"
    run_tests = flag != "--demos"
    failures = []

    if run_demos:
        for path in sorted((ROOT / "code").glob("*.py")):
            if not run([str(path)], f"DEMO  {path.name}"):
                failures.append(path.name)
        if not run([str(ROOT / "exercises" / "solutions.py")], "DEMO  solutions.py"):
            failures.append("solutions.py")

    if run_tests:
        if not run(["-m", "unittest", "discover", "-s", "tests", "-v"], "TEST SUITE"):
            failures.append("tests")

    banner("SUMMARY")
    if failures:
        print("  FAILED: " + ", ".join(failures))
        return 1
    print("  Everything passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
