#!/usr/bin/python3
"""The module is a function for reading textfiles"""


def read_file(filename=""):
    """"prints contents of a utf-8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
