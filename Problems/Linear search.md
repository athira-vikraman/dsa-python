---
tags:
  - problem
  - searching
---

# Linear search

> [!question] The question
> Find the position of a value in an unsorted list.

| | |
|---|---|
| **Technique** | [[Concepts/Searching\|Searching]] · [[Concepts/Arrays\|Arrays]] |
| **Time** | `O(n)` — [[Concepts/Linear time\|linear time]] |
| **Space** | `O(1)` — [[Concepts/Constant time\|constant time]] |

## Why this technique

Why O(n)? The list is unsorted, so the value could be anywhere. You cannot know box 5 is not the one without opening it. Best case 1 box, worst case all n — and we always quote the worst case.

## The code

```python
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
```

## Watch it run

Open `visualizer.html`, go to **Run a problem**, and pick **Linear search**. Step through it once before you try writing it from memory.

## My notes

<!-- Did you get it first try? What tripped you up? Tag it #stuck. -->


## Same family

- [[Problems/Binary search\|Binary search]]
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
