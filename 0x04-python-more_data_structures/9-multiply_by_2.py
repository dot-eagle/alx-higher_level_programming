#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary)
    for keys in a_dictionary:
        new_dic[keys] *= 2
    return new_dic
