# Lesson 9 — The Big O Cheat Sheet

> Print this. Stick it near your desk. Revise it before every interview.

---

## The growth ranking (memorise this line)

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
 best ────────────────────────────────────────────────────────────► worst
```

---

## The four simplification rules

1. **Drop constants** — `O(3n)` → `O(n)`
2. **Drop lower terms** — `O(n² + n)` → `O(n²)`
3. **Sequential adds, nested multiplies** — "and then" = `+`, "for each" = `×`
4. **Different inputs, different letters** — `O(a · b)`, never `O(n²)`

---

## Spot the complexity by shape

| What the code looks like | Complexity |
|--------------------------|-----------|
| No loop; direct index/hash access | O(1) |
| Input halves each step (`i //= 2`, `i *= 2`) | O(log n) |
| One loop over the input | O(n) |
| Sort, or divide-and-conquer with a linear merge | O(n log n) |
| Two nested loops over the same input | O(n²) |
| Three nested loops | O(n³) |
| Recursion with 2 calls, input shrinks by 1 | O(2ⁿ) |
| Generating all permutations | O(n!) |

---

## Python built-ins (the ones that bite)

| Operation | Cost |
|-----------|------|
| `list[i]`, `len()`, `append()`, `pop()` | O(1) |
| `x in list`, `list.index(x)`, `remove()` | **O(n)** |
| `list.pop(0)`, `list.insert(0, x)` | **O(n)** |
| `list[a:b]` slice | O(b−a) — it copies |
| `sort()` / `sorted()` | O(n log n) |
| `x in dict`, `x in set`, `d[k]`, `s.add(x)` | **O(1)** |
| `str + str`, `s += x` in a loop | O(n) / **O(n²)** |
| `"".join(list)` | O(total length) |
| `deque.appendleft()` / `popleft()` | O(1) |
| `heappush` / `heappop` | O(log n) |
| `heapify` | O(n) |

---

## Classic algorithms

### Searching
| Algorithm | Time (avg) | Time (worst) | Space |
|-----------|-----------|--------------|-------|
| Linear search | O(n) | O(n) | O(1) |
| Binary search (sorted) | O(log n) | O(log n) | O(1) iterative |
| Hash table lookup | O(1) | O(n) | O(n) |

### Sorting
| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick sort | O(n log n) | O(n log n) | **O(n²)** | O(log n) | No |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Timsort** (Python) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

### Data structures
| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array / list | O(1) | O(n) | O(n) | O(n) |
| Stack (list) | O(n) | O(n) | O(1) | O(1) |
| Queue (deque) | O(n) | O(n) | O(1) | O(1) |
| Linked list | O(n) | O(n) | O(1)* | O(1)* |
| Hash table | — | O(1) | O(1) | O(1) |
| Binary search tree (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |
| Binary search tree (degenerate) | O(n) | O(n) | O(n) | O(n) |
| Heap | O(1) peek | O(n) | O(log n) | O(log n) |

\* once you already hold a pointer to the node

### Graph traversal (V vertices, E edges)
| Algorithm | Time | Space |
|-----------|------|-------|
| BFS / DFS | O(V + E) | O(V) |
| Dijkstra (binary heap) | O((V + E) log V) | O(V) |

---

## What's "good enough"? (by input size)

| n up to | Acceptable complexity |
|---------|----------------------|
| 10 | O(n!) |
| 20 | O(2ⁿ) |
| 500 | O(n³) |
| 5,000 | O(n²) |
| 1,000,000 | O(n log n) |
| 100,000,000 | O(n) or O(log n) |

Competitive programmers use this table to pick an approach *before* coding.
Assume roughly 10⁷–10⁸ simple operations per second in Python.

---

## The optimisation moves

| Problem | Move |
|---------|------|
| Nested-loop search | dict / set → O(n) |
| Repeated subproblems | memoize → O(n) |
| Sorted data, linear scan | binary search → O(log n) |
| Repeated min/max | heap → O(log n) |
| Front insert/remove | deque → O(1) |
| String building | `"".join()` |
| Counting | `collections.Counter` |
| Pairs in a sorted array | two pointers → O(n) |
| Contiguous subarray | sliding window → O(n) |

---

## The sentence to say in interviews

> "Let n be `<the input>`. This is **O(…) time** and **O(…) space** because
> `<reason>`. I could trade `<space>` for `<time>` by `<move>`."

---

Back to the [course index](../README.md)
