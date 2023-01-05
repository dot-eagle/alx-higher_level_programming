#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercase, not followed by a new line.
"""
for alph in range(97, 123):
    print("{:c}".format(alph), end=" ")
  #  print("{}".format(chr(letter)), end="")
  #  print(f"{alph:c}", end=" ")
