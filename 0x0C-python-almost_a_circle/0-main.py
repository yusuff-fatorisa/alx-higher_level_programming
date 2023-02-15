#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    print(dir(b1))
    print("==============")
    print(b1.__module__)
    print("===================")
    print(b1.__class__.__name__)
    print(dir(b1.__class__))
