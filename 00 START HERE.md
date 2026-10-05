---
tags:
  - dashboard
---

# DSA — start here

Welcome to your study vault. This note is the front door: every lesson,
exercise and bit of code is one click away from here.

> [!tip] New to Obsidian?
> Read [[How to use this vault]] first. It takes five minutes and covers
> everything you need: opening notes, searching, ticking boxes, and the
> graph view.

---

## Where you are

| Topic | Status | Start at |
|---|---|---|
| 01 — Big O notation | ✅ done | [[01_Big_O_Notation/README\|Topic 01 index]] |
| 02 — Arrays & strings | ✅ done | [[02_Arrays_And_Strings/README\|Topic 02 index]] |
| 03 — Hash maps & sets | ⬜ next | — |

Tick off what you finish in [[Progress tracker]].

---

## The two indexes

| | |
|---|---|
| [[Problems/_All problems\|🧩 All 31 problems]] | one note each: the question, the technique, the complexity, the code |
| [[Concepts/_All concepts\|🧠 All 18 concepts]] | the ideas the problems share — these are the hubs in the graph |

> [!tip] See the graph
> Press `Ctrl + G`. Each **concept** sits at the centre of a cluster of the
> problems that use it. Click any dot to open that note.
>
> Even better: open a single note and press `Ctrl + P` → **"Open local
> graph"**. That shows only what *this* note connects to, which is far easier
> to read than the whole web.

---

## Topic 01 — Big O notation

The measuring tool. Read these in order.

1. [[01_Big_O_Notation/notes/01_why_complexity_matters|Why we measure code]]
2. [[01_Big_O_Notation/notes/02_what_is_big_o|What Big O actually means]]
3. [[01_Big_O_Notation/notes/03_rules_of_big_o|The four rules]]
4. [[01_Big_O_Notation/notes/04_common_complexity_classes|The complexity classes]]
5. [[01_Big_O_Notation/notes/05a_time_vs_space_for_beginners|Time vs space — the gentle version]] ⭐ *start here if lesson 5 was hard*
6. [[01_Big_O_Notation/notes/05_space_complexity|Space complexity]]
7. [[01_Big_O_Notation/notes/06_recursion_and_amortized|Recursion & amortized]]
8. [[01_Big_O_Notation/notes/07_python_operation_costs|What every Python operation costs]]
9. [[01_Big_O_Notation/notes/08_how_to_analyze_any_code|How to analyse any code]]
10. [[01_Big_O_Notation/notes/09_cheatsheet|Cheat sheet]] 📌

Practice: [[01_Big_O_Notation/exercises/exercises|Exercises & answer key]]

---

## Topic 02 — Arrays & strings

Two pointers and sliding windows.

1. [[02_Arrays_And_Strings/notes/01_what_is_an_array|What is an array?]]
2. [[02_Arrays_And_Strings/notes/02_what_is_a_string|Strings can't change]]
3. [[02_Arrays_And_Strings/notes/03_two_pointers|Two pointers]]
4. [[02_Arrays_And_Strings/notes/04_sliding_window|Sliding window]]
5. [[02_Arrays_And_Strings/notes/05_which_technique|Which technique do I use?]]
6. [[02_Arrays_And_Strings/notes/06_cheatsheet|Cheat sheet]] 📌

Practice: [[02_Arrays_And_Strings/exercises/exercises|Exercises & answer key]]

---

## The two cheat sheets

When you only have five minutes, revise these:

- [[01_Big_O_Notation/notes/09_cheatsheet|Big O cheat sheet]] — the growth
  ranking, the four rules, Python operation costs
- [[02_Arrays_And_Strings/notes/06_cheatsheet|Arrays cheat sheet]] — the four
  templates and the decision list

---

## Watch it run

`visualizer.html` in this folder animates 31 classic problems step by step.
Obsidian cannot open it, so **double-click the file in your file manager**
and it opens in your browser.

In a terminal, from this folder:

```bash
xdg-open visualizer.html
```

---

## Run the code

Every lesson has runnable Python beside it. From a terminal in this folder:

```bash
cd 01_Big_O_Notation
python3 code/11_sorting_algorithms.py     # nine sorts, timed
python3 run_all.py                        # every demo + all 138 tests
```

```bash
cd 02_Arrays_And_Strings
python3 code/03_two_pointers_ends.py      # watch the fingers move
python3 -m unittest discover -s tests -v  # grade your practice work
```

---

## Logging your practice

Every time you solve a problem, make a note from the template:

- [[Templates/Problem log]] — one note per problem you solve
- [[Templates/Daily study note]] — what you did today

See [[How to use this vault]] for how to insert a template in one shortcut.
