"""
Tests for the lesson files in code/.

Every "slow" and "fast" pair must agree on the answer - an optimisation
that changes the answer is not an optimisation.

Run:  python3 -m unittest discover -s tests -v
"""

import random
import unittest

from dsa_import import load_code

arrays = load_code("01_array_basics.py")
strings = load_code("02_string_basics.py")
ends = load_code("03_two_pointers_ends.py")
rw = load_code("04_two_pointers_reader_writer.py")
fixed = load_code("05_sliding_window_fixed.py")
growing = load_code("06_sliding_window_growing.py")
choosing = load_code("07_choosing_the_technique.py")


class TestArrayBasics(unittest.TestCase):
    def test_get_box(self):
        self.assertEqual(arrays.get_box([7, 12, 3], 1), 12)
        self.assertEqual(arrays.get_box([7, 12, 3], -1), 3)

    def test_find_box_number(self):
        self.assertEqual(arrays.find_box_number([7, 12, 3], 3), 2)
        self.assertEqual(arrays.find_box_number([7, 12, 3], 99), -1)
        self.assertEqual(arrays.find_box_number([], 1), -1)

    def test_add_everything_up(self):
        self.assertEqual(arrays.add_everything_up([1, 2, 3]), 6)
        self.assertEqual(arrays.add_everything_up([]), 0)

    def test_add_at_end_and_front(self):
        self.assertEqual(arrays.add_at_end([1, 2], 3), [1, 2, 3])
        self.assertEqual(arrays.add_at_front([1, 2], 0), [0, 1, 2])

    def test_three_ways_to_walk_agree(self):
        items = ["a", "b", "c"]
        way1, way2, way3 = arrays.three_ways_to_walk(items)
        self.assertEqual(way1, items)
        self.assertEqual(way2, way3)


class TestStringBasics(unittest.TestCase):
    def test_get_letter(self):
        self.assertEqual(strings.get_letter("PYTHON", 0), "P")

    def test_count_letter(self):
        self.assertEqual(strings.count_letter("banana", "a"), 3)
        self.assertEqual(strings.count_letter("banana", "z"), 0)

    def test_strings_are_frozen(self):
        self.assertIn("TypeError", strings.try_to_change_a_string("cat"))

    def test_change_first_letter(self):
        self.assertEqual(strings.change_first_letter("cat", "b"), "bat")

    def test_list_way(self):
        self.assertEqual(strings.change_letter_the_list_way("hello", 0, "j"), "jello")

    def test_both_joins_agree(self):
        words = ["I", "love", "python"]
        self.assertEqual(strings.join_words_badly(words), strings.join_words_well(words))

    def test_join_handles_edges(self):
        self.assertEqual(strings.join_words_well([]), "")
        self.assertEqual(strings.join_words_well(["solo"]), "solo")


