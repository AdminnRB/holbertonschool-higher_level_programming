#!/usr/bin/env python3
"""Basic serialization module using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data: A Python dictionary with the data to serialize.
        filename: The output JSON filename. Replaced if it already exists.
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename: The input JSON filename.

    Returns:
        A Python dictionary with the deserialized JSON data.
    """
    with open(filename, "r") as f:
        return json.load(f)
