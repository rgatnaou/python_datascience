def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


if __name__ == "__main__":
    # Example usage of ft_filter
    numbers = [0, 1, 2, 3, 4, 5]
    even_numbers = list(ft_filter(lambda x: x % 2 == 0, numbers))
    ft = ft_filter(lambda x: x % 2 == 0, numbers)
    print("next even number:", next(ft))  # Should print 0
    print("next even number:", next(ft))  # Should print 0
    print("next even number:", next(ft))  # Should print 0

    print("Even numbers:", even_numbers)


    # Example with None function
    mixed_values = [0, "", None, "Hello", 42]
    truthy_values = list(ft_filter(None, mixed_values))
    print("Truthy values:", truthy_values)
    print(filter.__doc__ == ft_filter.__doc__)  # Should print True
    print(ft_filter.__doc__)  # Should print the docstring of ft_filter
    print(type(filter(None, mixed_values)))  # Should print <class 'filter'>