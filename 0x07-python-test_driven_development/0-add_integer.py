#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
The name of the function is 'add_integer'
Details about this function,(declaration and definition),
can be found in the function documentation.
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers.
    It receives 1 or 2 integer parameter(s),
    and returns the output as an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
