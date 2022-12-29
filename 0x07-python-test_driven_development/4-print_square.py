#!/usr/bin/python3
"""
This module contains a function 'print_square'
that prints a function to the stdout.
The complete information of the function
(prototype, declaration & definition)
can be found in the function's documentation
"""


def print_square(size):
    """
    This function prints a square with the character '#'.
    It takes as a parameter
    'size' => which is a non-negative integer
    and uses the symbol to represent the square,
    accordingly.
    Then returns 'None'.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        count = 0
        while count < size:
            val = 0
            while val < size:
                print("#", end="")
                val += 1
            print()
            count += 1
