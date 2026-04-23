# 04 — DFA Minimization (Hopcroft)

**Theory reference:** Myhill–Nerode theorem (Sipser problem 1.52). Minimization produces the unique (up to isomorphism) smallest DFA for a regular language.

## What you're building

Hopcroft's partition-refinement algorithm. Start with the partition `{accept, non-accept}`, then repeatedly refine by splitting any block whose members disagree on where some symbol sends them.

## Pairs well with

- Project 01 (consumes DFAs in the same JSON format)
- Project 03 (minimize the DFA produced by subset construction on a regex's NFA; compare state counts before/after)

## Run

```bash
python hopcroft.py ../01_dfa_nfa/examples/contains_101.json
# Prints: original states=N, minimized states=M
```

## Level-up

- Graphviz side-by-side rendering of pre- and post-minimization DFAs.
- Confirm empirically that minimizing `(a|b)*abb` yields the textbook 4-state DFA.
