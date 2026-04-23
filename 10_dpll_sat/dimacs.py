"""DIMACS CNF format reader / writer.

File shape:
    c comment lines
    p cnf <num_vars> <num_clauses>
    <literal>* 0     # one clause per line, 0-terminated
"""

from __future__ import annotations

from pathlib import Path

from beartype import beartype

Literal = int  # positive = variable, negative = its negation
Clause = list[Literal]
Formula = list[Clause]


@beartype
def read(path: str | Path) -> tuple[int, Formula]:
    """Return (num_vars, clauses)."""
    raise NotImplementedError


@beartype
def write(path: str | Path, num_vars: int, clauses: Formula) -> None:
    raise NotImplementedError
