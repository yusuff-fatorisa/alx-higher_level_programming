#!/usr/bin/python3
"""
This module contains a function returns
the JSON representation of n object.
"""


def to_json_string(my_obj):
    """
    This function returns the JSON
    representation of an object. It takes as
    a parameter
    'my_obj'=> which is the object to be serialized.
    It returns the string representation of the object
    """
    import json

    my_str = json.dumps(my_obj)
    return my_str
