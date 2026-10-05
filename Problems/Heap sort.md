---
tags:
  - problem
  - sorting
---

# Heap sort

> [!question] The question
> Turn the list into a heap so the biggest value is always on top, then pull it off one at a time.

| | |
|---|---|
| **Technique** | [[Concepts/Sorting\|Sorting]] · [[Concepts/In-place algorithms\|In-place algorithms]] |
| **Time** | `O(n log n)` — [[Concepts/Linearithmic time\|linearithmic time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

The array IS the tree. Box 0 is the top. The children of box p live at boxes 2p+1 and 2p+2. No pointers, no nodes — just arithmetic. That is why heap sort needs no extra memory, unlike merge sort's O(n).

## The code

```python
def heap_sort(items):
    n = len(items)
    for parent in range(n // 2 - 1, -1, -1):
        sift_down(items, parent, n)
    for end in range(n - 1, 0, -1):
        items[0], items[end] = items[end], items[0]
        sift_down(items, 0, end)
    return items

def sift_down(items, parent, size):
    big = parent
    left = 2 * parent + 1
    right = 2 * parent + 2
    if left < size and items[left] > items[big]:
        big = left
    if right < size and items[right] > items[big]:
        big = right
    if big != parent:
        items[parent], items[big] = items[big], items[parent]
        sift_down(items, big, size)
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Heap sort**. Step through it once before you try writing it from memory.

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
- [[Problems/Counting sort\|Counting sort]]
- [[Problems/Radix sort\|Radix sort]]
- [[Problems/Bucket sort\|Bucket sort]]

Back to [[Problems/_All problems\|all problems]] · [[00 START HERE]]
