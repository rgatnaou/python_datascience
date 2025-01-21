def all_thing_is_obj(object: any) -> int:
    typeOfParm = type(object)
    msg = str(typeOfParm)
    msg_type= msg.split('\'')[1].capitalize()
    if (typeOfParm is int):
        print("Type not found")
    elif (typeOfParm is str):
        print(f"{object} is in the kitchen : {typeOfParm}")
    else:
        print(f"{msg_type} : {msg}")
    return 42