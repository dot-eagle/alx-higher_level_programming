#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    new_list = list(my_list)

    if not my_list:
        return (my_list)

    for check in my_list:
        if (check % 2 == 0):
            new_list[check] = True
        else:
            new_list[check] = False
    return (new_list)





