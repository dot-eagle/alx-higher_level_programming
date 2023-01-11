#!/usr/bin/python3

C = [36.5, 37, 37.5, 38, 39]

F = list(map(lambda x: (float(9)/5)*x + 32, C))

C = list(map(lambda x: (float(5)/9)*(x-32), F))

print(F)

print(C)



