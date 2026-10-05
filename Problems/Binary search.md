---
tags:
  - problem
  - searching
---

# Binary search

> [!question] The question
> Find a value in a sorted list. 1,000,000 items in about 20 steps.

| | |
|---|---|
| **Technique** | [[Concepts/Searching\|Searching]] · [[Concepts/Divide and conquer\|Divide and conquer]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(log n)` — [[Concepts/Logarithmic time\|logarithmic time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why O(log n)? Every guess throws away half of what is left. Halving 1,000,000 down to 1 takes only 20 steps. The list must be sorted — that is what makes 'go left' or 'go right' a safe decision.

## The code

```python
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Binary search**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Linear search\|Linear search]]
- [[Problems/Bubble sort\|Bubble sort]]
- [[Problems/Selection sort\|Selection sort]]
- [[Problems/Insertion sort\|Insertion sort]]
- [[Problems/Merge sort\|Merge sort]]
- [[Problems/Quick sort\|Quick sort]]
- [[Problems/Heap sort\|Heap sort]]
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
