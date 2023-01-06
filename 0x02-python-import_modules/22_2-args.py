#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]
    len_arg = len(argv)

    if (len_arg == 0):
        print("0 argument.")
    elif (len_arg == 1):
        print("{:d} argument:".format(len_arg))
    else:
        print("{:d} arguments:".format(len_arg))
        index = 1
        while index <= len_arg:
            print("{:d}: {:s}".format(index, argv[index]))
            index += 1



""" 
   ecount = len(argv)
    argc = ecount - 1

    if (ecount == 1):
        print("0 argument.")
    elif (ecount == 2):
        print("{:d} argument.".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    for n, x in enumerate(argv):
        if (n == 0):
            continue
        print("{:d}: {:s}".format(n, x))

"""

