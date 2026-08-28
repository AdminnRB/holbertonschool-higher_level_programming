#!/usr/bin/python3
"""Module that provides a function to read a text file to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its whole content to stdout.

    Args:
        filename: The path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
