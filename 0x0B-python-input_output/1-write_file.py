#!/usr/bin/python3
"""
This module contains a function that writes
a string to a text file and returns the
number of characters written.
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file
    (UTF8). It takes as parameters
    'filename'=> The file to write to, defualt to empty string
    'text'=> The text to be written, default to empty string
    Returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        my_file = file.write(text)
        return my_file
