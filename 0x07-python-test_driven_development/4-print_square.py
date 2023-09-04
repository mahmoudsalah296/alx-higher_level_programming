#!/usr/bin/python3
"""a module contain function that prints a square of #"""


def print_square(size):
    """
    a function that prints a square with the character #

    parameters:
        size (int): length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
