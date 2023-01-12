#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
         if a_dictionary[key] == value:
             del a_dictionary[key]
             # a_dictionary = dict({k: v for k, v in a_dictionary.items() if v != value}
    return (a_dictionary)
