# 06 — tinylang: a Mini-Compiler

**Theory reference:** Sipser 2.1–2.2 (CFGs and PDAs) and 3.1 (Turing-equivalent computation). Lexing ↔ regular languages. Recursive-descent parsing ↔ pushdown automata. Interpretation of loops + conditionals + unbounded state ↔ Turing machines.

## The language

```
let x = 2 + 3 * 4;
let y = x * x;
print y;
if y > 10 { print "big"; } else { print "small"; }
while x > 0 { let x = x - 1; print x; }
```

Integers, strings, boolean comparisons, arithmetic, `let`/`print`/`if`/`while`.

## Pipeline

| Stage | File | TOC concept |
|-------|------|-------------|
| Lex | `lexer.py` | Regular languages (one big DFA over the source) |
| Parse | `parser.py` | Recursive descent ≡ PDA |
| Eval | `interpreter.py` | AST walk; Turing-equivalent with loops |

## Run

```bash
python repl.py
python interpreter.py examples/factorial.tiny
```

## Level-up

- Add a static type checker over the AST.
- Compile to a bytecode VM instead of tree-walking.
- Error messages with line/column (lexer already tracks position).
