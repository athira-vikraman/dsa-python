---
tags:
  - technique
---

# Searching

Finding a value. Which method you can use depends entirely on whether the data
is **sorted**.

| Situation | Method | Cost |
|---|---|---|
| Unsorted list | [[Problems/Linear search\|Linear search]] | O(n) |
| Sorted list | [[Problems/Binary search\|Binary search]] | O(log n) |
| You can build a set first | [[Concepts/Hashing\|Hashing]] | O(1) per lookup |

> Binary search on unsorted data gives **wrong answers**, not slow ones. And
> sorting first costs O(n log n), so for a single lookup a plain scan is
> cheaper. Binary search pays off when you search the same sorted data many
> times.

Related: [[Concepts/Divide and conquer|Divide and conquer]] · [[Concepts/Logarithmic time|Logarithmic time]]

Back to [[00 START HERE]]
