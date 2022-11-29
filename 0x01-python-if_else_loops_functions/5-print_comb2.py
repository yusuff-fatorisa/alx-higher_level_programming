#!/usr/bin/python3
for value in range(10):
    for value1 in range(10):
        if value == 9 and value1 == 9:
            print("{:d}{:d}".format(value, value1), end="\n")
        else:
            print("{:d}{:d}, ".format(value, value1), end="")
