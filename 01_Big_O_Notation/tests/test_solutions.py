"""
Tests for exercises/solutions.py — the model answers.

These should ALL pass out of the box. If one fails, something is broken
in the repository, not in your work.

Run:  python3 -m unittest discover -s tests -v
"""

import unittest

from dsa_import import load_exercise

sol = load_exercise("solutions.py")


class TestGetFirstAndLast(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(sol.get_first_and_last([1, 2, 3, 4]), (1, 4))

    def test_single_element(self):
        self.assertEqual(sol.get_first_and_last([7]), (7, 7))

    def test_empty(self):
        self.assertEqual(sol.get_first_and_last([]), (None, None))


class TestCountOccurrences(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(sol.count_occurrences([1, 2, 2, 3, 2], 2), 3)

    def test_absent(self):
        self.assertEqual(sol.count_occurrences([1, 2, 3], 9), 0)

    def test_empty(self):
        self.assertEqual(sol.count_occurrences([], 1), 0)

    def test_strings(self):
        self.assertEqual(sol.count_occurrences(["a", "b", "a"], "a"), 2)


class TestHasDuplicates(unittest.TestCase):
    def test_with_duplicates(self):
        self.assertTrue(sol.has_duplicates([1, 2, 3, 2]))

    def test_without_duplicates(self):
        self.assertFalse(sol.has_duplicates([1, 2, 3, 4]))

    def test_empty(self):
        self.assertFalse(sol.has_duplicates([]))

    def test_all_same(self):
        self.assertTrue(sol.has_duplicates([5, 5, 5]))


class TestFindPairWithSum(unittest.TestCase):
    def test_found(self):
        self.assertEqual(sol.find_pair_with_sum([2, 7, 11, 15], 9), (2, 7))

    def test_not_found(self):
        self.assertIsNone(sol.find_pair_with_sum([1, 2, 3], 100))

    def test_negative_numbers(self):
        result = sol.find_pair_with_sum([-3, 4, 1, 90], 1)
        self.assertEqual(sorted(result), [-3, 4])

    def test_does_not_reuse_one_element(self):
        # 5 + 5 needs TWO fives; a single 5 must not pair with itself
        self.assertIsNone(sol.find_pair_with_sum([5, 1, 2], 10))
        self.assertIsNotNone(sol.find_pair_with_sum([5, 1, 5], 10))

    def test_empty(self):
        self.assertIsNone(sol.find_pair_with_sum([], 5))


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 3, 5, 7, 9, 11, 13]

    def test_finds_every_element(self):
        for index, value in enumerate(self.data):
            self.assertEqual(sol.binary_search(self.data, value), index)

    def test_first_and_last(self):
        self.assertEqual(sol.binary_search(self.data, 1), 0)
        self.assertEqual(sol.binary_search(self.data, 13), 6)

    def test_missing(self):
        self.assertEqual(sol.binary_search(self.data, 4), -1)
        self.assertEqual(sol.binary_search(self.data, 100), -1)
        self.assertEqual(sol.binary_search(self.data, -5), -1)

    def test_empty(self):
        self.assertEqual(sol.binary_search([], 1), -1)

    def test_large_sorted_range(self):
        big = list(range(100_000))
        self.assertEqual(sol.binary_search(big, 99_999), 99_999)
        self.assertEqual(sol.binary_search(big, 0), 0)


class TestReverseInPlace(unittest.TestCase):
    def test_even_length(self):
        self.assertEqual(sol.reverse_in_place([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_odd_length(self):
        self.assertEqual(sol.reverse_in_place([1, 2, 3]), [3, 2, 1])

    def test_empty_and_single(self):
        self.assertEqual(sol.reverse_in_place([]), [])
        self.assertEqual(sol.reverse_in_place([9]), [9])

    def test_actually_in_place(self):
        """The caller's own list object must be mutated - that is the point."""
        original = [1, 2, 3]
        returned = sol.reverse_in_place(original)
        self.assertIs(returned, original)          # same object, not a copy
        self.assertEqual(original, [3, 2, 1])      # mutated


class TestFirstNonRepeating(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sol.first_non_repeating(['a', 'b', 'a', 'c', 'b']), 'c')

    def test_first_element(self):
        self.assertEqual(sol.first_non_repeating([1, 2, 2, 3, 3]), 1)

    def test_all_repeating(self):
        self.assertIsNone(sol.first_non_repeating([1, 1, 2, 2]))

    def test_empty(self):
        self.assertIsNone(sol.first_non_repeating([]))


class TestFibonacci(unittest.TestCase):
    def test_known_values(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for n, value in enumerate(expected):
            self.assertEqual(sol.fibonacci(n), value, f"fibonacci({n})")

    def test_large_input_is_fast(self):
        """An O(2^n) solution would never finish this."""
        self.assertEqual(len(str(sol.fibonacci(1000))), 209)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            sol.fibonacci(-1)


class TestMergeSortedLists(unittest.TestCase):
    def test_interleaved(self):
        self.assertEqual(sol.merge_sorted_lists([1, 3, 5], [2, 4, 6]),
                         [1, 2, 3, 4, 5, 6])

    def test_one_empty(self):
        self.assertEqual(sol.merge_sorted_lists([], [1, 2]), [1, 2])
        self.assertEqual(sol.merge_sorted_lists([1, 2], []), [1, 2])
        self.assertEqual(sol.merge_sorted_lists([], []), [])

    def test_different_lengths(self):
        self.assertEqual(sol.merge_sorted_lists([1], [2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_kept(self):
        self.assertEqual(sol.merge_sorted_lists([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])

    def test_matches_sorted(self):
        import random
        a = sorted(random.randint(0, 50) for _ in range(30))
        b = sorted(random.randint(0, 50) for _ in range(20))
        self.assertEqual(sol.merge_sorted_lists(a, b), sorted(a + b))


class TestMostFrequent(unittest.TestCase):
    def test_clear_winner(self):
        self.assertEqual(sol.most_frequent([1, 2, 2, 3, 3, 3]), 3)

    def test_single(self):
        self.assertEqual(sol.most_frequent([7]), 7)

    def test_empty(self):
        self.assertIsNone(sol.most_frequent([]))

    def test_tie_goes_to_the_first_to_reach_the_count(self):
        self.assertEqual(sol.most_frequent(['a', 'b', 'a', 'b']), 'a')

    def test_strings(self):
        self.assertEqual(sol.most_frequent(['x', 'y', 'y']), 'y')


class TestIsAnagram(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(sol.is_anagram('listen', 'silent'))
        self.assertTrue(sol.is_anagram('', ''))
        self.assertTrue(sol.is_anagram('aabb', 'bbaa'))

    def test_false_cases(self):
        self.assertFalse(sol.is_anagram('hello', 'world'))
        self.assertFalse(sol.is_anagram('abc', 'ab'))       # different lengths
        self.assertFalse(sol.is_anagram('aab', 'abb'))      # same letters, wrong counts


class TestBuildSentence(unittest.TestCase):
    def test_joins_with_spaces(self):
        self.assertEqual(sol.build_sentence(['big', 'o', 'notation']), 'big o notation')

    def test_single_word(self):
        self.assertEqual(sol.build_sentence(['hello']), 'hello')

    def test_empty(self):
        self.assertEqual(sol.build_sentence([]), '')


if __name__ == "__main__":
    unittest.main(verbosity=2)
