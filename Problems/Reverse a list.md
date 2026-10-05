---
tags:
  - problem
  - two-pointers
---

# Reverse a list

> [!question] The question
> Reverse a list in place, without building a second list.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/In-place algorithms\|In-place algorithms]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why O(1) space? We never build a second list. Two fingers walk toward each other swapping as they go, so the only extra memory is two numbers. items[::-1] gives the same answer in O(n) space.

## The code

```python
def reverse(items):
    left, right = 0, len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Reverse a list**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Valid palindrome\|Valid palindrome]]
- [[Problems/Two Sum sorted\|Two Sum sorted]]
- [[Problems/Squares of a sorted array\|Squares of a sorted array]]
- [[Problems/Container with most water\|Container with most water]]
- [[Problems/3Sum triplets to zero\|3Sum triplets to zero]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
