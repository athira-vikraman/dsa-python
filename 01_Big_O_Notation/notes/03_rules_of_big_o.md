# Lesson 3 — The Rules for Simplifying Big O

> **Goal:** take any messy step count like `4n² + 7n + 12` and confidently
> reduce it to `O(n²)`.

There are only four rules. Learn these and 90% of complexity analysis is done.

---

## Rule 1 — Drop the constant multipliers

`O(2n)` → `O(n)`  `O(n/2)` → `O(n)`  `O(500)` → `O(1)`

**Why?** Doubling the work doesn't change the *shape* of the growth. Both `n`
and `2n` double when `n` doubles. The constant depends on your CPU and language;
the shape belongs to the algorithm.

```python
def print_twice(items):
    for x in items:   # n steps
        print(x)
    for x in items:   # n more steps
        print(x)
    # total 2n -> O(n)
```

---

## Rule 2 — Drop the lower-order terms

`O(n² + n)` → `O(n²)`  `O(n + log n)` → `O(n)`  `O(n! + 2ⁿ)` → `O(n!)`

**Why?** At large `n`, the biggest term drowns out the rest.
At `n = 1,000,000`: `n² = 1,000,000,000,000` and `n = 1,000,000`.
The `n` is 0.0001% of the total. It's noise.

```python
def mixed(items):
    n = len(items)
    for x in items:              # n
        print(x)
    for x in items:              # n²
        for y in items:
            print(x, y)
    # total n² + n -> O(n²)
```

**The keeper rule:** in a sum, keep only the fastest-growing term.

Growth ranking, slowest-growing (best) to fastest-growing (worst):

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

---

## Rule 3 — Sequential code ADDS, nested code MULTIPLIES

This is the rule people get wrong most often.

**Sequential (one after the other) → add, then drop the smaller:**

```python
for x in a:      # O(n)
    print(x)
for y in b:      # O(m)
    print(y)
# O(n + m)   -- if a and b are the same list: O(2n) = O(n)
```

**Nested (a loop inside a loop) → multiply:**

```python
for x in a:          # runs n times ...
    for y in b:      # ... and each time runs m times
        print(x, y)
# O(n * m)   -- if both are the same list: O(n²)
```

> **Reading trick:** the word "**and then**" means `+`.
> The word "**for each**" means `×`.

⚠️ **Nested does not automatically mean O(n²).** What matters is *how many
times the inner loop actually runs*:

```python
for i in range(n):        # n times
    for j in range(3):    # only 3 times, constant!
        print(i, j)
# O(n * 3) = O(n)   <- linear, not quadratic
```

---

## Rule 4 — Different inputs get different variable names

If a function takes two collections, you may **not** call them both `n`.

```python
def bad_naming(list_a, list_b):
    for x in list_a:
        for y in list_b:
            print(x, y)
```

This is `O(a · b)`, **not** `O(n²)`. If `list_a` has 1 million items and
`list_b` has 2 items, the truth is "2 million steps", which `O(n²)` would
wildly overstate. Interviewers specifically listen for this.

---

## Putting it together — worked examples

### Example A
```python
def example_a(items):          # n = len(items)
    total = 0                  # O(1)
    for x in items:            # O(n)
        total += x
    for x in items:            # O(n)
        for y in items:        # O(n) each
            total += x * y     # -> O(n²)
    return total               # O(1)
```
Count: `1 + n + n² + 1` = `n² + n + 2`
→ drop constants and lower terms → **O(n²)**

### Example B
```python
def example_b(items):
    n = len(items)
    i = 1
    while i < n:               # i: 1, 2, 4, 8, 16 ... doubling
        print(items[i])
        i *= 2
```
Doubling until reaching `n` takes `log₂(n)` iterations → **O(log n)**

### Example C
```python
def example_c(items):
    for x in items:            # n times
        for y in items:        # n times
            for z in items:    # n times
                print(x,y,z)
```
`n × n × n` → **O(n³)**

### Example D — the sneaky one
```python
def example_d(items, target):
    for x in items:            # n times
        if target in items:    # `in` on a list is O(n) itself!
            return True
    return False
```
The `in` check hides a loop. `n × n` → **O(n²)**.
**Lesson: a function call is not automatically O(1). You must know what's
inside it.** (Lesson 7 lists the cost of every common Python operation.)

---

## Check yourself

Reduce these to simplest Big O:

1. `O(5n + 3)`
2. `O(n² + 100n + 5000)`
3. `O(n · log n + n)`
4. Two separate loops over the same list of `n` items
5. A loop over `n` containing a loop over `m`
6. `O(2ⁿ + n¹⁰⁰)`

(Answers in `exercises/exercises.md`.)

Next: [Lesson 4 — The common complexity classes](04_common_complexity_classes.md)

---

## Related concepts

[[Concepts/Big O notation|Big O notation]] · [[Concepts/Quadratic time|Quadratic time]] · [[Concepts/Logarithmic time|Logarithmic time]]

See also [[Problems/_All problems|all 31 problems]] · [[00 START HERE]]
