#!/usr/bin/python3
"""Module that provides a function to describe an object for JSON."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are all serializable
            (list, dictionary, string, integer or boolean).

    Returns:
        A dictionary holding a copy of the object's instance attributes.
    """
    return dict(obj.__dict__)
