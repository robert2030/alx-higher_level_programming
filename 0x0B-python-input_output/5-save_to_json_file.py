#!/usr/bin/python3
"""test"""


import json


def save_to_json_file(my_obj, filename):
    """test2"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
