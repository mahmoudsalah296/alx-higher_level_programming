#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for char in my_string:
        if char not in "cC":
            newstr += char
    return newstr
