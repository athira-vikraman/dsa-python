# Lesson 5a — Time vs Space, the Gentle Version

> **Read this BEFORE [Lesson 5](05_space_complexity.md).**
> No jargon. One idea at a time.

---

## 1. The kitchen

Imagine you are cooking in a kitchen.

Two completely different questions can be asked about your cooking:

1. **"How long did it take?"** → that is **TIME**
2. **"How many bowls and plates did you dirty?"** → that is **SPACE**

That's it. That is the whole difference.

- **Time complexity** = how much **work** your code does.
- **Space complexity** = how much **extra storage** your code uses.

They are two separate questions about the same recipe. A dish can be:

- fast and use few bowls (great)
- fast but dirty every bowl in the kitchen (fast, memory hungry)
- slow but use one bowl (slow, memory friendly)
- slow and dirty every bowl (bad at both)

Your code can be any of those four, too.

---

## 2. Counting time = counting steps

Forget seconds. **Count how many times the computer does something.**

```python
def add_up(numbers):
    total = 0              # 1 step
    for n in numbers:      # repeats once per number
        total = total + n  # 1 step each time
    return total           # 1 step
```

If `numbers` has 5 items, the loop body runs 5 times.
If it has 1000 items, it runs 1000 times.

> The work grows **in step with the list**. We call that **O(n)** time.
> (`n` is just a short name for "how many items are in the input".)

---

## 3. Counting space = counting the boxes YOU create

Now look at the *same* function again, but ask the other question:
**how many new storage boxes did I make?**

```python
def add_up(numbers):
    total = 0              # box 1  <- I made this
    for n in numbers:      # box 2  <- I made this
        total = total + n
    return total
```

I made **2 boxes**: `total` and `n`.

Now the key question — and this is the one that unlocks everything:

> **If the list had 1 million items instead of 5, would I need MORE boxes?**

No! Still just `total` and `n`. Two boxes. Always two.

> The number of boxes never grows. We call that **O(1)** space.
> O(1) means "a fixed amount, no matter how big the input is".

**So `add_up` is O(n) time and O(1) space.** It does a lot of work, but it
barely uses any memory. Two different answers, two different questions.

---

## 4. Now a function that DOES need more boxes

```python
def double_everything(numbers):
    result = []                  # a new, EMPTY list
    for n in numbers:
        result.append(n * 2)     # the list grows... and grows...
    return result
```

Ask the two questions:

**Time?** The loop runs once per item → **O(n)**.

**Space?** Here is the difference. That `result` list ends up holding **one
item for every item in the input**.

- Input has 5 items → `result` holds 5 items
- Input has 1,000,000 items → `result` holds 1,000,000 items

> The storage grows in step with the input. That is **O(n)** space.

**So `double_everything` is O(n) time and O(n) space.**

---

## 5. Compare them side by side

| | `add_up` | `double_everything` |
|---|---|---|
| What it makes | one number | a whole new list |
| Boxes needed for 5 items | 2 | 5 |
| Boxes needed for 1,000,000 items | **2** | **1,000,000** |
| Time | O(n) | O(n) |
| **Space** | **O(1)** | **O(n)** |

Same time. Very different memory. That's why we need both numbers.

---

## 6. Why don't we count the input itself?

A fair question! `numbers` has a million items sitting in memory — isn't that
space too?

Yes, but **somebody else already paid for it**. The list existed before your
function was called. You were handed it.

> Space complexity only counts what **YOU** create inside the function.

Think of it like a kitchen again: the vegetables were already on the counter
when you walked in. We're counting the **bowls you dirtied**, not the
ingredients you were given.

(The textbook word for "what you created" is **auxiliary space**. That's the
word that confused you in Lesson 5. It just means "extra" — the bowls, not
the vegetables.)

---

## 7. How to find space complexity, in 3 questions

Look at your function and ask, in order:

**Q1. Did I create any new list, dict, set or string?**
- No → probably O(1) space.
- Yes → go to Q2.

**Q2. Does that thing grow bigger when the input gets bigger?**
- No (it always holds 5 things, or 26 letters) → still **O(1)** space.
- Yes (one entry per input item) → **O(n)** space.

**Q3. Does my function call itself (recursion)?**
- Yes → see section 8 below. Recursion secretly uses space.

That's the whole method. Let's practise it.

```python
def count_evens(numbers):
    count = 0                    # Q1: no new list. Just a number.
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count
# Time: O(n)  (looks at every number)
# Space: O(1) (one counter, forever)
```

```python
def get_evens(numbers):
    evens = []                   # Q1: yes, a new list!
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)      # Q2: grows with the input -> O(n)
    return evens
# Time: O(n)
# Space: O(n)
```

Look how similar those two functions are. One counts, one collects.
**Collecting costs memory. Counting does not.** That single difference is
most of space complexity.

---

## 8. The confusing bit: recursion uses space

