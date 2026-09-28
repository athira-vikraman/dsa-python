"""
Tests for the lesson files in code/.

They prove that every example you are learning from actually works -
the "slow" and "fast" versions of each algorithm must agree on the answer.
An optimisation that changes the answer is not an optimisation.

Run:  python3 -m unittest discover -s tests -v
"""

import random
import unittest

from dsa_import import load_code

constant = load_code("01_constant_time.py")
linear = load_code("02_linear_time.py")
quadratic = load_code("03_quadratic_time.py")
logarithmic = load_code("04_logarithmic_time.py")
linearithmic = load_code("05_linearithmic_time.py")
exponential = load_code("06_exponential_time.py")
space = load_code("07_space_complexity.py")


class TestConstantTime(unittest.TestCase):
    def test_first_element(self):
        self.assertEqual(constant.first_element([10, 20, 30]), 10)
        self.assertIsNone(constant.first_element([]))

    def test_is_even(self):
        self.assertTrue(constant.is_even(4))
        self.assertFalse(constant.is_even(7))

    def test_get_price(self):
        prices = {"pen": 10}
        self.assertEqual(constant.get_price(prices, "pen"), 10)
        self.assertEqual(constant.get_price(prices, "missing"), 0)

    def test_summary_shape(self):
        self.assertEqual(len(constant.summary([1, 2, 3])), 5)