class TestTwoPointersEnds(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(ends.reverse_in_place([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(ends.reverse_in_place([]), [])

    def test_reverse_matches_slicing(self):
        for _ in range(20):
            data = [random.randint(0, 50) for _ in range(random.randint(0, 12))]
            self.assertEqual(ends.reverse_in_place(list(data)), data[::-1])

    def test_palindrome(self):
        for word in ("madam", "racecar", "", "a"):
            self.assertTrue(ends.is_palindrome(word), word)
        for word in ("hello", "ab"):
            self.assertFalse(ends.is_palindrome(word), word)

    def test_palindrome_ignoring_punctuation(self):
        self.assertTrue(ends.is_palindrome_ignoring_punctuation("A man, a plan, a canal: Panama"))
        self.assertTrue(ends.is_palindrome_ignoring_punctuation("race a car!") is False)
        self.assertTrue(ends.is_palindrome_ignoring_punctuation(".,"))

    def test_two_sum_versions_agree(self):
        for _ in range(40):
            numbers = sorted(random.sample(range(40), random.randint(0, 10)))
            target = random.randint(0, 50)
            fast = ends.two_sum_sorted(numbers, target)
            slow = ends.two_sum_brute_force(numbers, target)
            self.assertEqual(fast is None, slow is None, f"{numbers} {target}")
            if fast:
                self.assertEqual(sum(fast), target)

    def test_sorted_squares(self):
        self.assertEqual(ends.sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(ends.sorted_squares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

    def test_sorted_squares_matches_sorting(self):
        for _ in range(20):
            data = sorted(random.randint(-30, 30) for _ in range(random.randint(1, 12)))
            self.assertEqual(ends.sorted_squares(data), sorted(x * x for x in data))


class TestReaderWriter(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual(rw.move_zeros_to_end([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(rw.move_zeros_to_end([1, 0, 0]), [1, 0, 0])

    def test_move_zeros_keeps_the_same_numbers(self):
        for _ in range(30):
            data = [random.choice([0, 0, 1, 2, 3]) for _ in range(random.randint(0, 12))]
            result = rw.move_zeros_to_end(list(data))
            self.assertEqual(sorted(result), sorted(data))

    def test_remove_value(self):
        items = [3, 1, 3, 2, 3]
        count = rw.remove_value(items, 3)
        self.assertEqual(count, 2)
        self.assertEqual(items[:count], [1, 2])

    def test_remove_duplicates_sorted(self):
        items = [1, 1, 2, 2, 2, 3]
        count = rw.remove_duplicates_sorted(items)
        self.assertEqual(items[:count], [1, 2, 3])
        self.assertEqual(rw.remove_duplicates_sorted([]), 0)

    def test_keep_only_even(self):
        items = [1, 2, 3, 4, 5, 6]
        count = rw.keep_only_even(items)
        self.assertEqual(items[:count], [2, 4, 6])

    def test_merge_sorted(self):
        self.assertEqual(rw.merge_sorted([1, 3, 5], [2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(rw.merge_sorted([], [1]), [1])
        self.assertEqual(rw.merge_sorted([1], []), [1])
        self.assertEqual(rw.merge_sorted([], []), [])

    def test_merge_matches_sorted(self):
        for _ in range(30):
            a = sorted(random.randint(0, 30) for _ in range(random.randint(0, 8)))
            b = sorted(random.randint(0, 30) for _ in range(random.randint(0, 8)))
            self.assertEqual(rw.merge_sorted(a, b), sorted(a + b))


class TestFixedWindow(unittest.TestCase):
    def test_both_versions_agree(self):
        for _ in range(40):
            n = random.randint(1, 15)
            numbers = [random.randint(-20, 20) for _ in range(n)]
            k = random.randint(1, n)
            self.assertEqual(fixed.max_sum_of_k(numbers, k),
                             fixed.max_sum_of_k_slow(numbers, k),
                             f"{numbers} k={k}")

    def test_known_answers(self):
        self.assertEqual(fixed.max_sum_of_k([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(fixed.max_sum_of_k([1, 4, 2, 10, 2, 3, 1, 0, 20], 4), 24)

    def test_too_short(self):
        self.assertIsNone(fixed.max_sum_of_k([1, 2], 5))
        self.assertIsNone(fixed.max_sum_of_k_slow([1, 2], 5))

    def test_averages(self):
        self.assertEqual(fixed.averages_of_k([1, 3, 2, 6], 2), [2.0, 2.5, 4.0])
        self.assertEqual(fixed.averages_of_k([1], 5), [])

    def test_max_vowels(self):
        self.assertEqual(fixed.max_vowels_in_k("abciiidef", 3), 3)
        self.assertEqual(fixed.max_vowels_in_k("rhythms", 3), 0)
        self.assertEqual(fixed.max_vowels_in_k("ab", 5), 0)


class TestGrowingWindow(unittest.TestCase):
    def test_longest_without_repeats_agrees_with_brute_force(self):
        for _ in range(40):
            text = "".join(random.choice("abcd") for _ in range(random.randint(0, 14)))
            self.assertEqual(growing.longest_without_repeats(text),
                             growing.longest_without_repeats_slow(text), text)

    def test_longest_known(self):
        self.assertEqual(growing.longest_without_repeats("abcabcbb"), 3)
        self.assertEqual(growing.longest_without_repeats("bbbbb"), 1)
        self.assertEqual(growing.longest_without_repeats("pwwkew"), 3)
        self.assertEqual(growing.longest_without_repeats(""), 0)

    def test_shortest_subarray_agrees_with_brute_force(self):
        for _ in range(40):
            numbers = [random.randint(1, 10) for _ in range(random.randint(0, 14))]
            target = random.randint(1, 40)
            self.assertEqual(growing.shortest_subarray_with_sum(numbers, target),
                             growing.shortest_subarray_with_sum_slow(numbers, target),
                             f"{numbers} target={target}")

    def test_shortest_known(self):
        self.assertEqual(growing.shortest_subarray_with_sum([2, 1, 5, 2, 3, 2], 7), 2)
        self.assertEqual(growing.shortest_subarray_with_sum([1, 2], 100), 0)

    def test_at_most_k_distinct(self):
        self.assertEqual(growing.longest_with_at_most_k_distinct("araaci", 2), 4)
        self.assertEqual(growing.longest_with_at_most_k_distinct("araaci", 1), 2)
        self.assertEqual(growing.longest_with_at_most_k_distinct("cbbebi", 3), 5)
        self.assertEqual(growing.longest_with_at_most_k_distinct("", 2), 0)

    def test_at_most_k_distinct_brute_force(self):
        def brute(text, k):
            best = 0
            for i in range(len(text)):
                for j in range(i, len(text)):
                    if len(set(text[i:j + 1])) <= k:
                        best = max(best, j - i + 1)
            return best

        for _ in range(30):
            text = "".join(random.choice("abcd") for _ in range(random.randint(0, 12)))
            k = random.randint(1, 4)
            self.assertEqual(growing.longest_with_at_most_k_distinct(text, k),
                             brute(text, k), f"{text!r} k={k}")


class TestChoosingTheTechnique(unittest.TestCase):
    def test_pair_sum_versions_agree(self):
        for _ in range(30):
            numbers = random.sample(range(50), random.randint(0, 12))
            target = random.randint(0, 60)
            expected = choosing.pair_sum_nested_loops(numbers, target)
            self.assertEqual(choosing.pair_sum_with_set(numbers, target), expected)
            self.assertEqual(choosing.pair_sum_two_pointers(sorted(numbers), target),
                             expected)

    def test_window_versions_agree(self):
        for _ in range(20):
            n = random.randint(1, 15)
            numbers = [random.randint(0, 30) for _ in range(n)]
            k = random.randint(1, n)
            self.assertEqual(choosing.max_window_slicing(numbers, k),
                             choosing.max_window_sliding(numbers, k))

    def test_remove_zeros_versions_agree(self):
        for _ in range(20):
            data = [random.choice([0, 0, 1, 2]) for _ in range(random.randint(0, 12))]
            a = choosing.remove_zeros_badly(list(data))
            b = choosing.remove_zeros_with_new_list(list(data))
            c = choosing.remove_zeros_reader_writer(list(data))
            self.assertEqual(a, b)
            self.assertEqual(b, c)

    def test_palindrome_versions_agree(self):
        for _ in range(30):
            word = "".join(random.choice("ab") for _ in range(random.randint(0, 8)))
            self.assertEqual(choosing.palindrome_by_copying(word),
                             choosing.palindrome_two_pointers(word), word)


if __name__ == "__main__":
    unittest.main(verbosity=2)
