#!/usr/bin/python3
"""append to file module"""


def append_write(filename="", text=""):
    """append to file function
    Args:
        filename (file): file to be appended to
        text (str): text to be appended
    """
    with open(filename, "a") as f:
        return f.write(text)
