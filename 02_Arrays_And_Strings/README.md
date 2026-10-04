# Arrays & Strings — two pointers and sliding window

Topic 02. Pictures first, jargon later. Everything runnable, everything tested.

No third-party packages. Python 3.8+ and the standard library only.

> **Watch it run:** [`../visualizer.html`](../visualizer.html) is an interactive
> page with all six algorithms from this topic animated step by step, plus 25
> more related questions including every classic sort. Open it in a browser
> alongside these notes.

---

## Start here

```bash
cd 17_DSA/02_Arrays_And_Strings

# 1. Read lesson 1
less notes/01_what_is_an_array.md

# 2. Run the matching demo - it draws the fingers moving
python3 code/01_array_basics.py

# 3. When you reach the exercises, check your work
python3 -m unittest discover -s tests -v
```

---

## The path (about 5–7 hours over a few days)

| # | Read | Then run | You'll be able to |
|---|------|----------|-------------------|
| 1 | [What is an array?](notes/01_what_is_an_array.md) | `code/01_array_basics.py` | say why the front of a list is expensive |
| 2 | [Strings can't change](notes/02_what_is_a_string.md) | `code/02_string_basics.py` | stop writing `+=` in a loop |
| 3 | [Two pointers](notes/03_two_pointers.md) | `code/03_...py`, `code/04_...py` | reverse, palindrome, pair-sum in O(1) space |
| 4 | [Sliding window](notes/04_sliding_window.md) | `code/05_...py`, `code/06_...py` | turn O(n·k) into O(n) |
| 5 | [Which technique?](notes/05_which_technique.md) | `code/07_choosing_the_technique.py` | pick the right tool from the wording |
| 6 | [Cheat sheet](notes/06_cheatsheet.md) | — | revise the topic in 5 minutes |

Then do the [exercises](exercises/exercises.md).

---

## The two big ideas

### Two pointers = two fingers on the shelf

```
SHAPE 1 - opposite ends, walking inward     SHAPE 2 - reader & writer
                                             
 [ a, b, c, d, e, f ]                        [ a, b, c, d, e, f ]
   →              ←                            →  →
  left         right                         writer reader

 palindromes, reversing,                     remove, filter, squash,
 pairs in SORTED data                        "move all the X" - IN PLACE
```

### Sliding window = a train window on the shelf

```
FIXED size k                                 GROWING size
                                             
[ 2  1  5 ] 1  3  2                          [ a ]        happy, grow
  2 [ 1  5  1 ] 3  2                         [ a  b ]     happy, grow
                                             [ a  b  a ]  broken! shrink
sum += joiner - leaver                         [ b  a ]   happy again
```

Both replace nested loops. Both are O(n).

---

## What's in each folder

```
02_Arrays_And_Strings/
├── README.md                        <- you are here
├── notes/                           6 lessons, in reading order
├── code/                            7 runnable demonstrations
│   ├── 01_array_basics.py                the shelf: prices of every move
│   ├── 02_string_basics.py               frozen strings, the += trap
│   ├── 03_two_pointers_ends.py           TRACES the fingers moving
│   ├── 04_two_pointers_reader_writer.py  TRACES reader & writer
│   ├── 05_sliding_window_fixed.py        TRACES the window sliding
│   ├── 06_sliding_window_growing.py      TRACES grow and shrink
│   └── 07_choosing_the_technique.py      same problem, 2-3 ways, timed
├── exercises/
│   ├── exercises.md                 name-the-tool, trace-by-hand, answer key
│   ├── practice.py                  14 functions for YOU to write
│   └── solutions.py                 model answers, with the reasoning
└── tests/
    ├── test_solutions.py            proves the model answers are right
    ├── test_practice.py             grades YOUR work (skips what's undone)
    └── test_code_examples.py        proves every lesson example works
```

The `code/` files **draw** what's happening. For example:

```
$ python3 code/03_two_pointers_ends.py

  Reversing [1, 2, 3, 4, 5] with two fingers:
       1    2    3    4    5
       L                   R   step 1: swap 1 and 5
       5    2    3    4    1
            L         R        step 2: swap 2 and 4
       5    4    3    2    1
    the fingers met - DONE after 2 swaps -> [5, 4, 3, 2, 1]
```

---

## Running the tests

```bash
# everything (113 tests)
python3 -m unittest discover -s tests -v

# just your practice work
python3 -m unittest discover -s tests -p "test_practice.py" -v

# every demo plus the full suite
python3 run_all.py
```

Two things worth knowing about `test_practice.py`:

1. **It skips what you haven't written**, so it's a progress report, not a
   wall of red.
2. **It checks more than the answer.** In-place functions must genuinely
   mutate your list (it compares object identity), and the window functions
   are timed on large inputs. A nested loop that returns the right answer
   still fails, with a message telling you which technique to reach for.

Many tests also cross-check against a brute-force version on dozens of
random inputs — so "it works on the example" isn't enough.

---

## The 60-second version

```
STRETCH of neighbours?       -> sliding window
PAIR + sorted?               -> two pointers from the ends
PAIR + not sorted?           -> a set
Filter / remove IN PLACE?    -> reader & writer
"Seen this before?"          -> a set or dict
None of the above?           -> one plain loop

"O(1) extra space" in the question = use two pointers.
Window size = right - left + 1          (the +1 catches everybody once)
Never build a string with += in a loop  (use "".join())
```

---

## Where to go next

Topic 03: **Hash maps & sets** — the "have I seen this before?" tool that
keeps turning up in the answers above. See the
[course roadmap](../README.md).

Keep doing the thing that makes this stick: **say the time and space
complexity out loud for every function you write.**
