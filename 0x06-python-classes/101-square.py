#!/usr/bin/python3
"""Define a square object"""


class Square:
    """Object representation"""

    def __init__(self, size=0, position=(0, 0)):
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

        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Computes and return area of the square object
        Return:
            res : the area of the square
        """
        res = self.__size ** 2
        return res

    def my_print(self):
        """ Prints the size of the square object represented by #"""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")