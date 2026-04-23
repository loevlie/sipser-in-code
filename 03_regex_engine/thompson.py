"""AST → NFA via Thompson's construction.

Each sub-NFA has exactly one start and one accept state. Four cases:
  Char(a):    start --a--> accept
  Concat:     ε-link N(L).accept → N(R).start
  Alt:        new_start -ε-> N(L).start, -ε-> N(R).start
              N(L).accept, N(R).accept -ε-> new_accept
  Star:       new_start -ε-> N(X).start and -ε-> new_accept
              N(X).accept -ε-> N(X).start and -ε-> new_accept
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import count

from beartype import beartype

from ast_nodes import Regex


@beartype
@dataclass
class NFA:
    start: int
    accept: int
    # transitions[state][symbol] -> list[state]; "" means ε
    transitions: dict[int, dict[str, list[int]]] = field(default_factory=dict)


@beartype
def compile_to_nfa(r: Regex) -> NFA:
    """Thompson construct: dispatch on node type, glue sub-NFAs."""
    raise NotImplementedError
