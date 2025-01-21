import sys

try:
    params = sys.argv
    lenght = len(params)
    assert lenght < 3 , "AssertionError: more than one argument is provided"
    if (lenght > 1):
        assert params[1].isdigit() ,"AssertionError: argument is not an integer"
        nb = int(params[1])
        if(nb % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as msg:
    print(msg)