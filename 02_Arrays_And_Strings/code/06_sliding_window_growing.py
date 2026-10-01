"""
SLIDING WINDOW — GROWING (the size changes as you go)
=====================================================
Goes with notes/04_sliding_window.md, section 4

No size is given. A RULE is given instead.
    right grows the window.
    while the rule is broken, left shrinks it.
    record the answer every step.

Run me:  python3 code/06_sliding_window_growing.py
"""

import time


# ----------------------------------------------------------------------
# 1. Longest stretch with no repeated letter
# ----------------------------------------------------------------------
def longest_without_repeats(text):
    """"abcabcbb" -> 3  (the stretch "abc")

    Rule: no letter may appear twice inside the window.

    Time:  O(n)   - see the note below about why this is NOT O(n^2)
    Space: O(k)   - the set holds at most k different letters
    """
    seen = set()
    left = 0
    best = 0

    for right in range(len(text)):
        while text[right] in seen:             # rule broken - shrink!
            seen.remove(text[left])
            left += 1

        seen.add(text[right])                  # now it's safe
        best = max(best, right - left + 1)     # mind the +1

    return best


# ----------------------------------------------------------------------
# 2. Shortest stretch that adds up to at least `target`
# ----------------------------------------------------------------------
def shortest_subarray_with_sum(numbers, target):
    """[2, 1, 5, 2, 3, 2], target 7 -> 2  (the stretch [5, 2])

    Rule: the window sum must be at least target.
    When it is, we have a candidate - so we SHRINK to try for shorter.

    Time: O(n)   Space: O(1)
    """
    left = 0
    window_sum = 0
    best = float("inf")

    for right in range(len(numbers)):
        window_sum += numbers[right]           # grow

        while window_sum >= target:            # good enough? try shorter
            best = min(best, right - left + 1)
            window_sum -= numbers[left]
            left += 1

    return 0 if best == float("inf") else best


# ----------------------------------------------------------------------
# 3. Longest stretch with at most k different letters
# ----------------------------------------------------------------------
def longest_with_at_most_k_distinct(text, k):
    """"araaci", k=2 -> 4  (the stretch "araa")

    Here the window needs a DICT, not a set, because we must know
    how many copies of each letter are inside.

    Time: O(n)   Space: O(k)
    """
    counts = {}
    left = 0
    best = 0

    for right in range(len(text)):
        counts[text[right]] = counts.get(text[right], 0) + 1    # grow

        while len(counts) > k:                 # too many different letters
            letter = text[left]
            counts[letter] -= 1
            if counts[letter] == 0:
                del counts[letter]             # that letter has left entirely
            left += 1

        best = max(best, right - left + 1)

    return best


# ----------------------------------------------------------------------
# 4. The brute-force versions, for comparison
# ----------------------------------------------------------------------
def longest_without_repeats_slow(text):
    """Check every possible stretch. Time: O(n^2) or worse. Space: O(n)."""
    best = 0
    for start in range(len(text)):
        seen = set()
        for end in range(start, len(text)):
            if text[end] in seen:
                break
            seen.add(text[end])
            best = max(best, end - start + 1)
    return best


def shortest_subarray_with_sum_slow(numbers, target):
    """Check every stretch. Time: O(n^2). Space: O(1)."""
    best = float("inf")
    for start in range(len(numbers)):
        total = 0
        for end in range(start, len(numbers)):
            total += numbers[end]
            if total >= target:
                best = min(best, end - start + 1)
                break
    return 0 if best == float("inf") else best


# ----------------------------------------------------------------------
# Tracing
# ----------------------------------------------------------------------
def _draw(text, left, right, note):
    """Draw the string with the window in brackets.

    Every letter gets a 3-character cell, so the columns stay lined up
    however big or small the window is.
    """
    cells = []
    for i, c in enumerate(text):
        opener = "[" if i == left else " "
        closer = "]" if i == right else " "
        cells.append(f"{opener}{c}{closer}")
    print(f"    {''.join(cells)}  {note}")


def trace_longest_without_repeats(text):
    print(f"\n  longest_without_repeats({text!r})")
    seen = set()
    left = 0
    best = 0

    for right in range(len(text)):
        while text[right] in seen:
            _draw(text, left, right - 1,
                  f"{text[right]!r} is already inside - SHRINK (drop {text[left]!r})")
            seen.remove(text[left])
            left += 1

        seen.add(text[right])
        size = right - left + 1
        flag = "  <- new best!" if size > best else ""
        best = max(best, size)
        _draw(text, left, right, f"added {text[right]!r}, window size {size}{flag}")

    print(f"    -> longest stretch with no repeats = {best}")
    return best


