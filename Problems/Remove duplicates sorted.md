---
tags:
  - problem
  - two-pointers
---

# Remove duplicates sorted

> [!question] The question
> Squash duplicates out of a sorted list in place. Return how many unique values remain.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/In-place algorithms\|In-place algorithms]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why sorted matters: in a sorted list every copy of a value sits next to its twins, so you only have to compare with the last value you kept. No set needed — which is how this stays O(1) space.

## The code

```python
def remove_duplicates(items):
    if not items:
        return 0
    writer = 1
    for reader in range(1, len(items)):
        if items[reader] != items[writer - 1]:
            items[writer] = items[reader]
            writer += 1
    return writer
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Remove duplicates (sorted)**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Move zeros to the end\|Move zeros to the end]]
- [[Problems/Remove all of one value\|Remove all of one value]]
- [[Problems/Merge two sorted lists\|Merge two sorted lists]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
