---
tags:
  - problem
  - sorting
---

# Merge sort

> [!question] The question
> Split the list in half, sort each half, then merge them back together.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/Divide and conquer\|Divide and conquer]] · [[Concepts/Recursion\|Recursion]] |
| **Time** | `O(n log n)` — [[Concepts/Linearithmic time\|linearithmic time]] |
| **Space** | `O(n)` — [[Concepts/Linear time\|linear time]] |

## Why this technique

Why O(n log n)? Splitting in half takes log n levels to reach single boxes. At every level, merging touches all n values once. log n levels × n work = n log n. The O(n) space is the temporary buffer the merge needs.

## The code

```python
def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def merge(left, right):
    out = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i = i + 1
        else:
            out.append(right[j])
            j = j + 1
    while i < len(left):
        out.append(left[i])
        i = i + 1
    while j < len(right):
        out.append(right[j])
        j = j + 1
    return out
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Merge sort**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Linear search\|Linear search]]
- [[Problems/Binary search\|Binary search]]
- [[Problems/Bubble sort\|Bubble sort]]
- [[Problems/Selection sort\|Selection sort]]
- [[Problems/Insertion sort\|Insertion sort]]
- [[Problems/Quick sort\|Quick sort]]
- [[Problems/Heap sort\|Heap sort]]
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
