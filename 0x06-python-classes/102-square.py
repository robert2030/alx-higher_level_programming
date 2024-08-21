#!/usr/bin/python3
"""Define a square object"""


class Square:
    """Object representation"""

    def __init__(self, size=0):
        """ Initialize new public attributes

        Args:
            size(int) : Represents the size of the square
        """

        if isinstance(size, (int)):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ Getter to retrive the size of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter to update the size of the object
        Args:
            value(int): Represent the new value for the object size
        """

        if isinstance(value, (int)):

            if value < 0:
                raise ValueError("size must be >= 0")

            else:
                self.__size = value

        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Computes and return area of the square object
        Return:
            res : the area of the square
        """
        res = self.__size ** 2
        return res

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()