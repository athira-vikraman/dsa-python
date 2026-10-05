---
tags:
  - problem
  - hashing
---

# First non-repeating character

> [!question] The question
> Which is the first character that appears exactly once?

| | |
|---|---|
| **Technique** | [[Concepts/Hashing\|Hashing]] · [[Concepts/Strings\|Strings]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(k)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Two passes are still O(n). You cannot know a letter is unique until you have seen the whole word, so pass one counts and pass two finds the first count of 1. n + n = 2n = O(n). Only nested loops multiply.

## The code

```python
def first_unique_char(text):
    counts = {}
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    for i, c in enumerate(text):
        if counts[c] == 1:
            return i
    return -1
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **First non-repeating character**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Two Sum unsorted\|Two Sum unsorted]]
- [[Problems/Contains a duplicate\|Contains a duplicate]]
- [[Problems/Are these anagrams\|Are these anagrams]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
