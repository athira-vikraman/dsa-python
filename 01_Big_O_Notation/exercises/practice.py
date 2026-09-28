"""
PRACTICE — your turn to write the code
======================================
Each function below has a docstring stating the REQUIRED complexity.
Replace the `pass` (or the TODO) with a working implementation.

Rules:
  * Meet the stated complexity. Passing the tests with an O(n^2) solution
    where O(n) is required means you have not finished the exercise.
  * Do not import anything beyond the standard library.

Check your work:
    python3 -m unittest discover -s tests -v

Model solutions with commentary: exercises/solutions.py
(Look ONLY after you have genuinely tried.)
"""


# ======================================================================
# 1. O(1) time, O(1) space
# ======================================================================
def get_first_and_last(items):
    """Return (first, last) as a tuple. Return (None, None) if empty.

    Required: O(1) time, O(1) space.
    Hint: indexing is O(1). Do not loop.
    """
    # TODO: implement
    pass


# ======================================================================
# 2. O(n) time, O(1) space
# ======================================================================
def count_occurrences(items, target):
    """Return how many times `target` appears in `items`.

    Required: O(n) time, O(1) space.
    """
    # TODO: implement
    pass


# ======================================================================
# 3. O(n) time, O(n) space
# ======================================================================
def has_duplicates(items):
    """Return True if any value appears more than once.

    Required: O(n) time, O(n) space.
    The obvious nested-loop answer is O(n^2) - do not use it.
    Hint: what data structure has O(1) membership testing?
    """
    # TODO: implement
    pass


# ======================================================================
# 4. O(n) time, O(n) space
# ======================================================================
def find_pair_with_sum(numbers, target):
    """Return a tuple (a, b) of two DIFFERENT elements whose values add
    up to `target`, or None if no such pair exists.

    Required: O(n) time, O(n) space.
    Hint: while scanning, for each value x ask "have I already seen
    target - x?" Store what you have seen in a dict.

    Example: find_pair_with_sum([2, 7, 11, 15], 9) -> (2, 7)
    """
    # TODO: implement
    pass


# ======================================================================
# 5. O(log n) time, O(1) space
# ======================================================================
def binary_search(sorted_items, target):
    """Return the index of `target` in a SORTED list, or -1.

    Required: O(log n) time, O(1) space.
    Do not use .index() and do not loop over every element.
    """
    # TODO: implement
    pass


# ======================================================================
# 6. O(n) time, O(1) space
# ======================================================================
def reverse_in_place(items):
    """Reverse `items` IN PLACE and return it.

    Required: O(n) time, O(1) space.
    So: no items[::-1], no reversed(), no new list. Two pointers.
    """
    # TODO: implement
    pass


# ======================================================================
# 7. O(n) time, O(n) space
# ======================================================================
def first_non_repeating(items):
    """Return the first value that appears exactly once, or None.

    Required: O(n) time, O(n) space.
    Hint: two passes are still O(n). Count first, then scan.

    Example: first_non_repeating(['a','b','a','c','b']) -> 'c'
    """
    # TODO: implement
    pass


# ======================================================================
# 8. O(n) time, O(1) space
# ======================================================================
def fibonacci(n):
    """Return the nth Fibonacci number (fibonacci(0) = 0, fibonacci(1) = 1).

    Required: O(n) time, O(1) space.
    So: no naive recursion (that is O(2^n)) and no memo dict (that is
    O(n) space). Two variables are enough.
    """
    # TODO: implement
    pass


# ======================================================================
# 9. O(n + m) time
# ======================================================================
def merge_sorted_lists(list_a, list_b):
    """Merge two ALREADY SORTED lists into one sorted list.

    Required: O(n + m) time.
    Do NOT do `sorted(list_a + list_b)` - that is O((n+m) log(n+m)) and
    throws away the fact that the inputs are already sorted.
    Hint: two pointers, one per list.
    """
    # TODO: implement
    pass


# ======================================================================
# 10. O(n) time
# ======================================================================
def most_frequent(items):
    """Return the value that appears most often. Return None if empty.
    If there is a tie, return the one that reached its count first.

    Required: O(n) time, O(n) space.
    """
    # TODO: implement
    pass


# ======================================================================
# 11. O(n) time
# ======================================================================
def is_anagram(word_a, word_b):
    """Return True if the two words use exactly the same letters.

    Required: O(n) time.
    sorted(a) == sorted(b) works but is O(n log n) - beat it.
    """
    # TODO: implement
    pass


# ======================================================================
# 12. O(total length) time
# ======================================================================
def build_sentence(words):
    """Join `words` into one space-separated string.

    Required: O(total length).
    Using `result += word + " "` in a loop is O(n^2) - do not.
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print("Implement the functions above, then run:")
    print("    python3 -m unittest discover -s tests -v")
