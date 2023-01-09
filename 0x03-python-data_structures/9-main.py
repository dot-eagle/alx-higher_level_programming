#!/usr/bin/python3

max_integer = __import__('9-max_integer').max_integer

# my_list = []
my_list = [1, 90, 2, 13, 34, 5, -13, 3, -4, 19, 23, -9]
max_value = max_integer(my_list)

print("Max: {}".format(max_value))



'''

#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        a = my_list[0]
        for index in range(0, len(my_list)):
             if my_list[index] > a:
                 a = my_list[index]
        return a
    else:
        return None

'''
