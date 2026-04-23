# 11 — NP-Reduction Library

**Theory reference:** Sipser 7.4 (NP-completeness) and the classical 3-SAT reductions. The theorems say "A ≤ₚ B"; this project makes the reduction a runnable function.

## What you're building

Executable, verifiable reductions from 3-SAT to several classic NP-complete problems.

| Reduction | File | Theorem |
|-----------|------|---------|
| 3-SAT → 3-COLOR | `sat_to_3col.py` | Sipser 7.30-ish construction |
| 3-SAT → CLIQUE | `sat_to_clique.py` | Sipser Theorem 7.32 |
| 3-SAT → SUBSET-SUM | `sat_to_subsetsum.py` | Sipser Theorem 7.56 |

Each module exposes `reduce(formula) -> Instance` and `decode(certificate) -> Assignment` so you can chain: solve 3-SAT with `10_dpll_sat/`, or solve the target problem directly and use the decoder to recover a satisfying assignment.

## The round-trip check

For every reduction, include a test: start with a 3-CNF formula F, reduce to instance I, solve I by brute force (small inputs only), decode to an assignment, and verify it actually satisfies F. If all three agree, the reduction is correct.

## Run

```bash
python -m pytest
python sat_to_3col.py examples/tiny.cnf  # prints the graph
```

## Level-up

- Chain the reductions: 3-SAT → 3-COLOR → SAT → CLIQUE. Visualize each intermediate instance.
- Reduce a natural problem like "exam scheduling" to 3-COLOR to k-SAT to SAT, then hand it to `10_dpll_sat/` and get an actual schedule back.
