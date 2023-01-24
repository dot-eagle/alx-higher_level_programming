#!/usr/bin/python3

try:
    aList = [1,2,3,4]

    print(aList[5])

    print(lista[2])

    print(aList)

    #print(aList[])

    print(aLis[2])

#except(IndexError, NameError):

except IndexError:
    print("Sorry that index doesn't exist")

except:
    print("An unknown error occurred")
