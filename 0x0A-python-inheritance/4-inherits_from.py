#!/usr/bin/python3
"""Define a checking inheritance function"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    :param obj: The object to be  checked.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class,
        otherwise False.
    """

        base_classes = obj.__class__.__bases__

    if a_class in base_classes:
        return True

    for base_class in base_classes:
        if inherits_from(base_class, a_class):
            return True

    return False
