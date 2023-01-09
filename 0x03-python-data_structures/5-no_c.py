#!/usr/bin/python3

def no_c(my_string):
    indx = 0
    list_my_string = list(my_string)

    for element in list_my_string:
        if (element == 'C' or element == 'c'):
            list_my_string[indx] = ''
        indx += 1

    return "".join(list_my_string)
