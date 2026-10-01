# Lesson 4 — The Sliding Window

> The second big technique. Also easy, also replaces nested loops.

---

## 1. The train window

Imagine you're on a train, looking out of the window.

The window shows you **3 seats** at a time. As the train moves, the window
**slides** along — one new seat appears on the right, one old seat disappears
on the left.

```
Seats:  [ 2,  1,  5,  1,  3,  2 ]

Window 1: [ 2  1  5 ] 1  3  2      you see 2, 1, 5
Window 2:   2 [ 1  5  1 ] 3  2     1 left, 1 joined
Window 3:   2  1 [ 5  1  3 ] 2     5 left, 3 joined
Window 4:   2  1  5 [ 1  3  2 ]    1 left, 2 joined
```

That's a **sliding window**. A box that slides along the shelf, looking at
a group of neighbours at a time.

> **Use it when the problem asks about a group of items that are
> NEXT TO EACH OTHER.** Words like *"subarray"*, *"substring"*,
> *"consecutive"*, *"in a row"* — those all mean "a window".

---

## 2. The slow way (and why it's slow)

**Problem:** find the biggest sum of any 3 numbers in a row.

```python
numbers = [2, 1, 5, 1, 3, 2]
```

The beginner way: look at each starting spot, and add up 3 numbers.

```python
def biggest_sum_of_3_slow(numbers):
    best = 0
    for start in range(len(numbers) - 2):     # every starting spot
        total = 0
        for i in range(start, start + 3):     # add up 3 numbers
            total += numbers[i]
        best = max(best, total)
    return best
```

This works! But look at the wasted effort:

```
Window 1: 2 + 1 + 5     = 8
Window 2:     1 + 5 + 1 = 7      <- I added 1 and 5 AGAIN
Window 3:         5 + 1 + 3 = 9  <- I added 5 and 1 AGAIN
```

We keep re-adding numbers we already added. That's **O(n · k)** — slow.

---

## 3. The sliding window way

Here's the trick, and it's beautiful:

> When the window slides one step, **only two things change.**
> One number joins on the right. One number leaves on the left.
> Everything in the middle is the same — so don't touch it!

So instead of re-adding everything:

```
total = 8          (2 + 1 + 5)

Slide: 2 leaves, 1 joins
total = 8 - 2 + 1 = 7       ✅ one subtraction, one addition

Slide: 1 leaves, 3 joins
total = 7 - 1 + 3 = 9       ✅
```

Two operations per slide instead of k. Here's the code:

```python
def biggest_sum_of_3(numbers):
    k = 3

    # Step 1: build the FIRST window
    window_sum = sum(numbers[:k])
    best = window_sum

    # Step 2: slide it along
    for i in range(k, len(numbers)):
        window_sum = window_sum + numbers[i] - numbers[i - k]
        #                         ↑ joins      ↑ leaves
        best = max(best, window_sum)

    return best
```

- **Time: O(n)** — each number joins once and leaves once.
- **Space: O(1)** — just a couple of number variables.

Down from O(n · k). And notice: **the window size never changes.** That's
called a **fixed window**.

> 🧠 **The one line to remember:**
> `window_sum += numbers[i] - numbers[i - k]`
> *"add the one joining, subtract the one leaving."*

---

## 4. The two kinds of window

### Fixed window — the size never changes

The problem **tells you** the size. "Any 3 in a row." "Every 5 days."
"A substring of length 4."

```
[ 2  1  5 ] 1  3        size 3
  2 [ 1  5  1 ] 3       still size 3
```

**Recipe:**
1. Build the first window (the first `k` items).
2. Slide: add the newcomer, remove the leaver, check your answer.

### Growing window — the size changes as you go

The problem gives you a **rule** instead of a size. "The longest stretch
with no repeated letters." "The shortest stretch that adds up to 50."

The window **stretches** when it's happy, and **shrinks** when it breaks
the rule.

```
[ a ]           happy, stretch
[ a  b ]        happy, stretch
[ a  b  c ]     happy, stretch
[ a  b  c  a ]  broken! 'a' twice -> SHRINK from the left
  [ b  c  a ]   happy again, carry on
```

