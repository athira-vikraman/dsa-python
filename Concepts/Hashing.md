---
tags:
  - technique
---

# Hashing

Sets and dictionaries answer **"have I seen this before?"** in O(1), instead
of the O(n) it costs to scan a list.

```python
x in my_list    # O(n)  - walks the whole list
x in my_set     # O(1)  - hashes straight to the answer
```

## The one-line optimisation you will use forever

Testing membership inside a loop? Build a set first. **O(n²) becomes O(n).**

```python
# slow: O(n × m)
common = [x for x in list_a if x in list_b]

# fast: O(n + m)
set_b = set(list_b)
common = [x for x in list_a if x in set_b]
```

## The trade

You **buy time with space**. The set costs O(n) memory. Usually a bargain —
but say it out loud, because on data bigger than memory the slow version is
the one that actually runs.

## Set or dict?

A set answers *is it there?*. A dict also answers *how many?* — which you need
the moment something leaves a window.

Read: [[01_Big_O_Notation/notes/07_python_operation_costs|What every Python operation costs]]
Related: [[Concepts/Sliding window|Sliding window]] · [[Concepts/Quadratic time|Quadratic time]]

Back to [[00 START HERE]]
