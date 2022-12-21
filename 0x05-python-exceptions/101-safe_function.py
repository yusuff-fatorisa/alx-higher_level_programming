#!usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError, ZeroDivisionError, IndexError, TypeError) as e:
        import sys
        print("Exception: {}".format(e.args[0]), file=sys.stderr)
        return None
