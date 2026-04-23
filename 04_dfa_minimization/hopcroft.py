"""Hopcroft's DFA minimization.

Partition states into equivalence classes under indistinguishability.
Start: P = { F, Q \\ F }.
Refine: split a block B by any (symbol a, target-block T) where some states
in B go into T on a and others don't. Continue until stable.
"""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype

# Reuse the shared Automaton dataclass from project 01.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "01_dfa_nfa"))
from automaton import Automaton, load  # noqa: E402


@beartype
def minimize(dfa: Automaton) -> Automaton:
    """Return an equivalent DFA with the minimum number of states."""
    raise NotImplementedError


if __name__ == "__main__":
    dfa = load(sys.argv[1])
    mini = minimize(dfa)
    print(f"original states={len(dfa.states)}  minimized states={len(mini.states)}")
