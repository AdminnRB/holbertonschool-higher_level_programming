#!/usr/bin/python3
"""Module defining a Student class with JSON save and reload support."""


class Student:
    """Defines a student by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.

        Args:
            attrs: Optional list of attribute names to keep. When it is a
                list of strings, only those attributes are returned;
                otherwise every attribute is returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return dict(self.__dict__)

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json: A dictionary whose keys are public attribute names and
                whose values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
