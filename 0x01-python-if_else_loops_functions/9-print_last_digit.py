#!/usr/bin/python3
def print_last_digit(number):
    ldigit = abs(number) % 10
    print(f"{ldigit:d}".format(), end="")
    return (ldigit)
