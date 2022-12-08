#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        weight_list = list(map(lambda x: x[0] * x[-1], my_list))
        weight_divisor = list(map(lambda x: x[-1], my_list))
        return sum(weight_list) / sum(weight_divisor)
