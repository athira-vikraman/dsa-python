---
tags:
  - complexity
---

# Quadratic time

**O(n²)** — for every item, you loop over all the items again.

Double the input and the work **quadruples**. Fine at n = 100, painful at
n = 10,000, hopeless at n = 1,000,000.

> 🚩 **The red flag:** a nested loop over the same collection. The moment you
> see one, ask: *can a dict or set make this O(n)?* The answer is usually yes —
> see [[Concepts/Hashing|Hashing]].

Note that a triangular loop (`for j in range(i+1, n)`) is still quadratic.
Half of n² is n².

Related: [[Concepts/Big O notation|Big O notation]] · [[Concepts/Sorting|Sorting]]

Back to [[00 START HERE]]
