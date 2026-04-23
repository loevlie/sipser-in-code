"""NFA → DFA via the subset construction (Sipser Theorem 1.39).

States of the resulting DFA are subsets of the NFA's states, reachable from
ε-closure({q0}) under the transition function.
"""

from __future__ import annotations

from beartype import beartype

from automaton import Automaton


@beartype
def nfa_to_dfa(nfa: Automaton) -> Automaton:
    raise NotImplementedError
