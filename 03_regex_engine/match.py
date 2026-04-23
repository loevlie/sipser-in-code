"""Match a string against a compiled regex NFA."""

from __future__ import annotations

from beartype import beartype

from parser import parse
from thompson import NFA, compile_to_nfa


@beartype
def epsilon_closure(nfa: NFA, states: set[int]) -> set[int]:
    raise NotImplementedError


@beartype
def match_nfa(nfa: NFA, s: str) -> bool:
    """Simulate the NFA by tracking a set of live states."""
    raise NotImplementedError


@beartype
def fullmatch(pattern: str, s: str) -> bool:
    return match_nfa(compile_to_nfa(parse(pattern)), s)


if __name__ == "__main__":
    import sys

    print("match" if fullmatch(sys.argv[1], sys.argv[2]) else "no match")
