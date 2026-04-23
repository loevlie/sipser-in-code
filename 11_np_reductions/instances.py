"""Shared instance types for the reductions."""

from __future__ import annotations

from dataclasses import dataclass

from beartype import beartype


@beartype
@dataclass
class Graph:
    """Undirected simple graph."""
    n: int
    edges: set[tuple[int, int]]


@beartype
@dataclass
class ColoringInstance:
    graph: Graph
    k: int  # number of colors


@beartype
@dataclass
class CliqueInstance:
    graph: Graph
    k: int  # target clique size


@beartype
@dataclass
class SubsetSumInstance:
    numbers: list[int]
    target: int
