#!/usr/bin/python3
"""module to compute area and perimeter of a rectangle"""


class Rectangle:
    """Rectangle class with private attribute"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialization method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """method returns area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """method returns perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """str method"""
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """repr method"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """del method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Raises:
            TypeError: if rect_1 or rect_2 is not instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
