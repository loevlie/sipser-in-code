# 12 — Chomsky Hierarchy Explorer (Capstone)

**Theory reference:** the whole book. Regular ⊊ Context-Free ⊊ Decidable ⊊ Recognizable. One app that demonstrates all four classes by wrapping the simulators you already wrote.

## The pitch

A single web UI with four tabs. The user enters a language description — regex, CFG, or TM — and the app:

1. Places it on the Chomsky hierarchy.
2. Visualizes the corresponding machine (DFA, PDA, TM).
3. Accepts or rejects input strings, step by step, with animation.

## Architecture

```
backend/     FastAPI. Thin wrappers around the simulators from earlier projects.
frontend/    React + Vite. One tab component per hierarchy level.
```

Backend endpoints (sketch):

- `POST /regex/compile` — body: `{pattern}` → NFA JSON
- `POST /regex/match`   — body: `{pattern, input}` → `{accept, trace}`
- `POST /cfg/parse`     — body: `{grammar, input}` → `{accept, chart}`
- `POST /tm/step`       — body: `{tm, tape, state, head}` → `{tape, state, head, halted}`

## Prerequisites

Finish projects 01, 03, 05, and 07 first. This project is glue.

## Run (dev)

```bash
# backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# frontend
cd frontend
npm install
npm run dev
```

## Level-up

- Deploy: backend on Render/Fly, frontend on Vercel.
- "Guess the language class" quiz mode.
- Integrate `10_dpll_sat/` and classify problems by attempting a SAT reduction.
