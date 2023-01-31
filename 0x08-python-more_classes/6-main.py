#!/usr/bin/python3

Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(4, 6)
my_rectangle_2 = Rectangle(4, 6)
my_rectangle_3 = Rectangle(4, 6)
my_rectangle_4 = Rectangle(4, 6)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

del my_rectangle_3
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

del my_rectangle_4
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
