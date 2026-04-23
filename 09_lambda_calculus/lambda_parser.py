"""Parser for λ-calculus source:  λx.M  or  \\x.M  for abstraction;
application is left-associative juxtaposition."""

from __future__ import annotations

from beartype import beartype

from lambda_term import Term


@beartype
def parse(src: str) -> Term:
    raise NotImplementedError
