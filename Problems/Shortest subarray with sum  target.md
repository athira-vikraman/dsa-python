---
tags:
  - problem
  - sliding-window
---

# Shortest subarray with sum  target

> [!question] The question
> What is the shortest run of numbers that adds up to at least the target?

| | |
|---|---|
| **Technique** | [[Concepts/Sliding window\|Sliding window]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

This is the MIRROR of the longest problem, and the mirror is what trips people up. Longest: shrink while the window is BAD. Shortest: shrink while the window is GOOD, because something shorter might still reach the target. (Needs all-positive numbers.)

## The code

```python
def shortest_subarray(numbers, target):
    left = 0
    window_sum = 0
    best = len(numbers) + 1
    for right in range(len(numbers)):
        window_sum = window_sum + numbers[right]
        while window_sum >= target:
            length = right - left + 1
            if length < best:
                best = length
            window_sum = window_sum - numbers[left]
            left = left + 1
    if best == len(numbers) + 1:
        return 0
    return best
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Shortest subarray with sum ≥ target**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Longest stretch no repeats\|Longest stretch no repeats]]
- [[Problems/Longest with at most k different\|Longest with at most k different]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
