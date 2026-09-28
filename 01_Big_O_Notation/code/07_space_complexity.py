"""
SPACE COMPLEXITY — how much EXTRA memory an algorithm needs
===========================================================
The input is already in memory. We count only what YOU allocate on top,
which includes the recursion call stack.

Run me:  python3 code/07_space_complexity.py
"""

import sys
import tracemalloc


# ----------------------------------------------------------------------
# O(1) SPACE - a fixed number of variables
# ----------------------------------------------------------------------
def total_o1_space(numbers):
    """Time: O(n)   Space: O(1) - one accumulator, whatever n is."""
    result = 0
    for value in numbers:
        result += value
    return result


def reverse_in_place(items):
    """Two pointers swapping toward the middle.

    Time: O(n)   Space: O(1)   <- mutates the caller's list, no copy
    """
    left, right = 0, len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items


# ----------------------------------------------------------------------
# O(n) SPACE - a structure that grows with the input
# ----------------------------------------------------------------------
def doubled_on_space(numbers):
    """Time: O(n)   Space: O(n) - the new list has n elements."""
    return [value * 2 for value in numbers]


def reverse_copy(items):
    """Time: O(n)   Space: O(n) - slicing builds a whole new list."""
    return items[::-1]


def count_frequencies(items):
    """Time: O(n)   Space: O(k) where k = number of DISTINCT values.

    Worst case (all distinct): O(n).
    Be precise about which variable you mean - it earns marks.
    """
    counts = {}
    for value in items:
        counts[value] = counts.get(value, 0) + 1
    return counts


# ----------------------------------------------------------------------
# RECURSION USES SPACE even when it allocates nothing
# ----------------------------------------------------------------------
def countdown_recursive(n):
    """Allocates no data structure. Still O(n) space!

    n nested calls are alive at once, each with its own stack frame.
    Time: O(n)   Space: O(n)
    """
    if n <= 0:
        return 0
    return 1 + countdown_recursive(n - 1)


def countdown_iterative(n):
    """Same result, no stack growth.

    Time: O(n)   Space: O(1)
    """
    count = 0
    while n > 0:
        count += 1
        n -= 1
    return count


def max_recursion_depth():
    """Python caps recursion depth (~1000) to protect the stack.

    This is space complexity you can actually crash into.
    """
    return sys.getrecursionlimit()


def deepest_safe_recursion():
    """Find how deep we can actually go before RecursionError."""
    depth = 0

    def go():
        nonlocal depth
        depth += 1
        go()

    try:
        go()
    except RecursionError:
        pass
    return depth


# ----------------------------------------------------------------------
# THE TIME <-> SPACE TRADE-OFF
# ----------------------------------------------------------------------
def has_duplicate_low_space(items):
    """Time: O(n^2)   Space: O(1)   - slow, but uses no extra memory."""
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


def has_duplicate_low_time(items):
    """Time: O(n)     Space: O(n)   - fast, but stores a set.

    Neither is 'correct'. On a 100 GB dataset the O(1)-space version may
    be the only one that runs. On a 1000-item list, use the fast one.
    Knowing WHY you chose is the actual skill.
    """
    seen = set()
    for value in items:
        if value in seen:
            return True
        seen.add(value)
    return False


def _measure_peak_memory(func, *args):
    """Measure peak extra memory allocated by func, in kilobytes."""
    tracemalloc.start()
    tracemalloc.reset_peak()
    func(*args)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024


def _demo():
    print("=" * 62)
    print("SPACE COMPLEXITY - measured, not guessed")
    print("=" * 62)

    print("\n  Peak EXTRA memory used (input excluded):")
    print(f"    {'n':>10} {'O(1) sum':>14} {'O(n) doubled':>16}")
    for n in (10_000, 100_000, 1_000_000):
        data = list(range(n))
        o1 = _measure_peak_memory(total_o1_space, data)
        on = _measure_peak_memory(doubled_on_space, data)
        print(f"    {n:>10,} {o1:>12.1f} KB {on:>14,.1f} KB")

    print("\n    O(1) column stays flat. O(n) column grows with n. That's the whole idea.")

    print("\n  In-place vs copy reversal:")
    data = list(range(500_000))
    in_place = _measure_peak_memory(reverse_in_place, data)
    copying = _measure_peak_memory(reverse_copy, data)
    print(f"    reverse_in_place : {in_place:>10.1f} KB   (O(1) space)")
    print(f"    reverse_copy     : {copying:>10,.1f} KB   (O(n) space)")

    print("\n  Recursion costs memory even with no data structure:")
    print(f"    Python recursion limit : {max_recursion_depth():,}")
    print(f"    Actual depth reached   : {deepest_safe_recursion():,} before RecursionError")
    print(f"    countdown_recursive(900) = {countdown_recursive(900)}   # O(n) space")
    print(f"    countdown_iterative(900) = {countdown_iterative(900)}   # O(1) space")
    print("    countdown_recursive(100000) would CRASH. The iterative one would not.")

    print("\n  The trade-off, side by side:")
    print("    has_duplicate_low_space : O(n^2) time, O(1) space")
    print("    has_duplicate_low_time  : O(n)   time, O(n) space")
    sample = [1, 2, 3, 4, 2]
    print(f"    both agree on {sample}: "
          f"{has_duplicate_low_space(sample)} / {has_duplicate_low_time(sample)}")

    print("\n  Say it like this in an interview:")
    print('    "O(n) time and O(1) auxiliary space, not counting the output."')
    print("=" * 62)


if __name__ == "__main__":
    _demo()
