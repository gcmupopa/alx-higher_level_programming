#!/usr/bin/python3

import dis


def magic_calculation(a, b):
    from magic_calculation_102 import (
            magic_calculation_102_add as add,
            magic_calculation_102_sub as sub
            )

    if a < b:
        c = add(a, b)
        for index in range(4, 7):
            c = add(c, index)
    else:
        return sub(a, b)

    return c


bytecode = compile(magic_calculation.__code__, filename='', mode='eval')
dis.dis(bytecode)
