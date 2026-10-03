import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
}


def takeProps():
    """Read exactly one argument from argv."""
    props = sys.argv
    assert len(props) == 2, "the arguments are bad"
    return props[1]


def main():
    try:
        props = takeProps()
        for char in props:
            assert char.isalnum() or char == " ", "the arguments are bad"
        print(" ".join([NESTED_MORSE[char.upper()] for char in props]))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()