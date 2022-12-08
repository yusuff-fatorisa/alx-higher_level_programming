#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(
        lambda small_list: list(map(lambda x: x ** 2, small_list)), matrix))
