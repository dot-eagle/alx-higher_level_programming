#!/usr/bin/python3

divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1


'''

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [True if index % 2 == 0 else False for index in my_list]
    return new_list

'''

"""

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    if not my_list:
        return (my_list)
    for check in my_list:
        if (check % 2 == 0):
            new_list[check] = True
        else:
            new_list[check] = False
    return (new_list)

"""
