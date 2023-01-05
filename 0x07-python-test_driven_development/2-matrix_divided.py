#!/usr/bin/python3
"""
This module contains a function 'matrix_divided(matrix, div)',
that divides all the elements of a matrix.
Detailed info about this function(prototype, declaration and definition)
is contained in the documentation of this function.
"""


def matrix_divided(matrix, div):
    """
    This function divides all the elements of a matrix
    It takes as parameters
    - matrix => which is a array of equal length  arrays
    - div => which is a non-zero integer/float
    It returns an equivalent array of same length and size,
    as the 'matrix' argument.
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list):
        raise TypeError(f"{error}")
    elif all(isinstance(value, list) for value in matrix) is False:
        raise TypeError(f"{error}")
    elif all(len(value) == len(matrix[0]) for value in matrix) is False:
        raise TypeError(f"{error2}")
    new = [isinstance(num, (int, float)) for val in matrix for num in val]
    if all(new) is False:
        raise TypeError(f"{error}")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        a = map(lambda s: list(map(lambda x: round(x / div, 2), s)), matrix)
        return list(a)
