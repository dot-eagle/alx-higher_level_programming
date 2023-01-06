#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    if len == 0:
        print("0 argument.")
    elif len == 1:
        print("1 argument:".format(len))
    else:
        print("{} arguments:".format(len))
        for i in range(1, len+1):
            print("{:d}: {:s}".format(i, sys.argv[i]))


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

