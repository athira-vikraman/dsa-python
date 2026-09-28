"""
O(2^n) — EXPONENTIAL TIME  (and how to escape it)
=================================================
Each extra input element DOUBLES the work.
n = 50 is already impossible. n = 100 outlives the universe.

The good news: most exponential code you meet is exponential by ACCIDENT,
and memoization fixes it. This file shows the fix three ways.

Run me:  python3 code/06_exponential_time.py
"""

import time
from functools import lru_cache


# ----------------------------------------------------------------------
# Example 1: naive Fibonacci - O(2^n), the famous disaster
# ----------------------------------------------------------------------
def fib_slow(n):
    """Time:  O(2^n) - two recursive calls per call
    Space: O(n)   - deepest call-stack path

    The problem: it recomputes the same values over and over.
        fib(5) -> fib(4) + fib(3)
        fib(4) -> fib(3) + fib(2)     <- fib(3) computed AGAIN
    """
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)


CALL_COUNT = {"n": 0}


def fib_counted(n):
    """Same as fib_slow, but counts calls so you can SEE the explosion."""
    CALL_COUNT["n"] += 1
    if n <= 1:
        return n
    return fib_counted(n - 1) + fib_counted(n - 2)


# ----------------------------------------------------------------------
# Example 2: FIX #1 - memoization by hand -> O(n)
# ----------------------------------------------------------------------
def fib_memo(n, memo=None):
    """Cache each result so every fib(k) is computed exactly ONCE.

    Time:  O(n)   <- from O(2^n). The single biggest win in this course.
    Space: O(n)   - the memo dict plus the call stack
    """
    if memo is None:
        memo = {}
    if n in memo:                     # O(1) lookup
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ----------------------------------------------------------------------
# Example 3: FIX #2 - the same idea with one decorator
# ----------------------------------------------------------------------
@lru_cache(maxsize=None)
def fib_cached(n):
    """functools.lru_cache does the memoization for you.

    Time: O(n)   Space: O(n)
    """
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


# ----------------------------------------------------------------------
# Example 4: FIX #3 - iterative, the true champion
# ----------------------------------------------------------------------
def fib_iterative(n):
    """No recursion, no cache, just two variables.

    Time:  O(n)
    Space: O(1)   <- beats memoization on memory
    """
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


# ----------------------------------------------------------------------
# Example 5: genuinely exponential - all subsets
# ----------------------------------------------------------------------
def all_subsets(items):
    """A set of n elements has exactly 2^n subsets.

    Time:  O(2^n)   Space: O(2^n)

    This one is NOT a mistake: the OUTPUT itself has 2^n entries, so no
    algorithm can be faster. When the output is exponential, the
    algorithm must be too - the fix is to change the QUESTION
    (e.g. "the best subset" instead of "all subsets" -> dynamic programming).
    """
    subsets = [[]]
    for item in items:
        subsets += [subset + [item] for subset in subsets]   # doubles each time
    return subsets


# ----------------------------------------------------------------------
# Example 6: O(n!) - all permutations
# ----------------------------------------------------------------------
def all_permutations(items):
    """Time: O(n!) - n=10 is 3.6 million, n=20 is 2.4 x 10^18."""
    if len(items) <= 1:
        return [list(items)]
    result = []
    for i, item in enumerate(items):
        rest = items[:i] + items[i + 1:]
        for perm in all_permutations(rest):
            result.append([item] + perm)
    return result


def _demo():
    print("=" * 62)
    print("O(2^n) EXPONENTIAL - and the memoization escape hatch")
    print("=" * 62)

    print("\n  How many function calls does naive fib(n) make?")
    for n in (5, 10, 15, 20, 25, 30):
        CALL_COUNT["n"] = 0
        fib_counted(n)
        print(f"    fib({n:>2}) -> {CALL_COUNT['n']:>10,} calls")
    print("    ...each +5 multiplies the calls by about 11. This is the explosion.")

    print("\n  Timing: naive vs memoized vs iterative")
    print(f"    {'n':>4} {'O(2^n) naive':>16} {'O(n) memo':>14} {'O(n) iterative':>16}")
    for n in (20, 25, 30, 32):
        start = time.perf_counter()
        fib_slow(n)
        slow = time.perf_counter() - start

        start = time.perf_counter()
        fib_memo(n)
        memo = time.perf_counter() - start

        start = time.perf_counter()
        fib_iterative(n)
        fast = time.perf_counter() - start

        print(f"    {n:>4} {slow:>15.4f}s {memo:>13.6f}s {fast:>15.6f}s")

    print("\n  fib(100):")
    print("    naive      : would take longer than the age of the universe")
    start = time.perf_counter()
    value = fib_iterative(100)
    elapsed = time.perf_counter() - start
    print(f"    iterative  : {value:,} in {elapsed:.8f}s")

    print("\n  Genuinely exponential problems:")
    print(f"    all_subsets([1,2,3])       = {all_subsets([1, 2, 3])}")
    print(f"    len(all_subsets(range(10))) = {len(all_subsets(list(range(10))))}  (= 2^10)")
    print(f"    all_permutations([1,2,3])   = {all_permutations([1, 2, 3])}")
    print(f"    len(all_permutations(range(6))) = {len(all_permutations(list(range(6))))}  (= 6!)")

    print("\n  RULE: two recursive calls + input shrinking by 1 => think MEMOIZE.")
    print("=" * 62)


if __name__ == "__main__":
    _demo()
