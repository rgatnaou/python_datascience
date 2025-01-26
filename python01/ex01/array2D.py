def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert (type(family) is list), "AssertionError: the 2Dlist varibale is not a list"
        assert (type(family[0]) is list), "AssertionError: the 2Dlist varibale is not a 2DList"
        assert (type(start) is int), "AssertionError: the 'start' varibale is not a int"
        assert (type(end) is int), "AssertionError: the 'end' varibale is not a int"
        rows = len(family)
        columns = len(family[0])
        x = slice(start,end)
        for item in family:
            assert (len(item) == columns), "AssertionError: the columns in the 2Dlist not the same size"
        print(f"My shape is : ({rows}, {columns})\nMy new shape is : ({len(family[x])}, {columns})")
        return family[x]
    except AssertionError as msg:
        print(msg)
        return []


family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))