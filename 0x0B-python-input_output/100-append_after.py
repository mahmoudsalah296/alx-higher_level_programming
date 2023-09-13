#!/usr/bin/python3
"""append after specific text"""


def append_after(filename="", search_string="", new_string=""):
    """append after specific text method"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        for line in f:
            if search_string in line:
                f.write(new_string)
