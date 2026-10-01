# Exercises & Answer Key

Three parts:

1. **Part A — name the tool.** Read the problem, say which technique. No code.
2. **Part B — trace by hand.** Walk through code on paper.
3. **Part C — write the code.** Fill in `practice.py`, run the tests.

Answers are at the bottom. Try first — reading answers feels like learning
and isn't.

---

## Part A — name the tool

For each problem, say which technique you'd use **and why**.

1. Find the longest substring with no repeated characters.
2. Given a sorted array, find two numbers that add to 50.
3. Given an **unsorted** array, find two numbers that add to 50.
4. Remove all the 7s from an array, in place, using O(1) extra space.
5. Find the maximum sum of any 5 consecutive numbers.
6. Check whether a word is a palindrome.
7. Find the smallest subarray whose sum is at least 100.
8. Does this array contain any duplicate values?
9. Find the longest substring with at most 3 different characters.
10. Find any three numbers in the array that add to 20.
11. Merge two already-sorted arrays into one sorted array.
12. Find the first character in a string that appears exactly once.

---

## Part B — trace by hand

### B1
```python
items = [5, 2, 8, 1]
left, right = 0, 3
while left < right:
    items[left], items[right] = items[right], items[left]
    left += 1
    right -= 1
```
What is `items` at the end? How many swaps happened?

### B2
```python
numbers = [1, 4, 6, 8, 10]
target = 14
```
Trace `two_sum_sorted`. Write down the sum at each step and which finger
moved. How many steps before it finds the answer?

### B3
```python
items = [1, 0, 2, 0, 0, 3]
```
Trace `move_zeros_to_end`. Where is the writer after the main loop?

### B4
```python
numbers = [3, 1, 4, 1, 5], k = 2
```
List every window and its sum. Show the `+= joiner - leaver` arithmetic.

### B5
```python
text = "abba"
```
Trace `longest_without_repeats`. What does the window look like at each
step, and what's the answer?

### B6
`left = 2`, `right = 6`. How many items are in the window?

---

## Part C — write the code

Open `exercises/practice.py` — 14 functions, grouped by technique.
Then run:

```bash
python3 -m unittest discover -s tests -v
```

Exercises you haven't written yet are **skipped**, not failed.

| Part | Function | Technique | Required |
|---|---|---|---|
| A | `reverse_list_in_place` | two pointers, ends | O(n) time, **O(1)** space |
| A | `is_palindrome` | two pointers, ends | O(n) time, **O(1)** space |
| A | `two_sum_sorted` | two pointers, ends | O(n) time, O(1) space |
| B | `move_zeros_to_end` | reader & writer | O(n) time, **O(1)** space |
| B | `remove_all` | reader & writer | O(n) time, **O(1)** space |
| B | `remove_duplicates_sorted` | reader & writer | O(n) time, **O(1)** space |
| C | `max_sum_of_k` | fixed window | O(n) time, O(1) space |
| C | `averages_of_k` | fixed window | O(n) time |
| D | `longest_without_repeats` | growing window + set | O(n) time |
| D | `shortest_subarray_with_sum` | growing window | O(n) time, O(1) space |
| E | `reverse_words` | split + join | O(n) time |
| E | `is_anagram` | dict counting | O(n) time |
| E | `first_unique_char` | dict counting | O(n) time |

> The tests check more than the answer. `test_practice.py` also checks that
> your in-place functions really mutate the list, and that your window
> solutions are fast enough on big inputs — so a nested loop will be caught
> even when the answer is right.

---
---

# ANSWER KEY

## Part A

**1. Longest substring, no repeats** → **growing window + set.**
"substring" = neighbours = window. "Longest" with a rule and no size given
= growing. The set answers "is this letter in my window?" in O(1).
→ O(n) time, O(k) space.

**2. Pair summing to 50, SORTED** → **two pointers from the ends.**
Sorted means each step is a safe decision. → O(n) time, O(1) space.

**3. Pair summing to 50, UNSORTED** → **a set.**
Two pointers needs sorted data. Ask instead: "have I seen `50 - x`?"
→ O(n) time, O(n) space. (Or sort first and use two pointers: O(n log n)
time but O(1) space. Say which trade you chose.)

**4. Remove all 7s in place, O(1) space** → **reader & writer.**
"In place" + "O(1) space" is practically the examiner naming the technique.

**5. Max sum of 5 in a row** → **fixed sliding window.**
"Consecutive" = window; the size 5 is given = fixed.
→ `window_sum += new - old`. O(n) time, O(1) space.

**6. Palindrome** → **two pointers from the ends.**
O(n) time, O(1) space. (`word == word[::-1]` is also fine and actually
faster in real seconds — but O(n) space. Both are good answers.)

**7. Smallest subarray with sum ≥ 100** → **growing window.**
"Smallest" + a rule, no size. Remember the mirror: shrink while the window
is GOOD. → O(n) time, O(1) space.

**8. Contains a duplicate?** → **a set.**
Not a pair, not a stretch, not in place. "Seen this before?" → set.
→ O(n) time, O(n) space.

