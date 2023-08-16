#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None:
        return 0

    tscore = 0
    tweight = 0
    for score, weight in my_list:
        tscore += score * weight
        tweight += weight

    return tscore / tweight
