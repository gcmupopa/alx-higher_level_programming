#!/usr/bin/python3
def magic_string():
    counter = len(magic_string.calls)
    magic_string.calls.append(None)
    return "BestSchool" * counter
