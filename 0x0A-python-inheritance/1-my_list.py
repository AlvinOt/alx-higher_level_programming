#!/usr/bin/python3
""" this module inherit from list class"""


class MyList(list):
    """this class inherits from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
