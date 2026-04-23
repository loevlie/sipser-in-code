# Contributing

This repo is a learning resource. Two kinds of contributions are welcome:

## 1. New project skeletons

If there's a concept in Sipser we don't cover and you think it deserves its own folder (think: pumping-lemma game, Rice's theorem illustrator, Savitch's theorem as code, a CDCL upgrade of the DPLL solver), open an issue first so we can talk about scope before you write code.

A good new project has:

- A short README with a **Theory reference** section citing the Sipser chapter and theorem.
- A typed function skeleton — public functions annotated and decorated with `@beartype` (Python) or proper `Result`/types (Rust).
- At least one example input and one test that fails until the skeleton is filled in.
- Links from its README to sibling projects it depends on.

## 2. Filled-in implementations

Each project is left intentionally as a skeleton so learners build it themselves. Please **don't submit PRs that fill in the `NotImplementedError` bodies for learners** — that defeats the purpose. If you want to share your solution, fork the repo and link it from a discussion thread.

What *is* welcome as a PR:

- Clearer explanatory comments in READMEs.
- Additional example inputs (more automata in the recognizer zoo, more TM specs, more test grammars).
- Improved test scaffolding (more `xfail` tests that specify the expected behavior without giving away the implementation).
- Fixes for typos, broken imports, wrong Sipser references.
- Translating a project to a new language (e.g., a Rust port of the regex engine) in a new folder — don't overwrite the existing one.

## Style

- Python: annotate public function parameters and returns; decorate with `@beartype`. Use `from __future__ import annotations`. Keep modules small and single-purpose.
- Rust: follow `rustfmt` defaults; prefer `Result<T, String>` for user-facing errors in these toy projects.
- Every project has its own `requirements.txt` or `Cargo.toml` and its own `README.md`. Don't pull shared state into a root package.

## Opening a PR

1. Fork, branch off `main`.
2. Small, focused commits; short commit messages.
3. Reference the Sipser section in your PR description if the change is theory-related.
