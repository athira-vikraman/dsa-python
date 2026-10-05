---
tags:
  - problem
  - sorting
---

# Counting sort

> [!question] The question
> Sort small whole numbers by tallying them instead of comparing them.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/Non-comparison sorting\|Non-comparison sorting]] |
| **Time** | `O(n + k)` — [[Concepts/Non-comparison sorting\|non-comparison sorting]] |
| **Space** | `O(k)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

This beats O(n log n) — how? The n log n limit only applies to sorts that work by comparing pairs. This one never compares anything; it just counts. The catch is k, the size of the number range: counting sort on values up to a million would need a million counters, so it only wins when the numbers are small and tightly packed.

## The code

```python
def counting_sort(items):
    biggest = max(items)
    counts = [0] * (biggest + 1)
    for value in items:
        counts[value] = counts[value] + 1
    out = 0
    for value in range(len(counts)):
        for _ in range(counts[value]):
            items[out] = value
            out = out + 1
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Counting sort**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Linear search\|Linear search]]
- [[Problems/Binary search\|Binary search]]
- [[Problems/Bubble sort\|Bubble sort]]
- [[Problems/Selection sort\|Selection sort]]
- [[Problems/Insertion sort\|Insertion sort]]
- [[Problems/Merge sort\|Merge sort]]
- [[Problems/Quick sort\|Quick sort]]
- [[Problems/Heap sort\|Heap sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
