"""
O(1) — CONSTANT TIME
====================
The number of steps does NOT depend on the input size.
A list of 10 items or 10 million items: same work.

Run me:  python3 code/01_constant_time.py
"""

import time


# ----------------------------------------------------------------------
# Example 1: index access
# ----------------------------------------------------------------------
def first_element(items):
    """Return the first element.

    Time:  O(1) - one memory lookup, regardless of len(items)
    Space: O(1) - no extra storage
    """
    if not items:
        return None
    return items[0]


# ----------------------------------------------------------------------
# Example 2: arithmetic is constant time
# ----------------------------------------------------------------------
def is_even(number):
    """Time: O(1)   Space: O(1)"""
    return number % 2 == 0


# ----------------------------------------------------------------------
# Example 3: a dictionary lookup (the most useful O(1) in all of DSA)
# ----------------------------------------------------------------------
def get_price(prices, item_name):
    """Hash tables jump straight to the value; they do not scan.

    Time:  O(1) average   Space: O(1)
    """
    return prices.get(item_name, 0)


# ----------------------------------------------------------------------
# Example 4: STILL O(1) even with many statements
# ----------------------------------------------------------------------
def summary(items):
    """100 constant-time statements is still O(1): O(100) -> O(1).

    Big O measures GROWTH, not the absolute amount of work.
    """
    a = items[0] if items else None
    b = items[-1] if items else None
    c = len(items)          # len() on a Python list is O(1) - it is stored
    d = c * 2
    e = d + 7
    return (a, b, c, d, e)


# ----------------------------------------------------------------------
# Example 5: appending to the end of a list - O(1) amortized
# ----------------------------------------------------------------------
def add_item(items, value):
    """Time: O(1) amortized (see notes/06_recursion_and_amortized.md)"""
    items.append(value)
    return items


# ----------------------------------------------------------------------
# NOT O(1) - the common look-alikes
# ----------------------------------------------------------------------
def looks_constant_but_is_not(items):
    """LOOKS like one line. It is O(n): `in` scans the whole list."""
    return 42 in items          # O(n)!


def actually_constant(items_set):
    """Same question, but on a set: genuinely O(1)."""
    return 42 in items_set      # O(1)


def _demo():
    print("=" * 62)
    print("O(1) CONSTANT TIME - proof by measurement")
    print("=" * 62)

    small = list(range(10))
    large = list(range(10_000_000))

    for name, data in (("10 items", small), ("10,000,000 items", large)):
        start = time.perf_counter()
        for _ in range(100_000):
            first_element(data)
        elapsed = time.perf_counter() - start
        print(f"  first_element on {name:<20} 100k calls -> {elapsed:.4f}s")

    print("\n  The two times are nearly identical even though the input is")
    print("  a million times bigger. THAT is what O(1) means.\n")

    prices = {"pen": 10, "book": 250, "bag": 900}
    print(f"  get_price(prices, 'book') = {get_price(prices, 'book')}   # O(1)")
    print(f"  is_even(10)               = {is_even(10)}   # O(1)")
    print(f"  summary([1,2,3])          = {summary([1, 2, 3])}   # O(1)")

    print("\n  Look-alike check:")
    print("    `42 in my_list`  -> O(n)  (scans)")
    print("    `42 in my_set`   -> O(1)  (hashes)")
    print("=" * 62)


if __name__ == "__main__":
    _demo()
