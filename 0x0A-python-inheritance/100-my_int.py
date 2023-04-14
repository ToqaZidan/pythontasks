#!/usr/bin/python3
"""Define a class MyInt which inherites fron Int """


class MyInt(int):
    """A subclass of `int` that flips
    the behavior of the `==` and `!=` operators.

    Inherits from:
        int: The built-in integer class
    
    Example:
        x = MyInt(1)
        y = MyInt(2)
        print(x == y)  # True
        print(x != y)  # False
    """
    
    def __eq__(self, other):
        """Inverts the behavior of the `==` operator."""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """Inverts the behavior of the `!=` operator."""
        return super().__eq__(other)
