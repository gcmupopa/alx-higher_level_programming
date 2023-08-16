#!/usr/bin/python3

def uniq_add(my_list=[]):
    nulist = set(my_list)
    summ = 0
    for element in nulist:
        summ += element

    return summ
