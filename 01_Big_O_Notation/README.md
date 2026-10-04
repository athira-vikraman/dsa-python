# Big O Notation — from beginner to confident

A complete, self-contained module: **notes to read**, **code to run**,
**exercises to solve**, and **tests that check your work**.

No third-party packages. Python 3.8+ and the standard library only.

> **Watch it run:** [`../visualizer.html`](../visualizer.html) is an interactive
> page with the growth curves, a side-by-side table of all nine sorts, eight
> "name the complexity" drills, and 31 animated problems. Open it in a browser
> alongside these notes.

---

## Start here

```bash
cd 17_DSA/01_Big_O_Notation

# 1. Read lesson 1
less notes/01_why_complexity_matters.md

# 2. Run the matching code and watch the theory happen
python3 code/01_constant_time.py

# 3. When you reach the exercises, check your work
python3 -m unittest discover -s tests -v
```

---

## The path (about 6–8 hours, spread over a few days)

| # | Read | Then run | You will be able to |
|---|------|----------|---------------------|
| 1 | [Why we measure code](notes/01_why_complexity_matters.md) | — | say why seconds are the wrong unit |
| 2 | [What Big O means](notes/02_what_is_big_o.md) | — | define O, Ω, Θ, and worst vs average case |
| 3 | [The rules](notes/03_rules_of_big_o.md) | — | reduce `4n² + 7n + 12` to `O(n²)` |
| 4 | [The complexity classes](notes/04_common_complexity_classes.md) | `code/01`–`code/06` | recognise each class on sight |
| 5a | [**Time vs space, gentle version**](notes/05a_time_vs_space_for_beginners.md) | `code/10_time_vs_space_simple.py` | explain the difference in your own words |
| 5 | [Space complexity](notes/05_space_complexity.md) | `code/07_space_complexity.py` | answer "…and the space complexity?" |
| 6 | [Recursion & amortized](notes/06_recursion_and_amortized.md) | `code/06_exponential_time.py` | analyse recursion; explain amortized O(1) |
| 7 | [Python operation costs](notes/07_python_operation_costs.md) | `code/08_python_builtin_costs.py` | stop writing accidental O(n²) |
| 8 | [How to analyse any code](notes/08_how_to_analyze_any_code.md) | `code/09_growth_experiment.py` | analyse unfamiliar code under pressure |
| 9 | [The cheat sheet](notes/09_cheatsheet.md) | — | revise the whole module in 5 minutes |
| + | *(bonus)* nine sorts as a Big O case study | `code/11_sorting_algorithms.py` | see O(n²), O(n log n) and O(n + k) race each other |

Then do the [exercises](exercises/exercises.md).

---

## What's in each folder

```
01_Big_O_Notation/
├── README.md                  <- you are here
├── notes/                     10 lessons, in reading order
├── code/                      11 runnable demonstrations
│   ├── 01_constant_time.py         O(1)
│   ├── 02_linear_time.py           O(n)
│   ├── 03_quadratic_time.py        O(n²) + how to fix it
│   ├── 04_logarithmic_time.py      O(log n), binary search
│   ├── 05_linearithmic_time.py     O(n log n), merge & quick sort
│   ├── 06_exponential_time.py      O(2ⁿ) + memoization escape
│   ├── 07_space_complexity.py      measured memory usage
│   ├── 08_python_builtin_costs.py  the 5 Python performance traps
│   ├── 09_growth_experiment.py     ASCII charts of every curve
│   ├── 10_time_vs_space_simple.py  time vs space, measured (beginner)
│   └── 11_sorting_algorithms.py   nine sorts, O(n^2) to O(n + k)
├── exercises/
│   ├── exercises.md           15 analysis drills + answer key
│   ├── practice.py            12 functions for YOU to write
│   └── solutions.py           model answers, with the reasoning
└── tests/
    ├── test_solutions.py      proves the model answers are correct
    ├── test_practice.py       grades YOUR work (skips what you haven't done)
    ├── test_code_examples.py  proves every lesson example works
    ├── test_sorting.py        nine sorts vs sorted(), on awkward inputs
    └── test_complexity.py     times functions to verify their GROWTH
```

Every code file runs on its own and prints an explained demonstration:

```bash
python3 code/03_quadratic_time.py
python3 code/09_growth_experiment.py     # the most fun one
```

---

## Running the tests

```bash
# everything
python3 -m unittest discover -s tests -v

# just your practice work
python3 -m unittest discover -s tests -p "test_practice.py" -v

# skip the timing-based tests (useful on a busy machine)
SKIP_TIMING_TESTS=1 python3 -m unittest discover -s tests

# or run every demo + the full suite in one go
python3 run_all.py
```

`tests/test_complexity.py` is unusual and worth reading: instead of checking
*what* a function returns, it times the function at `n` and at `2n` and
asserts on the **ratio**. A ratio near 2 means linear; near 4 means quadratic.
That is how you verify a complexity claim empirically.

---

## The 60-second version

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

1. **Drop constants**: `O(3n)` → `O(n)`
2. **Drop lower terms**: `O(n² + n)` → `O(n²)`
3. **Sequential adds, nested multiplies**
4. **Different inputs get different letters**: `O(a · b)`, not `O(n²)`

And the one habit worth more than all the theory: when you see a nested loop
searching for a value, reach for a **set or dict** — `O(n²)` becomes `O(n)`.

---

## Where to go next

Big O is the measuring tool. Now learn things worth measuring:

1. Arrays & strings (two pointers, sliding window)
2. Hash maps & sets
3. Stacks & queues
4. Linked lists
5. Recursion & backtracking
6. Trees & BSTs
7. Heaps
8. Graphs (BFS, DFS)
9. Sorting & searching in depth
10. Dynamic programming

Bring the cheat sheet to every one of them — state the time and space
complexity of every solution you write, out loud, every time. That habit is
what turns this module into a skill.
