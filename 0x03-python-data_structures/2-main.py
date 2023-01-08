#!/usr/bin/python3

replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5, 6, 7]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)



"""
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx <= len(my_list) - 1 and idx >= 0:
        my_list[idx] = element
        return my_list
"""
