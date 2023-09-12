#!/usr/bin/python3
"""read from file module"""


def read_file(filename=""):
    """read from file function
    Args:
        filename (file): file to be read
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
