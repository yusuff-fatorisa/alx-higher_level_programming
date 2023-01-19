#!/usr/bin/python3
"""
This module contains a class 'Base'

Attributes ===>
        __nb_objects

Methods ===>
        __init__
"""


import json
import csv


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
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of 'lists_objs' to a file"""
        files = []
        if list_objs is not None:
            for elem in list_objs:
                files.append(cls.to_dictionary(elem))
        my_file = cls.__name__ + ".json"
        with open(my_file, "w") as f:
            f.write(cls.to_json_string(files))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON string representation """
        if json_string is None or len(json_string) == 0:
            return json.loads([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns the list of instances """
        my_file = cls.__name__ + ".json"
        my_list = []
        try:
            with open(my_file, "r") as f:
                instances = cls.from_json_string(f.read())
            for m, n in enumerate(instances):
                my_list.append(cls.create(**instances[m]))
        except:
            pass
        return my_list
