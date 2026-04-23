# 03 — Regex Engine (Thompson's Construction)

**Theory reference:** Sipser 1.3, Theorem 1.54 (Kleene). Regex ↔ NFA ↔ DFA equivalence.

## What you're building

A regex engine with three stages:

1. **parser.py** — regex string → AST (`Char`, `Concat`, `Alt`, `Star`).
2. **thompson.py** — AST → NFA via Thompson's construction.
3. **match.py** — simulate the NFA (or the derived DFA) against an input.

## The payoff benchmark

```python
# benchmark.py
pattern = "a?" * 25 + "a" * 25
string  = "a" * 25
# Python's re: >60s (catastrophic backtracking)
# Yours:       <1ms (tracks a set of NFA states)
```

Ref: Russ Cox, *Regular Expression Matching Can Be Simple And Fast*.

## Supported syntax (start small)

- Concatenation: `ab`
- Alternation: `a|b`
- Kleene star: `a*`
- Grouping: `(ab)*`

Level-up: `+`, `?`, character classes `[a-z]`.

## Gotcha

Preprocess the regex by inserting explicit concatenation operators. `ab` → `a·b`. Then the parser is a plain shunting-yard or recursive-descent over `·`, `|`, `*`.

## Run

```bash
python match.py "a(b|c)*" "abccb"
python benchmark.py
```
