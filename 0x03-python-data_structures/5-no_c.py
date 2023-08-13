#!/usr/bin/python3

def no_c(my_string):
    nu_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            nu_string += char
    return nu_string
