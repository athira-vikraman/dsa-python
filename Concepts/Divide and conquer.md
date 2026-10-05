---
tags:
  - technique
---

# Divide and conquer

Split the problem in half, solve each half, combine the answers.

- [[Problems/Binary search|Binary search]] — throw away one half, O(log n)
- [[Problems/Merge sort|Merge sort]] — sort both halves, merge them, O(n log n)
- [[Problems/Quick sort|Quick sort]] — partition around a pivot, O(n log n)

## Why log n keeps appearing

Halving something until you reach one takes `log₂ n` steps. If you do O(n)
work at each of those levels, you get O(n log n). If you do O(1) work, you get
O(log n). That is the whole arithmetic.

Related: [[Concepts/Recursion|Recursion]] · [[Concepts/Linearithmic time|Linearithmic time]]

Back to [[00 START HERE]]
