"""Tree-walking interpreter for tinylang."""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype

from ast_nodes import Expr, Stmt
from lexer import tokenize
from parser import parse

Value = int | str | bool
Env = dict[str, Value]


@beartype
def run(program: list[Stmt], env: Env | None = None) -> Env:
    env = {} if env is None else env
    raise NotImplementedError


@beartype
def eval_expr(e: Expr, env: Env) -> Value:
    raise NotImplementedError


if __name__ == "__main__":
    src = Path(sys.argv[1]).read_text()
    run(parse(tokenize(src)))
