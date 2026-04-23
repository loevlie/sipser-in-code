"""Render a DFA to Graphviz SVG. Useful for before/after minimization diffs."""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "01_dfa_nfa"))
from automaton import Automaton  # noqa: E402


@beartype
def to_dot(dfa: Automaton, name: str = "DFA") -> str:
    """Return a Graphviz DOT source string."""
    raise NotImplementedError
