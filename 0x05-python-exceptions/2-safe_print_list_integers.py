#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    idx = 0

    for ele in my_list:
        try:
            print("{:d}".format(ele), end='')
            idx += 1

            if idx == x:
                break

        except (ValueError, TypeError):
            pass

    print()

    return (idx)
