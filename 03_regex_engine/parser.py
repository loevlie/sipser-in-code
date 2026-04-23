"""Regex string → AST.

Grammar (recursive descent):
    regex   := term ('|' term)*
    term    := factor factor*
    factor  := atom '*'?
    atom    := CHAR | '(' regex ')'
"""

from __future__ import annotations

from beartype import beartype

from ast_nodes import Regex


@beartype
def parse(pattern: str) -> Regex:
    raise NotImplementedError
