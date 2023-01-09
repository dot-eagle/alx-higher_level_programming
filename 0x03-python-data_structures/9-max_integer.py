#!/usr/bin/python3

def max_integer(my_list=[]):
    if (my_list == [] or len(my_list) == 0):
        return (None)
    else:
        maxi_val = None

    for digit in list(my_list):
        if (maxi_val is None or digit > maxi_val):
            maxi_val = digit
    return (maxi_val)


# print('Maximum value:', max_value)
