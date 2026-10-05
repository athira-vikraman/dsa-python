---
tags:
  - problem
  - two-pointers
---

# Remove all of one value

> [!question] The question
> Delete every copy of a value in place, and return the new length.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/In-place algorithms\|In-place algorithms]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Same four lines as move-zeros — only the if changed. Compare with while v in items: items.remove(v), which searches (O(n)) and then shifts (O(n)) on every single call: O(n²) for the same job.

## The code

```python
def remove_all(items, value):
    writer = 0
    for reader in range(len(items)):
        if items[reader] != value:
            items[writer] = items[reader]
            writer += 1
    return writer
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Remove all of one value**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Move zeros to the end\|Move zeros to the end]]
- [[Problems/Remove duplicates sorted\|Remove duplicates sorted]]
- [[Problems/Merge two sorted lists\|Merge two sorted lists]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
