"""
TWO POINTERS, SHAPE 1 — fingers at opposite ends, walking inward
================================================================
Goes with notes/03_two_pointers.md

A "pointer" is just a variable holding a box number. Your finger.
This file PRINTS where the fingers are at every step, so you can watch.

Run me:  python3 code/03_two_pointers_ends.py
"""

import time


# ----------------------------------------------------------------------
# 1. Reverse a list in place
# ----------------------------------------------------------------------
def reverse_in_place(items):
    """Swap the ends, then step inward. Repeat until the fingers meet.

    Time:  O(n)  - each finger walks halfway, so n/2 swaps
    Space: O(1)  - two number variables. NO new list.
    """
    left = 0
    right = len(items) - 1

    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

    return items


# ----------------------------------------------------------------------
# 2. Palindrome check
# ----------------------------------------------------------------------
def is_palindrome(word):
    """The letters under the two fingers must match.

    Time:  O(n)   Space: O(1)

    Compare with `word == word[::-1]`: also O(n) time, but O(n) SPACE,
    because it builds a reversed copy. This version builds nothing, and
    quits early on the first mismatch.
    """
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_ignoring_punctuation(text):
    """"A man, a plan, a canal: Panama" counts as a palindrome.

    Same two fingers, but they SKIP anything that isn't a letter or digit.
    Time: O(n)   Space: O(1)
    """
    left = 0
    right = len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1                                   # skip junk
        while left < right and not text[right].isalnum():
            right -= 1                                  # skip junk
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1

    return True


# ----------------------------------------------------------------------
# 3. Two Sum on a SORTED list  (the classic)
# ----------------------------------------------------------------------
def two_sum_sorted(numbers, target):
    """Find two numbers that add up to target. The list MUST be sorted.

    Sum too small -> move LEFT finger right  (need a bigger number)
    Sum too big   -> move RIGHT finger left  (need a smaller number)

    Time:  O(n)   <- down from O(n^2)
    Space: O(1)
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return (numbers[left], numbers[right])
        elif total < target:
            left += 1
        else:
            right -= 1

    return None


def two_sum_brute_force(numbers, target):
    """The slow way: test every pair. Time O(n^2), Space O(1)."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None


# ----------------------------------------------------------------------
# 4. Bonus: squares of a sorted array (a lovely two-pointer puzzle)
# ----------------------------------------------------------------------
def sorted_squares(numbers):
    """Input is sorted but may contain negatives: [-4, -1, 0, 3, 10]
    Output must be the squares, sorted: [0, 1, 9, 16, 100]

    The trick: the BIGGEST square is always at one of the two ENDS
    (because -4 squared is 16, bigger than 3 squared). So fill the
    answer from the back, taking the bigger end each time.

    Time: O(n)   Space: O(n) for the output
    (Sorting the squares would be O(n log n) - this beats it.)
    """
    result = [0] * len(numbers)
    left = 0
    right = len(numbers) - 1

    for position in range(len(numbers) - 1, -1, -1):     # fill back to front
        left_square = numbers[left] ** 2
        right_square = numbers[right] ** 2
        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1

    return result


# ----------------------------------------------------------------------
# Tracing helpers - these PRINT the fingers so you can see them move
# ----------------------------------------------------------------------
def _show_fingers(items, left, right, note=""):
    """Draw the list with ^ under the two fingers."""
    cells = [f"{v!s:>4}" for v in items]
    line = " ".join(cells)
    marks = [" " * 4] * len(items)
    if 0 <= left < len(items):
        marks[left] = "   L"
    if 0 <= right < len(items):
        marks[right] = "   R" if right != left else "  LR"
    print(f"    {line}")
    print(f"    {' '.join(marks)}   {note}")


def trace_reverse(items):
    print(f"\n  Reversing {items} with two fingers:")
    left, right = 0, len(items) - 1
    step = 0
    while left < right:
        step += 1
        _show_fingers(items, left, right, f"step {step}: swap {items[left]} and {items[right]}")
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    print(f"    {' '.join(f'{v!s:>4}' for v in items)}")
    print(f"    the fingers met - DONE after {step} swaps -> {items}")
    return items


