#!/usr/bin/python3
"""test1"""


def append_write(filename="", text=""):
    """test"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
