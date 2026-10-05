---
tags:
  - problem
  - two-pointers
---

# Valid palindrome

> [!question] The question
> Does this word read the same backwards?

| | |
|---|---|
| **Technique** | [[Concepts/Two pointers\|Two pointers]] · [[Concepts/Strings\|Strings]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Worth knowing: word == word[::-1] is also O(n), and in Python it is actually faster in seconds because it runs in C. Two fingers win on space (O(1), no copy) and can quit on the first mismatch.

## The code

```python
def is_palindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Valid palindrome**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Reverse a list\|Reverse a list]]
- [[Problems/Two Sum sorted\|Two Sum sorted]]
- [[Problems/Squares of a sorted array\|Squares of a sorted array]]
- [[Problems/Container with most water\|Container with most water]]
- [[Problems/3Sum triplets to zero\|3Sum triplets to zero]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
