#!/usr/bin/python3
"""test"""


def read_file(filename=""):
    """test2"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
