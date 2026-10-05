---
tags:
  - problem
  - sliding-window
---

# Longest with at most k different

> [!question] The question
> How long is the longest run containing at most k different letters?

| | |
|---|---|
| **Technique** | [[Concepts/Sliding window\|Sliding window]] · [[Concepts/Strings\|Strings]] · [[Concepts/Hashing\|Hashing]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(k)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why a dict and not a set? A set only answers 'is it in there?'. When a letter leaves the window you need to know whether that was its last copy — which means counting. Drop the key only when its count hits zero.

## The code

```python
def longest_k_distinct(text, k):
    counts = {}
    left = 0
    best = 0
    for right in range(len(text)):
        letter = text[right]
        counts[letter] = counts.get(letter, 0) + 1
        while len(counts) > k:
            leaving = text[left]
            counts[leaving] = counts[leaving] - 1
            if counts[leaving] == 0:
                del counts[leaving]
            left = left + 1
        best = max(best, right - left + 1)
    return best
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Longest with at most k different**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Longest stretch no repeats\|Longest stretch no repeats]]
- [[Problems/Shortest subarray with sum  target\|Shortest subarray with sum  target]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
