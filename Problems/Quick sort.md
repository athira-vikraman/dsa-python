---
tags:
  - problem
  - sorting
---

# Quick sort

> [!question] The question
> Pick a pivot, push everything smaller to its left, then repeat on each side.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/Divide and conquer\|Divide and conquer]] · [[Concepts/Recursion\|Recursion]] · [[Concepts/In-place algorithms\|In-place algorithms]] |
| **Time** | `O(n log n) average` — [[Concepts/Linearithmic time\|linearithmic time]] |
| **Space** | `O(log n)` — [[Concepts/Logarithmic time\|logarithmic time]] |

## Why this technique

Why is the worst case O(n²)? If the pivot is always the biggest or smallest value, each round shrinks the job by only one instead of halving it. Picking a random or middle pivot makes that almost impossible, which is why quick sort is usually the fastest sort in practice despite the scary worst case.

## The code

```python
def quick_sort(items, low, high):
    if low >= high:
        return
    pivot = items[high]
    i = low
    for j in range(low, high):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            i = i + 1
    items[i], items[high] = items[high], items[i]
    quick_sort(items, low, i - 1)
    quick_sort(items, i + 1, high)
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Quick sort**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Linear search\|Linear search]]
- [[Problems/Binary search\|Binary search]]
- [[Problems/Bubble sort\|Bubble sort]]
- [[Problems/Selection sort\|Selection sort]]
- [[Problems/Insertion sort\|Insertion sort]]
- [[Problems/Merge sort\|Merge sort]]
- [[Problems/Heap sort\|Heap sort]]
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
