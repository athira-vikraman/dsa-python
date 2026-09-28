"""
SOLUTIONS — with the reasoning, not just the code
=================================================
Read the WHY under each one. The code is the easy part; choosing the
data structure is the skill being taught.

Run me:  python3 exercises/solutions.py
"""


# ======================================================================
# 1. O(1) time, O(1) space
# ======================================================================
def get_first_and_last(items):
    """Time: O(1)   Space: O(1)

    WHY: indexing into a Python list is a direct memory offset - one step
    whether the list holds 5 or 5 billion items. len() is O(1) too,
    because CPython stores the length rather than counting.
    """
    if not items:
        return (None, None)
    return (items[0], items[-1])


# ======================================================================
# 2. O(n) time, O(1) space
# ======================================================================
def count_occurrences(items, target):
    """Time: O(n)   Space: O(1)

    WHY: you must look at every element - there is no way to know if the
    last one matches without checking it. One counter variable, so O(1)
    space. (items.count(target) is the same O(n), just written in C.)
    """
    count = 0
    for value in items:
        if value == target:
            count += 1
    return count


# ======================================================================
# 3. O(n) time, O(n) space
# ======================================================================
def has_duplicates(items):
    """Time: O(n)   Space: O(n)

    WHY: the naive answer compares every pair - O(n^2). A set gives O(1)
    membership tests, so one pass suffices. We BOUGHT time WITH space:
    O(1) -> O(n) memory in exchange for O(n^2) -> O(n) time. Say that
    trade out loud in an interview.

    Bonus: we return as soon as we find a duplicate, so the best case
    is O(1).
    """
    seen = set()
    for value in items:
        if value in seen:        # O(1) average
            return True
        seen.add(value)          # O(1) average
    return False


# ======================================================================
# 4. O(n) time, O(n) space
# ======================================================================
def find_pair_with_sum(numbers, target):
    """Time: O(n)   Space: O(n)

    WHY: the brute force checks every pair - O(n^2). The insight: as you
    scan, you already know which number would complete the pair. Looking
    up "have I seen target - x?" in a set is O(1), so one pass is enough.

    This "complement" pattern is THE most common interview trick. Learn it
    once and you will use it constantly.
    """
    seen = set()
    for value in numbers:
        complement = target - value
        if complement in seen:           # O(1)
            return (complement, value)
        seen.add(value)
    return None


# ======================================================================
# 5. O(log n) time, O(1) space
# ======================================================================
def binary_search(sorted_items, target):
    """Time: O(log n)   Space: O(1)

    WHY: each comparison discards HALF of what remains. Halving n until
    1 takes log2(n) steps: a million items need only ~20 comparisons.
    Iterative, so no call stack - O(1) space. (The recursive version is
    equally fast but uses O(log n) space for the stack.)

    NOTE the `low + (high - low) // 2` form: in languages with fixed-size
    integers, (low + high) can overflow. Python integers are unbounded so
    it is safe here, but this habit travels well to C++/Java.
    """
    low = 0
    high = len(sorted_items) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ======================================================================
# 6. O(n) time, O(1) space
# ======================================================================
def reverse_in_place(items):
    """Time: O(n)   Space: O(1)

    WHY: items[::-1] is also O(n) time but allocates a whole second list -
    O(n) space. Two pointers walking toward each other swap n/2 pairs
    using only two extra variables. On a 10 GB list, this is the
    difference between working and running out of memory.
    """
    left = 0
    right = len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items


# ======================================================================
# 7. O(n) time, O(n) space
# ======================================================================
def first_non_repeating(items):
    """Time: O(n)   Space: O(n)

    WHY: two sequential passes is O(n) + O(n) = O(2n) = O(n). Students
    often assume two loops means O(n^2) - only NESTED loops multiply.

    Pass 1 counts. Pass 2 finds the first with count 1, in the original
    order (Python dicts preserve insertion order, so iterating `counts`
    would also work).
    """
    counts = {}
    for value in items:                       # pass 1: O(n)
        counts[value] = counts.get(value, 0) + 1

    for value in items:                       # pass 2: O(n)
        if counts[value] == 1:                # O(1) lookup
            return value
    return None


