#!/usr/bin/python3
"""
devide matrix module
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.
    Parameters:
        matrix (list): the matrix which element will be divided
        div (int) or (float): number that will be divided on
    Returns:
        new matrix of divided elements
    """
    if not matrix or not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    new_matrix = []
    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        length = len(matrix[0])
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in (float, int):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            if type(div) not in (int, float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
