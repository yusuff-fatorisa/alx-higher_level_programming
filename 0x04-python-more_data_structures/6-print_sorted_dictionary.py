#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_keys = list(sorted(a_dictionary.keys()))
    for key in dic_keys:
        print("{}: {}".format(key, a_dictionary[key]))
