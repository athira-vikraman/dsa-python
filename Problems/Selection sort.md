---
tags:
  - problem
  - sorting
---

# Selection sort

> [!question] The question
> Repeatedly find the smallest remaining value and put it next.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/In-place algorithms\|In-place algorithms]] |
| **Time** | `O(n²)` — [[Concepts/Quadratic time\|quadratic time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Always O(n²), even on a sorted list — it has no early exit, because it cannot know a value is the smallest without scanning the rest. In exchange it makes at most n swaps, which matters when writing is expensive.

## The code

```python
def selection_sort(items):
    n = len(items)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Selection sort**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Linear search\|Linear search]]
- [[Problems/Binary search\|Binary search]]
- [[Problems/Bubble sort\|Bubble sort]]
- [[Problems/Insertion sort\|Insertion sort]]
- [[Problems/Merge sort\|Merge sort]]
- [[Problems/Quick sort\|Quick sort]]
- [[Problems/Heap sort\|Heap sort]]
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
