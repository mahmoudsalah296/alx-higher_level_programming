#!/usr/bin/python3
"""a script to define square class with private instance attribute"""


class Square:
    """simple square class"""
    def __init__(self, size):
        """
        constructor method

        Parameters:
            size (int): size of the square
        """
        self.__size = size
