# Lesson 4 — The Common Complexity Classes

> **Goal:** recognise each growth class on sight, and know one real algorithm
> from each.

Every runnable example here lives in the `code/` folder — read the note, then
run the file.

---

## O(1) — Constant time

**Work does not depend on input size at all.** A list of 10 or 10 billion:
same number of steps.

```python
def first_element(items):
    return items[0]          # one lookup, always
```

Real examples: array index access, dictionary/set lookup, push/pop at the end
of a list, arithmetic, `len()` on a Python list.

> 🧠 **Mental picture:** flipping a light switch. Room size is irrelevant.

📄 `code/01_constant_time.py`

---

## O(log n) — Logarithmic time

**Each step throws away a fixed fraction (usually half) of the remaining data.**

```python
def binary_search(sorted_items, target):
    low, high = 0, len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            low = mid + 1        # throw away left half
        else:
            high = mid - 1       # throw away right half
    return -1
```

Why `log n`? Halving `n` repeatedly until 1 takes `log₂ n` steps.
`n = 1,000,000` → only **20** steps. `n = 1,000,000,000` → only **30** steps.

Real examples: binary search, balanced BST operations, heap push/pop.

> 🧠 **Mental picture:** finding a word in a dictionary by opening the middle,
> then the middle of the correct half, and so on.

📄 `code/04_logarithmic_time.py`

---

## O(n) — Linear time

**You touch each item a constant number of times.**

```python
def find_max(items):
    best = items[0]
    for x in items:          # every item, once
        if x > best:
            best = x
    return best
```

Real examples: `sum()`, `max()`, `x in my_list`, `.count()`, one pass over a
file, copying a list.

> 🧠 **Mental picture:** reading every page of a book once.

📄 `code/02_linear_time.py`

---

## O(n log n) — Linearithmic time

**You do a linear amount of work, `log n` times** (or: divide in half
repeatedly, doing `O(n)` work at each level).

This is the speed limit for comparison-based sorting — no comparison sort can
beat it. Python's `sorted()` and `.sort()` (Timsort) are `O(n log n)`.

```python
def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])       # log n levels of splitting
    right = merge_sort(items[mid:])
    return merge(left, right)            # O(n) merge at each level
```

Real examples: merge sort, heap sort, quicksort (average), Timsort.

> 🧠 **Mental picture:** `log n` rounds of a tournament, each round touching
> all `n` players.

📄 `code/05_linearithmic_time.py`

---

## O(n²) — Quadratic time

**For every item, you loop over all items again.**

```python
def has_duplicate_slow(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False
```

Real examples: bubble/selection/insertion sort, comparing every pair, naive
nested-loop joins.

Red flag: **a nested loop over the same collection.** Ask yourself right away:
"can a dictionary or set make this `O(n)`?" Usually, yes — see
`code/03_quadratic_time.py`, which shows the `O(n²)` version and the `O(n)`
set-based fix side by side.

> 🧠 **Mental picture:** every guest at a party shaking hands with every other
> guest.

📄 `code/03_quadratic_time.py`

---

## O(2ⁿ) — Exponential time

**Each extra input element doubles the total work.**

```python
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)   # two calls per call
```

`fib_slow(50)` would run for days. With memoization it becomes `O(n)` and
finishes instantly — the file shows both.

Real examples: naive recursive Fibonacci, brute-force subsets, naive
travelling-salesman.

> 🧠 **Mental picture:** a rumour where each person tells two new people.

📄 `code/06_exponential_time.py`

---

## O(n!) — Factorial time

**Every possible ordering of the input.** `n = 20` → 2.4 × 10¹⁸ orderings.
Hopeless beyond ~10 items. Shows up in brute-force permutation problems.

---

## The summary table

| Big O | Name | n=10 | n=1,000 | n=1,000,000 | Typical source |
|-------|------|------|---------|-------------|----------------|
| O(1) | constant | 1 | 1 | 1 | dict/set lookup, index |
| O(log n) | logarithmic | 3 | 10 | 20 | binary search |
| O(n) | linear | 10 | 1,000 | 1,000,000 | single loop |
| O(n log n) | linearithmic | 33 | 10,000 | 20,000,000 | good sorting |
| O(n²) | quadratic | 100 | 1,000,000 | 10¹² | nested loop |
| O(2ⁿ) | exponential | 1,024 | 10³⁰¹ | ☠️ | naive recursion |
| O(n!) | factorial | 3,628,800 | ☠️ | ☠️ | permutations |

**The practical rule of thumb for interviews and real work:**
`O(1)` and `O(log n)` are excellent, `O(n)` and `O(n log n)` are good and
usually the target, `O(n²)` is acceptable only for small `n`, anything
exponential needs a rethink (memoization, DP, or a better idea).

---

## Check yourself

Name the complexity:

1. Looking up `d["key"]` in a dictionary
2. Sorting a list with `sorted()`
3. Checking `if x in my_list` (a list, not a set)
4. Checking `if x in my_set`
5. Two nested loops over the same list
6. Repeatedly halving a number until it reaches 1

Next: [Lesson 5 — Space complexity](05_space_complexity.md)

---

## Related concepts

[[Concepts/Constant time|Constant time]] · [[Concepts/Logarithmic time|Logarithmic time]] · [[Concepts/Linear time|Linear time]] · [[Concepts/Linearithmic time|Linearithmic time]] · [[Concepts/Quadratic time|Quadratic time]]

See also [[Problems/_All problems|all 31 problems]] · [[00 START HERE]]
