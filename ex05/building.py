import sys


def getProps():
    props = sys.argv
    assert len(props) < 3, "AssertionError: more than one argument is provided"
    if len(props) == 1:
        print('What is the text to count?')
        text = sys.stdin.readline()
        props.append(text)
    return props[1]


def punchmark(char):
    marks = "!@#$%^&*()_+-={}[]|:;<>,.?/~`"
    return char in marks


def loop(list: str):
    dict = {
        "upper": 0,
        "lower": 0,
        "marks": 0,
        "space": 0,
        "digit": 0,
    }
    for item in list:
        if item.isupper():
            dict["upper"] += 1
        elif item.islower():
            dict["lower"] += 1
        elif item.isnumeric():
            dict["digit"] += 1
        elif item.isspace():
            dict["space"] += 1
        elif punchmark(item):
            dict["marks"] += 1
    return dict


def main():
    try:
        props = getProps()
        dict = loop(props)
        print(f"The text contains {len(props)} characters:")
        print(f"{dict['upper']} upper letters")
        print(f"{dict['lower']} lower letters")
        print(f"{dict['marks']} punctuation mark")
        print(f"{dict['space']} spaces")
        print(f"{dict['digit']} digits")
    except AssertionError as msg:
        print(msg)
    except Exception:
        pass


if __name__ == "__main__":
    main()
