#!/usr/bin/python3
"""
Define a function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file"""

    with open(filename) as new_file:
        return json.load(new_file)
