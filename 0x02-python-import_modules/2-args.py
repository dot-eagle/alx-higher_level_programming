#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

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



