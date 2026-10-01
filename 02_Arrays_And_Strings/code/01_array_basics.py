"""
ARRAYS (Python lists) — the shelf of numbered boxes
===================================================
Goes with notes/01_what_is_an_array.md

Run me:  python3 code/01_array_basics.py
"""

import time
from collections import deque


# ----------------------------------------------------------------------
# The cheap moves: O(1)
# ----------------------------------------------------------------------
def get_box(items, i):
    """Grab one box by its number. INSTANT, however long the shelf is.

    Time: O(1)   Space: O(1)
    """
    return items[i]


def add_at_end(items, value):
    """Nobody has to move. Cheap.

    Time: O(1) (amortized)   Space: O(1)
    """
    items.append(value)
    return items


# ----------------------------------------------------------------------
# The fair moves: O(n)
# ----------------------------------------------------------------------
def find_box_number(items, value):
    """Where is this value? We may have to open every box.

    Time: O(n)   Space: O(1)
    """
    for i in range(len(items)):
        if items[i] == value:
            return i
    return -1


def add_everything_up(items):
    """Time: O(n)   Space: O(1)"""
    total = 0
    for value in items:
        total += value
    return total


# ----------------------------------------------------------------------
# The expensive moves: O(n) because EVERYONE SHUFFLES
# ----------------------------------------------------------------------
def add_at_front(items, value):
    """Every box shifts right to make room. Expensive.

    Time: O(n)   Space: O(1)
    """
    items.insert(0, value)
    return items


# ----------------------------------------------------------------------
# Walking the shelf, three ways
# ----------------------------------------------------------------------
def three_ways_to_walk(items):
    """All three are O(n). Pick the one that says what you mean."""
    way1 = [value for value in items]                      # just the values
    way2 = [(i, items[i]) for i in range(len(items))]      # index by hand
    way3 = [(i, value) for i, value in enumerate(items)]   # both, nicely
    return way1, way2, way3


def main():
    print("=" * 66)
    print("  ARRAYS - the shelf of numbered boxes")
    print("=" * 66)

    toys = [7, 12, 3, 9, 21]
    print(f"\n  Our shelf: {toys}")
    print("""
    box number:    0      1      2      3      4
                 +-----+------+------+------+------+
                 |  7  |  12  |  3   |  9   |  21  |
                 +-----+------+------+------+------+
    from back:    -5     -4     -3     -2     -1
""")
    print(f"    toys[0]   = {toys[0]}      <- first box")
    print(f"    toys[3]   = {toys[3]}      <- straight there, one step")
    print(f"    toys[-1]  = {toys[-1]}     <- last box")
    print(f"    toys[-2]  = {toys[-2]}      <- second from the end")
    print(f"    len(toys) = {len(toys)}      <- so the last box number is 4, not 5!")

    print("\n  Slicing - taking a piece of the shelf:")
    numbers = [10, 20, 30, 40, 50]
    print(f"    numbers        = {numbers}")
    print(f"    numbers[1:4]   = {numbers[1:4]}   <- boxes 1,2,3. STOPS BEFORE 4!")
    print(f"    numbers[:3]    = {numbers[:3]}")
    print(f"    numbers[2:]    = {numbers[2:]}")
    print(f"    numbers[::-1]  = {numbers[::-1]}   <- backwards")

    print("\n  Searching - we may open every box:")
    print(f"    find_box_number({toys}, 9)  = {find_box_number(toys, 9)}")
    print(f"    find_box_number({toys}, 99) = {find_box_number(toys, 99)}  (not found)")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  PROVING IT: grabbing a box costs the same on ANY shelf")
    print("=" * 66)

    tiny = list(range(10))
    huge = list(range(10_000_000))
    for label, shelf in (("10 boxes", tiny), ("10,000,000 boxes", huge)):
        start = time.perf_counter()
        for _ in range(200_000):
            get_box(shelf, len(shelf) - 1)
        elapsed = time.perf_counter() - start
        print(f"    200,000 grabs from a shelf of {label:<18} {elapsed:.4f}s")
    print("\n    Same time. A million times more boxes made no difference.")
    print("    THAT is O(1) - the superpower of arrays.")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  PROVING IT: the END is cheap, the FRONT is expensive")
    print("=" * 66)

    n = 50_000
    start = time.perf_counter()
    end_list = []
    for i in range(n):
        end_list.append(i)                 # O(1) each
    end_time = time.perf_counter() - start

    start = time.perf_counter()
    front_list = []
    for i in range(n):
        front_list.insert(0, i)            # O(n) each - everyone shuffles!
    front_time = time.perf_counter() - start

    print(f"\n    {n:,} x append(x)      [at the END]   : {end_time:.4f}s")
    print(f"    {n:,} x insert(0, x)   [at the FRONT] : {front_time:.4f}s")
    print(f"    -> the front is {front_time / end_time:,.0f}x slower")
    print("""
    Why? The boxes are nailed side by side with no gaps. To put
    something at the front, EVERY box has to shuffle right first.
    At the end, nobody moves.""")

    print("\n  Need a fast front? Use a deque (a shelf open at both ends):")
    start = time.perf_counter()
    d = deque()
    for i in range(n):
        d.appendleft(i)                    # O(1)!
    deque_time = time.perf_counter() - start
    print(f"    {n:,} x deque.appendleft(x)          : {deque_time:.4f}s")
    print(f"    -> {front_time / deque_time:,.0f}x faster than list.insert(0, x)")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  WALKING THE SHELF")
    print("=" * 66)
    fruits = ["apple", "banana", "cherry"]
    way1, way2, way3 = three_ways_to_walk(fruits)
    print(f"\n    for f in fruits              -> {way1}")
    print(f"    for i in range(len(fruits))  -> {way2}")
    print(f"    for i, f in enumerate(fruits)-> {way3}")
    print("\n    Use the first when you want values.")
    print("    Use enumerate when you need to know WHERE you are.")
    print("    (Two pointers and windows always need to know where they are.)")

    print("\n" + "=" * 66)
    print("""  REMEMBER:

    Grab box by number   -> O(1)  INSTANT   <- the superpower
    Search for a value   -> O(n)  fair
    Add/remove at END    -> O(1)  cheap
    Add/remove at FRONT  -> O(n)  expensive (everyone shuffles)
    Slicing              -> makes a COPY
    First box is 0. Last box is len - 1.""")
    print("=" * 66)


if __name__ == "__main__":
    main()
