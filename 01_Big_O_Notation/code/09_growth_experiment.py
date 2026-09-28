"""
THE GROWTH EXPERIMENT — seeing Big O with your own eyes
=======================================================
Theory says O(n) doubles, O(n^2) quadruples, O(log n) barely moves.
This file MEASURES real functions and prints the curves as ASCII charts,
so you can watch the theory happen.

Run me:  python3 code/09_growth_experiment.py
"""

import math
import random
import time


# ----------------------------------------------------------------------
# One function per complexity class
# ----------------------------------------------------------------------
def constant(items):
    """O(1)"""
    return items[0] if items else None


def logarithmic(items):
    """O(log n) - binary search for a value that is present."""
    target = items[-1]
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def linear(items):
    """O(n)"""
    biggest = items[0]
    for value in items:
        if value > biggest:
            biggest = value
    return biggest


def linearithmic(items):
    """O(n log n)"""
    return sorted(items)


def quadratic(items):
    """O(n^2) - compare every pair (capped so the demo finishes)."""
    count = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                count += 1
    return count


# ----------------------------------------------------------------------
# Measurement helpers
# ----------------------------------------------------------------------
def measure(func, items, repeats=1):
    """Return the best of `repeats` runs, in seconds.

    Best-of is more stable than average: it filters out interference
    from other processes on your machine.
    """
    best = float("inf")
    for _ in range(repeats):
        start = time.perf_counter()
        func(items)
        best = min(best, time.perf_counter() - start)
    return best


def ascii_bar(value, largest, width=40):
    """Draw a proportional bar."""
    if largest <= 0:
        return ""
    filled = max(1, int(round(width * value / largest)))
    return "#" * filled


def growth_report(name, func, sizes, repeats=1, sorted_input=False):
    """Time `func` at each size and print the doubling ratios."""
    print(f"\n  {name}")
    print(f"    {'n':>9} {'time (s)':>12} {'ratio':>8}   chart")
    results = []
    previous = None
    for n in sizes:
        items = list(range(n)) if sorted_input else [random.randint(0, n) for _ in range(n)]
        elapsed = measure(func, items, repeats)
        ratio = elapsed / previous if previous else None
        results.append((n, elapsed, ratio))
        previous = elapsed

    largest = max(r[1] for r in results)
    for n, elapsed, ratio in results:
        ratio_text = f"{ratio:.2f}x" if ratio else "  -  "
        print(f"    {n:>9,} {elapsed:>12.6f} {ratio_text:>8}   {ascii_bar(elapsed, largest)}")
    return results


def _demo():
    print("=" * 72)
    print("GROWTH EXPERIMENT - what each complexity class looks like when timed")
    print("=" * 72)
    print("\n  Read the 'ratio' column. Each row DOUBLES n, so:")
    print("     ~1.00x  ->  O(1)         (no growth)")
    print("     ~1.05x  ->  O(log n)     (one extra step)")
    print("     ~2.00x  ->  O(n)         (doubles)")
    print("     ~2.10x  ->  O(n log n)   (a little more than doubles)")
    print("     ~4.00x  ->  O(n^2)       (quadruples)")

    growth_report("O(1)  constant  - first_element",
                  constant, [100_000, 200_000, 400_000, 800_000], repeats=5)

    growth_report("O(log n)  logarithmic - binary search",
                  logarithmic, [100_000, 200_000, 400_000, 800_000],
                  repeats=5, sorted_input=True)

    growth_report("O(n)  linear - find max",
                  linear, [200_000, 400_000, 800_000, 1_600_000], repeats=3)

    growth_report("O(n log n)  linearithmic - sorted()",
                  linearithmic, [200_000, 400_000, 800_000, 1_600_000], repeats=3)

    growth_report("O(n^2)  quadratic - compare every pair",
                  quadratic, [500, 1_000, 2_000, 4_000], repeats=1)

    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("PREDICTION: how long would n = 1,000,000 take?")
    print("=" * 72)
    n = 4_000
    items = [random.randint(0, n) for _ in range(n)]
    measured = measure(quadratic, items)
    target_n = 1_000_000
    predicted = measured * (target_n / n) ** 2
    print(f"\n  Measured O(n^2) at n = {n:,}: {measured:.4f}s")
    print(f"  Since work scales with n^2, going to n = {target_n:,} multiplies it by")
    print(f"  ({target_n:,}/{n:,})^2 = {(target_n / n) ** 2:,.0f}")
    if predicted >= 86_400:
        human = f"{predicted / 86400:,.1f} DAYS"
    elif predicted >= 3_600:
        human = f"{predicted / 3600:,.1f} HOURS"
    else:
        human = f"{predicted / 60:,.1f} minutes"
    print(f"  Predicted time: {predicted:,.0f} seconds = {human}")
    print("\n  You just predicted a runtime you will never have to sit through.")
    print("  THAT is what Big O is for.")

    print("\n" + "=" * 72)
    print("THE SAME PROBLEM, TWO COMPLEXITIES")
    print("=" * 72)
    print("\n  Counting duplicate pairs: O(n^2) nested loops vs O(n) with a dict")

    def quadratic_count(items):
        count = 0
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] == items[j]:
                    count += 1
        return count

    def linear_count(items):
        seen = {}
        count = 0
        for value in items:
            count += seen.get(value, 0)
            seen[value] = seen.get(value, 0) + 1
        return count

    print(f"\n    {'n':>8} {'O(n^2)':>12} {'O(n)':>12} {'speed-up':>12}")
    for n in (1_000, 2_000, 4_000, 8_000):
        items = [random.randint(0, n // 2) for _ in range(n)]
        slow = measure(quadratic_count, items)
        fast = measure(linear_count, items, repeats=3)
        assert quadratic_count(items) == linear_count(items), "results must match!"
        print(f"    {n:>8,} {slow:>11.4f}s {fast:>11.6f}s {slow / fast:>11,.0f}x")

    print("\n  Same answer every time - the assert proves it. Only the speed differs,")
    print("  and the gap WIDENS as n grows. That widening gap is Big O.")
    print("=" * 72)


if __name__ == "__main__":
    random.seed(42)          # reproducible numbers
    _demo()
