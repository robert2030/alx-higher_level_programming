#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """ student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list) or \
                not all(isinstance(attr, str)for attr in attrs):
            return self.__dict__
        return {attr: getattr(self, attr, None) for attr in attrs
                if hasattr(self, attr)}
