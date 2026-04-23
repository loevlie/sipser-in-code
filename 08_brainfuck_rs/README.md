# 08 — Brainfuck Interpreter (Rust)

**Theory reference:** Sipser 3.3 — Turing-equivalence. Brainfuck has eight instructions operating on a byte tape and one data pointer, and it is Turing-complete. Build this and you've built a second model of computation, which is the whole point of the Church–Turing thesis.

## Why Rust here

Perfect "learn Rust" project:

- Tight instruction-dispatch loop → teaches `match` and `u8` arithmetic.
- Bracket matching with a `Vec` → teaches `Vec`, indexing, iterator patterns.
- Program-as-`&[u8]`, tape-as-`Vec<u8>` → teaches borrowing and slice lifetimes.
- No heap allocation in the hot loop → you'll feel the zero-cost-abstraction claim.

## The eight instructions

| Char | Effect |
|------|--------|
| `>`  | `ptr += 1` |
| `<`  | `ptr -= 1` |
| `+`  | `tape[ptr] = tape[ptr].wrapping_add(1)` |
| `-`  | `tape[ptr] = tape[ptr].wrapping_sub(1)` |
| `.`  | write `tape[ptr]` to stdout |
| `,`  | read one byte from stdin into `tape[ptr]` |
| `[`  | if `tape[ptr] == 0`, jump past matching `]` |
| `]`  | if `tape[ptr] != 0`, jump back to matching `[` |

## Run

```bash
cargo run --release -- examples/hello.bf
cargo test
```

## Level-up

- Precompute bracket-match table once, then the main loop is branch-free on `[` / `]`.
- Compile Brainfuck to x86-64 with Cranelift (then you've written a BF JIT).
