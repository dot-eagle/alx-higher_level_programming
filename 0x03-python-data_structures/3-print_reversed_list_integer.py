#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for m in my_list[::-1]:
    # for m in reversed(my_list):
        print("{:d}".format(m))
