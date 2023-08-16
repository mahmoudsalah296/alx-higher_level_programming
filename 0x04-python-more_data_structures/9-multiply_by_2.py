#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    for i in a_dictionary:
        newDict[i] = a_dictionary[i] * 2
    return newDict
