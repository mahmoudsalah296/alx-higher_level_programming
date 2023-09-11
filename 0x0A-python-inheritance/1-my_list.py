#!/usr/bin/python3
"""module for inheretance"""


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """print list in sorted order"""
        print(sorted(self))
