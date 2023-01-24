#!/usr/bin/python3


class Dog:

    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("spot")

    doug = Dog("doug")

    freg = Dog("freg")

    spot.getNumOfDogs()

    doug.getNumOfDogs()

    freg.getNumOfDogs()


main()
