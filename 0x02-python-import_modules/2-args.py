#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    # lenOfArg = len(argv)
    cout = len(argv) - 1

    if (cout == 0):
        print("0 argument.")
    elif (cout == 1):
        print("1 argument.")
    else:
        print("{:d} arguments:".format(cout))
    for n in range(1, cout+1):
        print("{:d}: {:s}".format(n, argv[n]))
