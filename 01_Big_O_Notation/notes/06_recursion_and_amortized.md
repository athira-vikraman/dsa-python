# Lesson 6 — Recursion and Amortized Analysis

> **Goal:** analyse recursive functions without panic, and understand why
> `list.append()` is called `O(1)` when it sometimes copies the whole list.

This is the most "advanced" lesson in this module. Read it after you are
comfortable with Lessons 1–5.

---

## Part 1 — Analysing recursion

### 6.1 The recursion cost formula

For a recursive function, ask two questions:

1. **How many times does it call itself?** (the branching factor)
2. **How much does the input shrink each time?**

Then: `total work ≈ (number of calls) × (work per call)`

### 6.2 Three patterns you will meet constantly

**Pattern A — one call, input shrinks by 1 → `O(n)`**

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)     # 1 call, n-1
```
Calls: `n, n-1, n-2, ..., 1` → n calls, O(1) work each → **O(n) time, O(n) space**

**Pattern B — one call, input halves → `O(log n)`**

```python
def binary_search(items, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if items[mid] == target:
        return mid
    if items[mid] < target:
        return binary_search(items, target, mid + 1, high)   # half
    return binary_search(items, target, low, mid - 1)        # half
```
Halving until 1 → **O(log n) time, O(log n) space**

**Pattern C — two calls, input shrinks by 1 → `O(2ⁿ)`** ⚠️

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)   # TWO calls
```
Each level doubles the number of calls: 1, 2, 4, 8, … → **O(2ⁿ)**.
This is the danger pattern. The moment you see two recursive calls on an input
that shrinks by a constant, think "**can I memoize?**"

**Pattern D — two calls, input halves → `O(n log n)` or `O(n)`**

```python
def merge_sort(items):
    if len(items) <= 1: return items
    mid = len(items) // 2
    left  = merge_sort(items[:mid])    # two calls, each half
    right = merge_sort(items[mid:])
    return merge(left, right)          # O(n) work to combine
```
`log n` levels × `O(n)` work per level → **O(n log n)**.
(If the combine step were `O(1)` instead, it'd be `O(n)`.)

### 6.3 The recursion tree — how to see it

Draw the calls as a tree. Work out (a) how deep it goes, (b) how wide each
level is.

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   └── fib(1)
│   └── fib(2)
└── fib(3)          <-- fib(3) computed AGAIN
    ├── fib(2)
    └── fib(1)
```

Depth = n, width doubles each level → about `2ⁿ` nodes.
Notice `fib(3)` appears twice, `fib(2)` three times. **Repeated subproblems are
exactly what memoization eliminates** — cache each result, compute each `fib(k)`
once, and `O(2ⁿ)` collapses to `O(n)`.

### 6.4 The Master Theorem (a quick reference)

For divide-and-conquer recurrences of the form `T(n) = a·T(n/b) + O(nᵈ)`:

| Condition | Result |
|-----------|--------|
| `a < bᵈ` | `O(nᵈ)` — the combine step dominates |
| `a = bᵈ` | `O(nᵈ log n)` — balanced |
| `a > bᵈ` | `O(n^(log_b a))` — the recursion dominates |

Merge sort: `a=2, b=2, d=1` → `2 = 2¹` → balanced → `O(n log n)` ✅
Binary search: `a=1, b=2, d=0` → `1 = 2⁰` → `O(log n)` ✅

You don't need to memorise this for beginner interviews. Recognise it, and
come back when you study divide-and-conquer properly.

---

## Part 2 — Amortized analysis

### 6.5 The puzzle

Python lists are stored as contiguous blocks of memory. When a list is full and
you `append()`, Python must:

1. allocate a bigger block (roughly 1.125× larger, plus a margin),
2. copy every existing element over — that's `O(n)` work!
3. then append.

So `append()` is sometimes `O(n)`. Yet every reference says **`append()` is
O(1)**. Are they lying?

### 6.6 The answer: amortized cost

> **Amortized complexity = total cost of a sequence of operations, divided by
> the number of operations.**

The expensive resize is rare, and it gets rarer as the list grows, because
capacity grows *multiplicatively*. Appending `n` items triggers resizes at
sizes roughly `1, 2, 4, 8, 16, ... n`. The total copying work is:

```
1 + 2 + 4 + 8 + ... + n  ≈  2n
```

That's `O(n)` total copy work spread over `n` appends → **`O(1)` per append on
average**. We say `append()` is **amortized O(1)**.

It is *not* the same as "average case". Average case is about lucky vs unlucky
*inputs*; amortized is a guarantee about a *sequence* of operations — the total
is bounded even though individual operations vary.

### 6.7 Where amortized analysis shows up

| Operation | Worst case (one op) | Amortized |
|-----------|--------------------|-----------|
| `list.append(x)` | O(n) (resize) | **O(1)** |
| `list.pop()` (end) | O(1) | O(1) |
| `dict[key] = value` | O(n) (rehash/collisions) | **O(1)** |
| `set.add(x)` | O(n) | **O(1)** |
| Dynamic array growth generally | O(n) | O(1) |

⚠️ `list.insert(0, x)` and `list.pop(0)` are **genuinely O(n)** — every element
shifts, every single time. No amortization saves you. If you need fast
inserts/removals at the front, use `collections.deque`, which gives `O(1)` at
both ends. This is one of the most common real performance bugs in Python code.

```python
from collections import deque
q = deque()
q.appendleft(1)   # O(1)  -- a list would be O(n)
q.popleft()       # O(1)  -- a list would be O(n)
```

---

## Check yourself

1. A recursive function calls itself twice, each time with `n-1`. Complexity?
2. A recursive function calls itself once with `n/2`. Complexity?
3. Why is `list.append()` called O(1) when it sometimes copies everything?
4. What is the difference between *average case* and *amortized*?
5. You are writing a queue. Why is `list.pop(0)` a bug, and what should you use?

Next: [Lesson 7 — The cost of every Python operation](07_python_operation_costs.md)
