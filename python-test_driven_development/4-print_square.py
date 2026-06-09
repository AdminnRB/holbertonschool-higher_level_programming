#!/usr/bin/python3
"""
This is the "4-print_square" module.
The module supplies one function, print_square(size).
"""


def print_square(size):
    """
    Prints a square with the character # based on the given size.
    size must be an integer and greater than or equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
