---
tags:
  - problem
  - two-pointers
---

# Merge two sorted lists

> [!question] The question
> Combine two already-sorted lists into one sorted list.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n + m)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(n + m)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

Do not re-sort. sorted(a + b) is O((n+m) log(n+m)) and throws away the fact that both lists are already in order. The next smallest value is always at one of the two fronts, so one pass is enough. This is the merge step inside merge sort.

## The code

```python
def merge_sorted(a, b):
    out = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i = i + 1
        else:
            out.append(b[j])
            j = j + 1
    while i < len(a):
        out.append(a[i])
        i = i + 1
    while j < len(b):
        out.append(b[j])
        j = j + 1
    return out
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Merge two sorted lists**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Move zeros to the end\|Move zeros to the end]]
- [[Problems/Remove duplicates sorted\|Remove duplicates sorted]]
- [[Problems/Remove all of one value\|Remove all of one value]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
