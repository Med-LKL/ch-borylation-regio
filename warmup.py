"""
WARM-UP: 20 micro-exercises to get the syntax back
==================================================

This is NOT a test. Different rules from the diagnostic:

  - Looking things up is encouraged. docs.python.org, or the W3Schools
    Python reference, whatever gets you unstuck fastest.
  - Stuck for 3 minutes? Look up the answer, type it out yourself,
    move on. The point is contact with the syntax, not recall.
  - Run the file as often as you like:  python warmup.py
    It prints a pass/fail line per exercise and does not stop at the
    first failure.

Each exercise is 1 to 3 lines. If one is taking longer than that,
you are overcomplicating it.

Target: all 20 green in about 30 minutes.
"""

# =====================================================================
# 1 to 4: strings
# =====================================================================


def ex01(name, energy):
    """Return the string:  "ts1 has energy -412.88 kcal/mol"

    Use an f-string. Round the energy to 2 decimal places.
    ex01("ts1", -412.88177) -> "ts1 has energy -412.88 kcal/mol"
    """
    return f"{name} has energy {energy:.2f} kcal/mol" 


def ex02(line):
    """Strip the whitespace off both ends and make it lowercase.

    ex02("  Conformer_03  ") -> "conformer_03"
    """
    return line.strip().lower() 


def ex03(line):
    """Split on whitespace and return the resulting list.

    ex03("conformer_03   -412.88177") -> ["conformer_03", "-412.88177"]
    """
    return line.split()


def ex04(filename):
    """Return the filename without its extension.

    ex04("opt_freq.log") -> "opt_freq"
    Assume exactly one dot. Slicing or a string method, your choice.
    """
    return filename.split(".")[0]


# =====================================================================
# 5 to 9: lists
# =====================================================================


def ex05(values):
    """Return the first and last items as a 2-item list.

    ex05([3, 7, 1, 9]) -> [3, 9]
    """
    return [values[0], values[-1]]


def ex06(values):
    """Return a NEW list with every value doubled. Use a list comprehension.

    ex06([1, 2, 3]) -> [2, 4, 6]
    """
    return [2*x for x in values]


def ex07(values):
    """Return a NEW list with only the negative values. List comprehension.

    ex07([1, -2, 3, -4]) -> [-2, -4]
    """
    return [ num for num in values if num<0]


def ex08(symbols):
    """Return the list sorted alphabetically, without changing the original.

    ex08(["O", "C", "H"]) -> ["C", "H", "O"]
    (There are two ways to sort in Python. You want the one that
    returns a new list rather than sorting in place.)
    """
    return sorted(symbols)


def ex09(values):
    """Return a list of "index: value" strings. Use enumerate.

    ex09(["a", "b"]) -> ["0: a", "1: b"]
    """
    return [f"{i}: {val}" for i, val in enumerate(values)]


# =====================================================================
# 10 to 13: dictionaries
# =====================================================================


def ex10(d, key):
    """Return d[key], or the string "missing" if the key is not there.

    Do not use try/except. There is a dict method for exactly this.
    ex10({"a": 1}, "b") -> "missing"
    """
    return d.get(key, "missing")


def ex11(d):
    """Return a list of "key=value" strings, one per item.

    ex11({"C": 3, "H": 1}) -> ["C=3", "H=1"]
    Iterate over the items, not just the keys.
    """
    return [ f"{element}={num}" for element, num in d.items()]


def ex12(keys, values):
    """Build a dict pairing each key with the value at the same position.

    ex12(["a", "b"], [1, 2]) -> {"a": 1, "b": 2}
    Use zip.
    """
    return dict(zip(keys, values))


def ex13(d):
    """Return the key whose value is largest.

    ex13({"a": 3, "b": 9}) -> "b"
    One line with max() and a key argument, or a loop. Either is fine.
    """
    return max(d, key=d.get)


# =====================================================================
# 14 to 17: control flow and functions
# =====================================================================


def ex14(energy):
    """Classify an energy:
        below -400      -> "low"
        -400 to 0       -> "medium"
        above 0         -> "high"

    ex14(-412.9) -> "low"   ex14(-200.0) -> "medium"   ex14(5.0) -> "high"
    """
    if energy < -400:
    	return "low"
    elif energy <=0:
    	return "medium"
    else:
    	return "high"   


def ex15(values):
    """Sum the values WITHOUT using sum(). Write the loop.

    ex15([1, 2, 3]) -> 6
    """
    total=0
    for x in values:
        total +=x
    return total


