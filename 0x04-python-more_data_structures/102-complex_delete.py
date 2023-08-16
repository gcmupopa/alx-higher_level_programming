#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key2del = []
    for key, val in a_dictionary.items():
        if val == value:
            key2del.append(key)

    for key in key2del:
        del a_dictionary[key]

    return a_dictionary
