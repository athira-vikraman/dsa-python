---
tags:
  - technique
---

# Two pointers

Two variables holding two **box numbers** — two fingers on the shelf. That is
the whole idea.

## Shape 1 — opposite ends, walking inward

```
 [ a, b, c, d, e, f ]
   →                ←
  left           right
```

For **pairs**: palindromes, reversing, two-sum in sorted data. Usually needs
**sorted** input, because that is what makes "move left for a bigger sum" a
safe decision.

## Shape 2 — reader and writer, same direction

```
 [ a, b, c, d, e, f ]
   →  →
 writer reader
```

For **filtering in place**: remove, keep only, move all the X to the end. The
reader looks at every box; the writer only moves when it keeps something.

## The giveaway

If a question says **"in place"** or **"O(1) extra space"**, it is asking for
this. Nothing else gives you constant space.

Read: [[02_Arrays_And_Strings/notes/03_two_pointers|The full lesson]]
Related: [[Concepts/Sliding window|Sliding window]] (same two variables, different job) ·
[[Concepts/In-place algorithms|In-place algorithms]]

Back to [[00 START HERE]]
