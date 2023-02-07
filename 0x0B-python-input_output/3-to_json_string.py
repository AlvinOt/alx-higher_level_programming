#!/usr/bin/python3
"""this module defines string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Return json representation of string object"""
    return json.dumps(my_obj)
