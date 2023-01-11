#!/usr/bin/python3
"""
This module contains a function that appends a string
at the end of a text file and returns the number of
characters added.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file
    (`UTF8`). It takes a parameters
    'filename'=> the file to add the text into
    'text'=> the text content to be appended.
    It returns the number of characters added to the file
    """
    with open(filename, 'a', encoding="utf-8") as file:
        my_file = file.write(text)
        return my_file
