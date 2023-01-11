#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    order_k = list(sorted(a_dictionary.items()))
    for key, item in order_k:
        print("{}: {}".format(key, item))