def ex16(n, start=1):
    """Return a list of n consecutive integers beginning at `start`.

    ex16(3) -> [1, 2, 3]
    ex16(3, start=10) -> [10, 11, 12]
    Note the default argument: it is already written for you. Use range.
    """
    return list(range(start, start+n))


def ex17(pairs):
    """pairs is a list of (name, energy) tuples.

    Return a list of just the names. Unpack the tuple in the loop
    or comprehension rather than indexing with [0].

    ex17([("ts1", 1.0), ("ts2", 2.0)]) -> ["ts1", "ts2"]
    """
    return [x for x,y in pairs]


# =====================================================================
# 18 to 20: files, errors, sets
# =====================================================================


def ex18(path):
    """Return a list of the file's lines with newlines stripped.

    Use `with open(...)`. Do not call .close() yourself.
    """
    with open (path, "r") as f:
    	return [line.strip() for line in f]
    	
    


def ex19(text):
    """Convert `text` to a float and return it.

    If it cannot be converted, return None instead of crashing.
    ex19("3.5") -> 3.5      ex19("abc") -> None
    Use try/except ValueError.
    """
    try:
    	return float(text)
	
    except ValueError:
    	return None


def ex20(a, b):
    """a and b are lists. Return a SET of the items that appear in both.

    ex20([1, 2, 3], [2, 3, 4]) -> {2, 3}
    """
    return set(a) & set(b)



# =====================================================================
# Checker. Do not edit below this line.
# =====================================================================

def _run_checks():
    import os
    import tempfile

    tmp = os.path.join(tempfile.gettempdir(), "_warmup_sample.txt")
    with open(tmp, "w") as fh:
        fh.write("alpha\nbeta\ngamma\n")

    checks = [
        ("ex01", lambda: ex01("ts1", -412.88177), "ts1 has energy -412.88 kcal/mol"),
        ("ex02", lambda: ex02("  Conformer_03  "), "conformer_03"),
        ("ex03", lambda: ex03("conformer_03   -412.88177"),
         ["conformer_03", "-412.88177"]),
        ("ex04", lambda: ex04("opt_freq.log"), "opt_freq"),
        ("ex05", lambda: ex05([3, 7, 1, 9]), [3, 9]),
        ("ex06", lambda: ex06([1, 2, 3]), [2, 4, 6]),
        ("ex07", lambda: ex07([1, -2, 3, -4]), [-2, -4]),
        ("ex08", lambda: ex08(["O", "C", "H"]), ["C", "H", "O"]),
        ("ex09", lambda: ex09(["a", "b"]), ["0: a", "1: b"]),
        ("ex10", lambda: ex10({"a": 1}, "b"), "missing"),
        ("ex11", lambda: ex11({"C": 3, "H": 1}), ["C=3", "H=1"]),
        ("ex12", lambda: ex12(["a", "b"], [1, 2]), {"a": 1, "b": 2}),
        ("ex13", lambda: ex13({"a": 3, "b": 9}), "b"),
        ("ex14", lambda: [ex14(-412.9), ex14(-200.0), ex14(5.0)],
         ["low", "medium", "high"]),
        ("ex15", lambda: ex15([1, 2, 3]), 6),
        ("ex16", lambda: [ex16(3), ex16(3, start=10)],
         [[1, 2, 3], [10, 11, 12]]),
        ("ex17", lambda: ex17([("ts1", 1.0), ("ts2", 2.0)]), ["ts1", "ts2"]),
        ("ex18", lambda: ex18(tmp), ["alpha", "beta", "gamma"]),
        ("ex19", lambda: [ex19("3.5"), ex19("abc")], [3.5, None]),
        ("ex20", lambda: ex20([1, 2, 3], [2, 3, 4]), {2, 3}),
    ]

    done = 0
    todo = 0
    wrong = 0

    print()
    for name, call, expected in checks:
        try:
            got = call()
        except NotImplementedError:
            print(f"  {name}   .  not attempted")
            todo += 1
            continue
        except Exception as exc:
            print(f"  {name}   X  {type(exc).__name__}: {exc}")
            wrong += 1
            continue

        if got == expected:
            print(f"  {name}   OK")
            done += 1
        else:
            print(f"  {name}   X  got {got!r}, expected {expected!r}")
            wrong += 1

    print()
    print(f"  {done} passing, {wrong} wrong, {todo} not attempted")
    print()

    os.remove(tmp)


if __name__ == "__main__":
    _run_checks()
