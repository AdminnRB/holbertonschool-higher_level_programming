#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
For example, add_integer(1, 2) will return 3.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers or floats.
    a and b must be integers or floats, otherwise raise a TypeError.
    If they are floats, they are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # inf və NaN kimi xüsusi float dəyərlərini burda tuturuq
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
