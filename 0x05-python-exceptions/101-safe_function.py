#!usr/bin/python3
def safe_function(fct, *args):
    import sys

    a, b = args
    try:
        return fct(a, b)
    except Exception as e:
        print("Exception: {}".format(e.args[0]), file=sys.stderr)
        return None
