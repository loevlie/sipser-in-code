"""Convert a general CFG to Chomsky Normal Form (Sipser Theorem 2.9).

Steps:
  1. Add a new start symbol S0 → S.
  2. Remove ε-productions (except at the new start).
  3. Remove unit productions A → B.
  4. Break up long RHSs: A → X1 X2 X3 X4  becomes  A → X1 A1, A1 → X2 A2, ...
  5. Replace terminals in length-≥2 RHSs with fresh nonterminals wrapping them.
"""

from __future__ import annotations

from beartype import beartype

from cfg import CFG


@beartype
def to_cnf(g: CFG) -> CFG:
    raise NotImplementedError
