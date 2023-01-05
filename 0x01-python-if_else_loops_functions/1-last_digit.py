#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numb = abs(number)
l_digi = numb % 10 if numb >= 0 else (numb * -1) % 10
# l_digit = number % 10
if (l_digi > 5):
    print(f"Last digit of {numb:d} is {l_digi:d} and is greater than 5")
elif (l_digi == 0):
    print(f"Last digit of {numb:d} is {l_digi:d} and is 0")
elif (l_digi < 6 and l_digi != 0):
    print(f"Last digit of {numb:d} is {l_digi:d} and is less than 6 and not 0")
