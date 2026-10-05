---
tags:
  - problem
  - sorting
---

# Bubble sort

> [!question] The question
> Sort by repeatedly swapping neighbours that are in the wrong order.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/In-place algorithms\|In-place algorithms]] |
| **Time** | `O(n²)` — [[Concepts/Quadratic time\|quadratic time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why O(n²)? Each pass bubbles one value to its final place, and there are n passes. The early exit makes an already-sorted list O(n) — that is its one redeeming feature. Never use it in real code; sort() is O(n log n).

## The code

```python
def bubble_sort(items):
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Bubble sort**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Linear search\|Linear search]]
- [[Problems/Binary search\|Binary search]]
- [[Problems/Selection sort\|Selection sort]]
- [[Problems/Insertion sort\|Insertion sort]]
- [[Problems/Merge sort\|Merge sort]]
- [[Problems/Quick sort\|Quick sort]]
- [[Problems/Heap sort\|Heap sort]]
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
