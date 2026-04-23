# 07 — Turing Machine Simulator

**Theory reference:** Sipser 3.1 (formal definition) and 3.2 (variants; multi-tape / nondeterministic are equivalent to single-tape).

## What you're building

A single-tape deterministic TM simulator. Reads a transition-table file plus an input string. Produces accept / reject / timeout, the final tape, and optionally a trace of every step.

## File format

```
# Tape alphabet uses `_` for blank.
states: q0, q1, q_accept, q_reject
input_alphabet: 0, 1
tape_alphabet: 0, 1, _
start: q0
accept: q_accept
reject: q_reject

# current_state, read -> next_state, write, L|R
q0, 0 -> q0, 0, R
q0, 1 -> q1, 1, R
q0, _ -> q_accept, _, R
```

## Classic machines to encode

- Unary increment (`011` → `0111`)
- Palindrome recognizer over {a,b}
- {aⁿbⁿcⁿ : n ≥ 0} — non-context-free but TM-decidable
- Binary successor
- Replicator: `w#` → `w#w`

## Run

```bash
python tm.py examples/palindrome.tm aabbaa --trace
```

## Level-up

- Universal TM: feed another TM's description plus an input on the tape.
- Multi-tape simulator with a reducer to single-tape (Sipser Theorem 3.13 in code).
- Terminal animation of the head moving across the tape.
