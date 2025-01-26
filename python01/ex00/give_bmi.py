def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert (type(height) is list), "AssertionError: the 'height' varibale is not a list"
        assert (type(weight) is list), "AssertionError: the 'weight' varibale is not a list"
        len_height = len(height)
        len_weight = len(weight)
        assert (len_height == len_weight), "AssertionError: the lists are not the same size"
        i = 0
        bmi = []
        while(i < len_height):
            assert ((type(height[i]) in [int , float])), "AssertionError:the 'height' varibale is not a list[int | float]"
            assert ((type(weight[i]) in  [int , float])), "AssertionError:the 'weight' varibale is not a list[int | float]"
            assert (height[i] != 0), "AssertionError: cannot divide by zero (height)"
            bmi.append(weight[i] / (height[i] ** 2))
            i += 1
    except AssertionError as msg:
        print(msg)
        return []
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    validation = []
    try:
        assert (type(bmi) is list), "AssertionError: the 'bmi' varibale is not a list"
        assert (type(limit) is int), "AssertionError:  the 'limit' varibale is not an int"
        for item in bmi:
            assert (type(item) in [int , float]), "AssertionError:the 'bmi' varibale is not a list[int | float]"
            validation.append(item > limit)
        return validation
    except AssertionError as msg:
        print(msg)
        return validation
