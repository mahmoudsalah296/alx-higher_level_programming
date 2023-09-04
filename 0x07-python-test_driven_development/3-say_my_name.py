#!/usr/bin/python3
"""say my full name module"""


def say_my_name(first_name, last_name=""):
    """
    print the full name
    parameters:
        first_name (string): first name
        last_name (string): last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
