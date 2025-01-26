import math

def NULL_not_found(object: any) -> int:
    typeOfParm = type(object)
    if (object == None):
        print(f"Nothing: {object} {typeOfParm}")
    elif (typeOfParm is not  str and math.isnan(object) ):
        print(f"Cheese: {object} {typeOfParm}")
    elif (object == 0):
        print(f"Zero: {object} {typeOfParm}")
    elif (object == ""):
        print(f"Empty: {object} {typeOfParm}")
    elif (typeOfParm is bool):
        print(f"Fake: {object} {typeOfParm}")
    else:
        print(f"Type not Found")
        return 1
    return 0
                