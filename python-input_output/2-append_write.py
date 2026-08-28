#!/usr/bin/python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file.

    Args:
        filename: The path of the file to append to (created if missing).
        text: The string to append into the file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
