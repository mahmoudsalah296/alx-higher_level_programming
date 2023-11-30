#!/usr/bin/python3
"""peack finder"""


def find_peack_helper(array, lower, upper):
    """helper function"""
    mid = (lower + upper) // 2

    if mid == lower or mid == upper:
        return array[mid]

    if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
        return array[mid]
    if array[mid + 1] > array[mid]:
        return find_peack_helper(array, mid, upper)
    else:
        return find_peack_helper(array, lower, mid)


def find_peak(list_of_integers):
    """find the peak in a list"""
    lower = 0
    upper = len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return (
            list_of_integers[0]
            if list_of_integers[0] > list_of_integers[1]
            else list_of_integers[1]
        )
    return find_peack_helper(list_of_integers, lower, upper)
