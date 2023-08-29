#!/usr/bin/python3
"""script for square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """constructor method
        Parameters:
            size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method to calculate square area
        Returns:
            square area
        """
        return self.__size * self.__size
