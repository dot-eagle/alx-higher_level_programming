#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as ag
    sum = 0
    for n in range(1, len(ag)):
        sum += int(ag[n])
        print("{:d}".format(sum))
