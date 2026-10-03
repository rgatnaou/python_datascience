from typing import Any


def NULL_not_found(object: Any) -> int:
    typeOfParm = type(object)

    if object is None:
        print(f"Nothing: {object} {typeOfParm}")

    elif typeOfParm is float and object != object:
        print(f"Cheese: {object} {typeOfParm}")

    elif typeOfParm is int and object == 0:
        print(f"Zero: {object} {typeOfParm}")

    elif typeOfParm is str and object == "":
        print(f"Empty: {typeOfParm}")

    elif typeOfParm is bool and object is False:
        print(f"Fake: {object} {typeOfParm}")

    else:
        print("Type not Found")
        return 1

    return 0