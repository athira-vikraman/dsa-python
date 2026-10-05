---
tags:
  - problem
  - hashing
---

# Are these anagrams

> [!question] The question
> Do two words use exactly the same letters?

| | |
|---|---|
| **Technique** | [[Concepts/Hashing\|Hashing]] · [[Concepts/Strings\|Strings]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(k)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why not just sort both? sorted(a) == sorted(b) is correct but O(n log n). Counting is O(n): add one for each letter of A, subtract one for each letter of B, and every count must land on zero.

## The code

```python
def is_anagram(a, b):
    if len(a) != len(b):
        return False
    counts = {}
    for c in a:
        counts[c] = counts.get(c, 0) + 1
    for c in b:
        if c not in counts:
            return False
        counts[c] = counts[c] - 1
        if counts[c] == 0:
            del counts[c]
    return len(counts) == 0
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Are these anagrams?**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Two Sum unsorted\|Two Sum unsorted]]
- [[Problems/Contains a duplicate\|Contains a duplicate]]
- [[Problems/First non-repeating character\|First non-repeating character]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
