#!/usr/bin/python3
"""
Square module
"""


class Square:
    """class square"""
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    def area(self):
        return self.__size * self.__size
