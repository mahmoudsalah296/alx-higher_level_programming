#!/usr/bin/python3
"""a script for square class that print square of hashes"""


class Square:
    """a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor method
        Parameters:
            size (int): size of the square
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position getter
        Returns:
            position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter
        Parameters:
            value (tuple): position of the square
        """
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
