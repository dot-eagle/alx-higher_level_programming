#!/usr/bin/python3


try:
    my_file = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was found")
    print(type(ex))
    print(ex.args)
    print(ex)

else:
    print("File :", my_file.read())
    my_file.close()

finally:
    print("Finished working with file")
   # print(ex)
   # print(type(ex))
