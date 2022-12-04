#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) >= len(tuple_b):
        max_len = len(tuple_a)
    else:
        max_len = len(tuple_b)

    sum_list = []

    for value in range(max_len):
        if value < len(tuple_a):
            first = tuple_a[value]
        else:
            first = 0

        if value < len(tuple_b):
            second = tuple_b[value]
        else:
            second = 0

        sum_list.append(first + second)

    return tuple(sum_list)
