"""
O(log n) — LOGARITHMIC TIME
===========================
Each step throws away HALF the remaining work.
Double the input -> only ONE extra step.

n = 1,000,000 needs about 20 steps. That is the magic.

Run me:  python3 code/04_logarithmic_time.py
"""

import time


# ----------------------------------------------------------------------
# Example 1: binary search, iterative (the algorithm to know by heart)
# ----------------------------------------------------------------------
def binary_search(sorted_items, target):
    """Find target in a SORTED list. Returns the index, or -1.

    Time:  O(log n) - the search range halves every iteration
    Space: O(1)     - only three variables

    PRECONDITION: the list must already be sorted. If it isn't, sorting
    first costs O(n log n), and for a single lookup a plain O(n) scan
    would have been cheaper. Binary search pays off when you search
    the same sorted data many times.
    """
    low = 0
    high = len(sorted_items) - 1

    while low <= high:
        mid = (low + high) // 2          # middle index
        guess = sorted_items[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1                # discard the left half
        else:
            high = mid - 1               # discard the right half

    return -1


# ----------------------------------------------------------------------
# Example 2: the same thing recursively
# ----------------------------------------------------------------------
def binary_search_recursive(sorted_items, target, low=0, high=None):
    """Time: O(log n)   Space: O(log n) - one stack frame per level."""
    if high is None:
        high = len(sorted_items) - 1

    if low > high:                       # base case: not found
        return -1

    mid = (low + high) // 2
    if sorted_items[mid] == target:
        return mid
    if sorted_items[mid] < target:
        return binary_search_recursive(sorted_items, target, mid + 1, high)
    return binary_search_recursive(sorted_items, target, low, mid - 1)


# ----------------------------------------------------------------------
# Example 3: a halving loop - the shape to recognise
# ----------------------------------------------------------------------
def count_halvings(n):
    """How many times can n be halved before it reaches 1?

    That count IS log2(n).
    Time: O(log n)   Space: O(1)
    """
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    return steps


# ----------------------------------------------------------------------
# Example 4: a doubling loop - also O(log n)
# ----------------------------------------------------------------------
def doubling_loop(n):
    """i: 1, 2, 4, 8, 16 ... reaching n takes log2(n) iterations.

    Multiplying or dividing the loop variable => logarithmic.
    Adding or subtracting => linear.
    """
    visited = []
    i = 1
    while i < n:
        visited.append(i)
        i *= 2
    return visited


# ----------------------------------------------------------------------
# Example 5: digits in a number - O(log n)
# ----------------------------------------------------------------------
def count_digits(number):
    """Each division by 10 removes one digit: log10(n) steps.

    Any base of logarithm is O(log n) - bases differ by a constant factor,
    and Big O drops constants. That's why nobody writes the base.
    """
    number = abs(number)
    if number == 0:
        return 1
    digits = 0
    while number > 0:
        number //= 10
        digits += 1
    return digits


# ----------------------------------------------------------------------
# Example 6: O(n log n) - a linear loop whose body is logarithmic
# ----------------------------------------------------------------------
def search_many(sorted_items, targets):
    """Binary search, repeated for each target.

    Time: O(m log n) where m = len(targets), n = len(sorted_items)
    If m == n, that is O(n log n).
    """
    return [binary_search(sorted_items, t) for t in targets]


def _demo():
    print("=" * 62)
    print("O(log n) LOGARITHMIC - 1000x more data, only 10 more steps")
    print("=" * 62)

    print("\n  How many halvings to get from n down to 1?")
    for n in (10, 100, 1_000, 1_000_000, 1_000_000_000):
        print(f"    n = {n:>15,}  ->  {count_halvings(n):>2} steps")

    print("\n  Binary search step-by-step on a sorted list of 1..100, target 73:")
    data = list(range(1, 101))
    low, high, step = 0, len(data) - 1, 0
    while low <= high:
        step += 1
        mid = (low + high) // 2
        print(f"    step {step}: range [{low:>3}..{high:>3}]  mid={data[mid]:>3}  "
              f"{'FOUND' if data[mid] == 73 else ('go right' if data[mid] < 73 else 'go left')}")
        if data[mid] == 73:
            break
        if data[mid] < 73:
            low = mid + 1
        else:
            high = mid - 1
    print(f"    -> found in {step} steps instead of up to 100. log2(100) ~ 7")

    print("\n  Linear search vs binary search on 10,000,000 sorted items")
    print("  (worst case: the target is the very last element)")
    big = list(range(10_000_000))
    target = 9_999_999

    start = time.perf_counter()
    big.index(target)                    # O(n) scan
    linear = time.perf_counter() - start

    start = time.perf_counter()
    binary_search(big, target)           # O(log n)
    binary = time.perf_counter() - start

    print(f"    linear O(n)     : {linear:.6f}s")
    print(f"    binary O(log n) : {binary:.8f}s")
    print(f"    speed-up        : {linear / binary:,.0f}x")

    print("\n  Sanity checks:")
    s = [1, 3, 5, 7, 9, 11]
    print(f"    binary_search({s}, 7)  = {binary_search(s, 7)}")
    print(f"    binary_search({s}, 4)  = {binary_search(s, 4)}  (absent)")
    print(f"    binary_search_recursive({s}, 11) = {binary_search_recursive(s, 11)}")
    print(f"    doubling_loop(100) = {doubling_loop(100)}")
    print(f"    count_digits(98765) = {count_digits(98765)}")
    print("=" * 62)


if __name__ == "__main__":
    _demo()
