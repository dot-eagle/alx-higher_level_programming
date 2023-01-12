#!/usr/bin/python3

multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)

print(new_list)
print(my_list)


"""
def mutiply_list_map(my_list=[], number=0):
        return list(map(lambda other_number: other_number * number, my_list))
"""
