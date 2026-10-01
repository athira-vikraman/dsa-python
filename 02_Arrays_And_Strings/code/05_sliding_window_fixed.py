"""
SLIDING WINDOW — FIXED SIZE
===========================
Goes with notes/04_sliding_window.md

The train window shows k seats. As the train moves, one seat joins on the
right and one leaves on the left. Everything in the middle is unchanged -
so don't recalculate it!

    window_sum += items[i] - items[i - k]      <- joiner minus leaver

Run me:  python3 code/05_sliding_window_fixed.py
"""

import time


# ----------------------------------------------------------------------
# 1. The slow way - recalculating every window
# ----------------------------------------------------------------------
def max_sum_of_k_slow(numbers, k):
    """Add up each window from scratch.

    Time:  O(n * k)  <- re-adds the same numbers again and again
    Space: O(1)
    """
    if len(numbers) < k:
        return None

    best = None
    for start in range(len(numbers) - k + 1):
        total = 0
        for i in range(start, start + k):      # the wasteful inner loop
            total += numbers[i]
        if best is None or total > best:
            best = total
    return best


# ----------------------------------------------------------------------
# 2. The sliding window way
# ----------------------------------------------------------------------
def max_sum_of_k(numbers, k):
    """Slide the window: add the joiner, subtract the leaver.

    Time:  O(n)  - each number joins once and leaves once
    Space: O(1)
    """
    if len(numbers) < k:
        return None

    window_sum = sum(numbers[:k])              # build the FIRST window
    best = window_sum

    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]    # joiner - leaver
        if window_sum > best:
            best = window_sum

    return best


# ----------------------------------------------------------------------
# 3. Averages of every window (same trick)
# ----------------------------------------------------------------------
def averages_of_k(numbers, k):
    """The average temperature of every k consecutive days.

    Time: O(n)   Space: O(n) for the output list
    """
    if len(numbers) < k:
        return []

    result = []
    window_sum = sum(numbers[:k])
    result.append(window_sum / k)

    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        result.append(window_sum / k)

    return result


# ----------------------------------------------------------------------
# 4. A window that is not a sum: count the vowels
# ----------------------------------------------------------------------
def max_vowels_in_k(text, k):
    """Most vowels in any k letters in a row.

    The window doesn't have to hold a SUM. Anything you can update
    with "+1 for the joiner, -1 for the leaver" works.

    Time: O(n)   Space: O(1)
    """
    if len(text) < k:
        return 0

    vowels = set("aeiouAEIOU")
    count = sum(1 for c in text[:k] if c in vowels)
    best = count

    for i in range(k, len(text)):
        if text[i] in vowels:                  # joiner
            count += 1
        if text[i - k] in vowels:              # leaver
            count -= 1
        best = max(best, count)

    return best


# ----------------------------------------------------------------------
# Tracing
# ----------------------------------------------------------------------
def trace_window(numbers, k):
    """Draw the window sliding along, step by step."""
    print(f"\n  max_sum_of_k({numbers}, k={k})")
    if len(numbers) < k:
        print("    list is shorter than the window - nothing to do")
        return None

    window_sum = sum(numbers[:k])
    best = window_sum

    # draw the first window
    parts = []
    for i, v in enumerate(numbers):
        if i == 0:
            parts.append(f"[{v:>3}")
        elif i == k - 1:
            parts.append(f"{v:>3} ]")
        elif i < k:
            parts.append(f"{v:>3}")
        else:
            parts.append(f"{v:>3}")
    print(f"    {' '.join(parts)}   first window: sum = {window_sum}")

    for i in range(k, len(numbers)):
        joiner = numbers[i]
        leaver = numbers[i - k]
        window_sum += joiner - leaver

        parts = []
        for j, v in enumerate(numbers):
            if j == i - k + 1:
                parts.append(f"[{v:>3}")
            elif j == i:
                parts.append(f"{v:>3} ]")
            else:
                parts.append(f"{v:>3}")
        marker = "  <- new best!" if window_sum > best else ""
        print(f"    {' '.join(parts)}   {leaver} left, {joiner} joined: "
              f"{window_sum - joiner + leaver} - {leaver} + {joiner} = {window_sum}{marker}")
        best = max(best, window_sum)

    print(f"    -> biggest window sum = {best}")
    return best


def main():
    print("=" * 74)
    print("  SLIDING WINDOW - FIXED SIZE")
    print("=" * 74)
    print("""
  The train window shows k seats at a time. When the train moves:
      ONE seat joins on the right.
      ONE seat leaves on the left.
      Everything in the middle is the SAME.

  So never re-add the middle. Just:  sum += joiner - leaver""")

    trace_window([2, 1, 5, 1, 3, 2], 3)
    trace_window([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)

    print("\n" + "=" * 74)
    print("  AVERAGES OF EVERY WINDOW (same trick)")
    print("=" * 74)
    temps = [30, 32, 31, 35, 36, 34, 33]
    print(f"\n    daily temperatures: {temps}")
    print(f"    3-day averages    : {[round(a, 1) for a in averages_of_k(temps, 3)]}")

    print("\n" + "=" * 74)
    print("  A WINDOW DOESN'T HAVE TO HOLD A SUM")
    print("=" * 74)
    text = "abciiidef"
    print(f"\n    most vowels in any 3 letters of {text!r} = {max_vowels_in_k(text, 3)}")
    print("    (the window 'iii' has 3 vowels)")
    print("\n    We just did +1 for the joiner and -1 for the leaver.")
    print("    Anything you can update that way can slide.")

    # ------------------------------------------------------------------
    print("\n" + "=" * 74)
    print("  SPEED: sliding window O(n)  vs  recalculating O(n*k)")
    print("=" * 74)

    print(f"\n    {'list size':>12} {'window k':>10} {'slow O(n*k)':>16} {'window O(n)':>16}")
    for n, k in ((20_000, 100), (20_000, 500), (40_000, 500)):
        numbers = list(range(n))

        start = time.perf_counter()
        slow_answer = max_sum_of_k_slow(numbers, k)
        slow = time.perf_counter() - start

        start = time.perf_counter()
        fast_answer = max_sum_of_k(numbers, k)
        fast = time.perf_counter() - start

        assert slow_answer == fast_answer, "both must give the same answer!"
        print(f"    {n:>12,} {k:>10,} {slow:>15.4f}s {fast:>15.6f}s")

    print("\n    Same answers (the assert checks it). The slow one gets worse")
    print("    as the WINDOW grows; the sliding one doesn't care about k at all.")

    print("\n" + "=" * 74)
    print("""  REMEMBER:

    window_sum = sum(items[:k])            # build the first window
    best = window_sum
    for i in range(k, len(items)):
        window_sum += items[i] - items[i - k]      # joiner - leaver
        best = max(best, window_sum)

    Use it when the problem gives you a SIZE:
      "any k in a row", "every 7 days", "a substring of length 4"

    O(n) time, O(1) space.""")
    print("=" * 74)


if __name__ == "__main__":
    main()
