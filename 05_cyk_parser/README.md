# 05 — CYK Parser

**Theory reference:** Sipser 2.1. Context-free grammars, Chomsky Normal Form (Theorem 2.9), the membership problem for CFLs.

## What you're building

1. A CFG data type (`cfg.py`).
2. A CFG → CNF converter (`cnf_converter.py`). Sipser Theorem 2.9 in code.
3. A CYK recognizer (`cyk.py`). Given a grammar in CNF and a token list, decide membership in O(n³·|G|) time.

## CYK in one sentence

Fill an n×n table `T[i][j]` = set of nonterminals deriving `tokens[i..j]`, in increasing span length. The input is in the language iff the start symbol is in `T[0][n-1]`.

## Grammar format (JSON)

```json
{
  "start": "S",
  "rules": {
    "S": [["A", "B"], ["a"]],
    "A": [["a"]],
    "B": [["b"]]
  }
}
```

Each right-hand side is a list of symbols. In CNF every RHS has length 1 (terminal) or 2 (two nonterminals).

## Run

```bash
python cyk.py examples/palindrome_even.json aabbaa
python cnf_converter.py examples/raw_grammar.json
```

## Level-up

- Produce a parse tree, not just a yes/no answer.
- Pretty-print the CYK chart.
- Benchmark against an Earley parser for non-CNF grammars.
