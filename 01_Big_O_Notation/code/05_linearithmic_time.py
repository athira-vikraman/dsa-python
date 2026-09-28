"""
O(n log n) — LINEARITHMIC TIME
==============================
"Do O(n) work, log n times."
This is the speed limit for comparison-based sorting: no algorithm that
sorts by comparing pairs can beat O(n log n) in the worst case.

Run me:  python3 code/05_linearithmic_time.py
"""

import random
import time


# ----------------------------------------------------------------------
# Example 1: merge sort - the clearest O(n log n) algorithm
# ----------------------------------------------------------------------
def merge_sort(items):
    """Divide in half, sort each half, merge.

    Time:  O(n log n) in ALL cases (best, average, worst)
           - log n levels of splitting
           - O(n) work merging at each level
    Space: O(n) - the merge buffers
    """
    if len(items) <= 1:                  # base case
        return list(items)

    mid = len(items) // 2
    left = merge_sort(items[:mid])       # T(n/2)
    right = merge_sort(items[mid:])      # T(n/2)
    return _merge(left, right)           # O(n)


def _merge(left, right):
    """Merge two sorted lists into one sorted list.

    Time: O(len(left) + len(right)) - each element moved once
    """
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:          # <= keeps the sort STABLE
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])              # leftovers
    merged.extend(right[j:])
    return merged


# ----------------------------------------------------------------------
# Example 2: quick sort
# ----------------------------------------------------------------------
def quick_sort(items):
    """Pick a pivot, partition, recurse.

    Best/Average: O(n log n) - pivot splits the data roughly in half
    Worst:        O(n^2)     - pivot is always the min or max
                               (e.g. already-sorted data + first-element pivot)
    Space:        O(n) in this simple version (O(log n) if done in place)

    This version picks the MIDDLE element as pivot, which avoids the
    worst case on already-sorted input.
    """
    if len(items) <= 1:
        return list(items)

    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]    # O(n)
    equal   = [x for x in items if x == pivot]   # O(n)
    larger  = [x for x in items if x > pivot]    # O(n)
    return quick_sort(smaller) + equal + quick_sort(larger)


# ----------------------------------------------------------------------
# Example 3: the "sort first, then scan" pattern
# ----------------------------------------------------------------------
def has_duplicate_by_sorting(items):
    """Sorting puts equal values next to each other.

    Time:  O(n log n) sort + O(n) scan = O(n log n)
    Space: O(n) for the sorted copy

    A set gives O(n) time, so this is not the best tool for THIS job -
    but the pattern is everywhere: sort, then solve in one pass.
    """
    ordered = sorted(items)                       # O(n log n)
    for i in range(len(ordered) - 1):             # O(n)
        if ordered[i] == ordered[i + 1]:
            return True
    return False


def closest_pair_difference(items):
    """Smallest gap between any two numbers.

    Brute force over all pairs: O(n^2).
    Sort first, then only ADJACENT pairs can be closest: O(n log n).
    """
    if len(items) < 2:
        return None
    ordered = sorted(items)                       # O(n log n)
    smallest = float("inf")
    for i in range(len(ordered) - 1):             # O(n)
        smallest = min(smallest, ordered[i + 1] - ordered[i])
    return smallest


# ----------------------------------------------------------------------
# Example 4: Python's own sort (Timsort)
# ----------------------------------------------------------------------
def python_sort_notes(items):
    """
    sorted(items)  -> O(n log n) time, O(n) space, returns a NEW list
    items.sort()   -> O(n log n) time, O(1) extra*, sorts IN PLACE

    Python uses Timsort: merge sort + insertion sort, with a trick -
    it detects already-sorted runs, so nearly-sorted data approaches O(n).
    """
    return sorted(items)


def _demo():
    print("=" * 62)
    print("O(n log n) LINEARITHMIC - a bit more than double per doubling")
    print("=" * 62)

    print("\n  Theory: how many operations for each n?")
    print(f"    {'n':>10} {'n':>14} {'n log2 n':>14} {'n^2':>18}")
    import math
    for n in (10, 100, 1_000, 1_000_000):
        print(f"    {n:>10,} {n:>14,} {int(n * math.log2(n)):>14,} {n * n:>18,}")

    print("\n  merge_sort timing (watch the ratio: a little over 2x):")
    previous = None
    for n in (10_000, 20_000, 40_000, 80_000):
        data = [random.randint(0, 1_000_000) for _ in range(n)]
        start = time.perf_counter()
        merge_sort(data)
        elapsed = time.perf_counter() - start
        ratio = f"{elapsed / previous:.2f}x" if previous else "  -  "
        print(f"    n = {n:>7,}   time = {elapsed:.4f}s   vs previous: {ratio}")
        previous = elapsed

    print("\n    O(n)      would show ratio 2.00")
    print("    O(n log n) shows slightly MORE than 2.00  <- what we see")
    print("    O(n^2)     would show ratio 4.00")

    print("\n  Our merge sort vs Python's built-in sorted() (n = 200,000):")
    data = [random.randint(0, 1_000_000) for _ in range(200_000)]
    start = time.perf_counter()
    mine = merge_sort(data)
    mine_time = time.perf_counter() - start
    start = time.perf_counter()
    builtin = sorted(data)
    builtin_time = time.perf_counter() - start
    print(f"    merge_sort (Python) : {mine_time:.4f}s")
    print(f"    sorted()   (C)      : {builtin_time:.4f}s")
    print(f"    same result?        : {mine == builtin}")
    print(f"    -> {mine_time / builtin_time:.0f}x faster in seconds, but the SAME O(n log n).")
    print("       Big O hides constant factors - and here the constant is C vs Python.")

    print("\n  Sanity checks:")
    sample = [5, 3, 8, 1, 9, 2]
    print(f"    merge_sort({sample}) = {merge_sort(sample)}")
    print(f"    quick_sort({sample}) = {quick_sort(sample)}")
    print(f"    has_duplicate_by_sorting([1,2,3,2]) = {has_duplicate_by_sorting([1,2,3,2])}")
    print(f"    closest_pair_difference([10,3,7,1])  = {closest_pair_difference([10,3,7,1])}")
    print("=" * 62)


if __name__ == "__main__":
    _demo()
