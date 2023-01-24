#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    idx = 0

    while True:
        try:
            if my_list is None:
                return (0)

            else:
                for ele in range(x):
                    print("{:d}".format(my_list[ele]), end='')
                    idx = idx + 1

        except (ValueError, TypeError):
            idx = idx + 1

        finally:
            print()

        return (idx)
