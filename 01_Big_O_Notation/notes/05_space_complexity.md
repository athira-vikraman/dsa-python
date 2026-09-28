# Lesson 5 — Space Complexity

> **Goal:** answer the second half of every interview question —
> "...and what's the space complexity?"

---

## 5.1 The question space complexity asks

> **How much EXTRA memory does the algorithm need as the input grows?**

The word **extra** (also called *auxiliary space*) is the whole trick.
The input itself is already in memory — you were handed it. We count only what
*you allocate on top of it*.

---

## 5.2 O(1) space — "in-place"

You use a fixed number of variables, no matter how large the input.

```python
def total(numbers):
    result = 0           # 1 variable
    for x in numbers:    # the loop variable is 1 more
        result += x
    return result
# Space: O(1)  -- two variables whether numbers has 10 or 10 million items
```

Algorithms that rearrange data without a second copy are called **in-place**:
reversing a list with two pointers, bubble sort, quicksort's partition step.

---

## 5.3 O(n) space — a copy that grows with the input

```python
def doubled(numbers):
    result = []              # grows to n items
    for x in numbers:
        result.append(x * 2)
    return result
# Time: O(n)   Space: O(n)
```

Any time you build a new list, dict or set whose size tracks `n`, that's `O(n)`
space. This includes the memo dictionary in memoization, and the `seen` set in
a duplicate check.

> ⚖️ **The classic trade-off:** you almost always *buy* time with space.
> The `O(n²)` duplicate check uses `O(1)` space. The `O(n)` fix uses an `O(n)`
> set. That trade is usually worth it — but say it out loud in an interview,
> because it shows you understand the cost.

---

## 5.4 Recursion uses space even when you allocate nothing

This is the part beginners miss. **Every pending function call sits on the
call stack and occupies memory.**

```python
def countdown(n):
    if n == 0:
        return
    countdown(n - 1)
# Allocates no list. But n nested calls are alive at once.
# Space: O(n)
```

Compare recursion depths:

| Algorithm | Recursion depth | Space |
|-----------|-----------------|-------|
| `countdown(n)` | n | O(n) |
| Binary search (recursive) | log n | O(log n) |
| Merge sort | log n deep, but **O(n)** for merge buffers | O(n) |
| Naive `fib(n)` | n (deepest path) | O(n) |

Python also enforces a recursion limit (~1000 by default) and raises
`RecursionError` beyond it — a real, practical consequence of stack space.
`code/07_space_complexity.py` demonstrates this safely.

---

## 5.5 Output space: counted or not?

Convention: **space required for the output is usually excluded** when the
problem inherently requires producing that output.

- "Return a sorted copy of the list" → the returned list is required output,
  so people typically report `O(n)` auxiliary space anyway, being explicit.
- "Return True if a duplicate exists" → output is one boolean, so any `O(n)`
  set you build is genuinely extra space and must be counted.

When in doubt in an interview, state your assumption:
*"O(n) auxiliary space, not counting the output list."* That sentence alone
sounds senior.

---

## 5.6 Worked comparisons

### Reversing a list

```python
# Version A — extra space
def reverse_copy(items):
    return items[::-1]          # Time O(n), Space O(n)

# Version B — in place
def reverse_in_place(items):
    left, right = 0, len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items                # Time O(n), Space O(1)
```

Same time complexity, very different memory. On a 10 GB dataset, this choice
decides whether your program runs at all.

### Fibonacci, three ways

| Version | Time | Space |
|---------|------|-------|
| Naive recursion | O(2ⁿ) | O(n) (call stack) |
| Memoized recursion | O(n) | O(n) (memo + stack) |
| Iterative, two variables | O(n) | **O(1)** |

The iterative version wins on both axes. See `code/06_exponential_time.py`.

---

## 5.7 How to report complexity like a professional

Always give both numbers, and name the variable:

> "This is **O(n log n) time** and **O(n) space**, where n is the number of
> elements in the input list."

If there are two inputs: *"O(a + b) time, O(1) space, where a and b are the
lengths of the two lists."*

---

## Check yourself

1. What is the space complexity of `sum(my_list)`?
2. What is the space complexity of `sorted(my_list)`?
3. Why does `countdown(n)` use `O(n)` space when it creates no data structure?
4. A function builds a `seen` set to detect duplicates in one pass.
   Time and space?
5. Which uses less memory: `items[::-1]` or a two-pointer in-place reverse?

Next: [Lesson 6 — Recursion and amortized analysis](06_recursion_and_amortized.md)
