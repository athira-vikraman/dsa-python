---
tags:
  - dashboard
---

# How to use this vault

You have never used Obsidian before, so here is only what you actually need.
Five minutes, and you can ignore everything else the app offers.

---

## 1. What Obsidian even is

Obsidian is a **reader and editor for a folder of text files**. That is all.

- A **vault** = a folder on your laptop. This one is `17_DSA`.
- A **note** = a `.md` (Markdown) file inside it.
- Nothing is uploaded anywhere. Your notes are plain files you already own.

If you deleted Obsidian tomorrow, every file here would still open in any
text editor. That is the whole appeal — no lock-in.

---

## 2. The four things you will use every day

### Open any note instantly — `Ctrl + O`
Start typing a name (`sliding`, `cheat`, `two point`) and press Enter.
Faster than clicking through folders. This is the shortcut to learn first.

### Search inside every note — `Ctrl + Shift + F`
Type `amortized` or `O(n log n)` and see every note that mentions it, with
the surrounding line. Brilliant for "where did I read about that?"

### Go back — `Ctrl + Alt + ←`
Like a browser's back button. Use it after following a link.

### Command palette — `Ctrl + P`
Type what you want ("graph", "template", "theme") instead of hunting menus.

---

## 3. Links between notes

In the notes you will see `[[like this]]`. That is a **wikilink** — click it
to jump to that note.

Two things make links powerful:

**Backlinks.** Open any note and look at the right-hand panel: it lists every
other note that links *to* this one. Open the Big O cheat sheet and you can
see which lessons point at it.

**The graph** (`Ctrl + P` → "Open graph view"). A map of your notes as dots
joined by lines. In this vault the dots are coloured by folder, so topic 01
and topic 02 show up as two clusters. It is genuinely useful for spotting
which lesson connects to which.

---

## 4. Checkboxes — your progress tracker

In Markdown, this is a checkbox:

```markdown
- [ ] not done yet
- [x] done
```

In reading mode you can **click the box** to tick it. That is how
[[Progress tracker]] works — click boxes as you finish lessons.

---

## 5. Reading mode vs editing mode — `Ctrl + E`

Every note has two views:

- **Reading mode** — tables, checkboxes and headings rendered nicely. This
  vault opens in reading mode by default, which is what you want for study.
- **Editing mode** — the raw Markdown, for when you want to write.

`Ctrl + E` flips between them.

---

## 6. Tags

A word starting with `#` becomes a tag, like `#revise` or `#stuck`.

The most useful habit: when something does not click, type `#stuck` next to
it. Later, click the tag (or open the Tags panel on the right) to get a list
of everything you found hard. That is your revision list, built for free.

Some tags already used here: `#dashboard`, `#bigo`, `#arrays`.

---

## 7. Templates — stop writing the same note twice

A template is a note you reuse. This vault has two in the `Templates` folder.

To use one: `Ctrl + P` → type `Insert template` → pick it.

- [[Templates/Problem log]] — for each practice problem you solve. It asks
  you the right questions: what technique, what complexity, what tripped you
  up.
- [[Templates/Daily study note]] — what you studied today, what to do next.

Writing the problem log is not busywork. Explaining why you picked a
technique is the thing that makes it stick.

---

## 8. Daily notes

`Ctrl + P` → "Open today's daily note" makes a note named with today's date
in the `Study log` folder, using the daily template. One per study session.

After a month you can scroll your `Study log` folder and see exactly what you
covered and where you got stuck.

---

## 9. What Obsidian will NOT do here

- **It cannot run your Python.** Use a terminal for that. The `.py` files
  appear in the file list but open as plain text.
- **It cannot open `visualizer.html`.** Double-click that file in your file
  manager instead and it opens in your browser.
- It does not change your files in any way you did not ask for. Everything
  in this folder is the same as it was on GitHub.

---

## 10. One habit worth forming

At the end of each study session:

1. Tick what you finished in [[Progress tracker]].
2. Make a daily note and write two lines: what clicked, what did not.
3. Tag anything confusing with `#stuck`.

Next session, start by clicking `#stuck` and clearing one item. That loop is
worth more than any app feature.

---

Back to [[00 START HERE]]
