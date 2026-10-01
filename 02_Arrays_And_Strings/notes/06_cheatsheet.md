# Lesson 6 — Arrays & Strings Cheat Sheet

> Print it. Stick it next to the Big O cheat sheet.

---

## Array prices (Python `list`)

| Operation | Price |
|---|---|
| `items[i]`, `items[i] = x`, `len(items)` | **O(1)** |
| `items.append(x)`, `items.pop()` | **O(1)** |
| `items.insert(0, x)`, `items.pop(0)` | **O(n)** ⚠️ |
| `x in items`, `items.index(x)`, `items.remove(x)` | O(n) |
| `items[a:b]` (slice) | O(b−a) — **copies** |
| `items.sort()` / `sorted(items)` | O(n log n) |
| `items.reverse()` | O(n), O(1) space |
| `min()`, `max()`, `sum()` | O(n) |

**End = cheap. Front = expensive.** Need a fast front? `collections.deque`.

---

## String prices

| Operation | Price |
|---|---|
| `word[i]`, `len(word)` | **O(1)** |
| `word[a:b]` | O(b−a) — copies |
| `c in word`, `word.find(c)` | O(n) |
| `.lower()`, `.upper()`, `.strip()`, `.split()`, `.replace()` | O(n) |
| `word1 + word2` | O(n+m) |
| `word += x` **in a loop** | **O(n²)** ❌ |
| `"".join(list)` | **O(n)** ✅ |

**Strings are frozen (immutable).** To edit letters:
`list(word)` → change → `"".join(letters)`

---

## The four templates

```python
# 1. TWO POINTERS - opposite ends  (pairs, palindromes, sorted data)
left, right = 0, len(items) - 1
while left < right:
    if <condition>: left += 1
    else:           right -= 1

# 2. TWO POINTERS - reader & writer  (filter in place)
writer = 0
for reader in range(len(items)):
    if <keep it?>:
        items[writer] = items[reader]
        writer += 1

# 3. SLIDING WINDOW - fixed size k
window_sum = sum(items[:k])
best = window_sum
for i in range(k, len(items)):
    window_sum += items[i] - items[i - k]      # joiner - leaver
    best = max(best, window_sum)

# 4. SLIDING WINDOW - growing
left = best = 0
for right in range(len(items)):
    # add items[right]
    while <rule broken>:
        # remove items[left]
        left += 1
    best = max(best, right - left + 1)         # mind the +1
```

---

## Choosing, in one block

```
STRETCH of neighbours?      -> sliding window  (size given = fixed,
                                                rule given = growing)
PAIR + sorted?              -> two pointers from the ends
PAIR + unsorted?            -> a set
Filter / remove IN PLACE?   -> reader & writer
"Seen this before?"         -> set or dict
Count of each thing?        -> dict / collections.Counter
Nothing fits?               -> one plain loop
```

**"O(1) extra space" in the question = two pointers.**

---

## Classic problems and their tools

| Problem | Tool | Time | Space |
|---|---|---|---|
| Reverse an array | two pointers (ends) | O(n) | O(1) |
| Valid palindrome | two pointers (ends) | O(n) | O(1) |
| Two Sum (sorted) | two pointers (ends) | O(n) | O(1) |
| Two Sum (unsorted) | set | O(n) | O(n) |
| 3Sum | sort + loop + two pointers | O(n²) | O(1) |
| Move zeros to the end | reader & writer | O(n) | O(1) |
| Remove duplicates (sorted) | reader & writer | O(n) | O(1) |
| Merge two sorted arrays | one pointer each | O(n+m) | O(n+m) |
| Max sum of k in a row | fixed window | O(n) | O(1) |
| Longest substring, no repeats | growing window + set | O(n) | O(k) |
| Smallest subarray, sum ≥ X | growing window | O(n) | O(1) |
| Anagram check | dict counting | O(n) | O(k) |
| First unique character | dict counting | O(n) | O(k) |
| Contains a duplicate | set | O(n) | O(n) |

---

## The three tests that catch most bugs

Before you say "done", run your function on:

1. **Empty** — `[]` or `""`
2. **One item** — `[5]` or `"a"`
3. **The edge** — window bigger than the list, target not found, all items
   the same

---

## Off-by-one survival kit

- Last index is `len(items) - 1`, **not** `len(items)`
- `items[a:b]` **excludes** `b`
- Window size is `right - left + 1`
- `range(len(items))` gives `0 .. len-1` ✅
- A pair loop is `for j in range(i + 1, n)` — start *after* i

---

Back to the [topic index](../README.md) · [Big O cheat sheet](../../01_Big_O_Notation/notes/09_cheatsheet.md)
