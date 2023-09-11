#!/usr/bin/python3
"""rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """init method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """__str__ method"""
        return f"[Rectangle] {self.__width}/{self.__height}"
