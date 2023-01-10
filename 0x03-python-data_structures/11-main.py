#!/usr/bin/python3

delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5, 6, 7]
idx = 3

new_list = delete_at(my_list, idx)

print(new_list)
print(my_list)



"""
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
"""
