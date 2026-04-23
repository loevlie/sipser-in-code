"""FastAPI entrypoint for the Chomsky Hierarchy Explorer.

Each router forwards to a simulator from an earlier project. Keep this file
thin; the heavy lifting lives in the project folders it wraps.
"""

from __future__ import annotations

import sys
from pathlib import Path

from beartype import beartype
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Put the sibling project modules on the path.
ROOT = Path(__file__).resolve().parent.parent.parent
for proj in ("01_dfa_nfa", "03_regex_engine", "05_cyk_parser", "07_turing_machine"):
    sys.path.insert(0, str(ROOT / proj))


app = FastAPI(title="Chomsky Hierarchy Explorer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class RegexReq(BaseModel):
    pattern: str
    input: str


class CFGReq(BaseModel):
    grammar: dict
    input: str


class TMStepReq(BaseModel):
    tm: dict
    tape: list[str]
    state: str
    head: int


@beartype
@app.post("/regex/match")
def regex_match(req: RegexReq) -> dict:
    # TODO: call into ../03_regex_engine/match.py:fullmatch
    raise NotImplementedError


@beartype
@app.post("/cfg/parse")
def cfg_parse(req: CFGReq) -> dict:
    # TODO: call into ../05_cyk_parser/cyk.py:recognize
    raise NotImplementedError


@beartype
@app.post("/tm/step")
def tm_step(req: TMStepReq) -> dict:
    # TODO: call into ../07_turing_machine/tm.py one step at a time
    raise NotImplementedError


@beartype
@app.get("/health")
def health() -> dict:
    return {"ok": True}
