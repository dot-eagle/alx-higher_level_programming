#!/usr/bin/python3

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5, 6, 7]
print_reversed_list_integer(my_list)


"""
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
for index in my_list[::-1]:
print("{:d}".format(index))

"""

