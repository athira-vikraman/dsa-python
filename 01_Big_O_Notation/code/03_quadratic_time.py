"""
O(n^2) — QUADRATIC TIME
=======================
A loop inside a loop over the same data.
Double the input -> FOUR times the work.

This file also shows how to FIX quadratic code, which is the single most
valuable optimisation skill in interviews.

Run me:  python3 code/03_quadratic_time.py
"""

import time


# ----------------------------------------------------------------------
# Example 1: every pair (the classic nested loop)
# ----------------------------------------------------------------------
def all_pairs(items):
    """Build every pair of elements.

    Time:  O(n^2) - n iterations x n iterations
    Space: O(n^2) - the result holds n^2 pairs
    """
    pairs = []
    for a in items:              # n times
        for b in items:          #   n times each -> n * n
            pairs.append((a, b))
    return pairs


# ----------------------------------------------------------------------
# Example 2: the triangular loop - HALF of n^2 is still O(n^2)
# ----------------------------------------------------------------------
def unique_pairs(items):
    """Each unordered pair once: (n-1) + (n-2) + ... + 1 = n(n-1)/2 steps.

    Time:  O(n^2)  <- n^2/2 - n/2, drop constants and lower terms
    Space: O(n^2)
    """
    pairs = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):    # shrinking inner loop
            pairs.append((items[i], items[j]))
    return pairs


# ----------------------------------------------------------------------
# Example 3: THE optimisation - O(n^2) -> O(n) with a set
# ----------------------------------------------------------------------
def has_duplicate_slow(items):
    """Compare every pair.

    Time:  O(n^2)   Space: O(1)
    """
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


def has_duplicate_fast(items):
    """One pass, O(1) set lookups.

    Time:  O(n)   Space: O(n)   <- we traded memory for speed
    """
    seen = set()
    for value in items:
        if value in seen:        # O(1), not O(n)
            return True
        seen.add(value)          # O(1)
    return False


# ----------------------------------------------------------------------
# Example 4: hidden quadratic - the trap you WILL write by accident
# ----------------------------------------------------------------------
def remove_duplicates_slow(items):
    """Looks like one loop. `not in result` is itself O(n).

    Time: O(n^2)   Space: O(n)
    """
    result = []
    for value in items:
        if value not in result:  # <-- HIDDEN O(n) SCAN
            result.append(value)
    return result


def remove_duplicates_fast(items):
    """Same output, order preserved, O(1) membership test.

    Time: O(n)   Space: O(n)
    """
    seen = set()
    result = []
    for value in items:
        if value not in seen:    # O(1)
            seen.add(value)
            result.append(value)
    return result


# ----------------------------------------------------------------------
# Example 5: bubble sort - a textbook O(n^2) algorithm
# ----------------------------------------------------------------------
def bubble_sort(items):
    """Repeatedly swap adjacent out-of-order elements.

    Best:  O(n)   - already sorted (thanks to the early exit)
    Worst: O(n^2) - reverse sorted
    Space: O(1)   - sorts in place
    """
    data = list(items)                     # copy so we don't mutate the input
    n = len(data)
    for i in range(n):                     # n passes
        swapped = False
        for j in range(0, n - i - 1):      # shrinking inner loop
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:                    # early exit -> O(n) best case
            break
    return data


# ----------------------------------------------------------------------
# Example 6: nested loops over DIFFERENT inputs are O(a*b), NOT O(n^2)
# ----------------------------------------------------------------------
def common_items_slow(list_a, list_b):
    """Time: O(a * b)   Space: O(1) extra (plus the result)"""
    result = []
    for x in list_a:             # a times
        if x in list_b:          #   O(b) scan each
            result.append(x)
    return result


def common_items_fast(list_a, list_b):
    """Time: O(a + b)   Space: O(b)"""
    set_b = set(list_b)          # O(b) once
    return [x for x in list_a if x in set_b]   # O(a) x O(1)


def _demo():
    print("=" * 62)
    print("O(n^2) QUADRATIC - watch the time QUADRUPLE when n doubles")
    print("=" * 62)

    previous = None
    for n in (1000, 2000, 4000, 8000):
        data = list(range(n))            # no duplicates -> worst case
        start = time.perf_counter()
        has_duplicate_slow(data)
        elapsed = time.perf_counter() - start
        ratio = f"{elapsed / previous:.2f}x" if previous else "  -  "
        print(f"  n = {n:>6,}   O(n^2) time = {elapsed:.4f}s   vs previous: {ratio}")
        previous = elapsed

    print("\n  Each ratio is about 4.00. Doubling n QUADRUPLES the work.\n")

    print("  Now the same job with a set - O(n):")
    previous = None
    for n in (1000, 2000, 4000, 8000):
        data = list(range(n))
        start = time.perf_counter()
        has_duplicate_fast(data)
        elapsed = time.perf_counter() - start
        ratio = f"{elapsed / previous:.2f}x" if previous else "  -  "
        print(f"  n = {n:>6,}   O(n)   time = {elapsed:.6f}s   vs previous: {ratio}")
        previous = elapsed

    print("\n  Head-to-head at n = 10,000:")
    data = list(range(10_000))
    start = time.perf_counter()
    has_duplicate_slow(data)
    slow = time.perf_counter() - start
    start = time.perf_counter()
    has_duplicate_fast(data)
    fast = time.perf_counter() - start
    print(f"    O(n^2): {slow:.4f}s")
    print(f"    O(n)  : {fast:.6f}s")
    print(f"    speed-up: {slow / fast:,.0f}x faster")

    print("\n  Sanity checks:")
    sample = [5, 2, 9, 2, 7]
    print(f"    unique_pairs([1,2,3])              = {unique_pairs([1, 2, 3])}")
    print(f"    remove_duplicates_fast({sample})  = {remove_duplicates_fast(sample)}")
    print(f"    bubble_sort({sample})             = {bubble_sort(sample)}")
    print(f"    common_items_fast([1,2,3],[2,3,4]) = {common_items_fast([1,2,3],[2,3,4])}")
    print("=" * 62)


if __name__ == "__main__":
    _demo()
