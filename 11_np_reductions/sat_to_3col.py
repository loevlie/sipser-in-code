"""Reduction 3-SAT → 3-COLOR.

Classical gadget construction (see Sipser 7.30-style problems):
  - Three "palette" nodes True/False/Base, pairwise connected.
  - For each variable x: two nodes x, ¬x connected to each other and to Base.
    In any 3-coloring, {x, ¬x} are forced to {True, False}.
  - Each clause (a ∨ b ∨ c) gets an OR-gadget ensuring at least one literal
    receives the True color.

Exposes:
  reduce(clauses)   -> ColoringInstance
  decode(coloring)  -> dict[int, bool]    (maps variable id to its boolean value)
"""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "10_dpll_sat"))
from dimacs import Formula  # noqa: E402

from instances import ColoringInstance  # noqa: E402


@beartype
def reduce(clauses: Formula) -> ColoringInstance:
    raise NotImplementedError


@beartype
def decode(coloring: dict[int, int]) -> dict[int, bool]:
    """Given a 3-coloring of the gadget graph, recover the 3-SAT assignment."""
    raise NotImplementedError
