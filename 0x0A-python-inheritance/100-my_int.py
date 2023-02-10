#!/usr/bin/python3

"""
Python module class MyInt that inherits from int
"""


class MyInt(int):
    """ Function class MyInt that inherits from int """

    def __eq__(self, value):
        """ Magic method ''equals'' """

        not_equals = super().__ne__(value)
        return (not_equals)

    def __ne__(self, value):
        """ Magic method ''not equals'' """

        equals = super().__eq__(value)
        return (equals)
