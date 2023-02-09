#!/usr/bin/python3

"""
Python class MyList that inherits frm list
"""


class MyList(list):
    """ class MyList that inherits frm list """

    '''def __init__(self, list):
        """ def __init__(self, *args, **kwargs):
        Initialize and construct MyList instatnces """
        super(list).__init__(*args, **kwargs)'''

    def print_sorted(self):
        """ prints the list, but in ascending sort order """
        """ super(list).sorted() """
        '''print(sorted(super(list)))
        print(self) '''
        print("{}".format(sorted(self)))

