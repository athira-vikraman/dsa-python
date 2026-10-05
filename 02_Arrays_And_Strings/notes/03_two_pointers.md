# Lesson 3 — The Two Pointers Trick

> This is the first real **technique** in your DSA journey. It turns slow
> code into fast code, and it is genuinely easy once you see the picture.

---

## 1. First, what is a "pointer"?

Scary word. Simple thing.

> A **pointer** is just a variable that holds a **box number**.

That's it. If `left = 0`, we say "the left pointer is pointing at box 0".
It's like putting your finger on a box.

```python
items = [10, 20, 30, 40, 50]
left = 0        # my left finger is on box 0
right = 4       # my right finger is on box 4

items[left]     # 10
items[right]    # 50
```

**Two pointers** = **two fingers** on the shelf. That's the whole idea.

---

## 2. The problem it solves

Let's reverse a list: `[1, 2, 3, 4, 5]` → `[5, 4, 3, 2, 1]`.

A beginner might build a brand-new list. That uses extra memory.

Instead, put **one finger at each end** and **swap** what they're pointing
at. Then move both fingers one step inward. Repeat until they meet.

```
Start:    [1, 2, 3, 4, 5]
           ↑           ↑
          left       right        swap 1 and 5

Step 1:   [5, 2, 3, 4, 1]
              ↑     ↑
            left  right           swap 2 and 4

Step 2:   [5, 4, 3, 2, 1]
                 ↑
            they met - STOP
```

Done! Here's the code:

```python
def reverse(items):
    left = 0
    right = len(items) - 1

    while left < right:                   # keep going until they meet
        items[left], items[right] = items[right], items[left]   # swap
        left = left + 1                   # left finger moves right
        right = right - 1                 # right finger moves left

    return items
```

- **Time: O(n)** — each finger walks halfway, so n/2 swaps. Drop the ½ → O(n).
- **Space: O(1)** — just two number variables. No new list!

That's two pointers. You already understand it.

---

## 3. Shape 1: fingers at opposite ends, walking toward each other

This is the shape you just saw. Use it when the answer involves **a pair,
one from each end**.

```
 [ a, b, c, d, e, f ]
   →                ←
  left           right
```

### Example: is this word a palindrome?

A palindrome reads the same backwards: **madam**, **racecar**, **level**.

Picture it: put a finger on each end. The letters under your fingers must
**match**. If they do, step inward and check again.

```
m a d a m
↑       ↑     'm' == 'm' ✅  step inward
  ↑   ↑       'a' == 'a' ✅  step inward
    ↑         met in the middle - it's a palindrome!
```

```python
def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False               # mismatch! stop immediately
        left += 1
        right -= 1

    return True                        # never found a mismatch
```

**Time O(n), Space O(1).**

> **Honest comparison.** `word == word[::-1]` also works, and is also O(n)
> time. The two-pointer version wins on **space** (O(1) vs O(n)) and can
> **quit early** on the first mismatch.
>
> But here's the twist, and you should know it: on a real palindrome,
> `word[::-1]` is about **50× FASTER in actual seconds**, because slicing
> and `==` run as compiled C loops while our two-pointer loop is interpreted
> Python. Same Big O, very different constant factor.
>
> So neither is simply "better":
> - Want the fastest Python? Use `word == word[::-1]`.
> - Need O(1) space, or an early exit on bad input? Use two pointers.
>
> `code/07_choosing_the_technique.py` measures both so you can see it.
> This is Big O being honest about its own blind spot: it ignores
> constants, and sometimes the constant is what matters.

### Example: find two numbers that add to a target (in a SORTED list)

```python
numbers = [1, 3, 5, 7, 9, 11]
target = 14
```

The slow way is to test every pair — that's two nested loops, **O(n²)**.

The clever way uses the fact that the list is **sorted**. Put a finger at
each end and look at the sum:

```
[1, 3, 5, 7, 9, 11]   1 + 11 = 12. Too SMALL. I need a bigger number...
 ↑              ↑     ...so move the LEFT finger right.

[1, 3, 5, 7, 9, 11]   3 + 11 = 14. FOUND IT! ✅
    ↑           ↑
```

Why does this work? Because the list is sorted:
- Sum too **small**? The only way to get bigger is to **move left finger right**.
- Sum too **big**? The only way to get smaller is to **move right finger left**.

Every step throws away a possibility you'll never need again.

```python
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return (numbers[left], numbers[right])    # found!
        elif total < target:
            left += 1          # too small -> need a bigger number
        else:
            right -= 1         # too big -> need a smaller number

    return None
```

**O(n) time, O(1) space** — down from O(n²). That's the win.

> ⚠️ This only works because the list is **sorted**. Two pointers at
> opposite ends almost always needs sorted data. If it isn't sorted, either
> sort it first (O(n log n)) or use a set instead.

---

