"""Lex tinylang source into tokens.

Illustrates that token classes (identifiers, numbers, string literals,
operators) are exactly the regular languages. A production lexer is one big
DFA; this starter uses longest-match with small regex classes per kind.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

from beartype import beartype


class Tok(Enum):
    INT = auto()
    STR = auto()
    IDENT = auto()
    KEYWORD = auto()
    OP = auto()
    PUNCT = auto()
    EOF = auto()


@beartype
@dataclass
class Token:
    kind: Tok
    lexeme: str
    line: int
    col: int


@beartype
def tokenize(src: str) -> list[Token]:
    raise NotImplementedError
