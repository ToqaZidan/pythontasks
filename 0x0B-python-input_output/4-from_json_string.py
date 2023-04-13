#!/usr/bin/python3
"""Define function that returns
object represented by JSON string"""


import json


def from_json_string(my_str):
    """
    function that returns object represented by JSON string

    Args:
    my_obj: object to be converted

    Return:
    object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
