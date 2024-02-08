#!/usr/bin/python3
"""test"""


import json


def load_from_json_file(filename):
    """test2"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
