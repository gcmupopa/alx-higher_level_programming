#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keysort = sorted(a_dictionary.keys())

    for key in keysort:
        print(key, ":", a_dictionary[key])
