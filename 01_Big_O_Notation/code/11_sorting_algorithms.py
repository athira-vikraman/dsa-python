"""
THE NINE SORTS — the clearest Big O lesson there is
===================================================
Same job, nine ways, and the complexities range from O(n^2) to O(n + k).

The first six work by COMPARING pairs of values. No sort that does that can
beat O(n log n) in the worst case - that is a proven limit, not a missing
trick. The last three never compare anything: they count or bucket instead,
which is how they slip under the limit.

Every function here is written the simple way, not the clever way: one
statement per line, no tricks. Read it, then watch it run in
../visualizer.html.

Run me:  python3 code/11_sorting_algorithms.py
"""

import random
import time


# ======================================================================
# COMPARISON SORTS
# ======================================================================

def bubble_sort(items):
    """Swap neighbours that are in the wrong order, over and over.

    Best:  O(n)    - already sorted, the early exit fires on pass 1
    Worst: O(n^2)  - every pass bubbles one value to the end
    Space: O(1)    - sorts in place
    """
    items = list(items)
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def selection_sort(items):
    """Find the smallest value left, put it next.

    Always O(n^2) - no early exit is possible, because you cannot know a
    value is the smallest without looking at all the others.
    Space: O(1). Makes at most n swaps, which matters if writing is costly.
    """
    items = list(items)
    n = len(items)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
    return items


def insertion_sort(items):
    """Sort the way you sort a hand of playing cards.

    Best:  O(n)    - nearly sorted data: each card moves a step or two
    Worst: O(n^2)
    Space: O(1)

    This is the useful quadratic sort. Python's Timsort runs insertion sort
    on short chunks inside its O(n log n) merge.
    """
    items = list(items)
    for i in range(1, len(items)):
        card = items[i]
        j = i - 1
        while j >= 0 and items[j] > card:
            items[j + 1] = items[j]
            j = j - 1
        items[j + 1] = card
    return items


def merge_sort(items):
    """Split in half, sort each half, merge them back.

    O(n log n) in ALL cases - log n levels of splitting, O(n) work merging
    at each level.
    Space: O(n) for the merge buffers. Stable.
    """
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


def merge(left, right):
    """Merge two already-sorted lists. O(n + m)."""
    out = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i = i + 1
        else:
            out.append(right[j])
            j = j + 1
    while i < len(left):
        out.append(left[i])
        i = i + 1
    while j < len(right):
        out.append(right[j])
        j = j + 1
    return out


def quick_sort(items):
    """Pick a pivot, push smaller values left of it, repeat on each side.

    Average: O(n log n)  - a decent pivot roughly halves the job
    Worst:   O(n^2)      - a pivot that is always the min or max
    Space:   O(log n)    - the recursion stack

    Usually the fastest sort in practice, despite the worst case.
    """
    items = list(items)
    _quick_sort(items, 0, len(items) - 1)
    return items


def _quick_sort(items, low, high):
    if low >= high:
        return
    pivot = items[high]
    i = low
    for j in range(low, high):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            i = i + 1
    items[i], items[high] = items[high], items[i]
    _quick_sort(items, low, i - 1)
    _quick_sort(items, i + 1, high)


