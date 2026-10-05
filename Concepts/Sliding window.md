---
tags:
  - technique
---

# Sliding window

A window of **neighbours** that slides along the data. Use it whenever the
answer is a *stretch* of items that sit next to each other — the words
**subarray**, **substring**, **consecutive**, **in a row**.

## Fixed size

The problem gives you `k`. Only two things change per slide:

```python
window_sum += items[i] - items[i - k]   # the joiner minus the leaver
```

Never re-add the middle. That one line turns O(n·k) into O(n).

## Growing size

The problem gives you a **rule** instead of a size. `right` grows the window;
`left` shrinks it while the rule is broken.

> **The mirror that catches everyone:**
> *Longest* → shrink while the window is **bad**.
> *Shortest* → shrink while the window is **good**, to try for shorter.

## Window size is `right - left + 1`

The `+ 1` catches everybody once. Boxes 2 to 4 is three boxes.

> ⚠️ If the items can be **scattered**, it is not a window problem. Windows
> are only ever neighbours.

Read: [[02_Arrays_And_Strings/notes/04_sliding_window|The full lesson]]
Related: [[Concepts/Two pointers|Two pointers]] · [[Concepts/Hashing|Hashing]]

Back to [[00 START HERE]]
