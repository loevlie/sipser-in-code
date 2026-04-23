# 09 — Untyped λ-Calculus Interpreter

**Theory reference:** Sipser 3.3. A second Turing-complete model with nothing but substitution. Churches' thesis says "computable" means the same thing here as on a TM — and once you've built this, you've verified it.

## Syntax

```
term := var | (λ var . term) | (term term)
```

Three cases. Everything else (numbers, booleans, recursion) is encoded.

## Goal

- Parse a term from text.
- Rename bound variables to avoid capture (α-conversion).
- Perform β-reduction to normal form (when one exists).
- Run Church numerals: define `0`, `1`, `succ`, `plus`, `mult`, verify `mult 2 3 ≡ 6` by β-normalizing.

## Run

```bash
python lambda_repl.py
> let two = λf.λx.f (f x)
> let three = λf.λx.f (f (f x))
> let mult = λm.λn.λf.m (n f)
> mult two three
λf.λx.f (f (f (f (f (f x)))))
```

## Level-up

- Y-combinator: implement factorial and Fibonacci using recursion-from-fixed-point.
- Normal-order vs. applicative-order reduction; show where the latter diverges.
- de Bruijn indices instead of named variables (no α-renaming needed).
