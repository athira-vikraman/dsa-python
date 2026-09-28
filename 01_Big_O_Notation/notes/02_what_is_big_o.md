# Lesson 2 — What Big O Actually Means

> **Goal:** be able to say, precisely, what `O(n)` claims — and what it does not.

---

## 2.1 The one-sentence definition

> **Big O describes an upper bound on how fast an algorithm's cost grows
> as the input size grows, ignoring constants and small terms.**

Three ideas are packed in there. Let's unpack each.

### (a) "Cost" — usually time, sometimes space
Big O is just a growth language. We use it for **time complexity** (number of
steps) and for **space complexity** (extra memory used). Same notation, two
different questions.

### (b) "As the input grows" — we only care about large n
Big O is about the *trend as n gets big*. For tiny inputs, everything is fast
and nothing matters. A shopkeeper doesn't optimise for one customer; they plan
for the festival rush.

### (c) "Ignoring constants and small terms"
`3n + 50` and `n` are both `O(n)`. This feels like cheating at first, but it is
the point: a constant like 3 depends on your CPU and language, the shape `n`
does not.

---

## 2.2 The formal definition (don't be scared, read it once)

We say `f(n) = O(g(n))` if there exist positive constants `c` and `n₀` such
that:

```
f(n) ≤ c · g(n)        for all n ≥ n₀
```

In plain English: *past some point (`n₀`), `f` never rises above a scaled-up
copy of `g`.* So `g` is a ceiling on `f`'s growth.

**Worked example:** is `3n + 50 = O(n)`?
Pick `c = 4`. Then we need `3n + 50 ≤ 4n`, i.e. `50 ≤ n`.
So with `c = 4` and `n₀ = 50`, the inequality holds forever after. ✅ Yes.

You will almost never do this algebra in practice. But knowing the ceiling idea
explains the next section, which trips up nearly every beginner.

---

## 2.3 The family: O, Ω, Θ (Big O, Big Omega, Big Theta)

| Symbol | Name | Meaning | Everyday analogy |
|--------|------|---------|------------------|
| `O(g)` | Big O | grows **at most** like g — upper bound | "It'll take *at most* an hour" |
| `Ω(g)` | Big Omega | grows **at least** like g — lower bound | "It'll take *at least* 20 minutes" |
| `Θ(g)` | Big Theta | grows **exactly** like g — both bounds | "It takes *about* 40 minutes" |

Technically, if something is `Θ(n)` it is also `O(n²)` — a true upper bound,
just a useless one. In conversation and in interviews, people say "O" but mean
the **tight** bound `Θ`. So when you answer, always give the tightest honest
bound: say `O(n)`, not `O(n³)`, even though both are "correct".

---

## 2.4 Best / Average / Worst case — a *different* axis

Students constantly mix this up, so read this twice:

- **O, Ω, Θ** are about *bounding a function*.
- **Best / average / worst case** are about *which input you were given*.

They are independent. You can talk about the worst case and still use O, Ω or Θ.

Example — linear search for `target` in a list of `n` items:

```python
def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1
```

| Case | Input | Steps | Complexity |
|------|-------|-------|------------|
| Best | target is the first element | 1 | `O(1)` |
| Average | target is somewhere in the middle | n/2 | `O(n)` |
| Worst | target is last, or missing | n | `O(n)` |

**Default rule: when someone asks "what's the complexity?", answer the worst
case** — unless they say otherwise. Worst case is the promise you can actually
keep to your users.

---

## 2.5 What Big O deliberately hides

Big O is a blunt instrument, on purpose. Things it does *not* tell you:

- **Constants.** An `O(n)` algorithm that reads a file from disk per element is
  far slower than an `O(n log n)` algorithm working in RAM.
- **Small inputs.** Python's `sort()` switches to insertion sort for small
  chunks because `O(n²)` with tiny constants beats `O(n log n)` when n is ~16.
- **Which is faster in seconds.** Big O ranks *growth*, not runtime.

So: use Big O to choose the algorithm, use a benchmark to confirm the choice.
`code/09_growth_experiment.py` in this folder does exactly that — it times real
functions and shows the curve matching the theory.

---

## 2.6 How to pronounce it

- `O(1)` → "oh of one" / "constant time"
- `O(log n)` → "oh of log n" / "logarithmic time"
- `O(n)` → "oh of n" / "linear time"
- `O(n log n)` → "n log n" / "linearithmic time"
- `O(n²)` → "oh of n squared" / "quadratic time"
- `O(2ⁿ)` → "two to the n" / "exponential time"
- `O(n!)` → "n factorial" / "factorial time"

---

## Check yourself

1. Is `O(n)` a statement about seconds or about growth?
2. True or false: `n + 5` is `O(n²)`. Is that a *useful* answer?
3. For binary search: what is the best case, and what is the worst case?
4. Why do we default to the worst case?

Next: [Lesson 3 — The rules for simplifying Big O](03_rules_of_big_o.md)
