#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as val:
        print("Exception: {}".format(val.args[0]))
        return False
