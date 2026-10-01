"""
STRINGS — shelves of letters that CANNOT be changed
===================================================
Goes with notes/02_what_is_a_string.md

Run me:  python3 code/02_string_basics.py
"""

import time


# ----------------------------------------------------------------------
# Reading a string is exactly like reading an array
# ----------------------------------------------------------------------
def get_letter(word, i):
    """Time: O(1)   Space: O(1)"""
    return word[i]


def count_letter(word, letter):
    """Time: O(n)   Space: O(1)"""
    count = 0
    for c in word:
        if c == letter:
            count += 1
    return count


# ----------------------------------------------------------------------
# Strings are FROZEN - you cannot change one, you make a new one
# ----------------------------------------------------------------------
def try_to_change_a_string(word):
    """Shows the error, so you recognise it when it happens to you."""
    try:
        word[0] = "X"
        return "it worked (this should never happen!)"
    except TypeError as error:
        return f"TypeError: {error}"


def change_first_letter(word, new_letter):
    """The right way: build a NEW string out of pieces.

    Time: O(n) - the new string must be copied   Space: O(n)
    """
    return new_letter + word[1:]


def change_letter_the_list_way(word, i, new_letter):
    """The unfreeze dance: list() -> change -> "".join()

    Use this whenever you need to edit several letters.
    Time: O(n)   Space: O(n)
    """
    letters = list(word)          # unfreeze
    letters[i] = new_letter       # change freely
    return "".join(letters)       # refreeze


# ----------------------------------------------------------------------
# THE TRAP: building a string with += inside a loop
# ----------------------------------------------------------------------
def join_words_badly(words):
    """Every round copies the whole sentence so far.

    Time: O(n^2)  <- the trap
    """
    sentence = ""
    for word in words:
        alias = sentence           # a second reference, so Python really copies
        sentence = alias + word + " "
    return sentence.strip()


def join_words_well(words):
    """join() works out the final size, allocates ONCE, copies each letter once.

    Time: O(total length)  <- the fix
    """
    return " ".join(words)


def main():
    print("=" * 66)
    print("  STRINGS - a shelf of letters")
    print("=" * 66)

    word = "PYTHON"
    print(f"\n  Our word: {word!r}")
    print("""
    index:    0    1    2    3    4    5
            +----+----+----+----+----+----+
            | P  | Y  | T  | H  | O  | N  |
            +----+----+----+----+----+----+
""")
    print(f"    word[0]    = {word[0]!r}")
    print(f"    word[-1]   = {word[-1]!r}")
    print(f"    word[1:4]  = {word[1:4]!r}   <- boxes 1,2,3")
    print(f"    len(word)  = {len(word)}")
    print(f"    'T' in word = {'T' in word}")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  THE BIG DIFFERENCE: lists bend, strings are frozen")
    print("=" * 66)

    items = [1, 2, 3]
    items[0] = 99
    print(f"\n    A LIST:   items[0] = 99  ->  {items}   works fine")
    print(f"    A STRING: word[0] = 'X'  ->  {try_to_change_a_string('cat')}")
    print("""
    A list is a shelf with loose boxes - swap a toy any time.
    A string is a shelf glued down - like a printed book.
    To 'change' it, you PRINT A NEW BOOK.""")

    print("\n  So we build new strings instead:")
    print(f"    change_first_letter('cat', 'b')        = {change_first_letter('cat', 'b')!r}")
    print(f"    change_letter_the_list_way('hello',0,'j') = "
          f"{change_letter_the_list_way('hello', 0, 'j')!r}")
    print("\n    The unfreeze dance:  list(word) -> change it -> ''.join(letters)")

    print("\n  And the original is ALWAYS untouched:")
    s = "hello"
    s.upper()
    print(f"    s = 'hello'; s.upper(); print(s)  ->  {s!r}   <- unchanged!")
    print(f"    You must SAVE it:  s = s.upper()  ->  {s.upper()!r}")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  THE TRAP: building a string with += in a loop")
    print("=" * 66)

    words = ["word"] * 20_000
    start = time.perf_counter()
    bad = join_words_badly(words)
    bad_time = time.perf_counter() - start

    start = time.perf_counter()
    good = join_words_well(words)
    good_time = time.perf_counter() - start

    print(f"\n    gluing {len(words):,} words with  += in a loop : {bad_time:.4f}s   O(n^2)")
    print(f"    gluing {len(words):,} words with  ' '.join()   : {good_time:.4f}s   O(n)")
    print(f"    -> join is {bad_time / good_time:,.0f}x faster")
    print(f"    same answer? {bad == good}")
    print("""
    Why is += so slow? Watch what it does:
        round 1: build "I "                 (copy 2 letters)
        round 2: build "I love "            (copy 7 letters)
        round 3: build "I love python "     (copy 14 letters)
    Every round copies the WHOLE sentence again. That is O(n^2).

    RULE FOR LIFE: never build a string with += inside a loop.
                   Collect the pieces in a LIST, then "".join() once.""")

    # ------------------------------------------------------------------
    print("\n" + "=" * 66)
    print("  HANDY STRING TOOLS (every one is O(n), every one makes a NEW string)")
    print("=" * 66)
    s = "  Hello World  "
    print(f"\n    s = {s!r}")
    for label, value in [
        ("s.strip()", s.strip()),
        ("s.lower()", s.lower()),
        ("s.upper()", s.upper()),
        ("s.split()", s.split()),
        ('"a,b,c".split(",")', "a,b,c".split(",")),
        ('"-".join(["a","b","c"])', "-".join(["a", "b", "c"])),
        ("s.replace('l', 'L')", s.replace("l", "L")),
        ("s.strip().find('World')", s.strip().find("World")),
        ('"cat" in "concat"', "cat" in "concat"),
    ]:
        print(f"    {label:<26} -> {value!r}")

    print("\n" + "=" * 66)
    print("""  REMEMBER:

    Reading a string = just like an array.  word[i] is O(1).
    CHANGING a string = impossible. You build a new one.

    Edit letters?    list(word) -> change -> "".join(letters)
    Build a string?  collect in a LIST, then "".join(list)
    NEVER:           result += piece   inside a loop""")
    print("=" * 66)


if __name__ == "__main__":
    main()
