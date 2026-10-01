# Lesson 1 — What Is an Array?

> No jargon. Pictures first.

---

## 1. The shelf of boxes

Imagine a long shelf in your room. The shelf has boxes nailed to it, side by
side. Each box has a number painted on it.

```
box number:    0      1      2      3      4
             ┌─────┬──────┬──────┬──────┬──────┐
             │  7  │  12  │  3   │  9   │  21  │
             └─────┴──────┴──────┴──────┴──────┘
```

You put one toy in each box. That shelf is an **array**.

Three rules about the shelf:

1. The boxes sit **next to each other**. No gaps.
2. Each box has a **number** (we call it the *index*).
3. **Counting starts at 0.** The first box is box 0, not box 1.

That last rule feels strange for about a week, then it feels normal forever.

In Python, an array is called a **list**:

```python
toys = [7, 12, 3, 9, 21]
```

---

## 2. The magic of the shelf: you can grab any box instantly

Say I ask you: *"What's in box 3?"*

You don't start at box 0 and count along. You just **walk straight to box 3**
and look inside. One step. Done.

```python
toys = [7, 12, 3, 9, 21]
print(toys[3])        # 9
```

It doesn't matter if the shelf has 5 boxes or 5 million boxes — grabbing one
box takes the **same** time.

> Grabbing one box by its number = **O(1) time**. Instant.

This is the superpower of arrays. Remember it.

---

## 3. Counting from the back

Python lets you count backwards with minus signs:

```
index:        0      1      2      3      4
            ┌─────┬──────┬──────┬──────┬──────┐
            │  7  │  12  │  3   │  9   │  21  │
            └─────┴──────┴──────┴──────┴──────┘
from back:   -5     -4     -3     -2     -1
```

```python
toys[-1]      # 21  <- the last box
toys[-2]      # 9   <- second from the end
```

`toys[-1]` is the easiest way to say "the last one".

---

## 4. What is slow about a shelf?

Arrays are brilliant at one thing and bad at another. Here's the bad part.

### Finding something when you don't know the box number

*"Which box has the 9 in it?"*

Now you have no choice. You must open box 0... box 1... box 2... box 3. Found
it. You had to **look at every box** until you got lucky.

```python
toys.index(9)      # 3, but it had to search
9 in toys          # True, but it had to search
```

> Searching for a value = **O(n) time**. You might open every box.

### Squeezing a new box into the middle

The boxes are nailed side by side with **no gaps**. So if you want to add a
new box at the front, every single box has to **shuffle along** to make room.

```
Before:  [7, 12, 3, 9, 21]
Insert 5 at the front...
         everyone shifts right →
After:   [5, 7, 12, 3, 9, 21]
```

If there are a million boxes, a million boxes must shuffle.

```python
toys.insert(0, 5)     # O(n)  <- slow! everyone shifts
toys.pop(0)           # O(n)  <- slow! everyone shifts back
```

But adding at the **end** is easy — nobody has to move:

```python
toys.append(99)       # O(1)  <- fast!
toys.pop()            # O(1)  <- fast!
```

> **The shelf rule:** the end is cheap, the front is expensive.

---

## 5. The whole list of moves, with prices

| What you want to do | Code | Price |
|---|---|---|
| Look in box 3 | `items[3]` | **O(1)** cheap |
| Change box 3 | `items[3] = 50` | **O(1)** cheap |
| How many boxes? | `len(items)` | **O(1)** cheap |
| Add at the end | `items.append(x)` | **O(1)** cheap |
| Remove from the end | `items.pop()` | **O(1)** cheap |
| Look at every box | `for x in items:` | O(n) fair |
| Find a value | `x in items` | O(n) fair |
| Add at the front | `items.insert(0, x)` | **O(n)** expensive |
| Remove from the front | `items.pop(0)` | **O(n)** expensive |
| Sort the shelf | `items.sort()` | O(n log n) |
| Copy part of the shelf | `items[1:4]` | O(size of the piece) |

Keep this table nearby. Half of being good at arrays is just **not paying
expensive prices by accident**.

---

## 6. Slicing — taking a piece of the shelf

`items[start:stop]` makes a **new little shelf** from part of the old one.

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4]     # [20, 30, 40]   boxes 1, 2, 3
numbers[:3]      # [10, 20, 30]   from the start up to box 3
numbers[2:]      # [30, 40, 50]   from box 2 to the end
numbers[:]       # a full copy
numbers[::-1]    # [50, 40, 30, 20, 10]   backwards!
```

> ⚠️ **The stop number is NOT included.** `numbers[1:4]` gives you boxes
> 1, 2 and 3 — it stops *before* 4. Everyone gets this wrong at first.
> Read it as "from 1, up to but not including 4".

⚠️ **Slicing copies.** `numbers[1:4]` builds a brand-new list. That costs
time and memory. Slicing once is fine. Slicing **inside a loop** is how
beginners accidentally write slow code.

---

## 7. Walking along the shelf (three ways)

```python
fruits = ["apple", "banana", "cherry"]

# Way 1: I only need the things
for fruit in fruits:
    print(fruit)

# Way 2: I need the box numbers too
for i in range(len(fruits)):
    print(i, fruits[i])

# Way 3: I need both, nicely (the best way)
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

Use **way 1** when you just want the values. Use **way 3** when you need to
know *where* you are. (Two pointers and sliding windows need to know where
they are, so get comfortable with indexes now.)

---

## 8. Remember this

```
An array is a shelf of numbered boxes, starting at 0.

Grab box by number  -> O(1)  INSTANT     <- the superpower
Search for a value  -> O(n)  fair
Add/remove at END   -> O(1)  cheap
Add/remove at FRONT -> O(n)  expensive   <- everyone shuffles
Slicing             -> makes a COPY
```

---

## Your turn

```python
items = [4, 8, 15, 16, 23, 42]
```

1. What is `items[0]`?
2. What is `items[-1]`?
3. What is `items[2:4]`?
4. What is `len(items)`?
5. Which is faster: `items.append(99)` or `items.insert(0, 99)`? Why?
6. What is `items[6]`?

### Answers

1. `4` — the first box is box 0.
2. `42` — `-1` always means the last box.
3. `[15, 16]` — boxes 2 and 3. It stops *before* box 4.
4. `6` — six boxes.
5. `append` is faster. It is O(1) because nobody moves. `insert(0, ...)` is
   O(n) because all six items shuffle right to make room.
6. An **error** (`IndexError`). The last box is number 5, because we started
   counting at 0. Six boxes means boxes 0 to 5.

Next: [Lesson 2 — Strings are arrays that can't change](02_what_is_a_string.md)
