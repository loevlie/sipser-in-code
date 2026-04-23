# 02 — Language Recognizer Zoo

**Theory reference:** Sipser Chapter 1.1. Practice encoding concrete regular languages as DFAs.

## What you're building

Ten hand-built DFAs for interesting regular languages, plus a runner that exercises each against positive and negative examples. Reuses the simulator from `01_dfa_nfa/`.

## Languages

| File | Language |
|------|----------|
| `divisible_by_3.json` | binary strings whose value mod 3 == 0 |
| `even_ones.json` | binary strings with an even number of 1s |
| `ends_with_ab.json` | strings over {a,b} ending in `ab` |
| `no_consecutive_ones.json` | binary strings with no `11` substring |
| `odd_length.json` | strings of odd length |
| `contains_abc.json` | strings over {a,b,c} containing `abc` |
| `decimal_multiples_of_5.json` | decimal strings divisible by 5 |
| `starts_and_ends_same.json` | non-empty strings where first == last char |
| `mod3_ones.json` | binary strings with `#1` ≡ 0 (mod 3) |
| `balanced_ab.json` | strings over {a,b} with `#a` ≡ `#b` (mod 2) |

## Run

```bash
python demo.py
```

Each recognizer is tested against a YES set and a NO set.
