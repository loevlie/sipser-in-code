"""Reduction 3-SAT → CLIQUE (Sipser Theorem 7.32).

For a 3-CNF formula with m clauses:
  - Create a node for each literal occurrence (so 3m nodes).
  - Add an edge between two nodes u, v iff (a) they are in *different* clauses
    AND (b) they are not complementary literals.
  - Target clique size k = m.

A size-m clique picks one consistent literal per clause.
"""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "10_dpll_sat"))
from dimacs import Formula  # noqa: E402

from instances import CliqueInstance  # noqa: E402


@beartype
def reduce(clauses: Formula) -> CliqueInstance:
    raise NotImplementedError


@beartype
def decode(clique_nodes: set[int], clauses: Formula) -> dict[int, bool]:
    raise NotImplementedError
