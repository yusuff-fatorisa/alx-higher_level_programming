#!/usr/bin/python3
def best_score(a_dictionary):
    from functools import reduce
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    else:
        best_value = reduce(
                lambda x, y: x if a_dictionary[x] > a_dictionary[y] else y,
                a_dictionary.keys())
        return best_value
