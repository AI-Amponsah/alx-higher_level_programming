#!/usr/bin/python3
"""define class"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """
        initialize a square
        argument:
        int(size): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
