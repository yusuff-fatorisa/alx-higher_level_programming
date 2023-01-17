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
