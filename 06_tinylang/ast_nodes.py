"""AST node dataclasses for tinylang."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from beartype import beartype


@beartype
@dataclass(frozen=True)
class IntLit:
    value: int


@beartype
@dataclass(frozen=True)
class StrLit:
    value: str


@beartype
@dataclass(frozen=True)
class Var:
    name: str


@beartype
@dataclass(frozen=True)
class BinOp:
    op: str  # "+" "-" "*" "/" ">" "<" "==" ...
    left: "Expr"
    right: "Expr"


Expr = Union[IntLit, StrLit, Var, BinOp]


@beartype
@dataclass(frozen=True)
class Let:
    name: str
    value: Expr


@beartype
@dataclass(frozen=True)
class Print:
    value: Expr


@beartype
@dataclass(frozen=True)
class If:
    cond: Expr
    then_block: list["Stmt"]
    else_block: list["Stmt"]


@beartype
@dataclass(frozen=True)
class While:
    cond: Expr
    body: list["Stmt"]


Stmt = Union[Let, Print, If, While]
