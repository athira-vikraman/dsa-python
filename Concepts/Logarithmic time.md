---
tags:
  - complexity
---

# Logarithmic time

**O(log n)** — each step throws away a fixed fraction, usually half, of what
is left.

Halving a million down to one takes **20 steps**. A billion takes 30. This is
why [[Problems/Binary search|binary search]] feels like magic.

How to spot it: the loop variable is **multiplied or divided** (`i *= 2`,
`i //= 2`) instead of added to. Adding gives you
[[Concepts/Linear time|linear time]]; multiplying gives you logarithmic.

Related: [[Concepts/Divide and conquer|Divide and conquer]] ·
[[Concepts/Big O notation|Big O notation]]

Back to [[00 START HERE]]
