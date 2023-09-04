#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class with private attribute"""
    def __init__(self, width=0, height=0):
        """initialization method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter
        Returns:
            recatangle width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter
        Args:
            width (int): recatangle width
        Raises:
            TypeError: if width is not integer
            ValueError: if width is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height getter
        Returns:
            recatangle width
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter
        Args:
            height (int): recatangle width
        Raises:
            TypeError: if height is not integer
            ValueError: if height is less than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
