# Lesson 1 — Why We Measure Code (and why not with a stopwatch)

> **Goal of this lesson:** understand *why* computer scientists invented Big O,
> before we learn *what* it is.

---

## 1.1 A story

You write a function that finds a name in a list of contacts.
On your laptop with 100 contacts, it runs in 0.001 seconds. 

Your company deploys it. Now there are 10,000,000 contacts.
The function takes 90 seconds. Users complain. You get a call at 2 AM.

Nothing about your code changed. **The input grew.**

Big O is the tool that would have warned you at your desk, in 10 seconds,
without ever running the code on 10 million contacts.

---

## 1.2 Why not just time the code?

The obvious idea is: run it, measure seconds with a stopwatch.

```python
import time
start = time.time()
my_function(data)
print(time.time() - start)
```

This is called **benchmarking**, and it is useful — but it is a bad way to
*compare algorithms*, because the number you get depends on:

| Thing that changes the seconds | Does it change the algorithm? |
|--------------------------------|-------------------------------|
| A faster CPU                   | No |
| Another program hogging RAM    | No |
| Python vs C++                  | No |
| Laptop on battery saver        | No |
| **The size of the input**      | **This is the real question** |

So we throw away everything machine-specific and keep only the one thing
that truly belongs to the algorithm:

> **How does the amount of work grow as the input grows?**

That relationship is what Big O captures. It is a statement about *shape*,
not about *seconds*.

---

## 1.3 Counting steps instead of seconds

Instead of seconds, we count **basic operations** — things that take a fixed
amount of time no matter how big the data is: one comparison, one addition,
one assignment, one list index lookup.

```python
def total(numbers):          # n = len(numbers)
    result = 0               # 1 step
    for x in numbers:        # loop runs n times
        result = result + x  #   1 step each time  -> n steps
    return result            # 1 step
```

Total steps ≈ `n + 2`.

Now ask: if `n` doubles, what happens to `n + 2`? It roughly doubles.
That is the honest description of this function: **work grows in proportion
to n**. We write it `O(n)` and say "order n" or "linear time".

---

## 1.4 The growth table (the reason anyone cares)

Assume one step takes 1 nanosecond. Here is how long different growth shapes
take as `n` grows:

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|------|----------|------|------------|-------|-------|
| 10 | 1 ns | 3 ns | 10 ns | 33 ns | 100 ns | 1 µs |
| 100 | 1 ns | 7 ns | 100 ns | 664 ns | 10 µs | 4×10¹³ years |
| 1,000 | 1 ns | 10 ns | 1 µs | 10 µs | 1 ms | forever |
| 1,000,000 | 1 ns | 20 ns | 1 ms | 20 ms | **16 minutes** | forever |
| 1,000,000,000 | 1 ns | 30 ns | 1 s | 30 s | **31 years** | forever |

Read the `O(n²)` column slowly. That is the difference between a feature that
ships and a feature that gets deleted. This single table is why interviewers
ask "what's the complexity?" in almost every interview.

---

## 1.5 What you should take away

1. Seconds depend on the machine; **growth depends on the algorithm**.
2. We count basic operations, then describe how that count grows with `n`.
3. Big O is a *prediction tool*: it tells you what happens at 10 million
   while you are still testing with 10.

---

## Check yourself

Answer in your head before moving on (answers in `exercises/exercises.md`):

1. Why is "my function takes 3 seconds" a weak statement to an interviewer?
2. A function does `5n + 100` steps. Another does `n²`. For very small `n`,
   which is faster? For very large `n`? Which one would you ship?
3. If an `O(n)` function takes 2 seconds on 1 million items, roughly how long
   on 4 million?

Next: [Lesson 2 — What Big O actually means](02_what_is_big_o.md)
