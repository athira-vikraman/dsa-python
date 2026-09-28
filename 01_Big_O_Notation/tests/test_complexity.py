"""
EMPIRICAL COMPLEXITY TESTS — tests that check the GROWTH of a function,
not just its answer.

Idea: run the function at n and at 2n, and look at the ratio of the times.
    O(1)    -> ratio ~ 1
    O(n)    -> ratio ~ 2
    O(n^2)  -> ratio ~ 4

Timing tests are inherently noisy, so the bounds here are deliberately
generous and each measurement takes the BEST of several runs. If your
machine is busy, these can still wobble; skip them with:

    SKIP_TIMING_TESTS=1 python3 -m unittest discover -s tests

Run:  python3 -m unittest discover -s tests -v
"""

import os
import random
import time
import unittest

from dsa_import import load_code, load_exercise

quadratic = load_code("03_quadratic_time.py")
exponential = load_code("06_exponential_time.py")
sol = load_exercise("solutions.py")

SKIP_TIMING = os.environ.get("SKIP_TIMING_TESTS") == "1"
skip_if_asked = unittest.skipIf(SKIP_TIMING, "SKIP_TIMING_TESTS=1 was set")


def best_time(func, *args, repeats=5):
    """Best-of-N wall time. Best-of filters out interference from other
    processes far better than an average does."""
    best = float("inf")
    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        best = min(best, time.perf_counter() - start)
    return best


def growth_ratio(func, make_input, n, repeats=5):
    """Time at n and at 2n; return time(2n) / time(n)."""
    small = best_time(func, make_input(n), repeats=repeats)
    large = best_time(func, make_input(2 * n), repeats=repeats)
    if small <= 0:
        return float("inf")
    return large / small


@skip_if_asked
class TestGrowthRates(unittest.TestCase):

    def test_binary_search_is_logarithmic_not_linear(self):
        """O(log n): 100x the data must NOT cost anything like 100x the time."""
        small_data = list(range(100_000))
        large_data = list(range(10_000_000))

        def search(data):
            for _ in range(2000):
                sol.binary_search(data, len(data) - 1)

        small = best_time(search, small_data, repeats=3)
        large = best_time(search, large_data, repeats=3)
        ratio = large / small

        self.assertLess(ratio, 4.0,
                        f"100x more data multiplied the time by {ratio:.1f}x. "
                        "That is not logarithmic.")

    def test_set_membership_beats_list_membership(self):
        """O(1) vs O(n) - the single most important optimisation in Python."""
        n = 200_000
        data_list = list(range(n))
        data_set = set(data_list)
        targets = list(range(0, n, n // 200))

        list_time = best_time(lambda: sum(1 for t in targets if t in data_list),
                              repeats=3)
        set_time = best_time(lambda: sum(1 for t in targets if t in data_set),
                             repeats=3)

        self.assertGreater(list_time / set_time, 10,
                           "a set should be dramatically faster than a list here")

    def test_has_duplicates_is_not_quadratic(self):
        """The set-based solution must scale linearly, not quadratically."""
        def make_input(n):
            return list(range(n))            # no duplicates -> full scan

        ratio = growth_ratio(sol.has_duplicates, make_input, 200_000, repeats=3)
        self.assertLess(ratio, 3.5,
                        f"doubling n multiplied the time by {ratio:.1f}x; "
                        "O(n) should be about 2x. Are you using a set?")

    def test_nested_loop_really_is_quadratic(self):
        """A sanity check on the method itself: a known O(n^2) function
        must show a ratio near 4. If this fails, the machine is too noisy
        for timing tests and the others should be read with suspicion."""
        def make_input(n):
            return list(range(n))

        ratio = growth_ratio(quadratic.has_duplicate_slow, make_input, 1500, repeats=3)
        self.assertGreater(ratio, 2.5, f"expected ~4x, measured {ratio:.1f}x")
        self.assertLess(ratio, 8.0, f"expected ~4x, measured {ratio:.1f}x")

    def test_fibonacci_solution_is_linear_not_exponential(self):
        """fib(35) naively is ~30 million calls. The O(n) version is instant."""
        elapsed = best_time(sol.fibonacci, 35, repeats=3)
        self.assertLess(elapsed, 0.05,
                        f"fibonacci(35) took {elapsed:.4f}s - that looks exponential")

    def test_memoization_beats_naive_recursion(self):
        naive = best_time(exponential.fib_slow, 27, repeats=1)
        memo = best_time(exponential.fib_memo, 27, repeats=1)
        self.assertGreater(naive / memo, 10,
                           "memoization should be orders of magnitude faster")

    def test_merge_sorted_lists_beats_resorting(self):
        """O(n + m) merge vs O((n+m) log(n+m)) re-sort - correctness first."""
        a = sorted(random.randint(0, 10_000) for _ in range(5_000))
        b = sorted(random.randint(0, 10_000) for _ in range(5_000))
        self.assertEqual(sol.merge_sorted_lists(a, b), sorted(a + b))

    def test_append_is_amortized_constant(self):
        """n appends must total O(n): doubling n should roughly double the time."""
        def append_n(n):
            out = []
            for i in range(n):
                out.append(i)

        small = best_time(append_n, 400_000, repeats=3)
        large = best_time(append_n, 800_000, repeats=3)
        ratio = large / small
        self.assertLess(ratio, 3.5,
                        f"n appends should be O(n) in total; measured {ratio:.1f}x")


if __name__ == "__main__":
    unittest.main(verbosity=2)