def trace_shortest_sum(numbers, target):
    print(f"\n  shortest_subarray_with_sum({numbers}, target={target})")
    left = 0
    window_sum = 0
    best = float("inf")

    for right in range(len(numbers)):
        window_sum += numbers[right]
        print(f"    grow:   window = {numbers[left:right + 1]}, sum = {window_sum}")

        while window_sum >= target:
            size = right - left + 1
            flag = "  <- new best!" if size < best else ""
            best = min(best, size)
            print(f"    hit {target}+: window = {numbers[left:right + 1]}, "
                  f"size {size}{flag} -> shrink to try shorter")
            window_sum -= numbers[left]
            left += 1

    answer = 0 if best == float("inf") else best
    print(f"    -> shortest stretch summing to >= {target} is {answer} long")
    return answer


def main():
    print("=" * 74)
    print("  SLIDING WINDOW - GROWING")
    print("=" * 74)
    print("""
  No size is given this time - a RULE is given.

      right walks forward, GROWING the window
      while the rule is broken, left walks forward, SHRINKING it
      record the answer after every step

  Window size is always:  right - left + 1   (don't forget the +1)""")

    trace_longest_without_repeats("abcabcbb")
    trace_longest_without_repeats("pwwkew")

    print("\n" + "=" * 74)
    print("  SHORTEST WINDOW THAT IS 'GOOD ENOUGH'")
    print("=" * 74)
    print("""
  Careful: this one is the MIRROR of the last one.
    Longest: shrink when the window is BAD.
    Shortest: shrink when the window is GOOD (to see if shorter also works).""")
    trace_shortest_sum([2, 1, 5, 2, 3, 2], 7)

    print("\n" + "=" * 74)
    print("  AT MOST K DIFFERENT LETTERS (the window needs a dict)")
    print("=" * 74)
    for text, k in (("araaci", 2), ("araaci", 1), ("cbbebi", 3)):
        print(f"\n    longest_with_at_most_k_distinct({text!r}, k={k}) = "
              f"{longest_with_at_most_k_distinct(text, k)}")
    print("""
    A set only answers "is it in there?". A dict also answers
    "how many copies?" - which is what we need to know when a letter
    leaves the window.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 74)
    print("  WHY IS THIS O(n)? There's a loop inside a loop!")
    print("=" * 74)
    print("""
    Good question - and the answer is the heart of the technique.

    Look at what the inner `while` actually does: it moves `left`
    FORWARD. Only ever forward. Never back.

    `left` starts at 0 and can never pass the end of the list. So across
    the WHOLE run, the inner loop can only run n times in total - no
    matter how those steps are spread out.

        right moves n times  +  left moves at most n times  =  2n steps

    2n is O(n). The nesting looks quadratic but isn't, because the two
    fingers only ever march in one direction.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 74)
    print("  SPEED: growing window O(n)  vs  checking every stretch O(n^2)")
    print("=" * 74)

    print(f"\n    {'size':>10} {'brute force O(n^2)':>22} {'window O(n)':>18}")
    for n in (3_000, 6_000, 12_000):
        text = "abcdefghij" * (n // 10)

        start = time.perf_counter()
        slow_answer = longest_without_repeats_slow(text)
        slow = time.perf_counter() - start

        start = time.perf_counter()
        fast_answer = longest_without_repeats(text)
        fast = time.perf_counter() - start

        assert slow_answer == fast_answer
        print(f"    {len(text):>10,} {slow:>21.4f}s {fast:>17.6f}s")

    numbers = list(range(1, 2001))
    assert (shortest_subarray_with_sum(numbers, 5000)
            == shortest_subarray_with_sum_slow(numbers, 5000))
    print("\n    (Both versions agree on every test - the asserts check it.)")

    print("\n" + "=" * 74)
    print("""  REMEMBER:

    left = 0
    for right in range(len(items)):
        # add items[right] to the window
        while <the rule is broken>:
            # remove items[left] from the window
            left += 1
        best = max(best, right - left + 1)

    LONGEST  -> shrink while the window is BAD
    SHORTEST -> shrink while the window is GOOD

    Use it when the problem gives a RULE instead of a size:
      "longest...", "shortest...", "at most k...", "sum at least X"
""")
    print("=" * 74)


if __name__ == "__main__":
    main()
