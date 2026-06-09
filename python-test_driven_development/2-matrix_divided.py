#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number (div).
    Returns a new matrix with elements rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # Matrisin ilk sətrinin uzunluğunu əsas götürürük
    if not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        raise TypeError(msg)
    
    row_len = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)) or elem != elem:
                raise TypeError(msg)
            if elem == float('inf') or elem == float('-inf'):
                raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    if div != div or div == float('inf') or div == float('-inf'):
        raise TypeError("div must be a number")

    # Yeni matris yaradırıq və elementləri bölüb yuvarlaqlaşdırırıq
    return [[round(elem / div, 2) for elem in row] for row in matrix]
