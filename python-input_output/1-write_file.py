#!/usr/bin/python3
"""Module that provides a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file, overwriting any existing content.

    Args:
        filename: The path of the file to write to (created if missing).
        text: The string to write into the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
