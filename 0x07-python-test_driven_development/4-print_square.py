#!/usr/bin/python3
"""test"""


def print_square(size):
    """test"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("x" * size)
