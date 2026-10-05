---
tags:
  - problem
  - sorting
---

# Radix sort

> [!question] The question
> Sort numbers by looking at one digit at a time: ones, then tens, then hundreds.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/Non-comparison sorting\|Non-comparison sorting]] |
| **Time** | `O(d × n)` — [[Concepts/Non-comparison sorting\|non-comparison sorting]] |
| **Space** | `O(n)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

Why start with the LAST digit? Because each pass keeps the order from the pass before it. Sorting by ones first, then tens, means two numbers with the same tens digit are still correctly ordered by their ones. Sorting from the left instead would wreck that.

## The code

```python
def radix_sort(items):
    place = 1
    while max(items) // place > 0:
        buckets = [[] for _ in range(10)]
        for value in items:
            digit = (value // place) % 10
            buckets[digit].append(value)
        out = 0
        for bucket in buckets:
            for value in bucket:
                items[out] = value
                out = out + 1
        place = place * 10
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Radix sort**. Step through it once before you try writing it from memory.

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
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
