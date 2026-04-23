"""Run each DFA in the zoo against its YES/NO test sets."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from beartype import beartype

# Assumes project 01 is on PYTHONPATH (or installed as a package later).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "01_dfa_nfa"))
from automaton import load  # noqa: E402
from simulator import run  # noqa: E402

ZOO = Path(__file__).parent / "recognizers"
TESTS = Path(__file__).parent / "tests.json"


@beartype
def main() -> None:
    cases: dict[str, dict[str, list[str]]] = json.loads(TESTS.read_text())
    for name, sets in cases.items():
        fa = load(ZOO / f"{name}.json")
        for w in sets["yes"]:
            assert run(fa, w), f"{name}: expected accept for {w!r}"
        for w in sets["no"]:
            assert not run(fa, w), f"{name}: expected reject for {w!r}"
        print(f"{name}: OK")


if __name__ == "__main__":
    main()
