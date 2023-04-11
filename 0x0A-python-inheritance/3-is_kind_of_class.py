#!/usr/bin/python3
"""Define  class checking a function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance of the specified class or
    an instance of a subclass of the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True - if obj is an instance of a_class or a subclass of a_class,
        otherwise - False.
    """
    return isinstance(obj, a_class)
