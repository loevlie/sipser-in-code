"""Run a DFA or NFA against an input string."""

from __future__ import annotations

from beartype import beartype

from automaton import Automaton


@beartype
def run(fa: Automaton, s: str) -> bool:
    if fa.kind == "DFA":
        return run_dfa(fa, s)
    return run_nfa(fa, s)


@beartype
def run_dfa(dfa: Automaton, s: str) -> bool:
    """Deterministic: single current state."""
    raise NotImplementedError


@beartype
def epsilon_closure(nfa: Automaton, states: set[str]) -> set[str]:
    """Set of states reachable from `states` via zero or more ε-moves."""
    raise NotImplementedError


@beartype
def run_nfa(nfa: Automaton, s: str) -> bool:
    """Nondeterministic: track a set of live states, closed under ε."""
    raise NotImplementedError


if __name__ == "__main__":
    import sys

    from automaton import load

    fa = load(sys.argv[1])
    print("accept" if run(fa, sys.argv[2]) else "reject")
