#!/usr/bin/python3
"""
This module supplies one function, text_indentation().
"""


def text_indentation(text):
    """
    Print a text with two new lines after each of these characters: ., ? and :.

    Args:
        text (str): the text to print.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for c in range(len(text)):
        line += text[c]
        if text[c] in ".?:":
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end='')
