"""The pathological input that blows up Python's `re` module.

Pattern: a?^n a^n   matched against   a^n
Python's backtracking engine explores O(2^n) paths. An NFA simulation tracks a
set of at most O(n) states, so it runs in linear time.
"""

from __future__ import annotations

import re
import time

from beartype import beartype

from match import fullmatch


@beartype
def bench(n: int) -> None:
    pattern_re = "a?" * n + "a" * n
    pattern_ours = pattern_re  # same syntax for the subset we support
    s = "a" * n

    t0 = time.perf_counter()
    ours = fullmatch(pattern_ours, s)
    t_ours = time.perf_counter() - t0

    t0 = time.perf_counter()
    theirs = bool(re.fullmatch(pattern_re, s))
    t_theirs = time.perf_counter() - t0

    print(f"n={n:>3}  ours={t_ours*1000:8.3f}ms  re={t_theirs*1000:10.3f}ms  "
          f"(agree={ours == theirs})")


if __name__ == "__main__":
    for n in [5, 10, 15, 20, 25]:
        bench(n)
