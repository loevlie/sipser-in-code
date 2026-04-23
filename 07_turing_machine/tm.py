"""Single-tape deterministic Turing machine."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from beartype import beartype

Direction = Literal["L", "R"]
BLANK = "_"


@beartype
@dataclass
class TM:
    states: set[str]
    input_alphabet: set[str]
    tape_alphabet: set[str]
    start: str
    accept: str
    reject: str
    # (state, symbol) -> (next_state, write, direction)
    transitions: dict[tuple[str, str], tuple[str, str, str]] = field(default_factory=dict)


@beartype
def load(path: str | Path) -> TM:
    """Parse the text format described in README.md."""
    raise NotImplementedError


@beartype
def run(
    tm: TM,
    input_str: str,
    max_steps: int = 10_000,
    trace: bool = False,
) -> tuple[str, list[str], int]:
    """Return (outcome, final_tape, steps). Outcome ∈ {"accept","reject","timeout"}."""
    raise NotImplementedError


@beartype
def render(tape: list[str], head: int, state: str) -> str:
    cells = "".join(f"[{c}]" if i == head else f" {c} " for i, c in enumerate(tape))
    return f"{state:>12}  {cells}"


if __name__ == "__main__":
    import sys

    tm = load(sys.argv[1])
    trace = "--trace" in sys.argv
    outcome, tape, steps = run(tm, sys.argv[2], trace=trace)
    print(f"{outcome} after {steps} steps. tape: {''.join(tape)}")
