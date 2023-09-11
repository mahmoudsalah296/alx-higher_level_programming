#!/usr/bin/python3
"""module for inheretance"""


def is_kind_of_class(obj, a_class):
    """check if obj is instance of a class"""

    if isinstance(obj, a_class):
        return True
    return False
