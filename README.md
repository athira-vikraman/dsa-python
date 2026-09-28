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
| 02 | Arrays & strings (two pointers, sliding window) | ⬜ next |
| 03 | Hash maps & sets | ⬜ |
| 04 | Stacks & queues | ⬜ |
| 05 | Linked lists | ⬜ |
| 06 | Recursion & backtracking | ⬜ |
| 07 | Trees & binary search trees | ⬜ |
| 08 | Heaps & priority queues | ⬜ |
| 09 | Graphs (BFS, DFS, shortest paths) | ⬜ |
| 10 | Sorting & searching in depth | ⬜ |
| 11 | Dynamic programming | ⬜ |

---

## Start here

```bash
cd 01_Big_O_Notation
cat README.md
python3 run_all.py        # run every demo and the full test suite
```

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

`binary_search.py` in this folder is an early scratch exercise, kept as-is.
The finished version, with the full analysis, lives in
[`01_Big_O_Notation/code/04_logarithmic_time.py`](01_Big_O_Notation/code/04_logarithmic_time.py).
