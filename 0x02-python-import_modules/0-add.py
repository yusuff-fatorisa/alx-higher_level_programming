#!/usr/bin/python3
if __name__ == "__main__":
    func = __import__("add_0")
    p, q = 1, 2
    add_func = func.add(p, q)
    print("{:d} + {:d} = {:d}".format(p, q, add_func))
