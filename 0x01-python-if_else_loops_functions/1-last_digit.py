#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# b numb = abs(number)
if number > 0:
    l_d = number % 10 # if number >= 0 else (number * -1) % 10
elif number < 0:
    l_d = (10 - number % 10) * -1
elif (number == 0):
    l_d = 0
    # if (number == 0):
  #  l_d = 0
if (number < 0):
    print(f"Last digit of {number:d} is {l_d:d} and is less than 6 and not 0")
elif (number % 10 < 6):
    print(f"Last digit of {number:d} is {l_d:d} and is less than 6 and not 0")
elif (number % 10 == 0):
    print(f"Last digit of {number:d} is {l_d:d} and is 0")
else:
    print(f"Last digit of {number:d} is {l_d:d} and is greater than 5")

# l_digi = numb % 10 if numb >= 0 else ((10 - numb % 10) * -1)
# l_digit = number % 10
# if (l_digi > 5):
  #  print(f"Last digit of {numb:d} is {l_digi:d} and is greater than 5")
# elif (l_digi == 0):
  #  print(f"Last digit of {numb:d} is {l_digi:d} and is 0")
# elif (l_digi < 6 and l_digi != 0):
  # print(f"Last digit of{numb:d} is{l_digi:d} and is less than 6 and not 0")
