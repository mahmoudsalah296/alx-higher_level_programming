#!/usr/bin/python3
"""student class module"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """object to json"""
        if attrs is None:
            return self.__dict__
        if all(isinstance(x, str) for x in attrs):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__
