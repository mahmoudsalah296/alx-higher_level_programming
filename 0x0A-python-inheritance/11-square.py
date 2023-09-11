#!/usr/bin/python3
"""square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """init method"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""
        return self.__size ** 2

    def __str__(self):
        """__str__ method"""
        return f"[Square] {self.__size}/{self.__size}"
