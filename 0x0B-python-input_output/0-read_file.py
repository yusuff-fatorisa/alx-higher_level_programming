#!/usr/bin/python3
"""
This module contains a function that
reads a text file (UTF8) and prints
it to the standard output.
"""


def read_file(filename=""):
    """
    This function reads a text file and
    prints it to the standard output.
    It takes as a parameter, a file name,
    which is by default, 'an empty string'.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
