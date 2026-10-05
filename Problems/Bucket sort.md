---
tags:
  - problem
  - sorting
---

# Bucket sort

> [!question] The question
> Spread values into a few buckets by size, sort each small bucket, then pour them out in order.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/Non-comparison sorting\|Non-comparison sorting]] |
| **Time** | `O(n + k) average` — [[Concepts/Non-comparison sorting\|non-comparison sorting]] |
| **Space** | `O(n)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

It is only fast if the values spread evenly. With five buckets and evenly scattered numbers, each bucket holds about n/5 items and sorting them is cheap. If every value lands in the same bucket you are just running the inner sort on the whole list, and the advantage vanishes.

## The code

```python
def bucket_sort(items):
    buckets = [[], [], [], [], []]
    biggest = max(items) + 1
    for value in items:
        index = value * 5 // biggest
        buckets[index].append(value)
    out = 0
    for bucket in buckets:
        bucket.sort()
        for value in bucket:
            items[out] = value
            out = out + 1
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Bucket sort**. Step through it once before you try writing it from memory.

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
- [[Problems/Radix sort\|Radix sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