**Recipe:**
1. `right` walks forward, growing the window (one step at a time).
2. **While** the window breaks the rule, move `left` forward to shrink it.
3. After every step, record your answer.

```python
def longest_without_repeats(text):
    seen = set()           # what's inside the window right now
    left = 0
    best = 0

    for right in range(len(text)):
        # the window is broken - shrink from the left until it's fixed
        while text[right] in seen:
            seen.remove(text[left])
            left += 1

        seen.add(text[right])                 # now it's safe to add
        best = max(best, right - left + 1)    # window size

    return best
```

> **Why is this O(n) and not O(n²)?** There's a loop inside a loop — looks
> quadratic! But look at what the inner loop does: it only ever moves `left`
> **forward**. `left` starts at 0 and can only reach the end, so across the
> *entire run* it moves at most n times. `right` also moves n times.
> Total: 2n steps → **O(n)**.
>
> This "each pointer only moves forward, so it's still linear" argument is
> worth understanding. It's the reason the technique works.

⚠️ **Window size is `right - left + 1`**, not `right - left`. Check it:
if `left = 2` and `right = 4`, you're holding boxes 2, 3 and 4 — that's
**3** boxes, and `4 - 2 + 1 = 3`. ✅ The `+ 1` catches everybody once.

---

## 5. How to spot a sliding window problem

| The problem says... | Window type |
|---|---|
| "subarray of size k" | fixed |
| "average of every k days" | fixed |
| "substring of length k" | fixed |
| "**longest** stretch where..." | growing |
| "**shortest** stretch where..." | growing |
| "at most k different letters" | growing |
| "sum is at least / at most X" | growing |

The giveaway: the answer is a **chunk of neighbours** — not scattered items.

> ❗ **If the items can be scattered** (any 3 items, not 3 in a row), it is
> **not** a window problem. Windows are always about **neighbours**.

---

## 6. Two pointers vs sliding window — what's the difference?

Honest answer: **a sliding window IS a two-pointer technique.** `left` and
`right` are two pointers. The difference is what they mean:

| | Two pointers (classic) | Sliding window |
|---|---|---|
| The fingers are... | at opposite ends, closing in | both on the left, moving right |
| You care about... | the **two items** under your fingers | **everything between** them |
| Needs sorted data? | usually yes | no |
| Typical question | "find a pair" | "find a stretch" |

> **A pair → classic two pointers. A stretch → sliding window.**

---

## 7. Remember this

```
SLIDING WINDOW = a box of neighbours that slides along the shelf

FIXED size (k given):
    build the first window, then:
    window_sum += new - old        <- add joiner, subtract leaver

GROWING size (a rule given):
    right grows the window
    while the rule is broken: left shrinks it
    record the answer every step

Window size = right - left + 1     <- remember the +1

Both are O(n) time, O(1) space (or O(k) if you keep a set/dict).
They replace nested loops - O(n^2) or O(n*k).
```

---

## Your turn

1. `[1, 4, 2, 10]`, window size 2. What are all the windows and their sums?
2. Why don't we re-add the whole window after every slide?
3. `left = 3`, `right = 7`. How many items are in the window?
4. "Find the longest substring with at most 2 different letters" — fixed or
   growing window?
5. "Find any 3 numbers in the list that add to 20" — is this a window
   problem?
6. In `longest_without_repeats`, why is it O(n) when there's a loop inside a
   loop?

### Answers

1. `[1,4]`=5, `[4,2]`=6, `[2,10]`=12. Biggest is 12.
2. Because only two numbers change when the window slides — one joins, one
   leaves. Re-adding the middle is wasted work. That's the whole trick.
3. `7 - 3 + 1 = ` **5** items (boxes 3, 4, 5, 6, 7).
4. **Growing.** You're asked for the *longest*, and the rule is "at most 2
   different letters" — no size was given.
5. **No.** "Any 3 numbers" means they can be scattered anywhere, not
   neighbours. Windows only work on neighbours. (That one needs sorting +
   two pointers, or a set.)
6. Because `left` only ever moves **forward**, never back. Across the whole
   run it moves at most n times total, no matter how the inner `while` is
   spread out. n steps for `right` + n steps for `left` = O(n).

Next: [Lesson 5 — Which technique do I use?](05_which_technique.md)
