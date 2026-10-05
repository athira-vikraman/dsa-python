---
tags:
  - problem
  - sliding-window
---

# Average of every k days

> [!question] The question
> Give the running average of every k consecutive values.

| | |
|---|---|
| **Technique** | [[Concepts/Sliding window\|Sliding window]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(n)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

Same slide, one division. This is the moving average every dashboard draws. The O(n) space is the output list; the window itself still only needs one running total.

## The code

```python
def averages_of_k(numbers, k):
    result = []
    window_sum = sum(numbers[:k])
    result.append(window_sum / k)
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        result.append(window_sum / k)
    return result
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Average of every k days**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Max sum of k in a row\|Max sum of k in a row]]
- [[Problems/Most vowels in k letters\|Most vowels in k letters]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
