#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for the max_integer function."""

    def test_max_at_end(self):
        """Test with a max value at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with a max value at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with a max value in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        """Test with one negative number in the list."""
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)

    def test_all_negative(self):
        """Test with a list of all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Test with no argument passed to the function."""
        self.assertEqual(max_integer(), None)

    def test_all_equal(self):
        """Test with a list where all elements are equal."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.7, -3.4, 0.5]), 2.7)


if __name__ == '__main__':
    unittest.main()
