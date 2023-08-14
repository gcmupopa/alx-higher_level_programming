#!/usr/bin/python3

def multiple_returns(sentence):
    lenth = len(sentence)
    f_char = None

    if lenth > 0:
        f_char = sentence[0]
    return lenth, f_char
