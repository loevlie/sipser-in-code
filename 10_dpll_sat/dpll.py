"""Davis–Putnam–Logemann–Loveland SAT solver.

Represent clauses as list[list[int]] where positive ints are variables and
negative ints are their negations. Assignments are dict[int, bool].
"""

from __future__ import annotations

import sys

from beartype import beartype

from dimacs import Clause, Formula, read


@beartype
def unit_propagate(
    clauses: Formula, assignment: dict[int, bool]
) -> tuple[Formula | None, dict[int, bool]]:
    """Repeat unit propagation to a fixed point. Return (None, _) on conflict."""
    raise NotImplementedError


@beartype
def pure_literal_eliminate(
    clauses: Formula, assignment: dict[int, bool]
) -> tuple[Formula, dict[int, bool]]:
    raise NotImplementedError


@beartype
def simplify(clauses: Formula, var: int, value: bool) -> Formula:
    """Drop satisfied clauses; strip the falsified literal from the rest."""
    raise NotImplementedError


@beartype
def pick_variable(clauses: Formula) -> int:
    """Heuristic choice (e.g., most frequent literal)."""
    raise NotImplementedError


@beartype
def dpll(clauses: Formula, assignment: dict[int, bool] | None = None) -> dict[int, bool] | None:
    """Return a satisfying assignment, or None if UNSAT."""
    raise NotImplementedError


if __name__ == "__main__":
    num_vars, clauses = read(sys.argv[1])
    result = dpll(clauses)
    if result is None:
        print("UNSAT")
    else:
        print("SAT")
        print(" ".join(f"{v if result[v] else -v}" for v in sorted(result)))
