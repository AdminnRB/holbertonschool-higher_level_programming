#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers for Pascal's triangle of n.

    Args:
        n: The number of rows to generate.

    Returns:
        The triangle as a list of rows, or an empty list when n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        prev = triangle[-1]
        row = [1]
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
