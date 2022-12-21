#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        return fct(*args)
    except(TypeError, ZeroDivisionError, ValueError, IndexError) as e:
        print("Exception: {}".format(e.args[0]), file=sys.stderr)
        return None