**9. Longest substring, at most 3 different characters** → **growing window
+ dict.** A dict, not a set, because you must know *how many copies* of a
character are inside to know when it has fully left the window.

**10. Any three numbers adding to 20** → **not a window!** "Any three" means
scattered, and windows are only ever neighbours. Sort, then loop + two
pointers → O(n²). (This is the classic "3Sum".)

**11. Merge two sorted arrays** → **one pointer per array.** The next
smallest item is always at one of the two fronts. → O(n + m).

**12. First character appearing once** → **a dict.** Count in one pass, then
scan in a second pass for the first with count 1. Two passes, still O(n).

---

## Part B

**B1** — `[1, 8, 2, 5]`, after **2 swaps**.
Step 1: swap boxes 0 and 3 → `[1, 2, 8, 5]`.
Step 2: `left=1, right=2`, swap → `[1, 8, 2, 5]`. Now `left=2, right=1`,
so `left < right` is False and the loop stops.

**B2** — target 14 in `[1, 4, 6, 8, 10]`:

| Step | left | right | sum | Decision |
|---|---|---|---|---|
| 1 | 1 | 10 | 11 | too small → move left |
| 2 | 4 | 10 | 14 | **found!** |

**2 steps.** The nested-loop version would have tested up to 10 pairs.

**B3** — `[1, 0, 2, 0, 0, 3]`:
reader sees 1 (keep, W→1), 0 (skip), 2 (keep, W→2), 0 (skip), 0 (skip),
3 (keep, W→3). The writer ends at **3**. Then the padding loop fills boxes
3, 4, 5 with zeros → `[1, 2, 3, 0, 0, 0]`.

**B4** — `[3, 1, 4, 1, 5]`, k=2:

| Window | Arithmetic | Sum |
|---|---|---|
| `[3,1]` | first window: 3+1 | 4 |
| `[1,4]` | 4 − 3 + 4 | 5 |
| `[4,1]` | 5 − 1 + 1 | 5 |
| `[1,5]` | 5 − 4 + 5 | 6 |

Biggest = **6**. Note each slide is one subtraction and one addition — never
a re-sum.

**B5** — `"abba"`:

| right | Letter | Action | Window | Size |
|---|---|---|---|---|
| 0 | a | add | `[a]` | 1 |
| 1 | b | add | `[ab]` | 2 ← best |
| 2 | b | repeat! drop `a`, drop `b`, then add | `[b]` | 1 |
| 3 | a | add | `[ba]` | 2 |

Answer **2**. Watch step 2 carefully: `left` had to move twice before the
rule was satisfied — that's why the shrink is a `while`, not an `if`.

**B6** — `6 − 2 + 1 = ` **5** items (boxes 2, 3, 4, 5, 6).

---

## Lesson check-yourself answers

**Lesson 1** — 1. `4` 2. `42` 3. `[15, 16]` 4. `6` 5. `append`, because it's
O(1) (nobody moves) while `insert(0, …)` is O(n) (everyone shuffles)
6. `IndexError` — six boxes are numbered 0 to 5.

**Lesson 2** — 1. `'P'` 2. `'M'` 3. `'PRO'` 4. `TypeError` — strings are
frozen 5. `"X" + word[1:]`, or the unfreeze dance 6. `+=` in a loop is
O(n²); use `"".join(...)` (or just `word.lower()`).

**Lesson 3** — 1. `<` is safe even if the fingers step past each other;
`!=` could loop forever. 2. Because "move left for a bigger sum" is only
true when everything to the right is bigger — i.e. sorted. 3. Writer ends
at 1; result `[1, 0, 0]`. 4. Yes; **3 comparisons** for 7 letters. 5. Reader
& writer.

**Lesson 4** — 1. `[1,4]`=5, `[4,2]`=6, `[2,10]`=12 → 12. 2. Only two
numbers change per slide; re-adding the middle is wasted work. 3. **5**.
4. Growing. 5. No — "any 3 numbers" means scattered, not neighbours.
6. Because `left` only moves forward, at most n times in total → 2n = O(n).

**Lesson 5** — 1. two pointers / `" ".join(reversed(s.split()))`
2. growing window 3. dict counting 4. fixed window, k=7 5. reader & writer
6. sort + loop + two pointers (3Sum) 7. dict counting.

---

## Part C — the two traps to watch for

**Trap 1: `shortest_subarray_with_sum` is the mirror image.**

```python
# LONGEST: shrink while the window is BAD
while <rule broken>:
    left += 1
best = max(best, right - left + 1)

# SHORTEST: shrink while the window is GOOD
while <rule satisfied>:
    best = min(best, right - left + 1)   # measure BEFORE shrinking
    left += 1
```

Getting these backwards is the single most common sliding-window bug.

**Trap 2: in-place means in-place.**
`items = [x for x in items if x != 0]` rebinds the local name and leaves the
caller's list untouched. The tests check object identity, so that won't
pass. Assign through the index: `items[writer] = items[reader]`.

Full worked solutions with commentary: `exercises/solutions.py`.
