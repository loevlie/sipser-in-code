# 10 — DPLL SAT Solver

**Theory reference:** Sipser 7.4, Cook–Levin (7.5). SAT is the canonical NP-complete problem — every other NP problem reduces to it.

## What you're building

A Davis–Putnam–Logemann–Loveland solver for CNF formulas. Inputs are DIMACS `.cnf` files; output is SAT with an assignment or UNSAT.

## Algorithm

1. **Unit propagation:** any clause with a single literal forces that literal.
2. **Pure literal elimination:** a variable appearing with only one polarity can be assigned to satisfy those clauses.
3. **Branch:** pick an unassigned variable, try True; on conflict, try False.
4. **Base cases:** no clauses = SAT; an empty clause = conflict = UNSAT.

## Layout

```
10_dpll_sat/
├── dpll.py     # the solver
├── dimacs.py   # DIMACS .cnf reader
├── sudoku.py   # encode a 9×9 Sudoku as CNF, solve, decode
└── benchmarks/ # small SATLIB uf50-218 instances, etc.
```

## Run

```bash
python dpll.py benchmarks/uf50-01.cnf
python sudoku.py puzzles/easy.txt
```

## Level-up

- CDCL (Conflict-Driven Clause Learning): the upgrade that powers modern solvers.
- Watched literals for fast unit propagation.
- Reduce 3-COLOR → SAT (see `11_np_reductions/`) and solve graph coloring with this tool.
