---
tags:
  - problem
  - two-pointers
---

# Container with most water

> [!question] The question
> Each number is a wall height. Pick two walls holding the most water between them.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why move the SHORTER wall? Water is limited by the shorter wall. Moving the taller one in can only make the width smaller and the height no better — so it can never help. Moving the shorter one is the only move that might. That reasoning turns O(n²) into O(n).

## The code

```python
def most_water(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        h = min(heights[left], heights[right])
        best = max(best, h * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Container with most water**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Reverse a list\|Reverse a list]]
- [[Problems/Valid palindrome\|Valid palindrome]]
- [[Problems/Two Sum sorted\|Two Sum sorted]]
- [[Problems/Squares of a sorted array\|Squares of a sorted array]]
- [[Problems/3Sum triplets to zero\|3Sum triplets to zero]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
