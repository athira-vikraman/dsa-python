---
tags:
  - problem
  - sliding-window
---

# Longest stretch no repeats

> [!question] The question
> How long is the longest run of letters with no repeats?

| | |
|---|---|
| **Technique** | [[Concepts/Sliding window\|Sliding window]] · [[Concepts/Strings\|Strings]] · [[Concepts/Hashing\|Hashing]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(k)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why is this O(n) with a loop inside a loop? Because left only ever moves forward, at most n times across the whole run. right moves n times, left moves n times: 2n steps, which is O(n).

## The code

```python
def longest_without_repeats(text):
    seen = set()
    left = 0
    best = 0
    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1
        seen.add(text[right])
        best = max(best, right - left + 1)
    return best
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Longest stretch, no repeats**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Shortest subarray with sum  target\|Shortest subarray with sum  target]]
- [[Problems/Longest with at most k different\|Longest with at most k different]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
