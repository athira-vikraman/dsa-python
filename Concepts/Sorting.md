---
tags:
  - technique
---

# Sorting

Putting things in order — and the clearest Big O lesson there is, because the
same job has nine solutions ranging from O(n²) to O(n + k).

## Comparison sorts

They work by comparing pairs, so **O(n log n) is their floor**.

| Sort | Average | Space | Use it when |
|---|---|---|---|
| [[Problems/Bubble sort\|Bubble sort]] | O(n²) | O(1) | never, it is here to read |
| [[Problems/Selection sort\|Selection sort]] | O(n²) | O(1) | writing is expensive |
| [[Problems/Insertion sort\|Insertion sort]] | O(n²) | O(1) | small or nearly sorted |
| [[Problems/Merge sort\|Merge sort]] | O(n log n) | O(n) | you need a guarantee |
| [[Problems/Quick sort\|Quick sort]] | O(n log n) | O(log n) | general purpose |
| [[Problems/Heap sort\|Heap sort]] | O(n log n) | O(1) | guarantee **and** no spare memory |

## Non-comparison sorts

See [[Concepts/Non-comparison sorting|Non-comparison sorting]].

## In real code

Use `sorted()`. It is Timsort, it is O(n log n), it is written in C, and it
beats everything you will write by hand.

Run `01_Big_O_Notation/code/11_sorting_algorithms.py` to watch all nine race.

Related: [[Concepts/Linearithmic time|Linearithmic time]] · [[Concepts/Divide and conquer|Divide and conquer]]

Back to [[00 START HERE]]
