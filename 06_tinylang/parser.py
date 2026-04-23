"""Recursive-descent parser for tinylang.

Grammar sketch:
    program := stmt*
    stmt    := let | print | if | while
    let     := 'let' IDENT '=' expr ';'
    print   := 'print' expr ';'
    if      := 'if' expr '{' stmt* '}' ('else' '{' stmt* '}')?
    while   := 'while' expr '{' stmt* '}'
    expr    := cmp
    cmp     := sum (('>' | '<' | '==') sum)?
    sum     := term (('+' | '-') term)*
    term    := atom (('*' | '/') atom)*
    atom    := INT | STR | IDENT | '(' expr ')'
"""

from __future__ import annotations

from beartype import beartype

from ast_nodes import Stmt
from lexer import Token


@beartype
def parse(tokens: list[Token]) -> list[Stmt]:
    raise NotImplementedError