This is the part nobody explains properly, so here it is slowly.

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)      # the function calls ITSELF
```

This creates **no list**. No dict. Nothing. So it must be O(1) space, right?

**No.** And here is why.

Imagine you ask a friend a question. Your friend doesn't know, so they ask
*their* friend. That friend asks another friend. And so on.

While friend #5 is thinking, friends #1, #2, #3 and #4 are all **still
waiting**. Nobody has gone home. They are all standing there, holding their
place in the conversation.

Each waiting friend takes up a chair. `countdown(1000)` means **1000 friends
all waiting at once** — 1000 chairs.

The computer calls those chairs the **call stack**. Each unfinished function
call sits on it, taking memory, until it finishes.

> **Recursion depth = space used.**
> `countdown(n)` goes n levels deep, so it is **O(n)** space.

Compare with the loop version:

```python
def countdown_loop(n):
    while n > 0:
        print(n)
        n -= 1
# Space: O(1)  -- nobody is waiting. One person does all the work.
```

Same output. Same O(n) time. But the loop needs **1 chair** and the recursion
needs **n chairs**.

You can even watch this break. Python only has about 1000 chairs:

```python
countdown(999)      # fine
countdown(100000)   # RecursionError: maximum recursion depth exceeded
```

That error message is space complexity, happening to you in real life.

---

## 9. Why do we care? A real story

You write a function that processes a list of customer records.
It is **O(n) time, O(n) space** — it builds a new list of results.

With 1,000 customers: fine.
With 50,000,000 customers: your program crashes. **Out of memory.**

The time was never the problem. The *copy* was. Your laptop had enough
patience but not enough RAM.

This is why every interviewer asks for both numbers. "Fast" is not enough if
it doesn't fit in memory.

---

## 10. The trade: you can swap one for the other

Here is the most useful idea in this whole lesson.

**You can often make code faster by using more memory.**

Remember finding duplicates?

```python
# Version A: slow, but tiny memory
def has_duplicate_slow(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False
# Time: O(n^2)  -- slow!
# Space: O(1)   -- but no extra memory at all

# Version B: fast, but needs memory
def has_duplicate_fast(items):
    seen = set()                 # a new box that grows
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False
# Time: O(n)    -- fast!
# Space: O(n)   -- the price we paid
```

Version B is thousands of times faster. We **bought** that speed by **paying**
memory for the `seen` set.

That's a trade, and trades have two sides. Usually it's worth it. On a
gigantic dataset with limited RAM, it isn't. Knowing there *is* a choice is
the skill.

---

## 11. The whole lesson in one box

```
TIME  = how many STEPS?        -> "how long does it take?"
SPACE = how many extra BOXES?  -> "how much memory does it need?"

O(1)  = a fixed amount. Doesn't grow with the input.
O(n)  = grows in step with the input.

Counting something  -> O(1) space
Collecting something -> O(n) space
Recursion n deep    -> O(n) space (the waiting friends)
```

Every time you write a function from now on, say both out loud:

> "This is O(n) time and O(1) space."

Do it twenty times and it stops feeling like maths.

---

## 12. Your turn — 6 questions

Say the **time** and **space** for each. Answers below, don't peek yet.

```python
# Q1
def first_item(items):
    return items[0]

# Q2
def copy_list(items):
    new = []
    for x in items:
        new.append(x)
    return new

# Q3
def biggest(items):
    best = items[0]
    for x in items:
        if x > best:
            best = x
    return best

# Q4
def letter_counts(word):
    counts = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts

# Q5
def add_up_recursive(items, i=0):
    if i == len(items):
        return 0
    return items[i] + add_up_recursive(items, i + 1)

# Q6
def last_three(items):
    keep = []
    for x in items[-3:]:
        keep.append(x)
    return keep
```

---

### Answers

**Q1** — O(1) time, O(1) space.
No loop, no new box. One lookup.

**Q2** — O(n) time, O(n) space.
The loop visits every item (time), and `new` ends up holding n items (space).
**Collecting** → O(n) space.

**Q3** — O(n) time, O(1) space.
It visits every item (time), but only ever keeps ONE value in `best`.
**Counting/tracking** → O(1) space. Compare with Q2 — nearly the same code,
very different memory.

**Q4** — O(n) time, O(n) space.
One pass over the word. The dict grows with the number of *different*
letters. Careful students say "O(k) where k is the distinct letters" — and
for English that's at most 26, so some would even argue O(1). Both answers
show you understood; just say which you mean.

**Q5** — O(n) time, **O(n) space**.
It creates no list at all — but it calls itself n times, so n calls are all
waiting at once. **n chairs.** This is the one most beginners get wrong.

**Q6** — O(1) time, O(1) space.
`items[-3:]` grabs at most 3 items, and the loop runs at most 3 times, no
matter how long `items` is. Nothing here grows with the input.

---

## Where to go next

Got all six? You now understand space complexity. Go read
[Lesson 5](05_space_complexity.md) again — it will read completely
differently now, and it adds the interview vocabulary on top of what you just
learned.

Want to see it measured? Run:

```bash
python3 code/10_time_vs_space_simple.py
```

That file builds the same function two ways and prints the actual memory each
one uses, so you can watch "O(1) space" and "O(n) space" with your own eyes.

---

## Related concepts

[[Concepts/Space complexity|Space complexity]] · [[Concepts/In-place algorithms|In-place algorithms]] · [[Concepts/Recursion|Recursion]] · [[Concepts/Hashing|Hashing]]

See also [[Problems/_All problems|all 31 problems]] · [[00 START HERE]]
