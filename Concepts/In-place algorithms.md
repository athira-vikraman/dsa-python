---
tags:
  - concept
---

# In-place algorithms

An algorithm that rearranges the data **without building a second copy** —
O(1) extra space.

```python
# O(n) space: builds a whole new list
reversed_copy = items[::-1]

# O(1) space: two fingers swapping
left, right = 0, len(items) - 1
while left < right:
    items[left], items[right] = items[right], items[left]
    left += 1
    right -= 1
```

Both are O(n) *time*. On a 10 GB dataset, only one of them runs.

## How to recognise the ask

The words **"in place"** and **"O(1) extra space"** in a question are
practically the examiner naming the technique:
[[Concepts/Two pointers|two pointers]].

Related: [[Concepts/Space complexity|Space complexity]] · [[Concepts/Constant time|Constant time]]

Back to [[00 START HERE]]
