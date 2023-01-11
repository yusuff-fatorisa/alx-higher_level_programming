#!/usr/bin/python3
"""
This module contains a Class definition
for a Student Object
"""


class Student(object):
    """
    This is Class Student which defines
    an Object of a Student.
    It has public attributes of
    - first_name
    - last_name
    - age
    """

    def __init__(self, first_name, last_name, age):
        """ defines the initialization of the Student Class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves the dictionary representation of Student object """
        if attrs is None:
            return self.__dict__
        else:
            attr_dic = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    attr_dic[item] = self.__dict__[item]
            return attr_dic
