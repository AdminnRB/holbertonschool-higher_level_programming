#!/usr/bin/env python3
"""Serialize and deserialize a custom class with the pickle module."""
import pickle


class CustomObject:
    """A simple custom object that can pickle and unpickle itself."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this instance to filename using pickle.

        Returns None on failure.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject from filename.

        Returns None if the file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
