#!/usr/bin/python3

if __name__ == "__main__":
    a = 1
    b = 2

    modu = __import__('add_0')
    add = modu.add

    print("{} + {} = {}\n".format(a, b, add(a, b)))
