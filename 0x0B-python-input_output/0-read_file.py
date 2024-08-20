#!/usr/bin/python3
"""
opens and prints a file
"""


def read_file(filename=""):
    """ prints file content"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
