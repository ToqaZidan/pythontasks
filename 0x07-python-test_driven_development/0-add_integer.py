#!/usr/bin/python3
"""Define intger addtion function"""


def add_integer(a, b=98):
    """Return integer addition of a and b.
    Float arguments are casted to intgers before addition is done.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b


if __name__ == "__main__":

    import doctest
    doctest.testmod()
