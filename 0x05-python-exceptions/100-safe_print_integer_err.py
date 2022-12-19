#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print(f"Exception: Unknown format code 'd' for object of type {type(value)}")
        return False
