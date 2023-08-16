#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    nudict = {}
    for key, value in a_dictionary.items():
        nudict[key] = value * 2
    return nudict
