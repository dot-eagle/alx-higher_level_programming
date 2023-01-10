#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)

    for check in new_list:
        if (check % 2 == 0):
            new_list[check] = True
        else:
            new_list[check] = False
    return (new_list)


"""

def divisible_by_2(my_list=[]):
     new_list = [True if check % 2 == 0 else False for check in my_list]
     return new_list

"""
