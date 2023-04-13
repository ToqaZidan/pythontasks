#!/usr/bin/python3
"""
Define a function that writes an Object to a text file,
using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation.

    Args:
    my_obj: Object to be written.
    filename: File to be wrriten in.
    """

    with open(filename, "w", encoding="UTF-8") as new_file:
        return json.dump(my_obj, new_file)
