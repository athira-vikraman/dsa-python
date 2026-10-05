---
tags:
  - problem
  - sorting
---

# Insertion sort

> [!question] The question
> Sort the way you sort a hand of playing cards.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/In-place algorithms\|In-place algorithms]] |
| **Time** | `O(n²)` — [[Concepts/Quadratic time\|quadratic time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

The useful quadratic sort. On a nearly-sorted list it approaches O(n), because each card only moves a step or two. That is why Python's Timsort uses insertion sort on short runs inside its O(n log n) merge.

## The code

```python
def insertion_sort(items):
    for i in range(1, len(items)):
        card = items[i]
        j = i - 1
        while j >= 0 and items[j] > card:
            items[j + 1] = items[j]
            j = j - 1
        items[j + 1] = card
    return items
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Insertion sort**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Linear search\|Linear search]]
- [[Problems/Binary search\|Binary search]]
- [[Problems/Bubble sort\|Bubble sort]]
- [[Problems/Selection sort\|Selection sort]]
- [[Problems/Merge sort\|Merge sort]]
- [[Problems/Quick sort\|Quick sort]]
- [[Problems/Heap sort\|Heap sort]]
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
