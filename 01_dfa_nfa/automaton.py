"""Load and represent finite automata from JSON."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from beartype import beartype


@beartype
@dataclass
class Automaton:
    kind: Literal["DFA", "NFA"]
    states: set[str]
    alphabet: set[str]
    # DFA: transitions[state][symbol] -> state (str)
    # NFA: transitions[state][symbol] -> list[state]; "" means ε
    transitions: dict[str, dict[str, object]]
    start: str
    accept: set[str]


@beartype
def load(path: str | Path) -> Automaton:
    """Parse a JSON file into an Automaton."""
    raise NotImplementedError
