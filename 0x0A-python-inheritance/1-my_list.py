#!/usr/bin/python3
"""
class mylist inherits from mylist
"""


class MyList(list):
    """ mylist class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
