#!/usr/bin/python3
"""peack finder"""


def find_peak(list_of_integers):
    """find the peak in a list"""
    if list_of_integers is None or list_of_integers == []:
        return None
    lower = 0
    upper = len(list_of_integers)
    mid = ((upper - lower) // 2) + lower
    mid = int(mid)
    if upper == 1:
        return list_of_integers[0]
    if upper == 2:
        return max(list_of_integers)
    if (
        list_of_integers[mid] >= list_of_integers[mid - 1]
        and list_of_integers[mid] >= list_of_integers[mid + 1]
    ):
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
