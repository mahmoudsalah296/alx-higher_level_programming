#!/usr/bin/python3
"""base geometry"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
