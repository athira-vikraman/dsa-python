---
tags:
  - problem
  - two-pointers
---

# Squares of a sorted array

> [!question] The question
> Square every number in a sorted list that may contain negatives, and keep the result sorted.

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(n)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

The insight: the biggest square always hides at one of the two ends, because -4 squared (16) beats 3 squared (9). So fill the answer from the BACK, taking the bigger end each time. Squaring then sorting would be O(n log n); this is O(n).

## The code

```python
def sorted_squares(numbers):
    result = [0] * len(numbers)
    left, right = 0, len(numbers) - 1
    for pos in range(len(numbers) - 1, -1, -1):
        if numbers[left]**2 > numbers[right]**2:
            result[pos] = numbers[left]**2
            left += 1
        else:
            result[pos] = numbers[right]**2
            right -= 1
    return result
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Squares of a sorted array**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Reverse a list\|Reverse a list]]
- [[Problems/Valid palindrome\|Valid palindrome]]
- [[Problems/Two Sum sorted\|Two Sum sorted]]
- [[Problems/Container with most water\|Container with most water]]
- [[Problems/3Sum triplets to zero\|3Sum triplets to zero]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
