# sipser-in-code

**Every machine in Sipser's *Introduction to the Theory of Computation*, built from scratch.**

Theory of computation is the one CS course where the math *is* the material — and paradoxically, the best way to make the math stick is to build the machines it describes. Every abstract object in Sipser corresponds to a small, buildable program. When you've built a DFA simulator, a regex-to-NFA compiler, a Turing machine, and a SAT solver, you'll never again forget what those things are.

This repo is twelve project skeletons, ordered roughly the way the course itself unfolds. Each folder has a README pinning it to a specific Sipser chapter, a typed function skeleton, example inputs, and tests that fail until you fill things in. Fork it, work through it, and by the end you'll have a portfolio that covers every topic in an undergraduate theory course.

## The curriculum

| #  | Project | Language | Sipser | ⭐ |
|----|---------|----------|--------|---|
| 01 | [DFA / NFA simulator](01_dfa_nfa/) | Python | 1.1–1.2 | ⭐ |
| 02 | [Language recognizer zoo](02_recognizer_zoo/) | Python | 1.1 | |
| 03 | [Regex engine (Thompson's construction)](03_regex_engine/) | Python | 1.3 | ⭐ |
| 04 | [DFA minimization (Hopcroft)](04_dfa_minimization/) | Python | — | |
| 05 | [CYK parser](05_cyk_parser/) | Python | 2.1 | ⭐ |
| 06 | [tinylang — a mini-compiler](06_tinylang/) | Python | 2.1–2.2 | ⭐ |
| 07 | [Turing machine simulator](07_turing_machine/) | Python | 3.1–3.2 | ⭐ |
| 08 | [Brainfuck interpreter](08_brainfuck_rs/) | **Rust** | 3.3 | |
| 09 | [Untyped λ-calculus](09_lambda_calculus/) | Python | 3.3 | |
| 10 | [DPLL SAT solver](10_dpll_sat/) | Python | 7.4 | ⭐ |
| 11 | [NP-reduction library](11_np_reductions/) | Python | 7.4–7.5 | |
| 12 | [Chomsky Hierarchy Explorer (capstone)](12_hierarchy_explorer/) | Python + React | — | ⭐ |

The ⭐ projects are the highest theory-per-hour return. If you only do those, you'll still hit every major concept.

## What you'll have built by the end

- A regex engine that beats Python's built-in `re` module on pathological inputs (Russ Cox's benchmark).
- A working compiler for a small imperative language (lexer → parser → tree-walking interpreter).
- A Turing machine that decides `{aⁿbⁿcⁿ}` with a trace of every step.
- A SAT solver that cracks a Sudoku in milliseconds.
- A web app that lets you type a regex, a grammar, or a TM spec and watch the matching machine run — the Chomsky hierarchy in one UI.

## How to use this repo

**Clone and work through it in order.** Each project builds on the previous ones — project 02 reuses project 01's simulator, project 04 reuses project 01's DFA type, project 11 reuses project 10's SAT solver, and the capstone glues 01, 03, 05, and 07 together. If you skip around, you'll have to patch imports.

**Every `NotImplementedError` is your job.** The skeletons give you the shape (function signatures, data types, grammar) and leave the bodies for you. The READMEs include enough theory to fill them in without extra references, but having Sipser open beside you is the best experience.

**Tests start as `xfail`.** Flip them to passing as you implement. When everything is green, the project is done.

## Conventions

- **Python** — every public function is annotated and decorated with `@beartype` for runtime type checking. You get the safety of a typed language without the ceremony.
- **Rust** — only the Brainfuck interpreter. It's a perfect "learn Rust" project: tight dispatch loop, byte tape, lots of `match`.
- **One project per folder, one folder per project.** Each has its own `README.md`, `requirements.txt` / `Cargo.toml`, and `.gitignore`.

## Setup

Python projects:

```bash
cd 01_dfa_nfa
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

The Rust project:

```bash
cd 08_brainfuck_rs
cargo run --release -- examples/hello.bf
cargo test
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: new skeletons and clearer explanations welcome; PRs that fill in the `NotImplementedError` bodies for learners are not — that defeats the point.

## Reference

Michael Sipser, *Introduction to the Theory of Computation*, 3rd edition. Each project's README cites the specific chapter and theorem it implements.

## License

[MIT](LICENSE).
