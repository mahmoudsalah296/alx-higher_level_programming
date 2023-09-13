#!/usr/bin/python3
"""Module for pascal_triangle method."""


def pascal_triangle(n):
    """pascal triangle method"""

    init_list = [[1]]
    if n == 0:
        return []
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(init_list[i - 1][j - 1] + init_list[i - 1][j])
        row.append(1)
        init_list.append(row)
    return init_list
