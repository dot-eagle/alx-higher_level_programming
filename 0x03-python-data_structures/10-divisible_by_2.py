#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    new_list = [True if (check % 2 == 0) else False for check in my_list]
    return (new_list)
