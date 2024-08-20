#!/usr/bin/python3
"""
class Square that inherits from Rectangle (9-rectangle.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ derived class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
