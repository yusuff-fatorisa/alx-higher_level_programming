#!/usr/bin/python3
"""
This module contains a class 'Base'

Attributes ===>
        __nb_objects

Methods ===>
        __init__
"""


class Base(object):
    """
    This class creates an instance of a Base Class.
    It has private attributes called __nb_objects, and
    the __init__ method for its initialization.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the 'JSON' string representation
        of a list of dictionaries
        """
        import json
        if len(list_dictionaries) < 1:
            return json.dumps("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, lists_objs):
        """ Writes the JSON string representation of 'lists_objs' to a file"""
        files = []
        if lists_objs is not None:
            for elem in lists_objs:
                files.append(cls.to_dictionary(elem))
        my_file = cls.__name__ + ".json"
        with open(my_file, "w") as f:
            f.write(cls.to_json_string(files))
