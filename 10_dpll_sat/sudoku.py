"""Solve 9×9 Sudoku by reduction to SAT.

Encoding: variable v(r,c,d) = "cell (r,c) holds digit d" for r,c,d ∈ 1..9.
Then 9³ = 729 variables. Constraints:

  (1) each cell holds some digit          — for each (r,c): OR_d v(r,c,d)
  (2) each cell holds at most one digit   — for each (r,c), d1<d2: ¬v(r,c,d1) ∨ ¬v(r,c,d2)
  (3) each row contains each digit        — for each (r,d): OR_c v(r,c,d)
  (4) each column contains each digit     — dual of (3)
  (5) each 3×3 box contains each digit    — dual over boxes
  (6) given clues fixed as unit clauses.
"""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype

from dimacs import Formula
from dpll import dpll


@beartype
def var(r: int, c: int, d: int) -> int:
    """Map (row, col, digit) ∈ 1..9 to a DIMACS variable id."""
    return (r - 1) * 81 + (c - 1) * 9 + d


@beartype
def encode(grid: list[list[int]]) -> Formula:
    """Return a CNF formula asserting the grid has a valid completion."""
    raise NotImplementedError


@beartype
def decode(assignment: dict[int, bool]) -> list[list[int]]:
    """Recover the solved grid from the SAT assignment."""
    raise NotImplementedError


@beartype
def load_grid(path: str | Path) -> list[list[int]]:
    """Read a 9×9 grid, 0 for blank cells."""
    raise NotImplementedError


if __name__ == "__main__":
    grid = load_grid(sys.argv[1])
    result = dpll(encode(grid))
    if result is None:
        print("UNSOLVABLE")
    else:
        for row in decode(result):
            print(" ".join(str(d) for d in row))
