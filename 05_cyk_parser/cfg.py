"""Context-free grammar representation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from beartype import beartype


@beartype
@dataclass
class CFG:
    start: str
    # nonterminal -> list of productions; each production is a list of symbols
    rules: dict[str, list[list[str]]]

    @beartype
    def nonterminals(self) -> set[str]:
        return set(self.rules.keys())

    @beartype
    def is_terminal(self, symbol: str) -> bool:
        return symbol not in self.rules


@beartype
def load(path: str | Path) -> CFG:
    data = json.loads(Path(path).read_text())
    return CFG(start=data["start"], rules=data["rules"])
