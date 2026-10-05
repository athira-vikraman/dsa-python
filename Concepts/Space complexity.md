---
tags:
  - concept
---

# Space complexity

**How much extra memory does the algorithm need as the input grows?**

The word *extra* is the whole trick. The input was already in memory — you
were handed it. We count only the **bowls you dirtied**, not the vegetables
you were given. (The textbook word is *auxiliary space*.)

## The rule that covers most cases

> **Counting** something → O(1) space.
> **Collecting** something → O(n) space.

```python
def count_evens(numbers):      def collect_evens(numbers):
    count = 0                      evens = []
    for n in numbers:              for n in numbers:
        if n % 2 == 0:                 if n % 2 == 0:
            count += 1                     evens.append(n)
    return count                   return evens
# O(1) space                   # O(n) space
```

Nearly identical code. Totally different memory.

## Recursion counts

See [[Concepts/Recursion|Recursion]] — n nested calls is O(n) space even with
no data structure in sight.

Read: [[01_Big_O_Notation/notes/05a_time_vs_space_for_beginners|Time vs space, the gentle version]]
Related: [[Concepts/In-place algorithms|In-place algorithms]] · [[Concepts/Big O notation|Big O notation]]

Back to [[00 START HERE]]
