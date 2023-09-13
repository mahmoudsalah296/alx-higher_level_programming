#!/usr/bin/python3
"""append after specific text"""


def append_after(filename="", search_string="", new_string=""):
    """append after specific text method"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
