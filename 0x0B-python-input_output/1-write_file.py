#!/usr/bin/python3
""" Define a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Function that truncate textfile if it was found, creat it if it
    was not found.

    Args:
    filename: file to be written over.
    text: text to be written.

    Return:
    number of characters written.
    """
    with open(filename, "w", encoding="UTF-8") as new_file:
        return new_file.write(text)
