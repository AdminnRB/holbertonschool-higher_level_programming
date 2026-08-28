#!/usr/bin/python3
"""Module that provides a function to serialize an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of a Python object.

    Args:
        my_obj: The object to serialize.

    Returns:
        A string containing the JSON representation of my_obj.
    """
    return json.dumps(my_obj)
