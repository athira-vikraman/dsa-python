---
tags:
  - problem
  - two-pointers
---

# 3Sum triplets to zero

> [!question] The question
> Find three numbers that add up to zero.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/Sorting\|Sorting]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n²)` — [[Concepts/Quadratic time\|quadratic time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Today's lesson with one loop on top. Sort first (O(n log n)). Then fix the first number with a loop and run two pointers on the rest to find the other two. One loop × one linear scan = O(n²) — far better than the O(n³) of three nested loops.

## The code

```python
def three_sum(nums):
    nums.sort()
    found = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplet = (nums[i], nums[left], nums[right])
                found.append(triplet)
                left = left + 1
                right = right - 1
            elif total < 0:
                left = left + 1
            else:
                right = right - 1
    return found
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **3Sum (triplets to zero)**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Reverse a list\|Reverse a list]]
- [[Problems/Valid palindrome\|Valid palindrome]]
- [[Problems/Two Sum sorted\|Two Sum sorted]]
- [[Problems/Squares of a sorted array\|Squares of a sorted array]]
- [[Problems/Container with most water\|Container with most water]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