class TestLinearTime(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(linear.find_max([3, 9, 2]), 9)
        self.assertEqual(linear.find_max([-5, -1, -9]), -1)
        self.assertIsNone(linear.find_max([]))

    def test_find_max_matches_builtin(self):
        data = [random.randint(-1000, 1000) for _ in range(200)]
        self.assertEqual(linear.find_max(data), max(data))

    def test_linear_search(self):
        self.assertEqual(linear.linear_search([5, 6, 7], 7), 2)
        self.assertEqual(linear.linear_search([5, 6, 7], 99), -1)

    def test_sum_and_product(self):
        self.assertEqual(linear.sum_and_product([1, 2, 3, 4]), (10, 24))

    def test_doubled(self):
        self.assertEqual(linear.doubled([1, 2, 3]), [2, 4, 6])

    def test_first_three(self):
        self.assertEqual(linear.first_three([1, 2, 3, 4, 5]), [1, 2, 3])
        self.assertEqual(linear.first_three([1]), [1])


class TestQuadraticTime(unittest.TestCase):
    def test_all_pairs_count(self):
        self.assertEqual(len(quadratic.all_pairs([1, 2, 3])), 9)      # n^2

    def test_unique_pairs_count(self):
        self.assertEqual(len(quadratic.unique_pairs([1, 2, 3, 4])), 6)  # n(n-1)/2

    def test_slow_and_fast_duplicate_checks_agree(self):
        """The whole point of the optimisation: SAME answer, less time."""
        for _ in range(30):
            data = [random.randint(0, 12) for _ in range(random.randint(0, 20))]
            self.assertEqual(quadratic.has_duplicate_slow(data),
                             quadratic.has_duplicate_fast(data),
                             f"disagreed on {data}")

    def test_remove_duplicates_versions_agree(self):
        for _ in range(30):
            data = [random.randint(0, 10) for _ in range(random.randint(0, 25))]
            self.assertEqual(quadratic.remove_duplicates_slow(data),
                             quadratic.remove_duplicates_fast(data))

    def test_remove_duplicates_preserves_order(self):
        self.assertEqual(quadratic.remove_duplicates_fast([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_bubble_sort(self):
        for _ in range(20):
            data = [random.randint(0, 100) for _ in range(random.randint(0, 30))]
            self.assertEqual(quadratic.bubble_sort(data), sorted(data))

    def test_bubble_sort_does_not_mutate_input(self):
        data = [3, 1, 2]
        quadratic.bubble_sort(data)
        self.assertEqual(data, [3, 1, 2])

    def test_common_items_versions_agree(self):
        a = [1, 2, 3, 4, 5]
        b = [4, 5, 6]
        self.assertEqual(quadratic.common_items_slow(a, b),
                         quadratic.common_items_fast(a, b))


class TestLogarithmicTime(unittest.TestCase):
    def test_binary_search_finds_everything(self):
        data = list(range(0, 200, 2))
        for index, value in enumerate(data):
            self.assertEqual(logarithmic.binary_search(data, value), index)

    def test_binary_search_missing(self):
        data = list(range(0, 200, 2))
        self.assertEqual(logarithmic.binary_search(data, 7), -1)
        self.assertEqual(logarithmic.binary_search([], 1), -1)

    def test_recursive_matches_iterative(self):
        data = sorted(random.sample(range(1000), 100))
        for value in data:
            self.assertEqual(logarithmic.binary_search(data, value),
                             logarithmic.binary_search_recursive(data, value))

    def test_count_halvings(self):
        self.assertEqual(logarithmic.count_halvings(1), 0)
        self.assertEqual(logarithmic.count_halvings(8), 3)
        self.assertEqual(logarithmic.count_halvings(1024), 10)

    def test_doubling_loop(self):
        self.assertEqual(logarithmic.doubling_loop(20), [1, 2, 4, 8, 16])

    def test_count_digits(self):
        self.assertEqual(logarithmic.count_digits(0), 1)
        self.assertEqual(logarithmic.count_digits(7), 1)
        self.assertEqual(logarithmic.count_digits(12345), 5)
        self.assertEqual(logarithmic.count_digits(-99), 2)


class TestLinearithmicTime(unittest.TestCase):
    def test_merge_sort(self):
        for _ in range(20):
            data = [random.randint(0, 500) for _ in range(random.randint(0, 60))]
            self.assertEqual(linearithmic.merge_sort(data), sorted(data))

    def test_quick_sort(self):
        for _ in range(20):
            data = [random.randint(0, 500) for _ in range(random.randint(0, 60))]
            self.assertEqual(linearithmic.quick_sort(data), sorted(data))

    def test_sorts_handle_already_sorted_and_reversed(self):
        ordered = list(range(50))
        backwards = list(reversed(ordered))
        self.assertEqual(linearithmic.merge_sort(ordered), ordered)
        self.assertEqual(linearithmic.merge_sort(backwards), ordered)
        self.assertEqual(linearithmic.quick_sort(backwards), ordered)

    def test_merge_sort_does_not_mutate_input(self):
        data = [3, 1, 2]
        linearithmic.merge_sort(data)
        self.assertEqual(data, [3, 1, 2])

    def test_has_duplicate_by_sorting(self):
        self.assertTrue(linearithmic.has_duplicate_by_sorting([1, 2, 3, 2]))
        self.assertFalse(linearithmic.has_duplicate_by_sorting([1, 2, 3]))
        self.assertFalse(linearithmic.has_duplicate_by_sorting([]))

    def test_closest_pair_difference(self):
        self.assertEqual(linearithmic.closest_pair_difference([10, 3, 7, 1]), 2)
        self.assertEqual(linearithmic.closest_pair_difference([5, 5]), 0)
        self.assertIsNone(linearithmic.closest_pair_difference([1]))


class TestExponentialTime(unittest.TestCase):
    def test_all_fib_versions_agree(self):
        for n in range(0, 20):
            value = exponential.fib_slow(n)
            self.assertEqual(value, exponential.fib_memo(n), f"fib_memo({n})")
            self.assertEqual(value, exponential.fib_cached(n), f"fib_cached({n})")
            self.assertEqual(value, exponential.fib_iterative(n), f"fib_iterative({n})")

    def test_fib_known_values(self):
        self.assertEqual(exponential.fib_iterative(10), 55)
        self.assertEqual(exponential.fib_iterative(50), 12586269025)

    def test_memoized_handles_large_n_quickly(self):
        """O(2^n) could never do this; O(n) does it instantly."""
        self.assertEqual(len(str(exponential.fib_memo(300))), 63)

    def test_all_subsets_count(self):
        for n in range(0, 8):
            self.assertEqual(len(exponential.all_subsets(list(range(n)))), 2 ** n)

    def test_all_subsets_contents(self):
        result = exponential.all_subsets([1, 2])
        self.assertEqual(sorted(result), [[], [1], [1, 2], [2]])

    def test_all_permutations_count(self):
        import math
        for n in range(1, 7):
            self.assertEqual(len(exponential.all_permutations(list(range(n)))),
                             math.factorial(n))

    def test_all_permutations_are_distinct(self):
        perms = exponential.all_permutations([1, 2, 3, 4])
        self.assertEqual(len({tuple(p) for p in perms}), 24)


class TestSpaceComplexity(unittest.TestCase):
    def test_total(self):
        self.assertEqual(space.total_o1_space([1, 2, 3]), 6)
        self.assertEqual(space.total_o1_space([]), 0)

    def test_reverse_in_place_mutates(self):
        data = [1, 2, 3]
        result = space.reverse_in_place(data)
        self.assertIs(result, data)
        self.assertEqual(data, [3, 2, 1])

    def test_reverse_copy_does_not_mutate(self):
        data = [1, 2, 3]
        result = space.reverse_copy(data)
        self.assertEqual(result, [3, 2, 1])
        self.assertEqual(data, [1, 2, 3])
        self.assertIsNot(result, data)

    def test_count_frequencies(self):
        self.assertEqual(space.count_frequencies(['a', 'b', 'a']), {'a': 2, 'b': 1})

    def test_countdown_versions_agree(self):
        for n in (0, 1, 10, 500):
            self.assertEqual(space.countdown_recursive(n), space.countdown_iterative(n))

    def test_duplicate_versions_agree(self):
        for _ in range(20):
            data = [random.randint(0, 8) for _ in range(random.randint(0, 15))]
            self.assertEqual(space.has_duplicate_low_space(data),
                             space.has_duplicate_low_time(data))


if __name__ == "__main__":
    unittest.main(verbosity=2)
