#!/usr/bin/python3
"""
This module contains a function that
returns an object (Pyhton Data Structure)
represented by a JSON string.
"""


def from_json_string(str):
    """
    This function returns an Object
    (Python Data Structure) represented by a JSON
    string. It takes as a parameter
    'my_str'=> which is the text to be converted.
    And return an object represemte by a JSON string.
    """
    import json
    my_file = json.loads(str)
    return my_file
