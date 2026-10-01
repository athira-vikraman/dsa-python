"""
SOLUTIONS — with the reasoning
==============================
Read the WHY under each one. Choosing the technique is the skill;
the code is never the hard part.

Run me:  python3 exercises/solutions.py
"""


# ======================================================================
# PART A — two pointers, opposite ends
# ======================================================================
def reverse_list_in_place(items):
    """Time: O(n)   Space: O(1)

    WHY: one finger at each end. Swap, then step inward. They meet in the
    middle after n/2 swaps.

    `items[::-1]` is also O(n) time but O(n) SPACE - it builds a copy.
    When a question says "in place" or "O(1) space", this is the shape
    being asked for.
    """
    left, right = 0, len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items


def is_palindrome(word):
    """Time: O(n)   Space: O(1)

    WHY: the letters under the two fingers must match. Step inward until
    they meet.

    Two bonuses over `word == word[::-1]`: no copy (O(1) space), and it
    quits on the FIRST mismatch instead of reversing the whole thing.
    Be aware though - on a true palindrome, `word[::-1]` is faster in
    real seconds, because it runs in C. Same O(n), smaller constant.
    """
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def two_sum_sorted(numbers, target):
    """Time: O(n)   Space: O(1)

    WHY: the list is SORTED, which makes each step a safe decision:
      sum too small -> the only bigger numbers are right of `left`
      sum too big   -> the only smaller numbers are left of `right`
    So every step throws away a pair we can prove we don't need. The
    nested-loop version tests all n^2/2 pairs instead.

    This ONLY works on sorted data. Unsorted? Use a set.
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return (numbers[left], numbers[right])
        elif total < target:
            left += 1
        else:
            right -= 1
    return None


# ======================================================================
# PART B — reader & writer
# ======================================================================
def move_zeros_to_end(items):
    """Time: O(n)   Space: O(1)

    WHY: the reader inspects every box; the writer only advances when it
    has stored a keeper. Everything worth keeping ends up packed at the
    front, in its original order, and the tail gets filled with zeros.

    Two passes (n + n = 2n) is still O(n). Only NESTED loops multiply.
    """
    writer = 0
    for reader in range(len(items)):
        if items[reader] != 0:
            items[writer] = items[reader]
            writer += 1
    while writer < len(items):
        items[writer] = 0
        writer += 1
    return items


def remove_all(items, value):
    """Time: O(n)   Space: O(1)

    WHY: identical shape to move_zeros_to_end - only the `if` differs.
    We return the count because the tail still holds junk; the caller
    reads items[:count]. That is the standard contract for in-place
    filtering (and exactly what LeetCode asks for).

    Compare `while value in items: items.remove(value)` - that is O(n)
    to search PLUS O(n) to shift, every single call: O(n^2) overall.
    """
    writer = 0
    for reader in range(len(items)):
        if items[reader] != value:
            items[writer] = items[reader]
            writer += 1
    return writer


def remove_duplicates_sorted(items):
    """Time: O(n)   Space: O(1)

    WHY: in a SORTED list, duplicates are always neighbours. So we only
    need to compare against the last value we kept - no set required,
    which is how we get O(1) space instead of O(n).
    """
    if not items:
        return 0
    writer = 1
    for reader in range(1, len(items)):
        if items[reader] != items[writer - 1]:
            items[writer] = items[reader]
            writer += 1
    return writer


# ======================================================================
# PART C — fixed sliding window
# ======================================================================
def max_sum_of_k(numbers, k):
    """Time: O(n)   Space: O(1)

    WHY: when the window slides, only two numbers change - one joins,
    one leaves. The middle is untouched, so re-adding it is pure waste.

        window_sum += numbers[i] - numbers[i - k]

    Recalculating each window would be O(n*k). Each number now joins
    exactly once and leaves exactly once, so it's O(n) - and the cost
    doesn't depend on k at all.
    """
    if k <= 0 or len(numbers) < k:
        return None
    window_sum = sum(numbers[:k])
    best = window_sum
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        if window_sum > best:
            best = window_sum
    return best


def averages_of_k(numbers, k):
    """Time: O(n)   Space: O(n) for the output

    WHY: the same slide, dividing by k each time. Note what we DON'T do:
    `sum(numbers[i:i+k])` inside a loop would copy k items every round
    and quietly turn this back into O(n*k).
    """
    if k <= 0 or len(numbers) < k:
        return []
    result = []
    window_sum = sum(numbers[:k])
    result.append(window_sum / k)
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        result.append(window_sum / k)
    return result


# ======================================================================
# PART D — growing sliding window
# ======================================================================
def longest_without_repeats(text):
    """Time: O(n)   Space: O(k), k = distinct characters

    WHY: `right` grows the window. The moment a letter repeats, the rule
    is broken, so `left` walks forward until it isn't. The set tells us
    in O(1) whether a letter is currently inside.

    Why O(n) and not O(n^2) despite the inner `while`? Because `left`
    only ever moves FORWARD, at most n times across the entire run. So
    the total work is right's n steps + left's n steps = 2n.

    Remember: window size is right - left + 1.
    """
    seen = set()
    left = 0
    best = 0
    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1
        seen.add(text[right])
        best = max(best, right - left + 1)
    return best


def shortest_subarray_with_sum(numbers, target):
    """Time: O(n)   Space: O(1)

    WHY: this is the MIRROR of the "longest" problem, and the mirror is
    what trips people up:

        LONGEST  -> shrink while the window is BAD  (fix it, then measure)
        SHORTEST -> shrink while the window is GOOD (measure, then try
                    shorter)

    So the moment the sum reaches the target we record the length AND
    keep shrinking, because something shorter might also reach it.

    This needs all-positive numbers. With negatives, shrinking no longer
    reliably lowers the sum, and you need prefix sums instead.
    """
    left = 0
    window_sum = 0
    best = float("inf")
    for right in range(len(numbers)):
        window_sum += numbers[right]
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= numbers[left]
            left += 1
    return 0 if best == float("inf") else best


# ======================================================================
# PART E — strings
# ======================================================================
def reverse_words(sentence):
    """Time: O(n)   Space: O(n)

    WHY: `.split()` with no argument is doing us a favour - it splits on
    any run of whitespace AND drops empty pieces, so the extra spaces
    collapse for free. Then join once.

    Note we join at the end rather than `result += word` in a loop, which
    would be O(n^2).
    """
    return " ".join(reversed(sentence.split()))


def is_anagram(word_a, word_b):
    """Time: O(n)   Space: O(k), k = distinct characters

    WHY: count up for the first word, count down for the second. If every
    count lands on zero, the letters match exactly.

    `sorted(a) == sorted(b)` is correct but O(n log n). Counting is O(n).
    The length check is an O(1) exit for the commonest rejection.
    """
    if len(word_a) != len(word_b):
        return False
    counts = {}
    for char in word_a:
        counts[char] = counts.get(char, 0) + 1
    for char in word_b:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] == 0:
            del counts[char]
    return len(counts) == 0


def first_unique_char(text):
    """Time: O(n)   Space: O(k)

    WHY: you cannot know a character is unique until you've seen the whole
    string - so one pass to count, a second pass to find the first with a
    count of 1. Two passes, still O(n).

    The nested-loop version (for each char, scan the rest) is O(n^2).
    """
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    for i, char in enumerate(text):
        if counts[char] == 1:
            return i
    return -1


# ======================================================================
def _demo():
    print("=" * 70)
    print("SOLUTIONS - self-check")
    print("=" * 70)

    items = [1, 2, 3, 4]
    zeros = [0, 1, 0, 3, 12]
    threes = [3, 1, 3, 2]
    dups = [1, 1, 2, 2, 3]

    checks = [
        ("reverse_list_in_place([1,2,3,4])", reverse_list_in_place(items), [4, 3, 2, 1]),
        ("is_palindrome('madam')", is_palindrome("madam"), True),
        ("is_palindrome('hello')", is_palindrome("hello"), False),
        ("two_sum_sorted([1,3,5,7], 10)", two_sum_sorted([1, 3, 5, 7], 10), (3, 7)),
        ("move_zeros_to_end([0,1,0,3,12])", move_zeros_to_end(zeros), [1, 3, 12, 0, 0]),
        ("remove_all([3,1,3,2], 3)", remove_all(threes, 3), 2),
        ("remove_duplicates_sorted([1,1,2,2,3])", remove_duplicates_sorted(dups), 3),
        ("max_sum_of_k([2,1,5,1,3,2], 3)", max_sum_of_k([2, 1, 5, 1, 3, 2], 3), 9),
        ("averages_of_k([1,3,2,6], 2)", averages_of_k([1, 3, 2, 6], 2), [2.0, 2.5, 4.0]),
        ("longest_without_repeats('abcabcbb')", longest_without_repeats("abcabcbb"), 3),
        ("shortest_subarray_with_sum([2,1,5,2,3,2], 7)",
         shortest_subarray_with_sum([2, 1, 5, 2, 3, 2], 7), 2),
        ("reverse_words('  the sky  is blue ')",
         reverse_words("  the sky  is blue "), "blue is sky the"),
        ("is_anagram('listen','silent')", is_anagram("listen", "silent"), True),
        ("first_unique_char('leetcode')", first_unique_char("leetcode"), 0),
        ("first_unique_char('aabb')", first_unique_char("aabb"), -1),
    ]

    for label, got, expected in checks:
        status = "PASS" if got == expected else "FAIL"
        print(f"  [{status}] {label:<48} -> {got!r}")

    failures = sum(1 for _, g, e in checks if g != e)
    print("=" * 70)
    print(f"  {len(checks) - failures}/{len(checks)} checks passed")
    print("=" * 70)


if __name__ == "__main__":
    _demo()
