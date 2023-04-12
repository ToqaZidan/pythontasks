#!/usr/bin/python3
"""
Presrib function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """Return list of attributes"""
    return (dir(obj))
