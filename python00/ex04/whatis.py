import sys


def is_valid_int(s):
    """Check if s is a valid string representation of an int."""
    if s.startswith("-") or s.startswith("+"):
        s = s[1:]
    return s.isdigit() and s != ""

try:
    params = sys.argv
    lenght = len(params)

    assert lenght < 3, "more than one argument is provided"
    if lenght == 1:
        exit()
    is_valid = is_valid_int(params[1])
    assert is_valid, "argument is not an integer"
    nb = int(params[1])
    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")