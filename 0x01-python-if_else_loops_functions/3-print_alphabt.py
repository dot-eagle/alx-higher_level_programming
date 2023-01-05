#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercas except q and ee, 
not followed by a new line.
"""
for alph in range(97, 123):
    if chr(alph) == 'e' or chr(alph) == 'q':
        continue
    print("{:c}".format(alph), end="")
