"""
TIME vs SPACE — the beginner version
====================================
Goes with notes/05a_time_vs_space_for_beginners.md

Two questions about the same code:
    TIME  = how many STEPS does it do?
    SPACE = how many extra BOXES does it make?

This file answers the second question by MEASURING it. Watch the numbers.

Run me:  python3 code/10_time_vs_space_simple.py
"""

import tracemalloc


# ======================================================================
# PAIR 1: counting vs collecting
# ======================================================================
def count_evens(numbers):
    """COUNTING. One box, forever.

    Time:  O(n)  - looks at every number
    Space: O(1)  - just `count`, whether the list has 5 or 5 million items
    """
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


def collect_evens(numbers):
    """COLLECTING. A box that grows.

    Time:  O(n)  - same as above
    Space: O(n)  - `evens` holds one item per even number in the input
    """
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens


# ======================================================================
# PAIR 2: tracking one value vs copying everything
# ======================================================================
def biggest(numbers):
    """Time: O(n)   Space: O(1) - only ever remembers ONE number."""
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best


def copy_list(numbers):
    """Time: O(n)   Space: O(n) - a second list, the same size as the first."""
    new = []
    for n in numbers:
        new.append(n)
    return new


# ======================================================================
# PAIR 3: recursion (n chairs) vs a loop (1 chair)
# ======================================================================
def add_up_recursive(numbers, i=0):
    """Creates NO list. Still O(n) space!

    Each unfinished call waits in its own chair, and there are n of them.
    Time: O(n)   Space: O(n)
    """
    if i == len(numbers):
        return 0
    return numbers[i] + add_up_recursive(numbers, i + 1)


def add_up_loop(numbers):
    """Same answer. Nobody waits.

    Time: O(n)   Space: O(1)
    """
    total = 0
    for n in numbers:
        total += n
    return total


# ======================================================================
# Measuring helper
# ======================================================================
def extra_memory_kb(func, *args):
    """How much NEW memory did this function use, in kilobytes?

    tracemalloc watches Python's allocations. We reset it first, so the
    input list (allocated earlier) is not counted - exactly like space
    complexity, which only counts what the function itself creates.
    """
    tracemalloc.start()
    tracemalloc.reset_peak()
    func(*args)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024


def show_pair(title, o1_name, o1_func, on_name, on_func, sizes):
    print(f"\n  {title}")
    print(f"    {'list size':>12} {o1_name:>22} {on_name:>22}")
    for n in sizes:
        data = list(range(n))
        a = extra_memory_kb(o1_func, data)
        b = extra_memory_kb(on_func, data)
        print(f"    {n:>12,} {a:>19.2f} KB {b:>19,.2f} KB")


def main():
    print("=" * 66)
    print("  TIME vs SPACE - two different questions")
    print("=" * 66)
    print("""
  TIME  = how many steps?  -> we count loops
  SPACE = how many boxes?  -> we measure memory, below

  In every pair below, BOTH functions are O(n) TIME. They do the same
  amount of work. Only the memory is different. That is the whole point.
""")

    show_pair("PAIR 1: count the evens  vs  collect the evens",
              "count -> O(1)", count_evens,
              "collect -> O(n)", collect_evens,
              [10_000, 100_000, 1_000_000])

    print("\n    The left column stays FLAT. The right column GROWS with the list.")
    print("    Flat = O(1) space. Growing = O(n) space. You just saw both.")

    show_pair("PAIR 2: find the biggest  vs  copy the list",
              "biggest -> O(1)", biggest,
              "copy -> O(n)", copy_list,
              [10_000, 100_000, 1_000_000])

    print("\n    `biggest` remembers one number. `copy_list` remembers all of them.")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  THE SNEAKY ONE: recursion uses memory with no list in sight")
    print("=" * 66)

    data = list(range(900))
    print(f"\n    add_up_recursive(900 items) = {add_up_recursive(data)}")
    print(f"    add_up_loop(900 items)      = {add_up_loop(data)}")
    print("    Same answer. Now watch what happens with a bigger list:\n")

    big = list(range(100_000))
    print(f"    add_up_loop(100,000 items)      = {add_up_loop(big):,}   <- fine")
    try:
        add_up_recursive(big)
        print("    add_up_recursive(100,000 items) = finished")
    except RecursionError:
        print("    add_up_recursive(100,000 items) = RecursionError!")
        print("""
    THAT is space complexity hitting a wall.

    The recursive version needs one 'chair' per call - 100,000 chairs -
    and Python only keeps about 1,000. The loop needs ONE chair, so it
    does not care how long the list is.

    Recursion n levels deep = O(n) space. No list required.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  THE TRADE: buy speed with memory")
    print("=" * 66)

    import time

    def has_duplicate_slow(items):
        """O(n^2) time, O(1) space"""
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] == items[j]:
                    return True
        return False

    def has_duplicate_fast(items):
        """O(n) time, O(n) space"""
        seen = set()
        for item in items:
            if item in seen:
                return True
            seen.add(item)
        return False

    items = list(range(5_000))

    start = time.perf_counter()
    has_duplicate_slow(items)
    slow_time = time.perf_counter() - start
    slow_memory = extra_memory_kb(has_duplicate_slow, items)

    start = time.perf_counter()
    has_duplicate_fast(items)
    fast_time = time.perf_counter() - start
    fast_memory = extra_memory_kb(has_duplicate_fast, items)

    print(f"\n    {'':<14} {'time':>12} {'memory':>14}")
    print(f"    {'slow version':<14} {slow_time:>11.4f}s {slow_memory:>11.1f} KB")
    print(f"    {'fast version':<14} {fast_time:>11.6f}s {fast_memory:>11.1f} KB")
    print(f"""
    The fast one is {slow_time / fast_time:,.0f}x quicker, and uses about
    {fast_memory / max(slow_memory, 0.01):,.0f}x more memory.

    You did not get something for nothing. You PAID memory to BUY speed.
    Usually a great deal - and now you know it is a deal at all.""")

    print("\n" + "=" * 66)
    print("""  REMEMBER:

    TIME  = how many steps        SPACE = how many extra boxes
    Counting   -> O(1) space      Collecting -> O(n) space
    Loop       -> O(1) space      Recursion n deep -> O(n) space

  Read along with: notes/05a_time_vs_space_for_beginners.md""")
    print("=" * 66)


if __name__ == "__main__":
    main()