## 4. Shape 2: both fingers walking the same way

Sometimes both fingers start at the left and walk right — but at
**different speeds**. One finger **reads**, the other finger **writes**.

```
 [ a, b, c, d, e, f ]
   →  →
  writer reader
```

### Example: move all the zeros to the end

`[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`

Think of it as two jobs:
- The **reader** finger looks at every box, one by one.
- The **writer** finger only moves when it has placed a non-zero number.

```
[0, 1, 0, 3, 12]   reader sees 0  -> skip it, writer stays
 W
 R

[1, 1, 0, 3, 12]   reader sees 1  -> write it at W, both move
 W→
    R→

[1, 3, 0, 3, 12]   reader sees 3  -> write it at W, both move
    W→
          R→

[1, 3, 12, 3, 12]  reader sees 12 -> write it at W, both move

Now fill the rest with zeros:
[1, 3, 12, 0, 0]  ✅
```

```python
def move_zeros_to_end(items):
    writer = 0

    for reader in range(len(items)):        # reader looks at every box
        if items[reader] != 0:
            items[writer] = items[reader]   # writer keeps the good stuff
            writer += 1                     # writer only moves on a hit

    while writer < len(items):              # pad the rest with zeros
        items[writer] = 0
        writer += 1

    return items
```

**O(n) time, O(1) space.** One pass, no new list.

> 🧠 **The reader/writer picture is worth memorising.** Any time a problem
> says *"remove"*, *"keep only"*, or *"squash duplicates"* **in place**,
> this is your shape.

### Example: remove duplicates from a sorted list

`[1, 1, 2, 2, 2, 3]` → `[1, 2, 3]` (first 3 boxes)

```python
def remove_duplicates_sorted(items):
    if not items:
        return 0

    writer = 1                                  # box 0 is always a keeper
    for reader in range(1, len(items)):
        if items[reader] != items[writer - 1]:  # a new value?
            items[writer] = items[reader]
            writer += 1

    return writer          # how many unique items are at the front
```

---

## 5. How to spot a two-pointer problem

Reach for two pointers when you see these words:

| The problem says... | Shape to use |
|---|---|
| "palindrome" | opposite ends |
| "reverse" | opposite ends |
| "pair that adds to X" + **sorted** | opposite ends |
| "closest pair" + **sorted** | opposite ends |
| "remove / keep only" + **in place** | reader & writer |
| "move all the X to the end" | reader & writer |
| "squash duplicates" + **sorted** | reader & writer |
| "merge two sorted lists" | one finger per list |

And the giveaway hint: **the problem says "O(1) extra space"** or
**"do it in place"**. That's practically an instruction to use two pointers.

---

## 6. Remember this

```
A pointer = a variable holding a box number = your finger.

SHAPE 1: fingers at both ends, walking inward
         while left < right: ... left += 1 ... right -= 1
         -> palindromes, reversing, pair-sums in SORTED lists

SHAPE 2: both fingers going right, at different speeds
         reader looks at everything, writer keeps the good stuff
         -> removing, filtering, squashing - IN PLACE

Both are O(n) time and O(1) space. They replace nested loops - O(n^2).
```

---

## Your turn

1. In `reverse`, why is the loop `while left < right` and not
   `while left != right`?
2. Why does `two_sum_sorted` need a sorted list?
3. `[0, 0, 1]` — trace `move_zeros_to_end` and say where the writer ends up.
4. Is "racecar" a palindrome? How many comparisons does the two-pointer
   version make?
5. Which shape would you use for "remove all the 5s from this list, in
   place"?

### Answers

1. Both work for an even-length list, but for an **odd**-length list the two
   fingers land on the **same middle box**. `left != right` would be False...
   actually it would stop correctly too — but `left < right` is safer,
   because if the fingers ever step *past* each other, `!=` would keep
   looping forever. `<` always stops. Use `<`.
2. Because the decision "move left for a bigger sum" only makes sense if the
   numbers to the right are bigger. In an unsorted list, moving a finger
   tells you nothing.
3. Reader sees 0 (skip), 0 (skip), 1 (write at box 0, writer → 1). Then the
   padding loop fills boxes 1 and 2 with zeros → `[1, 0, 0]`. The writer
   ends at 3 (past the end).
4. Yes. `r`↔`r`, `a`↔`a`, `c`↔`c`, then the fingers meet at the middle `e`.
   **3 comparisons** for a 7-letter word — about n/2.
5. Reader & writer. The reader checks every box; the writer only keeps the
   values that aren't 5.

Next: [Lesson 4 — The sliding window](04_sliding_window.md)

---

## Related concepts

[[Concepts/Two pointers|Two pointers]] · [[Concepts/In-place algorithms|In-place algorithms]] · [[Concepts/Arrays|Arrays]]

See also [[Problems/_All problems|all 31 problems]] · [[00 START HERE]]
