---
tags:
  - technique
---

# Recursion

A function that calls itself. Two questions tell you the cost:

1. **How many times does it call itself?**
2. **How much does the input shrink each time?**

| Pattern | Complexity |
|---|---|
| 1 call, shrink by 1 | O(n) |
| 1 call, halve | O(log n) |
| 2 calls, halve | O(n log n) |
| **2 calls, shrink by 1** | **O(2ⁿ)** 🚩 |

That last row is the danger. Two recursive calls on an input shrinking by one
means the call tree doubles every level. The fix is almost always
**memoization** — cache each result and O(2ⁿ) collapses to O(n).

## Recursion costs memory

Every unfinished call sits on the call stack. Picture asking a friend, who
asks a friend, who asks a friend — nobody has gone home, and each one takes a
chair. **Depth n = O(n) space**, even if you allocate nothing.

Python stops at about 1000 chairs and raises `RecursionError`.

Read: [[01_Big_O_Notation/notes/06_recursion_and_amortized|The full lesson]]
Related: [[Concepts/Divide and conquer|Divide and conquer]] · [[Concepts/Space complexity|Space complexity]]

Back to [[00 START HERE]]
