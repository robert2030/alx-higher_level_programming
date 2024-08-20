#!/usr/bin/python3
"""
 class Student that defines a student by:
 (based on 10-student.py)
 """


class Student:
    """ defines student"""
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

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
