#!/usr/bin/python3
"""Module that provides a function to load an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a file containing a JSON representation.

    Args:
        filename: The path of the JSON file to read.

    Returns:
        The Python object described by the file's content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
