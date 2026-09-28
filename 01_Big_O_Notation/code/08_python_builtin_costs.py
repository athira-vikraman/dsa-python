"""
THE REAL COST OF PYTHON BUILT-INS
=================================
You cannot analyse your own code until you know what one line of Python
actually costs. Every trap below is measured live.

Run me:  python3 code/08_python_builtin_costs.py
"""

import time
from collections import deque


def _time_it(func, *args, repeat=1):
    start = time.perf_counter()
    for _ in range(repeat):
        func(*args)
    return time.perf_counter() - start


# ----------------------------------------------------------------------
# TRAP 1: `x in list` is O(n), `x in set` is O(1)
# ----------------------------------------------------------------------
def membership_in_list(data_list, targets):
    """Time: O(len(targets) * len(data_list))"""
    return sum(1 for t in targets if t in data_list)


def membership_in_set(data_set, targets):
    """Time: O(len(targets))"""
    return sum(1 for t in targets if t in data_set)


# ----------------------------------------------------------------------
# TRAP 2: list.pop(0) is O(n); deque.popleft() is O(1)
# ----------------------------------------------------------------------
def drain_list_from_front(n):
    """Time: O(n^2) - each pop(0) shifts every remaining element."""
    items = list(range(n))
    while items:
        items.pop(0)


def drain_deque_from_front(n):
    """Time: O(n) - deque is built for both ends."""
    items = deque(range(n))
    while items:
        items.popleft()


# ----------------------------------------------------------------------
# TRAP 3: string += in a loop is O(n^2); "".join() is O(n)
# ----------------------------------------------------------------------
def build_string_with_plus(n):
    """Strings are immutable, so each += must copy everything so far: O(n^2).

    CAUTION: CPython has a private optimisation that mutates the string
    in place when it holds the ONLY reference, which can hide the O(n^2)
    behaviour in this exact shape. It is an implementation detail - it
    does not apply in PyPy, or whenever a second reference exists (see
    build_string_with_plus_no_optimisation below).
    """
    result = ""
    for i in range(n):
        result += "x"
    return result


def build_string_with_plus_no_optimisation(n):
    """Same loop, but a second reference blocks CPython's in-place trick.

    This is the TRUE cost of string concatenation in a loop: O(n^2).
    """
    result = ""
    for i in range(n):
        alias = result          # a second reference -> must copy
        result = alias + "x"
    return result


def build_string_with_join(n):
    """One allocation at the end. O(n)."""
    return "".join("x" for _ in range(n))


# ----------------------------------------------------------------------
# TRAP 4: list.insert(0, x) is O(n); deque.appendleft() is O(1)
# ----------------------------------------------------------------------
def prepend_to_list(n):
    """Time: O(n^2)"""
    items = []
    for i in range(n):
        items.insert(0, i)
    return items


def prepend_to_deque(n):
    """Time: O(n)"""
    items = deque()
    for i in range(n):
        items.appendleft(i)
    return items


# ----------------------------------------------------------------------
# TRAP 5: slicing inside a loop copies every time
# ----------------------------------------------------------------------
def sum_with_slicing(items):
    """Each items[i:] copies the tail -> O(n^2)."""
    total = 0
    for i in range(len(items)):
        total += items[i:][0]
    return total


def sum_with_indexing(items):
    """Index access is O(1) -> O(n) overall."""
    total = 0
    for i in range(len(items)):
        total += items[i]
    return total


