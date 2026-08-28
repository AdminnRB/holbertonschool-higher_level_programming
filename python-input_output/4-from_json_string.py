#!/usr/bin/python3
"""Module that provides a function to deserialize a JSON string."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.

    Args:
        my_str: The JSON string to deserialize.

    Returns:
        The Python object described by my_str.
    """
    return json.loads(my_str)
