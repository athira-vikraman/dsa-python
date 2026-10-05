# DSA in Python — from beginner to advanced

A self-taught course in data structures and algorithms, built one topic at a
time. Every topic follows the same shape:

```
<topic>/
├── README.md      what to read, in what order
├── notes/         the theory, explained from zero
├── code/          runnable, commented demonstrations
├── exercises/     problems to solve + model solutions
└── tests/         automated checks for your own work
```

Standard library only. Python 3.8+.

---

## Progress

| # | Topic | Status |
|---|-------|--------|
| 01 | [Big O Notation](01_Big_O_Notation/) — complexity analysis | ✅ done |
| 02 | [Arrays & Strings](02_Arrays_And_Strings/) — two pointers, sliding window | ✅ done |
| 03 | Hash maps & sets | ⬜ next |
| 04 | Stacks & queues | ⬜ |
| 05 | Linked lists | ⬜ |
| 06 | Recursion & backtracking | ⬜ |
| 07 | Trees & binary search trees | ⬜ |
| 08 | Heaps & priority queues | ⬜ |
| 09 | Graphs (BFS, DFS, shortest paths) | ⬜ |
| 10 | Sorting & searching in depth | ⬜ |
| 11 | Dynamic programming | ⬜ |

---

## In Obsidian

This folder is also an Obsidian vault. Open it and start at
[[00 START HERE]] — or browse the two indexes:

- [[Problems/_All problems|All 31 problems]] — one note each, with technique,
  complexity and code
- [[Concepts/_All concepts|All 18 concepts]] — the hubs those problems link to

Press `Ctrl + G` for the graph view to see how they connect.

## Start here

```bash
cd 01_Big_O_Notation
cat README.md
python3 run_all.py        # run every demo and the full test suite
```

### See it move first

[`visualizer.html`](visualizer.html) is an interactive page covering both
topics. Open it in a browser (double-click the file, or `python3 -m http.server`
in this folder) and you can:

- drag a slider and watch the six complexity curves pull apart
- **step through 31 classic questions** one frame at a time &mdash; searching,
  **all nine sorts** (bubble, selection, insertion, merge, quick, heap,
  counting, radix, bucket), every two-pointer shape, both sliding windows,
  and the hashing problems they compete with
- search the full index by problem, technique or complexity

Each frame shows the data as numbered boxes, marks where every pointer is,
shades the window, highlights the line of Python currently running, and says
in one sentence what just happened.

Reading the note and then watching the same algorithm run is the fastest way
to make a technique stick.

Big O comes first on purpose: it is the measuring tool. Once you can say
"this is O(n log n) time and O(n) space" about your own code, every later
topic has something to compare against.

---

## How to study this

1. **Read the note.** One lesson per sitting, no skimming.
2. **Run the code.** Every example prints an explained demonstration — change
   a number, re-run it, see what moves.
3. **Do the exercises before reading the solutions.** Reading answers feels
   like learning and isn't.
4. **Run the tests.** They skip what you haven't written yet, so the output
   is a progress report.
5. **Say the complexity out loud** for every function you write, forever.
   That habit is the actual skill.

---

Binary search, fully worked and analysed, lives in
[`01_Big_O_Notation/code/04_logarithmic_time.py`](01_Big_O_Notation/code/04_logarithmic_time.py) —
iterative and recursive versions, with the O(log n) reasoning.
