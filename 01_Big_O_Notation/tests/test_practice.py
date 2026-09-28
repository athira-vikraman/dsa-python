"""
Tests for YOUR work in exercises/practice.py.

Exercises you have not written yet are SKIPPED, not failed - so the
output is a progress report, not a wall of red.

Run:  python3 -m unittest discover -s tests -v
Or just this file:  python3 -m unittest tests.test_practice -v
"""

import unittest

from dsa_import import load_exercise

practice = load_exercise("practice.py")


def skip_if_unimplemented(func_name, *probe_args):
    """Skip the test when the student's function is still a `pass` stub."""
    func = getattr(practice, func_name, None)
    if func is None:
        return unittest.skip(f"{func_name} is missing from practice.py")
    try:
        result = func(*probe_args)
    except Exception:
        return lambda test_item: test_item        # raised -> let the test report it
    if result is None:
        return unittest.skip(f"{func_name} not implemented yet - your turn!")
    return lambda test_item: test_item


class TestPractice(unittest.TestCase):

    @skip_if_unimplemented("get_first_and_last", [1, 2, 3])
    def test_01_get_first_and_last(self):
        self.assertEqual(practice.get_first_and_last([1, 2, 3, 4]), (1, 4))
        self.assertEqual(practice.get_first_and_last([7]), (7, 7))
        self.assertEqual(practice.get_first_and_last([]), (None, None))

    @skip_if_unimplemented("count_occurrences", [1, 1], 1)
    def test_02_count_occurrences(self):
        self.assertEqual(practice.count_occurrences([1, 2, 2, 3, 2], 2), 3)
        self.assertEqual(practice.count_occurrences([1, 2, 3], 9), 0)
        self.assertEqual(practice.count_occurrences([], 1), 0)

    @skip_if_unimplemented("has_duplicates", [1, 1])
    def test_03_has_duplicates(self):
        self.assertTrue(practice.has_duplicates([1, 2, 3, 2]))
        self.assertFalse(practice.has_duplicates([1, 2, 3, 4]))
        self.assertFalse(practice.has_duplicates([]))

    @skip_if_unimplemented("find_pair_with_sum", [2, 7], 9)
    def test_04_find_pair_with_sum(self):
        self.assertEqual(sorted(practice.find_pair_with_sum([2, 7, 11, 15], 9)), [2, 7])
        self.assertIsNone(practice.find_pair_with_sum([1, 2, 3], 100))
        self.assertIsNone(practice.find_pair_with_sum([5, 1, 2], 10),
                          "must not pair an element with itself")

    @skip_if_unimplemented("binary_search", [1, 2, 3], 2)
    def test_05_binary_search(self):
        data = [1, 3, 5, 7, 9, 11, 13]
        for index, value in enumerate(data):
            self.assertEqual(practice.binary_search(data, value), index)
        self.assertEqual(practice.binary_search(data, 4), -1)
        self.assertEqual(practice.binary_search([], 1), -1)

    @skip_if_unimplemented("reverse_in_place", [1, 2])
    def test_06_reverse_in_place(self):
        self.assertEqual(practice.reverse_in_place([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(practice.reverse_in_place([1, 2, 3]), [3, 2, 1])
        original = [1, 2, 3]
        returned = practice.reverse_in_place(original)
        self.assertIs(returned, original, "must reverse IN PLACE - O(1) space")
        self.assertEqual(original, [3, 2, 1])

    @skip_if_unimplemented("first_non_repeating", ['a'])
    def test_07_first_non_repeating(self):
        self.assertEqual(practice.first_non_repeating(['a', 'b', 'a', 'c', 'b']), 'c')
        self.assertEqual(practice.first_non_repeating([1, 2, 2, 3, 3]), 1)
        self.assertIsNone(practice.first_non_repeating([1, 1, 2, 2]))

    @skip_if_unimplemented("fibonacci", 5)
    def test_08_fibonacci(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for n, value in enumerate(expected):
            self.assertEqual(practice.fibonacci(n), value, f"fibonacci({n})")

    @skip_if_unimplemented("fibonacci", 5)
    def test_08b_fibonacci_is_not_exponential(self):
        """fibonacci(35) finishes instantly at O(n) and crawls at O(2^n)."""
        import time
        start = time.perf_counter()
        practice.fibonacci(35)
        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 0.5,
                        "too slow - looks like naive O(2^n) recursion. "
                        "Build the answer up with two variables instead.")

    @skip_if_unimplemented("merge_sorted_lists", [1], [2])
    def test_09_merge_sorted_lists(self):
        self.assertEqual(practice.merge_sorted_lists([1, 3, 5], [2, 4, 6]),
                         [1, 2, 3, 4, 5, 6])
        self.assertEqual(practice.merge_sorted_lists([], [1, 2]), [1, 2])
        self.assertEqual(practice.merge_sorted_lists([1, 2], []), [1, 2])
        self.assertEqual(practice.merge_sorted_lists([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])

    @skip_if_unimplemented("most_frequent", [1])
    def test_10_most_frequent(self):
        self.assertEqual(practice.most_frequent([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(practice.most_frequent([7]), 7)
        self.assertIsNone(practice.most_frequent([]))
        self.assertEqual(practice.most_frequent(['a', 'b', 'a', 'b']), 'a')

    @skip_if_unimplemented("is_anagram", "a", "a")
    def test_11_is_anagram(self):
        self.assertTrue(practice.is_anagram('listen', 'silent'))
        self.assertFalse(practice.is_anagram('hello', 'world'))
        self.assertFalse(practice.is_anagram('abc', 'ab'))
        self.assertFalse(practice.is_anagram('aab', 'abb'))

    @skip_if_unimplemented("build_sentence", ["a"])
    def test_12_build_sentence(self):
        self.assertEqual(practice.build_sentence(['big', 'o', 'notation']), 'big o notation')
        self.assertEqual(practice.build_sentence(['hello']), 'hello')
        self.assertEqual(practice.build_sentence([]), '')


if __name__ == "__main__":
    unittest.main(verbosity=2)
