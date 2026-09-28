# Exercises & Answer Key

Three kinds of practice here:

1. **Part A — Analysis drills.** Read code, name the complexity. Paper only.
2. **Part B — Coding tasks.** Fill in `practice.py`, then run the tests.
3. **Part C — Interview questions.** Say the answers out loud.

Answers are at the bottom. **Attempt first, then check.** Reading answers feels
like learning and isn't.

---

## Part A — Analysis drills

Give the **time** and **space** complexity of each.

### A1
```python
def f(items):
    return items[0] + items[-1]
```

### A2
```python
def f(items):
    total = 0
    for x in items:
        total += x
    return total
```

### A3
```python
def f(items):
    for x in items:
        for y in items:
            print(x, y)
```

### A4
```python
def f(n):
    i = 1
    while i < n:
        i *= 2
```

### A5
```python
def f(items):
    for x in items:
        for i in range(10):
            print(x, i)
```

### A6
```python
def f(list_a, list_b):
    for x in list_a:
        for y in list_b:
            print(x, y)
```

### A7
```python
def f(items):
    result = []
    for x in items:
        if x not in result:
            result.append(x)
    return result
```

### A8
```python
def f(items):
    return sorted(items)[0]
```

### A9
```python
def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)
```

### A10
```python
def f(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] + items[j] == 100:
                return True
    return False
```

### A11
```python
def f(items):
    seen = set()
    for x in items:
        seen.add(x)
    return len(seen)
```

### A12
```python
def f(n):
    result = ""
    for i in range(n):
        result += str(i)
    return result
```

### A13
```python
def f(matrix):     # n x n matrix
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total
```

### A14
```python
def f(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### A15
```python
def f(items):
    for x in items:              # n
        print(x)
    for x in items:              # n
        for y in items:          # n
            print(x, y)
