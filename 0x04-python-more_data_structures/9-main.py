#!/usr/bin/python3

multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)



"""
def multiply_by_2(my_dict):
        return dict(zip(my_dict.keys(), (i * 2 for i in my_dict.values())))

"""
