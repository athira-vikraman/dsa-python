# Lesson 5 — Which Technique Do I Use?

> You now know three tools. This lesson is about **choosing** — which is the
> part interviews actually test.

---

## 1. Your toolbox so far

| Tool | What it's for | Cost |
|---|---|---|
| **One loop** | look at every item once | O(n) |
| **Two pointers (ends)** | find a *pair*, in sorted data | O(n), O(1) space |
| **Two pointers (reader/writer)** | filter or squash, *in place* | O(n), O(1) space |
| **Sliding window** | find a *stretch* of neighbours | O(n) |
| **A set or dict** | "have I seen this before?" instantly | O(n) time, O(n) space |

Almost every easy array problem is one of these five, or two of them stuck
together.

---

## 2. The decision flowchart

Read the problem, then walk down this list. **Stop at the first match.**

```
Is the answer a STRETCH of neighbours?
  (words: subarray, substring, consecutive, in a row)
        │
        ├── YES -> SLIDING WINDOW
        │           size given?  -> fixed window
        │           rule given?  -> growing window
        │
        └── NO
             │
             Is the answer a PAIR (or triple) of items?
                   │
                   ├── YES, and the list is SORTED
                   │        -> TWO POINTERS from the ends
                   │
                   ├── YES, but NOT sorted
                   │        -> use a SET  (or sort first, then two pointers)
                   │
                   └── NO
                        │
                        Am I removing / filtering IN PLACE?
                              │
                              ├── YES -> READER & WRITER pointers
                              │
                              └── NO  -> just one loop. Don't overthink it.
```

Print this. It answers most array questions.

---

## 3. The word → tool dictionary

Problems use the same words again and again. Learn the signals:

| If you read... | Think... |
|---|---|
| "subarray", "substring", "consecutive", "in a row" | **sliding window** |
| "longest...", "shortest...", "at most k..." | **growing window** |
| "of size k", "every k items" | **fixed window** |
| "palindrome", "reverse" | **two pointers, ends** |
| "pair that sums to X" + sorted | **two pointers, ends** |
| "pair that sums to X" + not sorted | **a set** |
| "in place", "O(1) extra space" | **two pointers** (a big hint!) |
| "remove", "keep only", "move all X" | **reader & writer** |
| "have I seen this?", "duplicate", "unique" | **a set or dict** |
| "count how many of each" | **a dict** (or `Counter`) |
| "merge two sorted lists" | **one pointer per list** |

> The phrase **"O(1) extra space"** in a problem is practically the examiner
> telling you to use two pointers. Nothing else gives you O(1) space.

---

## 4. Worked examples: reading the problem out loud

### "Find the longest substring without repeating characters"

- "substring" → neighbours → **window** ✅
- "longest" + a rule, no size → **growing window**
- Need to know what's inside the window → a **set**
- **Answer: growing window + set.** O(n) time, O(k) space.

### "Given a sorted array, find two numbers that add to 100"

- A **pair**, not a stretch → not a window
- The list is **sorted** → **two pointers from the ends** ✅
- O(n) time, O(1) space.

### "Given an UNSORTED array, find two numbers that add to 100"

