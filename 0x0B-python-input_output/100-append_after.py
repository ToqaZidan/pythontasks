#!/usr/bin/python3
"""
Define a function that nserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after
    each line containing specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The string to insert after each line containing
        the `search_string`.

    Returns:
        None

    Raises:
        None
    """
    txt = ""
    with open(filename) as rfile:
        for line in rfile:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "wfile") as wfile:
        wfile.write(txt)
