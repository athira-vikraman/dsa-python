# Lesson 7 — The Cost of Every Common Python Operation

> **Goal:** stop guessing. This is the lookup table you'll use for the rest of
> your DSA journey.

You cannot analyse your own code if you don't know what the built-ins cost.
`items.index(x)` looks like one innocent line — it's a hidden `O(n)` loop.

`n` = number of elements in the container.

---

## 7.1 `list`

| Operation | Complexity | Note |
|-----------|-----------|------|
| `items[i]` | **O(1)** | index access is direct |
| `items[i] = x` | O(1) | |
| `len(items)` | O(1) | length is stored, not counted |
| `items.append(x)` | O(1) amortized | see Lesson 6 |
| `items.pop()` | O(1) | from the END |
| `items.pop(0)` | **O(n)** | ⚠️ everything shifts left |
| `items.insert(0, x)` | **O(n)** | ⚠️ everything shifts right |
| `items.remove(x)` | O(n) | search + shift |
| `del items[i]` | O(n) | shift (O(1) if last) |
| `x in items` | **O(n)** | ⚠️ scans the whole list |
| `items.index(x)` | O(n) | hidden loop |
| `items.count(x)` | O(n) | |
| `items.sort()` | O(n log n) | Timsort, in place |
| `sorted(items)` | O(n log n) | returns a new list, O(n) space |
| `items.reverse()` | O(n) | in place, O(1) space |
| `items[a:b]` (slice) | O(b−a) | ⚠️ copies! slicing in a loop is a trap |
| `items + other` | O(n + m) | builds a new list |
| `min()`, `max()`, `sum()` | O(n) | |
| `items.copy()` / `items[:]` | O(n) | |

---

## 7.2 `dict` — your main tool for turning O(n²) into O(n)

| Operation | Average | Worst | Note |
|-----------|---------|-------|------|
| `d[key]` | **O(1)** | O(n) | hashing; worst case needs pathological collisions |
| `d[key] = value` | O(1) | O(n) | |
| `key in d` | **O(1)** | O(n) | the single most useful fact in DSA |
| `del d[key]` | O(1) | O(n) | |
| `d.get(key)` | O(1) | O(n) | |
| `len(d)` | O(1) | O(1) | |
| `d.keys()` / `.values()` / `.items()` | O(1) to create | — | O(n) to iterate |
| iterate over `d` | O(n) | O(n) | |

In practice treat dict lookups as **O(1)**. The worst case essentially never
happens with normal keys.

---

## 7.3 `set` — same magic, no values

| Operation | Average | Note |
|-----------|---------|------|
| `x in s` | **O(1)** | vs O(n) for a list — this is THE optimisation |
| `s.add(x)` | O(1) | |
| `s.remove(x)` / `.discard(x)` | O(1) | |
| `s1 \| s2` (union) | O(len(s1) + len(s2)) | |
| `s1 & s2` (intersection) | O(min(len(s1), len(s2))) | |
| `s1 - s2` (difference) | O(len(s1)) | |

> 🔑 **The one-line optimisation you will use forever:**
> if you are checking membership inside a loop, convert the list to a set first.
> `O(n²)` becomes `O(n)`.

```python
# SLOW: O(n * m)
common = [x for x in list_a if x in list_b]

# FAST: O(n + m)
set_b = set(list_b)
common = [x for x in list_a if x in set_b]
```

---

## 7.4 `str` (strings are immutable — this matters)

| Operation | Complexity | Note |
|-----------|-----------|------|
| `s[i]` | O(1) | |
| `len(s)` | O(1) | |
| `s1 + s2` | O(n + m) | ⚠️ builds a whole new string |
| `s += x` in a loop | **O(n²)** | ⚠️ classic beginner trap |
| `"".join(list_of_strings)` | **O(total length)** | ✅ the right way |
| `sub in s` | O(n · m) worst | substring search |
| `s.split()`, `.strip()`, `.replace()` | O(n) | |
| `s.upper()` / `.lower()` | O(n) | new string each time |

```python
# BAD — O(n²): each += copies the whole string so far
result = ""
for word in words:
    result += word

# GOOD — O(n)
result = "".join(words)
```

> ⚠️ **A caveat worth knowing.** CPython has a private optimisation that
> mutates a string in place when nothing else references it, which can make
> the bad version *look* linear in a micro-benchmark. It is an implementation
> detail: it disappears in PyPy, and the moment any other variable holds a
> reference to the string. `code/08_python_builtin_costs.py` measures both the
> optimised and the honest version so you can see the real O(n²). Always use
> `join()`.

---

## 7.5 `collections.deque` — the double-ended queue

| Operation | Complexity |
|-----------|-----------|
| `append(x)` / `pop()` | O(1) |
| `appendleft(x)` / `popleft()` | **O(1)** ← the reason it exists |
| `d[i]` (middle index) | O(n) ⚠️ |

Use `deque` for queues and BFS. Use `list` for stacks and random access.

---

## 7.6 `heapq` (priority queue on a list)

| Operation | Complexity |
|-----------|-----------|
| `heapq.heappush(h, x)` | O(log n) |
| `heapq.heappop(h)` | O(log n) |
| `h[0]` (peek smallest) | O(1) |
| `heapq.heapify(list)` | **O(n)** (not O(n log n)!) |
| `heapq.nsmallest(k, it)` | O(n log k) |

---

## 7.7 The traps, collected

Each of these looks like one cheap line and is not:

1. `if x in my_list:` inside a loop → **O(n²)**. Use a set.
2. `my_list.pop(0)` in a loop → **O(n²)**. Use `deque.popleft()`.
3. `my_string += piece` in a loop → **O(n²)**. Use `"".join()`.
4. `my_list.insert(0, x)` in a loop → **O(n²)**. Use `deque.appendleft()`.
5. Slicing inside a loop (`items[i:]`) → each slice is **O(n)**. Use indices.
6. `sorted()` inside a loop → **O(n² log n)**. Sort once, outside.
7. Calling `len()` — this one is fine, it's O(1) in Python. Don't over-optimise it.

`code/08_python_builtin_costs.py` measures several of these live so you can see
the curve with your own eyes.

---

## Check yourself

1. `x in my_list` vs `x in my_set` — complexities?
2. Why is building a string with `+=` in a loop O(n²)?
3. You need a queue. `list` or `deque`? Why?
4. Is `heapq.heapify()` O(n) or O(n log n)?
5. What does `items[1:]` cost inside a loop that runs n times?

Next: [Lesson 8 — How to analyse any code, step by step](08_how_to_analyze_any_code.md)
