#!/usr/bin/python3
"""
This module contains a function
which prints the exact text as
'My name is <first_name> <last_name>'
The full information about the
function(prototype, declaration and definition)
is contained its the function documentation
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints out the exact text =>
    'My name is <first_name> <last_name>'
    It takes 1 or 2 parameters,
    first_name => which must be a string
    last_name => which can be a default empty string
    or the specified string parameter
    It prints out the name and returns
    'None' as output
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
