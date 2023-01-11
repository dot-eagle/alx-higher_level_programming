#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = []
    for ele in my_list:
        if ele != search:
            new_list[len(new_list):] = [ele]
        else:
            new_list[len(new_list):] = [replace]
    return (new_list)
