"""Reduction 3-SAT → SUBSET-SUM (Sipser Theorem 7.56).

Build decimal numbers with one column per variable and one column per clause.
Each variable x_i contributes two numbers (x_i, ¬x_i), each with a 1 in the
variable column and 1s in the columns of clauses it satisfies.
Each clause contributes two "slack" numbers. Target is chosen so that
subset sums equal it iff the formula is satisfiable.
"""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "10_dpll_sat"))
from dimacs import Formula  # noqa: E402

from instances import SubsetSumInstance  # noqa: E402


@beartype
def reduce(clauses: Formula) -> SubsetSumInstance:
    raise NotImplementedError


@beartype
def decode(chosen_indices: set[int], num_vars: int) -> dict[int, bool]:
    raise NotImplementedError
