---
tags:
  - technique
---

# Non-comparison sorting

Sorts that **never compare two values**, so the O(n log n) floor simply does
not apply to them.

- [[Problems/Counting sort|Counting sort]] — tally each value — O(n + k)
- [[Problems/Radix sort|Radix sort]] — one digit at a time — O(d × n)
- [[Problems/Bucket sort|Bucket sort]] — spread into buckets — O(n + k)

## The catch is always `k`

Counting sort on exam marks 0–100 is wonderful. On values up to a million it
would need a million counters. These sorts win only when the data is
**restricted**: whole numbers, in a known and smallish range.

> That restriction *is* the trade. There is no free lunch — they beat the
> limit by refusing to solve the general problem.

Related: [[Concepts/Sorting|Sorting]] · [[Concepts/Linearithmic time|Linearithmic time]]

Back to [[00 START HERE]]
