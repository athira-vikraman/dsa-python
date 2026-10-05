---
tags:
  - problem
  - hashing
---

# Two Sum unsorted

> [!question] The question
> Find two numbers adding to a target in an unsorted list.

| | |
|---|---|
| **Technique** | [[Concepts/Hashing\|Hashing]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(n)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

The complement trick. As you scan, you already know which number would complete the pair: target − x. Asking a set 'have I seen that?' is O(1), so one pass is enough. This is the single most reused pattern in interviews.

## The code

```python
def two_sum(numbers, target):
    seen = set()
    for x in numbers:
        if target - x in seen:
            return (target - x, x)
        seen.add(x)
    return None
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Two Sum (unsorted)**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Contains a duplicate\|Contains a duplicate]]
- [[Problems/Are these anagrams\|Are these anagrams]]
- [[Problems/First non-repeating character\|First non-repeating character]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
