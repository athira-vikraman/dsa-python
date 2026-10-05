# Lesson 8 — How to Analyse Any Code, Step by Step

> **Goal:** a repeatable procedure you can run on unfamiliar code, in an
> interview, under pressure.

---

## 8.1 The 5-step method

**Step 1 — Name your variable(s).**
"Let n be the number of elements in `items`." If there are two inputs, use
`n` and `m`. Say it out loud; it prevents Rule 4 mistakes.

**Step 2 — Find every loop and recursive call.**
Ignore individual statements for now. Work happens in loops and recursion.

**Step 3 — For each loop, ask: how many times does this run?**
Not "what does it look like" — how many *iterations*.
- `for x in items` → n
- `for i in range(3)` → 3, a constant
- `while i < n: i *= 2` → log n
- `for j in range(i, n)` (inside a loop over i) → varies; sum it up

**Step 4 — Combine: nested = multiply, sequential = add.**
Then apply the simplification rules from Lesson 3.

**Step 5 — Check for hidden costs.**
Every function call: is it O(1)? `in` on a list is O(n). Slicing copies.
`sorted()` is O(n log n). String `+=` is O(n). This step catches the
mistakes that separate a confident answer from a wrong one.

Finally, **state both time and space**, naming the variable.

---

## 8.2 The triangular-loop pattern (learn this one)

```python
for i in range(n):
    for j in range(i + 1, n):
        print(i, j)
```

The inner loop doesn't run `n` times — it runs `n-1`, then `n-2`, … then 0.
Total:

```
(n-1) + (n-2) + ... + 1 + 0  =  n(n-1)/2  =  n²/2 - n/2
```

Drop constants and lower terms → **O(n²)**.

> 💡 Half of `n²` is still `n²`. Comparing every *pair* of items is quadratic,
> even though you skipped half the pairs.

---

## 8.3 Fully worked examples

### Example 1

```python
def example_1(items):
    n = len(items)                 # O(1)
    total = 0                      # O(1)
    for x in items:                # n iterations
        total += x                 #   O(1) each
    return total / n if n else 0   # O(1)
```

- Step 1: n = len(items)
- Step 3: one loop, n iterations, O(1) body
- Step 4: `1 + 1 + n + 1` → O(n)
- Step 5: no hidden costs; `len()` is O(1)
- **O(n) time, O(1) space**

---

### Example 2

```python
def example_2(items):
    result = []                    # O(1)
    for x in items:                # n
        if x not in result:        # ⚠️ O(len(result)) -> up to O(n)
            result.append(x)       # O(1) amortized
    return result
```

Step 5 catches it: `not in result` scans a list.
n iterations × O(n) check → **O(n²) time, O(n) space**.

The fix:

```python
def example_2_fast(items):
    seen = set()
    result = []
    for x in items:
        if x not in seen:          # O(1)
            seen.add(x)            # O(1)
            result.append(x)
    return result
# O(n) time, O(n) space
```

Same output, same line count, 1000× faster at n = 100,000.

---

### Example 3

```python
def example_3(matrix):             # matrix is r rows x c columns
    total = 0
    for row in matrix:             # r iterations
        for value in row:          # c iterations each
            total += value
    return total
```

Nested → multiply → **O(r · c) time, O(1) space**.

Note: this is "quadratic-looking" but it is actually **linear in the size of
the input**, because the input *is* `r · c` numbers. You cannot do better —
you must read every value. A nested loop is not automatically a problem.

---

### Example 4

```python
def example_4(items):
    items = sorted(items)          # O(n log n)
    for i in range(len(items)):    # O(n)
        print(items[i])
    return items[0]                # O(1)
```

Sequential: `n log n + n + 1` → keep the biggest → **O(n log n) time**.
`sorted()` builds a new list → **O(n) space**.

---

### Example 5 — two inputs

```python
def example_5(list_a, list_b):
    set_b = set(list_b)            # O(m)
    result = []
    for x in list_a:               # O(n)
        if x in set_b:             # O(1)
            result.append(x)
    return result
```

**O(n + m) time, O(m) space** — note we did *not* say O(n²).
The naive version (`if x in list_b`) would be O(n · m).

---

## 8.4 How to say it in an interview

Don't just blurt "O(n²)". Narrate the reasoning — that's what is actually being
graded:

> "Let n be the length of the input list. The outer loop runs n times, and
> for each iteration the `in` check on a list is O(n), so that's O(n²) time.
> I'm only using a few variables, so O(1) space.
> I can improve it: if I put the elements in a set, membership becomes O(1),
> which gives O(n) time at the cost of O(n) space. That trade is usually worth
> it — shall I write that version?"

That paragraph demonstrates analysis, optimisation, trade-off awareness, and
communication. It is the whole skill in five sentences.

---

## 8.5 The optimisation checklist

When you find your solution is too slow, run down this list:

| Symptom | Likely fix |
|---------|-----------|
| Nested loop searching for a value | **Use a dict/set** → O(n) |
| Repeated recursive subproblems | **Memoize** → often O(n) |
| Searching a sorted list linearly | **Binary search** → O(log n) |
| Need repeated min/max | **Heap** → O(log n) |
| Removing from the front of a list | **deque** → O(1) |
| Building a string with `+=` | **`"".join()`** → O(n) |
| Re-sorting inside a loop | **Sort once** outside |
| Counting occurrences with nested loops | **`collections.Counter`** → O(n) |

Nine out of ten "make it faster" problems are solved by one of these rows.

---

## Check yourself

Analyse each (answers in `exercises/exercises.md`):

```python
# A
for i in range(n):
    for j in range(n):
        for k in range(n):
            do_something()

# B
i = n
while i > 1:
    i = i // 2

# C
for i in range(n):
    for j in range(i, n):
        do_something()

# D
for i in range(n):
    do_something()
for j in range(m):
    do_something()

# E
def f(items):
    return sorted(set(items))
```

Next: [Lesson 9 — The cheat sheet](09_cheatsheet.md)

---

## Related concepts

[[Concepts/Big O notation|Big O notation]] · [[Concepts/Hashing|Hashing]] · [[Concepts/Quadratic time|Quadratic time]]

See also [[Problems/_All problems|all 31 problems]] · [[00 START HERE]]
