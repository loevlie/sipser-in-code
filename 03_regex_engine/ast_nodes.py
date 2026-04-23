"""AST nodes for a minimal regex grammar: Char | Concat | Alt | Star."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from beartype import beartype


@beartype
@dataclass(frozen=True)
class Char:
    c: str  # single character; use "" for ε


@beartype
@dataclass(frozen=True)
class Concat:
    left: "Regex"
    right: "Regex"


@beartype
@dataclass(frozen=True)
class Alt:
    left: "Regex"
    right: "Regex"


@beartype
@dataclass(frozen=True)
class Star:
    inner: "Regex"


Regex = Union[Char, Concat, Alt, Star]
