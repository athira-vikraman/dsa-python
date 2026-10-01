# Lesson 2 — Strings Are Shelves That Can't Change

---

## 1. A string is a shelf of letters

A **string** is just a shelf — but every box holds one letter.

```python
word = "PYTHON"
```

```
index:    0    1    2    3    4    5
        ┌────┬────┬────┬────┬────┬────┐
        │ P  │ Y  │ T  │ H  │ O  │ N  │
        └────┴────┴────┴────┴────┴────┘
```

Everything you learned about arrays works here:

```python
word[0]       # 'P'
word[-1]      # 'N'
word[1:4]     # 'YTH'
len(word)     # 6
for letter in word:
    print(letter)
```

So strings are easy. **Except for one big thing.**

---

## 2. The one big difference: strings are frozen

A list is a shelf with **loose** boxes. You can take a toy out and put a
different one in.

A string is a shelf where everything is **glued down**. You cannot change it.

```python
items = [1, 2, 3]
items[0] = 99          # ✅ works fine - lists are changeable

word = "cat"
word[0] = "b"          # ❌ TypeError! strings cannot be changed
```

The posh word for "frozen" is **immutable**. It just means *cannot be
changed after it is made*.

> 🧠 **Think of it like a printed book.** You can read any page. You cannot
> rub out a word and write a new one. To change anything, you must print a
> **whole new book**.

---

## 3. So how do we "change" a string?

You don't. You **make a new one**.

```python
word = "cat"
new_word = "b" + word[1:]      # "b" + "at" = "bat"
print(word)        # "cat"  <- the old one is untouched
print(new_word)    # "bat"  <- a brand new string
```

Every "change" to a string is secretly **building a new string**. This is the
single most important thing to know about strings, because of the next part.

---

## 4. The trap that catches everybody

You want to join a list of words into a sentence. You write this:

```python
words = ["I", "love", "python"]

sentence = ""
for word in words:
    sentence = sentence + word + " "    # ❌ SLOW
```

Looks innocent. Here's what actually happens:

```
Round 1: make a new string "I "                  (copy 2 letters)
Round 2: make a new string "I love "             (copy 7 letters)
Round 3: make a new string "I love python "      (copy 14 letters)
```

Every round **copies the whole sentence so far**. With 1000 words, you copy
the growing sentence 1000 times. That is **O(n²)** — the slow one.

**The fix** — `join()` builds the new string once:

```python
sentence = " ".join(words)       # ✅ FAST - O(n)
```

Read `" ".join(words)` as: *"glue these words together, putting a space
between each"*.

> **Rule for life: never build a string with `+=` inside a loop. Use
> `join()`.** If you remember one thing from this lesson, make it this.

---

## 5. If you really need to change letters, use a list

Strings are frozen, but lists are not. So: **unfreeze → change → refreeze**.

```python
word = "hello"

letters = list(word)          # unfreeze: ['h','e','l','l','o']
letters[0] = "j"              # change it freely
word = "".join(letters)       # refreeze: "jello"
```

This three-step dance (`list()` → change → `"".join()`) is the standard way
to edit a string. Use it whenever you need to swap, sort or replace letters.

---

## 6. Handy string tools

```python
s = "  Hello World  "

s.strip()            # "Hello World"   removes spaces at both ends
s.lower()            # "  hello world  "
s.upper()            # "  HELLO WORLD  "
s.split()            # ['Hello', 'World']   cuts at the spaces
"a,b,c".split(",")   # ['a', 'b', 'c']      cuts at the commas
"-".join(["a","b"])  # "a-b"
s.replace("l", "L")  # swaps every l
"cat" in "concat"    # True   is it hiding inside?
s.find("World")      # 8      where does it start? (-1 if not there)
"abc".isalpha()      # True   letters only?
"123".isdigit()      # True   digits only?
```

Each of these walks through the whole string, so each is **O(n)**.
And each one **returns a new string** — the original never changes:

```python
s = "hello"
s.upper()        # gives back "HELLO"
print(s)         # still "hello"!  <- you must SAVE the result
s = s.upper()    # ✅ this is how you keep it
```

---

## 7. Price list for strings

| What you do | Price | Note |
|---|---|---|
| `word[3]` | **O(1)** | instant, like an array |
| `len(word)` | **O(1)** | instant |
| `word[1:5]` | O(size of piece) | makes a copy |
| `for c in word` | O(n) | fair |
| `"a" in word` | O(n) | searches |
| `word.lower()` | O(n) | new string |
| `word1 + word2` | O(n + m) | new string |
| `word += x` **in a loop** | **O(n²)** | ❌ the trap |
| `"".join(list)` | **O(n)** | ✅ the fix |

---

## 8. Remember this

```
A string is a shelf of letters, numbered from 0.
Reading is easy. Changing is IMPOSSIBLE - you make a new one instead.

Need to edit letters?   list(word) -> change -> "".join(letters)
Need to build a string? collect in a LIST, then "".join(list)
NEVER do:               result += piece   inside a loop
```

---

## Your turn

```python
word = "PROGRAM"
```

1. What is `word[0]`?
2. What is `word[-1]`?
3. What is `word[0:3]`?
4. What happens if you run `word[0] = "X"`?
5. How do you make `word` into `"XROGRAM"`?
6. What's wrong with this?
   ```python
   out = ""
   for c in word:
       out += c.lower()
   ```

### Answers

1. `'P'`
2. `'M'`
3. `'PRO'` — boxes 0, 1, 2. Stops before 3.
4. `TypeError`. Strings are frozen (immutable). You cannot change a letter
   in place.
5. Either make a new string by joining pieces — `"X" + word[1:]` — or do the
   unfreeze dance:
   ```python
   letters = list(word)
   letters[0] = "X"
   word = "".join(letters)
   ```
6. `out += c` inside a loop builds a new string every round → **O(n²)**.
   Fix it by collecting into a list and joining once:
   ```python
   out = "".join(c.lower() for c in word)
   ```
   (Or just `word.lower()`, which is O(n) and already written in C!)

Next: [Lesson 3 — The two pointers trick](03_two_pointers.md)
