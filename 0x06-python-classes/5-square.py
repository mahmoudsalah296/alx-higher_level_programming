#!/usr/bin/python3
"""a script for square class that print square of hashes"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """constructor method
        Parameters:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """size getter
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Parameters:
            value (int): size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def area(self):
        """method to calculate square area
        Returns:
            square area
        """
        return self.__size * self.__size

    def my_print(self):
        """print square of hashes"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
