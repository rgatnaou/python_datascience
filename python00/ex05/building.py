import sys
import string


def get_text():
    """Read the text to analyze from argv or from stdin."""
    args = sys.argv
    assert len(args) < 3, "more than one argument is provided"
    if len(args) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline()
        args.append(text)
    return args[1]


def count_chars(text):
    """Count character categories inside text."""
    counts = {
        "upper": 0,
        "lower": 0,
        "marks": 0,
        "space": 0,
        "digit": 0,
    }
    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char.isdigit():
            counts["digit"] += 1
        elif char.isspace():
            counts["space"] += 1
        elif char in string.punctuation:
            counts["marks"] += 1
    return counts


def main():
    """Entry point: read text, count characters, print results."""
    try:
        text = get_text()
        counts = count_chars(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['marks']} punctuation marks")
        print(f"{counts['space']} spaces")
        print(f"{counts['digit']} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    main()