#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercase except q and e,
not followed by a new linee.
"""
for alph in range(97, 123):
    if chr(alph) == 'e' or chr(alph) == 'q':
        continue
    print("{:c}".format(alph), end="")
