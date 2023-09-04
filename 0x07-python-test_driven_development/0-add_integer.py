#!/usr/bin/python3
"""
add integers module
"""


def add_integer(a, b=98):
    """function to add two integers
    Parameters:
        a (int): first integer
        b (int): second integer
    Returns: sum of two integers"""

    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise OverflowError("a is too large")
    if b + 1 == b:
        raise OverflowError("b is too large")
    return int(a) + int(b)
