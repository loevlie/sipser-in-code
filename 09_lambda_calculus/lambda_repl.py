"""Interactive λ-calculus REPL with let-bindings expanded before reduction."""

from __future__ import annotations

from beartype import beartype

from lambda_parser import parse
from lambda_term import Term, pretty
from reduce import normalize, substitute


@beartype
def main() -> None:
    env: dict[str, Term] = {}
    while True:
        try:
            line = input("λ> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not line:
            continue
        if line.startswith("let "):
            # TODO: parse `let NAME = TERM`, store in env.
            raise NotImplementedError
        t = parse(line)
        for name, val in env.items():
            t = substitute(t, name, val)
        print(pretty(normalize(t)))


if __name__ == "__main__":
    main()
