---
tags:
  - concept
---

# Big O notation

The language for describing how an algorithm's cost grows as the input grows.

It is a statement about **shape**, not about seconds. `O(n)` means "double the
input, roughly double the work" — on your laptop, on a server, in any
language.

## The ranking

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
best ────────────────────────────────────────────► worst
```

- [[Concepts/Constant time|Constant time]] — O(1)
- [[Concepts/Logarithmic time|Logarithmic time]] — O(log n)
- [[Concepts/Linear time|Linear time]] — O(n)
- [[Concepts/Linearithmic time|Linearithmic time]] — O(n log n)
- [[Concepts/Quadratic time|Quadratic time]] — O(n²)

## The four rules

1. Drop constants — `O(3n)` → `O(n)`
2. Drop lower terms — `O(n² + n)` → `O(n²)`
3. Sequential adds, nested multiplies
4. Different inputs get different letters — `O(a · b)`, not `O(n²)`

## Read more

- [[01_Big_O_Notation/notes/02_what_is_big_o|What Big O actually means]]
- [[01_Big_O_Notation/notes/03_rules_of_big_o|The four rules in full]]
- [[01_Big_O_Notation/notes/09_cheatsheet|Cheat sheet]]

Every problem note in this vault states its Big O. See the backlinks panel.

Back to [[00 START HERE]]
