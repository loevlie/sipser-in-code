"""AST for the untyped λ-calculus: Var, Abs, App."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from beartype import beartype


@beartype
@dataclass(frozen=True)
class Var:
    name: str


@beartype
@dataclass(frozen=True)
class Abs:
    param: str
    body: "Term"


@beartype
@dataclass(frozen=True)
class App:
    func: "Term"
    arg: "Term"


Term = Union[Var, Abs, App]


@beartype
def free_vars(t: Term) -> set[str]:
    raise NotImplementedError


@beartype
def pretty(t: Term) -> str:
    raise NotImplementedError
