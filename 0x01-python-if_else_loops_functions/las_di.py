#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
#num = int(input("enter the number:"))
ldigit = num%10
print("last digit: {}".format(ldigit))
