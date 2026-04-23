"""β-reduction with α-renaming for the untyped λ-calculus.

Normal-order reduction (leftmost-outermost) to avoid unnecessary divergence
when a subterm has no normal form.
"""

from __future__ import annotations

from beartype import beartype

from lambda_term import Term


@beartype
def substitute(t: Term, x: str, s: Term) -> Term:
    """Capture-avoiding substitution: t[x := s]."""
    raise NotImplementedError


@beartype
def beta_step(t: Term) -> Term | None:
    """One normal-order β-reduction step, or None if t is in normal form."""
    raise NotImplementedError


@beartype
def normalize(t: Term, max_steps: int = 10_000) -> Term:
    """Iterate β-reduction until a normal form is reached or max_steps is hit."""
    raise NotImplementedError
