"""Tests for the DFA/NFA simulator."""

from pathlib import Path

import pytest

from automaton import load
from simulator import run
from subset_construct import nfa_to_dfa

EXAMPLES = Path(__file__).parent.parent / "examples"


@pytest.mark.xfail(reason="skeleton: implement simulator.run_dfa first")
def test_even_ones_accepts_empty():
    fa = load(EXAMPLES / "even_ones.json")
    assert run(fa, "") is True


@pytest.mark.xfail(reason="skeleton: implement simulator.run_dfa first")
def test_even_ones_rejects_odd_count():
    fa = load(EXAMPLES / "even_ones.json")
    assert run(fa, "111") is False


@pytest.mark.xfail(reason="skeleton: implement NFA simulation first")
def test_contains_101_nfa():
    fa = load(EXAMPLES / "contains_101.json")
    assert run(fa, "0001010") is True
    assert run(fa, "1111") is False


@pytest.mark.xfail(reason="skeleton: implement subset construction first")
def test_subset_construction_preserves_language():
    nfa = load(EXAMPLES / "contains_101.json")
    dfa = nfa_to_dfa(nfa)
    for w in ["", "101", "1010", "0001010", "11"]:
        assert run(nfa, w) == run(dfa, w)
