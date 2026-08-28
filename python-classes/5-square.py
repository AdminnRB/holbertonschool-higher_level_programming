#!/usr/bin/python3
"""Module that defines a Square class able to print itself."""


class Square:
    """Defines a square by its size and can print it with the # character."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size of the square (defaults to 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character, an empty line if size is 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
