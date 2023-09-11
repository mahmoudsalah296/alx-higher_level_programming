#!/usr/bin/python3
"""operator overloading"""


class MyInt(int):
    """subclass of int"""
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, obj):
        """equality overloading"""
        return self.value != obj

    def __ne__(self, obj):
        """inequality overloading"""
        return self.value == obj
