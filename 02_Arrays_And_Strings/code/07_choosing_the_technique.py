"""
CHOOSING THE TECHNIQUE — the same problems, solved badly and well
=================================================================
Goes with notes/05_which_technique.md

Every pair below gives the SAME answer (asserts prove it). The only
difference is which tool was used - and how long it takes.

Run me:  python3 code/07_choosing_the_technique.py
"""

import random
import time


# ======================================================================
# PROBLEM 1: find a pair that adds to a target  (UNSORTED list)
# ======================================================================
def pair_sum_nested_loops(numbers, target):
    """Test every pair. Time: O(n^2)   Space: O(1)"""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False


def pair_sum_with_set(numbers, target):
    """"Have I already seen the number that completes this pair?"

    Time: O(n)   Space: O(n)

    THIS is the tool for an unsorted list. Two pointers would not work -
    the "move a finger for a bigger sum" logic needs sorted data.
    """
    seen = set()
    for number in numbers:
        if target - number in seen:        # O(1) lookup
            return True
        seen.add(number)
    return False


def pair_sum_two_pointers(numbers, target):
    """Only valid if the list is SORTED. Time: O(n)   Space: O(1)"""
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False


# ======================================================================
# PROBLEM 2: biggest sum of k numbers in a row
# ======================================================================
def max_window_slicing(numbers, k):
    """Uses slicing inside a loop - a hidden copy every round!

    Time: O(n * k)   Space: O(k)
    """
    best = None
    for start in range(len(numbers) - k + 1):
        total = sum(numbers[start:start + k])      # copies k items. Ouch.
        if best is None or total > best:
            best = total
    return best


def max_window_sliding(numbers, k):
    """Time: O(n)   Space: O(1)"""
    if len(numbers) < k:
        return None
    window_sum = sum(numbers[:k])
    best = window_sum
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        best = max(best, window_sum)
    return best


# ======================================================================
# PROBLEM 3: remove all zeros, in place
# ======================================================================
def remove_zeros_badly(items):
    """`remove` searches AND shifts, every single call.

    Time: O(n^2)   Space: O(1)
    """
    while 0 in items:            # O(n) search...
        items.remove(0)          # ...then O(n) shift
    return items


def remove_zeros_with_new_list(items):
    """Clear and correct, but it builds a second list.

    Time: O(n)   Space: O(n)
    """
    return [x for x in items if x != 0]


def remove_zeros_reader_writer(items):
    """In place, no extra memory. Time: O(n)   Space: O(1)"""
    writer = 0
    for reader in range(len(items)):
        if items[reader] != 0:
            items[writer] = items[reader]
            writer += 1
    del items[writer:]           # throw away the junk at the end
    return items


# ======================================================================
# PROBLEM 4: is this a palindrome?
# ======================================================================
def palindrome_by_copying(word):
    """Time: O(n)   Space: O(n) - [::-1] builds a reversed copy."""
    return word == word[::-1]


def palindrome_two_pointers(word):
    """Time: O(n)   Space: O(1) - and quits early on a mismatch."""
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def _time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    return result, time.perf_counter() - start