def heap_sort(items):
    """Build a heap so the biggest value is on top, then pull it off.

    O(n log n) in all cases, and Space: O(1) - the only sort that gives you
    both. The array IS the tree: the children of box p are 2p+1 and 2p+2.
    """
    items = list(items)
    n = len(items)
    for parent in range(n // 2 - 1, -1, -1):
        sift_down(items, parent, n)
    for end in range(n - 1, 0, -1):
        items[0], items[end] = items[end], items[0]
        sift_down(items, 0, end)
    return items


def sift_down(items, parent, size):
    """Push a value down until it sits above both its children."""
    big = parent
    left = 2 * parent + 1
    right = 2 * parent + 2
    if left < size and items[left] > items[big]:
        big = left
    if right < size and items[right] > items[big]:
        big = right
    if big != parent:
        items[parent], items[big] = items[big], items[parent]
        sift_down(items, big, size)


# ======================================================================
# NON-COMPARISON SORTS
#
# These never compare two values, so the O(n log n) limit does not apply.
# The price is a restriction on what they can sort.
# ======================================================================

def counting_sort(items):
    """Tally how many times each value appears, then write them out in order.

    Time:  O(n + k) where k is the size of the number range
    Space: O(k)

    Only for whole numbers in a SMALL range. Sorting values up to a million
    would need a million counters.
    """
    if not items:
        return []
    items = list(items)
    biggest = max(items)
    counts = [0] * (biggest + 1)
    for value in items:
        counts[value] = counts[value] + 1
    out = 0
    for value in range(len(counts)):
        for _ in range(counts[value]):
            items[out] = value
            out = out + 1
    return items


def radix_sort(items):
    """Sort by the ones digit, then the tens, then the hundreds.

    Time:  O(d x n) where d is the number of digits
    Space: O(n)

    Start from the LAST digit: each pass preserves the order of the pass
    before it, so earlier digits stay correctly ordered within later ones.
    """
    if not items:
        return []
    items = list(items)
    place = 1
    while max(items) // place > 0:
        buckets = [[] for _ in range(10)]
        for value in items:
            digit = (value // place) % 10
            buckets[digit].append(value)
        out = 0
        for bucket in buckets:
            for value in bucket:
                items[out] = value
                out = out + 1
        place = place * 10
    return items


def bucket_sort(items):
    """Spread values into buckets by size, sort each bucket, pour them out.

    Average: O(n + k)  - values spread evenly, each bucket stays tiny
    Worst:   O(n^2)    - everything lands in one bucket
    Space:   O(n)

    Five buckets, written out literally, because a beginner reading
    `[[] for _ in range(bucket_count)]` has to decode two things at once.
    """
    if not items:
        return []
    items = list(items)
    buckets = [[], [], [], [], []]
    biggest = max(items) + 1
    for value in items:
        index = value * 5 // biggest
        buckets[index].append(value)
    out = 0
    for bucket in buckets:
        bucket.sort()
        for value in bucket:
            items[out] = value
            out = out + 1
    return items


# ======================================================================
ALL_SORTS = [
    ("bubble_sort", bubble_sort, "O(n^2)", "compares"),
    ("selection_sort", selection_sort, "O(n^2)", "compares"),
    ("insertion_sort", insertion_sort, "O(n^2)", "compares"),
    ("merge_sort", merge_sort, "O(n log n)", "compares"),
    ("quick_sort", quick_sort, "O(n log n)", "compares"),
    ("heap_sort", heap_sort, "O(n log n)", "compares"),
    ("counting_sort", counting_sort, "O(n + k)", "counts"),
    ("radix_sort", radix_sort, "O(d x n)", "counts"),
    ("bucket_sort", bucket_sort, "O(n + k)", "counts"),
]


def main():
    print("=" * 70)
    print("  NINE SORTS, ONE LIST")
    print("=" * 70)

    sample = [5, 2, 9, 1, 7, 3]
    print(f"\n  input: {sample}")
    for name, func, big_o, kind in ALL_SORTS:
        print(f"    {name:<16} {big_o:<12} -> {func(sample)}")

    print("\n  All nine agree. Only the route differs.")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("  WATCH THE SHAPES: time as n doubles")
    print("=" * 70)
    print("""
  O(n^2)     should roughly QUADRUPLE each row
  O(n log n) should roughly DOUBLE, plus a little
  O(n + k)   should roughly DOUBLE
""")
    header = f"    {'n':>7}"
    for name, _, _, _ in ALL_SORTS:
        header += f" {name.replace('_sort',''):>10}"
    print(header)

    previous = {}
    for n in (500, 1000, 2000):
        data = [random.randint(0, 999) for _ in range(n)]
        row = f"    {n:>7}"
        for name, func, _, _ in ALL_SORTS:
            start = time.perf_counter()
            func(data)
            elapsed = time.perf_counter() - start
            if name in previous and previous[name] > 0:
                row += f" {elapsed / previous[name]:>9.1f}x"
            else:
                row += f" {elapsed * 1000:>9.1f}ms"
            previous[name] = elapsed
        print(row)

    print("""
    First row is the time in milliseconds; the rows below are the ratio
    against the row above. The quadratic three climb toward 4.0x while the
    rest stay near 2.0x. That gap is the whole point of Big O.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("  WHEN THE NUMBERS ARE SMALL, COUNTING WINS OUTRIGHT")
    print("=" * 70)
    data = [random.randint(0, 50) for _ in range(200_000)]

    start = time.perf_counter()
    merge_sort(data)
    merge_time = time.perf_counter() - start

    start = time.perf_counter()
    counting_sort(data)
    count_time = time.perf_counter() - start

    print(f"\n    200,000 values, all between 0 and 50:")
    print(f"      merge_sort    O(n log n) : {merge_time:.4f}s")
    print(f"      counting_sort O(n + k)   : {count_time:.4f}s")
    print(f"      -> counting is {merge_time / count_time:.1f}x faster")
    print("""
    Counting sort never compares two values, so the O(n log n) limit simply
    does not apply to it. But widen the range to 0..1,000,000 and it would
    need a million counters - that k is the price.""")

    print("\n" + "=" * 70)
    print("""  CHOOSING:

    Small or nearly sorted      -> insertion sort
    General purpose             -> quick sort (what most libraries use)
    Need a guarantee + stable   -> merge sort
    Need a guarantee + no RAM   -> heap sort
    Small whole numbers         -> counting sort
    Numbers with few digits     -> radix sort
    Values spread evenly        -> bucket sort
    Real Python code            -> sorted(), which is Timsort and beats
                                   everything here by a wide margin""")
    print("=" * 70)


if __name__ == "__main__":
    random.seed(1)
    main()
