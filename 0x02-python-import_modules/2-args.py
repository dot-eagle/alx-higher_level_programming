#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    len_Arg = len(argv)
    cout = abs(len_Arg - 1)

    if (len_Arg == 0):
        print("0 argument.")
    elif (len_Arg == 1):
        print("{:d} argument.".format(cout))
    else:
        print("{:d} arguments:".format(cout))
    for n in range(1, len_Arg):
        print("{:d}: {:s}".format(n, argv[n]))
