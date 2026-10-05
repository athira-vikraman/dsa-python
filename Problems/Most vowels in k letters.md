---
tags:
  - problem
  - sliding-window
---

# Most vowels in k letters

> [!question] The question
> Which k consecutive letters contain the most vowels?

| | |
|---|---|
| **Technique** | [[Concepts/Sliding window\|Sliding window]] · [[Concepts/Strings\|Strings]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

A window does not have to hold a sum. Anything you can update with '+1 for the joiner, −1 for the leaver' can slide: a count, a total, a frequency table. That is the real pattern.

## The code

```python
def max_vowels(text, k):
    vowels = "aeiou"
    count = 0
    for letter in text[:k]:
        if letter in vowels:
            count = count + 1
    best = count
    for i in range(k, len(text)):
        if text[i] in vowels:
            count = count + 1
        if text[i - k] in vowels:
            count = count - 1
        best = max(best, count)
    return best
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Most vowels in k letters**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Max sum of k in a row\|Max sum of k in a row]]
- [[Problems/Average of every k days\|Average of every k days]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
