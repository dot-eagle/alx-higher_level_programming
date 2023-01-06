#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    num = len(argv)
    n = 1
    if num == 0:
        print("{:d} argument.".format(num))
    elif num == 1:
        print("{:d} argument:".format(num))
        print("{:d}: {:s}".format(n, sys.argv[1]))
    else:
        print("{:d} arguments:".format(num))
        while n <= num:
            print("{:d}: {:s}".format(n, sys.argv[n]))
            n += 1
