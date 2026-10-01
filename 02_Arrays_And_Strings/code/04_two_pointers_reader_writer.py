"""
TWO POINTERS, SHAPE 2 — reader & writer (both going the same way)
=================================================================
Goes with notes/03_two_pointers.md, section 4

The READER finger looks at every box.
The WRITER finger only moves when it has kept something.

Use this shape for: remove, filter, squash, "move all the X to the end"
                    - all IN PLACE, O(1) space.

Run me:  python3 code/04_two_pointers_reader_writer.py
"""


# ----------------------------------------------------------------------
# 1. Move all zeros to the end
# ----------------------------------------------------------------------
def move_zeros_to_end(items):
    """[0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]

    Time:  O(n)  - one pass, then one padding pass
    Space: O(1)  - no new list
    """
    writer = 0

    for reader in range(len(items)):
        if items[reader] != 0:
            items[writer] = items[reader]     # keep it
            writer += 1                       # writer only moves on a keeper

    while writer < len(items):                # pad the rest with zeros
        items[writer] = 0
        writer += 1

    return items


# ----------------------------------------------------------------------
# 2. Remove every copy of one value
# ----------------------------------------------------------------------
def remove_value(items, value):
    """Squash out every `value`. Returns how many items are left.

    The items AFTER the returned count are leftover junk - the caller
    only reads items[:count]. That is the usual contract for in-place
    filtering, and it is why we return a number instead of a list.

    Time: O(n)   Space: O(1)
    """
    writer = 0
    for reader in range(len(items)):
        if items[reader] != value:
            items[writer] = items[reader]
            writer += 1
    return writer


# ----------------------------------------------------------------------
# 3. Remove duplicates from a SORTED list
# ----------------------------------------------------------------------
def remove_duplicates_sorted(items):
    """[1, 1, 2, 2, 2, 3] -> first 3 boxes are [1, 2, 3]. Returns 3.

    Works because duplicates in a sorted list are always NEIGHBOURS,
    so we only need to compare with the last thing we kept.

    Time: O(n)   Space: O(1)
    """
    if not items:
        return 0

    writer = 1                                      # box 0 is always a keeper
    for reader in range(1, len(items)):
        if items[reader] != items[writer - 1]:      # different from last kept?
            items[writer] = items[reader]
            writer += 1
    return writer


# ----------------------------------------------------------------------
# 4. Keep only the even numbers
# ----------------------------------------------------------------------
def keep_only_even(items):
    """Same shape again - only the `if` changes.

    Time: O(n)   Space: O(1)
    """
    writer = 0
    for reader in range(len(items)):
        if items[reader] % 2 == 0:
            items[writer] = items[reader]
            writer += 1
    return writer


# ----------------------------------------------------------------------
# 5. Merge two sorted lists - one finger per list
# ----------------------------------------------------------------------
def merge_sorted(a, b):
    """A third shape: one finger walking each list.

    The next smallest item is always at one of the two fronts.
    Time: O(n + m)   Space: O(n + m) for the output
    """
    merged = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])          # whichever list has leftovers
    merged.extend(b[j:])
    return merged


# ----------------------------------------------------------------------
# Tracing
# ----------------------------------------------------------------------
def _show(items, writer, reader, note=""):
    cells = " ".join(f"{v!s:>4}" for v in items)
    marks = [" " * 4] * len(items)
    if writer < len(items):
        marks[writer] = "   W"
    if reader < len(items):
        marks[reader] = "   R" if reader != writer else "  WR"
    print(f"    {cells}")
    print(f"    {' '.join(marks)}   {note}")


def trace_move_zeros(items):
    print(f"\n  move_zeros_to_end({items})")
    writer = 0
    for reader in range(len(items)):
        if items[reader] != 0:
            _show(items, writer, reader, f"saw {items[reader]} - KEEP it, write at W")
            items[writer] = items[reader]
            writer += 1
        else:
            _show(items, writer, reader, "saw 0 - skip, W stays put")
    pad_from = writer
    while writer < len(items):
        items[writer] = 0
        writer += 1
    print(f"    {' '.join(f'{v!s:>4}' for v in items)}")
    print(f"    then pad boxes {pad_from}..{len(items) - 1} with zeros -> {items}")
    return items


def trace_remove_duplicates(items):
    print(f"\n  remove_duplicates_sorted({items})")
    if not items:
        return 0
    writer = 1
    for reader in range(1, len(items)):
        if items[reader] != items[writer - 1]:
            _show(items, writer, reader,
                  f"{items[reader]} is new (last kept was {items[writer - 1]}) - KEEP")
            items[writer] = items[reader]
            writer += 1
        else:
            _show(items, writer, reader, f"{items[reader]} is a repeat - skip")
    print(f"    kept {writer} unique items at the front: {items[:writer]}")
    print(f"    (boxes {writer}..{len(items) - 1} are leftover junk: {items[writer:]})")
    return writer


def main():
    print("=" * 70)
    print("  READER & WRITER - two fingers, same direction")
    print("=" * 70)
    print("""
  R = reader. It looks at EVERY box, one by one.
  W = writer. It only moves when the reader found something worth keeping.

  Think of it as tidying a shelf without buying a second shelf.""")

    trace_move_zeros([0, 1, 0, 3, 12])
    trace_move_zeros([1, 0, 0])

    print("\n" + "=" * 70)
    print("  REMOVING DUPLICATES FROM A SORTED LIST")
    print("=" * 70)
    trace_remove_duplicates([1, 1, 2, 2, 2, 3])
    print("""
    Why does it need to be SORTED? Because then all the copies of a
    value sit NEXT TO EACH OTHER, so we only have to compare with the
    last thing we kept. In an unsorted list you would need a set.""")

    print("\n" + "=" * 70)
    print("  THE SAME SHAPE, DIFFERENT `if`")
    print("=" * 70)

    examples = [
        ("remove every 3 from [3,1,3,2,3]", [3, 1, 3, 2, 3], lambda d: remove_value(d, 3)),
        ("keep only even in [1,2,3,4,5,6]", [1, 2, 3, 4, 5, 6], keep_only_even),
        ("remove dups in [1,1,1,2,3,3]", [1, 1, 1, 2, 3, 3], remove_duplicates_sorted),
    ]
    for label, data, func in examples:
        working = list(data)
        count = func(working)
        print(f"\n    {label}")
        print(f"      before: {data}")
        print(f"      after : {working[:count]}  (kept {count} items)")

    print("\n    Notice: all three are the SAME four lines of code.")
    print("    Only the `if` changes. Learn the shape once, reuse it forever.")

    print("\n" + "=" * 70)
    print("  A THIRD SHAPE: one finger per list (merging)")
    print("=" * 70)
    a = [1, 3, 5, 7]
    b = [2, 4, 6]
    print(f"\n    merge_sorted({a}, {b}) = {merge_sorted(a, b)}")
    print("""
    Both lists are already sorted, so the next smallest item must be at
    one of the two FRONTS. Take it, move that finger, repeat.
    O(n + m) - better than gluing them together and re-sorting,
    which would be O((n+m) log(n+m)).""")

    print("\n" + "=" * 70)
    print("""  REMEMBER:

    writer = 0
    for reader in range(len(items)):
        if <keep this one?>:
            items[writer] = items[reader]
            writer += 1
    # writer = how many we kept

    Use it when the problem says: remove, filter, squash, move all X,
    and especially when it says IN PLACE or O(1) extra space.""")
    print("=" * 70)


if __name__ == "__main__":
    main()
