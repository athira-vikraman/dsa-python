"""
Tests for code/11_sorting_algorithms.py — the nine sorts.

Every sort must agree with Python's own sorted() on the same input. That is
the only thing a sort has to get right, so it is the only thing we assert -
on a lot of inputs, including the awkward ones.

Run:  python3 -m unittest discover -s tests -v
"""

import random
import unittest

from dsa_import import load_code

sorts = load_code("11_sorting_algorithms.py")

# (name, function, does it only take non-negative whole numbers?)
COMPARISON_SORTS = [
    ("bubble_sort", sorts.bubble_sort),
    ("selection_sort", sorts.selection_sort),
    ("insertion_sort", sorts.insertion_sort),
    ("merge_sort", sorts.merge_sort),
    ("quick_sort", sorts.quick_sort),
    ("heap_sort", sorts.heap_sort),
]
COUNTING_SORTS = [
    ("counting_sort", sorts.counting_sort),
    ("radix_sort", sorts.radix_sort),
    ("bucket_sort", sorts.bucket_sort),
]
ALL_SORTS = COMPARISON_SORTS + COUNTING_SORTS

# The inputs that break naive implementations.
AWKWARD = [
    [],                         # empty
    [1],                        # single
    [2, 1],                     # one swap
    [1, 2, 3, 4, 5],            # already sorted
    [5, 4, 3, 2, 1],            # exactly backwards
    [7, 7, 7, 7],               # all the same
    [3, 1, 3, 1, 3],            # lots of duplicates
    [0, 0, 1, 0],               # zeros
    [9, 1, 8, 2, 7, 3, 6, 4],   # interleaved
]


class TestEveryS0rtAgreesWithSorted(unittest.TestCase):
    """The headline test: nine sorts, one correct answer."""

    def test_awkward_inputs(self):
        for name, func in ALL_SORTS:
            for data in AWKWARD:
                with self.subTest(sort=name, data=data):
                    self.assertEqual(func(data), sorted(data))

    def test_random_inputs(self):
        random.seed(7)
        for name, func in ALL_SORTS:
            for _ in range(25):
                data = [random.randint(0, 40) for _ in range(random.randint(0, 30))]
                with self.subTest(sort=name):
                    self.assertEqual(func(data), sorted(data))

    def test_negative_numbers_in_comparison_sorts(self):
        """Only the comparison sorts can handle negatives - that's the trade."""
        random.seed(11)
        for name, func in COMPARISON_SORTS:
            for _ in range(15):
                data = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
                with self.subTest(sort=name):
                    self.assertEqual(func(data), sorted(data))

    def test_larger_input(self):
        random.seed(3)
        data = [random.randint(0, 500) for _ in range(400)]
        expected = sorted(data)
        for name, func in ALL_SORTS:
            with self.subTest(sort=name):
                self.assertEqual(func(data), expected)


class TestSortsDoNotMutateTheInput(unittest.TestCase):
    """Each one returns a new list and leaves the caller's list alone."""

    def test_input_unchanged(self):
        for name, func in ALL_SORTS:
            with self.subTest(sort=name):
                data = [5, 2, 9, 1]
                func(data)
                self.assertEqual(data, [5, 2, 9, 1],
                                 f"{name} modified the list it was given")


class TestMergeHelper(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(sorts.merge([1, 3, 5], [2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sorts.merge([], [1]), [1])
        self.assertEqual(sorts.merge([1], []), [1])
        self.assertEqual(sorts.merge([], []), [])

    def test_merge_is_stable_on_equal_values(self):
        self.assertEqual(sorts.merge([1, 2], [2, 3]), [1, 2, 2, 3])


class TestHeapHelper(unittest.TestCase):
    def test_sift_down_puts_the_biggest_on_top(self):
        items = [1, 9, 5]
        sorts.sift_down(items, 0, len(items))
        self.assertEqual(items[0], 9, "the biggest of the three must end up on top")

    def test_sift_down_leaves_a_valid_heap_alone(self):
        items = [9, 5, 1]
        sorts.sift_down(items, 0, len(items))
        self.assertEqual(items, [9, 5, 1])


class TestCountingSortRange(unittest.TestCase):
    def test_handles_zero(self):
        self.assertEqual(sorts.counting_sort([0, 0, 0]), [0, 0, 0])

    def test_handles_a_gap_in_the_values(self):
        """Values 0..9 with most counters empty - the gaps must be skipped."""
        self.assertEqual(sorts.counting_sort([9, 0, 9]), [0, 9, 9])


class TestRadixSortDigits(unittest.TestCase):
    def test_mixed_digit_lengths(self):
        self.assertEqual(sorts.radix_sort([170, 45, 75, 90, 24, 2, 66]),
                         [2, 24, 45, 66, 75, 90, 170])

    def test_same_digits_different_order(self):
        self.assertEqual(sorts.radix_sort([321, 213, 132]), [132, 213, 321])

    def test_single_digits(self):
        self.assertEqual(sorts.radix_sort([5, 3, 9, 1]), [1, 3, 5, 9])


class TestBucketSortSpread(unittest.TestCase):
    def test_everything_in_one_bucket(self):
        """The worst case still has to produce the right answer."""
        self.assertEqual(sorts.bucket_sort([10, 10, 10, 10]), [10, 10, 10, 10])

    def test_values_landing_in_every_bucket(self):
        data = [0, 9, 19, 29, 39, 49]
        self.assertEqual(sorts.bucket_sort(data), sorted(data))


class TestComplexityShapes(unittest.TestCase):
    """Timing checks: the quadratic sorts must actually behave quadratically,
    and the n log n ones must not."""

    def _ratio(self, func, n):
        import time

        def best(size):
            data = [random.randint(0, 1000) for _ in range(size)]
            quickest = float("inf")
            for _ in range(3):
                start = time.perf_counter()
                func(data)
                quickest = min(quickest, time.perf_counter() - start)
            return quickest

        random.seed(5)
        return best(2 * n) / best(n)

    def test_insertion_sort_is_quadratic(self):
        ratio = self._ratio(sorts.insertion_sort, 700)
        self.assertGreater(ratio, 2.5, f"expected about 4x, measured {ratio:.1f}x")

    def test_merge_sort_is_not_quadratic(self):
        ratio = self._ratio(sorts.merge_sort, 2000)
        self.assertLess(ratio, 3.0, f"expected about 2x, measured {ratio:.1f}x")

    def test_counting_sort_is_linear(self):
        ratio = self._ratio(sorts.counting_sort, 20000)
        self.assertLess(ratio, 3.0, f"expected about 2x, measured {ratio:.1f}x")


if __name__ == "__main__":
    unittest.main(verbosity=2)
