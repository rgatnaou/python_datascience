import sys

def is_valid_int(s):
    """Check if s is a valid string representation of an int."""
    if s.startswith("-") or s.startswith("+"):
        s = s[1:]
    return s.isdigit() and s != ""


def takeProps():
    """Read exactly two arguments: a string and an integer."""
    props = sys.argv
    error_message = "the arguments are bad"
    assert len(props) == 3 and is_valid_int(props[2]), error_message
    return props[1:]


def ft_filter(fun, it):
    """Return items of it for which fun(item) is true."""
    return [x for x in it if fun(x)]


def compare(words, nb):
    """Return words whose length is greater than nb."""
    return ft_filter(lambda word: len(word) > nb, words)


def main():
    """Entry point: parse args and print filtered words."""
    try:
        props = takeProps()
        words = props[0].split(" ")
        nb = int(props[1])
        print(compare(words, nb))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()