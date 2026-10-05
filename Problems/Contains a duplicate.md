---
tags:
  - problem
  - hashing
---

# Contains a duplicate

> [!question] The question
> Does any value appear more than once?

| | |
|---|---|
| **Technique** | [[Concepts/Hashing\|Hashing]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(n)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

The classic time-for-space trade. Comparing every pair is O(n²) time and O(1) space. A set makes it O(n) time and O(n) space. Usually a bargain — but say the trade out loud, because on a dataset bigger than memory the slow version is the one that runs.

## The code

```python
def has_duplicate(items):
    seen = set()
    for x in items:
        if x in seen:
            return True
        seen.add(x)
    return False
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Contains a duplicate?**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Two Sum unsorted\|Two Sum unsorted]]
- [[Problems/Are these anagrams\|Are these anagrams]]
- [[Problems/First non-repeating character\|First non-repeating character]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
