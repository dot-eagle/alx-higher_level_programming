#!/usr/bin/python3
import random
numb = random.randint(-10000, 10000)
# b numb = abs(number)
l_digit = numb % 10
l_dig = (10 - numb % 10) * -1
if (numb < 0):
    print(f"Last digit of {numb:d} is {l_dig:d} and is less than 6 and not 0")
elif (numb % 10 < 6):
    print(f"Last digit of {numb:d} is {l_digit:d} and is less than 6 and not 0")
elif (numb % 10 == 0):
    print(f"Last digit of {numb:d} is {l_digit:d} and is 0")
else:
    print(f"Last digit of {numb:d} is {l_digit:d} and is greater than 5")

# l_digi = numb % 10 if numb >= 0 else ((10 - numb % 10) * -1)
# l_digit = number % 10
# if (l_digi > 5):
  #  print(f"Last digit of {numb:d} is {l_digi:d} and is greater than 5")
# elif (l_digi == 0):
  #  print(f"Last digit of {numb:d} is {l_digi:d} and is 0")
# elif (l_digi < 6 and l_digi != 0):
  #  print(f"Last digit of {numb:d} is {l_digi:d} and is less than 6 and not 0")
