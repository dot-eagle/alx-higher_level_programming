#!/usr/bin/python3

"""
Node Module: 100-singly_linked_list using Python
This module defines & implements a basic singly linked list
Defines class Node (with private data and next_node)
Defines class SinglyLinkedList (with private head and public sorted_insert)
"""


class Node:
    """ Definition of class Node of singly linked list
    Args:
        data (int): private
        next_node : private; can be None or must be Node object
    Functions:
        __init__(self, data, next_node=None)
        data(self)
        data(self, value) """

    def __init__(self, data, next_node=None):
        """ Initializes and constructs Node object
        Attributes:
            data (int): private Node data
            next_node : private; can be None or must be Node object """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """ Getter
            Raises: TypeError: If data is not an integer.
            Returns: data """
            return self.__data

        @data.setter
        def data(self, value):
            """ Setter
            Args:
                value: sets data to value if int """
            if type(value) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

        @property
        def next_node(self):
            """ Getter
            Raises: TypeError: If data is not an integer.
            Returns: next_node - int data of next Node """
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if type(value) is not int:
                raise TypeError("next_node must be an integer")
            else:
                self.__next_node = value


class SinglyLinkedList:
    """ Definiiontion of class SinglyLinkedList
    Args:
        head: private
        sorted_insert: public
    Functions:
        sorted_insert(self, value)
        __init__(self) """

    def __init__(self):
        """ Initialize singly linked list """
        self.__head = None

    def __str__(self):
        """ String represntation of singlylinked list needed to print """
        string = ""
        tr = self.__head
        while tr.next_node is not None:
            string += str(tr.data)
            tr = tr.next_node
            if tr.next_node is not None:
                string += "\n"
        return (string)

    def sorted_insert(self, value):
        """ inserts a new Node into list in sorted increasing order
        Args: value: int data to insert """
        try:
            new = Node(value)
        except Exception:
            return
        if self.__head is None:
            self.__head = new
        else:
            tr = self.__head
            while value > tr.data and tr.next_node is not None:
                prev = tr
                tr = tr. next_node
            new.next_node = tr
            if tr == self.__head:
                self.__head = new
            else:
                prev.next_node = new

            """ return

        tr = self.__head
        if new.data < tr.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tr.next_node is not None) and (new.data > tr.next_node.data):
            tr = tr.next_node
            new.next_node = tr.next_node
            tr.next_node = new
            return  """
