#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    r_list = []
    try:
        for i in range(list_length):
            try:
                elem1 = my_list_1[i]
                elem2 = my_list_2[i]
                if isinstance(elem1, (int, float)) and isinstance(elem2, (int, float)):
                    try:
                        res = elem1 / elem2
                        r_list.append(res)
                    except ZeroDivisionError:
                        print("division by 0")
                        r_list.append(0)
                else:
                    print("wrong type")
                    r_list.append(0)
            except IndexError:
                print("out of range")
                r_list.append(0)
    finally:
            return r_list