- A pair, but **not sorted** → two pointers won't work
- "Have I seen `100 - x` before?" → **a set** ✅
- O(n) time, O(n) space.
- (You *could* sort it first and use two pointers: O(n log n) time but O(1)
  space. Both are good answers — say which trade you're making.)

### "Remove all the zeros from this array in place"

- "in place" → **two pointers** ✅
- Filtering → **reader & writer**
- O(n) time, O(1) space.

### "Find the maximum sum of any 4 consecutive numbers"

- "consecutive" → **window** ✅
- Size 4 is given → **fixed window**
- O(n) time, O(1) space.

### "Does this array contain any duplicates?"

- Not a pair, not a stretch, not in place
- "Have I seen this?" → **a set** ✅
- O(n) time, O(n) space.

---

## 5. The mistakes everyone makes (including me)

**1. Using a window when the items can be scattered.**
"Any 3 numbers that add to 20" is *not* a window. Windows are neighbours
only. Always ask: "must they be next to each other?"

**2. Forgetting the `+ 1` in the window size.**
`right - left + 1`. Write it on your hand.

**3. Using two pointers from the ends on an unsorted list.**
The "move left for a bigger sum" logic needs sorted data. Without it, moving
a finger tells you nothing.

**4. Slicing inside a loop.**
`items[i:i+k]` inside a loop copies k items **every single time** — that
quietly undoes the whole optimisation. Use `window_sum += new - old` instead.

**5. Forgetting to shrink the window.**
In a growing window, the `while` that shrinks is not optional. Without it,
the window only ever grows and your answer is wrong.

**6. Off-by-one at the edges.**
Always test: empty list `[]`, one item `[5]`, and a window bigger than the
list. These three tests catch almost every bug.

---

## 6. The template to memorise

Write these out by hand a few times. They cover a huge number of problems.

```python
# ---- TWO POINTERS: opposite ends -------------------------
left, right = 0, len(items) - 1
while left < right:
    # look at items[left] and items[right]
    if <condition>:
        left += 1
    else:
        right -= 1


# ---- TWO POINTERS: reader & writer -----------------------
writer = 0
for reader in range(len(items)):
    if <keep this item?>:
        items[writer] = items[reader]
        writer += 1
# writer = how many items we kept


# ---- SLIDING WINDOW: fixed size k ------------------------
window_sum = sum(items[:k])
best = window_sum
for i in range(k, len(items)):
    window_sum += items[i] - items[i - k]
    best = max(best, window_sum)


# ---- SLIDING WINDOW: growing --------------------------------
left = 0
best = 0
for right in range(len(items)):
    # add items[right] to the window
    while <window breaks the rule>:
        # remove items[left] from the window
        left += 1
    best = max(best, right - left + 1)
```

---

## 7. Remember this

```
STRETCH of neighbours?       -> sliding window
PAIR + sorted?               -> two pointers from the ends
PAIR + not sorted?           -> a set
Filtering IN PLACE?          -> reader & writer
"Have I seen this before?"   -> a set or dict
None of the above?           -> one simple loop

"O(1) extra space" in the question = use two pointers.
Window size = right - left + 1
```

---

## Your turn — name the tool for each

1. "Reverse the words in a string."
2. "Find the smallest subarray whose sum is at least 100."
3. "Check if two words are anagrams."
4. "Find the average of every 7 consecutive days."
5. "Remove duplicates from a sorted array, in place."
6. "Find three numbers in a sorted array that add to zero."
7. "Find the first character in a string that appears only once."

### Answers

1. **Two pointers / built-ins.** `" ".join(reversed(s.split()))` is fine and
   O(n). If asked for O(1) space on a character array: reverse the whole
   thing, then reverse each word — a classic two-pointer trick.
2. **Growing window.** "Smallest" + a rule ("sum at least 100") and no size
   given.
3. **A dict** (count the letters). O(n). Sorting both also works but is
   O(n log n).
4. **Fixed window**, size 7. `window_sum += new - old`, divide by 7.
5. **Reader & writer.** "In place" is the giveaway.
6. **Loop + two pointers.** Fix the first number with a loop, then use two
   pointers on the rest → O(n²). This is the famous "3Sum" problem, and it's
   just today's lesson with one extra loop on top.
7. **A dict** to count, then one loop to find the first with count 1. Two
   passes, still O(n).

Next: [Lesson 6 — The cheat sheet](06_cheatsheet.md)

---

## Related concepts

[[Concepts/Two pointers|Two pointers]] · [[Concepts/Sliding window|Sliding window]] · [[Concepts/Hashing|Hashing]] · [[Concepts/Searching|Searching]]

See also [[Problems/_All problems|all 31 problems]] · [[00 START HERE]]
