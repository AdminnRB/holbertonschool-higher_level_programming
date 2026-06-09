#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Adds 2 integers or floats (casted to integers before addition).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