def _demo():
    print("=" * 66)
    print("THE COST OF PYTHON OPERATIONS - measured")
    print("=" * 66)

    # ---- TRAP 1 -------------------------------------------------------
    print("\n[TRAP 1]  `x in list`  O(n)   vs   `x in set`  O(1)")
    n = 50_000
    data_list = list(range(n))
    data_set = set(data_list)
    targets = list(range(0, n, n // 500))       # 500 lookups

    t_list = _time_it(membership_in_list, data_list, targets)
    t_set = _time_it(membership_in_set, data_set, targets)
    print(f"    500 lookups in a list of {n:,} : {t_list:.4f}s")
    print(f"    500 lookups in a set  of {n:,} : {t_set:.6f}s")
    print(f"    -> set is {t_list / t_set:,.0f}x faster")
    print("    FIX: if you test membership inside a loop, build a set first.")

    # ---- TRAP 2 -------------------------------------------------------
    print("\n[TRAP 2]  list.pop(0)  O(n)   vs   deque.popleft()  O(1)")
    n = 60_000
    t_list = _time_it(drain_list_from_front, n)
    t_deque = _time_it(drain_deque_from_front, n)
    print(f"    draining {n:,} items from the front of a list  : {t_list:.4f}s   (O(n^2))")
    print(f"    draining {n:,} items from the front of a deque : {t_deque:.4f}s   (O(n))")
    print(f"    -> deque is {t_list / t_deque:,.0f}x faster")
    print("    FIX: use collections.deque for queues and BFS.")

    # ---- TRAP 3 -------------------------------------------------------
    print("\n[TRAP 3]  string +=  O(n^2)   vs   ''.join()  O(n)")
    n = 60_000
    t_plus = _time_it(build_string_with_plus, n)
    t_plus_real = _time_it(build_string_with_plus_no_optimisation, n)
    t_join = _time_it(build_string_with_join, n)
    print(f"    {n:,} chars with += (CPython optimises this shape) : {t_plus:.4f}s")
    print(f"    {n:,} chars with += and a second reference        : {t_plus_real:.4f}s   <- the TRUE O(n^2)")
    print(f"    {n:,} chars with ''.join()                        : {t_join:.4f}s")
    print(f"    -> join is {t_plus_real / t_join:,.0f}x faster than honest concatenation")
    print("    NOTE: the first row looks fast only because CPython can mutate a")
    print("    string in place when nothing else references it. That is a private")
    print("    implementation detail - it vanishes in PyPy, or the moment anything")
    print("    else holds a reference. Always use ''.join().")

    # ---- TRAP 4 -------------------------------------------------------
    print("\n[TRAP 4]  list.insert(0, x)  O(n)   vs   deque.appendleft()  O(1)")
    n = 60_000
    t_list = _time_it(prepend_to_list, n)
    t_deque = _time_it(prepend_to_deque, n)
    print(f"    {n:,} prepends to a list  : {t_list:.4f}s   (O(n^2))")
    print(f"    {n:,} prepends to a deque : {t_deque:.4f}s   (O(n))")
    print(f"    -> deque is {t_list / t_deque:,.0f}x faster")

    # ---- TRAP 5 -------------------------------------------------------
    print("\n[TRAP 5]  slicing inside a loop copies the data")
    n = 20_000
    items = list(range(n))
    t_slice = _time_it(sum_with_slicing, items)
    t_index = _time_it(sum_with_indexing, items)
    print(f"    summing {n:,} items with items[i:] : {t_slice:.4f}s   (O(n^2))")
    print(f"    summing {n:,} items with items[i]  : {t_index:.4f}s   (O(n))")
    print(f"    -> indexing is {t_slice / t_index:,.0f}x faster")
    print("    FIX: pass indices around instead of slicing.")

    # ---- append is amortized O(1) -------------------------------------
    print("\n[AMORTIZED]  list.append() is O(1) on average")
    print("    Appending n items and timing the TOTAL:")
    previous = None
    for n in (250_000, 500_000, 1_000_000, 2_000_000):
        def append_n(count=n):
            out = []
            for i in range(count):
                out.append(i)
        elapsed = _time_it(append_n)
        ratio = f"{elapsed / previous:.2f}x" if previous else "  -  "
        print(f"      n = {n:>9,}   total = {elapsed:.4f}s   vs previous: {ratio}")
        previous = elapsed
    print("    Ratios ~2.00 => total O(n) => O(1) per append, amortized,")
    print("    even though individual appends occasionally resize the list.")

    print("\n" + "=" * 66)
    print("Full table: notes/07_python_operation_costs.md")
    print("=" * 66)


if __name__ == "__main__":
    _demo()
