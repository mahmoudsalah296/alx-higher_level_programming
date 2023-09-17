#!/usr/bin/python3
"""a module for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.type_validator("width", width)
        self.value_validator("width", width)
        self.__width = width
        self.type_validator("height", height)
        self.value_validator("height", height)
        self.__height = height
        self.type_validator("x", x)
        self.value_validator("x", x)
        self.__x = x
        self.type_validator("y", y)
        self.value_validator("y", y)
        self.__y = y

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.type_validator("width", width)
        self.value_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.type_validator("height", height)
        self.value_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.type_validator("x", x)
        self.value_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.type_validator("y", y)
        self.value_validator("y", y)
        self.__y = y

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """desplay the rectangle with #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """str method"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dictionary = {}
        attrs = ["id", "width", "height", "x", "y"]
        for i in range(len(attrs)):
            dictionary[attrs[i]] = getattr(self, attrs[i])
        return dictionary
