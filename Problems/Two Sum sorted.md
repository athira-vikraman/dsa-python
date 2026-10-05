---
tags:
  - problem
  - two-pointers
---

# Two Sum sorted

> [!question] The question
> In a sorted list, find two numbers that add up to a target.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why sorted matters: moving L right can only make the sum bigger, and moving R left can only make it smaller. In an unsorted list that reasoning is worthless — use a set instead (see Two Sum, unsorted).

## The code

```python
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return (numbers[left], numbers[right])
        elif total < target:
            left += 1
        else:
            right -= 1
    return None
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Two Sum (sorted)**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Reverse a list\|Reverse a list]]
- [[Problems/Valid palindrome\|Valid palindrome]]
- [[Problems/Squares of a sorted array\|Squares of a sorted array]]
- [[Problems/Container with most water\|Container with most water]]
- [[Problems/3Sum triplets to zero\|3Sum triplets to zero]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
