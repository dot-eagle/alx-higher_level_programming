#!/usr/bin/python3

def weight_average(my_list=[]):
    if (my_list == [] or not my_list):
        return (0)
    valu = 0.0
    scoli = list(t[0] * t[1] for t in my_list)
    scowi = list(t[1] for t in my_list)
    valu = sum(scoli) / sum(scowi)
    return (valu)

