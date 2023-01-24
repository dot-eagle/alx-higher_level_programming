#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    while True:
        try:
            if my_list is None:
                return (0)

            idx = 0

            for ele in range(x):
                print("{}".format(my_list[ele]), end='')
                idx = idx + 1

        except (ValueError, TypeError):
            pass

        finally:
            print()

        return (idx)