```

---

## Part B — Coding tasks

Open `exercises/practice.py`. Each function has a docstring describing the
required complexity. Implement them, then run:

```bash
python3 -m unittest discover -s tests -v
```

Tasks:

| # | Function | Required |
|---|----------|----------|
| 1 | `get_first_and_last` | O(1) time, O(1) space |
| 2 | `count_occurrences` | O(n) time, O(1) space |
| 3 | `has_duplicates` | O(n) time, O(n) space |
| 4 | `find_pair_with_sum` | O(n) time, O(n) space (naive is O(n²)) |
| 5 | `binary_search` | O(log n) time, O(1) space |
| 6 | `reverse_in_place` | O(n) time, **O(1)** space |
| 7 | `first_non_repeating` | O(n) time, O(n) space |
| 8 | `fibonacci` | O(n) time, O(1) space |
| 9 | `merge_sorted_lists` | O(n + m) time |
| 10 | `most_frequent` | O(n) time |
| 11 | `is_anagram` | O(n) time |
| 12 | `build_sentence` | O(total length) — no `+=` in a loop |

Solutions with commentary: `exercises/solutions.py`.

---

## Part C — Interview questions

Answer out loud, in full sentences.

1. What is Big O, in one sentence?
2. Why do we drop constants?
3. Difference between O, Ω and Θ?
4. Difference between worst case and amortized?
5. Why is `list.append()` O(1) when it sometimes copies the whole list?
6. `x in list` vs `x in set` — and why?
7. You have an O(n²) solution. Walk me through how you'd look for a better one.
8. What does O(n) space mean? Does recursion count?
9. When would you pick an O(n²) algorithm over an O(n log n) one?
10. Why is `O(n log n)` the limit for comparison sorting?

---
---

# ANSWER KEY

## Part A

**A1** — O(1) time, O(1) space. Two index lookups; no loop.

**A2** — O(n) time, O(1) space. One pass, one accumulator.

**A3** — O(n²) time, O(1) space. Nested loops over the same list → multiply.

**A4** — O(log n) time, O(1) space. `i` *multiplies*, so it reaches `n` in
log₂(n) steps. (If it were `i += 2`, it would be O(n).)

**A5** — **O(n)** time, O(1) space. The inner loop is bounded by the constant
10, not by n. `O(10n) = O(n)`. Nested ≠ automatically quadratic.

**A6** — **O(a · b)** time, O(1) space, where a and b are the two lengths.
Not O(n²) — different inputs get different letters.

**A7** — O(n²) time, O(n) space. `x not in result` is a hidden O(n) list scan.
Fix with a `seen` set → O(n) time.

**A8** — O(n log n) time, O(n) space. The sort dominates; `sorted()` copies.
(Just want the minimum? `min(items)` is O(n) time, O(1) space.)

**A9** — O(2ⁿ) time, O(n) space. Naive Fibonacci: two calls per call; the
space is the deepest call-stack path.

**A10** — O(n²) time, O(1) space. The triangular loop does n(n−1)/2 ≈ n²/2
iterations; halving doesn't change the class.
(A `seen` set makes it O(n) time, O(n) space.)

**A11** — O(n) time, O(n) space. One pass; the set can hold up to n items.

**A12** — O(n²) time, O(n) space. String `+=` in a loop copies the whole
string each iteration. `"".join(...)` makes it O(n).

**A13** — O(n²) time, O(1) space **for an n×n matrix** — but that's linear in
the *input size*, since the input contains n² numbers. You cannot do better;
you must read every value. Better phrased: O(r · c).

**A14** — O(log n) time, O(1) space. Iterative binary search; the range halves
each iteration and only three variables are used.

**A15** — O(n²) time, O(1) space. `n + n² → n²`. Drop the lower-order term.

---

## Lesson check-yourself answers

**Lesson 1**
1. Because seconds depend on your CPU, language and load — not on the
   algorithm. Growth is the property that belongs to the algorithm.
2. Small n: `n²` wins. At n = 10 it does 100 steps while `5n + 100` does 150.
   They cross near n ≈ 12.8; past that the linear one wins and the gap keeps
   widening (at n = 1000: 5,100 steps vs 1,000,000). Ship the linear one.
3. About 8 seconds — linear means 4× the input is 4× the time.

**Lesson 2**
1. Growth.
2. True, and useless — it's a valid but loose upper bound. Always give the
   tightest one.
3. Best O(1) (middle element is the target), worst O(log n).
4. Because it's the only promise you can keep to every user, on every input.

**Lesson 3**
1. O(n) 2. O(n²) 3. O(n log n) 4. O(n) 5. O(n · m) 6. O(2ⁿ) — exponential
beats any polynomial, however large the exponent.

**Lesson 4**
1. O(1) 2. O(n log n) 3. O(n) 4. O(1) 5. O(n²) 6. O(log n)

**Lesson 5**
1. O(1) — `sum()` keeps a single running total.
2. O(n) — it builds and returns a new list.
3. The call stack: n frames are alive simultaneously.
4. O(n) time, O(n) space.
5. The two-pointer in-place reverse — O(1) vs O(n).

**Lesson 6**
1. O(2ⁿ) 2. O(log n)
3. Because the resizes are rare and grow geometrically: total copying over n
   appends is O(n), so the average per append is O(1) — that's *amortized*.
4. Average case = expectation over *inputs*. Amortized = a guarantee over a
   *sequence of operations*, regardless of luck.
5. `pop(0)` shifts all remaining elements — O(n) each, O(n²) to drain the
   queue. Use `collections.deque` and `popleft()` → O(1).

**Lesson 7**
1. O(n) vs O(1).
2. Strings are immutable, so each `+=` allocates and copies the whole string
   so far: 1 + 2 + 3 + … + n = O(n²).
3. `deque` — O(1) at both ends; `list.pop(0)` is O(n).
4. O(n). (Pushing n items one at a time would be O(n log n); `heapify` is
   smarter.)
5. O(n) per slice → O(n²) over the loop.

**Lesson 8**
- **A** O(n³) — three nested loops.
- **B** O(log n) — repeated halving.
- **C** O(n²) — triangular loop, n(n−1)/2 ≈ n²/2.
- **D** O(n + m) — sequential, two different inputs. Not O(n²), not O(n).
- **E** O(n) for the set + O(k log k) for the sort where k = distinct values
  → O(n + k log k), worst case O(n log n). Space O(n).

---

## Part C — model answers

**1.** Big O describes how an algorithm's time or memory grows as the input
grows, ignoring constants and lower-order terms.

**2.** Constants depend on hardware and language, not on the algorithm. The
*shape* of the growth is what distinguishes algorithms, and it's what survives
being run on a different machine.

**3.** O = upper bound ("at most"), Ω = lower bound ("at least"), Θ = both
("exactly"). Everyday usage says "O" but usually means the tight bound Θ.

**4.** Worst case is about the unluckiest *input* for a single operation.
Amortized is the average cost per operation across a *sequence*, where rare
expensive operations are paid for by many cheap ones.

**5.** When the array is full, Python allocates a larger block and copies —
O(n). But capacity grows multiplicatively, so total copy work across n appends
is about 2n, i.e. O(1) per append amortized.

**6.** List: O(n), it scans element by element. Set: O(1), it hashes the value
and jumps straight to the bucket. Converting a list to a set costs O(n) once
and pays for itself immediately inside a loop.

**7.** "I'd look for repeated work. If the inner loop is searching, a
dict/set makes lookups O(1) and the whole thing O(n). If it's recursion with
overlapping subproblems, I'd memoize. If the data is sorted, binary search or
two pointers. If it's a contiguous range, a sliding window."

**8.** It means the extra memory you allocate grows proportionally with the
input. Yes — recursion counts, because each pending call holds a stack frame.
A recursion of depth n is O(n) space even if it allocates nothing.

**9.** When n is small (the constants dominate — this is why Timsort uses
insertion sort on short runs), when the O(n²) algorithm is in-place and memory
is scarce, or when the data is nearly sorted and insertion sort approaches
O(n).

**10.** There are n! possible orderings. Each comparison gives one bit of
information, halving the possibilities at best, so you need at least
log₂(n!) ≈ n log n comparisons to distinguish them. Sorts that beat it
(counting sort, radix sort) don't compare — they exploit the structure of the
keys.
