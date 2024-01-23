#!/usr/bin/python3

"""A module that defines a class square"""

class Square:

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private.
        """
        self.__size = size
