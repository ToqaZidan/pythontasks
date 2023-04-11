#!/usr/bin/python3
"""Define  class checking a function"""


def is_same_class(obj, a_class):
    """Define a function that object is exactly
    an instance of the specified class

    Args:
    obj: An object to be checked
    a_class: class which object will be checked in

    Return: True - if object is instance of class
        False - otherwise
        """

    return obj.__class__ is a_class
