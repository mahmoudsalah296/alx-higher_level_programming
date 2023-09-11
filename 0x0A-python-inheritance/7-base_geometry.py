#!/usr/bin/python3
"""base geometry"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