def trace_palindrome(word):
    print(f"\n  Is {word!r} a palindrome?")
    letters = list(word)
    left, right = 0, len(word) - 1
    comparisons = 0
    while left < right:
        comparisons += 1
        same = letters[left] == letters[right]
        _show_fingers(letters, left, right,
                      f"{letters[left]!r} vs {letters[right]!r} -> {'match' if same else 'MISMATCH'}")
        if not same:
            print(f"    -> NOT a palindrome (found out after {comparisons} comparisons)")
            return False
        left += 1
        right -= 1
    print(f"    -> YES, a palindrome ({comparisons} comparisons for {len(word)} letters)")
    return True


def trace_two_sum(numbers, target):
    print(f"\n  Find two numbers in {numbers} that add to {target}:")
    left, right = 0, len(numbers) - 1
    steps = 0
    while left < right:
        steps += 1
        total = numbers[left] + numbers[right]
        if total == target:
            _show_fingers(numbers, left, right,
                          f"{numbers[left]} + {numbers[right]} = {total}  FOUND!")
            print(f"    -> ({numbers[left]}, {numbers[right]}) in {steps} steps")
            return (numbers[left], numbers[right])
        elif total < target:
            _show_fingers(numbers, left, right,
                          f"{numbers[left]} + {numbers[right]} = {total}  too SMALL -> move L right")
            left += 1
        else:
            _show_fingers(numbers, left, right,
                          f"{numbers[left]} + {numbers[right]} = {total}  too BIG -> move R left")
            right -= 1
    print(f"    -> no pair found ({steps} steps)")
    return None


def main():
    print("=" * 70)
    print("  TWO POINTERS - fingers at both ends, walking inward")
    print("=" * 70)
    print("""
  A pointer is just a variable holding a box number. Your finger.
  L = left finger, R = right finger. Watch them move.""")

    trace_reverse([1, 2, 3, 4, 5])
    trace_reverse([10, 20, 30, 40])

    print("\n" + "=" * 70)
    print("  PALINDROMES")
    print("=" * 70)
    trace_palindrome("madam")
    trace_palindrome("racecar")
    trace_palindrome("hello")

    print(f"\n  Ignoring punctuation and capitals:")
    tricky = "A man, a plan, a canal: Panama"
    print(f"    {tricky!r}")
    print(f"    -> {is_palindrome_ignoring_punctuation(tricky)}")

    print("\n" + "=" * 70)
    print("  TWO SUM on a SORTED list")
    print("=" * 70)
    trace_two_sum([1, 3, 5, 7, 9, 11], 14)
    trace_two_sum([2, 4, 6, 8], 7)
    print("""
    Why does moving a finger work? Because the list is SORTED.
      Sum too small? The only bigger numbers are to the RIGHT of L.
      Sum too big?   The only smaller numbers are to the LEFT of R.
    Each step throws away a pair you will never need again.

    On an UNSORTED list this logic means nothing - use a set instead.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("  SPEED: two pointers O(n)  vs  every pair O(n^2)")
    print("=" * 70)

    print(f"\n    {'list size':>12} {'brute force O(n^2)':>22} {'two pointers O(n)':>22}")
    for n in (2_000, 4_000, 8_000):
        numbers = list(range(n))
        target = n * 2 - 3           # worst case: the pair is far apart

        start = time.perf_counter()
        two_sum_brute_force(numbers, target)
        slow = time.perf_counter() - start

        start = time.perf_counter()
        two_sum_sorted(numbers, target)
        fast = time.perf_counter() - start

        print(f"    {n:>12,} {slow:>21.4f}s {fast:>21.6f}s")

    print("\n    The brute-force column QUADRUPLES each row (O(n^2)).")
    print("    The two-pointer column barely moves (O(n)).")

    print("\n" + "=" * 70)
    print("  BONUS: squares of a sorted array")
    print("=" * 70)
    data = [-4, -1, 0, 3, 10]
    print(f"\n    input:  {data}")
    print(f"    output: {sorted_squares(data)}")
    print("""
    The biggest square hides at one of the ENDS (-4 squared = 16 beats
    3 squared = 9). So we fill the answer from the BACK, each time taking
    the bigger end. O(n) - beats squaring then sorting, which is O(n log n).""")

    print("\n" + "=" * 70)
    print("""  REMEMBER:

    left, right = 0, len(items) - 1
    while left < right:
        ...look at items[left] and items[right]...
        move one finger (or both) inward

    Use it for: palindromes, reversing, pairs in SORTED data.
    Always O(n) time, O(1) space. Replaces nested loops.""")
    print("=" * 70)


if __name__ == "__main__":
    main()
