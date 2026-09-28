"""
O(n) — LINEAR TIME
==================
You touch each element a constant number of times.
Double the input -> roughly double the time.

Run me:  python3 code/02_linear_time.py
"""

import time


# ----------------------------------------------------------------------
# Example 1: the classic single loop
# ----------------------------------------------------------------------
def find_max(items):
    """Find the largest value.

    Time:  O(n) - every element inspected once
    Space: O(1) - one variable, regardless of n
    """
    if not items:
        return None
    biggest = items[0]
    for value in items:          # n iterations
        if value > biggest:      # O(1) each
            biggest = value
    return biggest


# ----------------------------------------------------------------------
# Example 2: linear search
# ----------------------------------------------------------------------
def linear_search(items, target):
    """Return the index of target, or -1.

    Best case:    O(1)  - target is the first element
    Worst case:   O(n)  - target is last, or absent  <- we report this
    Average case: O(n)  - about n/2 steps, and O(n/2) = O(n)
    Space:        O(1)
    """
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


# ----------------------------------------------------------------------
# Example 3: TWO loops in sequence is still O(n)
# ----------------------------------------------------------------------
def sum_and_product(items):
    """2n steps -> O(2n) -> O(n). Constants are dropped.

    Time: O(n)   Space: O(1)
    """
    total = 0
    for value in items:          # n
        total += value
    product = 1
    for value in items:          # n more  -> 2n total
        product *= value
    return total, product


# ----------------------------------------------------------------------
# Example 4: linear time, linear space
# ----------------------------------------------------------------------
def doubled(items):
    """Time: O(n)   Space: O(n) - the new list grows with the input."""
    result = []
    for value in items:
        result.append(value * 2)
    return result


# ----------------------------------------------------------------------
# Example 5: built-ins that are secretly O(n) loops
# ----------------------------------------------------------------------
def builtin_linear_operations(items, target):
    """Every line here is a hidden O(n) loop written in C.

    Faster in seconds than a Python loop, but the SAME complexity.
    """
    return {
        "sum":   sum(items),          # O(n)
        "max":   max(items),          # O(n)
        "min":   min(items),          # O(n)
        "count": items.count(target), # O(n)
        "has":   target in items,     # O(n)
    }


# ----------------------------------------------------------------------
# Example 6: a loop that runs a CONSTANT number of times is O(1)
# ----------------------------------------------------------------------
def first_three(items):
    """The loop is bounded by 3, not by n.

    Time: O(1) - independent of input size
    """
    result = []
    for i in range(min(3, len(items))):
        result.append(items[i])
    return result


def _demo():
    print("=" * 62)
    print("O(n) LINEAR TIME - watch the time double when n doubles")
    print("=" * 62)

    previous = None
    for n in (1_000_000, 2_000_000, 4_000_000, 8_000_000):
        data = list(range(n))
        start = time.perf_counter()
        find_max(data)
        elapsed = time.perf_counter() - start
        ratio = f"{elapsed / previous:.2f}x" if previous else "  -  "
        print(f"  n = {n:>10,}   time = {elapsed:.4f}s   vs previous: {ratio}")
        previous = elapsed

    print("\n  Each ratio is close to 2.00: doubling n doubles the work.")
    print("  That straight-line relationship IS O(n).\n")

    sample = [3, 7, 1, 9, 4]
    print(f"  find_max({sample})            = {find_max(sample)}")
    print(f"  linear_search({sample}, 9)    = {linear_search(sample, 9)}")
    print(f"  linear_search({sample}, 100)  = {linear_search(sample, 100)}  (absent -> worst case)")
    print(f"  sum_and_product({sample})     = {sum_and_product(sample)}")
    print(f"  doubled({sample})             = {doubled(sample)}")
    print(f"  first_three({sample})         = {first_three(sample)}  <- O(1), loop bounded by 3")
    print("=" * 62)


if __name__ == "__main__":
    _demo()
