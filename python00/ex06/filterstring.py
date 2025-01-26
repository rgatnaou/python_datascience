import sys
from ft_filter import ft_filter


def takeProps():
    props = sys.argv
    msgError = "AssertionError: the arguments are bad"
    assert len(props) == 3 and props[2].isdigit(), msgError
    return props[1:]


def compare(test, nb):
    return ft_filter(lambda x: len(x) > nb, test)


def main():
    try:
        props = takeProps()
        list = props[0].split(" ")
        nb = int(props[1])
        print(compare(list, nb))
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
