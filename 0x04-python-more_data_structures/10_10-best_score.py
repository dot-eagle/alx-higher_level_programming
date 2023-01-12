#!/usr/bin/python3

def best_score(a_dictionary):

   # best_key = dict(a_dictionary)
    if (a_dictionary == {}):
        return (None)
    else:
        # best_score = max(a_dictionary, key=a_dictionary.get)
        for key, value in dict(a_dictionary):
            return (max(a_dictionary, key = a_dictionary.get()))
        # return (max(a_dictionary.items()))
 

