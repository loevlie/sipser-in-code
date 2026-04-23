# 01 — DFA / NFA Simulator

**Theory reference:** Sipser Chapter 1.1–1.2. Formal definitions of DFA and NFA (5-tuple `(Q, Σ, δ, q₀, F)`), ε-transitions, and the subset construction (Theorem 1.39).

## What you're building

A simulator for finite automata read from JSON files, plus an NFA-to-DFA converter.

## Layout

```
01_dfa_nfa/
├── automaton.py        # load / represent automata
├── simulator.py        # run DFA or NFA against an input string
├── subset_construct.py # NFA → DFA (Theorem 1.39)
├── examples/           # sample automata as JSON
├── tests/              # pytest
└── requirements.txt
```

## JSON format

```json
{
  "type": "DFA",
  "states": ["q0", "q1"],
  "alphabet": ["0", "1"],
  "transitions": { "q0": {"0": "q0", "1": "q1"} },
  "start": "q0",
  "accept": ["q1"]
}
```

NFA transitions map each `(state, symbol)` to a **list** of states; use `""` for ε.

## Run

```bash
python -m simulator examples/even_ones.json 1010
pytest
```

## Conventions

Public functions are annotated and decorated with `@beartype` for runtime type checking — catches bad JSON inputs and wrong call sites at the first violation instead of deep inside the simulator.

## Level-up

- Render automata with Graphviz (`pip install graphviz`).
- Add a small CLI: `fa run <file> <string>` and `fa nfa2dfa <file>`.
