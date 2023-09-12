#!/usr/bin/python3
"""write from file module"""


def write_file(filename="", text=""):
    """write from file function
    Args:
        filename (file): file to be written to
        text (str): text to be written
    """
    with open(filename, "w") as f:
        return f.write(text)
