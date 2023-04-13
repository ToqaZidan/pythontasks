#!/usr/bin/python3
"""Define function that returns
the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)

    Args:
    my_obj: object to be converted

    Return:
    JSON representation of a string object
    """
    return json.dumps(my_obj)
