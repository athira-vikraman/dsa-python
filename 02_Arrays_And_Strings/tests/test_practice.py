"""
Tests for YOUR work in exercises/practice.py.

Exercises you haven't written yet are SKIPPED, so this reads as a
progress report rather than a wall of red.

Some tests check MORE than the answer:
  * in-place functions must really mutate the caller's list
  * window functions must be fast on big inputs, so a nested loop is
    caught even when the answer is correct

Run:  python3 -m unittest discover -s tests -v
Just this file:  python3 -m unittest test_practice -v
"""

import time
import unittest

from dsa_import import load_exercise

practice = load_exercise("practice.py")


def needs(func_name, *probe_args):
    """Skip the test if the student's function is still a `pass` stub."""
    func = getattr(practice, func_name, None)
    if func is None:
        return unittest.skip(f"{func_name} is missing from practice.py")
    try:
        result = func(*probe_args)
    except Exception:
        return lambda item: item          # it raised - let the test report it
    if result is None:
        return unittest.skip(f"{func_name} not implemented yet - your turn!")
    return lambda item: item


class TestPartA_TwoPointersEnds(unittest.TestCase):

    @needs("reverse_list_in_place", [1, 2])
    def test_reverse(self):
        self.assertEqual(practice.reverse_list_in_place([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(practice.reverse_list_in_place([1, 2, 3]), [3, 2, 1])
        self.assertEqual(practice.reverse_list_in_place([9]), [9])

    @needs("reverse_list_in_place", [1, 2])
    def test_reverse_is_in_place(self):
        original = [1, 2, 3]
        returned = practice.reverse_list_in_place(original)
        self.assertIs(returned, original,
                      "must mutate the caller's list - that's what O(1) space means")
        self.assertEqual(original, [3, 2, 1])

    @needs("is_palindrome", "aa")
    def test_palindrome(self):
        for word in ("madam", "racecar", "a", "abba"):
            self.assertTrue(practice.is_palindrome(word), word)
        for word in ("hello", "ab", "abca"):
            self.assertFalse(practice.is_palindrome(word), word)

    @needs("two_sum_sorted", [1, 2], 3)
    def test_two_sum_sorted(self):
        self.assertEqual(practice.two_sum_sorted([1, 3, 5, 7], 10), (3, 7))
        self.assertIsNone(practice.two_sum_sorted([1, 3, 5], 100))
        self.assertIsNone(practice.two_sum_sorted([1, 2, 3], 6),
                          "must not pair an element with itself")

    @needs("two_sum_sorted", [1, 2], 3)
    def test_two_sum_is_not_quadratic(self):
        """Two pointers takes ~8,000 steps here. Nested loops take ~32 million.

        The size is chosen so a wrong answer fails in a couple of seconds
        rather than making you wait a minute and a half.
        """
        n = 8_000
        numbers = list(range(n))
        target = 2 * n - 3                    # the very last pair: worst case
        start = time.perf_counter()
        practice.two_sum_sorted(numbers, target)
        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 0.3,
                        f"took {elapsed:.2f}s - looks like nested loops. "
                        "Use two pointers from the ends.")


class TestPartB_ReaderWriter(unittest.TestCase):

    @needs("move_zeros_to_end", [0, 1])
    def test_move_zeros(self):
        self.assertEqual(practice.move_zeros_to_end([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(practice.move_zeros_to_end([0, 0, 0]), [0, 0, 0])
        self.assertEqual(practice.move_zeros_to_end([1, 2, 3]), [1, 2, 3])
        self.assertEqual(practice.move_zeros_to_end([0, 5, 0, 1, 0, 9]), [5, 1, 9, 0, 0, 0])

    @needs("move_zeros_to_end", [0, 1])
    def test_move_zeros_is_in_place(self):
        original = [0, 1, 2]
        returned = practice.move_zeros_to_end(original)
        self.assertIs(returned, original,
                      "must mutate the caller's list, not return a new one")

    @needs("remove_all", [1, 2], 1)
    def test_remove_all(self):
        items = [3, 1, 3, 2]
        count = practice.remove_all(items, 3)
        self.assertEqual(count, 2)
        self.assertEqual(items[:count], [1, 2])

        items = [1, 2, 3]
        self.assertEqual(practice.remove_all(items, 9), 3)

    @needs("remove_duplicates_sorted", [1, 1])
    def test_remove_duplicates(self):
        items = [1, 1, 2, 2, 3]
        count = practice.remove_duplicates_sorted(items)
        self.assertEqual(count, 3)
        self.assertEqual(items[:count], [1, 2, 3])

        items = [5, 5, 5]
        count = practice.remove_duplicates_sorted(items)
        self.assertEqual(count, 1)
        self.assertEqual(items[:count], [5])

        self.assertEqual(practice.remove_duplicates_sorted([1]), 1)


class TestPartC_FixedWindow(unittest.TestCase):

    @needs("max_sum_of_k", [1, 2], 2)
    def test_max_sum_of_k(self):
        self.assertEqual(practice.max_sum_of_k([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(practice.max_sum_of_k([1, 4, 2, 10, 2, 3, 1, 0, 20], 4), 24)
        self.assertEqual(practice.max_sum_of_k([1, 2, 3], 3), 6)
        self.assertEqual(practice.max_sum_of_k([4, 9, 2], 1), 9)
        self.assertEqual(practice.max_sum_of_k([-5, -1, -3], 2), -4)

    @needs("max_sum_of_k", [1, 2], 2)
    def test_max_sum_handles_short_lists(self):
        self.assertIsNone(practice.max_sum_of_k([1, 2], 5))

    @needs("max_sum_of_k", [1, 2], 2)
    def test_max_sum_slides_not_recalculates(self):
        """A big window is the giveaway.

        Sliding does n steps whatever k is. Re-summing (or slicing) does
        n * k steps - about 275 million here versus 60 thousand.

        The size matters: `sum(numbers[i:i+k])` runs in C, so at smaller
        sizes it is slow in theory but still quick on the clock. Measured
        here: sliding ~0.006s, slicing ~1.3s. A clear gap either way.
        """
        numbers = list(range(60_000))
        start = time.perf_counter()
        practice.max_sum_of_k(numbers, 5_000)
        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 0.3,
                        f"took {elapsed:.2f}s - are you re-summing each window, "
                        "or slicing inside the loop? Use window_sum += new - old.")

    @needs("averages_of_k", [1, 2], 2)
    def test_averages(self):
        self.assertEqual(practice.averages_of_k([1, 3, 2, 6], 2), [2.0, 2.5, 4.0])
        self.assertEqual(practice.averages_of_k([1], 5), [])


class TestPartD_GrowingWindow(unittest.TestCase):

    @needs("longest_without_repeats", "ab")
    def test_longest_without_repeats(self):
        self.assertEqual(practice.longest_without_repeats("abcabcbb"), 3)
        self.assertEqual(practice.longest_without_repeats("bbbbb"), 1)
        self.assertEqual(practice.longest_without_repeats("pwwkew"), 3)
        self.assertEqual(practice.longest_without_repeats("abba"), 2)
        self.assertEqual(practice.longest_without_repeats("abcdef"), 6)

    @needs("longest_without_repeats", "ab")
    def test_longest_is_linear(self):
        """Every character is DIFFERENT - which is what makes this a real test.

        On a short alphabet like "abcabc...", a brute-force scan breaks out
        after a few letters and looks fast. With all-distinct characters it
        has to scan to the end from every starting point: ~8 million steps
        instead of 4 thousand.
        """
        text = "".join(chr(0x4E00 + i) for i in range(4_000))
        start = time.perf_counter()
        answer = practice.longest_without_repeats(text)
        elapsed = time.perf_counter() - start
        self.assertEqual(answer, 4_000, "all characters are distinct here")
        self.assertLess(elapsed, 0.3,
                        f"took {elapsed:.2f}s - are you checking every possible "
                        "substring? Grow with right, shrink with left.")

    @needs("shortest_subarray_with_sum", [5], 5)
    def test_shortest_subarray(self):
        self.assertEqual(practice.shortest_subarray_with_sum([2, 1, 5, 2, 3, 2], 7), 2)
        self.assertEqual(practice.shortest_subarray_with_sum([2, 1, 5, 2, 8], 7), 1)
        self.assertEqual(practice.shortest_subarray_with_sum([3, 4, 1, 1, 6], 8), 3)
        self.assertEqual(practice.shortest_subarray_with_sum([1, 1, 1], 3), 3)

    @needs("shortest_subarray_with_sum", [5], 5)
    def test_shortest_subarray_impossible(self):
        self.assertEqual(practice.shortest_subarray_with_sum([1, 2], 100), 0,
                         "return 0 when no window reaches the target")


class TestPartE_Strings(unittest.TestCase):

    @needs("reverse_words", "a b")
    def test_reverse_words(self):
        self.assertEqual(practice.reverse_words("the sky is blue"), "blue is sky the")
        self.assertEqual(practice.reverse_words("  the sky  is blue "), "blue is sky the")
        self.assertEqual(practice.reverse_words("hello"), "hello")

    @needs("is_anagram", "a", "a")
    def test_is_anagram(self):
        self.assertTrue(practice.is_anagram("listen", "silent"))
        self.assertTrue(practice.is_anagram("aabb", "bbaa"))
        self.assertFalse(practice.is_anagram("hello", "world"))
        self.assertFalse(practice.is_anagram("abc", "ab"))
        self.assertFalse(practice.is_anagram("aab", "abb"))

    @needs("first_unique_char", "a")
    def test_first_unique_char(self):
        self.assertEqual(practice.first_unique_char("leetcode"), 0)
        self.assertEqual(practice.first_unique_char("loveleetcode"), 2)
        self.assertEqual(practice.first_unique_char("aabb"), -1)
        self.assertEqual(practice.first_unique_char("z"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
