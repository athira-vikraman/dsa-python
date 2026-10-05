---
tags:
  - concept
---

# Arrays

A shelf of numbered boxes, side by side, starting at **0**.

```
box number:    0      1      2      3      4
             ┌─────┬──────┬──────┬──────┬──────┐
             │  7  │  12  │  3   │  9   │  21  │
             └─────┴──────┴──────┴──────┴──────┘
```

## The superpower

Grabbing box `i` is **O(1)** — one jump, whether the shelf holds 5 boxes or 5
billion.

## The weakness

The boxes are nailed side by side with no gaps, so inserting at the front
makes **everyone shuffle**.

| Operation | Cost |
|---|---|
| `items[i]`, `len()`, `append()`, `pop()` | **O(1)** |
| `x in items`, `.index(x)`, `.remove(x)` | O(n) |
| `items.insert(0, x)`, `items.pop(0)` | **O(n)** ⚠️ |
| `items[a:b]` | O(b−a) — it **copies** |

**End cheap, front expensive.** Need a fast front? `collections.deque`.

Read: [[02_Arrays_And_Strings/notes/01_what_is_an_array|The full lesson]]
Related: [[Concepts/Strings|Strings]] · [[Concepts/Two pointers|Two pointers]]

Back to [[00 START HERE]]
