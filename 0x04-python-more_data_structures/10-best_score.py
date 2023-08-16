#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    maxk = None
    maxv = float('-inf')

    for key, value in a_dictionary.items():
        if value > maxv:
            maxk = key
            maxv = value

    return maxk