# ======================================================================
# 8. O(n) time, O(1) space
# ======================================================================
def fibonacci(n):
    """Time: O(n)   Space: O(1)

    WHY: naive recursion recomputes the same values exponentially often -
    O(2^n). Memoization fixes the time but costs O(n) memory. Iterating
    forward needs only the previous two values, so O(1) space.

    Best on BOTH axes. When a recursive solution is exponential, ask:
    "can I build the answer up from the bottom instead?" That question is
    the doorway to dynamic programming.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


# ======================================================================
# 9. O(n + m) time
# ======================================================================
def merge_sorted_lists(list_a, list_b):
    """Time: O(n + m)   Space: O(n + m) for the output

    WHY: sorted(list_a + list_b) is O((n+m) log(n+m)) - it throws away the
    fact that the inputs are ALREADY sorted. Two pointers exploit that:
    the next smallest element is always at one of the two fronts, so each
    element is examined exactly once.

    This merge step is the heart of merge sort.
    """
    merged = []
    i = j = 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            merged.append(list_a[i])
            i += 1
        else:
            merged.append(list_b[j])
            j += 1
    merged.extend(list_a[i:])      # whichever list still has items
    merged.extend(list_b[j:])
    return merged


# ======================================================================
# 10. O(n) time, O(n) space
# ======================================================================
def most_frequent(items):
    """Time: O(n)   Space: O(k) where k = number of distinct values

    WHY: counting with a dict is one O(n) pass; finding the max of k
    counts is O(k), and k <= n, so the total is O(n).

    Tracking the best value DURING the count avoids a second pass. Using
    strict `>` means the first value to reach a count keeps the title,
    which is the tie-break the docstring promises.

    (collections.Counter(items).most_common(1) does the same thing with
    the same complexity - use it in real code.)
    """
    if not items:
        return None
    counts = {}
    best_value = items[0]
    best_count = 0
    for value in items:
        counts[value] = counts.get(value, 0) + 1
        if counts[value] > best_count:        # strict > preserves the tie-break
            best_count = counts[value]
            best_value = value
    return best_value


# ======================================================================
# 11. O(n) time
# ======================================================================
def is_anagram(word_a, word_b):
    """Time: O(n)   Space: O(k), k = distinct characters (<= 26 for a-z)

    WHY: sorted(a) == sorted(b) is correct but O(n log n). Counting
    characters is O(n): count up for the first word, count down for the
    second, and every count must land on zero.

    The early length check is an O(1) exit for the commonest rejection.
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


# ======================================================================
# 12. O(total length)
# ======================================================================
def build_sentence(words):
    """Time: O(total length)   Space: O(total length)

    WHY: strings are immutable. `result += word` builds a brand-new
    string every iteration, copying everything accumulated so far:
    1 + 2 + 3 + ... + n = O(n^2) character copies.

    join() walks the list once to compute the final length, allocates
    exactly one buffer, and copies each character exactly once.
    """
    return " ".join(words)


# ======================================================================
def _demo():
    print("=" * 62)
    print("SOLUTIONS - quick self-check")
    print("=" * 62)
    checks = [
        ("get_first_and_last([1,2,3])", get_first_and_last([1, 2, 3]), (1, 3)),
        ("count_occurrences([1,2,2,3], 2)", count_occurrences([1, 2, 2, 3], 2), 2),
        ("has_duplicates([1,2,3])", has_duplicates([1, 2, 3]), False),
        ("has_duplicates([1,2,2])", has_duplicates([1, 2, 2]), True),
        ("find_pair_with_sum([2,7,11,15], 9)", find_pair_with_sum([2, 7, 11, 15], 9), (2, 7)),
        ("binary_search([1,3,5,7,9], 7)", binary_search([1, 3, 5, 7, 9], 7), 3),
        ("reverse_in_place([1,2,3,4])", reverse_in_place([1, 2, 3, 4]), [4, 3, 2, 1]),
        ("first_non_repeating(['a','b','a','c','b'])",
         first_non_repeating(['a', 'b', 'a', 'c', 'b']), 'c'),
        ("fibonacci(10)", fibonacci(10), 55),
        ("merge_sorted_lists([1,3,5],[2,4,6])", merge_sorted_lists([1, 3, 5], [2, 4, 6]),
         [1, 2, 3, 4, 5, 6]),
        ("most_frequent([1,2,2,3,3,3])", most_frequent([1, 2, 2, 3, 3, 3]), 3),
        ("is_anagram('listen','silent')", is_anagram('listen', 'silent'), True),
        ("is_anagram('hello','world')", is_anagram('hello', 'world'), False),
        ("build_sentence(['big','o','notation'])",
         build_sentence(['big', 'o', 'notation']), 'big o notation'),
    ]
    for label, got, expected in checks:
        status = "PASS" if got == expected else "FAIL"
        print(f"  [{status}] {label:<46} -> {got!r}")
    failures = sum(1 for _, g, e in checks if g != e)
    print("=" * 62)
    print(f"  {len(checks) - failures}/{len(checks)} checks passed")
    print("=" * 62)


if __name__ == "__main__":
    _demo()
