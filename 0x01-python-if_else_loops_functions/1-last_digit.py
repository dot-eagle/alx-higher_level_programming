#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

sign = 0

if (number < 0):
    number *= -1
    sign = 1
l_d = number % 10

if (sign):
    l_d *= -1
    number *= -1

if (l_d > 5):
    print(f"Last digit of {number:d} is {l_d:d} and is greater than 5")
elif (l_d < 6 and l_d != 0):
    print(f"Last digit of {number:d} is {l_d:d} and is less than 6 and not 0")
elif (l_d == 0):
    print(f"Last digit of {number:d} is {l_d:d} and is 0")
