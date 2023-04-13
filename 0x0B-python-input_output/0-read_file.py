#!/usr/bin/python3
"""Define a function that reads a file"""


def read_file(filename=""):
    """"
    Function that reads a file, file permission or file doesn't exist
    are not maneged, and print a text file to stdout
    """

    with open(filename, "r", encoding="UTF-8") as new_file:
        print(new_file.read(), end="")
