---
tags:
  - concept
---

# Strings

A shelf of letters — everything about [[Concepts/Arrays|arrays]] applies.
Except for one thing.

## Strings are frozen

```python
word = "cat"
word[0] = "b"      # ❌ TypeError - strings are immutable
```

Like a printed book: you can read any page, but to change a word you print a
**whole new book**. Every "change" to a string secretly builds a new one.

## The trap that catches everybody

```python
result = ""
for word in words:
    result += word          # ❌ O(n²) - copies everything, every round

result = "".join(words)     # ✅ O(n)
```

**Never build a string with `+=` inside a loop.** If you remember one thing
about strings, make it this.

## To edit letters: unfreeze, change, refreeze

```python
letters = list(word)     # unfreeze
letters[0] = "j"         # change freely
word = "".join(letters)  # refreeze
```

Read: [[02_Arrays_And_Strings/notes/02_what_is_a_string|The full lesson]]
Related: [[Concepts/Arrays|Arrays]] · [[Concepts/Hashing|Hashing]]

Back to [[00 START HERE]]
