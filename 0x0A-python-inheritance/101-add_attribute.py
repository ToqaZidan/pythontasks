#!/usr/bin/python3
"""Define a function that adds a new attribute to an object"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add the attribute to.
        attr (str): The name of the attribute to add.
        value (any): The value of the attribute to add.

    Raises:
        TypeError: If the object cannot have new attributes.

    Example:
        x = dict()
        add_attribute(x, 'foo', 'bar')
        print(x.foo)  # 'bar'
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
