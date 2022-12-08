#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    output = list(key for key, match in a_dictionary.items() if match == value)
    for item in output:
        del a_dictionary[item]
    return a_dictionary
