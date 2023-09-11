#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """check if obj is subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
