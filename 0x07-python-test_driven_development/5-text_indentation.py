#!/usr/bin/python3
"""
text indentation module
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Parameters:
        text (string): text to be indented
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while text[i] and text[i] == ' ':
        i += 1
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in ":.?":
            print('\n')
            while i+1 < len(text) and text[i+1] == ' ':
                i += 1
        i += 1
