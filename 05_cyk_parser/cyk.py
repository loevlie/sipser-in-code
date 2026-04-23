"""Cocke–Younger–Kasami membership algorithm.

Assumes grammar is already in CNF. See cnf_converter.py for the reduction.
"""

from __future__ import annotations

import sys
from typing import List

from beartype import beartype

from cfg import CFG, load


@beartype
def recognize(g: CFG, tokens: list[str]) -> bool:
    """Return True iff `tokens` is derivable from g.start under g (CNF)."""
    raise NotImplementedError


@beartype
def chart(g: CFG, tokens: list[str]) -> list[list[set[str]]]:
    """Return the filled CYK chart; handy for debugging and parse-tree recovery."""
    raise NotImplementedError


if __name__ == "__main__":
    g = load(sys.argv[1])
    # Treat each character as a separate token by default.
    toks = list(sys.argv[2])
    print("accept" if recognize(g, toks) else "reject")
