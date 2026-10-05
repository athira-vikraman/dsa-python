---
tags:
  - complexity
---

# Linearithmic time

**O(n log n)** — do O(n) work, log n times.

This is the **speed limit for comparison sorting**: no algorithm that sorts by
comparing pairs can beat it in the worst case. That is a proven limit, not a
missing trick.

[[Problems/Merge sort|Merge sort]], [[Problems/Heap sort|heap sort]] and
[[Problems/Quick sort|quick sort]] all live here, and so does Python's own
`sorted()`.

The only way under the limit is to stop comparing — see
[[Concepts/Non-comparison sorting|Non-comparison sorting]].

Related: [[Concepts/Sorting|Sorting]] · [[Concepts/Divide and conquer|Divide and conquer]]

Back to [[00 START HERE]]
