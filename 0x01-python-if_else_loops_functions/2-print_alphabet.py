#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercase, not followed by a new line.
"""
for alph in range(97, 123):
    print("{}".format(chr(alph)), end=" ")
  #  print(f"{alph:c}", end=" ")
  #  print("{:c}".format(alph), end=" ")
