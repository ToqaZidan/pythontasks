#!/usr/bin/python3
"""Defines a function that returns the dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
