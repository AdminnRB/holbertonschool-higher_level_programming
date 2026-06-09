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

    # 1. Matrisin ümumi strukturunun yoxlanılması
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 2. Hər bir elementin siyahı (row) olmasının və içinin düzgünlüyünün yoxlanılması
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)

    # 3. Sətirlərin ölçülərinin bərabərliyinin yoxlanılması
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. 'div' dəyişəninin tipinin və sıfıra bərabərliyinin yoxlanılması
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Yeni matrisin hesablanıb qaytarılması
    return [[round(elem / div, 2) for elem in row] for row in matrix]
