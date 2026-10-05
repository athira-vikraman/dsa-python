---
tags:
  - problem
  - sliding-window
---

# Max sum of k in a row

> [!question] The question
> What is the biggest sum of any k consecutive numbers?

| | |
|---|---|
| **Technique** | [[Concepts/Sliding window\|Sliding window]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

The one line to remember: window_sum += joiner - leaver. Re-adding the whole window every time is O(n×k); changing only the two numbers that moved makes it O(n), whatever k is.

## The code

```python
def max_sum_of_k(numbers, k):
    window_sum = sum(numbers[:k])
    best = window_sum
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        best = max(best, window_sum)
    return best
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Max sum of k in a row**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Average of every k days\|Average of every k days]]
- [[Problems/Most vowels in k letters\|Most vowels in k letters]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
