#!/usr/bin/python3

def best_score(a_dictionary):

    if bool(a_dictionary):
        return max(a_dictionary.items())[0]
    else:
        return None
