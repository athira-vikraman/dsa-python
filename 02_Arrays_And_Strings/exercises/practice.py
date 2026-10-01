"""
PRACTICE — your turn
====================
Each function says which TECHNIQUE to use and what complexity to hit.
Replace the TODO with your code.

Rules:
  * Meet the stated complexity. Passing with a nested loop where O(n)
    was asked for means the exercise is not finished.
  * Where it says IN PLACE, do not build a second list.
  * Standard library only.

Check your work:
    python3 -m unittest discover -s tests -v

Stuck? The matching code/ file shows the same shape with a trace.
Model answers (look only after a real try): exercises/solutions.py
"""


# ======================================================================
# PART A — two pointers, opposite ends
# ======================================================================
def reverse_list_in_place(items):
    """Reverse `items` IN PLACE and return it.

    Technique: two pointers, opposite ends
    Required:  O(n) time, O(1) space
    So: no items[::-1], no reversed(), no new list.
    """
    # TODO
    pass


def is_palindrome(word):
    """True if `word` reads the same backwards.

    Technique: two pointers, opposite ends
    Required:  O(n) time, O(1) space
    (An empty string and a single letter both count as palindromes.)
    """
    # TODO
    pass


def two_sum_sorted(numbers, target):
    """`numbers` is SORTED. Return a tuple (a, b) of two values that add
    up to `target`, smaller first, or None.

    Technique: two pointers, opposite ends
    Required:  O(n) time, O(1) space    (the nested-loop way is O(n^2))

    Example: two_sum_sorted([1, 3, 5, 7], 10) -> (3, 7)
    """
    # TODO
    pass


# ======================================================================
# PART B — two pointers, reader & writer
# ======================================================================
def move_zeros_to_end(items):
    """Move every 0 to the end, keeping the order of the other numbers.
    Change `items` IN PLACE and return it.

    Technique: reader & writer
    Required:  O(n) time, O(1) space

    Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
    """
    # TODO
    pass


def remove_all(items, value):
    """Remove every copy of `value` IN PLACE. Return how many items are
    left. (Anything after that count is leftover junk - that's fine.)

    Technique: reader & writer
    Required:  O(n) time, O(1) space

    Example: remove_all([3, 1, 3, 2], 3) -> 2, items starts with [1, 2]
    """
    # TODO
    pass


def remove_duplicates_sorted(items):
    """`items` is SORTED. Squash duplicates IN PLACE. Return how many
    unique values are now at the front.

    Technique: reader & writer
    Required:  O(n) time, O(1) space

    Example: [1, 1, 2, 2, 3] -> 3, items starts with [1, 2, 3]
    """
    # TODO
    pass


# ======================================================================
# PART C — sliding window, fixed size
# ======================================================================
def max_sum_of_k(numbers, k):
    """Biggest sum of any `k` numbers in a row. None if the list is
    shorter than k.

    Technique: fixed sliding window
    Required:  O(n) time, O(1) space
    Hint:      window_sum += numbers[i] - numbers[i - k]

    Example: max_sum_of_k([2, 1, 5, 1, 3, 2], 3) -> 9
    """
    # TODO
    pass


def averages_of_k(numbers, k):
    """A list of the averages of every `k` numbers in a row.
    Empty list if the input is shorter than k.

    Technique: fixed sliding window
    Required:  O(n) time

    Example: averages_of_k([1, 3, 2, 6], 2) -> [2.0, 2.5, 4.0]
    """
    # TODO
    pass


# ======================================================================
# PART D — sliding window, growing
# ======================================================================
def longest_without_repeats(text):
    """Length of the longest stretch of letters with no repeats.

    Technique: growing window + a set
    Required:  O(n) time

    Example: "abcabcbb" -> 3   ("abc")
             "bbbb" -> 1
    """
    # TODO
    pass


def shortest_subarray_with_sum(numbers, target):
    """Length of the SHORTEST stretch whose sum is >= target.
    Return 0 if no stretch reaches the target.
    (All numbers are positive.)

    Technique: growing window
    Required:  O(n) time, O(1) space

    Example: shortest_subarray_with_sum([2, 1, 5, 2, 3, 2], 7) -> 2  ([5,2])

    CAREFUL: this is the mirror of the "longest" problem. Here you shrink
    while the window is GOOD, to see if something shorter also works.
    """
    # TODO
    pass


# ======================================================================
# PART E — strings
# ======================================================================
def reverse_words(sentence):
    """Reverse the ORDER of the words (not the letters). Collapse any
    extra spaces to one.

    Required: O(n) time

    Example: "  the sky  is blue " -> "blue is sky the"
    """
    # TODO
    pass


def is_anagram(word_a, word_b):
    """True if both words use exactly the same letters.

    Technique: a dict (counting)
    Required:  O(n) time
    (sorted(a) == sorted(b) works but is O(n log n) - beat it.)
    """
    # TODO
    pass


def first_unique_char(text):
    """Return the INDEX of the first character that appears only once,
    or -1 if there isn't one.

    Technique: a dict (count, then scan)
    Required:  O(n) time

    Example: "leetcode" -> 0   ('l')
             "aabb" -> -1
    """
    # TODO
    pass


if __name__ == "__main__":
    print("Fill in the functions above, then run:")
    print("    python3 -m unittest discover -s tests -v")
