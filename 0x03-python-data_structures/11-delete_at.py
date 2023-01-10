#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_ = list(my_list)

    if (idx < 0):
        return (my_list)
    elif (idx > (len(list_) - 1)):
        return (my_list)
    else:
        my_list.remove(list_[idx])
    return (list_)


