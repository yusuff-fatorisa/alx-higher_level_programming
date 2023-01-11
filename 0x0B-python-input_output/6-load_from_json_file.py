#!/usr/bin/python3
"""
This module contains a function that creates
an `Object` from a `JSON` file.
"""


import json


def load_from_json_file(filename):
    """
    This function creates an `Object` from a
    JSON file. It takes as a parameter
    'filename'=> The name of the file process,
    and returns the python Object.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
