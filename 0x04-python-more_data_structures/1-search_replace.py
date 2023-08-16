#!/usr/bin/python3

def search_replace(my_list, search, replace):
    nulist = []
    for element in my_list:
        if element == search:
            nulist.append(replace)
        else:
            nulist.append(element)
    return nulist
