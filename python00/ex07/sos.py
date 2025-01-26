import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def takeProps():
    props = sys.argv
    assert len(props) == 2, "AssertionError: the arguments are bad"
    return props[1]


def main():
    try:
        props = takeProps()
        msg = ""
        space = False
        for char in props:
            assert char.isalpha(), "AssertionError: the arguments are bad"
            if (space):
                msg += " " + NESTED_MORSE[char.upper()]
            else:
                msg += NESTED_MORSE[char.upper()]
                space = True
        print(msg)

    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
