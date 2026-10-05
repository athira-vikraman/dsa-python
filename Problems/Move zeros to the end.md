---
tags:
  - problem
  - two-pointers
---

# Move zeros to the end

> [!question] The question
> Move every 0 to the end, keeping the other numbers in order, in place.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/In-place algorithms\|In-place algorithms]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

The shape to memorise: the reader looks at every box; the writer only moves when something is worth keeping. Any problem that says remove, filter or squash in place is this shape.

## The code

```python
def move_zeros_to_end(items):
    writer = 0
    for reader in range(len(items)):
        if items[reader] != 0:
            items[writer] = items[reader]
            writer += 1
    while writer < len(items):
        items[writer] = 0
        writer += 1
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Move zeros to the end**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Remove duplicates sorted\|Remove duplicates sorted]]
- [[Problems/Remove all of one value\|Remove all of one value]]
- [[Problems/Merge two sorted lists\|Merge two sorted lists]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
