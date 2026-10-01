"""
Tests for exercises/solutions.py — the model answers.

These should all pass out of the box.

Run:  python3 -m unittest discover -s tests -v
"""

import random
import unittest

from dsa_import import load_exercise

sol = load_exercise("solutions.py")


class TestReverseInPlace(unittest.TestCase):
    def test_even_and_odd(self):
        self.assertEqual(sol.reverse_list_in_place([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(sol.reverse_list_in_place([1, 2, 3]), [3, 2, 1])

    def test_empty_and_single(self):
        self.assertEqual(sol.reverse_list_in_place([]), [])
        self.assertEqual(sol.reverse_list_in_place([9]), [9])

    def test_really_in_place(self):
        original = [1, 2, 3]
        returned = sol.reverse_list_in_place(original)
        self.assertIs(returned, original, "must mutate the caller's list")
        self.assertEqual(original, [3, 2, 1])


class TestIsPalindrome(unittest.TestCase):
    def test_true(self):
        for word in ("madam", "racecar", "level", "a", "", "abba"):
            self.assertTrue(sol.is_palindrome(word), word)

    def test_false(self):
        for word in ("hello", "ab", "abca"):
            self.assertFalse(sol.is_palindrome(word), word)

    def test_matches_slicing_version(self):
        for _ in range(50):
            word = "".join(random.choice("ab") for _ in range(random.randint(0, 8)))
            self.assertEqual(sol.is_palindrome(word), word == word[::-1], word)


class TestTwoSumSorted(unittest.TestCase):
    def test_found(self):
        self.assertEqual(sol.two_sum_sorted([1, 3, 5, 7], 10), (3, 7))
        self.assertEqual(sol.two_sum_sorted([1, 2], 3), (1, 2))

    def test_not_found(self):
        self.assertIsNone(sol.two_sum_sorted([1, 3, 5], 100))
        self.assertIsNone(sol.two_sum_sorted([], 5))
        self.assertIsNone(sol.two_sum_sorted([5], 5))

    def test_negatives(self):
        self.assertEqual(sol.two_sum_sorted([-5, -2, 0, 3], -2), (-5, 3))

    def test_does_not_reuse_one_element(self):
        self.assertIsNone(sol.two_sum_sorted([1, 2, 3], 6),
                          "3+3 needs two 3s; one must not pair with itself")

    def test_matches_brute_force(self):
        for _ in range(40):
            numbers = sorted(random.sample(range(50), random.randint(0, 10)))
            target = random.randint(0, 60)
            expected = any(numbers[i] + numbers[j] == target
                           for i in range(len(numbers))
                           for j in range(i + 1, len(numbers)))
            got = sol.two_sum_sorted(numbers, target)
            self.assertEqual(got is not None, expected, f"{numbers} target {target}")
            if got:
                self.assertEqual(got[0] + got[1], target)


class TestMoveZeros(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sol.move_zeros_to_end([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_edges(self):
        self.assertEqual(sol.move_zeros_to_end([]), [])
        self.assertEqual(sol.move_zeros_to_end([0]), [0])
        self.assertEqual(sol.move_zeros_to_end([0, 0, 0]), [0, 0, 0])
        self.assertEqual(sol.move_zeros_to_end([1, 2, 3]), [1, 2, 3])

    def test_keeps_order_of_non_zeros(self):
        self.assertEqual(sol.move_zeros_to_end([0, 5, 0, 1, 0, 9]), [5, 1, 9, 0, 0, 0])

    def test_in_place(self):
        original = [0, 1, 2]
        returned = sol.move_zeros_to_end(original)
        self.assertIs(returned, original)

    def test_same_multiset(self):
        for _ in range(30):
            data = [random.choice([0, 0, 1, 2, 3]) for _ in range(random.randint(0, 12))]
            result = sol.move_zeros_to_end(list(data))
            self.assertEqual(sorted(result), sorted(data))


class TestRemoveAll(unittest.TestCase):
    def test_count_and_contents(self):
        items = [3, 1, 3, 2]
        count = sol.remove_all(items, 3)
        self.assertEqual(count, 2)
        self.assertEqual(items[:count], [1, 2])

    def test_remove_everything(self):
        items = [7, 7, 7]
        self.assertEqual(sol.remove_all(items, 7), 0)

    def test_remove_nothing(self):
        items = [1, 2, 3]
        count = sol.remove_all(items, 9)
        self.assertEqual(count, 3)
        self.assertEqual(items[:count], [1, 2, 3])

    def test_empty(self):
        self.assertEqual(sol.remove_all([], 1), 0)


class TestRemoveDuplicatesSorted(unittest.TestCase):
    def test_typical(self):
        items = [1, 1, 2, 2, 3]
        count = sol.remove_duplicates_sorted(items)
        self.assertEqual(count, 3)
        self.assertEqual(items[:count], [1, 2, 3])

    def test_all_same(self):
        items = [5, 5, 5, 5]
        count = sol.remove_duplicates_sorted(items)
        self.assertEqual(count, 1)
        self.assertEqual(items[:count], [5])

    def test_no_duplicates(self):
        items = [1, 2, 3]
        self.assertEqual(sol.remove_duplicates_sorted(items), 3)

    def test_empty_and_single(self):
        self.assertEqual(sol.remove_duplicates_sorted([]), 0)
        self.assertEqual(sol.remove_duplicates_sorted([1]), 1)

    def test_matches_sorted_set(self):
        for _ in range(30):
            data = sorted(random.choice([1, 1, 2, 3, 3, 4]) for _ in range(random.randint(0, 12)))
            items = list(data)
            count = sol.remove_duplicates_sorted(items)
            self.assertEqual(items[:count], sorted(set(data)))


class TestMaxSumOfK(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sol.max_sum_of_k([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(sol.max_sum_of_k([1, 4, 2, 10, 2, 3, 1, 0, 20], 4), 24)

    def test_k_equals_length(self):
        self.assertEqual(sol.max_sum_of_k([1, 2, 3], 3), 6)

    def test_k_of_one(self):
        self.assertEqual(sol.max_sum_of_k([4, 9, 2], 1), 9)

    def test_too_short(self):
        self.assertIsNone(sol.max_sum_of_k([1, 2], 5))
        self.assertIsNone(sol.max_sum_of_k([], 1))

    def test_negatives(self):
        self.assertEqual(sol.max_sum_of_k([-5, -1, -3], 2), -4)

    def test_matches_brute_force(self):
        for _ in range(40):
            n = random.randint(1, 15)
            numbers = [random.randint(-20, 20) for _ in range(n)]
            k = random.randint(1, n)
            expected = max(sum(numbers[i:i + k]) for i in range(n - k + 1))
            self.assertEqual(sol.max_sum_of_k(numbers, k), expected,
                             f"{numbers} k={k}")


class TestAveragesOfK(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sol.averages_of_k([1, 3, 2, 6], 2), [2.0, 2.5, 4.0])

    def test_too_short(self):
        self.assertEqual(sol.averages_of_k([1], 5), [])

    def test_matches_brute_force(self):
        for _ in range(30):
            n = random.randint(1, 12)
            numbers = [random.randint(0, 50) for _ in range(n)]
            k = random.randint(1, n)
            expected = [sum(numbers[i:i + k]) / k for i in range(n - k + 1)]
            got = sol.averages_of_k(numbers, k)
            self.assertEqual(len(got), len(expected))
            for a, b in zip(got, expected):
                self.assertAlmostEqual(a, b)


class TestLongestWithoutRepeats(unittest.TestCase):
    def test_known(self):
        self.assertEqual(sol.longest_without_repeats("abcabcbb"), 3)
        self.assertEqual(sol.longest_without_repeats("bbbbb"), 1)
        self.assertEqual(sol.longest_without_repeats("pwwkew"), 3)
        self.assertEqual(sol.longest_without_repeats("abba"), 2)

    def test_empty_and_single(self):
        self.assertEqual(sol.longest_without_repeats(""), 0)
        self.assertEqual(sol.longest_without_repeats("a"), 1)

    def test_all_unique(self):
        self.assertEqual(sol.longest_without_repeats("abcdef"), 6)

    def test_matches_brute_force(self):
        def brute(text):
            best = 0
            for i in range(len(text)):
                seen = set()
                for j in range(i, len(text)):
                    if text[j] in seen:
                        break
                    seen.add(text[j])
                    best = max(best, j - i + 1)
            return best

        for _ in range(40):
            text = "".join(random.choice("abcd") for _ in range(random.randint(0, 14)))
            self.assertEqual(sol.longest_without_repeats(text), brute(text), text)


class TestShortestSubarrayWithSum(unittest.TestCase):
    def test_known(self):
        self.assertEqual(sol.shortest_subarray_with_sum([2, 1, 5, 2, 3, 2], 7), 2)
        self.assertEqual(sol.shortest_subarray_with_sum([2, 1, 5, 2, 8], 7), 1)
        self.assertEqual(sol.shortest_subarray_with_sum([3, 4, 1, 1, 6], 8), 3)

    def test_impossible(self):
        self.assertEqual(sol.shortest_subarray_with_sum([1, 2], 100), 0)
        self.assertEqual(sol.shortest_subarray_with_sum([], 5), 0)

    def test_whole_array_needed(self):
        self.assertEqual(sol.shortest_subarray_with_sum([1, 1, 1], 3), 3)

    def test_matches_brute_force(self):
        def brute(numbers, target):
            best = float("inf")
            for i in range(len(numbers)):
                total = 0
                for j in range(i, len(numbers)):
                    total += numbers[j]
                    if total >= target:
                        best = min(best, j - i + 1)
                        break
            return 0 if best == float("inf") else best

        for _ in range(40):
            numbers = [random.randint(1, 10) for _ in range(random.randint(0, 14))]
            target = random.randint(1, 40)
            self.assertEqual(sol.shortest_subarray_with_sum(numbers, target),
                             brute(numbers, target), f"{numbers} target {target}")


class TestReverseWords(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sol.reverse_words("the sky is blue"), "blue is sky the")

    def test_extra_spaces(self):
        self.assertEqual(sol.reverse_words("  the sky  is blue "), "blue is sky the")

    def test_single_word(self):
        self.assertEqual(sol.reverse_words("hello"), "hello")

    def test_empty_and_spaces_only(self):
        self.assertEqual(sol.reverse_words(""), "")
        self.assertEqual(sol.reverse_words("     "), "")


class TestIsAnagram(unittest.TestCase):
    def test_true(self):
        self.assertTrue(sol.is_anagram("listen", "silent"))
        self.assertTrue(sol.is_anagram("", ""))
        self.assertTrue(sol.is_anagram("aabb", "bbaa"))

    def test_false(self):
        self.assertFalse(sol.is_anagram("hello", "world"))
        self.assertFalse(sol.is_anagram("abc", "ab"))
        self.assertFalse(sol.is_anagram("aab", "abb"))

    def test_matches_sorting(self):
        for _ in range(40):
            a = "".join(random.choice("abc") for _ in range(random.randint(0, 6)))
            b = "".join(random.choice("abc") for _ in range(random.randint(0, 6)))
            self.assertEqual(sol.is_anagram(a, b), sorted(a) == sorted(b), f"{a} {b}")


class TestFirstUniqueChar(unittest.TestCase):
    def test_known(self):
        self.assertEqual(sol.first_unique_char("leetcode"), 0)
        self.assertEqual(sol.first_unique_char("loveleetcode"), 2)
        self.assertEqual(sol.first_unique_char("aabb"), -1)

    def test_empty_and_single(self):
        self.assertEqual(sol.first_unique_char(""), -1)
        self.assertEqual(sol.first_unique_char("z"), 0)

    def test_matches_brute_force(self):
        for _ in range(40):
            text = "".join(random.choice("abc") for _ in range(random.randint(0, 10)))
            expected = -1
            for i, c in enumerate(text):
                if text.count(c) == 1:
                    expected = i
                    break
            self.assertEqual(sol.first_unique_char(text), expected, text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
