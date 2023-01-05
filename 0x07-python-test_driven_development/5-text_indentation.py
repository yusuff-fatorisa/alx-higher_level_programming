#!/usr/bin/python3
"""
This module contains a function 'text_indentation',
that prints a text with 2 new lines after it.
The complete information of the function
(prototype, declaration & definition)
can be found in the function's documentation
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after the ending character. It takes as a parameter
    'text' => which must be a string, or a TypeError is raised,
    then prints out a line of text with the specified character
    at the end. And also removes the trailing and ending whitespaces
    at the ends of the text printed
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        to_find = ["?", ".", ":"]
        char_output = []
        for elem in to_find:
            begin = 0
            try:
                while True:
                    index = text.index(elem, begin)
                    char_output.append(index)
                    begin = index + 1
            except ValueError:
                pass
        indices = sorted(char_output)
        if len(indices) == 0:
            indices += [len(text)]
        if indices[-1] < len(text):
            indices += [len(text)]
        init = 0
        for val in indices:
            if val != len(text):
                print(text[init: val + 1].strip())
                print()
                init = val + 1
            else:
                print(text[init: val + 1].strip(), end="")
