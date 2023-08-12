#!/usr/bin/python3

if __name__ == "__main__":
    a = 1
    b = 2

    modu = __import__('add_0')
    add = modu.add

    summ = add(a, b)
    print("{} + {} = {}\n".format(a, b, summ))
