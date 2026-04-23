"""Interactive tinylang REPL."""

from __future__ import annotations

from beartype import beartype

from interpreter import Env, run
from lexer import tokenize
from parser import parse


@beartype
def main() -> None:
    env: Env = {}
    while True:
        try:
            line = input("tiny> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line.strip():
            continue
        try:
            env = run(parse(tokenize(line)), env)
        except Exception as exc:  # noqa: BLE001
            print(f"error: {exc}")


if __name__ == "__main__":
    main()