def main():
    print("=" * 74)
    print("  CHOOSING THE RIGHT TECHNIQUE")
    print("=" * 74)
    print("""
  Every pair below returns the SAME answer. Only the speed differs.
  Picking the tool IS the skill - the code is never the hard part.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 74)
    print("  PROBLEM 1: a pair that adds to a target, in an UNSORTED list")
    print("=" * 74)
    random.seed(7)
    numbers = random.sample(range(1_000_000), 4_000)
    target = numbers[-1] + numbers[-2]          # worst case: the last pair

    slow_answer, slow = _time(pair_sum_nested_loops, numbers, target)
    fast_answer, fast = _time(pair_sum_with_set, numbers, target)
    assert slow_answer == fast_answer

    print(f"\n    nested loops   O(n^2)  : {slow:.4f}s")
    print(f"    a set          O(n)    : {fast:.6f}s")
    print(f"    -> {slow / fast:,.0f}x faster, same answer ({fast_answer})")
    print("""
    NOT two pointers! The list is unsorted, so "move the left finger for
    a bigger sum" means nothing. For unsorted pair-finding, use a SET.""")

    ordered = sorted(numbers)
    sorted_answer, sorted_time = _time(pair_sum_two_pointers, ordered, target)
    assert sorted_answer == fast_answer
    print(f"    (if it WERE sorted, two pointers: {sorted_time:.6f}s, O(1) space)")

    # ------------------------------------------------------------------
    print("\n" + "=" * 74)
    print("  PROBLEM 2: biggest sum of k in a row")
    print("=" * 74)
    numbers = list(range(50_000))
    k = 1_000

    slice_answer, slice_time = _time(max_window_slicing, numbers, k)
    slide_answer, slide_time = _time(max_window_sliding, numbers, k)
    assert slice_answer == slide_answer

    print(f"\n    slicing in a loop  O(n*k) : {slice_time:.4f}s")
    print(f"    sliding window     O(n)   : {slide_time:.6f}s")
    print(f"    -> {slice_time / slide_time:,.0f}x faster, same answer ({slide_answer:,})")
    print("""
    The slicing version LOOKS like one line of work per round, but
    items[start:start+k] copies k items every time. Slicing inside a
    loop is the quietest way to ruin a good algorithm.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 74)
    print("  PROBLEM 3: remove all the zeros, in place")
    print("=" * 74)
    base = [0 if i % 3 == 0 else i for i in range(30_000)]

    a, bad_time = _time(remove_zeros_badly, list(base))
    b, list_time = _time(remove_zeros_with_new_list, list(base))
    c, rw_time = _time(remove_zeros_reader_writer, list(base))
    assert a == b == c

    print(f"\n    while 0 in items: remove(0)   O(n^2) : {bad_time:.4f}s")
    print(f"    build a new list              O(n)   : {list_time:.6f}s  (O(n) space)")
    print(f"    reader & writer               O(n)   : {rw_time:.6f}s  (O(1) space)")
    print(f"    -> all three agree: {len(a):,} items left")
    print("""
    The list comprehension is perfectly good Python! Use it unless the
    problem demands O(1) space - then reader & writer is the only option.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 74)
    print("  PROBLEM 4: palindrome check")
    print("=" * 74)
    long_palindrome = "a" * 2_000_000
    not_palindrome = "b" + "a" * 2_000_000       # fails on the FIRST compare

    _, copy_time = _time(palindrome_by_copying, long_palindrome)
    _, tp_time = _time(palindrome_two_pointers, long_palindrome)
    print(f"\n    a real palindrome, 2,000,000 letters:")
    print(f"      word == word[::-1]   : {copy_time:.4f}s   O(n) time, O(n) SPACE")
    print(f"      two pointers         : {tp_time:.4f}s   O(n) time, O(1) space")
    print(f"      -> the SLICING one is {tp_time / copy_time:,.0f}x faster here!")
    print("""
    READ THAT AGAIN. The "clever" two-pointer version LOST, badly.

    Why? Both are O(n). But [::-1] and == run as compiled C loops, while
    our two-pointer loop is interpreted Python, doing a comparison and
    two additions per letter. Same growth, wildly different constant.

    Big O deliberately ignores constants - and here the constant is
    "C versus Python", which is worth about 50x. This is exactly why
    Lesson 2 of Big O said: use Big O to pick the algorithm, use a
    benchmark to confirm the choice.""")

    _, copy_time = _time(palindrome_by_copying, not_palindrome)
    _, tp_time = _time(palindrome_two_pointers, not_palindrome)
    print(f"\n    NOT a palindrome (fails on the very first letter):")
    print(f"      word == word[::-1]   : {copy_time:.4f}s   <- still copied everything")
    print(f"      two pointers         : {tp_time:.8f}s   <- quit after 1 comparison!")
    print(f"      -> now two pointers is {copy_time / max(tp_time, 1e-9):,.0f}x faster")
    print("""
    So which is better? It depends on what you are asked:

      Fastest in Python on real input    -> word == word[::-1]
      O(1) space (a huge string, or an
      interviewer who demands it)        -> two pointers
      Early exit on bad input            -> two pointers

    Both answers are correct. Knowing WHY you picked one is the skill -
    and "the C version wins because of constant factors" is a genuinely
    senior thing to be able to say.""")

    print("\n" + "=" * 74)
    print("""  THE DECISION LIST:

    STRETCH of neighbours?     -> sliding window
    PAIR + sorted?             -> two pointers from the ends
    PAIR + unsorted?           -> a set
    Filter / remove IN PLACE?  -> reader & writer
    "Seen this before?"        -> a set or dict
    Nothing fits?              -> one plain loop

    "O(1) extra space" in the question = use two pointers.""")
    print("=" * 74)


if __name__ == "__main__":
    main()
